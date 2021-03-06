from django.views import generic
from ranges.models import RangeStudents, StudentQuestions, Range
from accounts.models import User
from ranges.views import Housekeeping
from django.views.generic.base import TemplateView
from django.contrib import messages

class DashboardView(generic.ListView):
    template_name='dashboard/dashboard.html'
    context_object_name = 'assignedranges'

    def get_queryset(self):
        user = self.request.user
        assignedranges = RangeStudents.objects.filter(studentID=user, rangeID__rangeactive=1, rangeID__isdisabled=0).order_by('-lastaccess', '-dateJoined', '-pk')[:5]
        self.reportboxes = assignedranges[:4]
        latestfive = assignedranges[:5]
        currentranges = RangeStudents.objects.filter(studentID = user).values_list('rangeID')
        Housekeeping.get(self, currentranges)
        return latestfive

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        username = self.request.user
        
        latestrange = RangeStudents.objects.filter(studentID = username).order_by('-lastaccess', '-dateJoined')
        context['scoreboard'] = False
        if len(latestrange) != 0:
            context['scoreboard'] = True
            lateststudentrange = latestrange[0]
            latestrangeid = lateststudentrange.rangeID
            ranking = RangeStudents.objects.filter(rangeID=latestrangeid.rangeid).order_by('-points')
            context['rangeurl'] = Range.objects.filter(rangeid=latestrangeid.rangeid).values_list('rangeurl')[0][0]
            context['username'] = username
            context['rangename'] = latestrangeid.rangename
            context['maxscore'] = latestrangeid.maxscore
            context['userscore'] = lateststudentrange.points
            context['topfive'] = ranking[:5]
            # need to check if user in top 5 already
            intopfive = False
            for students in ranking[:5]:
                if students.studentID == username:
                    intopfive = True

            context['madeit'] = intopfive
            context['ranking'] = ranking
            context['reportboxes'] = self.reportboxes
        context['latestranges'] = latestrange
        if len(self.reportboxes) == 0:
            context['norange'] = True

        # check if the teacher's password is default 
        # get the current user 
        username = self.request.user
        # get the object
        userobj = User.objects.get(username = username)
        # check if the password is default
        if userobj.isdefault is True:
            messages.error(self.request, 'Default Password Detected. Please Change Your Password!')

        return context

class VPNTutorial(TemplateView):
    template_name = 'dashboard/vpn.html'