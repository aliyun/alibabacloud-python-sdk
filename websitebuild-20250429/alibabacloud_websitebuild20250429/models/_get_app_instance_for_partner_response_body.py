# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetAppInstanceForPartnerResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.GetAppInstanceForPartnerResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('Module') is not None:
            temp_model = main_models.GetAppInstanceForPartnerResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class GetAppInstanceForPartnerResponseBodyModule(DaraModel):
    def __init__(
        self,
        ai_staff_list: List[main_models.GetAppInstanceForPartnerResponseBodyModuleAiStaffList] = None,
        app_design_spec: main_models.GetAppInstanceForPartnerResponseBodyModuleAppDesignSpec = None,
        app_operation_address: main_models.GetAppInstanceForPartnerResponseBodyModuleAppOperationAddress = None,
        app_service_list: List[main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceList] = None,
        app_sub_type: str = None,
        app_type: str = None,
        biz_id: str = None,
        build_type: str = None,
        deleted: int = None,
        description: str = None,
        design_spec_biz_id: str = None,
        design_spec_id: str = None,
        domain: str = None,
        end_time: str = None,
        env: str = None,
        esp_biz_id: str = None,
        gmt_create: str = None,
        gmt_delete: str = None,
        gmt_modified: str = None,
        gmt_publish: str = None,
        icon_url: str = None,
        name: str = None,
        order_id: str = None,
        partner_detail: main_models.GetAppInstanceForPartnerResponseBodyModulePartnerDetail = None,
        profile: main_models.GetAppInstanceForPartnerResponseBodyModuleProfile = None,
        related_instance_list: List[main_models.GetAppInstanceForPartnerResponseBodyModuleRelatedInstanceList] = None,
        site_host: str = None,
        slug: str = None,
        source_type: str = None,
        start_time: str = None,
        status: str = None,
        status_text: str = None,
        thumbnail_url: str = None,
        user_id: str = None,
        version: str = None,
    ):
        self.ai_staff_list = ai_staff_list
        self.app_design_spec = app_design_spec
        self.app_operation_address = app_operation_address
        self.app_service_list = app_service_list
        self.app_sub_type = app_sub_type
        self.app_type = app_type
        self.biz_id = biz_id
        self.build_type = build_type
        self.deleted = deleted
        self.description = description
        # placeHolder
        self.design_spec_biz_id = design_spec_biz_id
        self.design_spec_id = design_spec_id
        self.domain = domain
        self.end_time = end_time
        self.env = env
        self.esp_biz_id = esp_biz_id
        self.gmt_create = gmt_create
        self.gmt_delete = gmt_delete
        self.gmt_modified = gmt_modified
        self.gmt_publish = gmt_publish
        self.icon_url = icon_url
        self.name = name
        self.order_id = order_id
        self.partner_detail = partner_detail
        self.profile = profile
        self.related_instance_list = related_instance_list
        self.site_host = site_host
        self.slug = slug
        self.source_type = source_type
        self.start_time = start_time
        self.status = status
        self.status_text = status_text
        self.thumbnail_url = thumbnail_url
        self.user_id = user_id
        self.version = version

    def validate(self):
        if self.ai_staff_list:
            for v1 in self.ai_staff_list:
                 if v1:
                    v1.validate()
        if self.app_design_spec:
            self.app_design_spec.validate()
        if self.app_operation_address:
            self.app_operation_address.validate()
        if self.app_service_list:
            for v1 in self.app_service_list:
                 if v1:
                    v1.validate()
        if self.partner_detail:
            self.partner_detail.validate()
        if self.profile:
            self.profile.validate()
        if self.related_instance_list:
            for v1 in self.related_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AiStaffList'] = []
        if self.ai_staff_list is not None:
            for k1 in self.ai_staff_list:
                result['AiStaffList'].append(k1.to_map() if k1 else None)

        if self.app_design_spec is not None:
            result['AppDesignSpec'] = self.app_design_spec.to_map()

        if self.app_operation_address is not None:
            result['AppOperationAddress'] = self.app_operation_address.to_map()

        result['AppServiceList'] = []
        if self.app_service_list is not None:
            for k1 in self.app_service_list:
                result['AppServiceList'].append(k1.to_map() if k1 else None)

        if self.app_sub_type is not None:
            result['AppSubType'] = self.app_sub_type

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.build_type is not None:
            result['BuildType'] = self.build_type

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.description is not None:
            result['Description'] = self.description

        if self.design_spec_biz_id is not None:
            result['DesignSpecBizId'] = self.design_spec_biz_id

        if self.design_spec_id is not None:
            result['DesignSpecId'] = self.design_spec_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.env is not None:
            result['Env'] = self.env

        if self.esp_biz_id is not None:
            result['EspBizId'] = self.esp_biz_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_delete is not None:
            result['GmtDelete'] = self.gmt_delete

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gmt_publish is not None:
            result['GmtPublish'] = self.gmt_publish

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.name is not None:
            result['Name'] = self.name

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.partner_detail is not None:
            result['PartnerDetail'] = self.partner_detail.to_map()

        if self.profile is not None:
            result['Profile'] = self.profile.to_map()

        result['RelatedInstanceList'] = []
        if self.related_instance_list is not None:
            for k1 in self.related_instance_list:
                result['RelatedInstanceList'].append(k1.to_map() if k1 else None)

        if self.site_host is not None:
            result['SiteHost'] = self.site_host

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_text is not None:
            result['StatusText'] = self.status_text

        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ai_staff_list = []
        if m.get('AiStaffList') is not None:
            for k1 in m.get('AiStaffList'):
                temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAiStaffList()
                self.ai_staff_list.append(temp_model.from_map(k1))

        if m.get('AppDesignSpec') is not None:
            temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAppDesignSpec()
            self.app_design_spec = temp_model.from_map(m.get('AppDesignSpec'))

        if m.get('AppOperationAddress') is not None:
            temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAppOperationAddress()
            self.app_operation_address = temp_model.from_map(m.get('AppOperationAddress'))

        self.app_service_list = []
        if m.get('AppServiceList') is not None:
            for k1 in m.get('AppServiceList'):
                temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceList()
                self.app_service_list.append(temp_model.from_map(k1))

        if m.get('AppSubType') is not None:
            self.app_sub_type = m.get('AppSubType')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BuildType') is not None:
            self.build_type = m.get('BuildType')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesignSpecBizId') is not None:
            self.design_spec_biz_id = m.get('DesignSpecBizId')

        if m.get('DesignSpecId') is not None:
            self.design_spec_id = m.get('DesignSpecId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('EspBizId') is not None:
            self.esp_biz_id = m.get('EspBizId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtDelete') is not None:
            self.gmt_delete = m.get('GmtDelete')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GmtPublish') is not None:
            self.gmt_publish = m.get('GmtPublish')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PartnerDetail') is not None:
            temp_model = main_models.GetAppInstanceForPartnerResponseBodyModulePartnerDetail()
            self.partner_detail = temp_model.from_map(m.get('PartnerDetail'))

        if m.get('Profile') is not None:
            temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleProfile()
            self.profile = temp_model.from_map(m.get('Profile'))

        self.related_instance_list = []
        if m.get('RelatedInstanceList') is not None:
            for k1 in m.get('RelatedInstanceList'):
                temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleRelatedInstanceList()
                self.related_instance_list.append(temp_model.from_map(k1))

        if m.get('SiteHost') is not None:
            self.site_host = m.get('SiteHost')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusText') is not None:
            self.status_text = m.get('StatusText')

        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetAppInstanceForPartnerResponseBodyModuleRelatedInstanceList(DaraModel):
    def __init__(
        self,
        app_sub_type: str = None,
        app_type: str = None,
        biz_id: str = None,
        build_type: str = None,
        deleted: int = None,
        description: str = None,
        design_spec_biz_id: str = None,
        design_spec_id: str = None,
        domain: str = None,
        end_time: str = None,
        env: str = None,
        esp_biz_id: str = None,
        gmt_create: str = None,
        gmt_delete: str = None,
        gmt_modified: str = None,
        gmt_publish: str = None,
        icon_url: str = None,
        name: str = None,
        order_id: str = None,
        profile: main_models.GetAppInstanceForPartnerResponseBodyModuleRelatedInstanceListProfile = None,
        site_host: str = None,
        slug: str = None,
        source_type: str = None,
        start_time: str = None,
        status: str = None,
        status_text: str = None,
        thumbnail_url: str = None,
        user_id: str = None,
        version: str = None,
    ):
        self.app_sub_type = app_sub_type
        self.app_type = app_type
        self.biz_id = biz_id
        self.build_type = build_type
        self.deleted = deleted
        self.description = description
        # placeHolder
        self.design_spec_biz_id = design_spec_biz_id
        self.design_spec_id = design_spec_id
        self.domain = domain
        self.end_time = end_time
        self.env = env
        self.esp_biz_id = esp_biz_id
        self.gmt_create = gmt_create
        self.gmt_delete = gmt_delete
        self.gmt_modified = gmt_modified
        self.gmt_publish = gmt_publish
        self.icon_url = icon_url
        self.name = name
        self.order_id = order_id
        self.profile = profile
        self.site_host = site_host
        self.slug = slug
        self.source_type = source_type
        self.start_time = start_time
        self.status = status
        self.status_text = status_text
        self.thumbnail_url = thumbnail_url
        self.user_id = user_id
        self.version = version

    def validate(self):
        if self.profile:
            self.profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_sub_type is not None:
            result['AppSubType'] = self.app_sub_type

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.build_type is not None:
            result['BuildType'] = self.build_type

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.description is not None:
            result['Description'] = self.description

        if self.design_spec_biz_id is not None:
            result['DesignSpecBizId'] = self.design_spec_biz_id

        if self.design_spec_id is not None:
            result['DesignSpecId'] = self.design_spec_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.env is not None:
            result['Env'] = self.env

        if self.esp_biz_id is not None:
            result['EspBizId'] = self.esp_biz_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_delete is not None:
            result['GmtDelete'] = self.gmt_delete

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gmt_publish is not None:
            result['GmtPublish'] = self.gmt_publish

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.name is not None:
            result['Name'] = self.name

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.profile is not None:
            result['Profile'] = self.profile.to_map()

        if self.site_host is not None:
            result['SiteHost'] = self.site_host

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_text is not None:
            result['StatusText'] = self.status_text

        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSubType') is not None:
            self.app_sub_type = m.get('AppSubType')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BuildType') is not None:
            self.build_type = m.get('BuildType')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesignSpecBizId') is not None:
            self.design_spec_biz_id = m.get('DesignSpecBizId')

        if m.get('DesignSpecId') is not None:
            self.design_spec_id = m.get('DesignSpecId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('EspBizId') is not None:
            self.esp_biz_id = m.get('EspBizId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtDelete') is not None:
            self.gmt_delete = m.get('GmtDelete')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GmtPublish') is not None:
            self.gmt_publish = m.get('GmtPublish')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Profile') is not None:
            temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleRelatedInstanceListProfile()
            self.profile = temp_model.from_map(m.get('Profile'))

        if m.get('SiteHost') is not None:
            self.site_host = m.get('SiteHost')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusText') is not None:
            self.status_text = m.get('StatusText')

        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetAppInstanceForPartnerResponseBodyModuleRelatedInstanceListProfile(DaraModel):
    def __init__(
        self,
        admin_url: str = None,
        application_type: str = None,
        application_type_text: str = None,
        bind_cname: str = None,
        biz_id: str = None,
        commodity_code: str = None,
        customer_service: str = None,
        deploy_area: str = None,
        domain_list: str = None,
        editor_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icpba_no: str = None,
        image_list: str = None,
        lx_instance_id: str = None,
        ord_time: str = None,
        order_id: str = None,
        order_num: int = None,
        partner_id: str = None,
        pay_time: str = None,
        preview_url: str = None,
        seo_site: str = None,
        site_logo: str = None,
        site_version: str = None,
        site_version_text: str = None,
        source: str = None,
        template_etag: str = None,
        template_id: str = None,
        text_list: str = None,
        thumbnail: str = None,
        upgrade_status: str = None,
    ):
        self.admin_url = admin_url
        self.application_type = application_type
        self.application_type_text = application_type_text
        self.bind_cname = bind_cname
        self.biz_id = biz_id
        self.commodity_code = commodity_code
        self.customer_service = customer_service
        self.deploy_area = deploy_area
        self.domain_list = domain_list
        self.editor_url = editor_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.icpba_no = icpba_no
        self.image_list = image_list
        self.lx_instance_id = lx_instance_id
        self.ord_time = ord_time
        self.order_id = order_id
        self.order_num = order_num
        self.partner_id = partner_id
        self.pay_time = pay_time
        self.preview_url = preview_url
        self.seo_site = seo_site
        self.site_logo = site_logo
        self.site_version = site_version
        self.site_version_text = site_version_text
        self.source = source
        self.template_etag = template_etag
        self.template_id = template_id
        self.text_list = text_list
        self.thumbnail = thumbnail
        self.upgrade_status = upgrade_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_url is not None:
            result['AdminUrl'] = self.admin_url

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.application_type_text is not None:
            result['ApplicationTypeText'] = self.application_type_text

        if self.bind_cname is not None:
            result['BindCname'] = self.bind_cname

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.customer_service is not None:
            result['CustomerService'] = self.customer_service

        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area

        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

        if self.editor_url is not None:
            result['EditorUrl'] = self.editor_url

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.icpba_no is not None:
            result['IcpbaNo'] = self.icpba_no

        if self.image_list is not None:
            result['ImageList'] = self.image_list

        if self.lx_instance_id is not None:
            result['LxInstanceId'] = self.lx_instance_id

        if self.ord_time is not None:
            result['OrdTime'] = self.ord_time

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_num is not None:
            result['OrderNum'] = self.order_num

        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id

        if self.pay_time is not None:
            result['PayTime'] = self.pay_time

        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url

        if self.seo_site is not None:
            result['SeoSite'] = self.seo_site

        if self.site_logo is not None:
            result['SiteLogo'] = self.site_logo

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

        if self.text_list is not None:
            result['TextList'] = self.text_list

        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail

        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminUrl') is not None:
            self.admin_url = m.get('AdminUrl')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('ApplicationTypeText') is not None:
            self.application_type_text = m.get('ApplicationTypeText')

        if m.get('BindCname') is not None:
            self.bind_cname = m.get('BindCname')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CustomerService') is not None:
            self.customer_service = m.get('CustomerService')

        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')

        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        if m.get('EditorUrl') is not None:
            self.editor_url = m.get('EditorUrl')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IcpbaNo') is not None:
            self.icpba_no = m.get('IcpbaNo')

        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')

        if m.get('LxInstanceId') is not None:
            self.lx_instance_id = m.get('LxInstanceId')

        if m.get('OrdTime') is not None:
            self.ord_time = m.get('OrdTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')

        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')

        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')

        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')

        if m.get('SeoSite') is not None:
            self.seo_site = m.get('SeoSite')

        if m.get('SiteLogo') is not None:
            self.site_logo = m.get('SiteLogo')

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

        if m.get('TextList') is not None:
            self.text_list = m.get('TextList')

        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')

        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')

        return self

class GetAppInstanceForPartnerResponseBodyModuleProfile(DaraModel):
    def __init__(
        self,
        admin_url: str = None,
        application_type: str = None,
        application_type_text: str = None,
        bind_cname: str = None,
        biz_id: str = None,
        commodity_code: str = None,
        customer_service: str = None,
        deploy_area: str = None,
        domain_list: str = None,
        editor_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icpba_no: str = None,
        image_list: str = None,
        lx_instance_id: str = None,
        ord_time: str = None,
        order_id: str = None,
        order_num: int = None,
        partner_id: str = None,
        pay_time: str = None,
        preview_url: str = None,
        seo_site: str = None,
        site_logo: str = None,
        site_version: str = None,
        site_version_text: str = None,
        source: str = None,
        template_etag: str = None,
        template_id: str = None,
        text_list: str = None,
        thumbnail: str = None,
        upgrade_status: str = None,
    ):
        self.admin_url = admin_url
        self.application_type = application_type
        self.application_type_text = application_type_text
        self.bind_cname = bind_cname
        self.biz_id = biz_id
        self.commodity_code = commodity_code
        self.customer_service = customer_service
        self.deploy_area = deploy_area
        self.domain_list = domain_list
        self.editor_url = editor_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.icpba_no = icpba_no
        self.image_list = image_list
        self.lx_instance_id = lx_instance_id
        self.ord_time = ord_time
        self.order_id = order_id
        self.order_num = order_num
        self.partner_id = partner_id
        self.pay_time = pay_time
        self.preview_url = preview_url
        self.seo_site = seo_site
        self.site_logo = site_logo
        self.site_version = site_version
        self.site_version_text = site_version_text
        self.source = source
        self.template_etag = template_etag
        self.template_id = template_id
        self.text_list = text_list
        self.thumbnail = thumbnail
        self.upgrade_status = upgrade_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_url is not None:
            result['AdminUrl'] = self.admin_url

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.application_type_text is not None:
            result['ApplicationTypeText'] = self.application_type_text

        if self.bind_cname is not None:
            result['BindCname'] = self.bind_cname

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.customer_service is not None:
            result['CustomerService'] = self.customer_service

        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area

        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

        if self.editor_url is not None:
            result['EditorUrl'] = self.editor_url

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.icpba_no is not None:
            result['IcpbaNo'] = self.icpba_no

        if self.image_list is not None:
            result['ImageList'] = self.image_list

        if self.lx_instance_id is not None:
            result['LxInstanceId'] = self.lx_instance_id

        if self.ord_time is not None:
            result['OrdTime'] = self.ord_time

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_num is not None:
            result['OrderNum'] = self.order_num

        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id

        if self.pay_time is not None:
            result['PayTime'] = self.pay_time

        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url

        if self.seo_site is not None:
            result['SeoSite'] = self.seo_site

        if self.site_logo is not None:
            result['SiteLogo'] = self.site_logo

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

        if self.text_list is not None:
            result['TextList'] = self.text_list

        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail

        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminUrl') is not None:
            self.admin_url = m.get('AdminUrl')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('ApplicationTypeText') is not None:
            self.application_type_text = m.get('ApplicationTypeText')

        if m.get('BindCname') is not None:
            self.bind_cname = m.get('BindCname')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CustomerService') is not None:
            self.customer_service = m.get('CustomerService')

        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')

        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        if m.get('EditorUrl') is not None:
            self.editor_url = m.get('EditorUrl')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IcpbaNo') is not None:
            self.icpba_no = m.get('IcpbaNo')

        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')

        if m.get('LxInstanceId') is not None:
            self.lx_instance_id = m.get('LxInstanceId')

        if m.get('OrdTime') is not None:
            self.ord_time = m.get('OrdTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')

        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')

        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')

        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')

        if m.get('SeoSite') is not None:
            self.seo_site = m.get('SeoSite')

        if m.get('SiteLogo') is not None:
            self.site_logo = m.get('SiteLogo')

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

        if m.get('TextList') is not None:
            self.text_list = m.get('TextList')

        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')

        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')

        return self

class GetAppInstanceForPartnerResponseBodyModulePartnerDetail(DaraModel):
    def __init__(
        self,
        bind_data: main_models.GetAppInstanceForPartnerResponseBodyModulePartnerDetailBindData = None,
        partner_id: str = None,
        status: str = None,
    ):
        # data
        self.bind_data = bind_data
        self.partner_id = partner_id
        self.status = status

    def validate(self):
        if self.bind_data:
            self.bind_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_data is not None:
            result['BindData'] = self.bind_data.to_map()

        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindData') is not None:
            temp_model = main_models.GetAppInstanceForPartnerResponseBodyModulePartnerDetailBindData()
            self.bind_data = temp_model.from_map(m.get('BindData'))

        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetAppInstanceForPartnerResponseBodyModulePartnerDetailBindData(DaraModel):
    def __init__(
        self,
        aliyun_pk: str = None,
        biz_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        grant_aliyun_pk: str = None,
        mobile: str = None,
        parent_pk: str = None,
        partner_id: str = None,
        user_display_name: str = None,
    ):
        # aliyun_pk
        self.aliyun_pk = aliyun_pk
        self.biz_id = biz_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.grant_aliyun_pk = grant_aliyun_pk
        self.mobile = mobile
        # parent_pk
        self.parent_pk = parent_pk
        self.partner_id = partner_id
        self.user_display_name = user_display_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_pk is not None:
            result['AliyunPk'] = self.aliyun_pk

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.grant_aliyun_pk is not None:
            result['GrantAliyunPk'] = self.grant_aliyun_pk

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.parent_pk is not None:
            result['ParentPk'] = self.parent_pk

        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id

        if self.user_display_name is not None:
            result['UserDisplayName'] = self.user_display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunPk') is not None:
            self.aliyun_pk = m.get('AliyunPk')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GrantAliyunPk') is not None:
            self.grant_aliyun_pk = m.get('GrantAliyunPk')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('ParentPk') is not None:
            self.parent_pk = m.get('ParentPk')

        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')

        if m.get('UserDisplayName') is not None:
            self.user_display_name = m.get('UserDisplayName')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAppServiceList(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        deleted: int = None,
        end_time: str = None,
        esp_biz_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group: main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListGroup = None,
        instance_biz_id: str = None,
        name: str = None,
        node_list: List[main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListNodeList] = None,
        operation_address: main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListOperationAddress = None,
        order_id: str = None,
        profile: main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListProfile = None,
        service_type: str = None,
        service_type_text: str = None,
        slug: str = None,
        start_time: str = None,
        status: str = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.deleted = deleted
        self.end_time = end_time
        # esp bizId
        self.esp_biz_id = esp_biz_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group = group
        self.instance_biz_id = instance_biz_id
        self.name = name
        self.node_list = node_list
        self.operation_address = operation_address
        self.order_id = order_id
        self.profile = profile
        self.service_type = service_type
        self.service_type_text = service_type_text
        self.slug = slug
        self.start_time = start_time
        self.status = status
        self.user_id = user_id

    def validate(self):
        if self.group:
            self.group.validate()
        if self.node_list:
            for v1 in self.node_list:
                 if v1:
                    v1.validate()
        if self.operation_address:
            self.operation_address.validate()
        if self.profile:
            self.profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.esp_biz_id is not None:
            result['EspBizId'] = self.esp_biz_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group is not None:
            result['Group'] = self.group.to_map()

        if self.instance_biz_id is not None:
            result['InstanceBizId'] = self.instance_biz_id

        if self.name is not None:
            result['Name'] = self.name

        result['NodeList'] = []
        if self.node_list is not None:
            for k1 in self.node_list:
                result['NodeList'].append(k1.to_map() if k1 else None)

        if self.operation_address is not None:
            result['OperationAddress'] = self.operation_address.to_map()

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.profile is not None:
            result['Profile'] = self.profile.to_map()

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.service_type_text is not None:
            result['ServiceTypeText'] = self.service_type_text

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EspBizId') is not None:
            self.esp_biz_id = m.get('EspBizId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Group') is not None:
            temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('InstanceBizId') is not None:
            self.instance_biz_id = m.get('InstanceBizId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.node_list = []
        if m.get('NodeList') is not None:
            for k1 in m.get('NodeList'):
                temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListNodeList()
                self.node_list.append(temp_model.from_map(k1))

        if m.get('OperationAddress') is not None:
            temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListOperationAddress()
            self.operation_address = temp_model.from_map(m.get('OperationAddress'))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Profile') is not None:
            temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListProfile()
            self.profile = temp_model.from_map(m.get('Profile'))

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('ServiceTypeText') is not None:
            self.service_type_text = m.get('ServiceTypeText')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAppServiceListProfile(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        design_type: str = None,
        design_type_text: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        lx_instance_id: str = None,
        order_id: str = None,
        service_spec: str = None,
        service_spec_text: str = None,
        upgrade_status: str = None,
    ):
        self.biz_id = biz_id
        self.design_type = design_type
        self.design_type_text = design_type_text
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.lx_instance_id = lx_instance_id
        self.order_id = order_id
        self.service_spec = service_spec
        self.service_spec_text = service_spec_text
        self.upgrade_status = upgrade_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.design_type is not None:
            result['DesignType'] = self.design_type

        if self.design_type_text is not None:
            result['DesignTypeText'] = self.design_type_text

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.lx_instance_id is not None:
            result['LxInstanceId'] = self.lx_instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.service_spec is not None:
            result['ServiceSpec'] = self.service_spec

        if self.service_spec_text is not None:
            result['ServiceSpecText'] = self.service_spec_text

        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DesignType') is not None:
            self.design_type = m.get('DesignType')

        if m.get('DesignTypeText') is not None:
            self.design_type_text = m.get('DesignTypeText')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LxInstanceId') is not None:
            self.lx_instance_id = m.get('LxInstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('ServiceSpec') is not None:
            self.service_spec = m.get('ServiceSpec')

        if m.get('ServiceSpecText') is not None:
            self.service_spec_text = m.get('ServiceSpecText')

        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAppServiceListOperationAddress(DaraModel):
    def __init__(
        self,
        actions: List[main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListOperationAddressActions] = None,
        ai_customer_config_url: str = None,
        ai_design_url: str = None,
        app_publish_url: str = None,
        dashboard_actions: List[main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListOperationAddressDashboardActions] = None,
        design_url: str = None,
        instance_login_url: str = None,
        renew_buy_url: str = None,
        server_delivery_url: str = None,
        upgrade_buy_url: str = None,
    ):
        self.actions = actions
        self.ai_customer_config_url = ai_customer_config_url
        self.ai_design_url = ai_design_url
        self.app_publish_url = app_publish_url
        self.dashboard_actions = dashboard_actions
        self.design_url = design_url
        self.instance_login_url = instance_login_url
        self.renew_buy_url = renew_buy_url
        self.server_delivery_url = server_delivery_url
        self.upgrade_buy_url = upgrade_buy_url

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()
        if self.dashboard_actions:
            for v1 in self.dashboard_actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.ai_customer_config_url is not None:
            result['AiCustomerConfigUrl'] = self.ai_customer_config_url

        if self.ai_design_url is not None:
            result['AiDesignUrl'] = self.ai_design_url

        if self.app_publish_url is not None:
            result['AppPublishUrl'] = self.app_publish_url

        result['DashboardActions'] = []
        if self.dashboard_actions is not None:
            for k1 in self.dashboard_actions:
                result['DashboardActions'].append(k1.to_map() if k1 else None)

        if self.design_url is not None:
            result['DesignUrl'] = self.design_url

        if self.instance_login_url is not None:
            result['InstanceLoginUrl'] = self.instance_login_url

        if self.renew_buy_url is not None:
            result['RenewBuyUrl'] = self.renew_buy_url

        if self.server_delivery_url is not None:
            result['ServerDeliveryUrl'] = self.server_delivery_url

        if self.upgrade_buy_url is not None:
            result['UpgradeBuyUrl'] = self.upgrade_buy_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListOperationAddressActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('AiCustomerConfigUrl') is not None:
            self.ai_customer_config_url = m.get('AiCustomerConfigUrl')

        if m.get('AiDesignUrl') is not None:
            self.ai_design_url = m.get('AiDesignUrl')

        if m.get('AppPublishUrl') is not None:
            self.app_publish_url = m.get('AppPublishUrl')

        self.dashboard_actions = []
        if m.get('DashboardActions') is not None:
            for k1 in m.get('DashboardActions'):
                temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAppServiceListOperationAddressDashboardActions()
                self.dashboard_actions.append(temp_model.from_map(k1))

        if m.get('DesignUrl') is not None:
            self.design_url = m.get('DesignUrl')

        if m.get('InstanceLoginUrl') is not None:
            self.instance_login_url = m.get('InstanceLoginUrl')

        if m.get('RenewBuyUrl') is not None:
            self.renew_buy_url = m.get('RenewBuyUrl')

        if m.get('ServerDeliveryUrl') is not None:
            self.server_delivery_url = m.get('ServerDeliveryUrl')

        if m.get('UpgradeBuyUrl') is not None:
            self.upgrade_buy_url = m.get('UpgradeBuyUrl')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAppServiceListOperationAddressDashboardActions(DaraModel):
    def __init__(
        self,
        action_key: str = None,
        action_text: str = None,
        enable: bool = None,
        href: str = None,
    ):
        self.action_key = action_key
        self.action_text = action_text
        self.enable = enable
        self.href = href

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_key is not None:
            result['ActionKey'] = self.action_key

        if self.action_text is not None:
            result['ActionText'] = self.action_text

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.href is not None:
            result['Href'] = self.href

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionKey') is not None:
            self.action_key = m.get('ActionKey')

        if m.get('ActionText') is not None:
            self.action_text = m.get('ActionText')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Href') is not None:
            self.href = m.get('Href')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAppServiceListOperationAddressActions(DaraModel):
    def __init__(
        self,
        action_key: str = None,
        action_text: str = None,
        enable: bool = None,
        href: str = None,
    ):
        self.action_key = action_key
        self.action_text = action_text
        self.enable = enable
        self.href = href

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_key is not None:
            result['ActionKey'] = self.action_key

        if self.action_text is not None:
            result['ActionText'] = self.action_text

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.href is not None:
            result['Href'] = self.href

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionKey') is not None:
            self.action_key = m.get('ActionKey')

        if m.get('ActionText') is not None:
            self.action_text = m.get('ActionText')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Href') is not None:
            self.href = m.get('Href')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAppServiceListNodeList(DaraModel):
    def __init__(
        self,
        children: List[Any] = None,
        final_step_no: int = None,
        finish_time: int = None,
        is_container_node: bool = None,
        node_id: str = None,
        node_name: str = None,
        node_status: str = None,
        operator_role: str = None,
        parent_node_id: str = None,
        step_no: int = None,
    ):
        self.children = children
        self.final_step_no = final_step_no
        self.finish_time = finish_time
        # IsContainerNode
        self.is_container_node = is_container_node
        self.node_id = node_id
        self.node_name = node_name
        self.node_status = node_status
        self.operator_role = operator_role
        self.parent_node_id = parent_node_id
        self.step_no = step_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.children is not None:
            result['Children'] = self.children

        if self.final_step_no is not None:
            result['FinalStepNo'] = self.final_step_no

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.is_container_node is not None:
            result['IsContainerNode'] = self.is_container_node

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role

        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id

        if self.step_no is not None:
            result['StepNo'] = self.step_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Children') is not None:
            self.children = m.get('Children')

        if m.get('FinalStepNo') is not None:
            self.final_step_no = m.get('FinalStepNo')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('IsContainerNode') is not None:
            self.is_container_node = m.get('IsContainerNode')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')

        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')

        if m.get('StepNo') is not None:
            self.step_no = m.get('StepNo')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAppServiceListGroup(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        qr_code: str = None,
        type: str = None,
        url: str = None,
    ):
        self.id = id
        self.name = name
        # QrCode
        self.qr_code = qr_code
        # dingtalk wx...
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.qr_code is not None:
            result['QrCode'] = self.qr_code

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QrCode') is not None:
            self.qr_code = m.get('QrCode')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAppOperationAddress(DaraModel):
    def __init__(
        self,
        actions: List[main_models.GetAppInstanceForPartnerResponseBodyModuleAppOperationAddressActions] = None,
        ai_customer_config_url: str = None,
        ai_design_url: str = None,
        app_publish_url: str = None,
        dashboard_actions: List[main_models.GetAppInstanceForPartnerResponseBodyModuleAppOperationAddressDashboardActions] = None,
        design_url: str = None,
        instance_login_url: str = None,
        renew_buy_url: str = None,
        server_delivery_url: str = None,
        upgrade_buy_url: str = None,
    ):
        self.actions = actions
        self.ai_customer_config_url = ai_customer_config_url
        self.ai_design_url = ai_design_url
        self.app_publish_url = app_publish_url
        self.dashboard_actions = dashboard_actions
        self.design_url = design_url
        self.instance_login_url = instance_login_url
        self.renew_buy_url = renew_buy_url
        self.server_delivery_url = server_delivery_url
        self.upgrade_buy_url = upgrade_buy_url

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()
        if self.dashboard_actions:
            for v1 in self.dashboard_actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.ai_customer_config_url is not None:
            result['AiCustomerConfigUrl'] = self.ai_customer_config_url

        if self.ai_design_url is not None:
            result['AiDesignUrl'] = self.ai_design_url

        if self.app_publish_url is not None:
            result['AppPublishUrl'] = self.app_publish_url

        result['DashboardActions'] = []
        if self.dashboard_actions is not None:
            for k1 in self.dashboard_actions:
                result['DashboardActions'].append(k1.to_map() if k1 else None)

        if self.design_url is not None:
            result['DesignUrl'] = self.design_url

        if self.instance_login_url is not None:
            result['InstanceLoginUrl'] = self.instance_login_url

        if self.renew_buy_url is not None:
            result['RenewBuyUrl'] = self.renew_buy_url

        if self.server_delivery_url is not None:
            result['ServerDeliveryUrl'] = self.server_delivery_url

        if self.upgrade_buy_url is not None:
            result['UpgradeBuyUrl'] = self.upgrade_buy_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAppOperationAddressActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('AiCustomerConfigUrl') is not None:
            self.ai_customer_config_url = m.get('AiCustomerConfigUrl')

        if m.get('AiDesignUrl') is not None:
            self.ai_design_url = m.get('AiDesignUrl')

        if m.get('AppPublishUrl') is not None:
            self.app_publish_url = m.get('AppPublishUrl')

        self.dashboard_actions = []
        if m.get('DashboardActions') is not None:
            for k1 in m.get('DashboardActions'):
                temp_model = main_models.GetAppInstanceForPartnerResponseBodyModuleAppOperationAddressDashboardActions()
                self.dashboard_actions.append(temp_model.from_map(k1))

        if m.get('DesignUrl') is not None:
            self.design_url = m.get('DesignUrl')

        if m.get('InstanceLoginUrl') is not None:
            self.instance_login_url = m.get('InstanceLoginUrl')

        if m.get('RenewBuyUrl') is not None:
            self.renew_buy_url = m.get('RenewBuyUrl')

        if m.get('ServerDeliveryUrl') is not None:
            self.server_delivery_url = m.get('ServerDeliveryUrl')

        if m.get('UpgradeBuyUrl') is not None:
            self.upgrade_buy_url = m.get('UpgradeBuyUrl')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAppOperationAddressDashboardActions(DaraModel):
    def __init__(
        self,
        action_key: str = None,
        action_text: str = None,
        enable: bool = None,
        href: str = None,
    ):
        self.action_key = action_key
        self.action_text = action_text
        self.enable = enable
        self.href = href

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_key is not None:
            result['ActionKey'] = self.action_key

        if self.action_text is not None:
            result['ActionText'] = self.action_text

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.href is not None:
            result['Href'] = self.href

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionKey') is not None:
            self.action_key = m.get('ActionKey')

        if m.get('ActionText') is not None:
            self.action_text = m.get('ActionText')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Href') is not None:
            self.href = m.get('Href')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAppOperationAddressActions(DaraModel):
    def __init__(
        self,
        action_key: str = None,
        action_text: str = None,
        enable: bool = None,
        href: str = None,
    ):
        self.action_key = action_key
        self.action_text = action_text
        self.enable = enable
        self.href = href

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_key is not None:
            result['ActionKey'] = self.action_key

        if self.action_text is not None:
            result['ActionText'] = self.action_text

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.href is not None:
            result['Href'] = self.href

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionKey') is not None:
            self.action_key = m.get('ActionKey')

        if m.get('ActionText') is not None:
            self.action_text = m.get('ActionText')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Href') is not None:
            self.href = m.get('Href')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAppDesignSpec(DaraModel):
    def __init__(
        self,
        bilingual: bool = None,
        biz_id: str = None,
        business_scope: str = None,
        color_style: str = None,
        company_name: str = None,
        deploy_area: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        main_business: str = None,
        reference_website: str = None,
        site_goals: str = None,
        site_language: str = None,
        site_logo: str = None,
        site_slogan: str = None,
        site_style: str = None,
        site_title: str = None,
        site_type: str = None,
        user_id: str = None,
    ):
        # bill
        self.bilingual = bilingual
        self.biz_id = biz_id
        # busincessScope
        self.business_scope = business_scope
        self.color_style = color_style
        self.company_name = company_name
        self.deploy_area = deploy_area
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        # business
        self.main_business = main_business
        # website
        self.reference_website = reference_website
        # sitegolas
        self.site_goals = site_goals
        # language
        self.site_language = site_language
        # sitelogo
        self.site_logo = site_logo
        # siteslogan
        self.site_slogan = site_slogan
        # sitestyle
        self.site_style = site_style
        # sitetitle
        self.site_title = site_title
        self.site_type = site_type
        # userid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bilingual is not None:
            result['Bilingual'] = self.bilingual

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.business_scope is not None:
            result['BusinessScope'] = self.business_scope

        if self.color_style is not None:
            result['ColorStyle'] = self.color_style

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.main_business is not None:
            result['MainBusiness'] = self.main_business

        if self.reference_website is not None:
            result['ReferenceWebsite'] = self.reference_website

        if self.site_goals is not None:
            result['SiteGoals'] = self.site_goals

        if self.site_language is not None:
            result['SiteLanguage'] = self.site_language

        if self.site_logo is not None:
            result['SiteLogo'] = self.site_logo

        if self.site_slogan is not None:
            result['SiteSlogan'] = self.site_slogan

        if self.site_style is not None:
            result['SiteStyle'] = self.site_style

        if self.site_title is not None:
            result['SiteTitle'] = self.site_title

        if self.site_type is not None:
            result['SiteType'] = self.site_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bilingual') is not None:
            self.bilingual = m.get('Bilingual')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BusinessScope') is not None:
            self.business_scope = m.get('BusinessScope')

        if m.get('ColorStyle') is not None:
            self.color_style = m.get('ColorStyle')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MainBusiness') is not None:
            self.main_business = m.get('MainBusiness')

        if m.get('ReferenceWebsite') is not None:
            self.reference_website = m.get('ReferenceWebsite')

        if m.get('SiteGoals') is not None:
            self.site_goals = m.get('SiteGoals')

        if m.get('SiteLanguage') is not None:
            self.site_language = m.get('SiteLanguage')

        if m.get('SiteLogo') is not None:
            self.site_logo = m.get('SiteLogo')

        if m.get('SiteSlogan') is not None:
            self.site_slogan = m.get('SiteSlogan')

        if m.get('SiteStyle') is not None:
            self.site_style = m.get('SiteStyle')

        if m.get('SiteTitle') is not None:
            self.site_title = m.get('SiteTitle')

        if m.get('SiteType') is not None:
            self.site_type = m.get('SiteType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetAppInstanceForPartnerResponseBodyModuleAiStaffList(DaraModel):
    def __init__(
        self,
        staff_id: str = None,
        staff_name: str = None,
        staff_type: str = None,
        status: str = None,
    ):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.staff_type = staff_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.staff_id is not None:
            result['StaffId'] = self.staff_id

        if self.staff_name is not None:
            result['StaffName'] = self.staff_name

        if self.staff_type is not None:
            result['StaffType'] = self.staff_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StaffId') is not None:
            self.staff_id = m.get('StaffId')

        if m.get('StaffName') is not None:
            self.staff_name = m.get('StaffName')

        if m.get('StaffType') is not None:
            self.staff_type = m.get('StaffType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

