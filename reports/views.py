from django.shortcuts import render
from rooms.models import Room
from guests.models import Guest
from payments.models import Payment
from django.db.models import Sum, Count


def reports_dashboard(request):
    # ── Rooms ──────────────────────────────────────────────
    total_rooms = Room.objects.count()
    occupied_rooms = Room.objects.filter(is_occupied=True).count()
    available_rooms = Room.objects.filter(is_occupied=False).count()

    # ── Guests ─────────────────────────────────────────────
    total_guests = Guest.objects.count()
    guests_with_room = Guest.objects.filter(room__isnull=False).count()
    guests_without_room = Guest.objects.filter(room__isnull=True).count()

    # ── Payments ───────────────────────────────────────────
    total_payments = Payment.objects.count()

    total_revenue = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
    mobile_money_total = Payment.objects.filter(
        payment_type='Mobile Money').aggregate(total=Sum('amount'))['total'] or 0
    cash_total = Payment.objects.filter(
        payment_type='Cash').aggregate(total=Sum('amount'))['total'] or 0

    # ── Recent Payments (last 5) ────────────────────────────
    recent_payments = Payment.objects.select_related('room').order_by('-payment_date')[:5]

    # ── Room category breakdown ─────────────────────────────
    category_stats = Room.objects.values('category').annotate(count=Count('id'))

    context = {
        # Rooms
        'total_rooms': total_rooms,
        'occupied_rooms': occupied_rooms,
        'available_rooms': available_rooms,

        # Guests
        'total_guests': total_guests,
        'guests_with_room': guests_with_room,
        'guests_without_room': guests_without_room,

        # Payments
        'total_payments': total_payments,
        'total_revenue': total_revenue,
        'mobile_money_total': mobile_money_total,
        'cash_total': cash_total,

        # Extras
        'recent_payments': recent_payments,
        'category_stats': category_stats,
    }

    return render(request, 'reports_dashboard.html', context)
