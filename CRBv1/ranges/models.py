from django.db import models
# Create your models here.

class Range(models.Model):
    rangeid = models.AutoField(db_column='rangeID', primary_key=True)  # Field name made lowercase.
    rangename = models.CharField(db_column='rangeName', max_length=45)  # Field name made lowercase.
    rangeactive = models.BooleanField(db_column='rangeActive', default=False)
    datetimecreated = models.DateTimeField(db_column='dateTimeCreated', blank=True, null=True)  # Field name made lowercase.
    datetimestart = models.DateTimeField(db_column='dateTimeStart', blank=True, null=True)  # Field name made lowercase.
    datetimeend = models.DateTimeField(db_column='dateTimeEnd', blank=True, null=True)  # Field name made lowercase.
    maxscore = models.IntegerField(db_column='maxScore', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddate = models.DateField(db_column='lastModifiedDate', blank=True, null=True)  # Field name made lowercase.
    rangecode = models.IntegerField(db_column='rangeCode', blank=True, null=True, unique=True)  # Field name made lowercase.
    username = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='lastModifiedBy', blank=True, null=True, related_name='LMBR')  # Field name made lowercase.
    username = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='createdby', related_name='CBR', default='super')  # Field name made lowercase.
    rangeurl = models.CharField(db_column='rangeURL', max_length=50, null=True)
    studentsinrange = models.IntegerField(db_column='studentsInRange', null=True)

    class Meta:
        db_table = 'Range'
        verbose_name_plural = 'Ranges'

class RangeStudents(models.Model):
    dateJoined = models.DateTimeField(db_column='dateJoined', max_length=45, blank=True, null=True)
    progress = models.CharField(db_column='progress', max_length=45, null=True)
    teamID = models.CharField(db_column='teamID', max_length=45, null=True)
    teamName = models.CharField(db_column='teamName', max_length=45, null=True)
    points = models.IntegerField(db_column='points', default=0)
    rangeID = models.ForeignKey(Range, models.DO_NOTHING, db_column='rangeID',unique=False)  # Field name made lowercase.
    studentID = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='email', unique=False)  # Field name made lowercase.
    datecompleted = models.DateField(db_column='dateCompleted', null=True)
    timecompleted = models.TimeField(db_column='timeCompleted', null=True)
    lastaccess = models.DateTimeField(db_column='lastaccess', null=True)

    REQUIRED_FIELDS = ['rangeID', 'studentID']

    class Meta:
        db_table = 'RangeStudents'
        verbose_name_plural = 'RangeStudents'


class QuestionTopic(models.Model):
    topicid = models.AutoField(db_column='topicid', primary_key=True)
    topicname = models.CharField(db_column='topicname', max_length=100, null=True)

    class Meta:
        db_table = 'QuestionTopic'
        verbose_name_plural = 'QuestionTopics'

class Questions(models.Model):
    questionid = models.AutoField(db_column='questionID', primary_key=True)

    FLAG = 'FL'
    MCQ = 'MCQ'
    SHORTANS = 'SA'
    OPENENDED = 'OE'
    TRUEFALSE = 'TF'
    QUESTION_TYPE_CHOICES = (
            (FLAG, 'Flag'),
            (MCQ, 'Multiple Choice'),
            (SHORTANS, 'Short Answer'),
            (OPENENDED, 'Open Ended'),
            (TRUEFALSE, 'True/False')
        )
    questiontype = models.CharField(db_column='questiontype', choices = QUESTION_TYPE_CHOICES, default='FL', max_length=100)
    title = models.CharField(db_column='questiontitle', max_length=100, null=True)
    text = models.CharField(db_column='questiontext', max_length=100)
    hint = models.CharField(db_column='hint', max_length=100)
    marks = models.IntegerField(db_column='marks')
    topicid = models.ForeignKey(QuestionTopic, models.DO_NOTHING, db_column='categoryid', unique=False, related_name='catid', null=True)

    class Meta:
        db_table = 'Questions'
        verbose_name_plural = 'Questions'

class MCQOptions(models.Model):
    questionid = models.ForeignKey(Questions, models.CASCADE, db_column='questionid', unique=False)
    optionone = models.CharField(db_column='OptionOne', max_length=100)
    optiontwo = models.CharField(db_column='OptionTwo', max_length=100)
    optionthree = models.CharField(db_column='OptionThree', max_length=100)
    optionfour = models.CharField(db_column='OptionFour', max_length=100)
    
    class Meta:
        db_table = 'MCQOptions'
        verbose_name_plural = 'MCQOptions'

class RangeQuestions(models.Model):
    rangequestionsid = models.AutoField(db_column='id', primary_key=True)
    #questionorder = models.IntegerField(db_column='order', primary_key=False)
    rangeid = models.ForeignKey(Range, models.DO_NOTHING, db_column='rangeID', unique=False)
    questionid = models.ForeignKey(Questions, models.DO_NOTHING, db_column='questionID', unique=False)
    answer = models.CharField(db_column='answer', max_length=100, null=True)

    class Meta:
        db_table = 'RangeQuestions'
        verbose_name_plural = 'RangeQuestions'

class StudentQuestions(models.Model):
    studentid = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='email', unique=False)
    rangeid = models.ForeignKey(Range, models.DO_NOTHING, db_column='rangeID',unique=False)
    questionid = models.ForeignKey(Questions, models.DO_NOTHING, db_column='questionid', unique=False)
    answergiven = models.CharField(db_column='answergiven', max_length=100)
    answercorrect = models.BooleanField(db_column='right/wrong', default=False)
    marksawarded = models.IntegerField(db_column='marksawarded')

    class Meta:
        db_table = 'StudentQuestions'
        verbose_name_plural = 'StudentQuestions'

class UnavailablePorts(models.Model):
    portnumber = models.IntegerField(db_column='portNumber', primary_key=True)
    studentid = models.ForeignKey('accounts.User', models.DO_NOTHING, db_column='studentid')

    class Meta:
        db_table = 'UnavailablePorts'
        verbose_name_plural = 'UnavailablePorts'