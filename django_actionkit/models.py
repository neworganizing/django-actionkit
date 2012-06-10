# Originally based on models by We Also Walk Dogs (http://actionkit.com/) pulled in via django's inspectdb
# Cleaned up using refactoring code built by Citizen Engagement Lab (http://engagementlab.org/, http://code.engagementlab.org/)

from django.db import models
from django_actionkit.managers import akit_manager, akitdb_manager
        
class _akit_model(models.Model):
    """
        The ActionKit DB is read only, we need to use the XML-RPC and/or REST interface to do anything
        Eventually we should replicate these functions using the API.
    """
    
    #akit = akit_manager()
    #objects = akitdb_manager()
    
    class Meta:
        abstract = True
            

class AuthGroup(_akit_model):
    name = models.CharField(max_length=240, unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'auth_group'

class AuthGroupPermissions(_akit_model):
    group = models.ForeignKey('AuthGroup', unique=True)
    permission = models.ForeignKey('AuthPermission')
    class Meta(_akit_model.Meta):
        db_table = u'auth_group_permissions'

class AuthMessage(_akit_model):
    user = models.ForeignKey('AuthUser')
    message = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'auth_message'

class AuthPermission(_akit_model):
    name = models.CharField(max_length=150)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=300, unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'auth_permission'

class AuthUser(_akit_model):
    username = models.CharField(max_length=90, unique=True)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'auth_user'

class AuthUserGroups(_akit_model):
    user = models.ForeignKey('AuthUser', unique=True)
    group = models.ForeignKey('AuthGroup')
    class Meta(_akit_model.Meta):
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(_akit_model):
    user = models.ForeignKey('AuthUser', unique=True)
    permission = models.ForeignKey('AuthPermission')
    class Meta(_akit_model.Meta):
        db_table = u'auth_user_user_permissions'

class AxesAccessattempt(_akit_model):
    user_agent = models.CharField(max_length=765)
    ip_address = models.CharField(max_length=45)
    get_data = models.TextField()
    post_data = models.TextField()
    http_accept = models.CharField(max_length=765)
    path_info = models.CharField(max_length=765)
    failures_since_start = models.IntegerField()
    attempt_time = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'axes_accessattempt'

class Cache(_akit_model):
    cache_key = models.CharField(max_length=765, primary_key=True)
    value = models.TextField()
    expires = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'cache'

class CeleryTaskmeta(_akit_model):
    task_id = models.CharField(max_length=765, unique=True)
    status = models.CharField(max_length=150)
    result = models.TextField(blank=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'celery_taskmeta'

class CeleryTasksetmeta(_akit_model):
    taskset_id = models.CharField(max_length=765, unique=True)
    result = models.TextField(blank=True)
    date_done = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'celery_tasksetmeta'

class CmsCallForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    introduction_text = models.TextField()
    script_text = models.TextField()
    survey_question_text = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_call_form'

class CmsCannedletter(_akit_model):
    lte_form = models.ForeignKey('CmsLteForm')
    subject = models.CharField(max_length=240)
    letter_text = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_cannedletter'

class CmsDonationForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    ask_text = models.TextField()
    is_recurring = models.IntegerField()
    show_other_amount = models.IntegerField()
    amount_order = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'cms_donation_form'

class CmsDonationamount(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_default = models.IntegerField()
    amount = models.CharField(max_length=30)
    donation_form = models.ForeignKey('CmsDonationForm')
    class Meta(_akit_model.Meta):
        db_table = u'cms_donationamount'

class CmsEventCreateForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    ground_rules = models.TextField()
    host_requirements = models.TextField()
    host_text = models.TextField()
    custom_field_html = models.TextField()
    tools_text = models.TextField()
    tools_sidebar = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_event_create_form'

class CmsEventSignupForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    ground_rules = models.TextField()
    search_page_text = models.TextField()
    signup_text = models.TextField()
    custom_field_html = models.TextField()
    tools_text = models.TextField()
    tools_sidebar = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_event_signup_form'

class CmsLetterForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    statement_leadin = models.TextField()
    letter_text = models.TextField()
    about_text = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_letter_form'

class CmsLteForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    introduction_text = models.TextField()
    talking_points = models.TextField()
    writing_tips = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_lte_form'

class CmsPetitionForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    statement_leadin = models.TextField()
    statement_text = models.TextField()
    about_text = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_petition_form'

class CmsRecurringdonationForm(_akit_model):
    donationform_ptr = models.ForeignKey('CmsDonationForm', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'cms_recurringdonation_form'

class CmsRecurringdonationcancelForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    please_stay_text = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_recurringdonationcancel_form'

class CmsRecurringdonationupdateForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    update_card_text = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_recurringdonationupdate_form'

class CmsSignupForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    introduction_text = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_signup_form'

class CmsSurveyForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    introduction_text = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_survey_form'

class CmsSurveyQuestion(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    question_label = models.TextField()
    question_html = models.TextField()
    survey_form = models.ForeignKey('CmsSurveyForm')
    class Meta(_akit_model.Meta):
        db_table = u'cms_survey_question'

class CmsTemplate(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    filename = models.CharField(max_length=765)
    code = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    code_hash = models.CharField(max_length=192)
    class Meta(_akit_model.Meta):
        db_table = u'cms_template'

class CmsTemplatecode(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    code_hash = models.CharField(max_length=192)
    code = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_templatecode'

class CmsTemplatehistory(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    templateset = models.ForeignKey('CmsTemplateset')
    filename = models.CharField(max_length=765)
    code_hash = models.CharField(max_length=192)
    user_name = models.CharField(max_length=192, blank=True)
    edit_type = models.CharField(max_length=192, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'cms_templatehistory'

class CmsTemplateset(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    description = models.CharField(max_length=765)
    editable = models.IntegerField()
    lang = models.ForeignKey('CoreLanguage', null=True, blank=True)
    is_default = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_templateset'

class CmsUnsubscribeForm(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    thank_you_text = models.TextField()
    templateset = models.ForeignKey('CmsTemplateset')
    page = models.ForeignKey('CorePage', unique=True)
    client_hosted = models.IntegerField()
    client_url = models.CharField(max_length=765)
    introduction_text = models.TextField()
    survey_question_text = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_unsubscribe_form'

class CmsUploadedfile(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    bucket = models.CharField(max_length=765)
    directory = models.CharField(max_length=765)
    filename = models.CharField(max_length=765)
    url = models.CharField(max_length=765, unique=True)
    etag = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'cms_uploadedfile'

class CoreAction(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('CoreUser')
    mailing = models.ForeignKey('CoreMailing', null=True, blank=True)
    page = models.ForeignKey('CorePage')
    link = models.IntegerField(null=True, blank=True)
    source = models.CharField(max_length=765)
    opq_id = models.CharField(max_length=765)
    created_user = models.IntegerField()
    subscribed_user = models.IntegerField()
    referring_user = models.ForeignKey('CoreUser', null=True, blank=True)
    referring_mailing = models.ForeignKey('CoreMailing', null=True, blank=True)
    taf_emails_sent = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=765)
    
    def fields(self):
        return CoreActionfield.objects.filter(parent_id=self)
    
    class Meta(_akit_model.Meta):
        db_table = u'core_action'

class CoreActionfield(_akit_model):
    parent = models.ForeignKey('CoreAction')
    name = models.CharField(max_length=765)
    value = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_actionfield'

class CoreActionnotification(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765)
    to = models.CharField(max_length=765, blank=True)
    from_line = models.ForeignKey('CoreFromline', null=True, blank=True)
    custom_from = models.CharField(max_length=765)
    subject = models.CharField(max_length=765)
    wrapper = models.ForeignKey('CoreEmailwrapper', null=True, blank=True)
    body = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_actionnotification'

class CoreActionnotificationToStaff(_akit_model):
    actionnotification = models.ForeignKey('CoreActionnotification', unique=True)
    user = models.ForeignKey('AuthUser')
    class Meta(_akit_model.Meta):
        db_table = u'core_actionnotification_to_staff'

class CoreActivityleveltargetingoption(_akit_model):
    code = models.CharField(max_length=765)
    description = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_activityleveltargetingoption'

class CoreAdminprefs(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', unique=True)
    content_type = models.ForeignKey('DjangoContentType')
    ordering = models.CharField(max_length=765, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_adminprefs'

class CoreAllowedpagefield(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, primary_key=True)
    always_show = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_allowedpagefield'

class CoreAlloweduserfield(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, primary_key=True)
    always_show = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_alloweduserfield'

class CoreAuthnettransactionlog(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    source = models.CharField(max_length=765)
    raw = models.TextField()
    processed = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_authnettransactionlog'

class CoreBackgroundtask(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    message = models.TextField()
    details = models.TextField()
    params = models.TextField()
    error = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_backgroundtask'

class CoreBackgroundtaskdetail(_akit_model):
    task = models.ForeignKey('CoreBackgroundtask')
    row = models.IntegerField()
    details = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_backgroundtaskdetail'

class CoreBlockedEmail(_akit_model):
    mailing_id = models.IntegerField(unique=True)
    user_id = models.IntegerField(unique=True)
    code = models.IntegerField()
    timestamp = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'core_blocked_email'

class CoreBounce(_akit_model):
    user_id = models.IntegerField(unique=True)
    mailing_id = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField()
    action_id = models.IntegerField(null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_bounce'

class CoreBounceState(_akit_model):
    bounce_id = models.IntegerField(primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_bounce_state'

class CoreBuiltintranslation(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    iso_code = models.CharField(max_length=30)
    translations = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_builtintranslation'

class CoreCallaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_callaction'

class CoreCallactionChecked(_akit_model):
    callaction = models.ForeignKey('CoreCallaction', unique=True)
    target = models.ForeignKey('CoreTarget')
    class Meta(_akit_model.Meta):
        db_table = u'core_callaction_checked'

class CoreCallactionTargeted(_akit_model):
    callaction = models.ForeignKey('CoreCallaction', unique=True)
    target = models.ForeignKey('CoreTarget')
    class Meta(_akit_model.Meta):
        db_table = u'core_callaction_targeted'

class CoreCallpage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    constituents_only_url = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_callpage'

class CoreCallpageTargetGroups(_akit_model):
    callpage = models.ForeignKey('CoreCallpage', unique=True)
    targetgroup = models.ForeignKey('CoreTargetgroup')
    class Meta(_akit_model.Meta):
        db_table = u'core_callpage_target_groups'

class CoreCandidate(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    portrait_url = models.CharField(max_length=765)
    description = models.TextField()
    status = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_candidate'

class CoreCandidateTags(_akit_model):
    candidate = models.ForeignKey('CoreCandidate', unique=True)
    tag = models.ForeignKey('CoreTag')
    class Meta(_akit_model.Meta):
        db_table = u'core_candidate_tags'

class CoreClick(_akit_model):
    clickurl_id = models.IntegerField()
    user_id = models.IntegerField(null=True, blank=True)
    mailing_id = models.IntegerField(null=True, blank=True)
    link_number = models.IntegerField(null=True, blank=True)
    source = models.CharField(max_length=765, blank=True)
    referring_user_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'core_click'

class CoreClickurl(_akit_model):
    url = models.CharField(max_length=765, unique=True)
    page = models.ForeignKey('CorePage', null=True, blank=True)
    created_at = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'core_clickurl'

class CoreClientdomain(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    domain = models.CharField(max_length=765, unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_clientdomain'

class CoreCongresstargetgroup(_akit_model):
    targetgroup_ptr = models.ForeignKey('CoreTargetgroup', primary_key=True)
    include_republicans = models.IntegerField()
    include_democrats = models.IntegerField()
    include_independents = models.IntegerField()
    states = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_congresstargetgroup'

class CoreCongresstargetgroupExcludes(_akit_model):
    congresstargetgroup = models.ForeignKey('CoreCongresstargetgroup', unique=True)
    target = models.ForeignKey('CoreTarget')
    class Meta(_akit_model.Meta):
        db_table = u'core_congresstargetgroup_excludes'

class CoreCongresstargetgroupTargets(_akit_model):
    congresstargetgroup = models.ForeignKey('CoreCongresstargetgroup', unique=True)
    target = models.ForeignKey('CoreTarget')
    class Meta(_akit_model.Meta):
        db_table = u'core_congresstargetgroup_targets'

class CoreDonationHpcRule(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    which_amount = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_donation_hpc_rule'

class CoreDonationHpcRuleCondition(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    rule = models.ForeignKey('CoreDonationHpcRule')
    threshold = models.CharField(max_length=30)
    ask = models.CharField(max_length=30)
    class Meta(_akit_model.Meta):
        db_table = u'core_donation_hpc_rule_condition'

class CoreDonationHpcRuleExcludeTags(_akit_model):
    donationhpcrule = models.ForeignKey('CoreDonationHpcRule', unique=True)
    tag = models.ForeignKey('CoreTag')
    class Meta(_akit_model.Meta):
        db_table = u'core_donation_hpc_rule_exclude_tags'

class CoreDonationaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_donationaction'

class CoreDonationcancellationaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_donationcancellationaction'

class CoreDonationcancellationpage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_donationcancellationpage'

class CoreDonationpage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    minimum_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_account = models.CharField(max_length=765)
    hpc_rule = models.ForeignKey('CoreDonationHpcRule', null=True, blank=True)
    allow_international = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_donationpage'

class CoreDonationpageCandidates(_akit_model):
    donationpage = models.ForeignKey('CoreDonationpage', unique=True)
    candidate = models.ForeignKey('CoreCandidate')
    class Meta(_akit_model.Meta):
        db_table = u'core_donationpage_candidates'

class CoreDonationpageProducts(_akit_model):
    donationpage = models.ForeignKey('CoreDonationpage', unique=True)
    product = models.ForeignKey('CoreProduct')
    class Meta(_akit_model.Meta):
        db_table = u'core_donationpage_products'

class CoreDonationupdateaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_donationupdateaction'

class CoreDonationupdatepage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_donationupdatepage'

class CoreEmailtemplate(_akit_model):
    name = models.CharField(max_length=765, unique=True)
    wrapper = models.ForeignKey('CoreEmailwrapper')
    from_line = models.CharField(max_length=765)
    subject = models.CharField(max_length=765)
    template = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_emailtemplate'

class CoreEmailwrapper(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    template = models.TextField()
    text_template = models.TextField()
    unsubscribe_text = models.TextField()
    unsubscribe_html = models.TextField()
    is_default = models.IntegerField(null=True, blank=True)
    lang = models.ForeignKey('CoreLanguage', null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_emailwrapper'

class CoreEventcreateaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    event = models.ForeignKey('EventsEvent')
    class Meta(_akit_model.Meta):
        db_table = u'core_eventcreateaction'

class CoreEventcreatepage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    campaign = models.ForeignKey('EventsCampaign')
    campaign_title = models.CharField(max_length=765, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_eventcreatepage'

class CoreEventsignupaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    signup = models.ForeignKey('EventsEventsignup')
    class Meta(_akit_model.Meta):
        db_table = u'core_eventsignupaction'

class CoreEventsignuppage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    campaign = models.ForeignKey('EventsCampaign')
    class Meta(_akit_model.Meta):
        db_table = u'core_eventsignuppage'

class CoreFormfield(_akit_model):
    name = models.CharField(max_length=765, unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_formfield'

class CoreFromline(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    from_line = models.CharField(max_length=765, unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_fromline'

class CoreHostingplatform(_akit_model):
    name = models.CharField(max_length=765, unique=True)
    after_basics_redirect_url = models.CharField(max_length=765)
    after_basics_redirect_name = models.CharField(max_length=765)
    end_redirect_url = models.CharField(max_length=765)
    end_redirect_name = models.CharField(max_length=765)
    after_action_redirect_url = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_hostingplatform'

class CoreImportaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_importaction'

class CoreImportpage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    subscribe = models.IntegerField()
    default_source = models.CharField(max_length=765, blank=True)
    unsubscribe_all = models.IntegerField(null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_importpage'

class CoreLanguage(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    translations = models.TextField()
    iso_code = models.CharField(max_length=30, blank=True)
    inherit_from_id = models.IntegerField(null=True, blank=True)
    ordering = models.IntegerField(null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_language'

class CoreLetteraction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_letteraction'

class CoreLetteractionTargeted(_akit_model):
    letteraction = models.ForeignKey('CoreLetteraction', unique=True)
    target = models.ForeignKey('CoreTarget')
    class Meta(_akit_model.Meta):
        db_table = u'core_letteraction_targeted'

class CoreLetterpage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    send_immediate_fax = models.IntegerField()
    send_immediate_email = models.IntegerField()
    immediate_email_subject = models.CharField(max_length=765)
    delivery_template = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_letterpage'

class CoreLetterpageTargetGroups(_akit_model):
    letterpage = models.ForeignKey('CoreLetterpage', unique=True)
    targetgroup = models.ForeignKey('CoreTargetgroup')
    class Meta(_akit_model.Meta):
        db_table = u'core_letterpage_target_groups'

class CoreList(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    is_default = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_list'

class CoreLocation(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('CoreUser', primary_key=True)
    us_district = models.CharField(max_length=15)
    us_state_senate = models.CharField(max_length=18)
    us_state_district = models.CharField(max_length=18)
    us_county = models.CharField(max_length=765)
    loc_code = models.CharField(max_length=90, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    country_code = models.CharField(max_length=6, blank=True)
    region_code = models.CharField(max_length=60, blank=True)
    lat_lon_precision = models.CharField(max_length=96, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_location'

class CoreLteaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    subject = models.CharField(max_length=240)
    letter_text = models.TextField()
    target = models.ForeignKey('CoreMediatarget', null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_lteaction'

class CoreLtepage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    national_newspapers = models.IntegerField()
    regional_newspapers = models.IntegerField()
    local_newspapers = models.IntegerField()
    show_phones = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_ltepage'

class CoreMailing(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    fromline = models.ForeignKey('CoreFromline', null=True, blank=True)
    custom_fromline = models.CharField(max_length=765)
    reply_to = models.CharField(max_length=765, blank=True)
    notes = models.CharField(max_length=765, blank=True)
    html = models.TextField(blank=True)
    text = models.TextField(blank=True)
    lang = models.ForeignKey('CoreLanguage', null=True, blank=True)
    emailwrapper = models.ForeignKey('CoreEmailwrapper', null=True, blank=True)
    landing_page = models.ForeignKey('CorePage', null=True, blank=True)
    target_group_from_landing_page = models.IntegerField()
    winning_subject = models.ForeignKey('CoreMailingsubject', null=True, blank=True)
    requested_proofs = models.IntegerField(null=True, blank=True)
    submitter = models.ForeignKey('AuthUser', null=True, blank=True)
    scheduled_for = models.DateTimeField(null=True, blank=True)
    scheduled_by = models.ForeignKey('AuthUser', null=True, blank=True)
    queue_task_id = models.CharField(max_length=765, blank=True)
    queued_at = models.DateTimeField(null=True, blank=True)
    queued_by = models.ForeignKey('AuthUser', null=True, blank=True)
    expected_send_count = models.IntegerField(null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    query_started_at = models.DateTimeField(null=True, blank=True)
    query_completed_at = models.DateTimeField(null=True, blank=True)
    query_status = models.CharField(max_length=765, blank=True)
    query_task_id = models.CharField(max_length=765, blank=True)
    targeting_version = models.IntegerField(null=True, blank=True)
    targeting_version_saved = models.IntegerField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    progress = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=765, blank=True)
    includes = models.ForeignKey('CoreMailingtargeting', null=True, blank=True)
    excludes = models.ForeignKey('CoreMailingtargeting', null=True, blank=True)
    limit = models.IntegerField(null=True, blank=True)
    sort_by = models.CharField(max_length=96, blank=True)
    pid = models.IntegerField(null=True, blank=True)
    sent_proofs = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_mailing'

class CoreMailingReviewers(_akit_model):
    mailing = models.ForeignKey('CoreMailing', unique=True)
    user = models.ForeignKey('CoreUser')
    class Meta(_akit_model.Meta):
        db_table = u'core_mailing_reviewers'

class CoreMailingTags(_akit_model):
    mailing = models.ForeignKey('CoreMailing', unique=True)
    tag = models.ForeignKey('CoreTag')
    class Meta(_akit_model.Meta):
        db_table = u'core_mailing_tags'

class CoreMailingerror(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    mailing = models.ForeignKey('CoreMailing')
    queue_task_id = models.CharField(max_length=765)
    traceback = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_mailingerror'

class CoreMailinghaiku(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    text = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_mailinghaiku'

class CoreMailingsubject(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    text = models.CharField(max_length=765)

    class Meta(_akit_model.Meta):
        db_table = u'core_mailingsubject'

class CoreMailingtargeting(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    states = models.TextField(blank=True)
    cds = models.TextField(blank=True)
    state_senate_districts = models.TextField(blank=True)
    state_house_districts = models.TextField(blank=True)
    zips = models.TextField(blank=True)
    zip_radius = models.IntegerField(null=True, blank=True)
    counties = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    has_donated = models.IntegerField()
    is_monthly_donor = models.IntegerField()
    activity_level = models.ForeignKey('CoreActivityleveltargetingoption', null=True, blank=True)
    raw_sql = models.TextField(blank=True)
    is_delivery = models.IntegerField()
    delivery_job = models.ForeignKey('CorePetitiondeliveryjob', null=True, blank=True)
    campaign_radius = models.IntegerField(null=True, blank=True)
    countries = models.TextField(blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_mailingtargeting'

class CoreMailingtargetingActions(_akit_model):
    mailingtargeting = models.ForeignKey('CoreMailingtargeting', unique=True)
    page = models.ForeignKey('CorePage')
    class Meta(_akit_model.Meta):
        db_table = u'core_mailingtargeting_actions'

class CoreMailingtargetingCampaigns(_akit_model):
    mailingtargeting = models.ForeignKey('CoreMailingtargeting', unique=True)
    campaign = models.ForeignKey('EventsCampaign')
    class Meta(_akit_model.Meta):
        db_table = u'core_mailingtargeting_campaigns'

class CoreMailingtargetingLanguages(_akit_model):
    mailingtargeting = models.ForeignKey('CoreMailingtargeting', unique=True)
    language = models.ForeignKey('CoreLanguage')
    class Meta(_akit_model.Meta):
        db_table = u'core_mailingtargeting_languages'

class CoreMailingtargetingLists(_akit_model):
    mailingtargeting = models.ForeignKey('CoreMailingtargeting', unique=True)
    list = models.ForeignKey('CoreList')
    class Meta(_akit_model.Meta):
        db_table = u'core_mailingtargeting_lists'

class CoreMailingtargetingMailings(_akit_model):
    mailingtargeting = models.ForeignKey('CoreMailingtargeting', unique=True)
    mailing = models.ForeignKey('CoreMailing')
    class Meta(_akit_model.Meta):
        db_table = u'core_mailingtargeting_mailings'

class CoreMailingtargetingTargetGroups(_akit_model):
    mailingtargeting = models.ForeignKey('CoreMailingtargeting', unique=True)
    congresstargetgroup = models.ForeignKey('CoreCongresstargetgroup')
    class Meta(_akit_model.Meta):
        db_table = u'core_mailingtargeting_target_groups'

class CoreMailingtargetingUsers(_akit_model):
    mailingtargeting = models.ForeignKey('CoreMailingtargeting', unique=True)
    user = models.ForeignKey('CoreUser')
    class Meta(_akit_model.Meta):
        db_table = u'core_mailingtargeting_users'

class CoreMailingtargetingWasMonthlyDonor(_akit_model):
    mailingtargeting = models.ForeignKey('CoreMailingtargeting', unique=True)
    recurringdonortargetingoption = models.ForeignKey('CoreRecurringdonortargetingoption')
    class Meta(_akit_model.Meta):
        db_table = u'core_mailingtargeting_was_monthly_donor'

class CoreMediatarget(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    address1 = models.CharField(max_length=765)
    address2 = models.CharField(max_length=765)
    city = models.CharField(max_length=765)
    state = models.CharField(max_length=765)
    region = models.CharField(max_length=765)
    postal = models.CharField(max_length=765)
    zip = models.CharField(max_length=15)
    plus4 = models.CharField(max_length=12)
    country = models.CharField(max_length=765)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    orgid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=765)
    phone = models.CharField(max_length=765, blank=True)
    fax = models.CharField(max_length=765, blank=True)
    email_address = models.CharField(max_length=765, blank=True)
    website_url = models.CharField(max_length=765, blank=True)
    circulation = models.IntegerField(null=True, blank=True)
    frequency = models.CharField(max_length=108, blank=True)
    language = models.CharField(max_length=192, blank=True)
    levelcode = models.CharField(max_length=192, blank=True)
    dmacode = models.CharField(max_length=30, blank=True)
    fipscode = models.IntegerField(null=True, blank=True)
    msacode = models.IntegerField(null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_mediatarget'

class CoreMessage(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('CoreUser')
    message = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_message'

class CoreMultilingualcampaign(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_multilingualcampaign'

class CoreOpen(_akit_model):
    user_id = models.IntegerField(null=True, blank=True)
    mailing_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'core_open'

class CoreOrder(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    action = models.ForeignKey('CoreAction')
    user = models.ForeignKey('CoreUser')
    user_detail = models.ForeignKey('CoreOrderUserDetail')
    card_num_last_four = models.CharField(max_length=12)
    shipping_address = models.ForeignKey('CoreOrderShippingAddress', null=True, blank=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=765)
    import_id = models.CharField(max_length=96, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_order'

class CoreOrderDetail(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    order = models.ForeignKey('CoreOrder')
    product = models.ForeignKey('CoreProduct', null=True, blank=True)
    candidate = models.ForeignKey('CoreCandidate', null=True, blank=True)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    class Meta(_akit_model.Meta):
        db_table = u'core_order_detail'

class CoreOrderShippingAddress(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    address1 = models.CharField(max_length=765)
    address2 = models.CharField(max_length=765)
    city = models.CharField(max_length=765)
    state = models.CharField(max_length=765)
    region = models.CharField(max_length=765)
    postal = models.CharField(max_length=765)
    zip = models.CharField(max_length=15)
    plus4 = models.CharField(max_length=12)
    country = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_order_shipping_address'

class CoreOrderUserDetail(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    email = models.CharField(max_length=765)
    prefix = models.CharField(max_length=765)
    first_name = models.CharField(max_length=765)
    middle_name = models.CharField(max_length=765)
    last_name = models.CharField(max_length=765)
    suffix = models.CharField(max_length=765)
    address1 = models.CharField(max_length=765)
    address2 = models.CharField(max_length=765)
    city = models.CharField(max_length=765)
    state = models.CharField(max_length=765)
    region = models.CharField(max_length=765)
    postal = models.CharField(max_length=765)
    zip = models.CharField(max_length=15)
    plus4 = models.CharField(max_length=12)
    country = models.CharField(max_length=765)
    source = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_order_user_detail'

class CoreOrderrecurring(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    order = models.ForeignKey('CoreOrder')
    action = models.ForeignKey('CoreAction')
    exp_date = models.CharField(max_length=18)
    card_num = models.CharField(max_length=12)
    recurring_id = models.CharField(max_length=765, blank=True)
    account = models.CharField(max_length=765, blank=True)
    user = models.ForeignKey('CoreUser')
    start = models.DateField()
    occurrences = models.IntegerField(null=True, blank=True)
    period = models.CharField(max_length=765)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_orderrecurring'

class CorePage(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    title = models.CharField(max_length=765)
    name = models.CharField(max_length=765, unique=True)
    hosted_with = models.ForeignKey('CoreHostingplatform')
    url = models.CharField(max_length=765)
    type = models.CharField(max_length=765)
    lang = models.ForeignKey('CoreLanguage', null=True, blank=True)
    multilingual_campaign = models.ForeignKey('CoreMultilingualcampaign', null=True, blank=True)
    goal = models.IntegerField(null=True, blank=True)
    goal_type = models.CharField(max_length=765)
    status = models.CharField(max_length=765)
    list = models.ForeignKey('CoreList')

    def fields(self):
        return CorePagefield.objects.filter(parent_id=self)
    
    def __unicode__(self):
        return self.name

    class Meta(_akit_model.Meta):
        db_table = u'core_page'

class CorePageRequiredFields(_akit_model):
    page = models.ForeignKey('CorePage', unique=True)
    formfield = models.ForeignKey('CoreFormfield')
    class Meta(_akit_model.Meta):
        db_table = u'core_page_required_fields'

class CorePageTags(_akit_model):
    page = models.ForeignKey('CorePage', unique=True)
    tag = models.ForeignKey('CoreTag')
    class Meta(_akit_model.Meta):
        db_table = u'core_page_tags'

class CorePagefield(_akit_model):
    parent = models.ForeignKey('CorePage')
    name = models.ForeignKey('CoreAllowedpagefield', db_column='name')
    value = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_pagefield'

class CorePagefollowup(_akit_model):
    page = models.ForeignKey('CorePage', unique=True)
    send_email = models.IntegerField()
    url = models.CharField(max_length=765)
    email_wrapper = models.ForeignKey('CoreEmailwrapper', null=True, blank=True)
    email_from_line = models.ForeignKey('CoreFromline', null=True, blank=True)
    email_custom_from = models.CharField(max_length=765)
    email_subject = models.CharField(max_length=765)
    email_body = models.TextField()
    send_taf = models.IntegerField()
    taf_subject = models.CharField(max_length=765)
    taf_body = models.TextField()
    send_notifications = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_pagefollowup'

class CorePagefollowupNotifications(_akit_model):
    pagefollowup = models.ForeignKey('CorePagefollowup', unique=True)
    actionnotification = models.ForeignKey('CoreActionnotification')
    class Meta(_akit_model.Meta):
        db_table = u'core_pagefollowup_notifications'

class CorePagetargetchange(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    page = models.ForeignKey('CorePage', unique=True)
    targets_representation = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_pagetargetchange'

class CorePetitionaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_petitionaction'

class CorePetitionactionTargeted(_akit_model):
    petitionaction = models.ForeignKey('CorePetitionaction', unique=True)
    target = models.ForeignKey('CoreTarget')
    class Meta(_akit_model.Meta):
        db_table = u'core_petitionaction_targeted'

class CorePetitiondeliveryjob(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    single_file = models.IntegerField()
    cover_html = models.TextField()
    print_template = models.ForeignKey('CorePrinttemplate')
    allow_pdf_download = models.IntegerField()
    allow_csv_download = models.IntegerField()
    include_email_in_csv = models.IntegerField()
    template_set = models.ForeignKey('CmsTemplateset', null=True, blank=True)
    limit_delivery = models.IntegerField()
    all_to_all = models.IntegerField()
    header_content = models.TextField()
    footer_content = models.TextField()
    backgroundtask = models.ForeignKey('CoreBackgroundtask', unique=True, null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_petitiondeliveryjob'

class CorePetitiondeliveryjobPetitions(_akit_model):
    petitiondeliveryjob = models.ForeignKey('CorePetitiondeliveryjob', unique=True)
    page = models.ForeignKey('CorePage')
    class Meta(_akit_model.Meta):
        db_table = u'core_petitiondeliveryjob_petitions'

class CorePetitiondeliveryjobTargetGroups(_akit_model):
    petitiondeliveryjob = models.ForeignKey('CorePetitiondeliveryjob', unique=True)
    targetgroup = models.ForeignKey('CoreTargetgroup')
    class Meta(_akit_model.Meta):
        db_table = u'core_petitiondeliveryjob_target_groups'

class CorePetitionpage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    send_immediate_fax = models.IntegerField()
    send_immediate_email = models.IntegerField()
    immediate_email_subject = models.CharField(max_length=765)
    delivery_template = models.TextField()
    one_click = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_petitionpage'

class CorePetitionpageTargetGroups(_akit_model):
    petitionpage = models.ForeignKey('CorePetitionpage', unique=True)
    targetgroup = models.ForeignKey('CoreTargetgroup')
    class Meta(_akit_model.Meta):
        db_table = u'core_petitionpage_target_groups'

class CorePhone(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('CoreUser')
    type = models.CharField(max_length=75, unique=True)
    phone = models.CharField(max_length=75)
    source = models.CharField(max_length=75, unique=True)
    normalized_phone = models.CharField(max_length=75)
    class Meta(_akit_model.Meta):
        db_table = u'core_phone'

class CorePrinttemplate(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    header_html = models.TextField()
    template = models.TextField()
    footer_html = models.TextField()
    font_family = models.CharField(max_length=765)
    font_size = models.FloatField()
    logo_url = models.CharField(max_length=765)
    page_size = models.CharField(max_length=765)
    margin_units = models.CharField(max_length=765)
    margin_top = models.FloatField()
    margin_bottom = models.FloatField()
    margin_left = models.FloatField()
    margin_right = models.FloatField()
    readonly = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_printtemplate'

class CoreProduct(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    shippable = models.IntegerField()
    status = models.CharField(max_length=765)
    maximum_order = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_product'

class CoreProductTags(_akit_model):
    product = models.ForeignKey('CoreProduct', unique=True)
    tag = models.ForeignKey('CoreTag')
    class Meta(_akit_model.Meta):
        db_table = u'core_product_tags'

class CoreRecurringdonationaction(_akit_model):
    donationaction_ptr = models.ForeignKey('CoreDonationaction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_recurringdonationaction'

class CoreRecurringdonationcancelaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_recurringdonationcancelaction'

class CoreRecurringdonationcancelpage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_recurringdonationcancelpage'

class CoreRecurringdonationpage(_akit_model):
    donationpage_ptr = models.ForeignKey('CoreDonationpage', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_recurringdonationpage'

class CoreRecurringdonationupdateaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_recurringdonationupdateaction'

class CoreRecurringdonationupdatepage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    minimum_amount = models.DecimalField(max_digits=12, decimal_places=2)
    class Meta(_akit_model.Meta):
        db_table = u'core_recurringdonationupdatepage'

class CoreRecurringdonortargetingoption(_akit_model):
    code = models.CharField(max_length=765)
    description = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_recurringdonortargetingoption'

class CoreRedirect(_akit_model):
    short_code = models.CharField(max_length=765, unique=True, blank=True)
    url = models.CharField(max_length=12288)
    created_at = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'core_redirect'

class CoreRedirectaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_redirectaction'

class CoreRedirectpage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_redirectpage'

class CoreSavedquerylog(_akit_model):
    mailing = models.ForeignKey('CoreMailing')
    action = models.CharField(max_length=765)
    reason = models.CharField(max_length=765)
    triggered_by = models.ForeignKey('CoreMailing', null=True, blank=True)
    created_at = models.DateTimeField()
    process_id = models.IntegerField(null=True, blank=True)
    targeting_version = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_savedquerylog'

class CoreSentadhocmail(_akit_model):
    template = models.ForeignKey('CoreEmailtemplate')
    user = models.ForeignKey('CoreUser')
    class Meta(_akit_model.Meta):
        db_table = u'core_sentadhocmail'

class CoreSignupaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_signupaction'

class CoreSignuppage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_signuppage'

class CoreSpecialtarget(_akit_model):
    target_ptr = models.ForeignKey('CoreTarget', primary_key=True)
    body = models.ForeignKey('CoreSpecialtargetgroup')
    class Meta(_akit_model.Meta):
        db_table = u'core_specialtarget'

class CoreSpecialtargetgroup(_akit_model):
    targetgroup_ptr = models.ForeignKey('CoreTargetgroup', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_specialtargetgroup'

class CoreSubscription(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('CoreUser')
    list = models.ForeignKey('CoreList')
    class Meta(_akit_model.Meta):
        db_table = u'core_subscription'

class CoreSubscriptionchangetype(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=765, unique=True)
    description = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_subscriptionchangetype'

class CoreSubscriptionhistory(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('CoreUser')
    list = models.ForeignKey('CoreList')
    change = models.ForeignKey('CoreSubscriptionchangetype')
    action = models.ForeignKey('CoreAction', null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_subscriptionhistory'

class CoreSurveyaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_surveyaction'

class CoreSurveypage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_surveypage'

class CoreTag(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    times_used = models.IntegerField(null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_tag'

class CoreTarget(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    type = models.CharField(max_length=765)
    seat = models.CharField(max_length=765)
    country = models.CharField(max_length=765)
    state = models.CharField(max_length=765)
    us_district = models.CharField(max_length=765)
    title = models.CharField(max_length=765)
    long_title = models.CharField(max_length=765)
    first = models.CharField(max_length=765)
    last = models.CharField(max_length=765)
    phone = models.CharField(max_length=765)
    fax = models.CharField(max_length=765)
    email = models.CharField(max_length=765)
    gender = models.CharField(max_length=3)
    party = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_target'

class CoreTargetcontact(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    target = models.ForeignKey('CoreTarget', null=True, blank=True)
    email = models.CharField(max_length=765)
    is_mailable = models.IntegerField()
    is_current = models.IntegerField()
    prefix = models.CharField(max_length=765)
    first_name = models.CharField(max_length=765)
    middle_name = models.CharField(max_length=765)
    last_name = models.CharField(max_length=765)
    suffix = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_targetcontact'

class CoreTargetgroup(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    type = models.CharField(max_length=765)
    readonly = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_targetgroup'

class CoreTargetingqueryreport(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    report = models.ForeignKey('ReportsQueryreport')
    targeting = models.ForeignKey('CoreMailingtargeting')
    class Meta(_akit_model.Meta):
        db_table = u'core_targetingqueryreport'

class CoreTargetingqueryreportparam(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    query = models.ForeignKey('CoreTargetingqueryreport')
    name = models.CharField(max_length=765)
    value = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_targetingqueryreportparam'

class CoreTargetoffice(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    target = models.ForeignKey('CoreTarget')
    type = models.CharField(max_length=765)
    address1 = models.CharField(max_length=765)
    address2 = models.CharField(max_length=765)
    name = models.CharField(max_length=765)
    city = models.CharField(max_length=765)
    state = models.CharField(max_length=765)
    zip = models.CharField(max_length=765)
    phone = models.CharField(max_length=765)
    fax = models.CharField(max_length=765)
    is_current = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_targetoffice'

class CoreTasktrace(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    task_id = models.CharField(max_length=108, unique=True)
    name = models.CharField(max_length=765)
    args = models.TextField()
    status = models.CharField(max_length=765)
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    requesting_machine = models.CharField(max_length=765, blank=True)
    processing_machine = models.CharField(max_length=765, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_tasktrace'

class CoreTimezonepreference(_akit_model):
    tz_name = models.CharField(max_length=192)
    user = models.ForeignKey('AuthUser', unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_timezonepreference'

class CoreTransaction(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type = models.CharField(max_length=765)
    order = models.ForeignKey('CoreOrder')
    account = models.CharField(max_length=765)
    test_mode = models.IntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    success = models.IntegerField()
    status = models.CharField(max_length=765)
    trans_id = models.CharField(max_length=765, blank=True)
    failure_description = models.CharField(max_length=765)
    failure_code = models.CharField(max_length=765, blank=True)
    failure_message = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_transaction'

class CoreUnsubEmail(_akit_model):
    user_id = models.IntegerField(unique=True)
    mailing_id = models.IntegerField(null=True, blank=True)
    action_id = models.IntegerField(unique=True, null=True, blank=True)
    timestamp = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'core_unsub_email'

class CoreUnsubEmailState(_akit_model):
    unsub_email_id = models.IntegerField(primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_unsub_email_state'

class CoreUnsubscribeaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_unsubscribeaction'

class CoreUnsubscribepage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    use_in_mail_wrapper = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_unsubscribepage'

class CoreUpload(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    path = models.CharField(max_length=765)
    submitter = models.ForeignKey('AuthUser', null=True, blank=True)
    page = models.ForeignKey('CorePage')
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    line_count = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=60, blank=True)
    format = models.CharField(max_length=30, blank=True)
    compression = models.CharField(max_length=60, blank=True)
    autocreate_user_fields = models.IntegerField()
    original_header = models.TextField()
    override_header = models.TextField(blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_upload'

class CoreUploaderror(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    upload = models.ForeignKey('CoreUpload')
    worker_pid = models.IntegerField(null=True, blank=True)
    row = models.IntegerField(null=True, blank=True)
    col = models.IntegerField(null=True, blank=True)
    message = models.TextField()
    exception = models.TextField(blank=True)
    value = models.TextField(blank=True)
    raw_row = models.TextField(blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_uploaderror'

class CoreUploadprogress(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    upload = models.ForeignKey('CoreUpload')
    worker_pid = models.IntegerField()
    ok = models.IntegerField()
    warnings = models.IntegerField()
    errors = models.IntegerField()
    rate = models.FloatField(null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_uploadprogress'

class CoreUploadwarning(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    upload = models.ForeignKey('CoreUpload')
    worker_pid = models.IntegerField(null=True, blank=True)
    row = models.IntegerField(null=True, blank=True)
    col = models.IntegerField(null=True, blank=True)
    message = models.TextField()
    exception = models.TextField(blank=True)
    value = models.TextField(blank=True)
    raw_row = models.TextField(blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_uploadwarning'

class CoreUser(_akit_model):
    id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    email = models.CharField(max_length=765, unique=True)
    prefix = models.CharField(max_length=765)
    first_name = models.CharField(max_length=765)
    middle_name = models.CharField(max_length=765)
    last_name = models.CharField(max_length=765)
    suffix = models.CharField(max_length=765)
    password = models.CharField(max_length=765)
    subscription_status = models.CharField(max_length=765)
    address1 = models.CharField(max_length=765)
    address2 = models.CharField(max_length=765)
    city = models.CharField(max_length=765)
    state = models.CharField(max_length=765)
    region = models.CharField(max_length=765)
    postal = models.CharField(max_length=765)
    zip = models.CharField(max_length=15)
    plus4 = models.CharField(max_length=12)
    country = models.CharField(max_length=765)
    source = models.CharField(max_length=765)
    lang = models.ForeignKey('CoreLanguage', null=True, blank=True)
    rand_id = models.IntegerField()
    
    def fields(self):
        return CoreUserfield.objects.select_related().filter(parent_id=self)
    
    def actions(self):
        return CoreAction.objects.select_related().filter(user_id=self)
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    class Meta(_akit_model.Meta):
        db_table = u'core_user'

class CoreUserfield(_akit_model):
    parent = models.ForeignKey('CoreUser')
    name = models.ForeignKey('CoreAlloweduserfield', db_column='name')
    value = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_userfield'

class CoreUsermailing(_akit_model):
    mailing = models.ForeignKey('CoreMailing')
    user = models.ForeignKey('CoreUser')
    subject = models.ForeignKey('CoreMailingsubject', null=True, blank=True)
    created_at = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'core_usermailing'

class CoreUseroriginal(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('CoreUser', primary_key=True)
    address1 = models.CharField(max_length=765)
    address2 = models.CharField(max_length=765)
    city = models.CharField(max_length=765)
    state = models.CharField(max_length=765)
    zip = models.CharField(max_length=765)
    address1_updated_at = models.DateTimeField(null=True, blank=True)
    address2_updated_at = models.DateTimeField(null=True, blank=True)
    city_updated_at = models.DateTimeField(null=True, blank=True)
    state_updated_at = models.DateTimeField(null=True, blank=True)
    zip_updated_at = models.DateTimeField(null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_useroriginal'

class CoreUserupdateaction(_akit_model):
    action_ptr = models.ForeignKey('CoreAction', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_userupdateaction'

class CoreUserupdatepage(_akit_model):
    page_ptr = models.ForeignKey('CorePage', primary_key=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_userupdatepage'

class CoreZp4Queue(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('CoreUser')
    class Meta(_akit_model.Meta):
        db_table = u'core_zp4queue'

class DjangoAdminLog(_akit_model):
    action_time = models.DateTimeField()
    user = models.ForeignKey('AuthUser')
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'django_admin_log'

class DjangoContentType(_akit_model):
    name = models.CharField(max_length=300)
    app_label = models.CharField(max_length=300, unique=True)
    model = models.CharField(max_length=300, unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'django_content_type'

class DjangoSession(_akit_model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta(_akit_model.Meta):
        db_table = u'django_session'

class EventsCampaign(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    title = models.CharField(max_length=765)
    name = models.CharField(max_length=765, unique=True)
    public_create_page = models.IntegerField()
    use_title = models.IntegerField()
    default_title = models.CharField(max_length=765)
    starts_at = models.DateTimeField(null=True, blank=True)
    use_start_date = models.IntegerField()
    use_start_time = models.IntegerField()
    require_staff_approval = models.IntegerField()
    require_email_confirmation = models.IntegerField()
    allow_private = models.IntegerField()
    max_event_size = models.IntegerField(null=True, blank=True)
    default_event_size = models.IntegerField(null=True, blank=True)
    public_search_page = models.IntegerField()
    show_title = models.IntegerField()
    show_venue = models.IntegerField()
    show_address1 = models.IntegerField()
    show_city = models.IntegerField()
    show_state = models.IntegerField()
    show_zip = models.IntegerField()
    show_public_description = models.IntegerField()
    show_directions = models.IntegerField()
    show_attendee_count = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'events_campaign'

class EventsEvent(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    address1 = models.CharField(max_length=765)
    address2 = models.CharField(max_length=765)
    city = models.CharField(max_length=765)
    state = models.CharField(max_length=765)
    region = models.CharField(max_length=765)
    postal = models.CharField(max_length=765)
    zip = models.CharField(max_length=15)
    plus4 = models.CharField(max_length=12)
    country = models.CharField(max_length=765)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    campaign = models.ForeignKey('EventsCampaign')
    title = models.CharField(max_length=765)
    creator = models.ForeignKey('CoreUser')
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=96)
    host_is_confirmed = models.IntegerField()
    is_private = models.IntegerField()
    is_approved = models.IntegerField()
    attendee_count = models.IntegerField()
    max_attendees = models.IntegerField(null=True, blank=True)
    venue = models.CharField(max_length=765)
    phone = models.CharField(max_length=765)
    public_description = models.TextField()
    directions = models.TextField()
    note_to_attendees = models.TextField()
    notes = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'events_event'

class EventsEventfield(_akit_model):
    parent = models.ForeignKey('EventsEvent')
    name = models.CharField(max_length=765)
    value = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'events_eventfield'

class EventsEventsignup(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('CoreUser')
    event = models.ForeignKey('EventsEvent')
    role = models.CharField(max_length=96)
    status = models.CharField(max_length=96)
    page_id = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'events_eventsignup'

class EventsEventsignupfield(_akit_model):
    parent = models.ForeignKey('EventsEventsignup')
    name = models.CharField(max_length=765)
    value = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'events_eventsignupfield'

class ReportsDashboardreport(_akit_model):
    report_ptr = models.ForeignKey('ReportsReport', primary_key=True)
    template = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'reports_dashboardreport'

class ReportsQueryreport(_akit_model):
    report_ptr = models.ForeignKey('ReportsReport', primary_key=True)
    sql = models.TextField()
    display_as = models.ForeignKey('ReportsQuerytemplate')
    email_always_csv = models.IntegerField(null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'reports_queryreport'

class ReportsQuerytemplate(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    template = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'reports_querytemplate'

class ReportsReport(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    short_name = models.CharField(max_length=765, unique=True, blank=True)
    description = models.CharField(max_length=765)
    type = models.CharField(max_length=765)
    run_every = models.CharField(max_length=765)
    to_emails = models.CharField(max_length=765)
    help_text = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'reports_report'

class ReportsReportCategories(_akit_model):
    report = models.ForeignKey('ReportsReport', unique=True)
    reportcategory = models.ForeignKey('ReportsReportcategory')
    class Meta(_akit_model.Meta):
        db_table = u'reports_report_categories'

class ReportsReportcategory(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'reports_reportcategory'