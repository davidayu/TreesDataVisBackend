# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailallowedtoregister(models.Model):
    email = models.CharField(unique=True, max_length=254)
    organization = models.ForeignKey('PathUniversity', models.DO_NOTHING, blank=True, null=True)
    token = models.TextField()
    email_send = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'account_emailallowedtoregister'


class AccountPasswordresettoken(models.Model):
    token = models.UUIDField(unique=True)
    user = models.OneToOneField('AccountUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_passwordresettoken'


class AccountUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    name = models.CharField(max_length=150)
    email_verified = models.BooleanField()
    verify_email_sent = models.BooleanField()
    university = models.ForeignKey('PathUniversity', models.DO_NOTHING, blank=True, null=True)
    is_organization_admin = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'account_user'


class AccountUserGroups(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_groups'
        unique_together = (('user', 'group'),)


class AccountUserUserPermissions(models.Model):
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_user_user_permissions'
        unique_together = (('user', 'permission'),)
# Unable to inspect table 'account_usersession'
# The error was: permission denied for table account_usersession


class AccountVerifyemailtoken(models.Model):
    token = models.UUIDField(unique=True)
    user = models.OneToOneField(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_verifyemailtoken'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FeedbackFeedback(models.Model):
    text = models.TextField()
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feedback_feedback'
# Unable to inspect table 'organization_admin_questiongroup'
# The error was: permission denied for table organization_admin_questiongroup
# Unable to inspect table 'organization_admin_questiongroup_assigned_to_user'
# The error was: permission denied for table organization_admin_questiongroup_assigned_to_user
# Unable to inspect table 'organization_admin_questiongroup_questions'
# The error was: permission denied for table organization_admin_questiongroup_questions
# Unable to inspect table 'path_filemodel'
# The error was: permission denied for table path_filemodel


class PathPath(models.Model):
    state = models.CharField(max_length=20)
    university = models.ForeignKey('PathUniversity', models.DO_NOTHING, blank=True, null=True)
    creator = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    video_link = models.CharField(max_length=277, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'path_path'
# Unable to inspect table 'path_path_path_to_category'
# The error was: permission denied for table path_path_path_to_category


class PathPathPathToUniversity(models.Model):
    path = models.ForeignKey(PathPath, models.DO_NOTHING)
    university = models.ForeignKey('PathUniversity', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'path_path_path_to_university'
        unique_together = (('path', 'university'),)


class PathPathcategory(models.Model):
    category = models.CharField(max_length=255)
    order = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=25)
    icon = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'path_pathcategory'


class PathPathcategoryCategorytouniversity(models.Model):
    pathcategory = models.ForeignKey(PathPathcategory, models.DO_NOTHING)
    university = models.ForeignKey('PathUniversity', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'path_pathcategory_categoryToUniversity'
        unique_together = (('pathcategory', 'university'),)


class PathPathdetail(models.Model):
    language = models.CharField(max_length=40)
    title = models.CharField(max_length=260)
    description = models.TextField()
    path = models.ForeignKey(PathPath, models.DO_NOTHING)
    search_vector = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'path_pathdetail'
        unique_together = (('path', 'language'),)


class PathPathmedia(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    file = models.TextField()
    timestamp = models.DateTimeField()
    path_step_detail = models.ForeignKey('PathPathstepdetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'path_pathmedia'


class PathPathstep(models.Model):
    order = models.IntegerField()
    path = models.ForeignKey(PathPath, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'path_pathstep'


class PathPathstepcomplete(models.Model):
    path_step = models.ForeignKey(PathPathstep, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    is_skipped = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'path_pathstepcomplete'
        unique_together = (('user', 'path_step'),)


class PathPathstepdetail(models.Model):
    language = models.CharField(max_length=40)
    step_name = models.CharField(max_length=255)
    description = models.TextField()
    path_step = models.ForeignKey(PathPathstep, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'path_pathstepdetail'
        unique_together = (('path_step', 'language'),)
# Unable to inspect table 'path_plansnotification'
# The error was: permission denied for table path_plansnotification
# Unable to inspect table 'path_status'
# The error was: permission denied for table path_status


class PathUniversity(models.Model):
    name = models.CharField(max_length=150)
    icon = models.CharField(max_length=100, blank=True, null=True)
    primary_color = models.CharField(max_length=10, blank=True, null=True)
    secondary_color = models.CharField(max_length=10, blank=True, null=True)
    tertiary_color = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.CharField(max_length=20)
    domain = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'path_university'


class PathUserpathfeedback(models.Model):
    rating = models.IntegerField()
    text = models.TextField()
    path = models.ForeignKey(PathPath, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'path_userpathfeedback'


class PathUserpathinteraction(models.Model):
    duration_ms = models.FloatField()
    outcome = models.CharField(max_length=10)
    path = models.ForeignKey(PathPath, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'path_userpathinteraction'


class PathUserpathscore(models.Model):
    score = models.FloatField()
    path = models.ForeignKey(PathPath, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'path_userpathscore'
        unique_together = (('user', 'path'),)


class PathUserpathstate(models.Model):
    state = models.CharField(max_length=10)
    path = models.ForeignKey(PathPath, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    liked = models.BooleanField()
    order = models.IntegerField()
    is_added_by_admin = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'path_userpathstate'
        unique_together = (('user', 'path'),)


class PathUserpathstepfeedback(models.Model):
    rating = models.IntegerField()
    text = models.TextField()
    step = models.ForeignKey(PathPathstep, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'path_userpathstepfeedback'
# Unable to inspect table 'path_viewedplans'
# The error was: permission denied for table path_viewedplans


class QuestionnaireAvailableanswer(models.Model):
    text = models.TextField()
    question = models.ForeignKey('QuestionnaireQuestion', models.DO_NOTHING)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'questionnaire_availableanswer'


class QuestionnairePathexclusion(models.Model):
    path = models.ForeignKey(PathPath, models.DO_NOTHING, blank=True, null=True)
    path_filter = models.ForeignKey('QuestionnairePathfilter', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questionnaire_pathexclusion'


class QuestionnairePathfilter(models.Model):
    available_answer = models.ForeignKey(QuestionnaireAvailableanswer, models.DO_NOTHING, blank=True, null=True)
    condition = models.CharField(max_length=50, blank=True, null=True)
    condition_value = models.IntegerField(blank=True, null=True)
    question = models.ForeignKey('QuestionnaireQuestion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questionnaire_pathfilter'


class QuestionnaireQuestion(models.Model):
    text = models.TextField()
    answer_type = models.CharField(max_length=20)
    order = models.IntegerField()
    reverse_scored = models.BooleanField()
    category = models.ForeignKey('QuestionnaireQuestioncategory', models.DO_NOTHING, blank=True, null=True)
    label = models.ForeignKey('QuestionnaireQuestionlabel', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=30)
    created_by = models.ForeignKey(AccountUser, models.DO_NOTHING, blank=True, null=True)
    is_delete = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'questionnaire_question'
# Unable to inspect table 'questionnaire_question_question_to_university'
# The error was: permission denied for table questionnaire_question_question_to_university


class QuestionnaireQuestionShowAnswer(models.Model):
    question = models.ForeignKey(QuestionnaireQuestion, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questionnaire_question_show_answer'
        unique_together = (('question', 'user'),)


class QuestionnaireQuestioncategory(models.Model):
    category = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'questionnaire_questioncategory'


class QuestionnaireQuestioncondition(models.Model):
    answer = models.ForeignKey(QuestionnaireAvailableanswer, models.DO_NOTHING)
    question = models.ForeignKey(QuestionnaireQuestion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questionnaire_questioncondition'


class QuestionnaireQuestionlabel(models.Model):
    label = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'questionnaire_questionlabel'
# Unable to inspect table 'questionnaire_questionnotification'
# The error was: permission denied for table questionnaire_questionnotification


class QuestionnaireSlideranswer(models.Model):
    position = models.TextField()
    text = models.TextField(blank=True, null=True)
    numeric_value = models.IntegerField(blank=True, null=True)
    question = models.ForeignKey(QuestionnaireQuestion, models.DO_NOTHING)
    hex_color = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'questionnaire_slideranswer'


class QuestionnaireSliderdisplayedtext(models.Model):
    text = models.CharField(max_length=100)
    order = models.IntegerField()
    question = models.ForeignKey(QuestionnaireQuestion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questionnaire_sliderdisplayedtext'


class QuestionnaireTextsuggestion(models.Model):
    text = models.CharField(max_length=100)
    question = models.ForeignKey(QuestionnaireQuestion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questionnaire_textsuggestion'
        unique_together = (('question', 'text'),)


class QuestionnaireUseranswer(models.Model):
    text_answer = models.TextField(blank=True, null=True)
    slider_answer = models.IntegerField(blank=True, null=True)
    numeric_answer = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    choice_answer = models.ForeignKey(QuestionnaireAvailableanswer, models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey(QuestionnaireQuestion, models.DO_NOTHING)
    user = models.ForeignKey(AccountUser, models.DO_NOTHING)
    reactions_ms = models.FloatField()
    question_group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'questionnaire_useranswer'


class QuestionnaireUseranswerMultipleAnswers(models.Model):
    useranswer = models.ForeignKey(QuestionnaireUseranswer, models.DO_NOTHING)
    availableanswer = models.ForeignKey(QuestionnaireAvailableanswer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questionnaire_useranswer_multiple_answers'
        unique_together = (('useranswer', 'availableanswer'),)
