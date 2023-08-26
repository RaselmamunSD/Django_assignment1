from django.shortcuts import render

def contact(request):
    return render(request, './first_app/index.html', { "name": "I am Rahim",
    "marks": 86,"lst" :[24,3,10,5], "blog" : "Lorem ipsum dolor,sit amet consectetur adipisicing elit. Harum quae tempora fugit labotum voluptas mollitia. Explicabo earum assumende obcaecati et."})