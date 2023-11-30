from django.shortcuts import render
import datetime
from datetime import  timedelta

# Create your views here.
def filter_all(request):
    data={"add_nu":10,"addSla":"i'm sakib",
          "dateTime":datetime.datetime.now(),"null":'',
          "list":[ {'name': 'zed', 'age': 19},
                  {'name': 'amy', 'age': 22},
                  {'name': 'joe', 'age': 31},],
                  "es":"&lt","up":"KAMAL IS a LOGER",
                  "delet":datetime.datetime.now() - timedelta(days=7),
                  "lorem":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem alias vel iure fugit dicta placeat? Reprehenderit rerum aut, et, sit itaque corporis inventore asperiores, reiciendis quis optio ipsam quidem expedita.",
                  "p":'<p><button>submit<button></p>'


          }
    return render(request, 'filter_all.html',data)
