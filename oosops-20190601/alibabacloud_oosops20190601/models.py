# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AuditPublicTemplateRegistrationRequest(TeaModel):
    def __init__(
        self,
        audit_action: str = None,
        comment: str = None,
        region_id: str = None,
        registration_id: str = None,
    ):
        self.audit_action = audit_action
        self.comment = comment
        self.region_id = region_id
        self.registration_id = registration_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_action is not None:
            result['AuditAction'] = self.audit_action
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditAction') is not None:
            self.audit_action = m.get('AuditAction')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        return self


class AuditPublicTemplateRegistrationResponseBody(TeaModel):
    def __init__(
        self,
        comment: str = None,
        detail: str = None,
        registration_id: str = None,
        request_id: str = None,
        status: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        self.comment = comment
        self.detail = detail
        self.registration_id = registration_id
        self.request_id = request_id
        self.status = status
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class AuditPublicTemplateRegistrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuditPublicTemplateRegistrationResponseBody = None,
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
            temp_model = AuditPublicTemplateRegistrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateActionRequest(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        action_type: str = None,
        content: str = None,
        popularity: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.action_name = action_name
        # This parameter is required.
        self.action_type = action_type
        # This parameter is required.
        self.content = content
        self.popularity = popularity
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.content is not None:
            result['Content'] = self.content
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateActionResponseBody(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        action_type: str = None,
        created_date: str = None,
        description: str = None,
        popularity: int = None,
        properties: str = None,
        request_id: str = None,
        template_version: str = None,
    ):
        self.action_name = action_name
        self.action_type = action_type
        self.created_date = created_date
        self.description = description
        self.popularity = popularity
        self.properties = properties
        self.request_id = request_id
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class CreateActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateActionResponseBody = None,
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
            temp_model = CreateActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePublicParameterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        constraints: str = None,
        description: str = None,
        name: str = None,
        parameter_type: str = None,
        region_id: str = None,
        value: str = None,
    ):
        self.client_token = client_token
        self.constraints = constraints
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.parameter_type = parameter_type
        self.region_id = region_id
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePublicParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parameter_version: int = None,
        region_id: str = None,
        share_type: str = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.constraints = constraints
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.name = name
        self.parameter_version = parameter_version
        self.region_id = region_id
        self.share_type = share_type
        self.type = type
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class CreatePublicParameterResponseBody(TeaModel):
    def __init__(
        self,
        parameter: CreatePublicParameterResponseBodyParameter = None,
        request_id: str = None,
    ):
        self.parameter = parameter
        self.request_id = request_id

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = CreatePublicParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePublicParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePublicParameterResponseBody = None,
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
            temp_model = CreatePublicParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePublicPatchBaselineRequest(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        operation_system: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.approval_rules = approval_rules
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.operation_system = operation_system
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreatePublicPatchBaselineResponseBodyPatchBaseline(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        operation_system: str = None,
        share_type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.approval_rules = approval_rules
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.name = name
        self.operation_system = operation_system
        self.share_type = share_type
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class CreatePublicPatchBaselineResponseBody(TeaModel):
    def __init__(
        self,
        patch_baseline: CreatePublicPatchBaselineResponseBodyPatchBaseline = None,
        request_id: str = None,
    ):
        self.patch_baseline = patch_baseline
        self.request_id = request_id

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = CreatePublicPatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m['PatchBaseline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePublicPatchBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePublicPatchBaselineResponseBody = None,
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
            temp_model = CreatePublicPatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePublicTemplateRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        content: str = None,
        is_example: bool = None,
        popularity: int = None,
        publisher: str = None,
        region_id: str = None,
        template_name: str = None,
        version_name: str = None,
    ):
        self.category = category
        # This parameter is required.
        self.content = content
        self.is_example = is_example
        self.popularity = popularity
        self.publisher = publisher
        self.region_id = region_id
        # This parameter is required.
        self.template_name = template_name
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.is_example is not None:
            result['IsExample'] = self.is_example
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.publisher is not None:
            result['Publisher'] = self.publisher
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('IsExample') is not None:
            self.is_example = m.get('IsExample')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('Publisher') is not None:
            self.publisher = m.get('Publisher')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreatePublicTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        category: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        hash: str = None,
        popularity: int = None,
        share_type: str = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.category = category
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.hash = hash
        self.popularity = popularity
        self.share_type = share_type
        self.template_format = template_format
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class CreatePublicTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template: CreatePublicTemplateResponseBodyTemplate = None,
    ):
        self.request_id = request_id
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = CreatePublicTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class CreatePublicTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePublicTemplateResponseBody = None,
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
            temp_model = CreatePublicTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFailureMsgRequest(TeaModel):
    def __init__(
        self,
        operation: str = None,
        request_fingerprint: str = None,
    ):
        # This parameter is required.
        self.operation = operation
        # This parameter is required.
        self.request_fingerprint = request_fingerprint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.request_fingerprint is not None:
            result['RequestFingerprint'] = self.request_fingerprint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('RequestFingerprint') is not None:
            self.request_fingerprint = m.get('RequestFingerprint')
        return self


class DeleteFailureMsgResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFailureMsgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFailureMsgResponseBody = None,
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
            temp_model = DeleteFailureMsgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePublicParameterRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeletePublicParameterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePublicParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePublicParameterResponseBody = None,
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
            temp_model = DeletePublicParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePublicPatchBaselineRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeletePublicPatchBaselineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePublicPatchBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePublicPatchBaselineResponseBody = None,
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
            temp_model = DeletePublicPatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePublicTemplateRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
    ):
        self.region_id = region_id
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DeletePublicTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePublicTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePublicTemplateResponseBody = None,
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
            temp_model = DeletePublicTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoCheckResourceRequest(TeaModel):
    def __init__(
        self,
        bid: str = None,
        country: str = None,
        gmt_wakeup: str = None,
        hid: int = None,
        interrupt: bool = None,
        invoker: str = None,
        level: int = None,
        message: str = None,
        pk: str = None,
        prompt: str = None,
        success: bool = None,
        task_extra_data: str = None,
        task_identifier: str = None,
        url: str = None,
    ):
        self.bid = bid
        self.country = country
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.interrupt = interrupt
        self.invoker = invoker
        self.level = level
        self.message = message
        self.pk = pk
        self.prompt = prompt
        self.success = success
        self.task_extra_data = task_extra_data
        self.task_identifier = task_identifier
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['bid'] = self.bid
        if self.country is not None:
            result['country'] = self.country
        if self.gmt_wakeup is not None:
            result['gmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['hid'] = self.hid
        if self.interrupt is not None:
            result['interrupt'] = self.interrupt
        if self.invoker is not None:
            result['invoker'] = self.invoker
        if self.level is not None:
            result['level'] = self.level
        if self.message is not None:
            result['message'] = self.message
        if self.pk is not None:
            result['pk'] = self.pk
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.success is not None:
            result['success'] = self.success
        if self.task_extra_data is not None:
            result['taskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['taskIdentifier'] = self.task_identifier
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bid') is not None:
            self.bid = m.get('bid')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('gmtWakeup') is not None:
            self.gmt_wakeup = m.get('gmtWakeup')
        if m.get('hid') is not None:
            self.hid = m.get('hid')
        if m.get('interrupt') is not None:
            self.interrupt = m.get('interrupt')
        if m.get('invoker') is not None:
            self.invoker = m.get('invoker')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('pk') is not None:
            self.pk = m.get('pk')
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('taskExtraData') is not None:
            self.task_extra_data = m.get('taskExtraData')
        if m.get('taskIdentifier') is not None:
            self.task_identifier = m.get('taskIdentifier')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class DoCheckResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bid: str = None,
        country: str = None,
        gmt_wakeup: str = None,
        hid: int = None,
        interrupt: bool = None,
        invoker: str = None,
        level: int = None,
        message: str = None,
        pk: str = None,
        prompt: str = None,
        success: bool = None,
        task_extra_data: str = None,
        task_identifier: str = None,
        url: str = None,
    ):
        self.request_id = request_id
        self.bid = bid
        self.country = country
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.interrupt = interrupt
        self.invoker = invoker
        self.level = level
        self.message = message
        self.pk = pk
        self.prompt = prompt
        self.success = success
        self.task_extra_data = task_extra_data
        self.task_identifier = task_identifier
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bid is not None:
            result['bid'] = self.bid
        if self.country is not None:
            result['country'] = self.country
        if self.gmt_wakeup is not None:
            result['gmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['hid'] = self.hid
        if self.interrupt is not None:
            result['interrupt'] = self.interrupt
        if self.invoker is not None:
            result['invoker'] = self.invoker
        if self.level is not None:
            result['level'] = self.level
        if self.message is not None:
            result['message'] = self.message
        if self.pk is not None:
            result['pk'] = self.pk
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.success is not None:
            result['success'] = self.success
        if self.task_extra_data is not None:
            result['taskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['taskIdentifier'] = self.task_identifier
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('bid') is not None:
            self.bid = m.get('bid')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('gmtWakeup') is not None:
            self.gmt_wakeup = m.get('gmtWakeup')
        if m.get('hid') is not None:
            self.hid = m.get('hid')
        if m.get('interrupt') is not None:
            self.interrupt = m.get('interrupt')
        if m.get('invoker') is not None:
            self.invoker = m.get('invoker')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('pk') is not None:
            self.pk = m.get('pk')
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('taskExtraData') is not None:
            self.task_extra_data = m.get('taskExtraData')
        if m.get('taskIdentifier') is not None:
            self.task_identifier = m.get('taskIdentifier')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class DoCheckResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DoCheckResourceResponseBody = None,
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
            temp_model = DoCheckResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetActionRequest(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        region_id: str = None,
    ):
        self.action_name = action_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetActionResponseBody(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        action_type: str = None,
        content: bytes = None,
        create_time: str = None,
        modified_time: str = None,
        popularity: str = None,
        request_id: str = None,
    ):
        self.action_name = action_name
        self.action_type = action_type
        self.content = content
        self.create_time = create_time
        self.modified_time = modified_time
        self.popularity = popularity
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetActionResponseBody = None,
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
            temp_model = GetActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowControlRequest(TeaModel):
    def __init__(
        self,
        api: str = None,
        service: str = None,
        type: int = None,
        uid: str = None,
    ):
        self.api = api
        self.service = service
        # This parameter is required.
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['Api'] = self.api
        if self.service is not None:
            result['Service'] = self.service
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetFlowControlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        value: int = None,
    ):
        self.request_id = request_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetFlowControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFlowControlResponseBody = None,
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
            temp_model = GetFlowControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicParameterRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameter_version: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.name = name
        self.parameter_version = parameter_version
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPublicParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parameter_version: int = None,
        region_id: str = None,
        share_type: str = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
        value: str = None,
    ):
        self.constraints = constraints
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.name = name
        self.parameter_version = parameter_version
        self.region_id = region_id
        self.share_type = share_type
        self.type = type
        self.updated_by = updated_by
        self.updated_date = updated_date
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetPublicParameterResponseBody(TeaModel):
    def __init__(
        self,
        parameter: GetPublicParameterResponseBodyParameter = None,
        request_id: str = None,
    ):
        self.parameter = parameter
        self.request_id = request_id

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = GetPublicParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPublicParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPublicParameterResponseBody = None,
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
            temp_model = GetPublicParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicPatchBaselineRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPublicPatchBaselineResponseBodyPatchBaseline(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        operation_system: str = None,
        share_type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.approval_rules = approval_rules
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.name = name
        self.operation_system = operation_system
        self.share_type = share_type
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class GetPublicPatchBaselineResponseBody(TeaModel):
    def __init__(
        self,
        patch_baseline: GetPublicPatchBaselineResponseBodyPatchBaseline = None,
        request_id: str = None,
    ):
        self.patch_baseline = patch_baseline
        self.request_id = request_id

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = GetPublicPatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m['PatchBaseline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPublicPatchBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPublicPatchBaselineResponseBody = None,
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
            temp_model = GetPublicPatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPublicTemplateRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        self.region_id = region_id
        # This parameter is required.
        self.template_name = template_name
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetPublicTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        hash: str = None,
        popularity: int = None,
        share_type: str = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.hash = hash
        self.popularity = popularity
        self.share_type = share_type
        self.template_format = template_format
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class GetPublicTemplateResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
        template: GetPublicTemplateResponseBodyTemplate = None,
    ):
        self.content = content
        self.request_id = request_id
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = GetPublicTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetPublicTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPublicTemplateResponseBody = None,
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
            temp_model = GetPublicTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaRequest(TeaModel):
    def __init__(
        self,
        quota_name: str = None,
        region_id: str = None,
        uid: str = None,
    ):
        # This parameter is required.
        self.quota_name = quota_name
        self.region_id = region_id
        # This parameter is required.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetQuotaResponseBodyQuota(TeaModel):
    def __init__(
        self,
        concurrent_execution: int = None,
        daily_tasks: int = None,
        total_template: int = None,
    ):
        self.concurrent_execution = concurrent_execution
        self.daily_tasks = daily_tasks
        self.total_template = total_template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrent_execution is not None:
            result['ConcurrentExecution'] = self.concurrent_execution
        if self.daily_tasks is not None:
            result['DailyTasks'] = self.daily_tasks
        if self.total_template is not None:
            result['TotalTemplate'] = self.total_template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrentExecution') is not None:
            self.concurrent_execution = m.get('ConcurrentExecution')
        if m.get('DailyTasks') is not None:
            self.daily_tasks = m.get('DailyTasks')
        if m.get('TotalTemplate') is not None:
            self.total_template = m.get('TotalTemplate')
        return self


class GetQuotaResponseBody(TeaModel):
    def __init__(
        self,
        quota: GetQuotaResponseBodyQuota = None,
        request_id: str = None,
        uid: str = None,
    ):
        self.quota = quota
        self.request_id = request_id
        self.uid = uid

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            temp_model = GetQuotaResponseBodyQuota()
            self.quota = temp_model.from_map(m['Quota'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaResponseBody = None,
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
            temp_model = GetQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserExecutionTemplateRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        execution_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        # This parameter is required.
        self.execution_id = execution_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetUserExecutionTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        hash: str = None,
        share_type: str = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.hash = hash
        self.share_type = share_type
        self.template_format = template_format
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class GetUserExecutionTemplateResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
        template: GetUserExecutionTemplateResponseBodyTemplate = None,
    ):
        self.content = content
        self.request_id = request_id
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = GetUserExecutionTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetUserExecutionTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserExecutionTemplateResponseBody = None,
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
            temp_model = GetUserExecutionTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserTemplateRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        region_id: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        self.region_id = region_id
        # This parameter is required.
        self.template_name = template_name
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetUserTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        hash: str = None,
        share_type: str = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.hash = hash
        self.share_type = share_type
        self.template_format = template_format
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class GetUserTemplateResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
        template: GetUserTemplateResponseBodyTemplate = None,
    ):
        self.content = content
        self.request_id = request_id
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = GetUserTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetUserTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserTemplateResponseBody = None,
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
            temp_model = GetUserTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListActionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        oosaction_name: str = None,
        region_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.oosaction_name = oosaction_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.oosaction_name is not None:
            result['OOSActionName'] = self.oosaction_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OOSActionName') is not None:
            self.oosaction_name = m.get('OOSActionName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListActionsResponseBodyActions(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        created_date: str = None,
        description: str = None,
        oosaction_name: str = None,
        popularity: int = None,
        properties: str = None,
        template_version: str = None,
        update_date: str = None,
    ):
        self.action_type = action_type
        self.created_date = created_date
        self.description = description
        self.oosaction_name = oosaction_name
        self.popularity = popularity
        self.properties = properties
        self.template_version = template_version
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.oosaction_name is not None:
            result['OOSActionName'] = self.oosaction_name
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OOSActionName') is not None:
            self.oosaction_name = m.get('OOSActionName')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListActionsResponseBody(TeaModel):
    def __init__(
        self,
        actions: List[ListActionsResponseBodyActions] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.actions = actions
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = ListActionsResponseBodyActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListActionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListActionsResponseBody = None,
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
            temp_model = ListActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDefaultQuotaResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        concurrent_execution: int = None,
        daily_tasks: int = None,
        total_template: int = None,
    ):
        self.concurrent_execution = concurrent_execution
        self.daily_tasks = daily_tasks
        self.total_template = total_template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrent_execution is not None:
            result['ConcurrentExecution'] = self.concurrent_execution
        if self.daily_tasks is not None:
            result['DailyTasks'] = self.daily_tasks
        if self.total_template is not None:
            result['TotalTemplate'] = self.total_template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrentExecution') is not None:
            self.concurrent_execution = m.get('ConcurrentExecution')
        if m.get('DailyTasks') is not None:
            self.daily_tasks = m.get('DailyTasks')
        if m.get('TotalTemplate') is not None:
            self.total_template = m.get('TotalTemplate')
        return self


class ListDefaultQuotaResponseBody(TeaModel):
    def __init__(
        self,
        quotas: List[ListDefaultQuotaResponseBodyQuotas] = None,
        request_id: str = None,
    ):
        self.quotas = quotas
        self.request_id = request_id

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListDefaultQuotaResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDefaultQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDefaultQuotaResponseBody = None,
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
            temp_model = ListDefaultQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFailureMsgsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_fingerprint: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_fingerprint = request_fingerprint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_fingerprint is not None:
            result['RequestFingerprint'] = self.request_fingerprint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestFingerprint') is not None:
            self.request_fingerprint = m.get('RequestFingerprint')
        return self


class ListFailureMsgsResponseBodyFailureMsgs(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        execution_id: str = None,
        message_body: str = None,
        reason: str = None,
        task_execution_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.execution_id = execution_id
        self.message_body = message_body
        self.reason = reason
        self.task_execution_id = task_execution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.message_body is not None:
            result['MessageBody'] = self.message_body
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('MessageBody') is not None:
            self.message_body = m.get('MessageBody')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        return self


class ListFailureMsgsResponseBody(TeaModel):
    def __init__(
        self,
        failure_msgs: List[ListFailureMsgsResponseBodyFailureMsgs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.failure_msgs = failure_msgs
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.failure_msgs:
            for k in self.failure_msgs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailureMsgs'] = []
        if self.failure_msgs is not None:
            for k in self.failure_msgs:
                result['FailureMsgs'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failure_msgs = []
        if m.get('FailureMsgs') is not None:
            for k in m.get('FailureMsgs'):
                temp_model = ListFailureMsgsResponseBodyFailureMsgs()
                self.failure_msgs.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFailureMsgsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFailureMsgsResponseBody = None,
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
            temp_model = ListFailureMsgsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOOSLogsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        execution_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        request_fingerprint: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        self.execution_id = execution_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.request_fingerprint = request_fingerprint
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_fingerprint is not None:
            result['RequestFingerprint'] = self.request_fingerprint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestFingerprint') is not None:
            self.request_fingerprint = m.get('RequestFingerprint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListOOSLogsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        ooslogs: str = None,
        request_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.ooslogs = ooslogs
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.ooslogs is not None:
            result['OOSLogs'] = self.ooslogs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OOSLogs') is not None:
            self.ooslogs = m.get('OOSLogs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListOOSLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOOSLogsResponseBody = None,
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
            temp_model = ListOOSLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicParametersRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        parameter_type: str = None,
        path: str = None,
        recursive: bool = None,
        region_id: str = None,
        sort_field: str = None,
        sort_order: str = None,
    ):
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.parameter_type = parameter_type
        self.path = path
        self.recursive = recursive
        self.region_id = region_id
        self.sort_field = sort_field
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListPublicParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parameter_version: str = None,
        region_id: str = None,
        share_type: str = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.name = name
        self.parameter_version = parameter_version
        self.region_id = region_id
        self.share_type = share_type
        self.type = type
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListPublicParametersResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        parameters: List[ListPublicParametersResponseBodyParameters] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.parameters = parameters
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ListPublicParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPublicParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPublicParametersResponseBody = None,
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
            temp_model = ListPublicParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicPatchBaselinesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        operation_system: str = None,
        region_id: str = None,
        share_type: str = None,
    ):
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.operation_system = operation_system
        self.region_id = region_id
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class ListPublicPatchBaselinesResponseBodyPatchBaselines(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        is_default: bool = None,
        name: str = None,
        operation_system: str = None,
        share_type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.is_default = is_default
        self.name = name
        self.operation_system = operation_system
        self.share_type = share_type
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListPublicPatchBaselinesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        patch_baselines: List[ListPublicPatchBaselinesResponseBodyPatchBaselines] = None,
        request_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.patch_baselines = patch_baselines
        self.request_id = request_id

    def validate(self):
        if self.patch_baselines:
            for k in self.patch_baselines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PatchBaselines'] = []
        if self.patch_baselines is not None:
            for k in self.patch_baselines:
                result['PatchBaselines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.patch_baselines = []
        if m.get('PatchBaselines') is not None:
            for k in m.get('PatchBaselines'):
                temp_model = ListPublicPatchBaselinesResponseBodyPatchBaselines()
                self.patch_baselines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPublicPatchBaselinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPublicPatchBaselinesResponseBody = None,
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
            temp_model = ListPublicPatchBaselinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicTemplateRegistrationsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        registration_id: str = None,
        status: str = None,
        template_name: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.registration_id = registration_id
        self.status = status
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListPublicTemplateRegistrationsResponseBodyRegistrations(TeaModel):
    def __init__(
        self,
        comment: str = None,
        created_date: str = None,
        detail: str = None,
        registration_id: str = None,
        show_pages: str = None,
        status: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        updated_date: str = None,
    ):
        self.comment = comment
        self.created_date = created_date
        self.detail = detail
        self.registration_id = registration_id
        self.show_pages = show_pages
        self.status = status
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.show_pages is not None:
            result['ShowPages'] = self.show_pages
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('ShowPages') is not None:
            self.show_pages = m.get('ShowPages')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListPublicTemplateRegistrationsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        registrations: List[ListPublicTemplateRegistrationsResponseBodyRegistrations] = None,
        request_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.registrations = registrations
        self.request_id = request_id

    def validate(self):
        if self.registrations:
            for k in self.registrations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Registrations'] = []
        if self.registrations is not None:
            for k in self.registrations:
                result['Registrations'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.registrations = []
        if m.get('Registrations') is not None:
            for k in m.get('Registrations'):
                temp_model = ListPublicTemplateRegistrationsResponseBodyRegistrations()
                self.registrations.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPublicTemplateRegistrationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPublicTemplateRegistrationsResponseBody = None,
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
            temp_model = ListPublicTemplateRegistrationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublicTemplatesRequest(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date_after: str = None,
        created_date_before: str = None,
        is_example: bool = None,
        max_results: int = None,
        next_token: str = None,
        popularity: int = None,
        region_id: str = None,
        share_type: str = None,
        sort_field: str = None,
        sort_order: str = None,
        template_format: str = None,
        template_name: str = None,
    ):
        self.created_by = created_by
        self.created_date_after = created_date_after
        self.created_date_before = created_date_before
        self.is_example = is_example
        self.max_results = max_results
        self.next_token = next_token
        self.popularity = popularity
        self.region_id = region_id
        self.share_type = share_type
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.template_format = template_format
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date_after is not None:
            result['CreatedDateAfter'] = self.created_date_after
        if self.created_date_before is not None:
            result['CreatedDateBefore'] = self.created_date_before
        if self.is_example is not None:
            result['IsExample'] = self.is_example
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDateAfter') is not None:
            self.created_date_after = m.get('CreatedDateAfter')
        if m.get('CreatedDateBefore') is not None:
            self.created_date_before = m.get('CreatedDateBefore')
        if m.get('IsExample') is not None:
            self.is_example = m.get('IsExample')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListPublicTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        hash: str = None,
        popularity: int = None,
        share_type: str = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        total_execution_count: int = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.hash = hash
        self.popularity = popularity
        self.share_type = share_type
        self.template_format = template_format
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.total_execution_count = total_execution_count
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.total_execution_count is not None:
            result['TotalExecutionCount'] = self.total_execution_count
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TotalExecutionCount') is not None:
            self.total_execution_count = m.get('TotalExecutionCount')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListPublicTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        templates: List[ListPublicTemplatesResponseBodyTemplates] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.templates = templates

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListPublicTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListPublicTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPublicTemplatesResponseBody = None,
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
            temp_model = ListPublicTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserExecutionLogsRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        execution_id: str = None,
        log_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        task_execution_id: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        # This parameter is required.
        self.execution_id = execution_id
        self.log_type = log_type
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.task_execution_id = task_execution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        return self


class ListUserExecutionLogsResponseBodyExecutionLogs(TeaModel):
    def __init__(
        self,
        log_type: str = None,
        message: str = None,
        task_execution_id: str = None,
        timestamp: str = None,
    ):
        self.log_type = log_type
        self.message = message
        self.task_execution_id = task_execution_id
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.message is not None:
            result['Message'] = self.message
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ListUserExecutionLogsResponseBody(TeaModel):
    def __init__(
        self,
        execution_logs: List[ListUserExecutionLogsResponseBodyExecutionLogs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.execution_logs = execution_logs
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.execution_logs:
            for k in self.execution_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExecutionLogs'] = []
        if self.execution_logs is not None:
            for k in self.execution_logs:
                result['ExecutionLogs'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.execution_logs = []
        if m.get('ExecutionLogs') is not None:
            for k in m.get('ExecutionLogs'):
                temp_model = ListUserExecutionLogsResponseBodyExecutionLogs()
                self.execution_logs.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserExecutionLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserExecutionLogsResponseBody = None,
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
            temp_model = ListUserExecutionLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserExecutionsRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        end_date_after: str = None,
        end_date_before: str = None,
        executed_by: str = None,
        execution_id: str = None,
        include_child_execution: bool = None,
        max_results: int = None,
        mode: str = None,
        next_token: str = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        region_id: str = None,
        sort_field: str = None,
        sort_order: str = None,
        start_date_after: str = None,
        start_date_before: str = None,
        status: str = None,
        template_name: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        self.end_date_after = end_date_after
        self.end_date_before = end_date_before
        self.executed_by = executed_by
        self.execution_id = execution_id
        self.include_child_execution = include_child_execution
        self.max_results = max_results
        self.mode = mode
        self.next_token = next_token
        self.parent_execution_id = parent_execution_id
        self.ram_role = ram_role
        self.region_id = region_id
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.start_date_after = start_date_after
        self.start_date_before = start_date_before
        self.status = status
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after
        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.include_child_execution is not None:
            result['IncludeChildExecution'] = self.include_child_execution
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after
        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before
        if self.status is not None:
            result['Status'] = self.status
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')
        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IncludeChildExecution') is not None:
            self.include_child_execution = m.get('IncludeChildExecution')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')
        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListUserExecutionsResponseBodyExecutionsCurrentTasks(TeaModel):
    def __init__(
        self,
        task_action: str = None,
        task_execution_id: str = None,
        task_name: str = None,
    ):
        self.task_action = task_action
        self.task_execution_id = task_execution_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListUserExecutionsResponseBodyExecutions(TeaModel):
    def __init__(
        self,
        counters: str = None,
        create_date: str = None,
        current_tasks: List[ListUserExecutionsResponseBodyExecutionsCurrentTasks] = None,
        end_date: str = None,
        executed_by: str = None,
        execution_id: str = None,
        is_parent: bool = None,
        mode: str = None,
        outputs: str = None,
        parameters: str = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        safety_check: str = None,
        start_date: str = None,
        status: str = None,
        status_message: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        update_date: str = None,
        waiting_status: str = None,
    ):
        self.counters = counters
        self.create_date = create_date
        self.current_tasks = current_tasks
        self.end_date = end_date
        self.executed_by = executed_by
        self.execution_id = execution_id
        self.is_parent = is_parent
        self.mode = mode
        self.outputs = outputs
        self.parameters = parameters
        self.parent_execution_id = parent_execution_id
        self.ram_role = ram_role
        self.safety_check = safety_check
        self.start_date = start_date
        self.status = status
        self.status_message = status_message
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.update_date = update_date
        self.waiting_status = waiting_status

    def validate(self):
        if self.current_tasks:
            for k in self.current_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.counters is not None:
            result['Counters'] = self.counters
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        result['CurrentTasks'] = []
        if self.current_tasks is not None:
            for k in self.current_tasks:
                result['CurrentTasks'].append(k.to_map() if k else None)
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.is_parent is not None:
            result['IsParent'] = self.is_parent
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.waiting_status is not None:
            result['WaitingStatus'] = self.waiting_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Counters') is not None:
            self.counters = m.get('Counters')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        self.current_tasks = []
        if m.get('CurrentTasks') is not None:
            for k in m.get('CurrentTasks'):
                temp_model = ListUserExecutionsResponseBodyExecutionsCurrentTasks()
                self.current_tasks.append(temp_model.from_map(k))
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IsParent') is not None:
            self.is_parent = m.get('IsParent')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('WaitingStatus') is not None:
            self.waiting_status = m.get('WaitingStatus')
        return self


class ListUserExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        executions: List[ListUserExecutionsResponseBodyExecutions] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.executions = executions
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.executions:
            for k in self.executions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Executions'] = []
        if self.executions is not None:
            for k in self.executions:
                result['Executions'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.executions = []
        if m.get('Executions') is not None:
            for k in m.get('Executions'):
                temp_model = ListUserExecutionsResponseBodyExecutions()
                self.executions.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserExecutionsResponseBody = None,
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
            temp_model = ListUserExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserInstancePatchStatesRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        instance_ids: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        # This parameter is required.
        self.instance_ids = instance_ids
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListUserInstancePatchStatesResponseBodyInstancePatchStates(TeaModel):
    def __init__(
        self,
        baseline_id: str = None,
        failed_count: str = None,
        installed_count: str = None,
        installed_other_count: str = None,
        installed_pending_reboot_count: str = None,
        installed_rejected_count: str = None,
        instance_id: str = None,
        missing_count: str = None,
        operation_end_time: str = None,
        operation_start_time: str = None,
        operation_type: str = None,
        owner_information: str = None,
        patch_group: str = None,
    ):
        self.baseline_id = baseline_id
        self.failed_count = failed_count
        self.installed_count = installed_count
        self.installed_other_count = installed_other_count
        self.installed_pending_reboot_count = installed_pending_reboot_count
        self.installed_rejected_count = installed_rejected_count
        self.instance_id = instance_id
        self.missing_count = missing_count
        self.operation_end_time = operation_end_time
        self.operation_start_time = operation_start_time
        self.operation_type = operation_type
        self.owner_information = owner_information
        self.patch_group = patch_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.installed_count is not None:
            result['InstalledCount'] = self.installed_count
        if self.installed_other_count is not None:
            result['InstalledOtherCount'] = self.installed_other_count
        if self.installed_pending_reboot_count is not None:
            result['InstalledPendingRebootCount'] = self.installed_pending_reboot_count
        if self.installed_rejected_count is not None:
            result['InstalledRejectedCount'] = self.installed_rejected_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.missing_count is not None:
            result['MissingCount'] = self.missing_count
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.owner_information is not None:
            result['OwnerInformation'] = self.owner_information
        if self.patch_group is not None:
            result['PatchGroup'] = self.patch_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('InstalledCount') is not None:
            self.installed_count = m.get('InstalledCount')
        if m.get('InstalledOtherCount') is not None:
            self.installed_other_count = m.get('InstalledOtherCount')
        if m.get('InstalledPendingRebootCount') is not None:
            self.installed_pending_reboot_count = m.get('InstalledPendingRebootCount')
        if m.get('InstalledRejectedCount') is not None:
            self.installed_rejected_count = m.get('InstalledRejectedCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MissingCount') is not None:
            self.missing_count = m.get('MissingCount')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OwnerInformation') is not None:
            self.owner_information = m.get('OwnerInformation')
        if m.get('PatchGroup') is not None:
            self.patch_group = m.get('PatchGroup')
        return self


class ListUserInstancePatchStatesResponseBody(TeaModel):
    def __init__(
        self,
        instance_patch_states: List[ListUserInstancePatchStatesResponseBodyInstancePatchStates] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.instance_patch_states = instance_patch_states
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.instance_patch_states:
            for k in self.instance_patch_states:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstancePatchStates'] = []
        if self.instance_patch_states is not None:
            for k in self.instance_patch_states:
                result['InstancePatchStates'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_patch_states = []
        if m.get('InstancePatchStates') is not None:
            for k in m.get('InstancePatchStates'):
                temp_model = ListUserInstancePatchStatesResponseBodyInstancePatchStates()
                self.instance_patch_states.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserInstancePatchStatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserInstancePatchStatesResponseBody = None,
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
            temp_model = ListUserInstancePatchStatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserInstancePatchesRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        # This parameter is required.
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListUserInstancePatchesResponseBodyPatches(TeaModel):
    def __init__(
        self,
        classification: str = None,
        installed_time: str = None,
        kbid: str = None,
        severity: str = None,
        status: str = None,
        title: str = None,
    ):
        self.classification = classification
        self.installed_time = installed_time
        self.kbid = kbid
        self.severity = severity
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.installed_time is not None:
            result['InstalledTime'] = self.installed_time
        if self.kbid is not None:
            result['KBId'] = self.kbid
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('InstalledTime') is not None:
            self.installed_time = m.get('InstalledTime')
        if m.get('KBId') is not None:
            self.kbid = m.get('KBId')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListUserInstancePatchesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        patches: List[ListUserInstancePatchesResponseBodyPatches] = None,
        request_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.patches = patches
        self.request_id = request_id

    def validate(self):
        if self.patches:
            for k in self.patches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Patches'] = []
        if self.patches is not None:
            for k in self.patches:
                result['Patches'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.patches = []
        if m.get('Patches') is not None:
            for k in m.get('Patches'):
                temp_model = ListUserInstancePatchesResponseBodyPatches()
                self.patches.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserInstancePatchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserInstancePatchesResponseBody = None,
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
            temp_model = ListUserInstancePatchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserInventoryEntriesRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        self.name = name
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListUserInventoryEntriesRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        filter: List[ListUserInventoryEntriesRequestFilter] = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        type_name: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        self.filter = filter
        # This parameter is required.
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        # This parameter is required.
        self.type_name = type_name

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListUserInventoryEntriesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class ListUserInventoryEntriesResponseBody(TeaModel):
    def __init__(
        self,
        capture_time: str = None,
        entries: List[Dict[str, Any]] = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        schema_version: str = None,
        type_name: str = None,
    ):
        self.capture_time = capture_time
        self.entries = entries
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.schema_version = schema_version
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.entries is not None:
            result['Entries'] = self.entries
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('Entries') is not None:
            self.entries = m.get('Entries')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class ListUserInventoryEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserInventoryEntriesResponseBody = None,
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
            temp_model = ListUserInventoryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserTaskExecutionsRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        end_date_after: str = None,
        end_date_before: str = None,
        execution_id: str = None,
        include_child_task_execution: bool = None,
        max_results: int = None,
        next_token: str = None,
        parent_task_execution_id: str = None,
        region_id: str = None,
        sort_field: str = None,
        sort_order: str = None,
        start_date_after: str = None,
        start_date_before: str = None,
        status: str = None,
        task_action: str = None,
        task_execution_id: str = None,
        task_name: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        self.end_date_after = end_date_after
        self.end_date_before = end_date_before
        self.execution_id = execution_id
        self.include_child_task_execution = include_child_task_execution
        self.max_results = max_results
        self.next_token = next_token
        self.parent_task_execution_id = parent_task_execution_id
        self.region_id = region_id
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.start_date_after = start_date_after
        self.start_date_before = start_date_before
        self.status = status
        self.task_action = task_action
        self.task_execution_id = task_execution_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after
        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.include_child_task_execution is not None:
            result['IncludeChildTaskExecution'] = self.include_child_task_execution
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.parent_task_execution_id is not None:
            result['ParentTaskExecutionId'] = self.parent_task_execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after
        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before
        if self.status is not None:
            result['Status'] = self.status
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')
        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IncludeChildTaskExecution') is not None:
            self.include_child_task_execution = m.get('IncludeChildTaskExecution')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ParentTaskExecutionId') is not None:
            self.parent_task_execution_id = m.get('ParentTaskExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')
        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListUserTaskExecutionsResponseBodyTaskExecutions(TeaModel):
    def __init__(
        self,
        child_execution_id: str = None,
        create_date: str = None,
        end_date: str = None,
        execution_id: str = None,
        extra_data: str = None,
        loop: str = None,
        loop_batch_number: int = None,
        loop_item: str = None,
        outputs: str = None,
        parent_task_execution_id: str = None,
        properties: str = None,
        start_date: str = None,
        status: str = None,
        status_message: str = None,
        task_action: str = None,
        task_execution_id: str = None,
        task_name: str = None,
        template_id: str = None,
        update_date: str = None,
    ):
        self.child_execution_id = child_execution_id
        self.create_date = create_date
        self.end_date = end_date
        self.execution_id = execution_id
        self.extra_data = extra_data
        self.loop = loop
        self.loop_batch_number = loop_batch_number
        self.loop_item = loop_item
        self.outputs = outputs
        self.parent_task_execution_id = parent_task_execution_id
        self.properties = properties
        self.start_date = start_date
        self.status = status
        self.status_message = status_message
        self.task_action = task_action
        self.task_execution_id = task_execution_id
        self.task_name = task_name
        self.template_id = template_id
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_execution_id is not None:
            result['ChildExecutionId'] = self.child_execution_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.loop is not None:
            result['Loop'] = self.loop
        if self.loop_batch_number is not None:
            result['LoopBatchNumber'] = self.loop_batch_number
        if self.loop_item is not None:
            result['LoopItem'] = self.loop_item
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parent_task_execution_id is not None:
            result['ParentTaskExecutionId'] = self.parent_task_execution_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildExecutionId') is not None:
            self.child_execution_id = m.get('ChildExecutionId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('Loop') is not None:
            self.loop = m.get('Loop')
        if m.get('LoopBatchNumber') is not None:
            self.loop_batch_number = m.get('LoopBatchNumber')
        if m.get('LoopItem') is not None:
            self.loop_item = m.get('LoopItem')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('ParentTaskExecutionId') is not None:
            self.parent_task_execution_id = m.get('ParentTaskExecutionId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListUserTaskExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        task_executions: List[ListUserTaskExecutionsResponseBodyTaskExecutions] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.task_executions = task_executions

    def validate(self):
        if self.task_executions:
            for k in self.task_executions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskExecutions'] = []
        if self.task_executions is not None:
            for k in self.task_executions:
                result['TaskExecutions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_executions = []
        if m.get('TaskExecutions') is not None:
            for k in m.get('TaskExecutions'):
                temp_model = ListUserTaskExecutionsResponseBodyTaskExecutions()
                self.task_executions.append(temp_model.from_map(k))
        return self


class ListUserTaskExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserTaskExecutionsResponseBody = None,
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
            temp_model = ListUserTaskExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserTemplatesRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        category: str = None,
        created_by: str = None,
        created_date_after: str = None,
        created_date_before: str = None,
        max_results: int = None,
        next_token: str = None,
        popularity: int = None,
        region_id: str = None,
        share_type: str = None,
        sort_field: str = None,
        sort_order: str = None,
        template_format: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        self.category = category
        self.created_by = created_by
        self.created_date_after = created_date_after
        self.created_date_before = created_date_before
        self.max_results = max_results
        self.next_token = next_token
        self.popularity = popularity
        self.region_id = region_id
        self.share_type = share_type
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.template_format = template_format
        self.template_name = template_name
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.category is not None:
            result['Category'] = self.category
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date_after is not None:
            result['CreatedDateAfter'] = self.created_date_after
        if self.created_date_before is not None:
            result['CreatedDateBefore'] = self.created_date_before
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDateAfter') is not None:
            self.created_date_after = m.get('CreatedDateAfter')
        if m.get('CreatedDateBefore') is not None:
            self.created_date_before = m.get('CreatedDateBefore')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListUserTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        hash: str = None,
        popularity: int = None,
        share_type: str = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        total_execution_count: int = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.hash = hash
        self.popularity = popularity
        self.share_type = share_type
        self.template_format = template_format
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.total_execution_count = total_execution_count
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.total_execution_count is not None:
            result['TotalExecutionCount'] = self.total_execution_count
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TotalExecutionCount') is not None:
            self.total_execution_count = m.get('TotalExecutionCount')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListUserTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        templates: List[ListUserTemplatesResponseBodyTemplates] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.templates = templates

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListUserTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListUserTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserTemplatesResponseBody = None,
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
            temp_model = ListUserTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetTimerTriggerExecutionRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        execution_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        # This parameter is required.
        self.execution_id = execution_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResetTimerTriggerExecutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetTimerTriggerExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetTimerTriggerExecutionResponseBody = None,
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
            temp_model = ResetTimerTriggerExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetUserExecutionRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        execution_id: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        # This parameter is required.
        self.execution_id = execution_id
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ResetUserExecutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetUserExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetUserExecutionResponseBody = None,
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
            temp_model = ResetUserExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFlowControlRequest(TeaModel):
    def __init__(
        self,
        api: str = None,
        service: str = None,
        type: int = None,
        uid: str = None,
        value: int = None,
    ):
        self.api = api
        self.service = service
        # This parameter is required.
        self.type = type
        self.uid = uid
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['Api'] = self.api
        if self.service is not None:
            result['Service'] = self.service
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SetFlowControlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetFlowControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetFlowControlResponseBody = None,
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
            temp_model = SetFlowControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetQuotaRequest(TeaModel):
    def __init__(
        self,
        quota_name: str = None,
        region_id: str = None,
        uid: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.quota_name = quota_name
        self.region_id = region_id
        # This parameter is required.
        self.uid = uid
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SetQuotaResponseBody(TeaModel):
    def __init__(
        self,
        quota: int = None,
        request_id: str = None,
        uid: str = None,
    ):
        self.quota = quota
        self.request_id = request_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SetQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetQuotaResponseBody = None,
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
            temp_model = SetQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateUserExecutionRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        execution_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        # This parameter is required.
        self.execution_id = execution_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class TerminateUserExecutionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TerminateUserExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TerminateUserExecutionResponseBody = None,
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
            temp_model = TerminateUserExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateActionRequest(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        action_type: str = None,
        content: str = None,
        popularity: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.action_name = action_name
        # This parameter is required.
        self.action_type = action_type
        # This parameter is required.
        self.content = content
        self.popularity = popularity
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.content is not None:
            result['Content'] = self.content
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateActionResponseBody(TeaModel):
    def __init__(
        self,
        action_name: str = None,
        action_type: str = None,
        created_date: str = None,
        description: str = None,
        popularity: int = None,
        properties: str = None,
        request_id: str = None,
        template_version: str = None,
    ):
        self.action_name = action_name
        self.action_type = action_type
        self.created_date = created_date
        self.description = description
        self.popularity = popularity
        self.properties = properties
        self.request_id = request_id
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class UpdateActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateActionResponseBody = None,
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
            temp_model = UpdateActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePublicParameterRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        region_id: str = None,
        value: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name
        self.region_id = region_id
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdatePublicParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parameter_version: int = None,
        region_id: str = None,
        share_type: str = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.constraints = constraints
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.name = name
        self.parameter_version = parameter_version
        self.region_id = region_id
        self.share_type = share_type
        self.type = type
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdatePublicParameterResponseBody(TeaModel):
    def __init__(
        self,
        parameter: UpdatePublicParameterResponseBodyParameter = None,
        request_id: str = None,
    ):
        self.parameter = parameter
        self.request_id = request_id

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = UpdatePublicParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePublicParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePublicParameterResponseBody = None,
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
            temp_model = UpdatePublicParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePublicPatchBaselineRequest(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.approval_rules = approval_rules
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdatePublicPatchBaselineResponseBodyPatchBaseline(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        operation_system: str = None,
        share_type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.approval_rules = approval_rules
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.name = name
        self.operation_system = operation_system
        self.share_type = share_type
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdatePublicPatchBaselineResponseBody(TeaModel):
    def __init__(
        self,
        patch_baseline: UpdatePublicPatchBaselineResponseBodyPatchBaseline = None,
        request_id: str = None,
    ):
        self.patch_baseline = patch_baseline
        self.request_id = request_id

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = UpdatePublicPatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m['PatchBaseline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePublicPatchBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePublicPatchBaselineResponseBody = None,
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
            temp_model = UpdatePublicPatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePublicTemplateRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        content: str = None,
        popularity: int = None,
        publisher: str = None,
        region_id: str = None,
        template_name: str = None,
        version_name: str = None,
    ):
        self.category = category
        # This parameter is required.
        self.content = content
        self.popularity = popularity
        self.publisher = publisher
        self.region_id = region_id
        # This parameter is required.
        self.template_name = template_name
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.publisher is not None:
            result['Publisher'] = self.publisher
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('Publisher') is not None:
            self.publisher = m.get('Publisher')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdatePublicTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        category: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        hash: str = None,
        popularity: int = None,
        share_type: str = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.category = category
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.hash = hash
        self.popularity = popularity
        self.share_type = share_type
        self.template_format = template_format
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdatePublicTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template: UpdatePublicTemplateResponseBodyTemplate = None,
    ):
        self.request_id = request_id
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdatePublicTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class UpdatePublicTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePublicTemplateResponseBody = None,
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
            temp_model = UpdatePublicTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidatePublicTemplateContentRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        region_id: str = None,
        template_name: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.region_id = region_id
        self.template_name = template_name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ValidatePublicTemplateContentResponseBodyTasks(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        outputs: str = None,
        properties: str = None,
        type: str = None,
    ):
        self.description = description
        self.name = name
        self.outputs = outputs
        self.properties = properties
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ValidatePublicTemplateContentResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        outputs: str = None,
        parameters: str = None,
        ram_role: str = None,
        request_id: str = None,
        tasks: List[ValidatePublicTemplateContentResponseBodyTasks] = None,
    ):
        self.description = description
        self.outputs = outputs
        self.parameters = parameters
        self.ram_role = ram_role
        self.request_id = request_id
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ValidatePublicTemplateContentResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ValidatePublicTemplateContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidatePublicTemplateContentResponseBody = None,
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
            temp_model = ValidatePublicTemplateContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


