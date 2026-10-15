# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class AppInstanceProfile(DaraModel):
    def __init__(
        self,
        application_type: str = None,
        application_type_text: str = None,
        biz_id: str = None,
        case_audit_status: str = None,
        case_shelf_status: str = None,
        chatbi_task_id: str = None,
        chatbi_task_status: str = None,
        commodity_code: str = None,
        customer_service: str = None,
        deploy_area: str = None,
        icpba_no: str = None,
        independent_deployment: main_models.AppInstanceProfileIndependentDeployment = None,
        instance_id: str = None,
        open_chat_bi: bool = None,
        ord_time: str = None,
        order_id: str = None,
        pay_time: str = None,
        preview_url: str = None,
        seo_site: str = None,
        share_render_watermark: str = None,
        site_version: str = None,
        site_version_text: str = None,
        source: str = None,
        template_etag: str = None,
        template_id: str = None,
    ):
        # The application type code. For example, PC_WebSite indicates a PC website.
        self.application_type = application_type
        # The display name of the application type.
        self.application_type_text = application_type_text
        # The business identifier of the application instance.
        self.biz_id = biz_id
        # The audit status.
        self.case_audit_status = case_audit_status
        # The listing status.
        self.case_shelf_status = case_shelf_status
        # The ID of the ChatBI BuildSchemaIndex asynchronous task.
        self.chatbi_task_id = chatbi_task_id
        # The status of the ChatBI BuildSchemaIndex task. Valid values: running, finish, and failed.
        self.chatbi_task_status = chatbi_task_status
        # The commodity code used when placing the order.
        self.commodity_code = commodity_code
        # The customer service contact information or description.
        self.customer_service = customer_service
        # The deployment region code of the application.
        self.deploy_area = deploy_area
        # The ICP filing number bound to the custom domain name. Multiple filing numbers are separated by commas (,).
        self.icpba_no = icpba_no
        # The dedicated server information. This field is computed in real time by DescribeAppInstance and is not populated in list API responses.
        self.independent_deployment = independent_deployment
        # The ID of the associated Lingxiao instance.
        self.instance_id = instance_id
        # Indicates whether the current user is included in the ChatBI feature canary release whitelist.
        self.open_chat_bi = open_chat_bi
        # The time when the order was placed, in the yyyy-MM-dd HH:mm:ss format.
        self.ord_time = ord_time
        # The order ID.
        self.order_id = order_id
        # The time when the payment was made, in the yyyy-MM-dd HH:mm:ss format.
        self.pay_time = pay_time
        # The URL used to access the application preview page.
        self.preview_url = preview_url
        # The SEO site configuration identifier.
        self.seo_site = seo_site
        # The switch for the share rendering watermark. A value of 1 indicates enabled, and a value of 0 indicates disabled. This field is empty if not configured.
        self.share_render_watermark = share_render_watermark
        # The site version code.
        self.site_version = site_version
        # The display name of the site version, including the deployment region.
        self.site_version_text = site_version_text
        # The identifier of the creation or synchronization source.
        self.source = source
        # The ETag identifier of the current application template.
        self.template_etag = template_etag
        # The template ID used by the current application.
        self.template_id = template_id

    def validate(self):
        if self.independent_deployment:
            self.independent_deployment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.application_type_text is not None:
            result['ApplicationTypeText'] = self.application_type_text

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.case_audit_status is not None:
            result['CaseAuditStatus'] = self.case_audit_status

        if self.case_shelf_status is not None:
            result['CaseShelfStatus'] = self.case_shelf_status

        if self.chatbi_task_id is not None:
            result['ChatbiTaskId'] = self.chatbi_task_id

        if self.chatbi_task_status is not None:
            result['ChatbiTaskStatus'] = self.chatbi_task_status

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.customer_service is not None:
            result['CustomerService'] = self.customer_service

        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area

        if self.icpba_no is not None:
            result['IcpbaNo'] = self.icpba_no

        if self.independent_deployment is not None:
            result['IndependentDeployment'] = self.independent_deployment.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.open_chat_bi is not None:
            result['OpenChatBi'] = self.open_chat_bi

        if self.ord_time is not None:
            result['OrdTime'] = self.ord_time

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.pay_time is not None:
            result['PayTime'] = self.pay_time

        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url

        if self.seo_site is not None:
            result['SeoSite'] = self.seo_site

        if self.share_render_watermark is not None:
            result['ShareRenderWatermark'] = self.share_render_watermark

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.site_version_text is not None:
            result['SiteVersionText'] = self.site_version_text

        if self.source is not None:
            result['Source'] = self.source

        if self.template_etag is not None:
            result['TemplateEtag'] = self.template_etag

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('ApplicationTypeText') is not None:
            self.application_type_text = m.get('ApplicationTypeText')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('CaseAuditStatus') is not None:
            self.case_audit_status = m.get('CaseAuditStatus')

        if m.get('CaseShelfStatus') is not None:
            self.case_shelf_status = m.get('CaseShelfStatus')

        if m.get('ChatbiTaskId') is not None:
            self.chatbi_task_id = m.get('ChatbiTaskId')

        if m.get('ChatbiTaskStatus') is not None:
            self.chatbi_task_status = m.get('ChatbiTaskStatus')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CustomerService') is not None:
            self.customer_service = m.get('CustomerService')

        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')

        if m.get('IcpbaNo') is not None:
            self.icpba_no = m.get('IcpbaNo')

        if m.get('IndependentDeployment') is not None:
            temp_model = main_models.AppInstanceProfileIndependentDeployment()
            self.independent_deployment = temp_model.from_map(m.get('IndependentDeployment'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OpenChatBi') is not None:
            self.open_chat_bi = m.get('OpenChatBi')

        if m.get('OrdTime') is not None:
            self.ord_time = m.get('OrdTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')

        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')

        if m.get('SeoSite') is not None:
            self.seo_site = m.get('SeoSite')

        if m.get('ShareRenderWatermark') is not None:
            self.share_render_watermark = m.get('ShareRenderWatermark')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('SiteVersionText') is not None:
            self.site_version_text = m.get('SiteVersionText')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TemplateEtag') is not None:
            self.template_etag = m.get('TemplateEtag')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class AppInstanceProfileIndependentDeployment(DaraModel):
    def __init__(
        self,
        can_retry: bool = None,
        deploy_area: str = None,
        dns_record_type: str = None,
        eligibility: str = None,
        enable_status: str = None,
        independent_ip: str = None,
        server_spec: str = None,
        task_id: int = None,
    ):
        # Specifies whether a retry is allowed after the dedicated server fails to start.
        self.can_retry = can_retry
        # The deployment region code of the dedicated server.
        self.deploy_area = deploy_area
        # The DNS record type used when binding a domain name to the dedicated IP address.
        self.dns_record_type = dns_record_type
        # The eligibility status of the dedicated server. Valid values:
        # - UPGRADE_REQUIRED: A version upgrade is required.
        # - AVAILABLE: The dedicated server can be started.
        # - UNAVAILABLE: The dedicated server is currently unavailable.
        self.eligibility = eligibility
        # The status of the dedicated server. Valid values:
        # - NOT_ENABLED: Not started.
        # - ENABLING: Starting.
        # - ACTIVE: Started.
        # - FAILED: Failed to start.
        self.enable_status = enable_status
        # The dedicated IP address assigned after the dedicated server is started.
        self.independent_ip = independent_ip
        # The display specification of the dedicated server. This does not represent the real-time resource usage of the container.
        self.server_spec = server_spec
        # The task ID for starting the dedicated server.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_retry is not None:
            result['CanRetry'] = self.can_retry

        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area

        if self.dns_record_type is not None:
            result['DnsRecordType'] = self.dns_record_type

        if self.eligibility is not None:
            result['Eligibility'] = self.eligibility

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.independent_ip is not None:
            result['IndependentIp'] = self.independent_ip

        if self.server_spec is not None:
            result['ServerSpec'] = self.server_spec

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanRetry') is not None:
            self.can_retry = m.get('CanRetry')

        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')

        if m.get('DnsRecordType') is not None:
            self.dns_record_type = m.get('DnsRecordType')

        if m.get('Eligibility') is not None:
            self.eligibility = m.get('Eligibility')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('IndependentIp') is not None:
            self.independent_ip = m.get('IndependentIp')

        if m.get('ServerSpec') is not None:
            self.server_spec = m.get('ServerSpec')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

