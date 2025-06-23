from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Requisition
from .forms import RequisitionForm
from django.contrib import messages


@login_required
def requisition_create(request):
    if request.method == 'POST':
        form = RequisitionForm(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.user = request.user
            requisition.save()
            return redirect('requisition_list')
    else:
        form = RequisitionForm()
    return render(request, 'requisitions/requisition_form.html', {'form': form})

@login_required
def requisition_list(request):
    requisitions = Requisition.objects.filter(user=request.user)
    return render(request, 'requisitions/requisition_list.html', {'requisitions': requisitions})



@login_required
def requisition_admin_list(request):
    if not request.user.profile.role in ['manager', 'admin']:
        return redirect('unauthorized')  # Optional page

    requisitions = Requisition.objects.all().order_by('-created_at')
    return render(request, 'requisitions/requisition_admin_list.html', {'requisitions': requisitions})

@login_required
def approve_requisition(request, pk):
    if request.user.profile.role not in ['manager', 'admin']:
        return redirect('unauthorized')

    req = get_object_or_404(Requisition, pk=pk)
    req.status = 'Approved'
    req.save()

    messages.success(request, f"{req.user.username}'s request for {req.quantity} {req.product.name}(s) was approved.")
    return redirect('requisition_admin_list')

@login_required
def reject_requisition(request, pk):
    if request.user.profile.role not in ['manager', 'admin']:
        return redirect('unauthorized')

    req = get_object_or_404(Requisition, pk=pk)
    req.status = 'Rejected'
    req.save()

    messages.error(request, f"{req.user.username}'s request for {req.quantity} {req.product.name}(s) was rejected.")
    return redirect('requisition_admin_list')
