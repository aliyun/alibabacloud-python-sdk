# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CancelExecutionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        execution_id: str = None,
    ):
        self.region_id = region_id
        self.execution_id = execution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        return self


class CancelExecutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelExecutionResponseBody = None,
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
            temp_model = CancelExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateParameterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
        description: str = None,
        client_token: str = None,
        constraints: str = None,
    ):
        self.region_id = region_id
        self.name = name
        self.type = type
        self.value = value
        self.description = description
        self.client_token = client_token
        self.constraints = constraints

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.description is not None:
            result['Description'] = self.description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        return self


class CreateParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        type: str = None,
        constraints: str = None,
        description: str = None,
        updated_date: str = None,
        updated_by: str = None,
        created_by: str = None,
        parameter_version: int = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.constraints = constraints
        self.description = description
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.created_by = created_by
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class CreateParameterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        parameter: CreateParameterResponseBodyParameter = None,
    ):
        self.request_id = request_id
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Parameter') is not None:
            temp_model = CreateParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class CreateParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateParameterResponseBody = None,
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
            temp_model = CreateParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecretParameterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
        description: str = None,
        key_id: str = None,
        client_token: str = None,
        constraints: str = None,
    ):
        self.region_id = region_id
        self.name = name
        self.type = type
        self.value = value
        self.description = description
        self.key_id = key_id
        self.client_token = client_token
        self.constraints = constraints

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.description is not None:
            result['Description'] = self.description
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        return self


class CreateSecretParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        type: str = None,
        updated_date: str = None,
        updated_by: str = None,
        key_id: str = None,
        constraints: str = None,
        description: str = None,
        created_by: str = None,
        parameter_version: int = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.key_id = key_id
        self.constraints = constraints
        self.description = description
        self.created_by = created_by
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class CreateSecretParameterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        parameter: CreateSecretParameterResponseBodyParameter = None,
    ):
        self.request_id = request_id
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Parameter') is not None:
            temp_model = CreateSecretParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class CreateSecretParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSecretParameterResponseBody = None,
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
            temp_model = CreateSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        content: str = None,
        tags: Dict[str, Any] = None,
        version_name: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.content = content
        self.tags = tags
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.content is not None:
            result['Content'] = self.content
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        content: str = None,
        tags_shrink: str = None,
        version_name: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.content = content
        self.tags_shrink = tags_shrink
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.content is not None:
            result['Content'] = self.content
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        hash: str = None,
        updated_date: str = None,
        updated_by: str = None,
        tags: Dict[str, Any] = None,
        template_name: str = None,
        template_version: str = None,
        template_format: str = None,
        description: str = None,
        created_by: str = None,
        created_date: str = None,
        has_trigger: bool = None,
        template_id: str = None,
        share_type: str = None,
    ):
        self.hash = hash
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.tags = tags
        self.template_name = template_name
        self.template_version = template_version
        self.template_format = template_format
        self.description = description
        self.created_by = created_by
        self.created_date = created_date
        self.has_trigger = has_trigger
        self.template_id = template_id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_type: str = None,
        template: CreateTemplateResponseBodyTemplate = None,
    ):
        self.request_id = request_id
        self.template_type = template_type
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('Template') is not None:
            temp_model = CreateTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTemplateResponseBody = None,
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExecutionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        execution_ids: str = None,
    ):
        self.region_id = region_id
        self.execution_ids = execution_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.execution_ids is not None:
            result['ExecutionIds'] = self.execution_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExecutionIds') is not None:
            self.execution_ids = m.get('ExecutionIds')
        return self


class DeleteExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteExecutionsResponseBody = None,
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
            temp_model = DeleteExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteParameterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
    ):
        self.region_id = region_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteParameterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteParameterResponseBody = None,
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
            temp_model = DeleteParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretParameterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
    ):
        self.region_id = region_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteSecretParameterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSecretParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSecretParameterResponseBody = None,
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
            temp_model = DeleteSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        auto_delete_executions: bool = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.auto_delete_executions = auto_delete_executions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.auto_delete_executions is not None:
            result['AutoDeleteExecutions'] = self.auto_delete_executions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('AutoDeleteExecutions') is not None:
            self.auto_delete_executions = m.get('AutoDeleteExecutions')
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTemplateResponseBody = None,
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplatesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_names: str = None,
        auto_delete_executions: bool = None,
    ):
        self.region_id = region_id
        self.template_names = template_names
        self.auto_delete_executions = auto_delete_executions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_names is not None:
            result['TemplateNames'] = self.template_names
        if self.auto_delete_executions is not None:
            result['AutoDeleteExecutions'] = self.auto_delete_executions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateNames') is not None:
            self.template_names = m.get('TemplateNames')
        if m.get('AutoDeleteExecutions') is not None:
            self.auto_delete_executions = m.get('AutoDeleteExecutions')
        return self


class DeleteTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTemplatesResponseBody = None,
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
            temp_model = DeleteTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        accept_language: str = None,
    ):
        self.region_id = region_id
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateExecutionPolicyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GenerateExecutionPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: str = None,
        request_id: str = None,
    ):
        self.policy = policy
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateExecutionPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateExecutionPolicyResponseBody = None,
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
            temp_model = GenerateExecutionPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExecutionTemplateRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        execution_id: str = None,
    ):
        self.region_id = region_id
        self.execution_id = execution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        return self


class GetExecutionTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        hash: str = None,
        updated_date: str = None,
        updated_by: str = None,
        tags: Dict[str, Any] = None,
        template_name: str = None,
        template_version: str = None,
        template_format: str = None,
        description: str = None,
        created_by: str = None,
        created_date: str = None,
        template_id: str = None,
        share_type: str = None,
    ):
        self.hash = hash
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.tags = tags
        self.template_name = template_name
        self.template_version = template_version
        self.template_format = template_format
        self.description = description
        self.created_by = created_by
        self.created_date = created_date
        self.template_id = template_id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class GetExecutionTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        content: str = None,
        template: GetExecutionTemplateResponseBodyTemplate = None,
    ):
        self.request_id = request_id
        self.content = content
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Template') is not None:
            temp_model = GetExecutionTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetExecutionTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExecutionTemplateResponseBody = None,
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
            temp_model = GetExecutionTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInventorySchemaRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        aggregator: bool = None,
        type_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.aggregator = aggregator
        self.type_name = type_name
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetInventorySchemaResponseBodySchemasAttributes(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        name: str = None,
    ):
        self.data_type = data_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetInventorySchemaResponseBodySchemas(TeaModel):
    def __init__(
        self,
        version: str = None,
        attributes: List[GetInventorySchemaResponseBodySchemasAttributes] = None,
        type_name: str = None,
    ):
        self.version = version
        self.attributes = attributes
        self.type_name = type_name

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = GetInventorySchemaResponseBodySchemasAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class GetInventorySchemaResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        schemas: List[GetInventorySchemaResponseBodySchemas] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.schemas = schemas

    def validate(self):
        if self.schemas:
            for k in self.schemas:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['Schemas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.schemas = []
        if m.get('Schemas') is not None:
            for k in m.get('Schemas'):
                temp_model = GetInventorySchemaResponseBodySchemas()
                self.schemas.append(temp_model.from_map(k))
        return self


class GetInventorySchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInventorySchemaResponseBody = None,
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
            temp_model = GetInventorySchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParameterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
        parameter_version: int = None,
    ):
        self.region_id = region_id
        self.name = name
        self.parameter_version = parameter_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        return self


class GetParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        type: str = None,
        updated_date: str = None,
        updated_by: str = None,
        value: str = None,
        constraints: str = None,
        description: str = None,
        created_by: str = None,
        parameter_version: int = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.value = value
        self.constraints = constraints
        self.description = description
        self.created_by = created_by
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.value is not None:
            result['Value'] = self.value
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class GetParameterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        parameter: GetParameterResponseBodyParameter = None,
    ):
        self.request_id = request_id
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Parameter') is not None:
            temp_model = GetParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class GetParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetParameterResponseBody = None,
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
            temp_model = GetParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParametersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        names: str = None,
    ):
        self.region_id = region_id
        self.names = names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.names is not None:
            result['Names'] = self.names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        return self


class GetParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        type: str = None,
        updated_date: str = None,
        updated_by: str = None,
        value: str = None,
        constraints: str = None,
        description: str = None,
        created_by: str = None,
        parameter_version: int = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.value = value
        self.constraints = constraints
        self.description = description
        self.created_by = created_by
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.value is not None:
            result['Value'] = self.value
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class GetParametersResponseBody(TeaModel):
    def __init__(
        self,
        parameters: List[GetParametersResponseBodyParameters] = None,
        request_id: str = None,
        invalid_parameters: List[str] = None,
    ):
        self.parameters = parameters
        self.request_id = request_id
        self.invalid_parameters = invalid_parameters

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invalid_parameters is not None:
            result['InvalidParameters'] = self.invalid_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvalidParameters') is not None:
            self.invalid_parameters = m.get('InvalidParameters')
        return self


class GetParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetParametersResponseBody = None,
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
            temp_model = GetParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParametersByPathRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        path: str = None,
        recursive: bool = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.region_id = region_id
        self.path = path
        self.recursive = recursive
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class GetParametersByPathResponseBodyParameters(TeaModel):
    def __init__(
        self,
        type: str = None,
        updated_date: str = None,
        updated_by: str = None,
        value: str = None,
        constraints: str = None,
        description: str = None,
        created_by: str = None,
        parameter_version: int = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.value = value
        self.constraints = constraints
        self.description = description
        self.created_by = created_by
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.value is not None:
            result['Value'] = self.value
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class GetParametersByPathResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        parameters: List[GetParametersByPathResponseBodyParameters] = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
    ):
        self.total_count = total_count
        self.parameters = parameters
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetParametersByPathResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class GetParametersByPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetParametersByPathResponseBody = None,
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
            temp_model = GetParametersByPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretParameterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
        parameter_version: int = None,
        with_decryption: bool = None,
    ):
        self.region_id = region_id
        self.name = name
        self.parameter_version = parameter_version
        self.with_decryption = with_decryption

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class GetSecretParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        type: str = None,
        updated_date: str = None,
        updated_by: str = None,
        key_id: str = None,
        value: str = None,
        constraints: str = None,
        description: str = None,
        created_by: str = None,
        parameter_version: int = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.key_id = key_id
        self.value = value
        self.constraints = constraints
        self.description = description
        self.created_by = created_by
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.value is not None:
            result['Value'] = self.value
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class GetSecretParameterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        parameter: GetSecretParameterResponseBodyParameter = None,
    ):
        self.request_id = request_id
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Parameter') is not None:
            temp_model = GetSecretParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class GetSecretParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSecretParameterResponseBody = None,
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
            temp_model = GetSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretParametersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        names: str = None,
        with_decryption: bool = None,
    ):
        self.region_id = region_id
        self.names = names
        self.with_decryption = with_decryption

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.names is not None:
            result['Names'] = self.names
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class GetSecretParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        type: str = None,
        updated_date: str = None,
        updated_by: str = None,
        key_id: str = None,
        value: str = None,
        constraints: str = None,
        description: str = None,
        created_by: str = None,
        parameter_version: int = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.key_id = key_id
        self.value = value
        self.constraints = constraints
        self.description = description
        self.created_by = created_by
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.value is not None:
            result['Value'] = self.value
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class GetSecretParametersResponseBody(TeaModel):
    def __init__(
        self,
        parameters: List[GetSecretParametersResponseBodyParameters] = None,
        request_id: str = None,
        invalid_parameters: List[str] = None,
    ):
        self.parameters = parameters
        self.request_id = request_id
        self.invalid_parameters = invalid_parameters

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invalid_parameters is not None:
            result['InvalidParameters'] = self.invalid_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetSecretParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvalidParameters') is not None:
            self.invalid_parameters = m.get('InvalidParameters')
        return self


class GetSecretParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSecretParametersResponseBody = None,
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
            temp_model = GetSecretParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretParametersByPathRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        path: str = None,
        recursive: bool = None,
        next_token: str = None,
        max_results: int = None,
        with_decryption: bool = None,
    ):
        self.region_id = region_id
        self.path = path
        self.recursive = recursive
        self.next_token = next_token
        self.max_results = max_results
        self.with_decryption = with_decryption

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class GetSecretParametersByPathResponseBodyParameters(TeaModel):
    def __init__(
        self,
        type: str = None,
        updated_date: str = None,
        updated_by: str = None,
        key_id: str = None,
        value: str = None,
        constraints: str = None,
        description: str = None,
        created_by: str = None,
        parameter_version: int = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.key_id = key_id
        self.value = value
        self.constraints = constraints
        self.description = description
        self.created_by = created_by
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.value is not None:
            result['Value'] = self.value
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class GetSecretParametersByPathResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        parameters: List[GetSecretParametersByPathResponseBodyParameters] = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
    ):
        self.total_count = total_count
        self.parameters = parameters
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetSecretParametersByPathResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class GetSecretParametersByPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSecretParametersByPathResponseBody = None,
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
            temp_model = GetSecretParametersByPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceSettingsResponseBodyServiceSettings(TeaModel):
    def __init__(
        self,
        delivery_oss_bucket_name: str = None,
        delivery_oss_key_prefix: str = None,
        delivery_sls_enabled: bool = None,
        delivery_oss_enabled: bool = None,
        delivery_sls_project_name: str = None,
    ):
        self.delivery_oss_bucket_name = delivery_oss_bucket_name
        self.delivery_oss_key_prefix = delivery_oss_key_prefix
        self.delivery_sls_enabled = delivery_sls_enabled
        self.delivery_oss_enabled = delivery_oss_enabled
        self.delivery_sls_project_name = delivery_sls_project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.delivery_oss_bucket_name is not None:
            result['DeliveryOssBucketName'] = self.delivery_oss_bucket_name
        if self.delivery_oss_key_prefix is not None:
            result['DeliveryOssKeyPrefix'] = self.delivery_oss_key_prefix
        if self.delivery_sls_enabled is not None:
            result['DeliverySlsEnabled'] = self.delivery_sls_enabled
        if self.delivery_oss_enabled is not None:
            result['DeliveryOssEnabled'] = self.delivery_oss_enabled
        if self.delivery_sls_project_name is not None:
            result['DeliverySlsProjectName'] = self.delivery_sls_project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryOssBucketName') is not None:
            self.delivery_oss_bucket_name = m.get('DeliveryOssBucketName')
        if m.get('DeliveryOssKeyPrefix') is not None:
            self.delivery_oss_key_prefix = m.get('DeliveryOssKeyPrefix')
        if m.get('DeliverySlsEnabled') is not None:
            self.delivery_sls_enabled = m.get('DeliverySlsEnabled')
        if m.get('DeliveryOssEnabled') is not None:
            self.delivery_oss_enabled = m.get('DeliveryOssEnabled')
        if m.get('DeliverySlsProjectName') is not None:
            self.delivery_sls_project_name = m.get('DeliverySlsProjectName')
        return self


class GetServiceSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_settings: List[GetServiceSettingsResponseBodyServiceSettings] = None,
    ):
        self.request_id = request_id
        self.service_settings = service_settings

    def validate(self):
        if self.service_settings:
            for k in self.service_settings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceSettings'] = []
        if self.service_settings is not None:
            for k in self.service_settings:
                result['ServiceSettings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_settings = []
        if m.get('ServiceSettings') is not None:
            for k in m.get('ServiceSettings'):
                temp_model = GetServiceSettingsResponseBodyServiceSettings()
                self.service_settings.append(temp_model.from_map(k))
        return self


class GetServiceSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetServiceSettingsResponseBody = None,
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
            temp_model = GetServiceSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        hash: str = None,
        updated_date: str = None,
        updated_by: str = None,
        tags: Dict[str, Any] = None,
        template_type: str = None,
        template_name: str = None,
        template_version: str = None,
        template_format: str = None,
        description: str = None,
        created_by: str = None,
        created_date: str = None,
        version_name: str = None,
        template_id: str = None,
        has_trigger: bool = None,
        share_type: str = None,
    ):
        self.hash = hash
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.tags = tags
        self.template_type = template_type
        self.template_name = template_name
        self.template_version = template_version
        self.template_format = template_format
        self.description = description
        self.created_by = created_by
        self.created_date = created_date
        self.version_name = version_name
        self.template_id = template_id
        self.has_trigger = has_trigger
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        content: str = None,
        template: GetTemplateResponseBodyTemplate = None,
    ):
        self.request_id = request_id
        self.content = content
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Template') is not None:
            temp_model = GetTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
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


class ListActionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        oosaction_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.oosaction_name = oosaction_name
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.oosaction_name is not None:
            result['OOSActionName'] = self.oosaction_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OOSActionName') is not None:
            self.oosaction_name = m.get('OOSActionName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListActionsResponseBodyActions(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        description: str = None,
        created_date: str = None,
        template_version: str = None,
        oosaction_name: str = None,
        properties: str = None,
    ):
        self.action_type = action_type
        self.description = description
        self.created_date = created_date
        self.template_version = template_version
        self.oosaction_name = oosaction_name
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.description is not None:
            result['Description'] = self.description
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.oosaction_name is not None:
            result['OOSActionName'] = self.oosaction_name
        if self.properties is not None:
            result['Properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('OOSActionName') is not None:
            self.oosaction_name = m.get('OOSActionName')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        return self


class ListActionsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        actions: List[ListActionsResponseBodyActions] = None,
        max_results: int = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.actions = actions
        self.max_results = max_results

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = ListActionsResponseBodyActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListActionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListActionsResponseBody = None,
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
            temp_model = ListActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionLogsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        execution_id: str = None,
        task_execution_id: str = None,
        log_type: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.execution_id = execution_id
        self.task_execution_id = task_execution_id
        self.log_type = log_type
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListExecutionLogsResponseBodyExecutionLogs(TeaModel):
    def __init__(
        self,
        task_execution_id: str = None,
        message: str = None,
        log_type: str = None,
        timestamp: str = None,
    ):
        self.task_execution_id = task_execution_id
        self.message = message
        self.log_type = log_type
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.message is not None:
            result['Message'] = self.message
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ListExecutionLogsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        execution_logs: List[ListExecutionLogsResponseBodyExecutionLogs] = None,
        max_results: int = None,
        is_truncated: bool = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.execution_logs = execution_logs
        self.max_results = max_results
        self.is_truncated = is_truncated

    def validate(self):
        if self.execution_logs:
            for k in self.execution_logs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ExecutionLogs'] = []
        if self.execution_logs is not None:
            for k in self.execution_logs:
                result['ExecutionLogs'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.execution_logs = []
        if m.get('ExecutionLogs') is not None:
            for k in m.get('ExecutionLogs'):
                temp_model = ListExecutionLogsResponseBodyExecutionLogs()
                self.execution_logs.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        return self


class ListExecutionLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListExecutionLogsResponseBody = None,
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
            temp_model = ListExecutionLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionRiskyTasksRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListExecutionRiskyTasksResponseBodyRiskyTasks(TeaModel):
    def __init__(
        self,
        service: str = None,
        task: List[str] = None,
        api: str = None,
        template: List[str] = None,
    ):
        self.service = service
        self.task = task
        self.api = api
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.task is not None:
            result['Task'] = self.task
        if self.api is not None:
            result['API'] = self.api
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('API') is not None:
            self.api = m.get('API')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class ListExecutionRiskyTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        risky_tasks: List[ListExecutionRiskyTasksResponseBodyRiskyTasks] = None,
    ):
        self.request_id = request_id
        self.risky_tasks = risky_tasks

    def validate(self):
        if self.risky_tasks:
            for k in self.risky_tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RiskyTasks'] = []
        if self.risky_tasks is not None:
            for k in self.risky_tasks:
                result['RiskyTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.risky_tasks = []
        if m.get('RiskyTasks') is not None:
            for k in m.get('RiskyTasks'):
                temp_model = ListExecutionRiskyTasksResponseBodyRiskyTasks()
                self.risky_tasks.append(temp_model.from_map(k))
        return self


class ListExecutionRiskyTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListExecutionRiskyTasksResponseBody = None,
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
            temp_model = ListExecutionRiskyTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        status: str = None,
        execution_id: str = None,
        start_date_before: str = None,
        start_date_after: str = None,
        end_date_before: str = None,
        end_date_after: str = None,
        mode: str = None,
        executed_by: str = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        include_child_execution: bool = None,
        category: str = None,
        tags: Dict[str, Any] = None,
        max_results: int = None,
        next_token: str = None,
        sort_field: str = None,
        sort_order: str = None,
        resource_id: str = None,
        resource_template_name: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.status = status
        self.execution_id = execution_id
        self.start_date_before = start_date_before
        self.start_date_after = start_date_after
        self.end_date_before = end_date_before
        self.end_date_after = end_date_after
        self.mode = mode
        self.executed_by = executed_by
        self.parent_execution_id = parent_execution_id
        self.ram_role = ram_role
        self.include_child_execution = include_child_execution
        self.category = category
        self.tags = tags
        self.max_results = max_results
        self.next_token = next_token
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.resource_id = resource_id
        self.resource_template_name = resource_template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.status is not None:
            result['Status'] = self.status
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before
        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after
        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.include_child_execution is not None:
            result['IncludeChildExecution'] = self.include_child_execution
        if self.category is not None:
            result['Category'] = self.category
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_template_name is not None:
            result['ResourceTemplateName'] = self.resource_template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')
        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')
        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('IncludeChildExecution') is not None:
            self.include_child_execution = m.get('IncludeChildExecution')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceTemplateName') is not None:
            self.resource_template_name = m.get('ResourceTemplateName')
        return self


class ListExecutionsShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        status: str = None,
        execution_id: str = None,
        start_date_before: str = None,
        start_date_after: str = None,
        end_date_before: str = None,
        end_date_after: str = None,
        mode: str = None,
        executed_by: str = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        include_child_execution: bool = None,
        category: str = None,
        tags_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        sort_field: str = None,
        sort_order: str = None,
        resource_id: str = None,
        resource_template_name: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.status = status
        self.execution_id = execution_id
        self.start_date_before = start_date_before
        self.start_date_after = start_date_after
        self.end_date_before = end_date_before
        self.end_date_after = end_date_after
        self.mode = mode
        self.executed_by = executed_by
        self.parent_execution_id = parent_execution_id
        self.ram_role = ram_role
        self.include_child_execution = include_child_execution
        self.category = category
        self.tags_shrink = tags_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.resource_id = resource_id
        self.resource_template_name = resource_template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.status is not None:
            result['Status'] = self.status
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before
        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after
        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.include_child_execution is not None:
            result['IncludeChildExecution'] = self.include_child_execution
        if self.category is not None:
            result['Category'] = self.category
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_template_name is not None:
            result['ResourceTemplateName'] = self.resource_template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')
        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')
        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('IncludeChildExecution') is not None:
            self.include_child_execution = m.get('IncludeChildExecution')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceTemplateName') is not None:
            self.resource_template_name = m.get('ResourceTemplateName')
        return self


class ListExecutionsResponseBodyExecutionsCurrentTasks(TeaModel):
    def __init__(
        self,
        task_execution_id: str = None,
        task_name: str = None,
        task_action: str = None,
    ):
        self.task_execution_id = task_execution_id
        self.task_name = task_name
        self.task_action = task_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        return self


class ListExecutionsResponseBodyExecutions(TeaModel):
    def __init__(
        self,
        status: str = None,
        waiting_status: str = None,
        targets: str = None,
        status_reason: str = None,
        tags: Dict[str, Any] = None,
        last_successful_trigger_time: str = None,
        mode: str = None,
        safety_check: str = None,
        template_name: str = None,
        template_version: str = None,
        create_date: str = None,
        current_tasks: List[ListExecutionsResponseBodyExecutionsCurrentTasks] = None,
        description: str = None,
        update_date: str = None,
        parent_execution_id: str = None,
        last_trigger_time: str = None,
        last_trigger_status: str = None,
        status_message: str = None,
        outputs: str = None,
        end_date: str = None,
        executed_by: str = None,
        is_parent: bool = None,
        start_date: str = None,
        execution_id: str = None,
        parameters: Dict[str, Any] = None,
        counters: Dict[str, Any] = None,
        category: str = None,
        template_id: str = None,
        ram_role: str = None,
        resource_status: str = None,
    ):
        self.status = status
        self.waiting_status = waiting_status
        self.targets = targets
        self.status_reason = status_reason
        self.tags = tags
        self.last_successful_trigger_time = last_successful_trigger_time
        self.mode = mode
        self.safety_check = safety_check
        self.template_name = template_name
        self.template_version = template_version
        self.create_date = create_date
        self.current_tasks = current_tasks
        self.description = description
        self.update_date = update_date
        self.parent_execution_id = parent_execution_id
        self.last_trigger_time = last_trigger_time
        self.last_trigger_status = last_trigger_status
        self.status_message = status_message
        self.outputs = outputs
        self.end_date = end_date
        self.executed_by = executed_by
        self.is_parent = is_parent
        self.start_date = start_date
        self.execution_id = execution_id
        self.parameters = parameters
        self.counters = counters
        self.category = category
        self.template_id = template_id
        self.ram_role = ram_role
        self.resource_status = resource_status

    def validate(self):
        if self.current_tasks:
            for k in self.current_tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.waiting_status is not None:
            result['WaitingStatus'] = self.waiting_status
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.last_successful_trigger_time is not None:
            result['LastSuccessfulTriggerTime'] = self.last_successful_trigger_time
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        result['CurrentTasks'] = []
        if self.current_tasks is not None:
            for k in self.current_tasks:
                result['CurrentTasks'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.last_trigger_time is not None:
            result['LastTriggerTime'] = self.last_trigger_time
        if self.last_trigger_status is not None:
            result['LastTriggerStatus'] = self.last_trigger_status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.is_parent is not None:
            result['IsParent'] = self.is_parent
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.counters is not None:
            result['Counters'] = self.counters
        if self.category is not None:
            result['Category'] = self.category
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WaitingStatus') is not None:
            self.waiting_status = m.get('WaitingStatus')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LastSuccessfulTriggerTime') is not None:
            self.last_successful_trigger_time = m.get('LastSuccessfulTriggerTime')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        self.current_tasks = []
        if m.get('CurrentTasks') is not None:
            for k in m.get('CurrentTasks'):
                temp_model = ListExecutionsResponseBodyExecutionsCurrentTasks()
                self.current_tasks.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('LastTriggerTime') is not None:
            self.last_trigger_time = m.get('LastTriggerTime')
        if m.get('LastTriggerStatus') is not None:
            self.last_trigger_status = m.get('LastTriggerStatus')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('IsParent') is not None:
            self.is_parent = m.get('IsParent')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Counters') is not None:
            self.counters = m.get('Counters')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        return self


class ListExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        executions: List[ListExecutionsResponseBodyExecutions] = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
    ):
        self.executions = executions
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results

    def validate(self):
        if self.executions:
            for k in self.executions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Executions'] = []
        if self.executions is not None:
            for k in self.executions:
                result['Executions'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.executions = []
        if m.get('Executions') is not None:
            for k in m.get('Executions'):
                temp_model = ListExecutionsResponseBodyExecutions()
                self.executions.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListExecutionsResponseBody = None,
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
            temp_model = ListExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInventoryEntriesRequestFilter(TeaModel):
    def __init__(
        self,
        value: List[str] = None,
        operator: str = None,
        name: str = None,
    ):
        self.value = value
        self.operator = operator
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListInventoryEntriesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        type_name: str = None,
        max_results: int = None,
        next_token: str = None,
        filter: List[ListInventoryEntriesRequestFilter] = None,
    ):
        self.instance_id = instance_id
        self.type_name = type_name
        self.max_results = max_results
        self.next_token = next_token
        self.filter = filter

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListInventoryEntriesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class ListInventoryEntriesResponseBody(TeaModel):
    def __init__(
        self,
        type_name: str = None,
        capture_time: str = None,
        next_token: str = None,
        request_id: str = None,
        schema_version: str = None,
        instance_id: str = None,
        max_results: int = None,
        entries: List[Dict[str, Any]] = None,
    ):
        self.type_name = type_name
        self.capture_time = capture_time
        self.next_token = next_token
        self.request_id = request_id
        self.schema_version = schema_version
        self.instance_id = instance_id
        self.max_results = max_results
        self.entries = entries

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.entries is not None:
            result['Entries'] = self.entries
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Entries') is not None:
            self.entries = m.get('Entries')
        return self


class ListInventoryEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInventoryEntriesResponseBody = None,
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
            temp_model = ListInventoryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParametersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
        max_results: int = None,
        next_token: str = None,
        sort_field: str = None,
        sort_order: str = None,
        type: str = None,
        path: str = None,
        recursive: bool = None,
    ):
        self.region_id = region_id
        self.name = name
        self.max_results = max_results
        self.next_token = next_token
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.type = type
        self.path = path
        self.recursive = recursive

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.type is not None:
            result['Type'] = self.type
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        return self


class ListParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        type: str = None,
        description: str = None,
        updated_date: str = None,
        updated_by: str = None,
        created_by: str = None,
        parameter_version: str = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.description = description
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.created_by = created_by
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.description is not None:
            result['Description'] = self.description
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class ListParametersResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        parameters: List[ListParametersResponseBodyParameters] = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
    ):
        self.total_count = total_count
        self.parameters = parameters
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ListParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListParametersResponseBody = None,
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
            temp_model = ListParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParameterVersionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
        max_results: int = None,
        next_token: str = None,
        share_type: str = None,
    ):
        self.region_id = region_id
        self.name = name
        self.max_results = max_results
        self.next_token = next_token
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class ListParameterVersionsResponseBodyParameterVersions(TeaModel):
    def __init__(
        self,
        value: str = None,
        updated_date: str = None,
        updated_by: str = None,
        parameter_version: int = None,
    ):
        self.value = value
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.parameter_version = parameter_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        return self


