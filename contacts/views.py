from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_ContactEnquiry = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_ContactEnquiry:
                messages.error(request, 'You have already made an enquiry for this listing')
                return redirect('/listings/'+listing_id)
        contact = Contact(listing_id=listing_id,listing=listing,email=email,name=name,phone=phone,message=message,user_id=user_id)
        contact.save()
        send_mail(
                'Inquiry for Listing',
                'This is body messgae for listing.'+ listing,
                'amit.gupta@kiwitech.com',
                [realtor_email],
                fail_silently=False,
            )
        messages.success(request, 'You query submitted successfully')
    return redirect('/listings/'+listing_id)
