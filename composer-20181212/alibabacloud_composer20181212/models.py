# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CloneFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        version_id: str = None,
    ):
        self.flow_id = flow_id
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CloneFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        flow_id: str = None,
    ):
        self.request_id = request_id
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class CloneFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloneFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloneFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        flow_description: str = None,
        definition: str = None,
        template_id: str = None,
        flow_source: str = None,
    ):
        self.flow_name = flow_name
        self.flow_description = flow_description
        self.definition = definition
        self.template_id = template_id
        self.flow_source = flow_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.flow_source is not None:
            result['FlowSource'] = self.flow_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FlowSource') is not None:
            self.flow_source = m.get('FlowSource')
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        flow_id: str = None,
    ):
        self.request_id = request_id
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DeleteFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DisableFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        flow_status: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.flow_status = flow_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        return self


class DisableFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class EnableFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        flow_status: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.flow_status = flow_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        return self


class EnableFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        flow_id: str = None,
        region_id: str = None,
        flow_name: str = None,
        flow_description: str = None,
        create_time: str = None,
        update_time: str = None,
        current_version_id: int = None,
        flow_status: str = None,
        definition: str = None,
        template_id: str = None,
        flow_source: str = None,
        flow_edit_mode: str = None,
    ):
        self.request_id = request_id
        self.flow_id = flow_id
        self.region_id = region_id
        self.flow_name = flow_name
        self.flow_description = flow_description
        self.create_time = create_time
        self.update_time = update_time
        self.current_version_id = current_version_id
        self.flow_status = flow_status
        self.definition = definition
        self.template_id = template_id
        self.flow_source = flow_source
        self.flow_edit_mode = flow_edit_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.current_version_id is not None:
            result['CurrentVersionId'] = self.current_version_id
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.flow_source is not None:
            result['FlowSource'] = self.flow_source
        if self.flow_edit_mode is not None:
            result['FlowEditMode'] = self.flow_edit_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CurrentVersionId') is not None:
            self.current_version_id = m.get('CurrentVersionId')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FlowSource') is not None:
            self.flow_source = m.get('FlowSource')
        if m.get('FlowEditMode') is not None:
            self.flow_edit_mode = m.get('FlowEditMode')
        return self


class GetFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        region_id: str = None,
        template_id: str = None,
        template_name: str = None,
        template_description: str = None,
        template_tag: str = None,
        definition: str = None,
        create_time: str = None,
        update_time: str = None,
        template_connector: str = None,
        template_summary: str = None,
        template_summary_en: str = None,
        template_locale: str = None,
        template_version: int = None,
        template_overview: str = None,
        template_creator: str = None,
    ):
        self.request_id = request_id
        self.region_id = region_id
        self.template_id = template_id
        self.template_name = template_name
        self.template_description = template_description
        self.template_tag = template_tag
        self.definition = definition
        self.create_time = create_time
        self.update_time = update_time
        self.template_connector = template_connector
        self.template_summary = template_summary
        self.template_summary_en = template_summary_en
        self.template_locale = template_locale
        self.template_version = template_version
        self.template_overview = template_overview
        self.template_creator = template_creator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_tag is not None:
            result['TemplateTag'] = self.template_tag
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.template_connector is not None:
            result['TemplateConnector'] = self.template_connector
        if self.template_summary is not None:
            result['TemplateSummary'] = self.template_summary
        if self.template_summary_en is not None:
            result['TemplateSummaryEn'] = self.template_summary_en
        if self.template_locale is not None:
            result['TemplateLocale'] = self.template_locale
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_overview is not None:
            result['TemplateOverview'] = self.template_overview
        if self.template_creator is not None:
            result['TemplateCreator'] = self.template_creator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateTag') is not None:
            self.template_tag = m.get('TemplateTag')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('TemplateConnector') is not None:
            self.template_connector = m.get('TemplateConnector')
        if m.get('TemplateSummary') is not None:
            self.template_summary = m.get('TemplateSummary')
        if m.get('TemplateSummaryEn') is not None:
            self.template_summary_en = m.get('TemplateSummaryEn')
        if m.get('TemplateLocale') is not None:
            self.template_locale = m.get('TemplateLocale')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateOverview') is not None:
            self.template_overview = m.get('TemplateOverview')
        if m.get('TemplateCreator') is not None:
            self.template_creator = m.get('TemplateCreator')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVersionRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        version_id: str = None,
    ):
        # 工作流 ID
        self.flow_id = flow_id
        # 工作流版本 ID
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetVersionResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        definition: str = None,
        flow_id: str = None,
        region_id: str = None,
        request_id: str = None,
        update_time: str = None,
        version_description: str = None,
        version_id: str = None,
        version_name: str = None,
        version_status: str = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 工作流定义
        self.definition = definition
        # 工作流 ID
        self.flow_id = flow_id
        # 地域 ID
        self.region_id = region_id
        # 请求 ID
        self.request_id = request_id
        # 更新时间
        self.update_time = update_time
        # 版本描述
        self.version_description = version_description
        # 版本 ID
        self.version_id = version_id
        # 版本名称
        self.version_name = version_name
        # 版本状态
        self.version_status = version_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version_description is not None:
            result['VersionDescription'] = self.version_description
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.version_status is not None:
            result['VersionStatus'] = self.version_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('VersionStatus') is not None:
            self.version_status = m.get('VersionStatus')
        return self


class GetVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GroupInvokeFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        group_key: str = None,
        data: str = None,
        client_token: str = None,
        total_count: int = None,
        tags: str = None,
    ):
        # FlowId
        self.flow_id = flow_id
        # GroupKey
        self.group_key = group_key
        # Data
        self.data = data
        # ClientToken
        self.client_token = client_token
        # TotalCount
        self.total_count = total_count
        # Tags
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.group_key is not None:
            result['GroupKey'] = self.group_key
        if self.data is not None:
            result['Data'] = self.data
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('GroupKey') is not None:
            self.group_key = m.get('GroupKey')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GroupInvokeFlowResponseBody(TeaModel):
    def __init__(
        self,
        current_count: int = None,
        group_invocation_id: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # 当前批次
        self.current_count = current_count
        # 执行 ID
        self.group_invocation_id = group_invocation_id
        # 请求 ID
        self.request_id = request_id
        # 状态
        self.status = status
        # 调用是否成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_count is not None:
            result['CurrentCount'] = self.current_count
        if self.group_invocation_id is not None:
            result['GroupInvocationId'] = self.group_invocation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentCount') is not None:
            self.current_count = m.get('CurrentCount')
        if m.get('GroupInvocationId') is not None:
            self.group_invocation_id = m.get('GroupInvocationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GroupInvokeFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GroupInvokeFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GroupInvokeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        parameters: str = None,
        data: str = None,
        client_token: str = None,
    ):
        self.flow_id = flow_id
        self.parameters = parameters
        self.data = data
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.data is not None:
            result['Data'] = self.data
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class InvokeFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        invocation_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.invocation_id = invocation_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InvokeFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InvokeFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InvokeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        flow_name: str = None,
        filter: str = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.flow_name = flow_name
        self.filter = filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.filter is not None:
            result['Filter'] = self.filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        return self


class ListFlowsResponseBodyFlows(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        region_id: str = None,
        flow_name: str = None,
        flow_description: str = None,
        version_id: int = None,
        create_time: str = None,
        update_time: str = None,
        flow_status: str = None,
        template_id: str = None,
        flow_source: str = None,
        flow_edit_mode: str = None,
    ):
        self.flow_id = flow_id
        self.region_id = region_id
        self.flow_name = flow_name
        self.flow_description = flow_description
        self.version_id = version_id
        self.create_time = create_time
        self.update_time = update_time
        self.flow_status = flow_status
        self.template_id = template_id
        self.flow_source = flow_source
        self.flow_edit_mode = flow_edit_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.flow_source is not None:
            result['FlowSource'] = self.flow_source
        if self.flow_edit_mode is not None:
            result['FlowEditMode'] = self.flow_edit_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FlowSource') is not None:
            self.flow_source = m.get('FlowSource')
        if m.get('FlowEditMode') is not None:
            self.flow_edit_mode = m.get('FlowEditMode')
        return self


class ListFlowsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        flows: List[ListFlowsResponseBodyFlows] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.flows = flows

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = ListFlowsResponseBodyFlows()
                self.flows.append(temp_model.from_map(k))
        return self


class ListFlowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFlowsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        total_count: int = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.total_count = total_count
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        name: str = None,
        tag: str = None,
        lang: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.name = name
        self.tag = tag
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        template_name: str = None,
        template_description: str = None,
        template_tag: str = None,
        create_time: str = None,
        update_time: str = None,
        template_connector: str = None,
        template_summary: str = None,
        template_summary_en: str = None,
        template_locale: str = None,
        template_version: int = None,
        template_creator: str = None,
        template_overview: str = None,
    ):
        self.template_id = template_id
        self.template_name = template_name
        self.template_description = template_description
        self.template_tag = template_tag
        self.create_time = create_time
        self.update_time = update_time
        self.template_connector = template_connector
        self.template_summary = template_summary
        self.template_summary_en = template_summary_en
        self.template_locale = template_locale
        self.template_version = template_version
        self.template_creator = template_creator
        self.template_overview = template_overview

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_tag is not None:
            result['TemplateTag'] = self.template_tag
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.template_connector is not None:
            result['TemplateConnector'] = self.template_connector
        if self.template_summary is not None:
            result['TemplateSummary'] = self.template_summary
        if self.template_summary_en is not None:
            result['TemplateSummaryEn'] = self.template_summary_en
        if self.template_locale is not None:
            result['TemplateLocale'] = self.template_locale
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_creator is not None:
            result['TemplateCreator'] = self.template_creator
        if self.template_overview is not None:
            result['TemplateOverview'] = self.template_overview
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateTag') is not None:
            self.template_tag = m.get('TemplateTag')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('TemplateConnector') is not None:
            self.template_connector = m.get('TemplateConnector')
        if m.get('TemplateSummary') is not None:
            self.template_summary = m.get('TemplateSummary')
        if m.get('TemplateSummaryEn') is not None:
            self.template_summary_en = m.get('TemplateSummaryEn')
        if m.get('TemplateLocale') is not None:
            self.template_locale = m.get('TemplateLocale')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateCreator') is not None:
            self.template_creator = m.get('TemplateCreator')
        if m.get('TemplateOverview') is not None:
            self.template_overview = m.get('TemplateOverview')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        templates: List[ListTemplatesResponseBodyTemplates] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.templates = templates

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVersionsRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.flow_id = flow_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListVersionsResponseBodyVersions(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        flow_id: str = None,
        version_name: int = None,
        version_status: int = None,
        create_time: str = None,
        update_time: str = None,
    ):
        self.version_id = version_id
        self.flow_id = flow_id
        self.version_name = version_name
        self.version_status = version_status
        self.create_time = create_time
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.version_status is not None:
            result['VersionStatus'] = self.version_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('VersionStatus') is not None:
            self.version_status = m.get('VersionStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        versions: List[ListVersionsResponseBodyVersions] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
        all: bool = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key
        self.all = all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        flow_name: str = None,
        flow_description: str = None,
        definition: str = None,
    ):
        self.flow_id = flow_id
        self.flow_name = flow_name
        self.flow_description = flow_description
        self.definition = definition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_description is not None:
            result['FlowDescription'] = self.flow_description
        if self.definition is not None:
            result['Definition'] = self.definition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowDescription') is not None:
            self.flow_description = m.get('FlowDescription')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        return self


class UpdateFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        current_version_id: int = None,
    ):
        self.request_id = request_id
        self.success = success
        self.current_version_id = current_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.current_version_id is not None:
            result['CurrentVersionId'] = self.current_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('CurrentVersionId') is not None:
            self.current_version_id = m.get('CurrentVersionId')
        return self


class UpdateFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