class ListParameterVersionsResponseBody(TeaModel):
    def __init__(
        self,
        type: str = None,
        total_count: int = None,
        parameter_versions: List[ListParameterVersionsResponseBodyParameterVersions] = None,
        description: str = None,
        created_by: str = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        created_date: str = None,
        id: str = None,
        name: str = None,
    ):
        self.type = type
        self.total_count = total_count
        self.parameter_versions = parameter_versions
        self.description = description
        self.created_by = created_by
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.created_date = created_date
        self.id = id
        self.name = name

    def validate(self):
        if self.parameter_versions:
            for k in self.parameter_versions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ParameterVersions'] = []
        if self.parameter_versions is not None:
            for k in self.parameter_versions:
                result['ParameterVersions'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.parameter_versions = []
        if m.get('ParameterVersions') is not None:
            for k in m.get('ParameterVersions'):
                temp_model = ListParameterVersionsResponseBodyParameterVersions()
                self.parameter_versions.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListParameterVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListParameterVersionsResponseBody = None,
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
            temp_model = ListParameterVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceExecutionStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        execution_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.execution_id = execution_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListResourceExecutionStatusResponseBodyResourceExecutionStatus(TeaModel):
    def __init__(
        self,
        outputs: str = None,
        status: str = None,
        execution_time: str = None,
        resource_id: str = None,
        execution_id: str = None,
    ):
        self.outputs = outputs
        self.status = status
        self.execution_time = execution_time
        self.resource_id = resource_id
        self.execution_id = execution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.status is not None:
            result['Status'] = self.status
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        return self


class ListResourceExecutionStatusResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_execution_status: List[ListResourceExecutionStatusResponseBodyResourceExecutionStatus] = None,
        max_results: int = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.resource_execution_status = resource_execution_status
        self.max_results = max_results

    def validate(self):
        if self.resource_execution_status:
            for k in self.resource_execution_status:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceExecutionStatus'] = []
        if self.resource_execution_status is not None:
            for k in self.resource_execution_status:
                result['ResourceExecutionStatus'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_execution_status = []
        if m.get('ResourceExecutionStatus') is not None:
            for k in m.get('ResourceExecutionStatus'):
                temp_model = ListResourceExecutionStatusResponseBodyResourceExecutionStatus()
                self.resource_execution_status.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListResourceExecutionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListResourceExecutionStatusResponseBody = None,
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
            temp_model = ListResourceExecutionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretParametersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
        max_results: int = None,
        next_token: str = None,
        sort_field: str = None,
        sort_order: str = None,
        path: str = None,
        recursive: bool = None,
    ):
        self.region_id = region_id
        self.name = name
        self.max_results = max_results
        self.next_token = next_token
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.path = path
        self.recursive = recursive

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        return self


class ListSecretParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        type: str = None,
        description: str = None,
        updated_date: str = None,
        updated_by: str = None,
        created_by: str = None,
        key_id: str = None,
        parameter_version: str = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.description = description
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.created_by = created_by
        self.key_id = key_id
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.description is not None:
            result['Description'] = self.description
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class ListSecretParametersResponseBody(TeaModel):
    def __init__(
        self,
        parameters: List[ListSecretParametersResponseBodyParameters] = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
    ):
        self.parameters = parameters
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ListSecretParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListSecretParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSecretParametersResponseBody = None,
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
            temp_model = ListSecretParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretParameterVersionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
        max_results: int = None,
        next_token: str = None,
        share_type: str = None,
        with_decryption: bool = None,
    ):
        self.region_id = region_id
        self.name = name
        self.max_results = max_results
        self.next_token = next_token
        self.share_type = share_type
        self.with_decryption = with_decryption

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class ListSecretParameterVersionsResponseBodyParameterVersions(TeaModel):
    def __init__(
        self,
        value: str = None,
        updated_date: str = None,
        updated_by: str = None,
        parameter_version: int = None,
    ):
        self.value = value
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.parameter_version = parameter_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        return self


