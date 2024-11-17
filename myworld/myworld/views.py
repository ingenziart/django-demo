from django.shortcuts import render

data = {
    "name": [
        {
            "name": "ongback",
            "year": 2024,
        },
        {"name": "jetri", "year": 2025},
        {"name": "badboys", "year": 2024},
    ]
}


def movies(request):
    return render(request, "movies/movies.html", data)
