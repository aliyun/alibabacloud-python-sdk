# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateLogoTaskRequest(TeaModel):
    def __init__(
        self,
        logo_version: str = None,
        negative_prompt: str = None,
        parameters: str = None,
        prompt: str = None,
    ):
        self.logo_version = logo_version
        self.negative_prompt = negative_prompt
        self.parameters = parameters
        self.prompt = prompt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logo_version is not None:
            result['LogoVersion'] = self.logo_version
        if self.negative_prompt is not None:
            result['NegativePrompt'] = self.negative_prompt
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogoVersion') is not None:
            self.logo_version = m.get('LogoVersion')
        if m.get('NegativePrompt') is not None:
            self.negative_prompt = m.get('NegativePrompt')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        return self


class CreateLogoTaskResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateLogoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLogoTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLogoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCreateLogoTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetCreateLogoTaskResponseBodyTask(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        task_status: str = None,
        urls: List[str] = None,
    ):
        self.task_id = task_id
        self.task_status = task_status
        self.urls = urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.urls is not None:
            result['Urls'] = self.urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Urls') is not None:
            self.urls = m.get('Urls')
        return self


class GetCreateLogoTaskResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        task: GetCreateLogoTaskResponseBodyTask = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task is not None:
            result['Task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Task') is not None:
            temp_model = GetCreateLogoTaskResponseBodyTask()
            self.task = temp_model.from_map(m['Task'])
        return self


class GetCreateLogoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCreateLogoTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCreateLogoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateAppInstanceForPartnerRequest(TeaModel):
    def __init__(
        self,
        extend: str = None,
        operate_event: str = None,
    ):
        self.extend = extend
        self.operate_event = operate_event

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.operate_event is not None:
            result['OperateEvent'] = self.operate_event
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('OperateEvent') is not None:
            self.operate_event = m.get('OperateEvent')
        return self


class OperateAppInstanceForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateAppInstanceForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateAppInstanceForPartnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OperateAppInstanceForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateAppServiceForPartnerRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        extend: str = None,
        operate_event: str = None,
        service_type: str = None,
    ):
        self.biz_id = biz_id
        self.extend = extend
        self.operate_event = operate_event
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.operate_event is not None:
            result['OperateEvent'] = self.operate_event
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('OperateEvent') is not None:
            self.operate_event = m.get('OperateEvent')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class OperateAppServiceForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateAppServiceForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateAppServiceForPartnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OperateAppServiceForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncAppInstanceForPartnerRequestAppInstanceProfile(TeaModel):
    def __init__(
        self,
        deploy_area: str = None,
        lx_instance_id: str = None,
        order_id: str = None,
        site_version: str = None,
        template_etag: str = None,
        template_id: str = None,
    ):
        self.deploy_area = deploy_area
        self.lx_instance_id = lx_instance_id
        self.order_id = order_id
        self.site_version = site_version
        self.template_etag = template_etag
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area
        if self.lx_instance_id is not None:
            result['LxInstanceId'] = self.lx_instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        if self.template_etag is not None:
            result['TemplateEtag'] = self.template_etag
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')
        if m.get('LxInstanceId') is not None:
            self.lx_instance_id = m.get('LxInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        if m.get('TemplateEtag') is not None:
            self.template_etag = m.get('TemplateEtag')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class SyncAppInstanceForPartnerRequestAppInstance(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        biz_id: str = None,
        deleted: str = None,
        domain: str = None,
        end_time: str = None,
        gmt_delete: str = None,
        gmt_publish: str = None,
        icon_url: str = None,
        name: str = None,
        profile: SyncAppInstanceForPartnerRequestAppInstanceProfile = None,
        site_host: str = None,
        slug: str = None,
        start_time: str = None,
        status: str = None,
        thumbnail_url: str = None,
        user_id: str = None,
    ):
        self.app_type = app_type
        self.biz_id = biz_id
        self.deleted = deleted
        self.domain = domain
        self.end_time = end_time
        self.gmt_delete = gmt_delete
        self.gmt_publish = gmt_publish
        self.icon_url = icon_url
        self.name = name
        self.profile = profile
        # siteId
        self.site_host = site_host
        self.slug = slug
        self.start_time = start_time
        self.status = status
        self.thumbnail_url = thumbnail_url
        # 123123123131232
        self.user_id = user_id

    def validate(self):
        if self.profile:
            self.profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_delete is not None:
            result['GmtDelete'] = self.gmt_delete
        if self.gmt_publish is not None:
            result['GmtPublish'] = self.gmt_publish
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile.to_map()
        if self.site_host is not None:
            result['SiteHost'] = self.site_host
        if self.slug is not None:
            result['Slug'] = self.slug
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtDelete') is not None:
            self.gmt_delete = m.get('GmtDelete')
        if m.get('GmtPublish') is not None:
            self.gmt_publish = m.get('GmtPublish')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            temp_model = SyncAppInstanceForPartnerRequestAppInstanceProfile()
            self.profile = temp_model.from_map(m['Profile'])
        if m.get('SiteHost') is not None:
            self.site_host = m.get('SiteHost')
        if m.get('Slug') is not None:
            self.slug = m.get('Slug')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SyncAppInstanceForPartnerRequest(TeaModel):
    def __init__(
        self,
        app_instance: SyncAppInstanceForPartnerRequestAppInstance = None,
        event_type: str = None,
        operator: str = None,
        source_biz_id: str = None,
        source_type: str = None,
    ):
        self.app_instance = app_instance
        self.event_type = event_type
        self.operator = operator
        self.source_biz_id = source_biz_id
        self.source_type = source_type

    def validate(self):
        if self.app_instance:
            self.app_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance is not None:
            result['AppInstance'] = self.app_instance.to_map()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.source_biz_id is not None:
            result['SourceBizId'] = self.source_biz_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstance') is not None:
            temp_model = SyncAppInstanceForPartnerRequestAppInstance()
            self.app_instance = temp_model.from_map(m['AppInstance'])
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('SourceBizId') is not None:
            self.source_biz_id = m.get('SourceBizId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SyncAppInstanceForPartnerShrinkRequest(TeaModel):
    def __init__(
        self,
        app_instance_shrink: str = None,
        event_type: str = None,
        operator: str = None,
        source_biz_id: str = None,
        source_type: str = None,
    ):
        self.app_instance_shrink = app_instance_shrink
        self.event_type = event_type
        self.operator = operator
        self.source_biz_id = source_biz_id
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_shrink is not None:
            result['AppInstance'] = self.app_instance_shrink
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.source_biz_id is not None:
            result['SourceBizId'] = self.source_biz_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstance') is not None:
            self.app_instance_shrink = m.get('AppInstance')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('SourceBizId') is not None:
            self.source_biz_id = m.get('SourceBizId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SyncAppInstanceForPartnerResponseBodyDataAppInstance(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class SyncAppInstanceForPartnerResponseBodyData(TeaModel):
    def __init__(
        self,
        app_instance: SyncAppInstanceForPartnerResponseBodyDataAppInstance = None,
    ):
        self.app_instance = app_instance

    def validate(self):
        if self.app_instance:
            self.app_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance is not None:
            result['AppInstance'] = self.app_instance.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstance') is not None:
            temp_model = SyncAppInstanceForPartnerResponseBodyDataAppInstance()
            self.app_instance = temp_model.from_map(m['AppInstance'])
        return self


class SyncAppInstanceForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        data: SyncAppInstanceForPartnerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SyncAppInstanceForPartnerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SyncAppInstanceForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncAppInstanceForPartnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SyncAppInstanceForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


