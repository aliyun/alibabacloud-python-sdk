# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AbortChangeRequest(TeaModel):
    def __init__(
        self,
        change_id: str = None,
    ):
        self.change_id = change_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        return self


class AbortChangeResponseBodyEnvChange(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class AbortChangeResponseBody(TeaModel):
    def __init__(
        self,
        env_change: AbortChangeResponseBodyEnvChange = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.env_change = env_change
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.env_change:
            self.env_change.validate()

    def to_map(self):
        result = dict()
        if self.env_change is not None:
            result['EnvChange'] = self.env_change.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvChange') is not None:
            temp_model = AbortChangeResponseBodyEnvChange()
            self.env_change = temp_model.from_map(m['EnvChange'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AbortChangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AbortChangeResponseBody = None,
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
            temp_model = AbortChangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppEnvRequest(TeaModel):
    def __init__(
        self,
        env_name: str = None,
        env_description: str = None,
        stack_id: str = None,
        app_id: str = None,
        pkg_version_id: str = None,
        option_settings: str = None,
        profile_name: str = None,
        source_env_id: str = None,
        template_id: str = None,
        dry_run: bool = None,
        extra_properties: str = None,
    ):
        self.env_name = env_name
        self.env_description = env_description
        self.stack_id = stack_id
        self.app_id = app_id
        self.pkg_version_id = pkg_version_id
        self.option_settings = option_settings
        self.profile_name = profile_name
        self.source_env_id = source_env_id
        self.template_id = template_id
        self.dry_run = dry_run
        self.extra_properties = extra_properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.env_description is not None:
            result['EnvDescription'] = self.env_description
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.pkg_version_id is not None:
            result['PkgVersionId'] = self.pkg_version_id
        if self.option_settings is not None:
            result['OptionSettings'] = self.option_settings
        if self.profile_name is not None:
            result['ProfileName'] = self.profile_name
        if self.source_env_id is not None:
            result['SourceEnvId'] = self.source_env_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.extra_properties is not None:
            result['ExtraProperties'] = self.extra_properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('EnvDescription') is not None:
            self.env_description = m.get('EnvDescription')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PkgVersionId') is not None:
            self.pkg_version_id = m.get('PkgVersionId')
        if m.get('OptionSettings') is not None:
            self.option_settings = m.get('OptionSettings')
        if m.get('ProfileName') is not None:
            self.profile_name = m.get('ProfileName')
        if m.get('SourceEnvId') is not None:
            self.source_env_id = m.get('SourceEnvId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ExtraProperties') is not None:
            self.extra_properties = m.get('ExtraProperties')
        return self


class CreateAppEnvResponseBodyEnvChangeDetailOperationsOperation(TeaModel):
    def __init__(
        self,
        operation_description: str = None,
        operation_type: str = None,
    ):
        self.operation_description = operation_description
        self.operation_type = operation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        return self


class CreateAppEnvResponseBodyEnvChangeDetailOperations(TeaModel):
    def __init__(
        self,
        operation: List[CreateAppEnvResponseBodyEnvChangeDetailOperationsOperation] = None,
    ):
        self.operation = operation

    def validate(self):
        if self.operation:
            for k in self.operation:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Operation'] = []
        if self.operation is not None:
            for k in self.operation:
                result['Operation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation = []
        if m.get('Operation') is not None:
            for k in m.get('Operation'):
                temp_model = CreateAppEnvResponseBodyEnvChangeDetailOperationsOperation()
                self.operation.append(temp_model.from_map(k))
        return self


class CreateAppEnvResponseBodyEnvChangeDetail(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
        operations: CreateAppEnvResponseBodyEnvChangeDetailOperations = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id
        self.operations = operations

    def validate(self):
        if self.operations:
            self.operations.validate()

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.operations is not None:
            result['Operations'] = self.operations.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Operations') is not None:
            temp_model = CreateAppEnvResponseBodyEnvChangeDetailOperations()
            self.operations = temp_model.from_map(m['Operations'])
        return self


class CreateAppEnvResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        env_change_detail: CreateAppEnvResponseBodyEnvChangeDetail = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.env_change_detail = env_change_detail
        self.code = code

    def validate(self):
        if self.env_change_detail:
            self.env_change_detail.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.env_change_detail is not None:
            result['EnvChangeDetail'] = self.env_change_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EnvChangeDetail') is not None:
            temp_model = CreateAppEnvResponseBodyEnvChangeDetail()
            self.env_change_detail = temp_model.from_map(m['EnvChangeDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateAppEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppEnvResponseBody = None,
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
            temp_model = CreateAppEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_description: str = None,
        category_name: str = None,
        using_shared_storage: bool = None,
    ):
        self.app_name = app_name
        self.app_description = app_description
        self.category_name = category_name
        self.using_shared_storage = using_shared_storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.using_shared_storage is not None:
            result['UsingSharedStorage'] = self.using_shared_storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('UsingSharedStorage') is not None:
            self.using_shared_storage = m.get('UsingSharedStorage')
        return self


class CreateApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        create_username: str = None,
        app_name: str = None,
        update_time: int = None,
        update_username: str = None,
        create_time: int = None,
        app_id: str = None,
        category_name: str = None,
        using_shared_storage: bool = None,
        app_description: str = None,
    ):
        self.create_username = create_username
        self.app_name = app_name
        self.update_time = update_time
        self.update_username = update_username
        self.create_time = create_time
        self.app_id = app_id
        self.category_name = category_name
        self.using_shared_storage = using_shared_storage
        self.app_description = app_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_username is not None:
            result['CreateUsername'] = self.create_username
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_username is not None:
            result['UpdateUsername'] = self.update_username
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.using_shared_storage is not None:
            result['UsingSharedStorage'] = self.using_shared_storage
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateUsername') is not None:
            self.create_username = m.get('CreateUsername')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUsername') is not None:
            self.update_username = m.get('UpdateUsername')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('UsingSharedStorage') is not None:
            self.using_shared_storage = m.get('UsingSharedStorage')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        application: CreateApplicationResponseBodyApplication = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.application = application

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.application is not None:
            result['Application'] = self.application.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Application') is not None:
            temp_model = CreateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateApplicationResponseBody = None,
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
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigTemplateRequest(TeaModel):
    def __init__(
        self,
        template_name: str = None,
        template_description: str = None,
        app_id: str = None,
        stack_id: str = None,
        source_template_id: str = None,
        source_env_id: str = None,
        profile_name: str = None,
        pkg_version_id: str = None,
        option_settings: str = None,
    ):
        self.template_name = template_name
        self.template_description = template_description
        self.app_id = app_id
        self.stack_id = stack_id
        self.source_template_id = source_template_id
        self.source_env_id = source_env_id
        self.profile_name = profile_name
        self.pkg_version_id = pkg_version_id
        self.option_settings = option_settings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.source_template_id is not None:
            result['SourceTemplateId'] = self.source_template_id
        if self.source_env_id is not None:
            result['SourceEnvId'] = self.source_env_id
        if self.profile_name is not None:
            result['ProfileName'] = self.profile_name
        if self.pkg_version_id is not None:
            result['PkgVersionId'] = self.pkg_version_id
        if self.option_settings is not None:
            result['OptionSettings'] = self.option_settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('SourceTemplateId') is not None:
            self.source_template_id = m.get('SourceTemplateId')
        if m.get('SourceEnvId') is not None:
            self.source_env_id = m.get('SourceEnvId')
        if m.get('ProfileName') is not None:
            self.profile_name = m.get('ProfileName')
        if m.get('PkgVersionId') is not None:
            self.pkg_version_id = m.get('PkgVersionId')
        if m.get('OptionSettings') is not None:
            self.option_settings = m.get('OptionSettings')
        return self


class CreateConfigTemplateResponseBodyConfigTemplate(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        create_time: int = None,
        template_type: str = None,
        stack_name: str = None,
        pkg_version_id: str = None,
        template_name: str = None,
        template_description: str = None,
        app_name: str = None,
        stack_id: str = None,
        pkg_version_label: str = None,
        app_id: str = None,
        template_id: str = None,
    ):
        self.update_time = update_time
        self.create_time = create_time
        self.template_type = template_type
        self.stack_name = stack_name
        self.pkg_version_id = pkg_version_id
        self.template_name = template_name
        self.template_description = template_description
        self.app_name = app_name
        self.stack_id = stack_id
        self.pkg_version_label = pkg_version_label
        self.app_id = app_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.pkg_version_id is not None:
            result['PkgVersionId'] = self.pkg_version_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.pkg_version_label is not None:
            result['PkgVersionLabel'] = self.pkg_version_label
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('PkgVersionId') is not None:
            self.pkg_version_id = m.get('PkgVersionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('PkgVersionLabel') is not None:
            self.pkg_version_label = m.get('PkgVersionLabel')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateConfigTemplateResponseBody(TeaModel):
    def __init__(
        self,
        config_template: CreateConfigTemplateResponseBodyConfigTemplate = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.config_template = config_template
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.config_template:
            self.config_template.validate()

    def to_map(self):
        result = dict()
        if self.config_template is not None:
            result['ConfigTemplate'] = self.config_template.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigTemplate') is not None:
            temp_model = CreateConfigTemplateResponseBodyConfigTemplate()
            self.config_template = temp_model.from_map(m['ConfigTemplate'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateConfigTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConfigTemplateResponseBody = None,
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
            temp_model = CreateConfigTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        product_name: str = None,
    ):
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class CreateOrderResponseBodyOrderDetail(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        order_detail: CreateOrderResponseBodyOrderDetail = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.order_detail = order_detail
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.order_detail:
            self.order_detail.validate()

    def to_map(self):
        result = dict()
        if self.order_detail is not None:
            result['OrderDetail'] = self.order_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderDetail') is not None:
            temp_model = CreateOrderResponseBodyOrderDetail()
            self.order_detail = temp_model.from_map(m['OrderDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOrderResponseBody = None,
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
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePkgVersionRequest(TeaModel):
    def __init__(
        self,
        pkg_version_label: str = None,
        pkg_version_description: str = None,
        app_id: str = None,
        package_source: str = None,
    ):
        self.pkg_version_label = pkg_version_label
        self.pkg_version_description = pkg_version_description
        self.app_id = app_id
        self.package_source = package_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pkg_version_label is not None:
            result['PkgVersionLabel'] = self.pkg_version_label
        if self.pkg_version_description is not None:
            result['PkgVersionDescription'] = self.pkg_version_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.package_source is not None:
            result['PackageSource'] = self.package_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PkgVersionLabel') is not None:
            self.pkg_version_label = m.get('PkgVersionLabel')
        if m.get('PkgVersionDescription') is not None:
            self.pkg_version_description = m.get('PkgVersionDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PackageSource') is not None:
            self.package_source = m.get('PackageSource')
        return self


class CreatePkgVersionResponseBodyPkgVersion(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        update_time: int = None,
        pkg_version_label: str = None,
        create_time: int = None,
        app_id: str = None,
        package_source: str = None,
        pkg_version_id: str = None,
        pkg_version_description: str = None,
    ):
        self.app_name = app_name
        self.update_time = update_time
        self.pkg_version_label = pkg_version_label
        self.create_time = create_time
        self.app_id = app_id
        self.package_source = package_source
        self.pkg_version_id = pkg_version_id
        self.pkg_version_description = pkg_version_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.pkg_version_label is not None:
            result['PkgVersionLabel'] = self.pkg_version_label
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.package_source is not None:
            result['PackageSource'] = self.package_source
        if self.pkg_version_id is not None:
            result['PkgVersionId'] = self.pkg_version_id
        if self.pkg_version_description is not None:
            result['PkgVersionDescription'] = self.pkg_version_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('PkgVersionLabel') is not None:
            self.pkg_version_label = m.get('PkgVersionLabel')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PackageSource') is not None:
            self.package_source = m.get('PackageSource')
        if m.get('PkgVersionId') is not None:
            self.pkg_version_id = m.get('PkgVersionId')
        if m.get('PkgVersionDescription') is not None:
            self.pkg_version_description = m.get('PkgVersionDescription')
        return self


class CreatePkgVersionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        pkg_version: CreatePkgVersionResponseBodyPkgVersion = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.pkg_version = pkg_version
        self.code = code

    def validate(self):
        if self.pkg_version:
            self.pkg_version.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pkg_version is not None:
            result['PkgVersion'] = self.pkg_version.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PkgVersion') is not None:
            temp_model = CreatePkgVersionResponseBodyPkgVersion()
            self.pkg_version = temp_model.from_map(m['PkgVersion'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreatePkgVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePkgVersionResponseBody = None,
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
            temp_model = CreatePkgVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStorageResponseBodyStorage(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        create_time: int = None,
        bucket_name: str = None,
    ):
        self.update_time = update_time
        self.create_time = create_time
        self.bucket_name = bucket_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        return self


class CreateStorageResponseBody(TeaModel):
    def __init__(
        self,
        storage: CreateStorageResponseBodyStorage = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.storage = storage
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.storage:
            self.storage.validate()

    def to_map(self):
        result = dict()
        if self.storage is not None:
            result['Storage'] = self.storage.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Storage') is not None:
            temp_model = CreateStorageResponseBodyStorage()
            self.storage = temp_model.from_map(m['Storage'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateStorageResponseBody = None,
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
            temp_model = CreateStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppEnvRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
    ):
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class DeleteAppEnvResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteAppEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAppEnvResponseBody = None,
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
            temp_model = DeleteAppEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteApplicationResponseBody = None,
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
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChangeRequest(TeaModel):
    def __init__(
        self,
        change_id: str = None,
    ):
        self.change_id = change_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        return self


class DeleteChangeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteChangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteChangeResponseBody = None,
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
            temp_model = DeleteChangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConfigTemplateRequest(TeaModel):
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


class DeleteConfigTemplateResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteConfigTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConfigTemplateResponseBody = None,
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
            temp_model = DeleteConfigTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePkgVersionRequest(TeaModel):
    def __init__(
        self,
        pkg_version_id: str = None,
    ):
        self.pkg_version_id = pkg_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pkg_version_id is not None:
            result['PkgVersionId'] = self.pkg_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PkgVersionId') is not None:
            self.pkg_version_id = m.get('PkgVersionId')
        return self


class DeletePkgVersionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeletePkgVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePkgVersionResponseBody = None,
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
            temp_model = DeletePkgVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployAppEnvRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        batch_size: int = None,
        batch_percent: int = None,
        batch_interval: int = None,
        pause_between_batches: bool = None,
        pkg_version_id: str = None,
    ):
        self.env_id = env_id
        self.batch_size = batch_size
        self.batch_percent = batch_percent
        self.batch_interval = batch_interval
        self.pause_between_batches = pause_between_batches
        self.pkg_version_id = pkg_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.batch_percent is not None:
            result['BatchPercent'] = self.batch_percent
        if self.batch_interval is not None:
            result['BatchInterval'] = self.batch_interval
        if self.pause_between_batches is not None:
            result['PauseBetweenBatches'] = self.pause_between_batches
        if self.pkg_version_id is not None:
            result['PkgVersionId'] = self.pkg_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('BatchPercent') is not None:
            self.batch_percent = m.get('BatchPercent')
        if m.get('BatchInterval') is not None:
            self.batch_interval = m.get('BatchInterval')
        if m.get('PauseBetweenBatches') is not None:
            self.pause_between_batches = m.get('PauseBetweenBatches')
        if m.get('PkgVersionId') is not None:
            self.pkg_version_id = m.get('PkgVersionId')
        return self


class DeployAppEnvResponseBodyEnvChange(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class DeployAppEnvResponseBody(TeaModel):
    def __init__(
        self,
        env_change: DeployAppEnvResponseBodyEnvChange = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.env_change = env_change
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.env_change:
            self.env_change.validate()

    def to_map(self):
        result = dict()
        if self.env_change is not None:
            result['EnvChange'] = self.env_change.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvChange') is not None:
            temp_model = DeployAppEnvResponseBodyEnvChange()
            self.env_change = temp_model.from_map(m['EnvChange'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeployAppEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployAppEnvResponseBody = None,
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
            temp_model = DeployAppEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppEnvInstanceHealthRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
    ):
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class DescribeAppEnvInstanceHealthResponseBodyEnvInstanceHealthInstanceHealthListInstanceHealth(TeaModel):
    def __init__(
        self,
        app_status: str = None,
        instance_id: str = None,
        disconnected_time: str = None,
        agent_status: str = None,
    ):
        self.app_status = app_status
        self.instance_id = instance_id
        self.disconnected_time = disconnected_time
        self.agent_status = agent_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.disconnected_time is not None:
            result['DisconnectedTime'] = self.disconnected_time
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DisconnectedTime') is not None:
            self.disconnected_time = m.get('DisconnectedTime')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        return self


class DescribeAppEnvInstanceHealthResponseBodyEnvInstanceHealthInstanceHealthList(TeaModel):
    def __init__(
        self,
        instance_health: List[DescribeAppEnvInstanceHealthResponseBodyEnvInstanceHealthInstanceHealthListInstanceHealth] = None,
    ):
        self.instance_health = instance_health

    def validate(self):
        if self.instance_health:
            for k in self.instance_health:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceHealth'] = []
        if self.instance_health is not None:
            for k in self.instance_health:
                result['InstanceHealth'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_health = []
        if m.get('InstanceHealth') is not None:
            for k in m.get('InstanceHealth'):
                temp_model = DescribeAppEnvInstanceHealthResponseBodyEnvInstanceHealthInstanceHealthListInstanceHealth()
                self.instance_health.append(temp_model.from_map(k))
        return self


class DescribeAppEnvInstanceHealthResponseBodyEnvInstanceHealth(TeaModel):
    def __init__(
        self,
        enable_health_check: bool = None,
        env_name: str = None,
        env_id: str = None,
        instance_health_list: DescribeAppEnvInstanceHealthResponseBodyEnvInstanceHealthInstanceHealthList = None,
    ):
        self.enable_health_check = enable_health_check
        self.env_name = env_name
        self.env_id = env_id
        self.instance_health_list = instance_health_list

    def validate(self):
        if self.instance_health_list:
            self.instance_health_list.validate()

    def to_map(self):
        result = dict()
        if self.enable_health_check is not None:
            result['EnableHealthCheck'] = self.enable_health_check
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.instance_health_list is not None:
            result['InstanceHealthList'] = self.instance_health_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableHealthCheck') is not None:
            self.enable_health_check = m.get('EnableHealthCheck')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('InstanceHealthList') is not None:
            temp_model = DescribeAppEnvInstanceHealthResponseBodyEnvInstanceHealthInstanceHealthList()
            self.instance_health_list = temp_model.from_map(m['InstanceHealthList'])
        return self


class DescribeAppEnvInstanceHealthResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        env_instance_health: DescribeAppEnvInstanceHealthResponseBodyEnvInstanceHealth = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.env_instance_health = env_instance_health

    def validate(self):
        if self.env_instance_health:
            self.env_instance_health.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.env_instance_health is not None:
            result['EnvInstanceHealth'] = self.env_instance_health.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnvInstanceHealth') is not None:
            temp_model = DescribeAppEnvInstanceHealthResponseBodyEnvInstanceHealth()
            self.env_instance_health = temp_model.from_map(m['EnvInstanceHealth'])
        return self


class DescribeAppEnvInstanceHealthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppEnvInstanceHealthResponseBody = None,
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
            temp_model = DescribeAppEnvInstanceHealthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppEnvsRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        app_id: str = None,
        include_terminated: bool = None,
        page_size: int = None,
        page_number: int = None,
        env_name: str = None,
        env_search: str = None,
        recent_updated: bool = None,
        stack_search: str = None,
    ):
        self.env_id = env_id
        self.app_id = app_id
        self.include_terminated = include_terminated
        self.page_size = page_size
        self.page_number = page_number
        self.env_name = env_name
        self.env_search = env_search
        self.recent_updated = recent_updated
        self.stack_search = stack_search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.include_terminated is not None:
            result['IncludeTerminated'] = self.include_terminated
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.env_search is not None:
            result['EnvSearch'] = self.env_search
        if self.recent_updated is not None:
            result['RecentUpdated'] = self.recent_updated
        if self.stack_search is not None:
            result['StackSearch'] = self.stack_search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('IncludeTerminated') is not None:
            self.include_terminated = m.get('IncludeTerminated')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('EnvSearch') is not None:
            self.env_search = m.get('EnvSearch')
        if m.get('RecentUpdated') is not None:
            self.recent_updated = m.get('RecentUpdated')
        if m.get('StackSearch') is not None:
            self.stack_search = m.get('StackSearch')
        return self


class DescribeAppEnvsResponseBodyAppEnvsAppEnv(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        total_instances: int = None,
        pkg_version_storage_key: str = None,
        latest_change_id: str = None,
        env_status: str = None,
        create_time: int = None,
        last_env_status: str = None,
        pkg_version_id: str = None,
        env_description: str = None,
        applying_change: bool = None,
        env_type: str = None,
        app_name: str = None,
        create_username: str = None,
        app_id: str = None,
        data_root: str = None,
        storage_base: str = None,
        update_username: str = None,
        env_name: str = None,
        log_base: str = None,
        stack_name: str = None,
        category_name: str = None,
        using_shared_storage: bool = None,
        change_banner: str = None,
        stack_id: str = None,
        pkg_version_label: str = None,
        env_id: str = None,
        aborting_change: bool = None,
    ):
        self.update_time = update_time
        self.total_instances = total_instances
        self.pkg_version_storage_key = pkg_version_storage_key
        self.latest_change_id = latest_change_id
        self.env_status = env_status
        self.create_time = create_time
        self.last_env_status = last_env_status
        self.pkg_version_id = pkg_version_id
        self.env_description = env_description
        self.applying_change = applying_change
        self.env_type = env_type
        self.app_name = app_name
        self.create_username = create_username
        self.app_id = app_id
        self.data_root = data_root
        self.storage_base = storage_base
        self.update_username = update_username
        self.env_name = env_name
        self.log_base = log_base
        self.stack_name = stack_name
        self.category_name = category_name
        self.using_shared_storage = using_shared_storage
        self.change_banner = change_banner
        self.stack_id = stack_id
        self.pkg_version_label = pkg_version_label
        self.env_id = env_id
        self.aborting_change = aborting_change

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.total_instances is not None:
            result['TotalInstances'] = self.total_instances
        if self.pkg_version_storage_key is not None:
            result['PkgVersionStorageKey'] = self.pkg_version_storage_key
        if self.latest_change_id is not None:
            result['LatestChangeId'] = self.latest_change_id
        if self.env_status is not None:
            result['EnvStatus'] = self.env_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_env_status is not None:
            result['LastEnvStatus'] = self.last_env_status
        if self.pkg_version_id is not None:
            result['PkgVersionId'] = self.pkg_version_id
        if self.env_description is not None:
            result['EnvDescription'] = self.env_description
        if self.applying_change is not None:
            result['ApplyingChange'] = self.applying_change
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_username is not None:
            result['CreateUsername'] = self.create_username
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.data_root is not None:
            result['DataRoot'] = self.data_root
        if self.storage_base is not None:
            result['StorageBase'] = self.storage_base
        if self.update_username is not None:
            result['UpdateUsername'] = self.update_username
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.log_base is not None:
            result['LogBase'] = self.log_base
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.using_shared_storage is not None:
            result['UsingSharedStorage'] = self.using_shared_storage
        if self.change_banner is not None:
            result['ChangeBanner'] = self.change_banner
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.pkg_version_label is not None:
            result['PkgVersionLabel'] = self.pkg_version_label
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.aborting_change is not None:
            result['AbortingChange'] = self.aborting_change
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('TotalInstances') is not None:
            self.total_instances = m.get('TotalInstances')
        if m.get('PkgVersionStorageKey') is not None:
            self.pkg_version_storage_key = m.get('PkgVersionStorageKey')
        if m.get('LatestChangeId') is not None:
            self.latest_change_id = m.get('LatestChangeId')
        if m.get('EnvStatus') is not None:
            self.env_status = m.get('EnvStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastEnvStatus') is not None:
            self.last_env_status = m.get('LastEnvStatus')
        if m.get('PkgVersionId') is not None:
            self.pkg_version_id = m.get('PkgVersionId')
        if m.get('EnvDescription') is not None:
            self.env_description = m.get('EnvDescription')
        if m.get('ApplyingChange') is not None:
            self.applying_change = m.get('ApplyingChange')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateUsername') is not None:
            self.create_username = m.get('CreateUsername')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DataRoot') is not None:
            self.data_root = m.get('DataRoot')
        if m.get('StorageBase') is not None:
            self.storage_base = m.get('StorageBase')
        if m.get('UpdateUsername') is not None:
            self.update_username = m.get('UpdateUsername')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('LogBase') is not None:
            self.log_base = m.get('LogBase')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('UsingSharedStorage') is not None:
            self.using_shared_storage = m.get('UsingSharedStorage')
        if m.get('ChangeBanner') is not None:
            self.change_banner = m.get('ChangeBanner')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('PkgVersionLabel') is not None:
            self.pkg_version_label = m.get('PkgVersionLabel')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('AbortingChange') is not None:
            self.aborting_change = m.get('AbortingChange')
        return self


class DescribeAppEnvsResponseBodyAppEnvs(TeaModel):
    def __init__(
        self,
        app_env: List[DescribeAppEnvsResponseBodyAppEnvsAppEnv] = None,
    ):
        self.app_env = app_env

    def validate(self):
        if self.app_env:
            for k in self.app_env:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AppEnv'] = []
        if self.app_env is not None:
            for k in self.app_env:
                result['AppEnv'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_env = []
        if m.get('AppEnv') is not None:
            for k in m.get('AppEnv'):
                temp_model = DescribeAppEnvsResponseBodyAppEnvsAppEnv()
                self.app_env.append(temp_model.from_map(k))
        return self


class DescribeAppEnvsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        app_envs: DescribeAppEnvsResponseBodyAppEnvs = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.app_envs = app_envs
        self.code = code

    def validate(self):
        if self.app_envs:
            self.app_envs.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.app_envs is not None:
            result['AppEnvs'] = self.app_envs.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('AppEnvs') is not None:
            temp_model = DescribeAppEnvsResponseBodyAppEnvs()
            self.app_envs = temp_model.from_map(m['AppEnvs'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeAppEnvsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppEnvsResponseBody = None,
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
            temp_model = DescribeAppEnvsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppEnvStatusRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
    ):
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class DescribeAppEnvStatusResponseBodyEnvStatusInstanceAgentStatus(TeaModel):
    def __init__(
        self,
        connected_instances: int = None,
        disconnected_instances: int = None,
    ):
        self.connected_instances = connected_instances
        self.disconnected_instances = disconnected_instances

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.connected_instances is not None:
            result['ConnectedInstances'] = self.connected_instances
        if self.disconnected_instances is not None:
            result['DisconnectedInstances'] = self.disconnected_instances
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectedInstances') is not None:
            self.connected_instances = m.get('ConnectedInstances')
        if m.get('DisconnectedInstances') is not None:
            self.disconnected_instances = m.get('DisconnectedInstances')
        return self


class DescribeAppEnvStatusResponseBodyEnvStatusInstanceAppStatus(TeaModel):
    def __init__(
        self,
        healthy_instances: int = None,
        stopped_instances: int = None,
        unhealthy_instances: int = None,
        unknown_instances: int = None,
    ):
        self.healthy_instances = healthy_instances
        self.stopped_instances = stopped_instances
        self.unhealthy_instances = unhealthy_instances
        self.unknown_instances = unknown_instances

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.healthy_instances is not None:
            result['HealthyInstances'] = self.healthy_instances
        if self.stopped_instances is not None:
            result['StoppedInstances'] = self.stopped_instances
        if self.unhealthy_instances is not None:
            result['UnhealthyInstances'] = self.unhealthy_instances
        if self.unknown_instances is not None:
            result['UnknownInstances'] = self.unknown_instances
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthyInstances') is not None:
            self.healthy_instances = m.get('HealthyInstances')
        if m.get('StoppedInstances') is not None:
            self.stopped_instances = m.get('StoppedInstances')
        if m.get('UnhealthyInstances') is not None:
            self.unhealthy_instances = m.get('UnhealthyInstances')
        if m.get('UnknownInstances') is not None:
            self.unknown_instances = m.get('UnknownInstances')
        return self


class DescribeAppEnvStatusResponseBodyEnvStatus(TeaModel):
    def __init__(
        self,
        change_banner: str = None,
        latest_change_id: str = None,
        env_status: str = None,
        env_name: str = None,
        instance_agent_status: DescribeAppEnvStatusResponseBodyEnvStatusInstanceAgentStatus = None,
        last_env_status: str = None,
        instance_app_status: DescribeAppEnvStatusResponseBodyEnvStatusInstanceAppStatus = None,
        env_id: str = None,
        aborting_change: bool = None,
        applying_change: bool = None,
    ):
        self.change_banner = change_banner
        self.latest_change_id = latest_change_id
        self.env_status = env_status
        self.env_name = env_name
        self.instance_agent_status = instance_agent_status
        self.last_env_status = last_env_status
        self.instance_app_status = instance_app_status
        self.env_id = env_id
        self.aborting_change = aborting_change
        self.applying_change = applying_change

    def validate(self):
        if self.instance_agent_status:
            self.instance_agent_status.validate()
        if self.instance_app_status:
            self.instance_app_status.validate()

    def to_map(self):
        result = dict()
        if self.change_banner is not None:
            result['ChangeBanner'] = self.change_banner
        if self.latest_change_id is not None:
            result['LatestChangeId'] = self.latest_change_id
        if self.env_status is not None:
            result['EnvStatus'] = self.env_status
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.instance_agent_status is not None:
            result['InstanceAgentStatus'] = self.instance_agent_status.to_map()
        if self.last_env_status is not None:
            result['LastEnvStatus'] = self.last_env_status
        if self.instance_app_status is not None:
            result['InstanceAppStatus'] = self.instance_app_status.to_map()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.aborting_change is not None:
            result['AbortingChange'] = self.aborting_change
        if self.applying_change is not None:
            result['ApplyingChange'] = self.applying_change
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeBanner') is not None:
            self.change_banner = m.get('ChangeBanner')
        if m.get('LatestChangeId') is not None:
            self.latest_change_id = m.get('LatestChangeId')
        if m.get('EnvStatus') is not None:
            self.env_status = m.get('EnvStatus')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('InstanceAgentStatus') is not None:
            temp_model = DescribeAppEnvStatusResponseBodyEnvStatusInstanceAgentStatus()
            self.instance_agent_status = temp_model.from_map(m['InstanceAgentStatus'])
        if m.get('LastEnvStatus') is not None:
            self.last_env_status = m.get('LastEnvStatus')
        if m.get('InstanceAppStatus') is not None:
            temp_model = DescribeAppEnvStatusResponseBodyEnvStatusInstanceAppStatus()
            self.instance_app_status = temp_model.from_map(m['InstanceAppStatus'])
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('AbortingChange') is not None:
            self.aborting_change = m.get('AbortingChange')
        if m.get('ApplyingChange') is not None:
            self.applying_change = m.get('ApplyingChange')
        return self


class DescribeAppEnvStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        env_status: DescribeAppEnvStatusResponseBodyEnvStatus = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.env_status = env_status
        self.code = code

    def validate(self):
        if self.env_status:
            self.env_status.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.env_status is not None:
            result['EnvStatus'] = self.env_status.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EnvStatus') is not None:
            temp_model = DescribeAppEnvStatusResponseBodyEnvStatus()
            self.env_status = temp_model.from_map(m['EnvStatus'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeAppEnvStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppEnvStatusResponseBody = None,
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
            temp_model = DescribeAppEnvStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_size: int = None,
        page_number: int = None,
        app_name: str = None,
        app_search: str = None,
        env_search: str = None,
        stack_search: str = None,
        category_search: str = None,
    ):
        self.app_id = app_id
        self.page_size = page_size
        self.page_number = page_number
        self.app_name = app_name
        self.app_search = app_search
        self.env_search = env_search
        self.stack_search = stack_search
        self.category_search = category_search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_search is not None:
            result['AppSearch'] = self.app_search
        if self.env_search is not None:
            result['EnvSearch'] = self.env_search
        if self.stack_search is not None:
            result['StackSearch'] = self.stack_search
        if self.category_search is not None:
            result['CategorySearch'] = self.category_search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppSearch') is not None:
            self.app_search = m.get('AppSearch')
        if m.get('EnvSearch') is not None:
            self.env_search = m.get('EnvSearch')
        if m.get('StackSearch') is not None:
            self.stack_search = m.get('StackSearch')
        if m.get('CategorySearch') is not None:
            self.category_search = m.get('CategorySearch')
        return self


class DescribeApplicationsResponseBodyApplicationsApplication(TeaModel):
    def __init__(
        self,
        total_envs: int = None,
        update_time: int = None,
        update_username: str = None,
        running_envs: int = None,
        create_time: int = None,
        category_name: str = None,
        using_shared_storage: str = None,
        create_username: str = None,
        app_name: str = None,
        app_id: str = None,
        terminated_envs: int = None,
        app_description: str = None,
    ):
        self.total_envs = total_envs
        self.update_time = update_time
        self.update_username = update_username
        self.running_envs = running_envs
        self.create_time = create_time
        self.category_name = category_name
        self.using_shared_storage = using_shared_storage
        self.create_username = create_username
        self.app_name = app_name
        self.app_id = app_id
        self.terminated_envs = terminated_envs
        self.app_description = app_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_envs is not None:
            result['TotalEnvs'] = self.total_envs
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_username is not None:
            result['UpdateUsername'] = self.update_username
        if self.running_envs is not None:
            result['RunningEnvs'] = self.running_envs
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.using_shared_storage is not None:
            result['UsingSharedStorage'] = self.using_shared_storage
        if self.create_username is not None:
            result['CreateUsername'] = self.create_username
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.terminated_envs is not None:
            result['TerminatedEnvs'] = self.terminated_envs
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalEnvs') is not None:
            self.total_envs = m.get('TotalEnvs')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUsername') is not None:
            self.update_username = m.get('UpdateUsername')
        if m.get('RunningEnvs') is not None:
            self.running_envs = m.get('RunningEnvs')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('UsingSharedStorage') is not None:
            self.using_shared_storage = m.get('UsingSharedStorage')
        if m.get('CreateUsername') is not None:
            self.create_username = m.get('CreateUsername')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TerminatedEnvs') is not None:
            self.terminated_envs = m.get('TerminatedEnvs')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        return self


class DescribeApplicationsResponseBodyApplications(TeaModel):
    def __init__(
        self,
        application: List[DescribeApplicationsResponseBodyApplicationsApplication] = None,
    ):
        self.application = application

    def validate(self):
        if self.application:
            for k in self.application:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application = []
        if m.get('Application') is not None:
            for k in m.get('Application'):
                temp_model = DescribeApplicationsResponseBodyApplicationsApplication()
                self.application.append(temp_model.from_map(k))
        return self


class DescribeApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        applications: DescribeApplicationsResponseBodyApplications = None,
        page_number: int = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.applications = applications
        self.page_number = page_number
        self.code = code

    def validate(self):
        if self.applications:
            self.applications.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Applications') is not None:
            temp_model = DescribeApplicationsResponseBodyApplications()
            self.applications = temp_model.from_map(m['Applications'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApplicationsResponseBody = None,
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
            temp_model = DescribeApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCategoriesResponseBodyCategoriesCategoryDemoProjectsDemoProject(TeaModel):
    def __init__(
        self,
        source_url: str = None,
        package_download_url: str = None,
        package_url: str = None,
        region_id: str = None,
    ):
        self.source_url = source_url
        self.package_download_url = package_download_url
        self.package_url = package_url
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.package_download_url is not None:
            result['PackageDownloadUrl'] = self.package_download_url
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('PackageDownloadUrl') is not None:
            self.package_download_url = m.get('PackageDownloadUrl')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCategoriesResponseBodyCategoriesCategoryDemoProjects(TeaModel):
    def __init__(
        self,
        demo_project: List[DescribeCategoriesResponseBodyCategoriesCategoryDemoProjectsDemoProject] = None,
    ):
        self.demo_project = demo_project

    def validate(self):
        if self.demo_project:
            for k in self.demo_project:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DemoProject'] = []
        if self.demo_project is not None:
            for k in self.demo_project:
                result['DemoProject'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.demo_project = []
        if m.get('DemoProject') is not None:
            for k in m.get('DemoProject'):
                temp_model = DescribeCategoriesResponseBodyCategoriesCategoryDemoProjectsDemoProject()
                self.demo_project.append(temp_model.from_map(k))
        return self


class DescribeCategoriesResponseBodyCategoriesCategory(TeaModel):
    def __init__(
        self,
        category_logo: str = None,
        update_time: str = None,
        demo_projects: DescribeCategoriesResponseBodyCategoriesCategoryDemoProjects = None,
        create_time: str = None,
        category_id: str = None,
        category_name: str = None,
        category_description: str = None,
    ):
        self.category_logo = category_logo
        self.update_time = update_time
        self.demo_projects = demo_projects
        self.create_time = create_time
        self.category_id = category_id
        self.category_name = category_name
        self.category_description = category_description

    def validate(self):
        if self.demo_projects:
            self.demo_projects.validate()

    def to_map(self):
        result = dict()
        if self.category_logo is not None:
            result['CategoryLogo'] = self.category_logo
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.demo_projects is not None:
            result['DemoProjects'] = self.demo_projects.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.category_description is not None:
            result['CategoryDescription'] = self.category_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryLogo') is not None:
            self.category_logo = m.get('CategoryLogo')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DemoProjects') is not None:
            temp_model = DescribeCategoriesResponseBodyCategoriesCategoryDemoProjects()
            self.demo_projects = temp_model.from_map(m['DemoProjects'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CategoryDescription') is not None:
            self.category_description = m.get('CategoryDescription')
        return self


class DescribeCategoriesResponseBodyCategories(TeaModel):
    def __init__(
        self,
        category: List[DescribeCategoriesResponseBodyCategoriesCategory] = None,
    ):
        self.category = category

    def validate(self):
        if self.category:
            for k in self.category:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Category'] = []
        if self.category is not None:
            for k in self.category:
                result['Category'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category = []
        if m.get('Category') is not None:
            for k in m.get('Category'):
                temp_model = DescribeCategoriesResponseBodyCategoriesCategory()
                self.category.append(temp_model.from_map(k))
        return self


class DescribeCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        categories: DescribeCategoriesResponseBodyCategories = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.categories = categories
        self.code = code

    def validate(self):
        if self.categories:
            self.categories.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.categories is not None:
            result['Categories'] = self.categories.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Categories') is not None:
            temp_model = DescribeCategoriesResponseBodyCategories()
            self.categories = temp_model.from_map(m['Categories'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCategoriesResponseBody = None,
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
            temp_model = DescribeCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChangeRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        change_id: str = None,
    ):
        self.env_id = env_id
        self.change_id = change_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        return self


class DescribeChangeResponseBodyChange(TeaModel):
    def __init__(
        self,
        change_paused: bool = None,
        change_description: str = None,
        finish_time: int = None,
        update_time: int = None,
        change_timedout: bool = None,
        create_time: int = None,
        change_message: str = None,
        action_name: str = None,
        change_finished: bool = None,
        create_username: str = None,
        change_id: str = None,
        change_aborted: bool = None,
        change_succeed: bool = None,
        env_id: str = None,
        change_name: str = None,
    ):
        self.change_paused = change_paused
        self.change_description = change_description
        self.finish_time = finish_time
        self.update_time = update_time
        self.change_timedout = change_timedout
        self.create_time = create_time
        self.change_message = change_message
        self.action_name = action_name
        self.change_finished = change_finished
        self.create_username = create_username
        self.change_id = change_id
        self.change_aborted = change_aborted
        self.change_succeed = change_succeed
        self.env_id = env_id
        self.change_name = change_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.change_paused is not None:
            result['ChangePaused'] = self.change_paused
        if self.change_description is not None:
            result['ChangeDescription'] = self.change_description
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.change_timedout is not None:
            result['ChangeTimedout'] = self.change_timedout
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.change_message is not None:
            result['ChangeMessage'] = self.change_message
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.change_finished is not None:
            result['ChangeFinished'] = self.change_finished
        if self.create_username is not None:
            result['CreateUsername'] = self.create_username
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.change_aborted is not None:
            result['ChangeAborted'] = self.change_aborted
        if self.change_succeed is not None:
            result['ChangeSucceed'] = self.change_succeed
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.change_name is not None:
            result['ChangeName'] = self.change_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangePaused') is not None:
            self.change_paused = m.get('ChangePaused')
        if m.get('ChangeDescription') is not None:
            self.change_description = m.get('ChangeDescription')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ChangeTimedout') is not None:
            self.change_timedout = m.get('ChangeTimedout')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChangeMessage') is not None:
            self.change_message = m.get('ChangeMessage')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ChangeFinished') is not None:
            self.change_finished = m.get('ChangeFinished')
        if m.get('CreateUsername') is not None:
            self.create_username = m.get('CreateUsername')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('ChangeAborted') is not None:
            self.change_aborted = m.get('ChangeAborted')
        if m.get('ChangeSucceed') is not None:
            self.change_succeed = m.get('ChangeSucceed')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ChangeName') is not None:
            self.change_name = m.get('ChangeName')
        return self


class DescribeChangeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        change: DescribeChangeResponseBodyChange = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.change = change
        self.code = code

    def validate(self):
        if self.change:
            self.change.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.change is not None:
            result['Change'] = self.change.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Change') is not None:
            temp_model = DescribeChangeResponseBodyChange()
            self.change = temp_model.from_map(m['Change'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeChangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChangeResponseBody = None,
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
            temp_model = DescribeChangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChangesRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        action_name: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.env_id = env_id
        self.action_name = action_name
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeChangesResponseBodyChangesChange(TeaModel):
    def __init__(
        self,
        change_paused: bool = None,
        change_description: str = None,
        finish_time: int = None,
        update_time: int = None,
        change_timedout: bool = None,
        create_time: int = None,
        change_message: str = None,
        action_name: str = None,
        change_finished: bool = None,
        create_username: str = None,
        change_id: str = None,
        change_aborted: bool = None,
        change_succeed: bool = None,
        env_id: str = None,
        change_name: str = None,
    ):
        self.change_paused = change_paused
        self.change_description = change_description
        self.finish_time = finish_time
        self.update_time = update_time
        self.change_timedout = change_timedout
        self.create_time = create_time
        self.change_message = change_message
        self.action_name = action_name
        self.change_finished = change_finished
        self.create_username = create_username
        self.change_id = change_id
        self.change_aborted = change_aborted
        self.change_succeed = change_succeed
        self.env_id = env_id
        self.change_name = change_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.change_paused is not None:
            result['ChangePaused'] = self.change_paused
        if self.change_description is not None:
            result['ChangeDescription'] = self.change_description
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.change_timedout is not None:
            result['ChangeTimedout'] = self.change_timedout
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.change_message is not None:
            result['ChangeMessage'] = self.change_message
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.change_finished is not None:
            result['ChangeFinished'] = self.change_finished
        if self.create_username is not None:
            result['CreateUsername'] = self.create_username
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.change_aborted is not None:
            result['ChangeAborted'] = self.change_aborted
        if self.change_succeed is not None:
            result['ChangeSucceed'] = self.change_succeed
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.change_name is not None:
            result['ChangeName'] = self.change_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangePaused') is not None:
            self.change_paused = m.get('ChangePaused')
        if m.get('ChangeDescription') is not None:
            self.change_description = m.get('ChangeDescription')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ChangeTimedout') is not None:
            self.change_timedout = m.get('ChangeTimedout')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChangeMessage') is not None:
            self.change_message = m.get('ChangeMessage')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ChangeFinished') is not None:
            self.change_finished = m.get('ChangeFinished')
        if m.get('CreateUsername') is not None:
            self.create_username = m.get('CreateUsername')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('ChangeAborted') is not None:
            self.change_aborted = m.get('ChangeAborted')
        if m.get('ChangeSucceed') is not None:
            self.change_succeed = m.get('ChangeSucceed')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ChangeName') is not None:
            self.change_name = m.get('ChangeName')
        return self


class DescribeChangesResponseBodyChanges(TeaModel):
    def __init__(
        self,
        change: List[DescribeChangesResponseBodyChangesChange] = None,
    ):
        self.change = change

    def validate(self):
        if self.change:
            for k in self.change:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Change'] = []
        if self.change is not None:
            for k in self.change:
                result['Change'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change = []
        if m.get('Change') is not None:
            for k in m.get('Change'):
                temp_model = DescribeChangesResponseBodyChangesChange()
                self.change.append(temp_model.from_map(k))
        return self


class DescribeChangesResponseBody(TeaModel):
    def __init__(
        self,
        changes: DescribeChangesResponseBodyChanges = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        code: str = None,
    ):
        self.changes = changes
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.code = code

    def validate(self):
        if self.changes:
            self.changes.validate()

    def to_map(self):
        result = dict()
        if self.changes is not None:
            result['Changes'] = self.changes.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Changes') is not None:
            temp_model = DescribeChangesResponseBodyChanges()
            self.changes = temp_model.from_map(m['Changes'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeChangesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChangesResponseBody = None,
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
            temp_model = DescribeChangesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigIndexRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        env_id: str = None,
        profile_name: str = None,
        template_id: str = None,
    ):
        self.stack_id = stack_id
        self.env_id = env_id
        self.profile_name = profile_name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.profile_name is not None:
            result['ProfileName'] = self.profile_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ProfileName') is not None:
            self.profile_name = m.get('ProfileName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPathsConfigPathConfigOptionsConfigOption(TeaModel):
    def __init__(
        self,
        regex_desc: str = None,
        max_value: int = None,
        editor_type: str = None,
        min_value: int = None,
        option_label: str = None,
        default_value: str = None,
        max_length: int = None,
        regex_pattern: str = None,
        change_severity: str = None,
        option_description: str = None,
        option_name: str = None,
        path_name: str = None,
        hidden_option: bool = None,
        value_type: str = None,
        min_length: int = None,
        value_options: str = None,
        readonly_option: bool = None,
    ):
        self.regex_desc = regex_desc
        self.max_value = max_value
        self.editor_type = editor_type
        self.min_value = min_value
        self.option_label = option_label
        self.default_value = default_value
        self.max_length = max_length
        self.regex_pattern = regex_pattern
        self.change_severity = change_severity
        self.option_description = option_description
        self.option_name = option_name
        self.path_name = path_name
        self.hidden_option = hidden_option
        self.value_type = value_type
        self.min_length = min_length
        self.value_options = value_options
        self.readonly_option = readonly_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.regex_desc is not None:
            result['RegexDesc'] = self.regex_desc
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.editor_type is not None:
            result['EditorType'] = self.editor_type
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.option_label is not None:
            result['OptionLabel'] = self.option_label
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.regex_pattern is not None:
            result['RegexPattern'] = self.regex_pattern
        if self.change_severity is not None:
            result['ChangeSeverity'] = self.change_severity
        if self.option_description is not None:
            result['OptionDescription'] = self.option_description
        if self.option_name is not None:
            result['OptionName'] = self.option_name
        if self.path_name is not None:
            result['PathName'] = self.path_name
        if self.hidden_option is not None:
            result['HiddenOption'] = self.hidden_option
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.value_options is not None:
            result['ValueOptions'] = self.value_options
        if self.readonly_option is not None:
            result['ReadonlyOption'] = self.readonly_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegexDesc') is not None:
            self.regex_desc = m.get('RegexDesc')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('EditorType') is not None:
            self.editor_type = m.get('EditorType')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('OptionLabel') is not None:
            self.option_label = m.get('OptionLabel')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('RegexPattern') is not None:
            self.regex_pattern = m.get('RegexPattern')
        if m.get('ChangeSeverity') is not None:
            self.change_severity = m.get('ChangeSeverity')
        if m.get('OptionDescription') is not None:
            self.option_description = m.get('OptionDescription')
        if m.get('OptionName') is not None:
            self.option_name = m.get('OptionName')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        if m.get('HiddenOption') is not None:
            self.hidden_option = m.get('HiddenOption')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('ValueOptions') is not None:
            self.value_options = m.get('ValueOptions')
        if m.get('ReadonlyOption') is not None:
            self.readonly_option = m.get('ReadonlyOption')
        return self


class DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPathsConfigPathConfigOptions(TeaModel):
    def __init__(
        self,
        config_option: List[DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPathsConfigPathConfigOptionsConfigOption] = None,
    ):
        self.config_option = config_option

    def validate(self):
        if self.config_option:
            for k in self.config_option:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConfigOption'] = []
        if self.config_option is not None:
            for k in self.config_option:
                result['ConfigOption'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_option = []
        if m.get('ConfigOption') is not None:
            for k in m.get('ConfigOption'):
                temp_model = DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPathsConfigPathConfigOptionsConfigOption()
                self.config_option.append(temp_model.from_map(k))
        return self


class DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPathsConfigPath(TeaModel):
    def __init__(
        self,
        path_name: str = None,
        hidden_path: bool = None,
        config_options: DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPathsConfigPathConfigOptions = None,
        path_label: str = None,
    ):
        self.path_name = path_name
        self.hidden_path = hidden_path
        self.config_options = config_options
        self.path_label = path_label

    def validate(self):
        if self.config_options:
            self.config_options.validate()

    def to_map(self):
        result = dict()
        if self.path_name is not None:
            result['PathName'] = self.path_name
        if self.hidden_path is not None:
            result['HiddenPath'] = self.hidden_path
        if self.config_options is not None:
            result['ConfigOptions'] = self.config_options.to_map()
        if self.path_label is not None:
            result['PathLabel'] = self.path_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        if m.get('HiddenPath') is not None:
            self.hidden_path = m.get('HiddenPath')
        if m.get('ConfigOptions') is not None:
            temp_model = DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPathsConfigPathConfigOptions()
            self.config_options = temp_model.from_map(m['ConfigOptions'])
        if m.get('PathLabel') is not None:
            self.path_label = m.get('PathLabel')
        return self


class DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPaths(TeaModel):
    def __init__(
        self,
        config_path: List[DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPathsConfigPath] = None,
    ):
        self.config_path = config_path

    def validate(self):
        if self.config_path:
            for k in self.config_path:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConfigPath'] = []
        if self.config_path is not None:
            for k in self.config_path:
                result['ConfigPath'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_path = []
        if m.get('ConfigPath') is not None:
            for k in m.get('ConfigPath'):
                temp_model = DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPathsConfigPath()
                self.config_path.append(temp_model.from_map(k))
        return self


class DescribeConfigIndexResponseBodyConfigGroupsConfigGroup(TeaModel):
    def __init__(
        self,
        config_paths: DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPaths = None,
        group_name: str = None,
        group_label: str = None,
    ):
        self.config_paths = config_paths
        self.group_name = group_name
        self.group_label = group_label

    def validate(self):
        if self.config_paths:
            self.config_paths.validate()

    def to_map(self):
        result = dict()
        if self.config_paths is not None:
            result['ConfigPaths'] = self.config_paths.to_map()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_label is not None:
            result['GroupLabel'] = self.group_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigPaths') is not None:
            temp_model = DescribeConfigIndexResponseBodyConfigGroupsConfigGroupConfigPaths()
            self.config_paths = temp_model.from_map(m['ConfigPaths'])
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupLabel') is not None:
            self.group_label = m.get('GroupLabel')
        return self


class DescribeConfigIndexResponseBodyConfigGroups(TeaModel):
    def __init__(
        self,
        config_group: List[DescribeConfigIndexResponseBodyConfigGroupsConfigGroup] = None,
    ):
        self.config_group = config_group

    def validate(self):
        if self.config_group:
            for k in self.config_group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConfigGroup'] = []
        if self.config_group is not None:
            for k in self.config_group:
                result['ConfigGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_group = []
        if m.get('ConfigGroup') is not None:
            for k in m.get('ConfigGroup'):
                temp_model = DescribeConfigIndexResponseBodyConfigGroupsConfigGroup()
                self.config_group.append(temp_model.from_map(k))
        return self


class DescribeConfigIndexResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        config_groups: DescribeConfigIndexResponseBodyConfigGroups = None,
        code: str = None,
        stack_name: str = None,
        stack_id: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.config_groups = config_groups
        self.code = code
        self.stack_name = stack_name
        self.stack_id = stack_id

    def validate(self):
        if self.config_groups:
            self.config_groups.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_groups is not None:
            result['ConfigGroups'] = self.config_groups.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigGroups') is not None:
            temp_model = DescribeConfigIndexResponseBodyConfigGroups()
            self.config_groups = temp_model.from_map(m['ConfigGroups'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class DescribeConfigIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConfigIndexResponseBody = None,
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
            temp_model = DescribeConfigIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigOptionsRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        env_id: str = None,
        profile_name: str = None,
    ):
        self.stack_id = stack_id
        self.env_id = env_id
        self.profile_name = profile_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.profile_name is not None:
            result['ProfileName'] = self.profile_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ProfileName') is not None:
            self.profile_name = m.get('ProfileName')
        return self


class DescribeConfigOptionsResponseBodyStackConfigOptionConfigOptionsConfigOption(TeaModel):
    def __init__(
        self,
        regex_desc: str = None,
        max_value: int = None,
        editor_type: str = None,
        min_value: int = None,
        default_value: str = None,
        max_length: int = None,
        option_label: str = None,
        regex_pattern: str = None,
        change_severity: str = None,
        option_description: str = None,
        option_name: str = None,
        path_name: str = None,
        hidden_option: bool = None,
        value_type: str = None,
        min_length: int = None,
        value_options: str = None,
        readonly_option: bool = None,
    ):
        self.regex_desc = regex_desc
        self.max_value = max_value
        self.editor_type = editor_type
        self.min_value = min_value
        self.default_value = default_value
        self.max_length = max_length
        self.option_label = option_label
        self.regex_pattern = regex_pattern
        self.change_severity = change_severity
        self.option_description = option_description
        self.option_name = option_name
        self.path_name = path_name
        self.hidden_option = hidden_option
        self.value_type = value_type
        self.min_length = min_length
        self.value_options = value_options
        self.readonly_option = readonly_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.regex_desc is not None:
            result['RegexDesc'] = self.regex_desc
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.editor_type is not None:
            result['EditorType'] = self.editor_type
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.option_label is not None:
            result['OptionLabel'] = self.option_label
        if self.regex_pattern is not None:
            result['RegexPattern'] = self.regex_pattern
        if self.change_severity is not None:
            result['ChangeSeverity'] = self.change_severity
        if self.option_description is not None:
            result['OptionDescription'] = self.option_description
        if self.option_name is not None:
            result['OptionName'] = self.option_name
        if self.path_name is not None:
            result['PathName'] = self.path_name
        if self.hidden_option is not None:
            result['HiddenOption'] = self.hidden_option
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.value_options is not None:
            result['ValueOptions'] = self.value_options
        if self.readonly_option is not None:
            result['ReadonlyOption'] = self.readonly_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegexDesc') is not None:
            self.regex_desc = m.get('RegexDesc')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('EditorType') is not None:
            self.editor_type = m.get('EditorType')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('OptionLabel') is not None:
            self.option_label = m.get('OptionLabel')
        if m.get('RegexPattern') is not None:
            self.regex_pattern = m.get('RegexPattern')
        if m.get('ChangeSeverity') is not None:
            self.change_severity = m.get('ChangeSeverity')
        if m.get('OptionDescription') is not None:
            self.option_description = m.get('OptionDescription')
        if m.get('OptionName') is not None:
            self.option_name = m.get('OptionName')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        if m.get('HiddenOption') is not None:
            self.hidden_option = m.get('HiddenOption')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('ValueOptions') is not None:
            self.value_options = m.get('ValueOptions')
        if m.get('ReadonlyOption') is not None:
            self.readonly_option = m.get('ReadonlyOption')
        return self


class DescribeConfigOptionsResponseBodyStackConfigOptionConfigOptions(TeaModel):
    def __init__(
        self,
        config_option: List[DescribeConfigOptionsResponseBodyStackConfigOptionConfigOptionsConfigOption] = None,
    ):
        self.config_option = config_option

    def validate(self):
        if self.config_option:
            for k in self.config_option:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConfigOption'] = []
        if self.config_option is not None:
            for k in self.config_option:
                result['ConfigOption'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_option = []
        if m.get('ConfigOption') is not None:
            for k in m.get('ConfigOption'):
                temp_model = DescribeConfigOptionsResponseBodyStackConfigOptionConfigOptionsConfigOption()
                self.config_option.append(temp_model.from_map(k))
        return self


class DescribeConfigOptionsResponseBodyStackConfigOption(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        config_options: DescribeConfigOptionsResponseBodyStackConfigOptionConfigOptions = None,
        stack_name: str = None,
    ):
        self.stack_id = stack_id
        self.config_options = config_options
        self.stack_name = stack_name

    def validate(self):
        if self.config_options:
            self.config_options.validate()

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.config_options is not None:
            result['ConfigOptions'] = self.config_options.to_map()
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ConfigOptions') is not None:
            temp_model = DescribeConfigOptionsResponseBodyStackConfigOptionConfigOptions()
            self.config_options = temp_model.from_map(m['ConfigOptions'])
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        return self


class DescribeConfigOptionsResponseBody(TeaModel):
    def __init__(
        self,
        stack_config_option: DescribeConfigOptionsResponseBodyStackConfigOption = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.stack_config_option = stack_config_option
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.stack_config_option:
            self.stack_config_option.validate()

    def to_map(self):
        result = dict()
        if self.stack_config_option is not None:
            result['StackConfigOption'] = self.stack_config_option.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackConfigOption') is not None:
            temp_model = DescribeConfigOptionsResponseBodyStackConfigOption()
            self.stack_config_option = temp_model.from_map(m['StackConfigOption'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeConfigOptionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConfigOptionsResponseBody = None,
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
            temp_model = DescribeConfigOptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigSettingsRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        template_id: str = None,
        path_name: str = None,
        option_name: str = None,
    ):
        self.env_id = env_id
        self.template_id = template_id
        self.path_name = path_name
        self.option_name = option_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        if self.option_name is not None:
            result['OptionName'] = self.option_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        if m.get('OptionName') is not None:
            self.option_name = m.get('OptionName')
        return self


class DescribeConfigSettingsResponseBodyConfigSettingsConfigSetting(TeaModel):
    def __init__(
        self,
        option_name: str = None,
        path_name: str = None,
        setting_value: str = None,
    ):
        self.option_name = option_name
        self.path_name = path_name
        self.setting_value = setting_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.option_name is not None:
            result['OptionName'] = self.option_name
        if self.path_name is not None:
            result['PathName'] = self.path_name
        if self.setting_value is not None:
            result['SettingValue'] = self.setting_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionName') is not None:
            self.option_name = m.get('OptionName')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        if m.get('SettingValue') is not None:
            self.setting_value = m.get('SettingValue')
        return self


class DescribeConfigSettingsResponseBodyConfigSettings(TeaModel):
    def __init__(
        self,
        config_setting: List[DescribeConfigSettingsResponseBodyConfigSettingsConfigSetting] = None,
    ):
        self.config_setting = config_setting

    def validate(self):
        if self.config_setting:
            for k in self.config_setting:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConfigSetting'] = []
        if self.config_setting is not None:
            for k in self.config_setting:
                result['ConfigSetting'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_setting = []
        if m.get('ConfigSetting') is not None:
            for k in m.get('ConfigSetting'):
                temp_model = DescribeConfigSettingsResponseBodyConfigSettingsConfigSetting()
                self.config_setting.append(temp_model.from_map(k))
        return self


class DescribeConfigSettingsResponseBody(TeaModel):
    def __init__(
        self,
        config_settings: DescribeConfigSettingsResponseBodyConfigSettings = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.config_settings = config_settings
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.config_settings:
            self.config_settings.validate()

    def to_map(self):
        result = dict()
        if self.config_settings is not None:
            result['ConfigSettings'] = self.config_settings.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSettings') is not None:
            temp_model = DescribeConfigSettingsResponseBodyConfigSettings()
            self.config_settings = temp_model.from_map(m['ConfigSettings'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeConfigSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConfigSettingsResponseBody = None,
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
            temp_model = DescribeConfigSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigTemplatesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        template_name: str = None,
        template_search: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.app_id = app_id
        self.template_name = template_name
        self.template_search = template_search
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_search is not None:
            result['TemplateSearch'] = self.template_search
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateSearch') is not None:
            self.template_search = m.get('TemplateSearch')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeConfigTemplatesResponseBodyConfigTemplatesConfigTemplate(TeaModel):
    def __init__(
        self,
        template_description: str = None,
        app_name: str = None,
        update_time: int = None,
        stack_id: str = None,
        pkg_version_label: str = None,
        create_time: int = None,
        app_id: str = None,
        stack_name: str = None,
        pkg_version_id: str = None,
        template_name: str = None,
        template_id: str = None,
    ):
        self.template_description = template_description
        self.app_name = app_name
        self.update_time = update_time
        self.stack_id = stack_id
        self.pkg_version_label = pkg_version_label
        self.create_time = create_time
        self.app_id = app_id
        self.stack_name = stack_name
        self.pkg_version_id = pkg_version_id
        self.template_name = template_name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.pkg_version_label is not None:
            result['PkgVersionLabel'] = self.pkg_version_label
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.pkg_version_id is not None:
            result['PkgVersionId'] = self.pkg_version_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('PkgVersionLabel') is not None:
            self.pkg_version_label = m.get('PkgVersionLabel')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('PkgVersionId') is not None:
            self.pkg_version_id = m.get('PkgVersionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeConfigTemplatesResponseBodyConfigTemplates(TeaModel):
    def __init__(
        self,
        config_template: List[DescribeConfigTemplatesResponseBodyConfigTemplatesConfigTemplate] = None,
    ):
        self.config_template = config_template

    def validate(self):
        if self.config_template:
            for k in self.config_template:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConfigTemplate'] = []
        if self.config_template is not None:
            for k in self.config_template:
                result['ConfigTemplate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_template = []
        if m.get('ConfigTemplate') is not None:
            for k in m.get('ConfigTemplate'):
                temp_model = DescribeConfigTemplatesResponseBodyConfigTemplatesConfigTemplate()
                self.config_template.append(temp_model.from_map(k))
        return self


class DescribeConfigTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        config_templates: DescribeConfigTemplatesResponseBodyConfigTemplates = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        code: str = None,
    ):
        self.config_templates = config_templates
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.code = code

    def validate(self):
        if self.config_templates:
            self.config_templates.validate()

    def to_map(self):
        result = dict()
        if self.config_templates is not None:
            result['ConfigTemplates'] = self.config_templates.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigTemplates') is not None:
            temp_model = DescribeConfigTemplatesResponseBodyConfigTemplates()
            self.config_templates = temp_model.from_map(m['ConfigTemplates'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeConfigTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConfigTemplatesResponseBody = None,
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
            temp_model = DescribeConfigTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnvResourceRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
    ):
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class DescribeEnvResourceResponseBodyEnvResourceVSwitchesVSwitch(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeEnvResourceResponseBodyEnvResourceVSwitches(TeaModel):
    def __init__(
        self,
        v_switch: List[DescribeEnvResourceResponseBodyEnvResourceVSwitchesVSwitch] = None,
    ):
        self.v_switch = v_switch

    def validate(self):
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_switch = []
        if m.get('VSwitch') is not None:
            for k in m.get('VSwitch'):
                temp_model = DescribeEnvResourceResponseBodyEnvResourceVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        return self


class DescribeEnvResourceResponseBodyEnvResourceVpc(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeEnvResourceResponseBodyEnvResourceMonitorGroup(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeEnvResourceResponseBodyEnvResourceLoadBalancersLoadBalancerListenersListener(TeaModel):
    def __init__(
        self,
        protocol: str = None,
        port: int = None,
    ):
        self.protocol = protocol
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeEnvResourceResponseBodyEnvResourceLoadBalancersLoadBalancerListeners(TeaModel):
    def __init__(
        self,
        listener: List[DescribeEnvResourceResponseBodyEnvResourceLoadBalancersLoadBalancerListenersListener] = None,
    ):
        self.listener = listener

    def validate(self):
        if self.listener:
            for k in self.listener:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Listener'] = []
        if self.listener is not None:
            for k in self.listener:
                result['Listener'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener = []
        if m.get('Listener') is not None:
            for k in m.get('Listener'):
                temp_model = DescribeEnvResourceResponseBodyEnvResourceLoadBalancersLoadBalancerListenersListener()
                self.listener.append(temp_model.from_map(k))
        return self


class DescribeEnvResourceResponseBodyEnvResourceLoadBalancersLoadBalancer(TeaModel):
    def __init__(
        self,
        imported: bool = None,
        protocol: str = None,
        address_type: str = None,
        listeners: DescribeEnvResourceResponseBodyEnvResourceLoadBalancersLoadBalancerListeners = None,
        port: int = None,
        id: str = None,
    ):
        self.imported = imported
        self.protocol = protocol
        self.address_type = address_type
        self.listeners = listeners
        self.port = port
        self.id = id

    def validate(self):
        if self.listeners:
            self.listeners.validate()

    def to_map(self):
        result = dict()
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.listeners is not None:
            result['Listeners'] = self.listeners.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('Listeners') is not None:
            temp_model = DescribeEnvResourceResponseBodyEnvResourceLoadBalancersLoadBalancerListeners()
            self.listeners = temp_model.from_map(m['Listeners'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeEnvResourceResponseBodyEnvResourceLoadBalancers(TeaModel):
    def __init__(
        self,
        load_balancer: List[DescribeEnvResourceResponseBodyEnvResourceLoadBalancersLoadBalancer] = None,
    ):
        self.load_balancer = load_balancer

    def validate(self):
        if self.load_balancer:
            for k in self.load_balancer:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LoadBalancer'] = []
        if self.load_balancer is not None:
            for k in self.load_balancer:
                result['LoadBalancer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer = []
        if m.get('LoadBalancer') is not None:
            for k in m.get('LoadBalancer'):
                temp_model = DescribeEnvResourceResponseBodyEnvResourceLoadBalancersLoadBalancer()
                self.load_balancer.append(temp_model.from_map(k))
        return self


class DescribeEnvResourceResponseBodyEnvResourceInstancesInstance(TeaModel):
    def __init__(
        self,
        imported: bool = None,
        id: str = None,
    ):
        self.imported = imported
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeEnvResourceResponseBodyEnvResourceInstances(TeaModel):
    def __init__(
        self,
        instance: List[DescribeEnvResourceResponseBodyEnvResourceInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeEnvResourceResponseBodyEnvResourceInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeEnvResourceResponseBodyEnvResourceDefaultSecurityGroupsSecurityGroup(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeEnvResourceResponseBodyEnvResourceDefaultSecurityGroups(TeaModel):
    def __init__(
        self,
        security_group: List[DescribeEnvResourceResponseBodyEnvResourceDefaultSecurityGroupsSecurityGroup] = None,
    ):
        self.security_group = security_group

    def validate(self):
        if self.security_group:
            for k in self.security_group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SecurityGroup'] = []
        if self.security_group is not None:
            for k in self.security_group:
                result['SecurityGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_group = []
        if m.get('SecurityGroup') is not None:
            for k in m.get('SecurityGroup'):
                temp_model = DescribeEnvResourceResponseBodyEnvResourceDefaultSecurityGroupsSecurityGroup()
                self.security_group.append(temp_model.from_map(k))
        return self


class DescribeEnvResourceResponseBodyEnvResourceScalingGroup(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeEnvResourceResponseBodyEnvResourceDomainsDomain(TeaModel):
    def __init__(
        self,
        is_default: bool = None,
        hosted_by: str = None,
        sub_domain: str = None,
        domain_name: str = None,
        managed_by: str = None,
    ):
        self.is_default = is_default
        self.hosted_by = hosted_by
        self.sub_domain = sub_domain
        self.domain_name = domain_name
        self.managed_by = managed_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.hosted_by is not None:
            result['HostedBy'] = self.hosted_by
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.managed_by is not None:
            result['ManagedBy'] = self.managed_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('HostedBy') is not None:
            self.hosted_by = m.get('HostedBy')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ManagedBy') is not None:
            self.managed_by = m.get('ManagedBy')
        return self


class DescribeEnvResourceResponseBodyEnvResourceDomains(TeaModel):
    def __init__(
        self,
        domain: List[DescribeEnvResourceResponseBodyEnvResourceDomainsDomain] = None,
    ):
        self.domain = domain

    def validate(self):
        if self.domain:
            for k in self.domain:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Domain'] = []
        if self.domain is not None:
            for k in self.domain:
                result['Domain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain = []
        if m.get('Domain') is not None:
            for k in m.get('Domain'):
                temp_model = DescribeEnvResourceResponseBodyEnvResourceDomainsDomain()
                self.domain.append(temp_model.from_map(k))
        return self


class DescribeEnvResourceResponseBodyEnvResourceRdsInstancesRdsInstance(TeaModel):
    def __init__(
        self,
        imported: bool = None,
        database_name: str = None,
        id: str = None,
        account_name: str = None,
    ):
        self.imported = imported
        self.database_name = database_name
        self.id = id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.imported is not None:
            result['Imported'] = self.imported
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.id is not None:
            result['Id'] = self.id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Imported') is not None:
            self.imported = m.get('Imported')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeEnvResourceResponseBodyEnvResourceRdsInstances(TeaModel):
    def __init__(
        self,
        rds_instance: List[DescribeEnvResourceResponseBodyEnvResourceRdsInstancesRdsInstance] = None,
    ):
        self.rds_instance = rds_instance

    def validate(self):
        if self.rds_instance:
            for k in self.rds_instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RdsInstance'] = []
        if self.rds_instance is not None:
            for k in self.rds_instance:
                result['RdsInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rds_instance = []
        if m.get('RdsInstance') is not None:
            for k in m.get('RdsInstance'):
                temp_model = DescribeEnvResourceResponseBodyEnvResourceRdsInstancesRdsInstance()
                self.rds_instance.append(temp_model.from_map(k))
        return self


class DescribeEnvResourceResponseBodyEnvResource(TeaModel):
    def __init__(
        self,
        launch_template_id: str = None,
        env_name: str = None,
        v_switches: DescribeEnvResourceResponseBodyEnvResourceVSwitches = None,
        vpc: DescribeEnvResourceResponseBodyEnvResourceVpc = None,
        monitor_group: DescribeEnvResourceResponseBodyEnvResourceMonitorGroup = None,
        launch_configuration_id: str = None,
        load_balancers: DescribeEnvResourceResponseBodyEnvResourceLoadBalancers = None,
        instances: DescribeEnvResourceResponseBodyEnvResourceInstances = None,
        default_security_groups: DescribeEnvResourceResponseBodyEnvResourceDefaultSecurityGroups = None,
        scaling_group: DescribeEnvResourceResponseBodyEnvResourceScalingGroup = None,
        domains: DescribeEnvResourceResponseBodyEnvResourceDomains = None,
        rds_instances: DescribeEnvResourceResponseBodyEnvResourceRdsInstances = None,
        env_id: str = None,
    ):
        self.launch_template_id = launch_template_id
        self.env_name = env_name
        self.v_switches = v_switches
        self.vpc = vpc
        self.monitor_group = monitor_group
        self.launch_configuration_id = launch_configuration_id
        self.load_balancers = load_balancers
        self.instances = instances
        self.default_security_groups = default_security_groups
        self.scaling_group = scaling_group
        self.domains = domains
        self.rds_instances = rds_instances
        self.env_id = env_id

    def validate(self):
        if self.v_switches:
            self.v_switches.validate()
        if self.vpc:
            self.vpc.validate()
        if self.monitor_group:
            self.monitor_group.validate()
        if self.load_balancers:
            self.load_balancers.validate()
        if self.instances:
            self.instances.validate()
        if self.default_security_groups:
            self.default_security_groups.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.domains:
            self.domains.validate()
        if self.rds_instances:
            self.rds_instances.validate()

    def to_map(self):
        result = dict()
        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        if self.vpc is not None:
            result['Vpc'] = self.vpc.to_map()
        if self.monitor_group is not None:
            result['MonitorGroup'] = self.monitor_group.to_map()
        if self.launch_configuration_id is not None:
            result['LaunchConfigurationId'] = self.launch_configuration_id
        if self.load_balancers is not None:
            result['LoadBalancers'] = self.load_balancers.to_map()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.default_security_groups is not None:
            result['DefaultSecurityGroups'] = self.default_security_groups.to_map()
        if self.scaling_group is not None:
            result['ScalingGroup'] = self.scaling_group.to_map()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.rds_instances is not None:
            result['RdsInstances'] = self.rds_instances.to_map()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('VSwitches') is not None:
            temp_model = DescribeEnvResourceResponseBodyEnvResourceVSwitches()
            self.v_switches = temp_model.from_map(m['VSwitches'])
        if m.get('Vpc') is not None:
            temp_model = DescribeEnvResourceResponseBodyEnvResourceVpc()
            self.vpc = temp_model.from_map(m['Vpc'])
        if m.get('MonitorGroup') is not None:
            temp_model = DescribeEnvResourceResponseBodyEnvResourceMonitorGroup()
            self.monitor_group = temp_model.from_map(m['MonitorGroup'])
        if m.get('LaunchConfigurationId') is not None:
            self.launch_configuration_id = m.get('LaunchConfigurationId')
        if m.get('LoadBalancers') is not None:
            temp_model = DescribeEnvResourceResponseBodyEnvResourceLoadBalancers()
            self.load_balancers = temp_model.from_map(m['LoadBalancers'])
        if m.get('Instances') is not None:
            temp_model = DescribeEnvResourceResponseBodyEnvResourceInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('DefaultSecurityGroups') is not None:
            temp_model = DescribeEnvResourceResponseBodyEnvResourceDefaultSecurityGroups()
            self.default_security_groups = temp_model.from_map(m['DefaultSecurityGroups'])
        if m.get('ScalingGroup') is not None:
            temp_model = DescribeEnvResourceResponseBodyEnvResourceScalingGroup()
            self.scaling_group = temp_model.from_map(m['ScalingGroup'])
        if m.get('Domains') is not None:
            temp_model = DescribeEnvResourceResponseBodyEnvResourceDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('RdsInstances') is not None:
            temp_model = DescribeEnvResourceResponseBodyEnvResourceRdsInstances()
            self.rds_instances = temp_model.from_map(m['RdsInstances'])
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class DescribeEnvResourceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        env_resource: DescribeEnvResourceResponseBodyEnvResource = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.env_resource = env_resource

    def validate(self):
        if self.env_resource:
            self.env_resource.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.env_resource is not None:
            result['EnvResource'] = self.env_resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnvResource') is not None:
            temp_model = DescribeEnvResourceResponseBodyEnvResource()
            self.env_resource = temp_model.from_map(m['EnvResource'])
        return self


class DescribeEnvResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEnvResourceResponseBody = None,
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
            temp_model = DescribeEnvResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventsRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        start_time: int = None,
        end_time: int = None,
        page_size: int = None,
        page_number: int = None,
        change_id: str = None,
        last_change_events: bool = None,
        reverse_by_timestamp: bool = None,
    ):
        self.env_id = env_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number
        self.change_id = change_id
        self.last_change_events = last_change_events
        self.reverse_by_timestamp = reverse_by_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.last_change_events is not None:
            result['LastChangeEvents'] = self.last_change_events
        if self.reverse_by_timestamp is not None:
            result['ReverseByTimestamp'] = self.reverse_by_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('LastChangeEvents') is not None:
            self.last_change_events = m.get('LastChangeEvents')
        if m.get('ReverseByTimestamp') is not None:
            self.reverse_by_timestamp = m.get('ReverseByTimestamp')
        return self


class DescribeEventsResponseBodyEventsEventObjectAttrsObjectAttr(TeaModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
    ):
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        return self


class DescribeEventsResponseBodyEventsEventObjectAttrs(TeaModel):
    def __init__(
        self,
        object_attr: List[DescribeEventsResponseBodyEventsEventObjectAttrsObjectAttr] = None,
    ):
        self.object_attr = object_attr

    def validate(self):
        if self.object_attr:
            for k in self.object_attr:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ObjectAttr'] = []
        if self.object_attr is not None:
            for k in self.object_attr:
                result['ObjectAttr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_attr = []
        if m.get('ObjectAttr') is not None:
            for k in m.get('ObjectAttr'):
                temp_model = DescribeEventsResponseBodyEventsEventObjectAttrsObjectAttr()
                self.object_attr.append(temp_model.from_map(k))
        return self


class DescribeEventsResponseBodyEventsEventMsgParams(TeaModel):
    def __init__(
        self,
        msg_param: List[str] = None,
    ):
        self.msg_param = msg_param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.msg_param is not None:
            result['MsgParam'] = self.msg_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgParam') is not None:
            self.msg_param = m.get('MsgParam')
        return self


class DescribeEventsResponseBodyEventsEvent(TeaModel):
    def __init__(
        self,
        primary_user_name: str = None,
        object_type: str = None,
        envent_name: str = None,
        event_timestamp: int = None,
        second_user_name: str = None,
        msg_code: str = None,
        object_name: str = None,
        event_message: str = None,
        event_id: str = None,
        object_attrs: DescribeEventsResponseBodyEventsEventObjectAttrs = None,
        app_id: str = None,
        event_level: str = None,
        object_id: str = None,
        msg_params: DescribeEventsResponseBodyEventsEventMsgParams = None,
        primary_user_id: str = None,
        env_id: str = None,
        trace_id: str = None,
        second_user_id: str = None,
    ):
        self.primary_user_name = primary_user_name
        self.object_type = object_type
        self.envent_name = envent_name
        self.event_timestamp = event_timestamp
        self.second_user_name = second_user_name
        self.msg_code = msg_code
        self.object_name = object_name
        self.event_message = event_message
        self.event_id = event_id
        self.object_attrs = object_attrs
        self.app_id = app_id
        self.event_level = event_level
        self.object_id = object_id
        self.msg_params = msg_params
        self.primary_user_id = primary_user_id
        self.env_id = env_id
        self.trace_id = trace_id
        self.second_user_id = second_user_id

    def validate(self):
        if self.object_attrs:
            self.object_attrs.validate()
        if self.msg_params:
            self.msg_params.validate()

    def to_map(self):
        result = dict()
        if self.primary_user_name is not None:
            result['PrimaryUserName'] = self.primary_user_name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.envent_name is not None:
            result['EnventName'] = self.envent_name
        if self.event_timestamp is not None:
            result['EventTimestamp'] = self.event_timestamp
        if self.second_user_name is not None:
            result['SecondUserName'] = self.second_user_name
        if self.msg_code is not None:
            result['MsgCode'] = self.msg_code
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.event_message is not None:
            result['EventMessage'] = self.event_message
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.object_attrs is not None:
            result['ObjectAttrs'] = self.object_attrs.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.msg_params is not None:
            result['MsgParams'] = self.msg_params.to_map()
        if self.primary_user_id is not None:
            result['PrimaryUserId'] = self.primary_user_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.second_user_id is not None:
            result['SecondUserId'] = self.second_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrimaryUserName') is not None:
            self.primary_user_name = m.get('PrimaryUserName')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('EnventName') is not None:
            self.envent_name = m.get('EnventName')
        if m.get('EventTimestamp') is not None:
            self.event_timestamp = m.get('EventTimestamp')
        if m.get('SecondUserName') is not None:
            self.second_user_name = m.get('SecondUserName')
        if m.get('MsgCode') is not None:
            self.msg_code = m.get('MsgCode')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('EventMessage') is not None:
            self.event_message = m.get('EventMessage')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('ObjectAttrs') is not None:
            temp_model = DescribeEventsResponseBodyEventsEventObjectAttrs()
            self.object_attrs = temp_model.from_map(m['ObjectAttrs'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('MsgParams') is not None:
            temp_model = DescribeEventsResponseBodyEventsEventMsgParams()
            self.msg_params = temp_model.from_map(m['MsgParams'])
        if m.get('PrimaryUserId') is not None:
            self.primary_user_id = m.get('PrimaryUserId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('SecondUserId') is not None:
            self.second_user_id = m.get('SecondUserId')
        return self


class DescribeEventsResponseBodyEvents(TeaModel):
    def __init__(
        self,
        event: List[DescribeEventsResponseBodyEventsEvent] = None,
    ):
        self.event = event

    def validate(self):
        if self.event:
            for k in self.event:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Event'] = []
        if self.event is not None:
            for k in self.event:
                result['Event'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event = []
        if m.get('Event') is not None:
            for k in m.get('Event'):
                temp_model = DescribeEventsResponseBodyEventsEvent()
                self.event.append(temp_model.from_map(k))
        return self


class DescribeEventsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        events: DescribeEventsResponseBodyEvents = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.events = events
        self.code = code

    def validate(self):
        if self.events:
            self.events.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.events is not None:
            result['Events'] = self.events.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Events') is not None:
            temp_model = DescribeEventsResponseBodyEvents()
            self.events = temp_model.from_map(m['Events'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEventsResponseBody = None,
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
            temp_model = DescribeEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatherLogResultRequest(TeaModel):
    def __init__(
        self,
        change_id: str = None,
    ):
        self.change_id = change_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        return self


class DescribeGatherLogResultResponseBodyGatherLogResultChange(TeaModel):
    def __init__(
        self,
        change_paused: bool = None,
        change_description: str = None,
        finish_time: int = None,
        update_time: int = None,
        change_timedout: bool = None,
        create_time: int = None,
        change_message: str = None,
        action_name: str = None,
        change_finished: bool = None,
        create_username: str = None,
        change_succeeded: bool = None,
        change_id: str = None,
        change_aborted: bool = None,
        env_id: str = None,
        change_name: str = None,
    ):
        self.change_paused = change_paused
        self.change_description = change_description
        self.finish_time = finish_time
        self.update_time = update_time
        self.change_timedout = change_timedout
        self.create_time = create_time
        self.change_message = change_message
        self.action_name = action_name
        self.change_finished = change_finished
        self.create_username = create_username
        self.change_succeeded = change_succeeded
        self.change_id = change_id
        self.change_aborted = change_aborted
        self.env_id = env_id
        self.change_name = change_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.change_paused is not None:
            result['ChangePaused'] = self.change_paused
        if self.change_description is not None:
            result['ChangeDescription'] = self.change_description
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.change_timedout is not None:
            result['ChangeTimedout'] = self.change_timedout
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.change_message is not None:
            result['ChangeMessage'] = self.change_message
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.change_finished is not None:
            result['ChangeFinished'] = self.change_finished
        if self.create_username is not None:
            result['CreateUsername'] = self.create_username
        if self.change_succeeded is not None:
            result['ChangeSucceeded'] = self.change_succeeded
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.change_aborted is not None:
            result['ChangeAborted'] = self.change_aborted
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.change_name is not None:
            result['ChangeName'] = self.change_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangePaused') is not None:
            self.change_paused = m.get('ChangePaused')
        if m.get('ChangeDescription') is not None:
            self.change_description = m.get('ChangeDescription')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ChangeTimedout') is not None:
            self.change_timedout = m.get('ChangeTimedout')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChangeMessage') is not None:
            self.change_message = m.get('ChangeMessage')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ChangeFinished') is not None:
            self.change_finished = m.get('ChangeFinished')
        if m.get('CreateUsername') is not None:
            self.create_username = m.get('CreateUsername')
        if m.get('ChangeSucceeded') is not None:
            self.change_succeeded = m.get('ChangeSucceeded')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('ChangeAborted') is not None:
            self.change_aborted = m.get('ChangeAborted')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ChangeName') is not None:
            self.change_name = m.get('ChangeName')
        return self


class DescribeGatherLogResultResponseBodyGatherLogResultInstanceResultsInstanceResult(TeaModel):
    def __init__(
        self,
        task_message: str = None,
        storage_key: str = None,
        instance_id: str = None,
        task_succeeded: bool = None,
    ):
        self.task_message = task_message
        self.storage_key = storage_key
        self.instance_id = instance_id
        self.task_succeeded = task_succeeded

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_message is not None:
            result['TaskMessage'] = self.task_message
        if self.storage_key is not None:
            result['StorageKey'] = self.storage_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_succeeded is not None:
            result['TaskSucceeded'] = self.task_succeeded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskMessage') is not None:
            self.task_message = m.get('TaskMessage')
        if m.get('StorageKey') is not None:
            self.storage_key = m.get('StorageKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskSucceeded') is not None:
            self.task_succeeded = m.get('TaskSucceeded')
        return self


class DescribeGatherLogResultResponseBodyGatherLogResultInstanceResults(TeaModel):
    def __init__(
        self,
        instance_result: List[DescribeGatherLogResultResponseBodyGatherLogResultInstanceResultsInstanceResult] = None,
    ):
        self.instance_result = instance_result

    def validate(self):
        if self.instance_result:
            for k in self.instance_result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceResult'] = []
        if self.instance_result is not None:
            for k in self.instance_result:
                result['InstanceResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_result = []
        if m.get('InstanceResult') is not None:
            for k in m.get('InstanceResult'):
                temp_model = DescribeGatherLogResultResponseBodyGatherLogResultInstanceResultsInstanceResult()
                self.instance_result.append(temp_model.from_map(k))
        return self


class DescribeGatherLogResultResponseBodyGatherLogResult(TeaModel):
    def __init__(
        self,
        log_path: str = None,
        change: DescribeGatherLogResultResponseBodyGatherLogResultChange = None,
        instance_results: DescribeGatherLogResultResponseBodyGatherLogResultInstanceResults = None,
    ):
        self.log_path = log_path
        self.change = change
        self.instance_results = instance_results

    def validate(self):
        if self.change:
            self.change.validate()
        if self.instance_results:
            self.instance_results.validate()

    def to_map(self):
        result = dict()
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        if self.change is not None:
            result['Change'] = self.change.to_map()
        if self.instance_results is not None:
            result['InstanceResults'] = self.instance_results.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        if m.get('Change') is not None:
            temp_model = DescribeGatherLogResultResponseBodyGatherLogResultChange()
            self.change = temp_model.from_map(m['Change'])
        if m.get('InstanceResults') is not None:
            temp_model = DescribeGatherLogResultResponseBodyGatherLogResultInstanceResults()
            self.instance_results = temp_model.from_map(m['InstanceResults'])
        return self


class DescribeGatherLogResultResponseBody(TeaModel):
    def __init__(
        self,
        gather_log_result: DescribeGatherLogResultResponseBodyGatherLogResult = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.gather_log_result = gather_log_result
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.gather_log_result:
            self.gather_log_result.validate()

    def to_map(self):
        result = dict()
        if self.gather_log_result is not None:
            result['GatherLogResult'] = self.gather_log_result.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatherLogResult') is not None:
            temp_model = DescribeGatherLogResultResponseBodyGatherLogResult()
            self.gather_log_result = temp_model.from_map(m['GatherLogResult'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeGatherLogResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGatherLogResultResponseBody = None,
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
            temp_model = DescribeGatherLogResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatherStatsResultRequest(TeaModel):
    def __init__(
        self,
        change_id: str = None,
    ):
        self.change_id = change_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        return self


class DescribeGatherStatsResultResponseBodyGatherStatsResultChange(TeaModel):
    def __init__(
        self,
        change_paused: bool = None,
        change_description: str = None,
        finish_time: int = None,
        update_time: int = None,
        change_timedout: bool = None,
        create_time: int = None,
        change_message: str = None,
        action_name: str = None,
        change_finished: bool = None,
        create_username: str = None,
        change_succeeded: bool = None,
        change_id: str = None,
        change_aborted: bool = None,
        env_id: str = None,
        change_name: str = None,
    ):
        self.change_paused = change_paused
        self.change_description = change_description
        self.finish_time = finish_time
        self.update_time = update_time
        self.change_timedout = change_timedout
        self.create_time = create_time
        self.change_message = change_message
        self.action_name = action_name
        self.change_finished = change_finished
        self.create_username = create_username
        self.change_succeeded = change_succeeded
        self.change_id = change_id
        self.change_aborted = change_aborted
        self.env_id = env_id
        self.change_name = change_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.change_paused is not None:
            result['ChangePaused'] = self.change_paused
        if self.change_description is not None:
            result['ChangeDescription'] = self.change_description
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.change_timedout is not None:
            result['ChangeTimedout'] = self.change_timedout
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.change_message is not None:
            result['ChangeMessage'] = self.change_message
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.change_finished is not None:
            result['ChangeFinished'] = self.change_finished
        if self.create_username is not None:
            result['CreateUsername'] = self.create_username
        if self.change_succeeded is not None:
            result['ChangeSucceeded'] = self.change_succeeded
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.change_aborted is not None:
            result['ChangeAborted'] = self.change_aborted
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.change_name is not None:
            result['ChangeName'] = self.change_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangePaused') is not None:
            self.change_paused = m.get('ChangePaused')
        if m.get('ChangeDescription') is not None:
            self.change_description = m.get('ChangeDescription')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ChangeTimedout') is not None:
            self.change_timedout = m.get('ChangeTimedout')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ChangeMessage') is not None:
            self.change_message = m.get('ChangeMessage')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ChangeFinished') is not None:
            self.change_finished = m.get('ChangeFinished')
        if m.get('CreateUsername') is not None:
            self.create_username = m.get('CreateUsername')
        if m.get('ChangeSucceeded') is not None:
            self.change_succeeded = m.get('ChangeSucceeded')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('ChangeAborted') is not None:
            self.change_aborted = m.get('ChangeAborted')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('ChangeName') is not None:
            self.change_name = m.get('ChangeName')
        return self


class DescribeGatherStatsResultResponseBodyGatherStatsResultInstanceResultsInstanceResult(TeaModel):
    def __init__(
        self,
        task_message: str = None,
        storage_key: str = None,
        instance_id: str = None,
        task_succeeded: bool = None,
    ):
        self.task_message = task_message
        self.storage_key = storage_key
        self.instance_id = instance_id
        self.task_succeeded = task_succeeded

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_message is not None:
            result['TaskMessage'] = self.task_message
        if self.storage_key is not None:
            result['StorageKey'] = self.storage_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_succeeded is not None:
            result['TaskSucceeded'] = self.task_succeeded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskMessage') is not None:
            self.task_message = m.get('TaskMessage')
        if m.get('StorageKey') is not None:
            self.storage_key = m.get('StorageKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskSucceeded') is not None:
            self.task_succeeded = m.get('TaskSucceeded')
        return self


class DescribeGatherStatsResultResponseBodyGatherStatsResultInstanceResults(TeaModel):
    def __init__(
        self,
        instance_result: List[DescribeGatherStatsResultResponseBodyGatherStatsResultInstanceResultsInstanceResult] = None,
    ):
        self.instance_result = instance_result

    def validate(self):
        if self.instance_result:
            for k in self.instance_result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceResult'] = []
        if self.instance_result is not None:
            for k in self.instance_result:
                result['InstanceResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_result = []
        if m.get('InstanceResult') is not None:
            for k in m.get('InstanceResult'):
                temp_model = DescribeGatherStatsResultResponseBodyGatherStatsResultInstanceResultsInstanceResult()
                self.instance_result.append(temp_model.from_map(k))
        return self


class DescribeGatherStatsResultResponseBodyGatherStatsResult(TeaModel):
    def __init__(
        self,
        change: DescribeGatherStatsResultResponseBodyGatherStatsResultChange = None,
        instance_results: DescribeGatherStatsResultResponseBodyGatherStatsResultInstanceResults = None,
    ):
        self.change = change
        self.instance_results = instance_results

    def validate(self):
        if self.change:
            self.change.validate()
        if self.instance_results:
            self.instance_results.validate()

    def to_map(self):
        result = dict()
        if self.change is not None:
            result['Change'] = self.change.to_map()
        if self.instance_results is not None:
            result['InstanceResults'] = self.instance_results.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Change') is not None:
            temp_model = DescribeGatherStatsResultResponseBodyGatherStatsResultChange()
            self.change = temp_model.from_map(m['Change'])
        if m.get('InstanceResults') is not None:
            temp_model = DescribeGatherStatsResultResponseBodyGatherStatsResultInstanceResults()
            self.instance_results = temp_model.from_map(m['InstanceResults'])
        return self


class DescribeGatherStatsResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        gather_stats_result: DescribeGatherStatsResultResponseBodyGatherStatsResult = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.gather_stats_result = gather_stats_result
        self.code = code

    def validate(self):
        if self.gather_stats_result:
            self.gather_stats_result.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.gather_stats_result is not None:
            result['GatherStatsResult'] = self.gather_stats_result.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GatherStatsResult') is not None:
            temp_model = DescribeGatherStatsResultResponseBodyGatherStatsResult()
            self.gather_stats_result = temp_model.from_map(m['GatherStatsResult'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeGatherStatsResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGatherStatsResultResponseBody = None,
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
            temp_model = DescribeGatherStatsResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceHealthRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceHealthResponseBodyInstanceHealth(TeaModel):
    def __init__(
        self,
        app_status: str = None,
        instance_id: str = None,
        disconnected_time: int = None,
        agent_status: str = None,
    ):
        self.app_status = app_status
        self.instance_id = instance_id
        self.disconnected_time = disconnected_time
        self.agent_status = agent_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.disconnected_time is not None:
            result['DisconnectedTime'] = self.disconnected_time
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DisconnectedTime') is not None:
            self.disconnected_time = m.get('DisconnectedTime')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        return self


class DescribeInstanceHealthResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        instance_health: DescribeInstanceHealthResponseBodyInstanceHealth = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.instance_health = instance_health
        self.code = code

    def validate(self):
        if self.instance_health:
            self.instance_health.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_health is not None:
            result['InstanceHealth'] = self.instance_health.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceHealth') is not None:
            temp_model = DescribeInstanceHealthResponseBodyInstanceHealth()
            self.instance_health = temp_model.from_map(m['InstanceHealth'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeInstanceHealthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceHealthResponseBody = None,
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
            temp_model = DescribeInstanceHealthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePkgVersionsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_size: int = None,
        page_number: int = None,
        pkg_version_label: str = None,
        pkg_version_search: str = None,
    ):
        self.app_id = app_id
        self.page_size = page_size
        self.page_number = page_number
        self.pkg_version_label = pkg_version_label
        self.pkg_version_search = pkg_version_search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.pkg_version_label is not None:
            result['PkgVersionLabel'] = self.pkg_version_label
        if self.pkg_version_search is not None:
            result['PkgVersionSearch'] = self.pkg_version_search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PkgVersionLabel') is not None:
            self.pkg_version_label = m.get('PkgVersionLabel')
        if m.get('PkgVersionSearch') is not None:
            self.pkg_version_search = m.get('PkgVersionSearch')
        return self


class DescribePkgVersionsResponseBodyPkgVersionsPkgVersion(TeaModel):
    def __init__(
        self,
        create_username: str = None,
        app_name: str = None,
        update_time: int = None,
        pkg_version_label: str = None,
        create_time: int = None,
        package_source: str = None,
        app_id: str = None,
        package_etag: str = None,
        pkg_version_id: str = None,
        pkg_version_description: str = None,
    ):
        self.create_username = create_username
        self.app_name = app_name
        self.update_time = update_time
        self.pkg_version_label = pkg_version_label
        self.create_time = create_time
        self.package_source = package_source
        self.app_id = app_id
        self.package_etag = package_etag
        self.pkg_version_id = pkg_version_id
        self.pkg_version_description = pkg_version_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_username is not None:
            result['CreateUsername'] = self.create_username
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.pkg_version_label is not None:
            result['PkgVersionLabel'] = self.pkg_version_label
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.package_source is not None:
            result['PackageSource'] = self.package_source
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.package_etag is not None:
            result['PackageETag'] = self.package_etag
        if self.pkg_version_id is not None:
            result['PkgVersionId'] = self.pkg_version_id
        if self.pkg_version_description is not None:
            result['PkgVersionDescription'] = self.pkg_version_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateUsername') is not None:
            self.create_username = m.get('CreateUsername')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('PkgVersionLabel') is not None:
            self.pkg_version_label = m.get('PkgVersionLabel')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PackageSource') is not None:
            self.package_source = m.get('PackageSource')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PackageETag') is not None:
            self.package_etag = m.get('PackageETag')
        if m.get('PkgVersionId') is not None:
            self.pkg_version_id = m.get('PkgVersionId')
        if m.get('PkgVersionDescription') is not None:
            self.pkg_version_description = m.get('PkgVersionDescription')
        return self


class DescribePkgVersionsResponseBodyPkgVersions(TeaModel):
    def __init__(
        self,
        pkg_version: List[DescribePkgVersionsResponseBodyPkgVersionsPkgVersion] = None,
    ):
        self.pkg_version = pkg_version

    def validate(self):
        if self.pkg_version:
            for k in self.pkg_version:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PkgVersion'] = []
        if self.pkg_version is not None:
            for k in self.pkg_version:
                result['PkgVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pkg_version = []
        if m.get('PkgVersion') is not None:
            for k in m.get('PkgVersion'):
                temp_model = DescribePkgVersionsResponseBodyPkgVersionsPkgVersion()
                self.pkg_version.append(temp_model.from_map(k))
        return self


class DescribePkgVersionsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        pkg_versions: DescribePkgVersionsResponseBodyPkgVersions = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.pkg_versions = pkg_versions
        self.code = code

    def validate(self):
        if self.pkg_versions:
            self.pkg_versions.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.pkg_versions is not None:
            result['PkgVersions'] = self.pkg_versions.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PkgVersions') is not None:
            temp_model = DescribePkgVersionsResponseBodyPkgVersions()
            self.pkg_versions = temp_model.from_map(m['PkgVersions'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribePkgVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePkgVersionsResponseBody = None,
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
            temp_model = DescribePkgVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePublicConfigTemplatesRequest(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.category_name = category_name
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribePublicConfigTemplatesResponseBodyPublicConfigTemplatesPublicConfigTemplate(TeaModel):
    def __init__(
        self,
        template_description: str = None,
        update_time: int = None,
        stack_id: str = None,
        template_logo: str = None,
        create_time: int = None,
        package_source: str = None,
        stack_name: str = None,
        template_name: str = None,
        category_name: str = None,
        template_id: str = None,
    ):
        self.template_description = template_description
        self.update_time = update_time
        self.stack_id = stack_id
        self.template_logo = template_logo
        self.create_time = create_time
        self.package_source = package_source
        self.stack_name = stack_name
        self.template_name = template_name
        self.category_name = category_name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.template_logo is not None:
            result['TemplateLogo'] = self.template_logo
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.package_source is not None:
            result['PackageSource'] = self.package_source
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('TemplateLogo') is not None:
            self.template_logo = m.get('TemplateLogo')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PackageSource') is not None:
            self.package_source = m.get('PackageSource')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribePublicConfigTemplatesResponseBodyPublicConfigTemplates(TeaModel):
    def __init__(
        self,
        public_config_template: List[DescribePublicConfigTemplatesResponseBodyPublicConfigTemplatesPublicConfigTemplate] = None,
    ):
        self.public_config_template = public_config_template

    def validate(self):
        if self.public_config_template:
            for k in self.public_config_template:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PublicConfigTemplate'] = []
        if self.public_config_template is not None:
            for k in self.public_config_template:
                result['PublicConfigTemplate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.public_config_template = []
        if m.get('PublicConfigTemplate') is not None:
            for k in m.get('PublicConfigTemplate'):
                temp_model = DescribePublicConfigTemplatesResponseBodyPublicConfigTemplatesPublicConfigTemplate()
                self.public_config_template.append(temp_model.from_map(k))
        return self


class DescribePublicConfigTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        public_config_templates: DescribePublicConfigTemplatesResponseBodyPublicConfigTemplates = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.public_config_templates = public_config_templates
        self.code = code

    def validate(self):
        if self.public_config_templates:
            self.public_config_templates.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.public_config_templates is not None:
            result['PublicConfigTemplates'] = self.public_config_templates.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PublicConfigTemplates') is not None:
            temp_model = DescribePublicConfigTemplatesResponseBodyPublicConfigTemplates()
            self.public_config_templates = temp_model.from_map(m['PublicConfigTemplates'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribePublicConfigTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePublicConfigTemplatesResponseBody = None,
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
            temp_model = DescribePublicConfigTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStacksRequest(TeaModel):
    def __init__(
        self,
        recommended_only: bool = None,
        category_name: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.recommended_only = recommended_only
        self.category_name = category_name
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.recommended_only is not None:
            result['RecommendedOnly'] = self.recommended_only
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecommendedOnly') is not None:
            self.recommended_only = m.get('RecommendedOnly')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeStacksResponseBodyStacksStack(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        stack_id: str = None,
        create_time: int = None,
        recommended_stack: bool = None,
        stack_name: str = None,
        category_name: str = None,
        version_code: int = None,
        latest_stack: bool = None,
    ):
        self.update_time = update_time
        self.stack_id = stack_id
        self.create_time = create_time
        self.recommended_stack = recommended_stack
        self.stack_name = stack_name
        self.category_name = category_name
        self.version_code = version_code
        self.latest_stack = latest_stack

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.recommended_stack is not None:
            result['RecommendedStack'] = self.recommended_stack
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.latest_stack is not None:
            result['LatestStack'] = self.latest_stack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RecommendedStack') is not None:
            self.recommended_stack = m.get('RecommendedStack')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('LatestStack') is not None:
            self.latest_stack = m.get('LatestStack')
        return self


class DescribeStacksResponseBodyStacks(TeaModel):
    def __init__(
        self,
        stack: List[DescribeStacksResponseBodyStacksStack] = None,
    ):
        self.stack = stack

    def validate(self):
        if self.stack:
            for k in self.stack:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Stack'] = []
        if self.stack is not None:
            for k in self.stack:
                result['Stack'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stack = []
        if m.get('Stack') is not None:
            for k in m.get('Stack'):
                temp_model = DescribeStacksResponseBodyStacksStack()
                self.stack.append(temp_model.from_map(k))
        return self


class DescribeStacksResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        stacks: DescribeStacksResponseBodyStacks = None,
        code: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.stacks = stacks
        self.code = code

    def validate(self):
        if self.stacks:
            self.stacks.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.stacks is not None:
            result['Stacks'] = self.stacks.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Stacks') is not None:
            temp_model = DescribeStacksResponseBodyStacks()
            self.stacks = temp_model.from_map(m['Stacks'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeStacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStacksResponseBody = None,
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
            temp_model = DescribeStacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStorageRequest(TeaModel):
    def __init__(
        self,
        using_shared_storage: bool = None,
    ):
        self.using_shared_storage = using_shared_storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.using_shared_storage is not None:
            result['UsingSharedStorage'] = self.using_shared_storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsingSharedStorage') is not None:
            self.using_shared_storage = m.get('UsingSharedStorage')
        return self


class DescribeStorageResponseBodyStorage(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        key_prefix: str = None,
        pkg_key_prefix: str = None,
        create_time: int = None,
        bucket_name: str = None,
    ):
        self.update_time = update_time
        self.key_prefix = key_prefix
        self.pkg_key_prefix = pkg_key_prefix
        self.create_time = create_time
        self.bucket_name = bucket_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.key_prefix is not None:
            result['KeyPrefix'] = self.key_prefix
        if self.pkg_key_prefix is not None:
            result['PkgKeyPrefix'] = self.pkg_key_prefix
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('KeyPrefix') is not None:
            self.key_prefix = m.get('KeyPrefix')
        if m.get('PkgKeyPrefix') is not None:
            self.pkg_key_prefix = m.get('PkgKeyPrefix')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        return self


class DescribeStorageResponseBody(TeaModel):
    def __init__(
        self,
        storage: DescribeStorageResponseBodyStorage = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.storage = storage
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.storage:
            self.storage.validate()

    def to_map(self):
        result = dict()
        if self.storage is not None:
            result['Storage'] = self.storage.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Storage') is not None:
            temp_model = DescribeStorageResponseBodyStorage()
            self.storage = temp_model.from_map(m['Storage'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStorageResponseBody = None,
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
            temp_model = DescribeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GatherAppEnvLogRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        target_instances: str = None,
        log_path: str = None,
    ):
        self.env_id = env_id
        self.target_instances = target_instances
        self.log_path = log_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.target_instances is not None:
            result['TargetInstances'] = self.target_instances
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('TargetInstances') is not None:
            self.target_instances = m.get('TargetInstances')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        return self


class GatherAppEnvLogResponseBodyEnvChange(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class GatherAppEnvLogResponseBody(TeaModel):
    def __init__(
        self,
        env_change: GatherAppEnvLogResponseBodyEnvChange = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.env_change = env_change
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.env_change:
            self.env_change.validate()

    def to_map(self):
        result = dict()
        if self.env_change is not None:
            result['EnvChange'] = self.env_change.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvChange') is not None:
            temp_model = GatherAppEnvLogResponseBodyEnvChange()
            self.env_change = temp_model.from_map(m['EnvChange'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GatherAppEnvLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GatherAppEnvLogResponseBody = None,
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
            temp_model = GatherAppEnvLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GatherAppEnvStatsRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        target_instances: str = None,
    ):
        self.env_id = env_id
        self.target_instances = target_instances

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.target_instances is not None:
            result['TargetInstances'] = self.target_instances
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('TargetInstances') is not None:
            self.target_instances = m.get('TargetInstances')
        return self


class GatherAppEnvStatsResponseBodyEnvChange(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class GatherAppEnvStatsResponseBody(TeaModel):
    def __init__(
        self,
        env_change: GatherAppEnvStatsResponseBodyEnvChange = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.env_change = env_change
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.env_change:
            self.env_change.validate()

    def to_map(self):
        result = dict()
        if self.env_change is not None:
            result['EnvChange'] = self.env_change.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvChange') is not None:
            temp_model = GatherAppEnvStatsResponseBodyEnvChange()
            self.env_change = temp_model.from_map(m['EnvChange'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GatherAppEnvStatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GatherAppEnvStatsResponseBody = None,
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
            temp_model = GatherAppEnvStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseChangeRequest(TeaModel):
    def __init__(
        self,
        change_id: str = None,
    ):
        self.change_id = change_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        return self


class PauseChangeResponseBodyEnvChange(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class PauseChangeResponseBody(TeaModel):
    def __init__(
        self,
        env_change: PauseChangeResponseBodyEnvChange = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.env_change = env_change
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.env_change:
            self.env_change.validate()

    def to_map(self):
        result = dict()
        if self.env_change is not None:
            result['EnvChange'] = self.env_change.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvChange') is not None:
            temp_model = PauseChangeResponseBodyEnvChange()
            self.env_change = temp_model.from_map(m['EnvChange'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class PauseChangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PauseChangeResponseBody = None,
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
            temp_model = PauseChangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebuildAppEnvRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        dry_run: bool = None,
    ):
        self.env_id = env_id
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class RebuildAppEnvResponseBodyEnvChangeDetailOperationsOperation(TeaModel):
    def __init__(
        self,
        operation_description: str = None,
        operation_type: str = None,
    ):
        self.operation_description = operation_description
        self.operation_type = operation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        return self


class RebuildAppEnvResponseBodyEnvChangeDetailOperations(TeaModel):
    def __init__(
        self,
        operation: List[RebuildAppEnvResponseBodyEnvChangeDetailOperationsOperation] = None,
    ):
        self.operation = operation

    def validate(self):
        if self.operation:
            for k in self.operation:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Operation'] = []
        if self.operation is not None:
            for k in self.operation:
                result['Operation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation = []
        if m.get('Operation') is not None:
            for k in m.get('Operation'):
                temp_model = RebuildAppEnvResponseBodyEnvChangeDetailOperationsOperation()
                self.operation.append(temp_model.from_map(k))
        return self


class RebuildAppEnvResponseBodyEnvChangeDetail(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
        operations: RebuildAppEnvResponseBodyEnvChangeDetailOperations = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id
        self.operations = operations

    def validate(self):
        if self.operations:
            self.operations.validate()

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.operations is not None:
            result['Operations'] = self.operations.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Operations') is not None:
            temp_model = RebuildAppEnvResponseBodyEnvChangeDetailOperations()
            self.operations = temp_model.from_map(m['Operations'])
        return self


class RebuildAppEnvResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        env_change_detail: RebuildAppEnvResponseBodyEnvChangeDetail = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.env_change_detail = env_change_detail
        self.code = code

    def validate(self):
        if self.env_change_detail:
            self.env_change_detail.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.env_change_detail is not None:
            result['EnvChangeDetail'] = self.env_change_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EnvChangeDetail') is not None:
            temp_model = RebuildAppEnvResponseBodyEnvChangeDetail()
            self.env_change_detail = temp_model.from_map(m['EnvChangeDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RebuildAppEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RebuildAppEnvResponseBody = None,
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
            temp_model = RebuildAppEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartAppEnvRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        batch_size: int = None,
        batch_percent: int = None,
        batch_interval: int = None,
        pause_between_batches: bool = None,
    ):
        self.env_id = env_id
        self.batch_size = batch_size
        self.batch_percent = batch_percent
        self.batch_interval = batch_interval
        self.pause_between_batches = pause_between_batches

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.batch_percent is not None:
            result['BatchPercent'] = self.batch_percent
        if self.batch_interval is not None:
            result['BatchInterval'] = self.batch_interval
        if self.pause_between_batches is not None:
            result['PauseBetweenBatches'] = self.pause_between_batches
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('BatchPercent') is not None:
            self.batch_percent = m.get('BatchPercent')
        if m.get('BatchInterval') is not None:
            self.batch_interval = m.get('BatchInterval')
        if m.get('PauseBetweenBatches') is not None:
            self.pause_between_batches = m.get('PauseBetweenBatches')
        return self


class RestartAppEnvResponseBodyEnvChange(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class RestartAppEnvResponseBody(TeaModel):
    def __init__(
        self,
        env_change: RestartAppEnvResponseBodyEnvChange = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.env_change = env_change
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.env_change:
            self.env_change.validate()

    def to_map(self):
        result = dict()
        if self.env_change is not None:
            result['EnvChange'] = self.env_change.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvChange') is not None:
            temp_model = RestartAppEnvResponseBodyEnvChange()
            self.env_change = temp_model.from_map(m['EnvChange'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RestartAppEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartAppEnvResponseBody = None,
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
            temp_model = RestartAppEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeChangeRequest(TeaModel):
    def __init__(
        self,
        change_id: str = None,
    ):
        self.change_id = change_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        return self


class ResumeChangeResponseBodyEnvChange(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class ResumeChangeResponseBody(TeaModel):
    def __init__(
        self,
        env_change: ResumeChangeResponseBodyEnvChange = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.env_change = env_change
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.env_change:
            self.env_change.validate()

    def to_map(self):
        result = dict()
        if self.env_change is not None:
            result['EnvChange'] = self.env_change.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvChange') is not None:
            temp_model = ResumeChangeResponseBodyEnvChange()
            self.env_change = temp_model.from_map(m['EnvChange'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ResumeChangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResumeChangeResponseBody = None,
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
            temp_model = ResumeChangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAppEnvRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
    ):
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class StartAppEnvResponseBodyEnvChange(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class StartAppEnvResponseBody(TeaModel):
    def __init__(
        self,
        env_change: StartAppEnvResponseBodyEnvChange = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.env_change = env_change
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.env_change:
            self.env_change.validate()

    def to_map(self):
        result = dict()
        if self.env_change is not None:
            result['EnvChange'] = self.env_change.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvChange') is not None:
            temp_model = StartAppEnvResponseBodyEnvChange()
            self.env_change = temp_model.from_map(m['EnvChange'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class StartAppEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartAppEnvResponseBody = None,
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
            temp_model = StartAppEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAppEnvRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
    ):
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class StopAppEnvResponseBodyEnvChange(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class StopAppEnvResponseBody(TeaModel):
    def __init__(
        self,
        env_change: StopAppEnvResponseBodyEnvChange = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.env_change = env_change
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.env_change:
            self.env_change.validate()

    def to_map(self):
        result = dict()
        if self.env_change is not None:
            result['EnvChange'] = self.env_change.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvChange') is not None:
            temp_model = StopAppEnvResponseBodyEnvChange()
            self.env_change = temp_model.from_map(m['EnvChange'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class StopAppEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopAppEnvResponseBody = None,
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
            temp_model = StopAppEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateAppEnvRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        dry_run: str = None,
    ):
        self.env_id = env_id
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        return self


class TerminateAppEnvResponseBodyEnvChangeDetailOperationsOperation(TeaModel):
    def __init__(
        self,
        operation_description: str = None,
        operation_type: str = None,
    ):
        self.operation_description = operation_description
        self.operation_type = operation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        return self


class TerminateAppEnvResponseBodyEnvChangeDetailOperations(TeaModel):
    def __init__(
        self,
        operation: List[TerminateAppEnvResponseBodyEnvChangeDetailOperationsOperation] = None,
    ):
        self.operation = operation

    def validate(self):
        if self.operation:
            for k in self.operation:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Operation'] = []
        if self.operation is not None:
            for k in self.operation:
                result['Operation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation = []
        if m.get('Operation') is not None:
            for k in m.get('Operation'):
                temp_model = TerminateAppEnvResponseBodyEnvChangeDetailOperationsOperation()
                self.operation.append(temp_model.from_map(k))
        return self


class TerminateAppEnvResponseBodyEnvChangeDetail(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
        operations: TerminateAppEnvResponseBodyEnvChangeDetailOperations = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id
        self.operations = operations

    def validate(self):
        if self.operations:
            self.operations.validate()

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.operations is not None:
            result['Operations'] = self.operations.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Operations') is not None:
            temp_model = TerminateAppEnvResponseBodyEnvChangeDetailOperations()
            self.operations = temp_model.from_map(m['Operations'])
        return self


class TerminateAppEnvResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        env_change_detail: TerminateAppEnvResponseBodyEnvChangeDetail = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.env_change_detail = env_change_detail
        self.code = code

    def validate(self):
        if self.env_change_detail:
            self.env_change_detail.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.env_change_detail is not None:
            result['EnvChangeDetail'] = self.env_change_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EnvChangeDetail') is not None:
            temp_model = TerminateAppEnvResponseBodyEnvChangeDetail()
            self.env_change_detail = temp_model.from_map(m['EnvChangeDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class TerminateAppEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TerminateAppEnvResponseBody = None,
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
            temp_model = TerminateAppEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppEnvRequest(TeaModel):
    def __init__(
        self,
        env_description: str = None,
        env_id: str = None,
        pkg_version_id: str = None,
        option_settings: str = None,
        stack_id: str = None,
        dry_run: bool = None,
        extra_properties: str = None,
        batch_size: str = None,
        batch_percent: str = None,
        batch_interval: str = None,
        pause_between_batches: bool = None,
    ):
        self.env_description = env_description
        self.env_id = env_id
        self.pkg_version_id = pkg_version_id
        self.option_settings = option_settings
        self.stack_id = stack_id
        self.dry_run = dry_run
        self.extra_properties = extra_properties
        self.batch_size = batch_size
        self.batch_percent = batch_percent
        self.batch_interval = batch_interval
        self.pause_between_batches = pause_between_batches

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_description is not None:
            result['EnvDescription'] = self.env_description
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.pkg_version_id is not None:
            result['PkgVersionId'] = self.pkg_version_id
        if self.option_settings is not None:
            result['OptionSettings'] = self.option_settings
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.extra_properties is not None:
            result['ExtraProperties'] = self.extra_properties
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size
        if self.batch_percent is not None:
            result['BatchPercent'] = self.batch_percent
        if self.batch_interval is not None:
            result['BatchInterval'] = self.batch_interval
        if self.pause_between_batches is not None:
            result['PauseBetweenBatches'] = self.pause_between_batches
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvDescription') is not None:
            self.env_description = m.get('EnvDescription')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('PkgVersionId') is not None:
            self.pkg_version_id = m.get('PkgVersionId')
        if m.get('OptionSettings') is not None:
            self.option_settings = m.get('OptionSettings')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ExtraProperties') is not None:
            self.extra_properties = m.get('ExtraProperties')
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')
        if m.get('BatchPercent') is not None:
            self.batch_percent = m.get('BatchPercent')
        if m.get('BatchInterval') is not None:
            self.batch_interval = m.get('BatchInterval')
        if m.get('PauseBetweenBatches') is not None:
            self.pause_between_batches = m.get('PauseBetweenBatches')
        return self


class UpdateAppEnvResponseBodyEnvChangeDetailOperationsOperation(TeaModel):
    def __init__(
        self,
        operation_description: str = None,
        operation_type: str = None,
    ):
        self.operation_description = operation_description
        self.operation_type = operation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        return self


class UpdateAppEnvResponseBodyEnvChangeDetailOperations(TeaModel):
    def __init__(
        self,
        operation: List[UpdateAppEnvResponseBodyEnvChangeDetailOperationsOperation] = None,
    ):
        self.operation = operation

    def validate(self):
        if self.operation:
            for k in self.operation:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Operation'] = []
        if self.operation is not None:
            for k in self.operation:
                result['Operation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation = []
        if m.get('Operation') is not None:
            for k in m.get('Operation'):
                temp_model = UpdateAppEnvResponseBodyEnvChangeDetailOperationsOperation()
                self.operation.append(temp_model.from_map(k))
        return self


class UpdateAppEnvResponseBodyEnvChangeDetail(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        change_id: str = None,
        env_id: str = None,
        operations: UpdateAppEnvResponseBodyEnvChangeDetailOperations = None,
    ):
        self.start_time = start_time
        self.change_id = change_id
        self.env_id = env_id
        self.operations = operations

    def validate(self):
        if self.operations:
            self.operations.validate()

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.change_id is not None:
            result['ChangeId'] = self.change_id
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.operations is not None:
            result['Operations'] = self.operations.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('Operations') is not None:
            temp_model = UpdateAppEnvResponseBodyEnvChangeDetailOperations()
            self.operations = temp_model.from_map(m['Operations'])
        return self


class UpdateAppEnvResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        env_change_detail: UpdateAppEnvResponseBodyEnvChangeDetail = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.env_change_detail = env_change_detail
        self.code = code

    def validate(self):
        if self.env_change_detail:
            self.env_change_detail.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.env_change_detail is not None:
            result['EnvChangeDetail'] = self.env_change_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EnvChangeDetail') is not None:
            temp_model = UpdateAppEnvResponseBodyEnvChangeDetail()
            self.env_change_detail = temp_model.from_map(m['EnvChangeDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateAppEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppEnvResponseBody = None,
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
            temp_model = UpdateAppEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_description: str = None,
    ):
        self.app_id = app_id
        self.app_description = app_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        return self


class UpdateApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        create_username: str = None,
        update_time: int = None,
        update_username: str = None,
        create_time: int = None,
        app_id: str = None,
        category_name: str = None,
        app_description: str = None,
    ):
        self.app_name = app_name
        self.create_username = create_username
        self.update_time = update_time
        self.update_username = update_username
        self.create_time = create_time
        self.app_id = app_id
        self.category_name = category_name
        self.app_description = app_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_username is not None:
            result['CreateUsername'] = self.create_username
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_username is not None:
            result['UpdateUsername'] = self.update_username
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateUsername') is not None:
            self.create_username = m.get('CreateUsername')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUsername') is not None:
            self.update_username = m.get('UpdateUsername')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        return self


class UpdateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        application: UpdateApplicationResponseBodyApplication = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.application = application

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.application is not None:
            result['Application'] = self.application.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Application') is not None:
            temp_model = UpdateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        return self


class UpdateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateApplicationResponseBody = None,
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
            temp_model = UpdateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigTemplateRequest(TeaModel):
    def __init__(
        self,
        template_description: str = None,
        template_id: str = None,
        option_settings: str = None,
    ):
        self.template_description = template_description
        self.template_id = template_id
        self.option_settings = option_settings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.option_settings is not None:
            result['OptionSettings'] = self.option_settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('OptionSettings') is not None:
            self.option_settings = m.get('OptionSettings')
        return self


class UpdateConfigTemplateResponseBodyConfigTemplate(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        update_time: int = None,
        stack_id: str = None,
        create_time: int = None,
        app_id: str = None,
        stack_name: str = None,
        template_name: str = None,
        template_id: str = None,
    ):
        self.app_name = app_name
        self.update_time = update_time
        self.stack_id = stack_id
        self.create_time = create_time
        self.app_id = app_id
        self.stack_name = stack_name
        self.template_name = template_name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateConfigTemplateResponseBody(TeaModel):
    def __init__(
        self,
        config_template: UpdateConfigTemplateResponseBodyConfigTemplate = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.config_template = config_template
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.config_template:
            self.config_template.validate()

    def to_map(self):
        result = dict()
        if self.config_template is not None:
            result['ConfigTemplate'] = self.config_template.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigTemplate') is not None:
            temp_model = UpdateConfigTemplateResponseBodyConfigTemplate()
            self.config_template = temp_model.from_map(m['ConfigTemplate'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateConfigTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateConfigTemplateResponseBody = None,
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
            temp_model = UpdateConfigTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateConfigSettingRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        template_id: str = None,
        stack_id: str = None,
        option_settings: str = None,
    ):
        self.env_id = env_id
        self.template_id = template_id
        self.stack_id = stack_id
        self.option_settings = option_settings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.option_settings is not None:
            result['OptionSettings'] = self.option_settings
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('OptionSettings') is not None:
            self.option_settings = m.get('OptionSettings')
        return self


class ValidateConfigSettingResponseBodyConfigValidationResultsConfigValidationResultConfigOption(TeaModel):
    def __init__(
        self,
        regex_desc: str = None,
        max_value: int = None,
        editor_type: str = None,
        min_value: int = None,
        default_value: str = None,
        max_length: int = None,
        option_label: str = None,
        regex_pattern: str = None,
        change_severity: str = None,
        option_description: str = None,
        option_name: str = None,
        path_name: str = None,
        hidden_option: bool = None,
        value_type: str = None,
        min_length: int = None,
        value_options: str = None,
        readonly_option: bool = None,
    ):
        self.regex_desc = regex_desc
        self.max_value = max_value
        self.editor_type = editor_type
        self.min_value = min_value
        self.default_value = default_value
        self.max_length = max_length
        self.option_label = option_label
        self.regex_pattern = regex_pattern
        self.change_severity = change_severity
        self.option_description = option_description
        self.option_name = option_name
        self.path_name = path_name
        self.hidden_option = hidden_option
        self.value_type = value_type
        self.min_length = min_length
        self.value_options = value_options
        self.readonly_option = readonly_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.regex_desc is not None:
            result['RegexDesc'] = self.regex_desc
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.editor_type is not None:
            result['EditorType'] = self.editor_type
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.option_label is not None:
            result['OptionLabel'] = self.option_label
        if self.regex_pattern is not None:
            result['RegexPattern'] = self.regex_pattern
        if self.change_severity is not None:
            result['ChangeSeverity'] = self.change_severity
        if self.option_description is not None:
            result['OptionDescription'] = self.option_description
        if self.option_name is not None:
            result['OptionName'] = self.option_name
        if self.path_name is not None:
            result['PathName'] = self.path_name
        if self.hidden_option is not None:
            result['HiddenOption'] = self.hidden_option
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.value_options is not None:
            result['ValueOptions'] = self.value_options
        if self.readonly_option is not None:
            result['ReadonlyOption'] = self.readonly_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegexDesc') is not None:
            self.regex_desc = m.get('RegexDesc')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('EditorType') is not None:
            self.editor_type = m.get('EditorType')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('OptionLabel') is not None:
            self.option_label = m.get('OptionLabel')
        if m.get('RegexPattern') is not None:
            self.regex_pattern = m.get('RegexPattern')
        if m.get('ChangeSeverity') is not None:
            self.change_severity = m.get('ChangeSeverity')
        if m.get('OptionDescription') is not None:
            self.option_description = m.get('OptionDescription')
        if m.get('OptionName') is not None:
            self.option_name = m.get('OptionName')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        if m.get('HiddenOption') is not None:
            self.hidden_option = m.get('HiddenOption')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('ValueOptions') is not None:
            self.value_options = m.get('ValueOptions')
        if m.get('ReadonlyOption') is not None:
            self.readonly_option = m.get('ReadonlyOption')
        return self


class ValidateConfigSettingResponseBodyConfigValidationResultsConfigValidationResult(TeaModel):
    def __init__(
        self,
        option_name: str = None,
        path_name: str = None,
        result_message: str = None,
        result_severity: str = None,
        config_option: ValidateConfigSettingResponseBodyConfigValidationResultsConfigValidationResultConfigOption = None,
    ):
        self.option_name = option_name
        self.path_name = path_name
        self.result_message = result_message
        self.result_severity = result_severity
        self.config_option = config_option

    def validate(self):
        if self.config_option:
            self.config_option.validate()

    def to_map(self):
        result = dict()
        if self.option_name is not None:
            result['OptionName'] = self.option_name
        if self.path_name is not None:
            result['PathName'] = self.path_name
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.result_severity is not None:
            result['ResultSeverity'] = self.result_severity
        if self.config_option is not None:
            result['ConfigOption'] = self.config_option.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionName') is not None:
            self.option_name = m.get('OptionName')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('ResultSeverity') is not None:
            self.result_severity = m.get('ResultSeverity')
        if m.get('ConfigOption') is not None:
            temp_model = ValidateConfigSettingResponseBodyConfigValidationResultsConfigValidationResultConfigOption()
            self.config_option = temp_model.from_map(m['ConfigOption'])
        return self


class ValidateConfigSettingResponseBodyConfigValidationResults(TeaModel):
    def __init__(
        self,
        config_validation_result: List[ValidateConfigSettingResponseBodyConfigValidationResultsConfigValidationResult] = None,
    ):
        self.config_validation_result = config_validation_result

    def validate(self):
        if self.config_validation_result:
            for k in self.config_validation_result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConfigValidationResult'] = []
        if self.config_validation_result is not None:
            for k in self.config_validation_result:
                result['ConfigValidationResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_validation_result = []
        if m.get('ConfigValidationResult') is not None:
            for k in m.get('ConfigValidationResult'):
                temp_model = ValidateConfigSettingResponseBodyConfigValidationResultsConfigValidationResult()
                self.config_validation_result.append(temp_model.from_map(k))
        return self


class ValidateConfigSettingResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        config_validation_results: ValidateConfigSettingResponseBodyConfigValidationResults = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.config_validation_results = config_validation_results
        self.code = code

    def validate(self):
        if self.config_validation_results:
            self.config_validation_results.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.config_validation_results is not None:
            result['ConfigValidationResults'] = self.config_validation_results.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConfigValidationResults') is not None:
            temp_model = ValidateConfigSettingResponseBodyConfigValidationResults()
            self.config_validation_results = temp_model.from_map(m['ConfigValidationResults'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ValidateConfigSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateConfigSettingResponseBody = None,
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
            temp_model = ValidateConfigSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


