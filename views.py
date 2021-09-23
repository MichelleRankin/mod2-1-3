from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from typing import List 
from dataclasses import dataclass


@dataclass
class Team:
    name: str 
    description: str 
    members: List[str]



def hello_view(request, name):
    context = {
        "name": name,
        "Teams": {
           "management": Team("Management Team",
                "A select few members of Base Camp who are tasked with keeping inventory, doing laundry, assigning chores, checking off chores, as well as keeping members of Base Camp on task.", 
                ["Rylee Chisholm", "Michelle Rankin", "Daelen Hollingsworth", "Dylan Goad", "Will Collins", "Logan Coley"]
                ),

           "procurement": Team("Procurement Team", 
                "A select few members of Bases Camp who are tasked with obtaining items for everyday lunches, and procuring items for cleaning and general day to day activities.",
                ["Gary", "Dylan S", "Richard", "Mariann", "Ethan", "Quinton"]
                ),

           "document": Team("Document Team", 
                "A select few members of Base Camp who are tasked with documenting the year's progress at Base Camp, as well as organizing posts on different social media platform to obtain sponsers for Base Camp.",
                ["Randy", "Isaac", "Ma'kyla", "Ben", "Ryan"]
                ),

            "community": Team("Community Team", 
                "A select few members of Base Camp who are tasked with organizing parties for birthdays, recognizing individual members weekly for different qualities noticed by their peers.",
                ["Jacen", "Rjay", "Logan W", "Justin", "Ariyana"]
                )
        }
    }
    return render(request, "hello.html", context)



