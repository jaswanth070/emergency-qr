from django.shortcuts import render,HttpResponse


# Create your views here.
def home(request):
    if request.method == 'POST':
        data = {}
        res = ""
        name = request.POST.get('Name')
        data["Name"] =name
        vhc_no = request.POST.get('Vhc_no')
        data["Vehical No"] =vhc_no
        gender = request.POST.get('Gender')
        data["Gender"] =gender
        phone1 = request.POST.get('Phone1')
        data["Phone 1"] =phone1
        phone2 = request.POST.get('Phone2')
        data["Phone 2"] = phone2
        phone3 = request.POST.get('Phone3')
        data["Phone 3"] = phone3
        occu = request.POST.get('Occupation')
        data["Occupation"] = occu
        address = request.POST.get('Address')
        data["Address"] = address
        bld_grp = request.POST.get('Blood_Group')
        data["Blood_Group"] = bld_grp
        med_cond = request.POST.get('Medical_cond')
        data["Medical_condition"] = med_cond

        # res = '\n'.join(f'{key}: {value}' for key, value in data.items())
        for i in data:
            res = res + (i+"  "+str(data[i])+' ')
        # res = ['\nName : ' + str(name)]
        # res.append('Gender : ' + str(gender))
        # res.append('Vehical Number : ' + str(vhc_no))
        # res.append('Emergency Number 1: ' + str(phone1))
        # res.append('Emergency Number 2: ' + str(phone2))
        # res.append('Optional Number : ' + str(phone3))
        # res.append('Occupation : ' + str(occu))
        # res.append('Address : ' + str(address))
        # res.append('Blood Group : ' + str(bld_grp))
        # res.append('Medical Condition : ' + str(med_cond))

        # ans = '\n'.join(res)
        return render(request,'display.html',{'data':res,'name':name,"bld_grp":bld_grp,"em_ph":phone1})

    return render(request,'home.html')


def download(request):
    return render(request,'display.html')

def docs(request):
    return render(request,'docs.html')

def about(request):
    return render(request,'about.html')

def test(request):
    return render(request,'temp.html')
