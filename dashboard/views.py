from django.db.models import Sum
from django.db.models.functions import TruncMonth
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from records.models import Record
from accounts.permissions import IsAnalyst
from django.db.models import Q


@api_view(['GET'])
@permission_classes([IsAnalyst])
def dashboard(request):
    records = Record.objects.all()

    # Summary
    total_income = records.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = records.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    # Category Wise
    category_data = records.values('category').annotate(total=Sum('amount'))

    # Recent Activity
    recent = records.order_by('-date')[:5]
    recent_data = [
        {
            "amount": r.amount,
            "type": r.type,
            "category": r.category,
            "date": r.date
        }
        for r in recent
    ]

    # Monthly Trends
    monthly = (
        records
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total_income=Sum('amount', filter=Q(type='income'), default=0))
        .annotate(total_expense=Sum('amount', filter=Q(type='expense'), default=0))
        .order_by('month')
    )

    return Response({
        "summary": {
            "total_income": total_income,
            "total_expense": total_expense,
            "net_balance": total_income - total_expense
        },
        "category_wise": list(category_data),
        "recent_activity": recent_data,
        "monthly_trends": list(monthly)
    })