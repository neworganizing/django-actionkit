# Originally based on models by We Also Walk Dogs (http://actionkit.com/) pulled in via django's inspectdb
# Cleaned up using refactoring code built by Citizen Engagement Lab (http://engagementlab.org/, http://code.engagementlab.org/)

from django.db import models
from django_actionkit.managers import akit_manager, akitdb_manager
        
class _akit_model(models.Model):
    """
        The ActionKit DB is read only, we need to use the XML-RPC and/or REST interface to do anything
        Eventually we should replicate these functions using the API. For now we'll just throw a custom exception
    """
    
    #akit = akit_manager()
    #objects = akitdb_manager()
    
    class Meta:
        abstract = True
            

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

class CoreUser(_akit_model):
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
    lang = models.ForeignKey(CoreLanguage, null=True, blank=True)
    rand_id = models.IntegerField()
    
    def fields(self):
        return CoreUserfield.objects.select_related().filter(parent_id=self)
    
    def actions(self):
        return CoreAction.objects.select_related().filter(user_id=self)
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    class Meta(_akit_model.Meta):
        db_table = u'core_user'

class CoreFromline(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    from_line = models.CharField(max_length=765, unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_fromline'

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
    lang = models.ForeignKey(CoreLanguage, null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_emailwrapper'

class CoreHostingplatform(_akit_model):
    name = models.CharField(max_length=765, unique=True)
    after_basics_redirect_url = models.CharField(max_length=765)
    after_basics_redirect_name = models.CharField(max_length=765)
    end_redirect_url = models.CharField(max_length=765)
    end_redirect_name = models.CharField(max_length=765)
    after_action_redirect_url = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_hostingplatform'

class CoreMultilingualcampaign(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_multilingualcampaign'

class CoreList(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    is_default = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_list'

class CorePage(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    title = models.CharField(max_length=765)
    name = models.CharField(max_length=765, unique=True)
    hosted_with = models.ForeignKey(CoreHostingplatform)
    url = models.CharField(max_length=765)
    type = models.CharField(max_length=765)
    lang = models.ForeignKey(CoreLanguage, null=True, blank=True)
    multilingual_campaign = models.ForeignKey(CoreMultilingualcampaign, null=True, blank=True)
    goal = models.IntegerField(null=True, blank=True)
    goal_type = models.CharField(max_length=765)
    status = models.CharField(max_length=765)
    list = models.ForeignKey(CoreList)
    
    def fields(self):
        return CorePagefield.objects.filter(parent_id=self)
    
    def __unicode__(self):
        return self.name
    
    class Meta(_akit_model.Meta):
        db_table = u'core_page'

class CoreMailingsubject(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    text = models.CharField(max_length=765)

    class Meta(_akit_model.Meta):
        db_table = u'core_mailingsubject'

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

class CoreActivityleveltargetingoption(_akit_model):
    code = models.CharField(max_length=765)
    description = models.CharField(max_length=765)
    class Meta(_akit_model.Meta):
        db_table = u'core_activityleveltargetingoption'

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

class CmsTemplateset(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    description = models.CharField(max_length=765)
    editable = models.IntegerField()
    lang = models.ForeignKey(CoreLanguage, null=True, blank=True)
    is_default = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'cms_templateset'

class CoreBackgroundtask(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    message = models.TextField()
    details = models.TextField()
    params = models.TextField()
    error = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_backgroundtask'

class CorePetitiondeliveryjob(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    single_file = models.IntegerField()
    cover_html = models.TextField()
    print_template = models.ForeignKey(CorePrinttemplate)
    allow_pdf_download = models.IntegerField()
    allow_csv_download = models.IntegerField()
    include_email_in_csv = models.IntegerField()
    template_set = models.ForeignKey(CmsTemplateset, null=True, blank=True)
    limit_delivery = models.IntegerField()
    all_to_all = models.IntegerField()
    header_content = models.TextField()
    footer_content = models.TextField()
    backgroundtask = models.ForeignKey(CoreBackgroundtask, unique=True, null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_petitiondeliveryjob'

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
    activity_level = models.ForeignKey(CoreActivityleveltargetingoption, null=True, blank=True)
    raw_sql = models.TextField(blank=True)
    is_delivery = models.IntegerField()
    delivery_job = models.ForeignKey(CorePetitiondeliveryjob, null=True, blank=True)
    campaign_radius = models.IntegerField(null=True, blank=True)
    countries = models.TextField(blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_mailingtargeting'

class CoreMailing(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    fromline = models.ForeignKey(CoreFromline, null=True, blank=True)
    custom_fromline = models.CharField(max_length=765)
    reply_to = models.CharField(max_length=765, blank=True)
    notes = models.CharField(max_length=765, blank=True)
    html = models.TextField(blank=True)
    text = models.TextField(blank=True)
    lang = models.ForeignKey(CoreLanguage, null=True, blank=True)
    emailwrapper = models.ForeignKey(CoreEmailwrapper, null=True, blank=True)
    landing_page = models.ForeignKey(CorePage, null=True, blank=True)
    target_group_from_landing_page = models.IntegerField()
    winning_subject = models.ForeignKey(CoreMailingsubject, null=True, blank=True)
    requested_proofs = models.IntegerField(null=True, blank=True)
    submitter = models.ForeignKey(AuthUser, null=True, blank=True)
    scheduled_for = models.DateTimeField(null=True, blank=True)
    scheduled_by = models.ForeignKey(AuthUser, null=True, blank=True)
    queue_task_id = models.CharField(max_length=765, blank=True)
    queued_at = models.DateTimeField(null=True, blank=True)
    queued_by = models.ForeignKey(AuthUser, null=True, blank=True)
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
    includes = models.ForeignKey(CoreMailingtargeting, null=True, blank=True)
    excludes = models.ForeignKey(CoreMailingtargeting, null=True, blank=True)
    limit = models.IntegerField(null=True, blank=True)
    sort_by = models.CharField(max_length=96, blank=True)
    pid = models.IntegerField(null=True, blank=True)
    sent_proofs = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_mailing'

class CoreAction(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(CoreUser)
    mailing = models.ForeignKey(CoreMailing, null=True, blank=True)
    page = models.ForeignKey(CorePage)
    link = models.IntegerField(null=True, blank=True)
    source = models.CharField(max_length=765)
    opq_id = models.CharField(max_length=765)
    created_user = models.IntegerField()
    subscribed_user = models.IntegerField()
    referring_user = models.ForeignKey(CoreUser, null=True, blank=True)
    referring_mailing = models.ForeignKey(CoreMailing, null=True, blank=True)
    taf_emails_sent = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=765)
    
    def fields(self):
        return CoreActionfield.objects.filter(parent_id=self)
    
    class Meta(_akit_model.Meta):
        db_table = u'core_action'

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

class CoreOrder(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    action = models.ForeignKey(CoreAction)
    user = models.ForeignKey(CoreUser)
    user_detail = models.ForeignKey(CoreOrderUserDetail)
    card_num_last_four = models.CharField(max_length=12)
    shipping_address = models.ForeignKey(CoreOrderShippingAddress, null=True, blank=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=765)
    import_id = models.CharField(max_length=96, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'core_order'

class CoreTransaction(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type = models.CharField(max_length=765)
    order = models.ForeignKey(CoreOrder)
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

class CoreActionfield(_akit_model):
    parent = models.ForeignKey(CoreAction)
    name = models.CharField(max_length=765)
    value = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'core_actionfield'

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

class CoreUserfield(_akit_model):
    parent = models.ForeignKey(CoreUser)
    name = models.ForeignKey(CoreAlloweduserfield, db_column='name')
    value = models.TextField()
    
    class Meta(_akit_model.Meta):
        db_table = u'core_userfield'

class CorePagefield(_akit_model):
    parent = models.ForeignKey(CorePage)
    name = models.ForeignKey(CoreAllowedpagefield, db_column='name')
    value = models.TextField()
    
    class Meta(_akit_model.Meta):
        db_table = u'core_pagefield'

class CorePhone(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(CoreUser)
    type = models.CharField(max_length=75, unique=True)
    phone = models.CharField(max_length=75)
    source = models.CharField(max_length=75, unique=True)
    normalized_phone = models.CharField(max_length=75)
    class Meta(_akit_model.Meta):
        db_table = u'core_phone'

class CorePagefollowup(_akit_model):
    page = models.ForeignKey(CorePage, unique=True)
    send_email = models.IntegerField()
    url = models.CharField(max_length=765)
    email_wrapper = models.ForeignKey(CoreEmailwrapper, null=True, blank=True)
    email_from_line = models.ForeignKey(CoreFromline, null=True, blank=True)
    email_custom_from = models.CharField(max_length=765)
    email_subject = models.CharField(max_length=765)
    email_body = models.TextField()
    send_taf = models.IntegerField()
    taf_subject = models.CharField(max_length=765)
    taf_body = models.TextField()
    send_notifications = models.IntegerField()
    class Meta(_akit_model.Meta):
        db_table = u'core_pagefollowup'

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

class ReportsQuerytemplate(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    template = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'reports_querytemplate'

class ReportsQueryreport(_akit_model):
    report_ptr = models.ForeignKey(ReportsReport, primary_key=True)
    sql = models.TextField()
    display_as = models.ForeignKey(ReportsQuerytemplate)
    email_always_csv = models.IntegerField(null=True, blank=True)
    class Meta(_akit_model.Meta):
        db_table = u'reports_queryreport'

class ReportsDashboardreport(_akit_model):
    report_ptr = models.ForeignKey(ReportsReport, primary_key=True)
    template = models.TextField()
    class Meta(_akit_model.Meta):
        db_table = u'reports_dashboardreport'

class ReportsReportcategory(_akit_model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    hidden = models.IntegerField()
    name = models.CharField(max_length=765, unique=True)
    class Meta(_akit_model.Meta):
        db_table = u'reports_reportcategory'

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