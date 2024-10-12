from django.http import HttpRequest
from django.shortcuts import render,redirect
from .form import Donate,Data_Getting
from AdminData.models import Admin_panel
from Getting_Data.models import Data_Getting




def index(request):
    data={
        "Webname":"BlockCharityChain",
        "quote":"Together, We Can Make a Difference",
        "quote1":"Join us in our mission to uplift communities and change lives through your generous support",
        "quote2":"Make a donation in memory or honor of someone special",
        "button_text":"Donate Now",
        "how_it_work_section":"How It Works ",
        "how_it_work_section1":"Donate",
        "how_it_work_section2":"Impact",
        "how_it_work_section3":"Get Involved",
        "how_it_work_section1_1":"Your contributions, big or small, directly support our programs and initiatives. Every dollar makes a difference",
        "how_it_work_section1_2":"See how your donations help real people. We provide regular updates and stories showcasing the lives you’ve touched",
        "how_it_work_section1_3":"Join our community of supporters! Explore various ways to contribute, from one-time donations to recurring support or volunteering your time.",
        "program":"Programs",
        "Education":"Education",
        "BasicNeeds":"Basic Needs",
        "HealthWellness":"Health & Wellness",
        "CommunityDevelopment":"Community Development",
        "Education_p1":"Providing educational resources and scholarships to underprivileged children, helping them access quality education.",
        "BasicNeeds_p1":"Distributing food, clothing, and shelter to families in crisis, ensuring they have the essentials to survive and access to vital support services.",
        "HealthWellness_p1":"Offering health services and mental health support to those in need, helping them lead healthier lives.",
        "CommunityDevelopment_p1":"Empowering local communities through skill-building workshops, job training, mentorship, and support programs.",
        "Testimonials":"What Our Supporters Say",
        "Tom":"I never realized how much my small contribution could help. Knowing that I'm making a difference feels incredible",
        "Jerry":"The impact of this organization on the community is truly inspiring. I am proud to be a part of it",
        "Get_Involved":"Get Involved",
        "Volunteer":"Volunteer",
        "Spread_the_Word":"Spread the Word",
        "Follow_Us_on_SocialMedia":"Follow Us on Social Media",
        "Volunteer_p":"Join our team of passionate volunteers! Whether you can lend a hand at events, help with administrative tasks, or provide mentorship, your time is invaluable to us",
        "Spread_the_Word_p":"Share our mission with your friends and family. Every conversation counts in raising awareness and support",
        "Follow_Us_on_SocialMedia_p":"Stay updated on our initiatives and impact by following us on [social media links]",
    }
   
    return render(request,"index.html",data)

def Donation(request):
    Donate_fu=Donate()
    Admin_Data=Admin_panel.objects.all()
    GettingData=Data_Getting()
    Donate_Data={
        "Donation_info":Donate_fu,
        "Admin_Data":Admin_Data,
        "Data_Getting":GettingData
    }
    try:
        if request.method=="POST":
            First_name=request.POST.get('First_name')
            last_name=request.POST.get('last_name')
            email_Address=request.POST.get('email_Address')
            phone_Number=request.POST.get('phone_Number')
            Purpose=request.POST.get('Purpose')

            Donate_Data={

                "Donation_info":Donate_fu,
                "Admin_Data":Admin_Data,
                "First_name":First_name,
                "last_name":last_name,
                "email_Address":email_Address,
                "phone_Number":phone_Number,
                "Purpose":Purpose,

            }

    
    except:
        pass

    if request.method=="POST":
        Name=request.POST.get('Name')
        Father_Name=request.POST.get('Father_Name')
        Mother_Name=request.POST.get('Mother_Name')

        
        Donate_Data={
        "Donation_info":Donate_fu,
        "Admin_Data":Admin_Data,
        "Data_Getting":GettingData,
        "Name":Name,
        "Father_Name":Father_Name,
        "Mother_Name":Mother_Name,
        

    }
        FormData=Data_Getting(Name=Name,Father_Name=Father_Name,Mother_Name=Mother_Name)
        FormData.save
        
    return render(request,'Donate.html',Donate_Data)