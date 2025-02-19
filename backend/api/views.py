from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Prefetch
from django.db.models import Q
from .models import User,Festival,Artist,Genre,City, TicketType, Ticket
from .forms import ContactForm
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone
import traceback



# Create your views here.
def index(request):
    #return render(request,"getgig/index.html",{})
    loggedIn = request.session.get('loggedIn', False)
    return render(request, 'getgig/index.html', {"loggedIn": loggedIn})

def about(request):
    return render(request,"getgig/about.html",{})

def contact(request):
    return render(request,"getgig/contact.html",{})

def register(request):
    return render(request,"getgig/register.html",{})

def signin(request):
    return render(request,"getgig/signin.html",{})

def booking(request):
    return render(request, "getgig/booking.html", {})

def events(request):
    festivals = Festival.objects.prefetch_related(
        Prefetch('artists', queryset=Artist.objects.prefetch_related('genres'))
    )
    genres = Genre.objects.all() 
    artists = Artist.objects.all()
    cities = City.objects.all()
    genres = Genre.objects.all()
    context = {
        'festivals': festivals,
        'genres': genres,
        'artists': artists,
        'cities': cities,
    }
    if request.path == '/gadmin/database':
        template_name = 'getgig-admin/database.html'
    else:
        template_name = 'getgig/events.html'
    
    return render(request, template_name, context)

def eventdetail(request, festival_id):
    festival = get_object_or_404(Festival, pk=festival_id)
    ticket_types = TicketType.objects.all()
    artists = festival.artists.all()

    
    context = {
        'festival': festival,
        'artists': artists,
        'ticket_types': ticket_types
    }
    return render(request, 'getgig/eventdetail.html', context)

def search(request):
    # Retrieve the text query from GET parameters
    query = request.GET.get('q', '')
    
    # Start with all festivals
    festivals = Festival.objects.all()
    
    # If a text query is provided, filter by festival name, city, artist, or genre name
    if query:
        festivals = festivals.filter(
            Q(fname__icontains=query) |
            Q(city__cname__icontains=query) |
            Q(artists__aname__icontains=query) |
            Q(artists__genres__gname__icontains=query)
        ).distinct()
    
    context = {
        'festivals': festivals,
        'query': query,
    }
    return render(request, 'getgig/searchresults.html', context)

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data
            return redirect('contact')  # Adjust to your success page
    else:
        form = ContactForm()  # Create a new, blank form instance

    return render(request, 'getgig/contact.html', {'form': form})

def insertuser(request):
    text_email = request.POST['tuemail']
    text_password = request.POST['tupassword']
    ob = User(uemail=text_email,upassword=text_password)
    ob.save()
    return redirect("index")

def admin(request):
    return render(request, "getgig-admin/admin.html", {})

def addfestivals(request):
    return render(request, "getgig-admin/addfestivals.html",{})

def insertfestival(request):
    if request.method == "POST":
        text_name = request.POST.get('fname', '').strip()
        date_start_date = request.POST.get('start_date')
        date_end_date = request.POST.get('end_date')
        number_cid = request.POST.get('cid')
        text_playlist = request.POST.get('playlist', '').strip()
        text_description = request.POST.get('description', '').strip()


        try:
            number_cid = int(number_cid)
        except (ValueError, TypeError):
            messages.error(request, "Invalid CID. It must be a number.")
            return redirect("addfestivals")


        try:
            cid_obj = City.objects.get(cid=number_cid)
        except City.DoesNotExist:
            messages.error(request, "City not found.")
            return redirect("addfestivals")


        ob = Festival(
            fname=text_name,
            start_date=date_start_date,
            end_date=date_end_date,
            city=cid_obj,
            playlist=text_playlist,
            description=text_description
        )
        ob.save()

        messages.success(request, "Festival added successfully!")
        return redirect("admin")

    return redirect("addfestivals")

def selectfestivaledit(request):
    return render(request, "getgig-admin/selectfestivaledit.html",{})

def editfestivals(request):
    festivals = Festival.objects.all()
    return render(request, "getgig-admin/editfestivals.html",{'festivals': festivals})

