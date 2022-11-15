from django.shortcuts import render,HttpResponse
import qrcode

# Create your views here.
def home(request):
    if request.method == 'POST':
        data = {}
        res = ""
        name = request.POST.get('Name')
        data["Name"] =name
        email = request.POST.get('Email')
        data["Email"] =email
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

        for i in data:
            res = res + (i+"  "+str(data[i])+' ')

        return render(request,'display.html',{'data':str(res)})

    return render(request,'home.html')



def generate_qr(data):
    qr = qrcode.QRCode(version = 1,
    				box_size = 10,
    				border = 5)
    for i in data:
        qr.add_data(str(i) + "  ")

    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black',
    					back_color = 'white')

    # img.save('res.png')
    return img

def download(request):
    return render(request,'display.html')

def test(request):
    return render(request,'temp.html')
