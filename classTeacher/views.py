# import csv
import xlwt
import datetime
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from login.models import Department, Admin, Class, Student, Faculty, Course, Attendance, Teache, ClassTeacher
from django.contrib import messages

# Create your views here.
cltrid = ""
clid = ""

final_attendance=[]
unique_courses=[]
sid=[]

def initial(a, b):
    global cltrid, clid
    cltrid = a
    clid = b

def initial2(a,b,c):
    global final_attendance,unique_courses,sid
    final_attendance=a
    unique_courses=b
    sid=c

def clalogin(request):
    if request.method == "POST":
        u, p = request.POST.get('username'), request.POST.get('password')
        clao = ClassTeacher.objects.filter(classTeacher_id=u)
        if clao.exists():
            if clao.get().password == p:
                a = clao.get().classTeacher_id
                b = clao.get().class_id.class_id
                initial(a, b)
                return clatrindex(request)
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('clalogin')
        else:
            messages.error(request, 'No such User exists')
            return redirect('clalogin')
    else:
        messages.error(request, 'Enter Credentials')
        return render(request, 'clatrlogin.html')


def clatrindex(request):
    final_attendance = []
    # all the courses assigned to class
    unique_courses = []
    temp_courses = Teache.objects.filter(class_id=clid)
    for f in temp_courses.values():
        unique_courses.append(f['course_id_id'])
    # student ids of all students belonging to that class
    sid = []
    temp_sid = Student.objects.filter(class_id=clid).order_by('stud_id')
    for i in temp_sid:
        sid.append(i.stud_id)
    for stu in sid:
        row = []
        for course in unique_courses:
            total_lectures = 0
            lec_attended = 0
            lec = Attendance.objects.all().filter(stud_id=stu, course_id=course)
            for x in lec.values():
                if (x['presence'] == 1):
                    lec_attended += 1
                total_lectures += 1
            row.append(lec_attended)
            row.append(round(lec_attended/total_lectures*100, 2))
        final_attendance.append(row)
    print("final attendance=", final_attendance)
    initial2(final_attendance,unique_courses,sid)
    course_names=[]
    for i in unique_courses:
        course_names.append(Course.objects.get(course_id=i).course_name)
    cltr_obj=ClassTeacher.objects.get(classTeacher_id=cltrid)
    return render(request, 'clatrindex.html', {"courses": course_names, "classname": clid,"firstname":cltr_obj.f_name,"lastname":cltr_obj.l_name})
    # fac_obj=Faculty.objects.get(fac_id=cltrid)
    # return render(request, 'clatrindex.html', {"courses": course_names, "classname": clid,"firstname":fac_obj.f_name,"lastname":fac_obj.l_name})


def down_report(request):
    print("form submitted")
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="AttendanceReport.xls"'
    wb= xlwt.Workbook(encoding="UTF-8")
    ws= wb.add_sheet('Report') 
    YELLOW_TABLE_HEADER = xlwt.easyxf(
        'font: bold 1, name Tahoma, height 250;'
        'align: vertical center, horizontal center, wrap on;'
        'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega'   
        )
    header_width=3+2*len(unique_courses)-1
    ws.write_merge(0, 1, 0, header_width, 'Sardar Patel Institute Of Technology', YELLOW_TABLE_HEADER)
    ws.write_merge(2, 2, 0, header_width, '(AUTONOMOUS INSTITUTE AFFILIATED TO MUMBAI UNIERSITY)', YELLOW_TABLE_HEADER)
    ws.write_merge(3, 3, 0, header_width, 'MUNSHI NAGAR ANDHERI (W), MUMBAI - 400058', YELLOW_TABLE_HEADER)
    current_datetime=datetime.datetime.now()
    d="Defaulter List Till ",current_datetime.strftime("%d-%m-%Y")
    ws.write_merge(4, 4, 0, header_width, d, YELLOW_TABLE_HEADER)
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    ytoskip=5
    ws.write_merge(ytoskip,1+ytoskip,0, 0, 'UID', xlwt.easyxf("font: bold 1 ; pattern: pattern solid , fore_color lavender"))
    ws.write_merge(ytoskip,1+ytoskip,1, 1, 'First Name', xlwt.easyxf("font: bold 1 ; pattern: pattern solid , fore_color lavender"))
    ws.write_merge(ytoskip,1+ytoskip,2, 2, 'Last Name', xlwt.easyxf("font: bold 1 ; pattern: pattern solid , fore_color lavender"))
    for i in range(len(unique_courses)):
        ws.write_merge(ytoskip,ytoskip,i*2+3,i*2+1+3,Course.objects.get(course_id=unique_courses[i]).course_name, xlwt.easyxf("font: bold 1; align: horiz center;pattern: pattern solid , fore_color lavender"))
        ws.write(1+ytoskip, 2*i+3, 'Lectures Attended', xlwt.easyxf("font: bold 1 ; pattern: pattern solid , fore_color lavender"))
        ws.write(1+ytoskip, 2*i+3+1, '% Attendance', xlwt.easyxf("font: bold 1 ; pattern: pattern solid , fore_color lavender"))
    for i in range(len(final_attendance)):
        arr = []
        ws.write(i+2+ytoskip, 0, sid[i],xlwt.easyxf("font: bold 1 ; pattern: pattern solid , fore_color ivory"))
        name = Student.objects.get(stud_id=sid[i])
        ws.write(i+2+ytoskip, 1, name.f_name,xlwt.easyxf("font: bold 1 ; pattern: pattern solid , fore_color ivory"))
        ws.write(i+2+ytoskip, 2, name.l_name,xlwt.easyxf("font: bold 1 ; pattern: pattern solid , fore_color ivory"))
        for j in range(len(final_attendance[i])):
            if j%2==1:
                if final_attendance[i][j]<75:
                    ws.write(i+2+ytoskip, j+3, final_attendance[i][j],xlwt.easyxf("pattern: pattern solid , fore_color coral; align: horiz center"))
                else:
                    ws.write(i+2+ytoskip, j+3, final_attendance[i][j],xlwt.easyxf("pattern: pattern solid , fore_color light_green ; align: horiz center"))
            else:
                ws.write(i+2+ytoskip, j+3, final_attendance[i][j],xlwt.easyxf("align: horiz center"))
    wb.save(response)
    return response
