from django.http import JsonResponse
from App.models import Values_Principle
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def index(request):
    return HttpResponse("python-test")


@csrf_exempt
def create_values_or_principle(request):
    response = {}

    if request.method == "POST":
        data = request.POST
        payload = {}
        for i in data.keys(): payload[i] = data[i]
        if payload:
            id = Values_Principle.objects.create(**payload)
            response["id"] = str(id)
            response["status"] = "Success"

    else:
        response["id"] = "None"
        response["status"] = "Failed"

    return JsonResponse(response)


@csrf_exempt
def read_values_principle(request, context_type, id):
    response = {}
    ret = None
    keys = ["Principle ID", "Principle"]

    try:
        if str(context_type) == "values":
            context_type = "V"
            keys = ["Values-ID", "Values"]
        else:
            context_type = "P"

        ret = Values_Principle.objects.get(id=id,context_type=context_type)

    except Exception:
        pass

    if ret:
        data = [ret.context_id,ret.context]
        for x in range(len(keys)):
            response[keys[x]] = data[x]

    return JsonResponse(response)


@csrf_exempt
def read_all_values_principle(request):
    response = {}
    payload = Values_Principle.objects.all()

    if payload:
        response["Values"] = {}
        response["Principle"] = {}

        for data in payload:
            id = data.context_id

            if data.context_type is "V":
                response["Values"][id] = {"#{}".format(id): data.context}
            else:
                response["Principle"][id] = {"#{}".format(id): data.context}

    return JsonResponse(response)


@csrf_exempt
def update_values_principle(request):
    response = {}
    if request.method == "POST":
        data = request.POST
        payload = {}
        for i in data.keys(): payload[i] = data[i]

        if payload:
            id = payload["id"]
            context = payload["context"]

            cl = Values_Principle.objects.get(id=id)
            cl.context = context
            cl.save()

    return JsonResponse(response)


@csrf_exempt
def delete_values_principle(request):
    response = {}

    if request.method == "POST":
        data = request.POST
        id = data["id"]

        entry = Values_Principle.objects.get(id=id)
        isdel = entry.delete()

        if isdel:
            response["msg"] = "Success"
            response["status_code"] = "202"

    return JsonResponse(response)


@csrf_exempt
def clearAll(request):
    response = {}

    entries = Values_Principle.objects.all()
    isdel = entries.delete()
    if isdel:
        response["msg"] = "CLEANING-DB"
        response["status_code"] = "202"

    return JsonResponse(response)


@csrf_exempt
def store_all_values_principle(request):
    data = [
        [1,"Individuals and Interactions Over Processes and Tools","V"],
        [2,"Working Software Over Comprehensive Documentation","V"],
        [3,"Customer Collaboration Over Contract Negotiation","V"],
        [4,"Responding to Change Over Following a Plan","V"],

        [1,"Customer satisfaction through early and continuous software delivery ","P"],
        [2,"Accommodate changing requirements throughout the development process","P"],
        [3, "Frequent delivery of working software", "P"],
        [4, "Collaboration between the business stakeholders and developers throughout the project", "P"],
        [5, "Support, trust, and motivate the people involved ", "P"],
        [6, "Enable face-to-face interactions", "P"],
        [7, "Working software is the primary measure of progress", "P"],
        [8, "Agile processes to support a consistent development pace", "P"],
        [9, "Attention to technical detail and design enhances agility", "P"],
        [10, "Simplicity", "P"],
        [11, "Self-organizing teams encourage great architectures, requirements, and designs", "P"],
        [12, "Regular reflections on how to become more effective", "P"],

    ]

    for i in data:
        context_id, context, context_type = i
        id = Values_Principle.objects.create(
            context=context,
            context_type=context_type,
            context_id=context_id
        )


    return HttpResponse("STORING DONE!")