class ListSecretParameterVersionsResponseBody(TeaModel):
    def __init__(
        self,
        type: str = None,
        total_count: int = None,
        parameter_versions: List[ListSecretParameterVersionsResponseBodyParameterVersions] = None,
        description: str = None,
        created_by: str = None,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        created_date: str = None,
        id: str = None,
        name: str = None,
    ):
        self.type = type
        self.total_count = total_count
        self.parameter_versions = parameter_versions
        self.description = description
        self.created_by = created_by
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.created_date = created_date
        self.id = id
        self.name = name

    def validate(self):
        if self.parameter_versions:
            for k in self.parameter_versions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ParameterVersions'] = []
        if self.parameter_versions is not None:
            for k in self.parameter_versions:
                result['ParameterVersions'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.parameter_versions = []
        if m.get('ParameterVersions') is not None:
            for k in m.get('ParameterVersions'):
                temp_model = ListSecretParameterVersionsResponseBodyParameterVersions()
                self.parameter_versions.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListSecretParameterVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSecretParameterVersionsResponseBody = None,
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
            temp_model = ListSecretParameterVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_type: str = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        keys: List[str] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagKeysResponseBody = None,
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids: Dict[str, Any] = None,
        resource_type: str = None,
        tags: Dict[str, Any] = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tags = tags
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tags_shrink: str = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.resource_ids_shrink = resource_ids_shrink
        self.resource_type = resource_type
        self.tags_shrink = tags_shrink
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
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


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_type: str = None,
        key: str = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.resource_type = resource_type
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        values: List[str] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagValuesResponseBody = None,
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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskExecutionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        execution_id: str = None,
        status: str = None,
        start_date_before: str = None,
        start_date_after: str = None,
        end_date_before: str = None,
        end_date_after: str = None,
        task_execution_id: str = None,
        task_name: str = None,
        task_action: str = None,
        parent_task_execution_id: str = None,
        include_child_task_execution: bool = None,
        max_results: int = None,
        next_token: str = None,
        sort_field: str = None,
        sort_order: str = None,
    ):
        self.region_id = region_id
        self.execution_id = execution_id
        self.status = status
        self.start_date_before = start_date_before
        self.start_date_after = start_date_after
        self.end_date_before = end_date_before
        self.end_date_after = end_date_after
        self.task_execution_id = task_execution_id
        self.task_name = task_name
        self.task_action = task_action
        self.parent_task_execution_id = parent_task_execution_id
        self.include_child_task_execution = include_child_task_execution
        self.max_results = max_results
        self.next_token = next_token
        self.sort_field = sort_field
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.status is not None:
            result['Status'] = self.status
        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before
        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after
        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.parent_task_execution_id is not None:
            result['ParentTaskExecutionId'] = self.parent_task_execution_id
        if self.include_child_task_execution is not None:
            result['IncludeChildTaskExecution'] = self.include_child_task_execution
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')
        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')
        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('ParentTaskExecutionId') is not None:
            self.parent_task_execution_id = m.get('ParentTaskExecutionId')
        if m.get('IncludeChildTaskExecution') is not None:
            self.include_child_task_execution = m.get('IncludeChildTaskExecution')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListTaskExecutionsResponseBodyTaskExecutions(TeaModel):
    def __init__(
        self,
        status: str = None,
        outputs: str = None,
        child_execution_id: str = None,
        end_date: str = None,
        parent_task_execution_id: str = None,
        task_name: str = None,
        start_date: str = None,
        loop_item: str = None,
        create_date: str = None,
        execution_id: str = None,
        task_action: str = None,
        task_execution_id: str = None,
        update_date: str = None,
        loop: Dict[str, Any] = None,
        template_id: str = None,
        loop_batch_number: int = None,
        status_message: str = None,
        extra_data: Dict[str, Any] = None,
        properties: str = None,
    ):
        self.status = status
        self.outputs = outputs
        self.child_execution_id = child_execution_id
        self.end_date = end_date
        self.parent_task_execution_id = parent_task_execution_id
        self.task_name = task_name
        self.start_date = start_date
        self.loop_item = loop_item
        self.create_date = create_date
        self.execution_id = execution_id
        self.task_action = task_action
        self.task_execution_id = task_execution_id
        self.update_date = update_date
        self.loop = loop
        self.template_id = template_id
        self.loop_batch_number = loop_batch_number
        self.status_message = status_message
        self.extra_data = extra_data
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.child_execution_id is not None:
            result['ChildExecutionId'] = self.child_execution_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.parent_task_execution_id is not None:
            result['ParentTaskExecutionId'] = self.parent_task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.loop_item is not None:
            result['LoopItem'] = self.loop_item
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.loop is not None:
            result['Loop'] = self.loop
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.loop_batch_number is not None:
            result['LoopBatchNumber'] = self.loop_batch_number
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.properties is not None:
            result['Properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('ChildExecutionId') is not None:
            self.child_execution_id = m.get('ChildExecutionId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ParentTaskExecutionId') is not None:
            self.parent_task_execution_id = m.get('ParentTaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('LoopItem') is not None:
            self.loop_item = m.get('LoopItem')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('Loop') is not None:
            self.loop = m.get('Loop')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('LoopBatchNumber') is not None:
            self.loop_batch_number = m.get('LoopBatchNumber')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        return self


class ListTaskExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        task_executions: List[ListTaskExecutionsResponseBodyTaskExecutions] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.task_executions = task_executions

    def validate(self):
        if self.task_executions:
            for k in self.task_executions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['TaskExecutions'] = []
        if self.task_executions is not None:
            for k in self.task_executions:
                result['TaskExecutions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.task_executions = []
        if m.get('TaskExecutions') is not None:
            for k in m.get('TaskExecutions'):
                temp_model = ListTaskExecutionsResponseBodyTaskExecutions()
                self.task_executions.append(temp_model.from_map(k))
        return self


class ListTaskExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTaskExecutionsResponseBody = None,
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
            temp_model = ListTaskExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        template_format: str = None,
        share_type: str = None,
        created_by: str = None,
        created_date_before: str = None,
        created_date_after: str = None,
        tags: Dict[str, Any] = None,
        category: str = None,
        max_results: int = None,
        next_token: str = None,
        sort_field: str = None,
        sort_order: str = None,
        has_trigger: bool = None,
        template_type: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.template_format = template_format
        self.share_type = share_type
        self.created_by = created_by
        self.created_date_before = created_date_before
        self.created_date_after = created_date_after
        self.tags = tags
        self.category = category
        self.max_results = max_results
        self.next_token = next_token
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.has_trigger = has_trigger
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date_before is not None:
            result['CreatedDateBefore'] = self.created_date_before
        if self.created_date_after is not None:
            result['CreatedDateAfter'] = self.created_date_after
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.category is not None:
            result['Category'] = self.category
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDateBefore') is not None:
            self.created_date_before = m.get('CreatedDateBefore')
        if m.get('CreatedDateAfter') is not None:
            self.created_date_after = m.get('CreatedDateAfter')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListTemplatesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        template_format: str = None,
        share_type: str = None,
        created_by: str = None,
        created_date_before: str = None,
        created_date_after: str = None,
        tags_shrink: str = None,
        category: str = None,
        max_results: int = None,
        next_token: str = None,
        sort_field: str = None,
        sort_order: str = None,
        has_trigger: bool = None,
        template_type: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.template_format = template_format
        self.share_type = share_type
        self.created_by = created_by
        self.created_date_before = created_date_before
        self.created_date_after = created_date_after
        self.tags_shrink = tags_shrink
        self.category = category
        self.max_results = max_results
        self.next_token = next_token
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.has_trigger = has_trigger
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date_before is not None:
            result['CreatedDateBefore'] = self.created_date_before
        if self.created_date_after is not None:
            result['CreatedDateAfter'] = self.created_date_after
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.category is not None:
            result['Category'] = self.category
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDateBefore') is not None:
            self.created_date_before = m.get('CreatedDateBefore')
        if m.get('CreatedDateAfter') is not None:
            self.created_date_after = m.get('CreatedDateAfter')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        hash: str = None,
        updated_date: str = None,
        updated_by: str = None,
        tags: Dict[str, Any] = None,
        template_type: str = None,
        template_name: str = None,
        template_version: str = None,
        template_format: str = None,
        popularity: int = None,
        description: str = None,
        total_execution_count: int = None,
        created_by: str = None,
        created_date: str = None,
        category: str = None,
        has_trigger: bool = None,
        template_id: str = None,
        share_type: str = None,
    ):
        self.hash = hash
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.tags = tags
        self.template_type = template_type
        self.template_name = template_name
        self.template_version = template_version
        self.template_format = template_format
        self.popularity = popularity
        self.description = description
        self.total_execution_count = total_execution_count
        self.created_by = created_by
        self.created_date = created_date
        self.category = category
        self.has_trigger = has_trigger
        self.template_id = template_id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.description is not None:
            result['Description'] = self.description
        if self.total_execution_count is not None:
            result['TotalExecutionCount'] = self.total_execution_count
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.category is not None:
            result['Category'] = self.category
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TotalExecutionCount') is not None:
            self.total_execution_count = m.get('TotalExecutionCount')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        templates: List[ListTemplatesResponseBodyTemplates] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.templates = templates

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
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


class ListTemplateVersionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        max_results: int = None,
        next_token: str = None,
        share_type: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.max_results = max_results
        self.next_token = next_token
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class ListTemplateVersionsResponseBodyTemplateVersions(TeaModel):
    def __init__(
        self,
        description: str = None,
        updated_date: str = None,
        updated_by: str = None,
        version_name: str = None,
        template_version: str = None,
        template_format: str = None,
    ):
        self.description = description
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.version_name = version_name
        self.template_version = template_version
        self.template_format = template_format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        return self


class ListTemplateVersionsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        template_versions: List[ListTemplateVersionsResponseBodyTemplateVersions] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.template_versions = template_versions

    def validate(self):
        if self.template_versions:
            for k in self.template_versions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['TemplateVersions'] = []
        if self.template_versions is not None:
            for k in self.template_versions:
                result['TemplateVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.template_versions = []
        if m.get('TemplateVersions') is not None:
            for k in m.get('TemplateVersions'):
                temp_model = ListTemplateVersionsResponseBodyTemplateVersions()
                self.template_versions.append(temp_model.from_map(k))
        return self


class ListTemplateVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTemplateVersionsResponseBody = None,
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
            temp_model = ListTemplateVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NotifyExecutionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        execution_id: str = None,
        notify_type: str = None,
        notify_note: str = None,
        task_name: str = None,
        task_execution_id: str = None,
        execution_status: str = None,
        parameters: str = None,
        loop_item: str = None,
        task_execution_ids: str = None,
    ):
        self.region_id = region_id
        self.execution_id = execution_id
        self.notify_type = notify_type
        self.notify_note = notify_note
        self.task_name = task_name
        self.task_execution_id = task_execution_id
        self.execution_status = execution_status
        self.parameters = parameters
        self.loop_item = loop_item
        self.task_execution_ids = task_execution_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.notify_note is not None:
            result['NotifyNote'] = self.notify_note
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.loop_item is not None:
            result['LoopItem'] = self.loop_item
        if self.task_execution_ids is not None:
            result['TaskExecutionIds'] = self.task_execution_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('NotifyNote') is not None:
            self.notify_note = m.get('NotifyNote')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('LoopItem') is not None:
            self.loop_item = m.get('LoopItem')
        if m.get('TaskExecutionIds') is not None:
            self.task_execution_ids = m.get('TaskExecutionIds')
        return self


class NotifyExecutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NotifyExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: NotifyExecutionResponseBody = None,
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
            temp_model = NotifyExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchInventoryRequestFilter(TeaModel):
    def __init__(
        self,
        value: List[str] = None,
        operator: str = None,
        name: str = None,
    ):
        self.value = value
        self.operator = operator
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SearchInventoryRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        next_token: str = None,
        max_results: int = None,
        filter: List[SearchInventoryRequestFilter] = None,
        aggregator: List[str] = None,
    ):
        self.region_id = region_id
        self.next_token = next_token
        self.max_results = max_results
        self.filter = filter
        self.aggregator = aggregator

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = SearchInventoryRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')
        return self


class SearchInventoryResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        max_results: int = None,
        entities: List[Dict[str, Any]] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
        self.entities = entities

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.entities is not None:
            result['Entities'] = self.entities
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Entities') is not None:
            self.entities = m.get('Entities')
        return self


class SearchInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchInventoryResponseBody = None,
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
            temp_model = SearchInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetServiceSettingsRequest(TeaModel):
    def __init__(
        self,
        delivery_oss_enabled: bool = None,
        delivery_oss_bucket_name: str = None,
        delivery_oss_key_prefix: str = None,
        delivery_sls_project_name: str = None,
        delivery_sls_enabled: bool = None,
    ):
        self.delivery_oss_enabled = delivery_oss_enabled
        self.delivery_oss_bucket_name = delivery_oss_bucket_name
        self.delivery_oss_key_prefix = delivery_oss_key_prefix
        self.delivery_sls_project_name = delivery_sls_project_name
        self.delivery_sls_enabled = delivery_sls_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.delivery_oss_enabled is not None:
            result['DeliveryOssEnabled'] = self.delivery_oss_enabled
        if self.delivery_oss_bucket_name is not None:
            result['DeliveryOssBucketName'] = self.delivery_oss_bucket_name
        if self.delivery_oss_key_prefix is not None:
            result['DeliveryOssKeyPrefix'] = self.delivery_oss_key_prefix
        if self.delivery_sls_project_name is not None:
            result['DeliverySlsProjectName'] = self.delivery_sls_project_name
        if self.delivery_sls_enabled is not None:
            result['DeliverySlsEnabled'] = self.delivery_sls_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryOssEnabled') is not None:
            self.delivery_oss_enabled = m.get('DeliveryOssEnabled')
        if m.get('DeliveryOssBucketName') is not None:
            self.delivery_oss_bucket_name = m.get('DeliveryOssBucketName')
        if m.get('DeliveryOssKeyPrefix') is not None:
            self.delivery_oss_key_prefix = m.get('DeliveryOssKeyPrefix')
        if m.get('DeliverySlsProjectName') is not None:
            self.delivery_sls_project_name = m.get('DeliverySlsProjectName')
        if m.get('DeliverySlsEnabled') is not None:
            self.delivery_sls_enabled = m.get('DeliverySlsEnabled')
        return self


class SetServiceSettingsResponseBodyServiceSettings(TeaModel):
    def __init__(
        self,
        delivery_oss_bucket_name: str = None,
        delivery_oss_key_prefix: str = None,
        delivery_sls_enabled: bool = None,
        delivery_oss_enabled: bool = None,
        delivery_sls_project_name: str = None,
    ):
        self.delivery_oss_bucket_name = delivery_oss_bucket_name
        self.delivery_oss_key_prefix = delivery_oss_key_prefix
        self.delivery_sls_enabled = delivery_sls_enabled
        self.delivery_oss_enabled = delivery_oss_enabled
        self.delivery_sls_project_name = delivery_sls_project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.delivery_oss_bucket_name is not None:
            result['DeliveryOssBucketName'] = self.delivery_oss_bucket_name
        if self.delivery_oss_key_prefix is not None:
            result['DeliveryOssKeyPrefix'] = self.delivery_oss_key_prefix
        if self.delivery_sls_enabled is not None:
            result['DeliverySlsEnabled'] = self.delivery_sls_enabled
        if self.delivery_oss_enabled is not None:
            result['DeliveryOssEnabled'] = self.delivery_oss_enabled
        if self.delivery_sls_project_name is not None:
            result['DeliverySlsProjectName'] = self.delivery_sls_project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryOssBucketName') is not None:
            self.delivery_oss_bucket_name = m.get('DeliveryOssBucketName')
        if m.get('DeliveryOssKeyPrefix') is not None:
            self.delivery_oss_key_prefix = m.get('DeliveryOssKeyPrefix')
        if m.get('DeliverySlsEnabled') is not None:
            self.delivery_sls_enabled = m.get('DeliverySlsEnabled')
        if m.get('DeliveryOssEnabled') is not None:
            self.delivery_oss_enabled = m.get('DeliveryOssEnabled')
        if m.get('DeliverySlsProjectName') is not None:
            self.delivery_sls_project_name = m.get('DeliverySlsProjectName')
        return self


class SetServiceSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_settings: List[SetServiceSettingsResponseBodyServiceSettings] = None,
    ):
        self.request_id = request_id
        self.service_settings = service_settings

    def validate(self):
        if self.service_settings:
            for k in self.service_settings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceSettings'] = []
        if self.service_settings is not None:
            for k in self.service_settings:
                result['ServiceSettings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_settings = []
        if m.get('ServiceSettings') is not None:
            for k in m.get('ServiceSettings'):
                temp_model = SetServiceSettingsResponseBodyServiceSettings()
                self.service_settings.append(temp_model.from_map(k))
        return self


class SetServiceSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetServiceSettingsResponseBody = None,
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
            temp_model = SetServiceSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartExecutionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        template_version: str = None,
        mode: str = None,
        loop_mode: str = None,
        parent_execution_id: str = None,
        safety_check: str = None,
        parameters: str = None,
        client_token: str = None,
        tags: Dict[str, Any] = None,
        description: str = None,
        template_content: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.template_version = template_version
        self.mode = mode
        self.loop_mode = loop_mode
        self.parent_execution_id = parent_execution_id
        self.safety_check = safety_check
        self.parameters = parameters
        self.client_token = client_token
        self.tags = tags
        self.description = description
        self.template_content = template_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.loop_mode is not None:
            result['LoopMode'] = self.loop_mode
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.description is not None:
            result['Description'] = self.description
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('LoopMode') is not None:
            self.loop_mode = m.get('LoopMode')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        return self


class StartExecutionShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        template_version: str = None,
        mode: str = None,
        loop_mode: str = None,
        parent_execution_id: str = None,
        safety_check: str = None,
        parameters: str = None,
        client_token: str = None,
        tags_shrink: str = None,
        description: str = None,
        template_content: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.template_version = template_version
        self.mode = mode
        self.loop_mode = loop_mode
        self.parent_execution_id = parent_execution_id
        self.safety_check = safety_check
        self.parameters = parameters
        self.client_token = client_token
        self.tags_shrink = tags_shrink
        self.description = description
        self.template_content = template_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.loop_mode is not None:
            result['LoopMode'] = self.loop_mode
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('LoopMode') is not None:
            self.loop_mode = m.get('LoopMode')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        return self


class StartExecutionResponseBodyExecutionCurrentTasks(TeaModel):
    def __init__(
        self,
        task_execution_id: str = None,
        task_name: str = None,
        task_action: str = None,
    ):
        self.task_execution_id = task_execution_id
        self.task_name = task_name
        self.task_action = task_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        return self


class StartExecutionResponseBodyExecution(TeaModel):
    def __init__(
        self,
        status: str = None,
        outputs: str = None,
        executed_by: str = None,
        end_date: str = None,
        is_parent: bool = None,
        start_date: str = None,
        tags: Dict[str, Any] = None,
        mode: str = None,
        safety_check: str = None,
        template_name: str = None,
        template_version: str = None,
        create_date: str = None,
        execution_id: str = None,
        current_tasks: List[StartExecutionResponseBodyExecutionCurrentTasks] = None,
        parameters: str = None,
        description: str = None,
        counters: Dict[str, Any] = None,
        update_date: str = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        template_id: str = None,
        status_message: str = None,
        loop_mode: str = None,
    ):
        self.status = status
        self.outputs = outputs
        self.executed_by = executed_by
        self.end_date = end_date
        self.is_parent = is_parent
        self.start_date = start_date
        self.tags = tags
        self.mode = mode
        self.safety_check = safety_check
        self.template_name = template_name
        self.template_version = template_version
        self.create_date = create_date
        self.execution_id = execution_id
        self.current_tasks = current_tasks
        self.parameters = parameters
        self.description = description
        self.counters = counters
        self.update_date = update_date
        self.parent_execution_id = parent_execution_id
        self.ram_role = ram_role
        self.template_id = template_id
        self.status_message = status_message
        self.loop_mode = loop_mode

    def validate(self):
        if self.current_tasks:
            for k in self.current_tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.is_parent is not None:
            result['IsParent'] = self.is_parent
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        result['CurrentTasks'] = []
        if self.current_tasks is not None:
            for k in self.current_tasks:
                result['CurrentTasks'].append(k.to_map() if k else None)
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.description is not None:
            result['Description'] = self.description
        if self.counters is not None:
            result['Counters'] = self.counters
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.loop_mode is not None:
            result['LoopMode'] = self.loop_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('IsParent') is not None:
            self.is_parent = m.get('IsParent')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        self.current_tasks = []
        if m.get('CurrentTasks') is not None:
            for k in m.get('CurrentTasks'):
                temp_model = StartExecutionResponseBodyExecutionCurrentTasks()
                self.current_tasks.append(temp_model.from_map(k))
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Counters') is not None:
            self.counters = m.get('Counters')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('LoopMode') is not None:
            self.loop_mode = m.get('LoopMode')
        return self


class StartExecutionResponseBody(TeaModel):
    def __init__(
        self,
        execution: StartExecutionResponseBodyExecution = None,
        request_id: str = None,
    ):
        self.execution = execution
        self.request_id = request_id

    def validate(self):
        if self.execution:
            self.execution.validate()

    def to_map(self):
        result = dict()
        if self.execution is not None:
            result['Execution'] = self.execution.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Execution') is not None:
            temp_model = StartExecutionResponseBodyExecution()
            self.execution = temp_model.from_map(m['Execution'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartExecutionResponseBody = None,
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
            temp_model = StartExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids: Dict[str, Any] = None,
        resource_type: str = None,
        tags: Dict[str, Any] = None,
    ):
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tags_shrink: str = None,
    ):
        self.region_id = region_id
        self.resource_ids_shrink = resource_ids_shrink
        self.resource_type = resource_type
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class TriggerExecutionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        execution_id: str = None,
        type: str = None,
        content: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.execution_id = execution_id
        self.type = type
        self.content = content
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.type is not None:
            result['Type'] = self.type
        if self.content is not None:
            result['Content'] = self.content
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class TriggerExecutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TriggerExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TriggerExecutionResponseBody = None,
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
            temp_model = TriggerExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids: Dict[str, Any] = None,
        resource_type: str = None,
        tag_keys: Dict[str, Any] = None,
        all: bool = None,
    ):
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tag_keys = tag_keys
        self.all = all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class UntagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tag_keys_shrink: str = None,
        all: bool = None,
    ):
        self.region_id = region_id
        self.resource_ids_shrink = resource_ids_shrink
        self.resource_type = resource_type
        self.tag_keys_shrink = tag_keys_shrink
        self.all = all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class UpdateExecutionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        execution_id: str = None,
        parameters: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.execution_id = execution_id
        self.parameters = parameters
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateExecutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateExecutionResponseBody = None,
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
            temp_model = UpdateExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceInformationRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        agent_version: str = None,
        platform_type: str = None,
        platform_name: str = None,
        platform_version: str = None,
        ip_address: str = None,
        computer_name: str = None,
        agent_name: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.agent_version = agent_version
        self.platform_type = platform_type
        self.platform_name = platform_name
        self.platform_version = platform_version
        self.ip_address = ip_address
        self.computer_name = computer_name
        self.agent_name = agent_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name
        if self.platform_version is not None:
            result['PlatformVersion'] = self.platform_version
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.computer_name is not None:
            result['ComputerName'] = self.computer_name
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')
        if m.get('PlatformVersion') is not None:
            self.platform_version = m.get('PlatformVersion')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('ComputerName') is not None:
            self.computer_name = m.get('ComputerName')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        return self


class UpdateInstanceInformationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInstanceInformationResponseBody = None,
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
            temp_model = UpdateInstanceInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateParameterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
        value: str = None,
        description: str = None,
    ):
        self.region_id = region_id
        self.name = name
        self.value = value
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        type: str = None,
        constraints: str = None,
        description: str = None,
        updated_date: str = None,
        updated_by: str = None,
        created_by: str = None,
        parameter_version: int = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.constraints = constraints
        self.description = description
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.created_by = created_by
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class UpdateParameterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        parameter: UpdateParameterResponseBodyParameter = None,
    ):
        self.request_id = request_id
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Parameter') is not None:
            temp_model = UpdateParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class UpdateParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateParameterResponseBody = None,
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
            temp_model = UpdateParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretParameterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        name: str = None,
        value: str = None,
        description: str = None,
    ):
        self.region_id = region_id
        self.name = name
        self.value = value
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateSecretParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        type: str = None,
        updated_date: str = None,
        updated_by: str = None,
        key_id: str = None,
        constraints: str = None,
        description: str = None,
        created_by: str = None,
        parameter_version: int = None,
        created_date: str = None,
        name: str = None,
        id: str = None,
        share_type: str = None,
    ):
        self.type = type
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.key_id = key_id
        self.constraints = constraints
        self.description = description
        self.created_by = created_by
        self.parameter_version = parameter_version
        self.created_date = created_date
        self.name = name
        self.id = id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class UpdateSecretParameterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        parameter: UpdateSecretParameterResponseBodyParameter = None,
    ):
        self.request_id = request_id
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Parameter') is not None:
            temp_model = UpdateSecretParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        return self


class UpdateSecretParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSecretParameterResponseBody = None,
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
            temp_model = UpdateSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        content: str = None,
        tags: Dict[str, Any] = None,
        version_name: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.content = content
        self.tags = tags
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.content is not None:
            result['Content'] = self.content
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        content: str = None,
        tags_shrink: str = None,
        version_name: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.content = content
        self.tags_shrink = tags_shrink
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.content is not None:
            result['Content'] = self.content
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        hash: str = None,
        updated_date: str = None,
        updated_by: str = None,
        tags: Dict[str, Any] = None,
        template_name: str = None,
        template_version: str = None,
        template_format: str = None,
        description: str = None,
        created_by: str = None,
        created_date: str = None,
        has_trigger: bool = None,
        template_id: str = None,
        share_type: str = None,
    ):
        self.hash = hash
        self.updated_date = updated_date
        self.updated_by = updated_by
        self.tags = tags
        self.template_name = template_name
        self.template_version = template_version
        self.template_format = template_format
        self.description = description
        self.created_by = created_by
        self.created_date = created_date
        self.has_trigger = has_trigger
        self.template_id = template_id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.description is not None:
            result['Description'] = self.description
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template: UpdateTemplateResponseBodyTemplate = None,
    ):
        self.request_id = request_id
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = UpdateTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTemplateResponseBody = None,
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
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateTemplateContentRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        content: str = None,
    ):
        self.region_id = region_id
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ValidateTemplateContentResponseBodyTasks(TeaModel):
    def __init__(
        self,
        outputs: str = None,
        type: str = None,
        description: str = None,
        name: str = None,
        properties: str = None,
    ):
        self.outputs = outputs
        self.type = type
        self.description = description
        self.name = name
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.type is not None:
            result['Type'] = self.type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        return self


class ValidateTemplateContentResponseBody(TeaModel):
    def __init__(
        self,
        parameters: str = None,
        tasks: List[ValidateTemplateContentResponseBodyTasks] = None,
        request_id: str = None,
        outputs: str = None,
        ram_role: str = None,
    ):
        self.parameters = parameters
        self.tasks = tasks
        self.request_id = request_id
        self.outputs = outputs
        self.ram_role = ram_role

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ValidateTemplateContentResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        return self


class ValidateTemplateContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateTemplateContentResponseBody = None,
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
            temp_model = ValidateTemplateContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