def inserteditfestivals(request):
    if request.method == "POST":
        festival_id = request.POST.get('festival_id')

        text_name = request.POST.get('fname', '').strip()
        date_start_date = request.POST.get('start_date')
        date_end_date = request.POST.get('end_date')
        number_cid = request.POST.get('cid')
        text_playlist = request.POST.get('playlist', '').strip()
        text_description = request.POST.get('description', '').strip()

        festival = get_object_or_404(Festival, fid=festival_id)

        try:
            number_cid = int(number_cid)
        except (ValueError, TypeError):
            messages.error(request, "Invalid CID. It must be a number.")
            return redirect("editfestival")


        try:
            cid_obj = City.objects.get(cid=number_cid)
        except City.DoesNotExist:
            messages.error(request, "City not found.")
            return redirect("editfestival")


        festival.fname = text_name
        festival.start_date = date_start_date
        festival.end_date = date_end_date
        festival.city = cid_obj
        festival.playlist = text_playlist
        festival.description = text_description
        festival.save()

        messages.success(request, "Festival updated successfully!")
        return redirect("admin")

    return redirect("editfestival")
"""
def custom_login(request):
    if request.method == "POST":
        email = request.POST['tuemail']
        passwd = request.POST['tupassword']
        try:
            user = User.objects.get(uemail=email)

            if user.upassword == passwd:
                print(f"Login successful for {email}")
                loggedIn=True
                if user.uemail == "admin@gmail.com":
                    return redirect('admin')
                else:
                    return redirect('index')
            else:
                return render(request,"getgig/signin.html",{})
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            
            
"""


def custom_login(request):
    if request.method == "POST":
        email = request.POST['tuemail']
        passwd = request.POST['tupassword']
        try:
            user = User.objects.get(uemail=email)
            if user.upassword == passwd:
                print(f"Login successful for {email}")
                loggedIn = True
                request.session['loggedIn'] = loggedIn  # Store in session
                request.session['userEmail'] = user.uemail  # Store in session
                if user.uemail == "admin@gmail.com":
                    return redirect('admin')
                else:
                    return redirect('index')
            else:
                return render(request, "getgig/signin.html", {"loggedIn": False})
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return render(request, "getgig/signin.html", {"loggedIn": False})

    return render(request, "getgig/signin.html", {"loggedIn": False})

def logout(request):
    request.session.flush()
    return redirect('index')

def ticket_prices(request):
    ticket_types = TicketType.objects.all().values('id','ticket_type_name', 'ticket_price')
    return JsonResponse(list(ticket_types), safe=False)

def booktickets(request,festival_id):
    if request.method == "POST":
        number_tunumberoftickets = int(request.POST.get('tunumberoftickets', 1))
        number_totalprice = int(request.POST.get('totalprice', 0))
        date_ticket_date_str = request.POST.get('tudate', None)
        number_fid = int(request.POST.get('fid', 0))
        number_ticket_type_id = int(request.POST.get('ticket_type_id', 0))
        text_uemail = request.POST.get('tuemail', None)


        date_ticket_date = datetime.strptime(date_ticket_date_str, "%Y-%m-%d").date()

        try:
            festival = Festival.objects.get(fid=festival_id)
        except Festival.DoesNotExist:
            messages.error(request, "Invalid festival ID.")
            return redirect("mybookings")

        try:
            ticket_type = TicketType.objects.get(id=number_ticket_type_id)
        except TicketType.DoesNotExist:
            messages.error(request, "Invalid ticket type ID.")
            return redirect("mybookings")

        try:
            user = User.objects.get(uemail=text_uemail)
        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist.")
            return redirect("mybookings")

        ob = Ticket(ticket_quantity=number_tunumberoftickets,total_price=number_totalprice,ticket_date=date_ticket_date,fid=festival,ticket_type_id=ticket_type,uemail=user)
        ob.save()
        messages.success(request, "Ticket booked successfully!")
        print("✅ Success: Ticket saved")
        return redirect("mybookings")

    return redirect("mybookings")

def mybookings(request):
    user_email = request.session.get('userEmail')

    print(user_email)

    if user_email:
        tickets = Ticket.objects.filter(
            uemail=user_email,
        )
        print(tickets, user_email)
    else:
        messages.error(request, "You must be logged in to view your bookings.")
        tickets = []

    return render(request, 'getgig/mybookings.html', {'tickets': tickets})