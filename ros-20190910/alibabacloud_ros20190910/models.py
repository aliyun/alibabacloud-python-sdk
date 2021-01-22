# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class GenerateTemplatePolicyRequest(TeaModel):
    def __init__(
        self,
        template_url: str = None,
        template_body: str = None,
        template_id: str = None,
        template_version: str = None,
    ):
        self.template_url = template_url
        self.template_body = template_body
        self.template_id = template_id
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GenerateTemplatePolicyResponsePolicyStatement(TeaModel):
    def __init__(
        self,
        resource: str = None,
        effect: str = None,
        action: List[str] = None,
    ):
        self.resource = resource
        self.effect = effect
        self.action = action

    def validate(self):
        self.validate_required(self.resource, 'resource')
        self.validate_required(self.effect, 'effect')
        self.validate_required(self.action, 'action')

    def to_map(self):
        result = dict()
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.action is not None:
            result['Action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        return self


class GenerateTemplatePolicyResponsePolicy(TeaModel):
    def __init__(
        self,
        version: str = None,
        statement: List[GenerateTemplatePolicyResponsePolicyStatement] = None,
    ):
        self.version = version
        self.statement = statement

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.statement, 'statement')
        if self.statement:
            for k in self.statement:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        result['Statement'] = []
        if self.statement is not None:
            for k in self.statement:
                result['Statement'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        self.statement = []
        if m.get('Statement') is not None:
            for k in m.get('Statement'):
                temp_model = GenerateTemplatePolicyResponsePolicyStatement()
                self.statement.append(temp_model.from_map(k))
        return self


class GenerateTemplatePolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        policy: GenerateTemplatePolicyResponsePolicy = None,
    ):
        self.request_id = request_id
        self.policy = policy

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.policy, 'policy')
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Policy') is not None:
            temp_model = GenerateTemplatePolicyResponsePolicy()
            self.policy = temp_model.from_map(m['Policy'])
        return self


class ListTemplateVersionsRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        template_id: str = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.template_id = template_id

    def validate(self):
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListTemplateVersionsResponseVersions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        update_time: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        description: str = None,
    ):
        self.create_time = create_time
        self.update_time = update_time
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.description = description

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.template_name, 'template_name')
        self.validate_required(self.template_version, 'template_version')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ListTemplateVersionsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        versions: List[ListTemplateVersionsResponseVersions] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.versions = versions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.versions, 'versions')
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListTemplateVersionsResponseVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class SetTemplatePermissionRequest(TeaModel):
    def __init__(
        self,
        share_option: str = None,
        version_option: str = None,
        account_ids: List[str] = None,
        template_version: str = None,
        template_id: str = None,
    ):
        self.share_option = share_option
        self.version_option = version_option
        self.account_ids = account_ids
        self.template_version = template_version
        self.template_id = template_id

    def validate(self):
        self.validate_required(self.share_option, 'share_option')
        self.validate_required(self.account_ids, 'account_ids')
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = dict()
        if self.share_option is not None:
            result['ShareOption'] = self.share_option
        if self.version_option is not None:
            result['VersionOption'] = self.version_option
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShareOption') is not None:
            self.share_option = m.get('ShareOption')
        if m.get('VersionOption') is not None:
            self.version_option = m.get('VersionOption')
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class SetTemplatePermissionResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class ListStackOperationRisksRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_id: str = None,
        operation_type: str = None,
        client_token: str = None,
        ram_role_name: str = None,
        retain_all_resources: bool = None,
        retain_resources: List[str] = None,
    ):
        self.region_id = region_id
        self.stack_id = stack_id
        self.operation_type = operation_type
        self.client_token = client_token
        self.ram_role_name = ram_role_name
        self.retain_all_resources = retain_all_resources
        self.retain_resources = retain_resources

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_id, 'stack_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.retain_all_resources is not None:
            result['RetainAllResources'] = self.retain_all_resources
        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RetainAllResources') is not None:
            self.retain_all_resources = m.get('RetainAllResources')
        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')
        return self


class ListStackOperationRisksResponseRiskResources(TeaModel):
    def __init__(
        self,
        logical_resource_id: str = None,
        physical_resource_id: str = None,
        resource_type: str = None,
        reason: str = None,
        risk_type: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.logical_resource_id = logical_resource_id
        self.physical_resource_id = physical_resource_id
        self.resource_type = resource_type
        self.reason = reason
        self.risk_type = risk_type
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.logical_resource_id, 'logical_resource_id')
        self.validate_required(self.physical_resource_id, 'physical_resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.reason, 'reason')
        self.validate_required(self.risk_type, 'risk_type')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.risk_type is not None:
            result['RiskType'] = self.risk_type
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListStackOperationRisksResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        risk_resources: List[ListStackOperationRisksResponseRiskResources] = None,
    ):
        self.request_id = request_id
        self.risk_resources = risk_resources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.risk_resources, 'risk_resources')
        if self.risk_resources:
            for k in self.risk_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RiskResources'] = []
        if self.risk_resources is not None:
            for k in self.risk_resources:
                result['RiskResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.risk_resources = []
        if m.get('RiskResources') is not None:
            for k in m.get('RiskResources'):
                temp_model = ListStackOperationRisksResponseRiskResources()
                self.risk_resources.append(temp_model.from_map(k))
        return self


class GetTemplateSummaryRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        template_body: str = None,
        region_id: str = None,
        template_id: str = None,
        template_url: str = None,
        change_set_id: str = None,
        template_version: str = None,
        stack_group_name: str = None,
    ):
        self.stack_id = stack_id
        self.template_body = template_body
        self.region_id = region_id
        self.template_id = template_id
        self.template_url = template_url
        self.change_set_id = change_set_id
        self.template_version = template_version
        self.stack_group_name = stack_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class GetTemplateSummaryResponseResourceIdentifierSummaries(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        logical_resource_ids: List[str] = None,
        resource_identifiers: List[str] = None,
    ):
        self.resource_type = resource_type
        self.logical_resource_ids = logical_resource_ids
        self.resource_identifiers = resource_identifiers

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.logical_resource_ids, 'logical_resource_ids')
        self.validate_required(self.resource_identifiers, 'resource_identifiers')

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.logical_resource_ids is not None:
            result['LogicalResourceIds'] = self.logical_resource_ids
        if self.resource_identifiers is not None:
            result['ResourceIdentifiers'] = self.resource_identifiers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('LogicalResourceIds') is not None:
            self.logical_resource_ids = m.get('LogicalResourceIds')
        if m.get('ResourceIdentifiers') is not None:
            self.resource_identifiers = m.get('ResourceIdentifiers')
        return self


class GetTemplateSummaryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        description: str = None,
        metadata: Dict[str, Any] = None,
        version: str = None,
        resource_identifier_summaries: List[GetTemplateSummaryResponseResourceIdentifierSummaries] = None,
        parameters: List[Dict[str, Any]] = None,
        resource_types: List[str] = None,
    ):
        self.request_id = request_id
        self.description = description
        self.metadata = metadata
        self.version = version
        self.resource_identifier_summaries = resource_identifier_summaries
        self.parameters = parameters
        self.resource_types = resource_types

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.metadata, 'metadata')
        self.validate_required(self.version, 'version')
        self.validate_required(self.resource_identifier_summaries, 'resource_identifier_summaries')
        if self.resource_identifier_summaries:
            for k in self.resource_identifier_summaries:
                if k:
                    k.validate()
        self.validate_required(self.parameters, 'parameters')
        self.validate_required(self.resource_types, 'resource_types')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.version is not None:
            result['Version'] = self.version
        result['ResourceIdentifierSummaries'] = []
        if self.resource_identifier_summaries is not None:
            for k in self.resource_identifier_summaries:
                result['ResourceIdentifierSummaries'].append(k.to_map() if k else None)
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        self.resource_identifier_summaries = []
        if m.get('ResourceIdentifierSummaries') is not None:
            for k in m.get('ResourceIdentifierSummaries'):
                temp_model = GetTemplateSummaryResponseResourceIdentifierSummaries()
                self.resource_identifier_summaries.append(temp_model.from_map(k))
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        next_token: str = None,
        key: str = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.next_token = next_token
        self.key = key

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.key, 'key')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        values: List[str] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.values = values

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.next_token = next_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        keys: List[str] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.keys = keys

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.keys, 'keys')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class SetDeletionProtectionRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        deletion_protection: str = None,
        region_id: str = None,
    ):
        self.stack_id = stack_id
        self.deletion_protection = deletion_protection
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.deletion_protection, 'deletion_protection')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetDeletionProtectionResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class UpdateStackTemplateByResourcesRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        dry_run: bool = None,
        region_id: str = None,
        client_token: str = None,
        template_format: str = None,
        logical_resource_id: List[str] = None,
    ):
        self.stack_id = stack_id
        self.dry_run = dry_run
        self.region_id = region_id
        self.client_token = client_token
        self.template_format = template_format
        self.logical_resource_id = logical_resource_id

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        return self


class UpdateStackTemplateByResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        old_template_body: str = None,
        new_template_body: str = None,
    ):
        self.request_id = request_id
        self.old_template_body = old_template_body
        self.new_template_body = new_template_body

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.old_template_body, 'old_template_body')
        self.validate_required(self.new_template_body, 'new_template_body')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.old_template_body is not None:
            result['OldTemplateBody'] = self.old_template_body
        if self.new_template_body is not None:
            result['NewTemplateBody'] = self.new_template_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OldTemplateBody') is not None:
            self.old_template_body = m.get('OldTemplateBody')
        if m.get('NewTemplateBody') is not None:
            self.new_template_body = m.get('NewTemplateBody')
        return self


class GetStackDriftDetectionStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        drift_detection_id: str = None,
    ):
        self.region_id = region_id
        self.drift_detection_id = drift_detection_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.drift_detection_id, 'drift_detection_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DriftDetectionId') is not None:
            self.drift_detection_id = m.get('DriftDetectionId')
        return self


class GetStackDriftDetectionStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        drift_detection_id: str = None,
        drift_detection_time: str = None,
        drift_detection_status: str = None,
        drift_detection_status_reason: str = None,
        stack_drift_status: str = None,
        stack_id: str = None,
        drifted_stack_resource_count: int = None,
    ):
        self.request_id = request_id
        self.drift_detection_id = drift_detection_id
        self.drift_detection_time = drift_detection_time
        self.drift_detection_status = drift_detection_status
        self.drift_detection_status_reason = drift_detection_status_reason
        self.stack_drift_status = stack_drift_status
        self.stack_id = stack_id
        self.drifted_stack_resource_count = drifted_stack_resource_count

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.drift_detection_id, 'drift_detection_id')
        self.validate_required(self.drift_detection_time, 'drift_detection_time')
        self.validate_required(self.drift_detection_status, 'drift_detection_status')
        self.validate_required(self.drift_detection_status_reason, 'drift_detection_status_reason')
        self.validate_required(self.stack_drift_status, 'stack_drift_status')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.drifted_stack_resource_count, 'drifted_stack_resource_count')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.drift_detection_status is not None:
            result['DriftDetectionStatus'] = self.drift_detection_status
        if self.drift_detection_status_reason is not None:
            result['DriftDetectionStatusReason'] = self.drift_detection_status_reason
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.drifted_stack_resource_count is not None:
            result['DriftedStackResourceCount'] = self.drifted_stack_resource_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DriftDetectionId') is not None:
            self.drift_detection_id = m.get('DriftDetectionId')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = m.get('DriftDetectionStatus')
        if m.get('DriftDetectionStatusReason') is not None:
            self.drift_detection_status_reason = m.get('DriftDetectionStatusReason')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('DriftedStackResourceCount') is not None:
            self.drifted_stack_resource_count = m.get('DriftedStackResourceCount')
        return self


class DetectStackGroupDriftRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        stack_group_name: str = None,
        operation_preferences: Dict[str, Any] = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.operation_preferences = operation_preferences

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        return self


class DetectStackGroupDriftShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        stack_group_name: str = None,
        operation_preferences_shrink: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.operation_preferences_shrink = operation_preferences_shrink

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        return self


class DetectStackGroupDriftResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operation_id: str = None,
    ):
        self.request_id = request_id
        self.operation_id = operation_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class ListStackResourceDriftsRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        region_id: str = None,
        max_results: int = None,
        resource_drift_status: List[str] = None,
        next_token: str = None,
    ):
        self.stack_id = stack_id
        self.region_id = region_id
        self.max_results = max_results
        self.resource_drift_status = resource_drift_status
        self.next_token = next_token

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListStackResourceDriftsResponseResourceDriftsPropertyDifferences(TeaModel):
    def __init__(
        self,
        property_path: str = None,
        actual_value: str = None,
        expected_value: str = None,
        difference_type: str = None,
    ):
        self.property_path = property_path
        self.actual_value = actual_value
        self.expected_value = expected_value
        self.difference_type = difference_type

    def validate(self):
        self.validate_required(self.property_path, 'property_path')
        self.validate_required(self.actual_value, 'actual_value')
        self.validate_required(self.expected_value, 'expected_value')
        self.validate_required(self.difference_type, 'difference_type')

    def to_map(self):
        result = dict()
        if self.property_path is not None:
            result['PropertyPath'] = self.property_path
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.expected_value is not None:
            result['ExpectedValue'] = self.expected_value
        if self.difference_type is not None:
            result['DifferenceType'] = self.difference_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyPath') is not None:
            self.property_path = m.get('PropertyPath')
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('ExpectedValue') is not None:
            self.expected_value = m.get('ExpectedValue')
        if m.get('DifferenceType') is not None:
            self.difference_type = m.get('DifferenceType')
        return self


class ListStackResourceDriftsResponseResourceDrifts(TeaModel):
    def __init__(
        self,
        drift_detection_time: str = None,
        resource_drift_status: str = None,
        stack_id: str = None,
        resource_type: str = None,
        physical_resource_id: str = None,
        logical_resource_id: str = None,
        actual_properties: str = None,
        expected_properties: str = None,
        property_differences: List[ListStackResourceDriftsResponseResourceDriftsPropertyDifferences] = None,
    ):
        self.drift_detection_time = drift_detection_time
        self.resource_drift_status = resource_drift_status
        self.stack_id = stack_id
        self.resource_type = resource_type
        self.physical_resource_id = physical_resource_id
        self.logical_resource_id = logical_resource_id
        self.actual_properties = actual_properties
        self.expected_properties = expected_properties
        self.property_differences = property_differences

    def validate(self):
        self.validate_required(self.drift_detection_time, 'drift_detection_time')
        self.validate_required(self.resource_drift_status, 'resource_drift_status')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.physical_resource_id, 'physical_resource_id')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')
        self.validate_required(self.actual_properties, 'actual_properties')
        self.validate_required(self.expected_properties, 'expected_properties')
        self.validate_required(self.property_differences, 'property_differences')
        if self.property_differences:
            for k in self.property_differences:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.actual_properties is not None:
            result['ActualProperties'] = self.actual_properties
        if self.expected_properties is not None:
            result['ExpectedProperties'] = self.expected_properties
        result['PropertyDifferences'] = []
        if self.property_differences is not None:
            for k in self.property_differences:
                result['PropertyDifferences'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('ActualProperties') is not None:
            self.actual_properties = m.get('ActualProperties')
        if m.get('ExpectedProperties') is not None:
            self.expected_properties = m.get('ExpectedProperties')
        self.property_differences = []
        if m.get('PropertyDifferences') is not None:
            for k in m.get('PropertyDifferences'):
                temp_model = ListStackResourceDriftsResponseResourceDriftsPropertyDifferences()
                self.property_differences.append(temp_model.from_map(k))
        return self


class ListStackResourceDriftsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        resource_drifts: List[ListStackResourceDriftsResponseResourceDrifts] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.resource_drifts = resource_drifts

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.resource_drifts, 'resource_drifts')
        if self.resource_drifts:
            for k in self.resource_drifts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ResourceDrifts'] = []
        if self.resource_drifts is not None:
            for k in self.resource_drifts:
                result['ResourceDrifts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.resource_drifts = []
        if m.get('ResourceDrifts') is not None:
            for k in m.get('ResourceDrifts'):
                temp_model = ListStackResourceDriftsResponseResourceDrifts()
                self.resource_drifts.append(temp_model.from_map(k))
        return self


class DetectStackResourceDriftRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        client_token: str = None,
        region_id: str = None,
        logical_resource_id: str = None,
    ):
        self.stack_id = stack_id
        self.client_token = client_token
        self.region_id = region_id
        self.logical_resource_id = logical_resource_id

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        return self


class DetectStackResourceDriftResponsePropertyDifferences(TeaModel):
    def __init__(
        self,
        property_path: str = None,
        actual_value: str = None,
        expected_value: str = None,
        difference_type: str = None,
    ):
        self.property_path = property_path
        self.actual_value = actual_value
        self.expected_value = expected_value
        self.difference_type = difference_type

    def validate(self):
        self.validate_required(self.property_path, 'property_path')
        self.validate_required(self.actual_value, 'actual_value')
        self.validate_required(self.expected_value, 'expected_value')
        self.validate_required(self.difference_type, 'difference_type')

    def to_map(self):
        result = dict()
        if self.property_path is not None:
            result['PropertyPath'] = self.property_path
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.expected_value is not None:
            result['ExpectedValue'] = self.expected_value
        if self.difference_type is not None:
            result['DifferenceType'] = self.difference_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyPath') is not None:
            self.property_path = m.get('PropertyPath')
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('ExpectedValue') is not None:
            self.expected_value = m.get('ExpectedValue')
        if m.get('DifferenceType') is not None:
            self.difference_type = m.get('DifferenceType')
        return self


class DetectStackResourceDriftResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        drift_detection_time: str = None,
        resource_drift_status: str = None,
        stack_id: str = None,
        resource_type: str = None,
        physical_resource_id: str = None,
        logical_resource_id: str = None,
        actual_properties: str = None,
        expected_properties: str = None,
        property_differences: List[DetectStackResourceDriftResponsePropertyDifferences] = None,
    ):
        self.request_id = request_id
        self.drift_detection_time = drift_detection_time
        self.resource_drift_status = resource_drift_status
        self.stack_id = stack_id
        self.resource_type = resource_type
        self.physical_resource_id = physical_resource_id
        self.logical_resource_id = logical_resource_id
        self.actual_properties = actual_properties
        self.expected_properties = expected_properties
        self.property_differences = property_differences

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.drift_detection_time, 'drift_detection_time')
        self.validate_required(self.resource_drift_status, 'resource_drift_status')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.physical_resource_id, 'physical_resource_id')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')
        self.validate_required(self.actual_properties, 'actual_properties')
        self.validate_required(self.expected_properties, 'expected_properties')
        self.validate_required(self.property_differences, 'property_differences')
        if self.property_differences:
            for k in self.property_differences:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.actual_properties is not None:
            result['ActualProperties'] = self.actual_properties
        if self.expected_properties is not None:
            result['ExpectedProperties'] = self.expected_properties
        result['PropertyDifferences'] = []
        if self.property_differences is not None:
            for k in self.property_differences:
                result['PropertyDifferences'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('ActualProperties') is not None:
            self.actual_properties = m.get('ActualProperties')
        if m.get('ExpectedProperties') is not None:
            self.expected_properties = m.get('ExpectedProperties')
        self.property_differences = []
        if m.get('PropertyDifferences') is not None:
            for k in m.get('PropertyDifferences'):
                temp_model = DetectStackResourceDriftResponsePropertyDifferences()
                self.property_differences.append(temp_model.from_map(k))
        return self


class DetectStackDriftRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        region_id: str = None,
        logical_resource_id: List[str] = None,
        client_token: str = None,
    ):
        self.stack_id = stack_id
        self.region_id = region_id
        self.logical_resource_id = logical_resource_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DetectStackDriftResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        drift_detection_id: str = None,
    ):
        self.request_id = request_id
        self.drift_detection_id = drift_detection_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.drift_detection_id, 'drift_detection_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DriftDetectionId') is not None:
            self.drift_detection_id = m.get('DriftDetectionId')
        return self


class UpdateStackInstancesRequestParameterOverrides(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class UpdateStackInstancesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        parameter_overrides: List[UpdateStackInstancesRequestParameterOverrides] = None,
        account_ids: Dict[str, Any] = None,
        region_ids: Dict[str, Any] = None,
        client_token: str = None,
        operation_description: str = None,
        operation_preferences: Dict[str, Any] = None,
        timeout_in_minutes: int = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.parameter_overrides = parameter_overrides
        self.account_ids = account_ids
        self.region_ids = region_ids
        self.client_token = client_token
        self.operation_description = operation_description
        self.operation_preferences = operation_preferences
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()
        self.validate_required(self.account_ids, 'account_ids')
        self.validate_required(self.region_ids, 'region_ids')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = UpdateStackInstancesRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        return self


class UpdateStackInstancesShrinkRequestParameterOverrides(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class UpdateStackInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        parameter_overrides: List[UpdateStackInstancesShrinkRequestParameterOverrides] = None,
        account_ids_shrink: str = None,
        region_ids_shrink: str = None,
        client_token: str = None,
        operation_description: str = None,
        operation_preferences_shrink: str = None,
        timeout_in_minutes: int = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.parameter_overrides = parameter_overrides
        self.account_ids_shrink = account_ids_shrink
        self.region_ids_shrink = region_ids_shrink
        self.client_token = client_token
        self.operation_description = operation_description
        self.operation_preferences_shrink = operation_preferences_shrink
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()
        self.validate_required(self.account_ids_shrink, 'account_ids_shrink')
        self.validate_required(self.region_ids_shrink, 'region_ids_shrink')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = UpdateStackInstancesShrinkRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        return self


class UpdateStackInstancesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operation_id: str = None,
    ):
        self.request_id = request_id
        self.operation_id = operation_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class ListStackGroupOperationsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListStackGroupOperationsResponseStackGroupOperations(TeaModel):
    def __init__(
        self,
        stack_group_name: str = None,
        stack_group_id: str = None,
        operation_id: str = None,
        operation_description: str = None,
        create_time: str = None,
        end_time: str = None,
        action: str = None,
        status: str = None,
    ):
        self.stack_group_name = stack_group_name
        self.stack_group_id = stack_group_id
        self.operation_id = operation_id
        self.operation_description = operation_description
        self.create_time = create_time
        self.end_time = end_time
        self.action = action
        self.status = status

    def validate(self):
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.stack_group_id, 'stack_group_id')
        self.validate_required(self.operation_id, 'operation_id')
        self.validate_required(self.operation_description, 'operation_description')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.action, 'action')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.action is not None:
            result['Action'] = self.action
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListStackGroupOperationsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        stack_group_operations: List[ListStackGroupOperationsResponseStackGroupOperations] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.stack_group_operations = stack_group_operations

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.stack_group_operations, 'stack_group_operations')
        if self.stack_group_operations:
            for k in self.stack_group_operations:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['StackGroupOperations'] = []
        if self.stack_group_operations is not None:
            for k in self.stack_group_operations:
                result['StackGroupOperations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.stack_group_operations = []
        if m.get('StackGroupOperations') is not None:
            for k in m.get('StackGroupOperations'):
                temp_model = ListStackGroupOperationsResponseStackGroupOperations()
                self.stack_group_operations.append(temp_model.from_map(k))
        return self


class GetStackGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class GetStackGroupResponseStackGroupParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetStackGroupResponseStackGroupStackGroupDriftDetectionDetail(TeaModel):
    def __init__(
        self,
        drift_detection_time: str = None,
        stack_group_drift_status: str = None,
        drift_detection_status: str = None,
        drifted_stack_instances_count: int = None,
        failed_stack_instances_count: int = None,
        cancelled_stack_instances_count: int = None,
        in_progress_stack_instances_count: int = None,
        in_sync_stack_instances_count: int = None,
        total_stack_instances_count: int = None,
    ):
        self.drift_detection_time = drift_detection_time
        self.stack_group_drift_status = stack_group_drift_status
        self.drift_detection_status = drift_detection_status
        self.drifted_stack_instances_count = drifted_stack_instances_count
        self.failed_stack_instances_count = failed_stack_instances_count
        self.cancelled_stack_instances_count = cancelled_stack_instances_count
        self.in_progress_stack_instances_count = in_progress_stack_instances_count
        self.in_sync_stack_instances_count = in_sync_stack_instances_count
        self.total_stack_instances_count = total_stack_instances_count

    def validate(self):
        self.validate_required(self.drift_detection_time, 'drift_detection_time')
        self.validate_required(self.stack_group_drift_status, 'stack_group_drift_status')
        self.validate_required(self.drift_detection_status, 'drift_detection_status')
        self.validate_required(self.drifted_stack_instances_count, 'drifted_stack_instances_count')
        self.validate_required(self.failed_stack_instances_count, 'failed_stack_instances_count')
        self.validate_required(self.cancelled_stack_instances_count, 'cancelled_stack_instances_count')
        self.validate_required(self.in_progress_stack_instances_count, 'in_progress_stack_instances_count')
        self.validate_required(self.in_sync_stack_instances_count, 'in_sync_stack_instances_count')
        self.validate_required(self.total_stack_instances_count, 'total_stack_instances_count')

    def to_map(self):
        result = dict()
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.stack_group_drift_status is not None:
            result['StackGroupDriftStatus'] = self.stack_group_drift_status
        if self.drift_detection_status is not None:
            result['DriftDetectionStatus'] = self.drift_detection_status
        if self.drifted_stack_instances_count is not None:
            result['DriftedStackInstancesCount'] = self.drifted_stack_instances_count
        if self.failed_stack_instances_count is not None:
            result['FailedStackInstancesCount'] = self.failed_stack_instances_count
        if self.cancelled_stack_instances_count is not None:
            result['CancelledStackInstancesCount'] = self.cancelled_stack_instances_count
        if self.in_progress_stack_instances_count is not None:
            result['InProgressStackInstancesCount'] = self.in_progress_stack_instances_count
        if self.in_sync_stack_instances_count is not None:
            result['InSyncStackInstancesCount'] = self.in_sync_stack_instances_count
        if self.total_stack_instances_count is not None:
            result['TotalStackInstancesCount'] = self.total_stack_instances_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = m.get('StackGroupDriftStatus')
        if m.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = m.get('DriftDetectionStatus')
        if m.get('DriftedStackInstancesCount') is not None:
            self.drifted_stack_instances_count = m.get('DriftedStackInstancesCount')
        if m.get('FailedStackInstancesCount') is not None:
            self.failed_stack_instances_count = m.get('FailedStackInstancesCount')
        if m.get('CancelledStackInstancesCount') is not None:
            self.cancelled_stack_instances_count = m.get('CancelledStackInstancesCount')
        if m.get('InProgressStackInstancesCount') is not None:
            self.in_progress_stack_instances_count = m.get('InProgressStackInstancesCount')
        if m.get('InSyncStackInstancesCount') is not None:
            self.in_sync_stack_instances_count = m.get('InSyncStackInstancesCount')
        if m.get('TotalStackInstancesCount') is not None:
            self.total_stack_instances_count = m.get('TotalStackInstancesCount')
        return self


class GetStackGroupResponseStackGroup(TeaModel):
    def __init__(
        self,
        stack_group_name: str = None,
        stack_group_id: str = None,
        status: str = None,
        description: str = None,
        template_body: str = None,
        execution_role_name: str = None,
        administration_role_name: str = None,
        parameters: List[GetStackGroupResponseStackGroupParameters] = None,
        stack_group_drift_detection_detail: GetStackGroupResponseStackGroupStackGroupDriftDetectionDetail = None,
    ):
        self.stack_group_name = stack_group_name
        self.stack_group_id = stack_group_id
        self.status = status
        self.description = description
        self.template_body = template_body
        self.execution_role_name = execution_role_name
        self.administration_role_name = administration_role_name
        self.parameters = parameters
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail

    def validate(self):
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.stack_group_id, 'stack_group_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.description, 'description')
        self.validate_required(self.template_body, 'template_body')
        self.validate_required(self.execution_role_name, 'execution_role_name')
        self.validate_required(self.administration_role_name, 'administration_role_name')
        self.validate_required(self.parameters, 'parameters')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        self.validate_required(self.stack_group_drift_detection_detail, 'stack_group_drift_detection_detail')
        if self.stack_group_drift_detection_detail:
            self.stack_group_drift_detection_detail.validate()

    def to_map(self):
        result = dict()
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.description is not None:
            result['Description'] = self.description
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.stack_group_drift_detection_detail is not None:
            result['StackGroupDriftDetectionDetail'] = self.stack_group_drift_detection_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetStackGroupResponseStackGroupParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('StackGroupDriftDetectionDetail') is not None:
            temp_model = GetStackGroupResponseStackGroupStackGroupDriftDetectionDetail()
            self.stack_group_drift_detection_detail = temp_model.from_map(m['StackGroupDriftDetectionDetail'])
        return self


class GetStackGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_group: GetStackGroupResponseStackGroup = None,
    ):
        self.request_id = request_id
        self.stack_group = stack_group

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_group, 'stack_group')
        if self.stack_group:
            self.stack_group.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_group is not None:
            result['StackGroup'] = self.stack_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackGroup') is not None:
            temp_model = GetStackGroupResponseStackGroup()
            self.stack_group = temp_model.from_map(m['StackGroup'])
        return self


class GetStackGroupOperationRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        operation_id: str = None,
    ):
        self.region_id = region_id
        self.operation_id = operation_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class GetStackGroupOperationResponseStackGroupOperationOperationPreferences(TeaModel):
    def __init__(
        self,
        failure_tolerance_count: int = None,
        failure_tolerance_percentage: int = None,
        max_concurrent_count: int = None,
        max_concurrent_percentage: int = None,
        region_ids_order: List[str] = None,
    ):
        self.failure_tolerance_count = failure_tolerance_count
        self.failure_tolerance_percentage = failure_tolerance_percentage
        self.max_concurrent_count = max_concurrent_count
        self.max_concurrent_percentage = max_concurrent_percentage
        self.region_ids_order = region_ids_order

    def validate(self):
        self.validate_required(self.failure_tolerance_count, 'failure_tolerance_count')
        self.validate_required(self.failure_tolerance_percentage, 'failure_tolerance_percentage')
        self.validate_required(self.max_concurrent_count, 'max_concurrent_count')
        self.validate_required(self.max_concurrent_percentage, 'max_concurrent_percentage')
        self.validate_required(self.region_ids_order, 'region_ids_order')

    def to_map(self):
        result = dict()
        if self.failure_tolerance_count is not None:
            result['FailureToleranceCount'] = self.failure_tolerance_count
        if self.failure_tolerance_percentage is not None:
            result['FailureTolerancePercentage'] = self.failure_tolerance_percentage
        if self.max_concurrent_count is not None:
            result['MaxConcurrentCount'] = self.max_concurrent_count
        if self.max_concurrent_percentage is not None:
            result['MaxConcurrentPercentage'] = self.max_concurrent_percentage
        if self.region_ids_order is not None:
            result['RegionIdsOrder'] = self.region_ids_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureToleranceCount') is not None:
            self.failure_tolerance_count = m.get('FailureToleranceCount')
        if m.get('FailureTolerancePercentage') is not None:
            self.failure_tolerance_percentage = m.get('FailureTolerancePercentage')
        if m.get('MaxConcurrentCount') is not None:
            self.max_concurrent_count = m.get('MaxConcurrentCount')
        if m.get('MaxConcurrentPercentage') is not None:
            self.max_concurrent_percentage = m.get('MaxConcurrentPercentage')
        if m.get('RegionIdsOrder') is not None:
            self.region_ids_order = m.get('RegionIdsOrder')
        return self


class GetStackGroupOperationResponseStackGroupOperationStackGroupDriftDetectionDetail(TeaModel):
    def __init__(
        self,
        drift_detection_time: str = None,
        stack_group_drift_status: str = None,
        drift_detection_status: str = None,
        drifted_stack_instances_count: int = None,
        failed_stack_instances_count: int = None,
        cancelled_stack_instances_count: int = None,
        in_progress_stack_instances_count: int = None,
        in_sync_stack_instances_count: int = None,
        total_stack_instances_count: int = None,
    ):
        self.drift_detection_time = drift_detection_time
        self.stack_group_drift_status = stack_group_drift_status
        self.drift_detection_status = drift_detection_status
        self.drifted_stack_instances_count = drifted_stack_instances_count
        self.failed_stack_instances_count = failed_stack_instances_count
        self.cancelled_stack_instances_count = cancelled_stack_instances_count
        self.in_progress_stack_instances_count = in_progress_stack_instances_count
        self.in_sync_stack_instances_count = in_sync_stack_instances_count
        self.total_stack_instances_count = total_stack_instances_count

    def validate(self):
        self.validate_required(self.drift_detection_time, 'drift_detection_time')
        self.validate_required(self.stack_group_drift_status, 'stack_group_drift_status')
        self.validate_required(self.drift_detection_status, 'drift_detection_status')
        self.validate_required(self.drifted_stack_instances_count, 'drifted_stack_instances_count')
        self.validate_required(self.failed_stack_instances_count, 'failed_stack_instances_count')
        self.validate_required(self.cancelled_stack_instances_count, 'cancelled_stack_instances_count')
        self.validate_required(self.in_progress_stack_instances_count, 'in_progress_stack_instances_count')
        self.validate_required(self.in_sync_stack_instances_count, 'in_sync_stack_instances_count')
        self.validate_required(self.total_stack_instances_count, 'total_stack_instances_count')

    def to_map(self):
        result = dict()
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.stack_group_drift_status is not None:
            result['StackGroupDriftStatus'] = self.stack_group_drift_status
        if self.drift_detection_status is not None:
            result['DriftDetectionStatus'] = self.drift_detection_status
        if self.drifted_stack_instances_count is not None:
            result['DriftedStackInstancesCount'] = self.drifted_stack_instances_count
        if self.failed_stack_instances_count is not None:
            result['FailedStackInstancesCount'] = self.failed_stack_instances_count
        if self.cancelled_stack_instances_count is not None:
            result['CancelledStackInstancesCount'] = self.cancelled_stack_instances_count
        if self.in_progress_stack_instances_count is not None:
            result['InProgressStackInstancesCount'] = self.in_progress_stack_instances_count
        if self.in_sync_stack_instances_count is not None:
            result['InSyncStackInstancesCount'] = self.in_sync_stack_instances_count
        if self.total_stack_instances_count is not None:
            result['TotalStackInstancesCount'] = self.total_stack_instances_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = m.get('StackGroupDriftStatus')
        if m.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = m.get('DriftDetectionStatus')
        if m.get('DriftedStackInstancesCount') is not None:
            self.drifted_stack_instances_count = m.get('DriftedStackInstancesCount')
        if m.get('FailedStackInstancesCount') is not None:
            self.failed_stack_instances_count = m.get('FailedStackInstancesCount')
        if m.get('CancelledStackInstancesCount') is not None:
            self.cancelled_stack_instances_count = m.get('CancelledStackInstancesCount')
        if m.get('InProgressStackInstancesCount') is not None:
            self.in_progress_stack_instances_count = m.get('InProgressStackInstancesCount')
        if m.get('InSyncStackInstancesCount') is not None:
            self.in_sync_stack_instances_count = m.get('InSyncStackInstancesCount')
        if m.get('TotalStackInstancesCount') is not None:
            self.total_stack_instances_count = m.get('TotalStackInstancesCount')
        return self


class GetStackGroupOperationResponseStackGroupOperation(TeaModel):
    def __init__(
        self,
        stack_group_name: str = None,
        stack_group_id: str = None,
        operation_id: str = None,
        operation_description: str = None,
        create_time: str = None,
        end_time: str = None,
        action: str = None,
        status: str = None,
        retain_stacks: bool = None,
        administrator_role_name: str = None,
        execution_role_name: str = None,
        operation_preferences: GetStackGroupOperationResponseStackGroupOperationOperationPreferences = None,
        stack_group_drift_detection_detail: GetStackGroupOperationResponseStackGroupOperationStackGroupDriftDetectionDetail = None,
    ):
        self.stack_group_name = stack_group_name
        self.stack_group_id = stack_group_id
        self.operation_id = operation_id
        self.operation_description = operation_description
        self.create_time = create_time
        self.end_time = end_time
        self.action = action
        self.status = status
        self.retain_stacks = retain_stacks
        self.administrator_role_name = administrator_role_name
        self.execution_role_name = execution_role_name
        self.operation_preferences = operation_preferences
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail

    def validate(self):
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.stack_group_id, 'stack_group_id')
        self.validate_required(self.operation_id, 'operation_id')
        self.validate_required(self.operation_description, 'operation_description')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.action, 'action')
        self.validate_required(self.status, 'status')
        self.validate_required(self.retain_stacks, 'retain_stacks')
        self.validate_required(self.administrator_role_name, 'administrator_role_name')
        self.validate_required(self.execution_role_name, 'execution_role_name')
        self.validate_required(self.operation_preferences, 'operation_preferences')
        if self.operation_preferences:
            self.operation_preferences.validate()
        self.validate_required(self.stack_group_drift_detection_detail, 'stack_group_drift_detection_detail')
        if self.stack_group_drift_detection_detail:
            self.stack_group_drift_detection_detail.validate()

    def to_map(self):
        result = dict()
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.action is not None:
            result['Action'] = self.action
        if self.status is not None:
            result['Status'] = self.status
        if self.retain_stacks is not None:
            result['RetainStacks'] = self.retain_stacks
        if self.administrator_role_name is not None:
            result['AdministratorRoleName'] = self.administrator_role_name
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences.to_map()
        if self.stack_group_drift_detection_detail is not None:
            result['StackGroupDriftDetectionDetail'] = self.stack_group_drift_detection_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RetainStacks') is not None:
            self.retain_stacks = m.get('RetainStacks')
        if m.get('AdministratorRoleName') is not None:
            self.administrator_role_name = m.get('AdministratorRoleName')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('OperationPreferences') is not None:
            temp_model = GetStackGroupOperationResponseStackGroupOperationOperationPreferences()
            self.operation_preferences = temp_model.from_map(m['OperationPreferences'])
        if m.get('StackGroupDriftDetectionDetail') is not None:
            temp_model = GetStackGroupOperationResponseStackGroupOperationStackGroupDriftDetectionDetail()
            self.stack_group_drift_detection_detail = temp_model.from_map(m['StackGroupDriftDetectionDetail'])
        return self


class GetStackGroupOperationResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_group_operation: GetStackGroupOperationResponseStackGroupOperation = None,
    ):
        self.request_id = request_id
        self.stack_group_operation = stack_group_operation

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_group_operation, 'stack_group_operation')
        if self.stack_group_operation:
            self.stack_group_operation.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_group_operation is not None:
            result['StackGroupOperation'] = self.stack_group_operation.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackGroupOperation') is not None:
            temp_model = GetStackGroupOperationResponseStackGroupOperation()
            self.stack_group_operation = temp_model.from_map(m['StackGroupOperation'])
        return self


class ListStackGroupsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        status: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.region_id = region_id
        self.status = status
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListStackGroupsResponseStackGroups(TeaModel):
    def __init__(
        self,
        stack_group_name: str = None,
        stack_group_id: str = None,
        status: str = None,
        description: str = None,
        drift_detection_time: str = None,
        stack_group_drift_status: str = None,
    ):
        self.stack_group_name = stack_group_name
        self.stack_group_id = stack_group_id
        self.status = status
        self.description = description
        self.drift_detection_time = drift_detection_time
        self.stack_group_drift_status = stack_group_drift_status

    def validate(self):
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.stack_group_id, 'stack_group_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.description, 'description')
        self.validate_required(self.drift_detection_time, 'drift_detection_time')
        self.validate_required(self.stack_group_drift_status, 'stack_group_drift_status')

    def to_map(self):
        result = dict()
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.description is not None:
            result['Description'] = self.description
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.stack_group_drift_status is not None:
            result['StackGroupDriftStatus'] = self.stack_group_drift_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = m.get('StackGroupDriftStatus')
        return self


class ListStackGroupsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        stack_groups: List[ListStackGroupsResponseStackGroups] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.stack_groups = stack_groups

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.stack_groups, 'stack_groups')
        if self.stack_groups:
            for k in self.stack_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['StackGroups'] = []
        if self.stack_groups is not None:
            for k in self.stack_groups:
                result['StackGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.stack_groups = []
        if m.get('StackGroups') is not None:
            for k in m.get('StackGroups'):
                temp_model = ListStackGroupsResponseStackGroups()
                self.stack_groups.append(temp_model.from_map(k))
        return self


class CreateStackInstancesRequestParameterOverrides(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class CreateStackInstancesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        parameter_overrides: List[CreateStackInstancesRequestParameterOverrides] = None,
        account_ids: Dict[str, Any] = None,
        region_ids: Dict[str, Any] = None,
        client_token: str = None,
        operation_description: str = None,
        operation_preferences: Dict[str, Any] = None,
        timeout_in_minutes: int = None,
        disable_rollback: bool = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.parameter_overrides = parameter_overrides
        self.account_ids = account_ids
        self.region_ids = region_ids
        self.client_token = client_token
        self.operation_description = operation_description
        self.operation_preferences = operation_preferences
        self.timeout_in_minutes = timeout_in_minutes
        self.disable_rollback = disable_rollback

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()
        self.validate_required(self.account_ids, 'account_ids')
        self.validate_required(self.region_ids, 'region_ids')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = CreateStackInstancesRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        return self


class CreateStackInstancesShrinkRequestParameterOverrides(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class CreateStackInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        parameter_overrides: List[CreateStackInstancesShrinkRequestParameterOverrides] = None,
        account_ids_shrink: str = None,
        region_ids_shrink: str = None,
        client_token: str = None,
        operation_description: str = None,
        operation_preferences_shrink: str = None,
        timeout_in_minutes: int = None,
        disable_rollback: bool = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.parameter_overrides = parameter_overrides
        self.account_ids_shrink = account_ids_shrink
        self.region_ids_shrink = region_ids_shrink
        self.client_token = client_token
        self.operation_description = operation_description
        self.operation_preferences_shrink = operation_preferences_shrink
        self.timeout_in_minutes = timeout_in_minutes
        self.disable_rollback = disable_rollback

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()
        self.validate_required(self.account_ids_shrink, 'account_ids_shrink')
        self.validate_required(self.region_ids_shrink, 'region_ids_shrink')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = CreateStackInstancesShrinkRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        return self


class CreateStackInstancesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operation_id: str = None,
    ):
        self.request_id = request_id
        self.operation_id = operation_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class CreateStackGroupRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class CreateStackGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        description: str = None,
        parameters: List[CreateStackGroupRequestParameters] = None,
        template_body: str = None,
        template_url: str = None,
        client_token: str = None,
        administration_role_name: str = None,
        execution_role_name: str = None,
        template_id: str = None,
        template_version: str = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.description = description
        self.parameters = parameters
        self.template_body = template_body
        self.template_url = template_url
        self.client_token = client_token
        self.administration_role_name = administration_role_name
        self.execution_role_name = execution_role_name
        self.template_id = template_id
        self.template_version = template_version

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.description is not None:
            result['Description'] = self.description
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateStackGroupRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class CreateStackGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_group_id: str = None,
    ):
        self.request_id = request_id
        self.stack_group_id = stack_group_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_group_id, 'stack_group_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        return self


class GetStackInstanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        stack_instance_account_id: str = None,
        stack_instance_region_id: str = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.stack_instance_account_id = stack_instance_account_id
        self.stack_instance_region_id = stack_instance_region_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.stack_instance_account_id, 'stack_instance_account_id')
        self.validate_required(self.stack_instance_region_id, 'stack_instance_region_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_instance_account_id is not None:
            result['StackInstanceAccountId'] = self.stack_instance_account_id
        if self.stack_instance_region_id is not None:
            result['StackInstanceRegionId'] = self.stack_instance_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackInstanceAccountId') is not None:
            self.stack_instance_account_id = m.get('StackInstanceAccountId')
        if m.get('StackInstanceRegionId') is not None:
            self.stack_instance_region_id = m.get('StackInstanceRegionId')
        return self


class GetStackInstanceResponseStackInstanceParameterOverrides(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetStackInstanceResponseStackInstance(TeaModel):
    def __init__(
        self,
        stack_group_name: str = None,
        stack_group_id: str = None,
        stack_id: str = None,
        account_id: str = None,
        region_id: str = None,
        status: str = None,
        status_reason: str = None,
        stack_drift_status: str = None,
        drift_detection_time: str = None,
        parameter_overrides: List[GetStackInstanceResponseStackInstanceParameterOverrides] = None,
    ):
        self.stack_group_name = stack_group_name
        self.stack_group_id = stack_group_id
        self.stack_id = stack_id
        self.account_id = account_id
        self.region_id = region_id
        self.status = status
        self.status_reason = status_reason
        self.stack_drift_status = stack_drift_status
        self.drift_detection_time = drift_detection_time
        self.parameter_overrides = parameter_overrides

    def validate(self):
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.stack_group_id, 'stack_group_id')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_reason, 'status_reason')
        self.validate_required(self.stack_drift_status, 'stack_drift_status')
        self.validate_required(self.drift_detection_time, 'drift_detection_time')
        self.validate_required(self.parameter_overrides, 'parameter_overrides')
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = GetStackInstanceResponseStackInstanceParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        return self


class GetStackInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_instance: GetStackInstanceResponseStackInstance = None,
    ):
        self.request_id = request_id
        self.stack_instance = stack_instance

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_instance, 'stack_instance')
        if self.stack_instance:
            self.stack_instance.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_instance is not None:
            result['StackInstance'] = self.stack_instance.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackInstance') is not None:
            temp_model = GetStackInstanceResponseStackInstance()
            self.stack_instance = temp_model.from_map(m['StackInstance'])
        return self


class UpdateStackGroupRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class UpdateStackGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        description: str = None,
        parameters: List[UpdateStackGroupRequestParameters] = None,
        account_ids: Dict[str, Any] = None,
        region_ids: Dict[str, Any] = None,
        template_body: str = None,
        template_url: str = None,
        client_token: str = None,
        operation_description: str = None,
        operation_preferences: Dict[str, Any] = None,
        administration_role_name: str = None,
        execution_role_name: str = None,
        template_id: str = None,
        template_version: str = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.description = description
        self.parameters = parameters
        self.account_ids = account_ids
        self.region_ids = region_ids
        self.template_body = template_body
        self.template_url = template_url
        self.client_token = client_token
        self.operation_description = operation_description
        self.operation_preferences = operation_preferences
        self.administration_role_name = administration_role_name
        self.execution_role_name = execution_role_name
        self.template_id = template_id
        self.template_version = template_version

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.description is not None:
            result['Description'] = self.description
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateStackGroupRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class UpdateStackGroupShrinkRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class UpdateStackGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        description: str = None,
        parameters: List[UpdateStackGroupShrinkRequestParameters] = None,
        account_ids_shrink: str = None,
        region_ids_shrink: str = None,
        template_body: str = None,
        template_url: str = None,
        client_token: str = None,
        operation_description: str = None,
        operation_preferences_shrink: str = None,
        administration_role_name: str = None,
        execution_role_name: str = None,
        template_id: str = None,
        template_version: str = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.description = description
        self.parameters = parameters
        self.account_ids_shrink = account_ids_shrink
        self.region_ids_shrink = region_ids_shrink
        self.template_body = template_body
        self.template_url = template_url
        self.client_token = client_token
        self.operation_description = operation_description
        self.operation_preferences_shrink = operation_preferences_shrink
        self.administration_role_name = administration_role_name
        self.execution_role_name = execution_role_name
        self.template_id = template_id
        self.template_version = template_version

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.description is not None:
            result['Description'] = self.description
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateStackGroupShrinkRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class UpdateStackGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operation_id: str = None,
    ):
        self.request_id = request_id
        self.operation_id = operation_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class ListStackInstancesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        stack_instance_account_id: str = None,
        stack_instance_region_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.stack_instance_account_id = stack_instance_account_id
        self.stack_instance_region_id = stack_instance_region_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_instance_account_id is not None:
            result['StackInstanceAccountId'] = self.stack_instance_account_id
        if self.stack_instance_region_id is not None:
            result['StackInstanceRegionId'] = self.stack_instance_region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackInstanceAccountId') is not None:
            self.stack_instance_account_id = m.get('StackInstanceAccountId')
        if m.get('StackInstanceRegionId') is not None:
            self.stack_instance_region_id = m.get('StackInstanceRegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListStackInstancesResponseStackInstances(TeaModel):
    def __init__(
        self,
        stack_group_name: str = None,
        stack_group_id: str = None,
        stack_id: str = None,
        account_id: str = None,
        region_id: str = None,
        status: str = None,
        status_reason: str = None,
        stack_drift_status: str = None,
        drift_detection_time: str = None,
    ):
        self.stack_group_name = stack_group_name
        self.stack_group_id = stack_group_id
        self.stack_id = stack_id
        self.account_id = account_id
        self.region_id = region_id
        self.status = status
        self.status_reason = status_reason
        self.stack_drift_status = stack_drift_status
        self.drift_detection_time = drift_detection_time

    def validate(self):
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.stack_group_id, 'stack_group_id')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_reason, 'status_reason')
        self.validate_required(self.stack_drift_status, 'stack_drift_status')
        self.validate_required(self.drift_detection_time, 'drift_detection_time')

    def to_map(self):
        result = dict()
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        return self


class ListStackInstancesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        stack_instances: List[ListStackInstancesResponseStackInstances] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.stack_instances = stack_instances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.stack_instances, 'stack_instances')
        if self.stack_instances:
            for k in self.stack_instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['StackInstances'] = []
        if self.stack_instances is not None:
            for k in self.stack_instances:
                result['StackInstances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.stack_instances = []
        if m.get('StackInstances') is not None:
            for k in m.get('StackInstances'):
                temp_model = ListStackInstancesResponseStackInstances()
                self.stack_instances.append(temp_model.from_map(k))
        return self


class ListStackGroupOperationResultsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        operation_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.region_id = region_id
        self.operation_id = operation_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListStackGroupOperationResultsResponseStackGroupOperationResults(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        region_id: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.account_id = account_id
        self.region_id = region_id
        self.status = status
        self.status_reason = status_reason

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_reason, 'status_reason')

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class ListStackGroupOperationResultsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        stack_group_operation_results: List[ListStackGroupOperationResultsResponseStackGroupOperationResults] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.stack_group_operation_results = stack_group_operation_results

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.stack_group_operation_results, 'stack_group_operation_results')
        if self.stack_group_operation_results:
            for k in self.stack_group_operation_results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['StackGroupOperationResults'] = []
        if self.stack_group_operation_results is not None:
            for k in self.stack_group_operation_results:
                result['StackGroupOperationResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.stack_group_operation_results = []
        if m.get('StackGroupOperationResults') is not None:
            for k in m.get('StackGroupOperationResults'):
                temp_model = ListStackGroupOperationResultsResponseStackGroupOperationResults()
                self.stack_group_operation_results.append(temp_model.from_map(k))
        return self


class StopStackGroupOperationRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        operation_id: str = None,
    ):
        self.region_id = region_id
        self.operation_id = operation_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        return self


class StopStackGroupOperationResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DeleteStackGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class DeleteStackGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DeleteStackInstancesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        account_ids: Dict[str, Any] = None,
        region_ids: Dict[str, Any] = None,
        retain_stacks: bool = None,
        client_token: str = None,
        operation_description: str = None,
        operation_preferences: Dict[str, Any] = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.account_ids = account_ids
        self.region_ids = region_ids
        self.retain_stacks = retain_stacks
        self.client_token = client_token
        self.operation_description = operation_description
        self.operation_preferences = operation_preferences

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.account_ids, 'account_ids')
        self.validate_required(self.region_ids, 'region_ids')
        self.validate_required(self.retain_stacks, 'retain_stacks')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.retain_stacks is not None:
            result['RetainStacks'] = self.retain_stacks
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('RetainStacks') is not None:
            self.retain_stacks = m.get('RetainStacks')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        return self


class DeleteStackInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_name: str = None,
        account_ids_shrink: str = None,
        region_ids_shrink: str = None,
        retain_stacks: bool = None,
        client_token: str = None,
        operation_description: str = None,
        operation_preferences_shrink: str = None,
    ):
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.account_ids_shrink = account_ids_shrink
        self.region_ids_shrink = region_ids_shrink
        self.retain_stacks = retain_stacks
        self.client_token = client_token
        self.operation_description = operation_description
        self.operation_preferences_shrink = operation_preferences_shrink

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.account_ids_shrink, 'account_ids_shrink')
        self.validate_required(self.region_ids_shrink, 'region_ids_shrink')
        self.validate_required(self.retain_stacks, 'retain_stacks')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.retain_stacks is not None:
            result['RetainStacks'] = self.retain_stacks
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('RetainStacks') is not None:
            self.retain_stacks = m.get('RetainStacks')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        return self


class DeleteStackInstancesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        operation_id: str = None,
    ):
        self.request_id = request_id
        self.operation_id = operation_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
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
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag
        self.next_token = next_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTagResourcesResponseTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        tag_resources: List[ListTagResourcesResponseTagResources] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.tag_resources = tag_resources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.tag_resources, 'tag_resources')
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
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
        all: bool = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.all = all

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

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
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        self.template_id = template_id

    def validate(self):
        self.validate_required(self.template_id, 'template_id')

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


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class UpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        template_url: str = None,
        template_name: str = None,
        description: str = None,
        template_body: str = None,
        template_id: str = None,
    ):
        self.template_url = template_url
        self.template_name = template_name
        self.description = description
        self.template_body = template_body
        self.template_id = template_id

    def validate(self):
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = dict()
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.description is not None:
            result['Description'] = self.description
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_id: str = None,
    ):
        self.request_id = request_id
        self.template_id = template_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListTemplatesRequestTag(TeaModel):
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


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        template_name: str = None,
        tag: List[ListTemplatesRequestTag] = None,
        share_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.template_name = template_name
        self.tag = tag
        self.share_type = share_type

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTemplatesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class ListTemplatesResponseTemplates(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        template_id: str = None,
        template_name: str = None,
        update_time: str = None,
        template_version: str = None,
        share_type: str = None,
        owner_id: str = None,
        template_arn: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.template_id = template_id
        self.template_name = template_name
        self.update_time = update_time
        self.template_version = template_version
        self.share_type = share_type
        self.owner_id = owner_id
        self.template_arn = template_arn

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.description, 'description')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.template_name, 'template_name')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.template_version, 'template_version')
        self.validate_required(self.share_type, 'share_type')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.template_arn, 'template_arn')

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_arn is not None:
            result['TemplateARN'] = self.template_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateARN') is not None:
            self.template_arn = m.get('TemplateARN')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        templates: List[ListTemplatesResponseTemplates] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.templates = templates

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.templates, 'templates')
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        template_url: str = None,
        description: str = None,
        template_body: str = None,
        template_name: str = None,
    ):
        self.template_url = template_url
        self.description = description
        self.template_body = template_body
        self.template_name = template_name

    def validate(self):
        self.validate_required(self.template_name, 'template_name')

    def to_map(self):
        result = dict()
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.description is not None:
            result['Description'] = self.description
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_id: str = None,
    ):
        self.request_id = request_id
        self.template_id = template_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateStackRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class CreateStackRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')

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


class CreateStackRequest(TeaModel):
    def __init__(
        self,
        disable_rollback: bool = None,
        template_body: str = None,
        parameters: List[CreateStackRequestParameters] = None,
        stack_policy_url: str = None,
        timeout_in_minutes: int = None,
        stack_policy_body: str = None,
        stack_name: str = None,
        region_id: str = None,
        client_token: str = None,
        template_url: str = None,
        notification_urls: List[str] = None,
        ram_role_name: str = None,
        deletion_protection: str = None,
        create_option: str = None,
        template_id: str = None,
        template_version: str = None,
        tags: List[CreateStackRequestTags] = None,
    ):
        self.disable_rollback = disable_rollback
        self.template_body = template_body
        self.parameters = parameters
        self.stack_policy_url = stack_policy_url
        self.timeout_in_minutes = timeout_in_minutes
        self.stack_policy_body = stack_policy_body
        self.stack_name = stack_name
        self.region_id = region_id
        self.client_token = client_token
        self.template_url = template_url
        self.notification_urls = notification_urls
        self.ram_role_name = ram_role_name
        self.deletion_protection = deletion_protection
        self.create_option = create_option
        self.template_id = template_id
        self.template_version = template_version
        self.tags = tags

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        self.validate_required(self.stack_name, 'stack_name')
        self.validate_required(self.region_id, 'region_id')
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.create_option is not None:
            result['CreateOption'] = self.create_option
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('CreateOption') is not None:
            self.create_option = m.get('CreateOption')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateStackRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateStackResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_id: str = None,
    ):
        self.request_id = request_id
        self.stack_id = stack_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_id, 'stack_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class GetStackRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        region_id: str = None,
        client_token: str = None,
    ):
        self.stack_id = stack_id
        self.region_id = region_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class GetStackResponseParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetStackResponseTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

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


class GetStackResponse(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        disable_rollback: bool = None,
        region_id: str = None,
        request_id: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        template_description: str = None,
        timeout_in_minutes: int = None,
        update_time: str = None,
        parent_stack_id: str = None,
        stack_drift_status: str = None,
        drift_detection_time: str = None,
        ram_role_name: str = None,
        deletion_protection: str = None,
        root_stack_id: str = None,
        stack_type: str = None,
        parameters: List[GetStackResponseParameters] = None,
        tags: List[GetStackResponseTags] = None,
        outputs: List[Dict[str, Any]] = None,
        notification_urls: List[str] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.disable_rollback = disable_rollback
        self.region_id = region_id
        self.request_id = request_id
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.status = status
        self.status_reason = status_reason
        self.template_description = template_description
        self.timeout_in_minutes = timeout_in_minutes
        self.update_time = update_time
        self.parent_stack_id = parent_stack_id
        self.stack_drift_status = stack_drift_status
        self.drift_detection_time = drift_detection_time
        self.ram_role_name = ram_role_name
        self.deletion_protection = deletion_protection
        self.root_stack_id = root_stack_id
        self.stack_type = stack_type
        self.parameters = parameters
        self.tags = tags
        self.outputs = outputs
        self.notification_urls = notification_urls

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.description, 'description')
        self.validate_required(self.disable_rollback, 'disable_rollback')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.stack_name, 'stack_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_reason, 'status_reason')
        self.validate_required(self.template_description, 'template_description')
        self.validate_required(self.timeout_in_minutes, 'timeout_in_minutes')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.parent_stack_id, 'parent_stack_id')
        self.validate_required(self.stack_drift_status, 'stack_drift_status')
        self.validate_required(self.drift_detection_time, 'drift_detection_time')
        self.validate_required(self.ram_role_name, 'ram_role_name')
        self.validate_required(self.deletion_protection, 'deletion_protection')
        self.validate_required(self.root_stack_id, 'root_stack_id')
        self.validate_required(self.stack_type, 'stack_type')
        self.validate_required(self.parameters, 'parameters')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        self.validate_required(self.tags, 'tags')
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        self.validate_required(self.outputs, 'outputs')
        self.validate_required(self.notification_urls, 'notification_urls')

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.root_stack_id is not None:
            result['RootStackId'] = self.root_stack_id
        if self.stack_type is not None:
            result['StackType'] = self.stack_type
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('RootStackId') is not None:
            self.root_stack_id = m.get('RootStackId')
        if m.get('StackType') is not None:
            self.stack_type = m.get('StackType')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetStackResponseParameters()
                self.parameters.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetStackResponseTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')
        return self


class DeleteStackRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        retain_all_resources: bool = None,
        region_id: str = None,
        retain_resources: List[str] = None,
        ram_role_name: str = None,
    ):
        self.stack_id = stack_id
        self.retain_all_resources = retain_all_resources
        self.region_id = region_id
        self.retain_resources = retain_resources
        self.ram_role_name = ram_role_name

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.retain_all_resources is not None:
            result['RetainAllResources'] = self.retain_all_resources
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RetainAllResources') is not None:
            self.retain_all_resources = m.get('RetainAllResources')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        return self


class DeleteStackResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class UpdateStackRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class UpdateStackRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')

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


class UpdateStackRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        client_token: str = None,
        stack_policy_during_update_body: str = None,
        timeout_in_minutes: int = None,
        template_body: str = None,
        parameters: List[UpdateStackRequestParameters] = None,
        stack_policy_url: str = None,
        stack_policy_during_update_url: str = None,
        stack_policy_body: str = None,
        use_previous_parameters: bool = None,
        region_id: str = None,
        disable_rollback: bool = None,
        template_url: str = None,
        ram_role_name: str = None,
        replacement_option: str = None,
        template_id: str = None,
        template_version: str = None,
        tags: List[UpdateStackRequestTags] = None,
    ):
        self.stack_id = stack_id
        self.client_token = client_token
        self.stack_policy_during_update_body = stack_policy_during_update_body
        self.timeout_in_minutes = timeout_in_minutes
        self.template_body = template_body
        self.parameters = parameters
        self.stack_policy_url = stack_policy_url
        self.stack_policy_during_update_url = stack_policy_during_update_url
        self.stack_policy_body = stack_policy_body
        self.use_previous_parameters = use_previous_parameters
        self.region_id = region_id
        self.disable_rollback = disable_rollback
        self.template_url = template_url
        self.ram_role_name = ram_role_name
        self.replacement_option = replacement_option
        self.template_id = template_id
        self.template_version = template_version
        self.tags = tags

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        self.validate_required(self.region_id, 'region_id')
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.stack_policy_during_update_body is not None:
            result['StackPolicyDuringUpdateBody'] = self.stack_policy_during_update_body
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        if self.stack_policy_during_update_url is not None:
            result['StackPolicyDuringUpdateURL'] = self.stack_policy_during_update_url
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.use_previous_parameters is not None:
            result['UsePreviousParameters'] = self.use_previous_parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.replacement_option is not None:
            result['ReplacementOption'] = self.replacement_option
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('StackPolicyDuringUpdateBody') is not None:
            self.stack_policy_during_update_body = m.get('StackPolicyDuringUpdateBody')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        if m.get('StackPolicyDuringUpdateURL') is not None:
            self.stack_policy_during_update_url = m.get('StackPolicyDuringUpdateURL')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('UsePreviousParameters') is not None:
            self.use_previous_parameters = m.get('UsePreviousParameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('ReplacementOption') is not None:
            self.replacement_option = m.get('ReplacementOption')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UpdateStackRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class UpdateStackResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_id: str = None,
    ):
        self.request_id = request_id
        self.stack_id = stack_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_id, 'stack_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class ListStacksRequestTag(TeaModel):
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


class ListStacksRequest(TeaModel):
    def __init__(
        self,
        status: List[str] = None,
        page_size: int = None,
        parent_stack_id: str = None,
        region_id: str = None,
        stack_name: List[str] = None,
        page_number: int = None,
        show_nested_stack: bool = None,
        tag: List[ListStacksRequestTag] = None,
        stack_id: str = None,
    ):
        self.status = status
        self.page_size = page_size
        self.parent_stack_id = parent_stack_id
        self.region_id = region_id
        self.stack_name = stack_name
        self.page_number = page_number
        self.show_nested_stack = show_nested_stack
        self.tag = tag
        self.stack_id = stack_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.show_nested_stack is not None:
            result['ShowNestedStack'] = self.show_nested_stack
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ShowNestedStack') is not None:
            self.show_nested_stack = m.get('ShowNestedStack')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListStacksRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class ListStacksResponseStacksTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

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


class ListStacksResponseStacks(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        disable_rollback: bool = None,
        region_id: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        timeout_in_minutes: int = None,
        parent_stack_id: str = None,
        update_time: str = None,
        stack_drift_status: str = None,
        drift_detection_time: str = None,
        stack_type: str = None,
        tags: List[ListStacksResponseStacksTags] = None,
    ):
        self.create_time = create_time
        self.disable_rollback = disable_rollback
        self.region_id = region_id
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.status = status
        self.status_reason = status_reason
        self.timeout_in_minutes = timeout_in_minutes
        self.parent_stack_id = parent_stack_id
        self.update_time = update_time
        self.stack_drift_status = stack_drift_status
        self.drift_detection_time = drift_detection_time
        self.stack_type = stack_type
        self.tags = tags

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.disable_rollback, 'disable_rollback')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.stack_name, 'stack_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_reason, 'status_reason')
        self.validate_required(self.timeout_in_minutes, 'timeout_in_minutes')
        self.validate_required(self.parent_stack_id, 'parent_stack_id')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.stack_drift_status, 'stack_drift_status')
        self.validate_required(self.drift_detection_time, 'drift_detection_time')
        self.validate_required(self.stack_type, 'stack_type')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.stack_type is not None:
            result['StackType'] = self.stack_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('StackType') is not None:
            self.stack_type = m.get('StackType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListStacksResponseStacksTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListStacksResponse(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        stacks: List[ListStacksResponseStacks] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.stacks = stacks

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.stacks, 'stacks')
        if self.stacks:
            for k in self.stacks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Stacks'] = []
        if self.stacks is not None:
            for k in self.stacks:
                result['Stacks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.stacks = []
        if m.get('Stacks') is not None:
            for k in m.get('Stacks'):
                temp_model = ListStacksResponseStacks()
                self.stacks.append(temp_model.from_map(k))
        return self


class PreviewStackRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class PreviewStackRequest(TeaModel):
    def __init__(
        self,
        disable_rollback: bool = None,
        timeout_in_minutes: int = None,
        parameters: List[PreviewStackRequestParameters] = None,
        template_body: str = None,
        stack_policy_url: str = None,
        region_id: str = None,
        stack_policy_body: str = None,
        stack_name: str = None,
        client_token: str = None,
        template_url: str = None,
        template_id: str = None,
        template_version: str = None,
    ):
        self.disable_rollback = disable_rollback
        self.timeout_in_minutes = timeout_in_minutes
        self.parameters = parameters
        self.template_body = template_body
        self.stack_policy_url = stack_policy_url
        self.region_id = region_id
        self.stack_policy_body = stack_policy_body
        self.stack_name = stack_name
        self.client_token = client_token
        self.template_url = template_url
        self.template_id = template_id
        self.template_version = template_version

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_name, 'stack_name')

    def to_map(self):
        result = dict()
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = PreviewStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class PreviewStackResponseStackParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class PreviewStackResponseStackResources(TeaModel):
    def __init__(
        self,
        description: str = None,
        logical_resource_id: str = None,
        properties: Dict[str, Any] = None,
        resource_type: str = None,
        stack: Dict[str, Any] = None,
        required_by: List[str] = None,
    ):
        self.description = description
        self.logical_resource_id = logical_resource_id
        self.properties = properties
        self.resource_type = resource_type
        self.stack = stack
        self.required_by = required_by

    def validate(self):
        self.validate_required(self.description, 'description')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')
        self.validate_required(self.properties, 'properties')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.stack, 'stack')
        self.validate_required(self.required_by, 'required_by')

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.stack is not None:
            result['Stack'] = self.stack
        if self.required_by is not None:
            result['RequiredBy'] = self.required_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Stack') is not None:
            self.stack = m.get('Stack')
        if m.get('RequiredBy') is not None:
            self.required_by = m.get('RequiredBy')
        return self


class PreviewStackResponseStack(TeaModel):
    def __init__(
        self,
        description: str = None,
        disable_rollback: bool = None,
        region_id: str = None,
        stack_name: str = None,
        stack_policy_body: Dict[str, Any] = None,
        template_description: str = None,
        timeout_in_minutes: int = None,
        parameters: List[PreviewStackResponseStackParameters] = None,
        resources: List[PreviewStackResponseStackResources] = None,
    ):
        self.description = description
        self.disable_rollback = disable_rollback
        self.region_id = region_id
        self.stack_name = stack_name
        self.stack_policy_body = stack_policy_body
        self.template_description = template_description
        self.timeout_in_minutes = timeout_in_minutes
        self.parameters = parameters
        self.resources = resources

    def validate(self):
        self.validate_required(self.description, 'description')
        self.validate_required(self.disable_rollback, 'disable_rollback')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_name, 'stack_name')
        self.validate_required(self.stack_policy_body, 'stack_policy_body')
        self.validate_required(self.template_description, 'template_description')
        self.validate_required(self.timeout_in_minutes, 'timeout_in_minutes')
        self.validate_required(self.parameters, 'parameters')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        self.validate_required(self.resources, 'resources')
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = PreviewStackResponseStackParameters()
                self.parameters.append(temp_model.from_map(k))
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = PreviewStackResponseStackResources()
                self.resources.append(temp_model.from_map(k))
        return self


class PreviewStackResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack: PreviewStackResponseStack = None,
    ):
        self.request_id = request_id
        self.stack = stack

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack, 'stack')
        if self.stack:
            self.stack.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack is not None:
            result['Stack'] = self.stack.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Stack') is not None:
            temp_model = PreviewStackResponseStack()
            self.stack = temp_model.from_map(m['Stack'])
        return self


class GetTemplateEstimateCostRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class GetTemplateEstimateCostRequest(TeaModel):
    def __init__(
        self,
        template_url: str = None,
        region_id: str = None,
        parameters: List[GetTemplateEstimateCostRequestParameters] = None,
        template_body: str = None,
        client_token: str = None,
        template_id: str = None,
        template_version: str = None,
    ):
        self.template_url = template_url
        self.region_id = region_id
        self.parameters = parameters
        self.template_body = template_body
        self.client_token = client_token
        self.template_id = template_id
        self.template_version = template_version

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetTemplateEstimateCostRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetTemplateEstimateCostResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resources: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.resources = resources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resources, 'resources')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class CancelUpdateStackRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        region_id: str = None,
        cancel_type: str = None,
    ):
        self.stack_id = stack_id
        self.region_id = region_id
        self.cancel_type = cancel_type

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cancel_type is not None:
            result['CancelType'] = self.cancel_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CancelType') is not None:
            self.cancel_type = m.get('CancelType')
        return self


class CancelUpdateStackResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class ContinueCreateStackRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class ContinueCreateStackRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        recreating_resources: List[str] = None,
        region_id: str = None,
        ram_role_name: str = None,
        mode: str = None,
        template_body: str = None,
        template_url: str = None,
        parameters: List[ContinueCreateStackRequestParameters] = None,
        dry_run: bool = None,
        template_id: str = None,
        template_version: str = None,
    ):
        self.stack_id = stack_id
        self.recreating_resources = recreating_resources
        self.region_id = region_id
        self.ram_role_name = ram_role_name
        self.mode = mode
        self.template_body = template_body
        self.template_url = template_url
        self.parameters = parameters
        self.dry_run = dry_run
        self.template_id = template_id
        self.template_version = template_version

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.recreating_resources is not None:
            result['RecreatingResources'] = self.recreating_resources
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RecreatingResources') is not None:
            self.recreating_resources = m.get('RecreatingResources')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ContinueCreateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class ContinueCreateStackResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_id: str = None,
    ):
        self.request_id = request_id
        self.stack_id = stack_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_id, 'stack_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class SetStackPolicyRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        region_id: str = None,
        stack_policy_body: str = None,
        stack_policy_url: str = None,
    ):
        self.stack_id = stack_id
        self.region_id = region_id
        self.stack_policy_body = stack_policy_body
        self.stack_policy_url = stack_policy_url

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        return self


class SetStackPolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class GetStackPolicyRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        region_id: str = None,
    ):
        self.stack_id = stack_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetStackPolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_policy_body: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.stack_policy_body = stack_policy_body

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_policy_body, 'stack_policy_body')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        return self


class ValidateTemplateRequest(TeaModel):
    def __init__(
        self,
        template_url: str = None,
        region_id: str = None,
        template_body: str = None,
    ):
        self.template_url = template_url
        self.region_id = region_id
        self.template_body = template_body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        return self


class ValidateTemplateResponse(TeaModel):
    def __init__(
        self,
        description: str = None,
        request_id: str = None,
        parameters: List[Dict[str, Any]] = None,
    ):
        self.description = description
        self.request_id = request_id
        self.parameters = parameters

    def validate(self):
        self.validate_required(self.description, 'description')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.parameters, 'parameters')

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        region_id: str = None,
        change_set_id: str = None,
        template_id: str = None,
        template_version: str = None,
        template_stage: str = None,
        include_permission: str = None,
        stack_group_name: str = None,
    ):
        self.stack_id = stack_id
        self.region_id = region_id
        self.change_set_id = change_set_id
        self.template_id = template_id
        self.template_version = template_version
        self.template_stage = template_stage
        self.include_permission = include_permission
        self.stack_group_name = stack_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.template_stage is not None:
            result['TemplateStage'] = self.template_stage
        if self.include_permission is not None:
            result['IncludePermission'] = self.include_permission
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TemplateStage') is not None:
            self.template_stage = m.get('TemplateStage')
        if m.get('IncludePermission') is not None:
            self.include_permission = m.get('IncludePermission')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class GetTemplateResponsePermissions(TeaModel):
    def __init__(
        self,
        share_option: str = None,
        version_option: str = None,
        template_version: str = None,
        account_id: str = None,
    ):
        self.share_option = share_option
        self.version_option = version_option
        self.template_version = template_version
        self.account_id = account_id

    def validate(self):
        self.validate_required(self.share_option, 'share_option')
        self.validate_required(self.version_option, 'version_option')
        self.validate_required(self.template_version, 'template_version')
        self.validate_required(self.account_id, 'account_id')

    def to_map(self):
        result = dict()
        if self.share_option is not None:
            result['ShareOption'] = self.share_option
        if self.version_option is not None:
            result['VersionOption'] = self.version_option
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShareOption') is not None:
            self.share_option = m.get('ShareOption')
        if m.get('VersionOption') is not None:
            self.version_option = m.get('VersionOption')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_body: str = None,
        stack_id: str = None,
        template_id: str = None,
        stack_group_name: str = None,
        change_set_id: str = None,
        region_id: str = None,
        create_time: str = None,
        description: str = None,
        template_name: str = None,
        update_time: str = None,
        template_version: str = None,
        share_type: str = None,
        owner_id: str = None,
        template_arn: str = None,
        permissions: List[GetTemplateResponsePermissions] = None,
    ):
        self.request_id = request_id
        self.template_body = template_body
        self.stack_id = stack_id
        self.template_id = template_id
        self.stack_group_name = stack_group_name
        self.change_set_id = change_set_id
        self.region_id = region_id
        self.create_time = create_time
        self.description = description
        self.template_name = template_name
        self.update_time = update_time
        self.template_version = template_version
        self.share_type = share_type
        self.owner_id = owner_id
        self.template_arn = template_arn
        self.permissions = permissions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.template_body, 'template_body')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.change_set_id, 'change_set_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.description, 'description')
        self.validate_required(self.template_name, 'template_name')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.template_version, 'template_version')
        self.validate_required(self.share_type, 'share_type')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.template_arn, 'template_arn')
        self.validate_required(self.permissions, 'permissions')
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_arn is not None:
            result['TemplateARN'] = self.template_arn
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateARN') is not None:
            self.template_arn = m.get('TemplateARN')
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = GetTemplateResponsePermissions()
                self.permissions.append(temp_model.from_map(k))
        return self


class GetChangeSetRequest(TeaModel):
    def __init__(
        self,
        show_template: bool = None,
        region_id: str = None,
        change_set_id: str = None,
    ):
        self.show_template = show_template
        self.region_id = region_id
        self.change_set_id = change_set_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.change_set_id, 'change_set_id')

    def to_map(self):
        result = dict()
        if self.show_template is not None:
            result['ShowTemplate'] = self.show_template
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowTemplate') is not None:
            self.show_template = m.get('ShowTemplate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        return self


class GetChangeSetResponseParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetChangeSetResponse(TeaModel):
    def __init__(
        self,
        change_set_id: str = None,
        change_set_name: str = None,
        change_set_type: str = None,
        create_time: str = None,
        description: str = None,
        disable_rollback: bool = None,
        execution_status: str = None,
        region_id: str = None,
        request_id: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        template_body: str = None,
        timeout_in_minutes: int = None,
        status_reason: str = None,
        parameters: List[GetChangeSetResponseParameters] = None,
        changes: List[Dict[str, Any]] = None,
    ):
        self.change_set_id = change_set_id
        self.change_set_name = change_set_name
        self.change_set_type = change_set_type
        self.create_time = create_time
        self.description = description
        self.disable_rollback = disable_rollback
        self.execution_status = execution_status
        self.region_id = region_id
        self.request_id = request_id
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.status = status
        self.template_body = template_body
        self.timeout_in_minutes = timeout_in_minutes
        self.status_reason = status_reason
        self.parameters = parameters
        self.changes = changes

    def validate(self):
        self.validate_required(self.change_set_id, 'change_set_id')
        self.validate_required(self.change_set_name, 'change_set_name')
        self.validate_required(self.change_set_type, 'change_set_type')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.description, 'description')
        self.validate_required(self.disable_rollback, 'disable_rollback')
        self.validate_required(self.execution_status, 'execution_status')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.stack_name, 'stack_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.template_body, 'template_body')
        self.validate_required(self.timeout_in_minutes, 'timeout_in_minutes')
        self.validate_required(self.status_reason, 'status_reason')
        self.validate_required(self.parameters, 'parameters')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        self.validate_required(self.changes, 'changes')

    def to_map(self):
        result = dict()
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name
        if self.change_set_type is not None:
            result['ChangeSetType'] = self.change_set_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.status is not None:
            result['Status'] = self.status
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.changes is not None:
            result['Changes'] = self.changes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')
        if m.get('ChangeSetType') is not None:
            self.change_set_type = m.get('ChangeSetType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetChangeSetResponseParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('Changes') is not None:
            self.changes = m.get('Changes')
        return self


class ListChangeSetsRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        status: List[str] = None,
        change_set_name: List[str] = None,
        page_size: int = None,
        region_id: str = None,
        page_number: int = None,
        execution_status: List[str] = None,
        change_set_id: str = None,
    ):
        self.stack_id = stack_id
        self.status = status
        self.change_set_name = change_set_name
        self.page_size = page_size
        self.region_id = region_id
        self.page_number = page_number
        self.execution_status = execution_status
        self.change_set_id = change_set_id

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.status is not None:
            result['Status'] = self.status
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        return self


class ListChangeSetsResponseChangeSets(TeaModel):
    def __init__(
        self,
        change_set_id: str = None,
        change_set_name: str = None,
        change_set_type: str = None,
        create_time: str = None,
        description: str = None,
        execution_status: str = None,
        region_id: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.change_set_id = change_set_id
        self.change_set_name = change_set_name
        self.change_set_type = change_set_type
        self.create_time = create_time
        self.description = description
        self.execution_status = execution_status
        self.region_id = region_id
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.status = status
        self.status_reason = status_reason

    def validate(self):
        self.validate_required(self.change_set_id, 'change_set_id')
        self.validate_required(self.change_set_name, 'change_set_name')
        self.validate_required(self.change_set_type, 'change_set_type')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.description, 'description')
        self.validate_required(self.execution_status, 'execution_status')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.stack_name, 'stack_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_reason, 'status_reason')

    def to_map(self):
        result = dict()
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name
        if self.change_set_type is not None:
            result['ChangeSetType'] = self.change_set_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')
        if m.get('ChangeSetType') is not None:
            self.change_set_type = m.get('ChangeSetType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class ListChangeSetsResponse(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        change_sets: List[ListChangeSetsResponseChangeSets] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.change_sets = change_sets

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.change_sets, 'change_sets')
        if self.change_sets:
            for k in self.change_sets:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ChangeSets'] = []
        if self.change_sets is not None:
            for k in self.change_sets:
                result['ChangeSets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.change_sets = []
        if m.get('ChangeSets') is not None:
            for k in m.get('ChangeSets'):
                temp_model = ListChangeSetsResponseChangeSets()
                self.change_sets.append(temp_model.from_map(k))
        return self


class ExecuteChangeSetRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        change_set_id: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.change_set_id = change_set_id
        self.client_token = client_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.change_set_id, 'change_set_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ExecuteChangeSetResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DeleteChangeSetRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        change_set_id: str = None,
    ):
        self.region_id = region_id
        self.change_set_id = change_set_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.change_set_id, 'change_set_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        return self


class DeleteChangeSetResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class ListStackEventsRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        status: List[str] = None,
        page_size: int = None,
        resource_type: List[str] = None,
        region_id: str = None,
        page_number: int = None,
        logical_resource_id: List[str] = None,
    ):
        self.stack_id = stack_id
        self.status = status
        self.page_size = page_size
        self.resource_type = resource_type
        self.region_id = region_id
        self.page_number = page_number
        self.logical_resource_id = logical_resource_id

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        return self


class ListStackEventsResponseEvents(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        event_id: str = None,
        logical_resource_id: str = None,
        physical_resource_id: str = None,
        resource_type: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.create_time = create_time
        self.event_id = event_id
        self.logical_resource_id = logical_resource_id
        self.physical_resource_id = physical_resource_id
        self.resource_type = resource_type
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.status = status
        self.status_reason = status_reason

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.event_id, 'event_id')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')
        self.validate_required(self.physical_resource_id, 'physical_resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.stack_name, 'stack_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_reason, 'status_reason')

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class ListStackEventsResponse(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        events: List[ListStackEventsResponseEvents] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.events = events

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.events, 'events')
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = ListStackEventsResponseEvents()
                self.events.append(temp_model.from_map(k))
        return self


class ListStackResourcesRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        region_id: str = None,
    ):
        self.stack_id = stack_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListStackResourcesResponseResources(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        logical_resource_id: str = None,
        physical_resource_id: str = None,
        resource_type: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        update_time: str = None,
        resource_drift_status: str = None,
        drift_detection_time: str = None,
    ):
        self.create_time = create_time
        self.logical_resource_id = logical_resource_id
        self.physical_resource_id = physical_resource_id
        self.resource_type = resource_type
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.status = status
        self.status_reason = status_reason
        self.update_time = update_time
        self.resource_drift_status = resource_drift_status
        self.drift_detection_time = drift_detection_time

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')
        self.validate_required(self.physical_resource_id, 'physical_resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.stack_name, 'stack_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_reason, 'status_reason')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.resource_drift_status, 'resource_drift_status')
        self.validate_required(self.drift_detection_time, 'drift_detection_time')

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        return self


class ListStackResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[ListStackResourcesResponseResources] = None,
    ):
        self.request_id = request_id
        self.resources = resources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resources, 'resources')
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListStackResourcesResponseResources()
                self.resources.append(temp_model.from_map(k))
        return self


class GetStackResourceRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        client_token: str = None,
        region_id: str = None,
        show_resource_attributes: bool = None,
        logical_resource_id: str = None,
    ):
        self.stack_id = stack_id
        self.client_token = client_token
        self.region_id = region_id
        self.show_resource_attributes = show_resource_attributes
        self.logical_resource_id = logical_resource_id

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show_resource_attributes is not None:
            result['ShowResourceAttributes'] = self.show_resource_attributes
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShowResourceAttributes') is not None:
            self.show_resource_attributes = m.get('ShowResourceAttributes')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        return self


class GetStackResourceResponse(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        logical_resource_id: str = None,
        metadata: Dict[str, Any] = None,
        physical_resource_id: str = None,
        request_id: str = None,
        resource_type: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        update_time: str = None,
        resource_drift_status: str = None,
        drift_detection_time: str = None,
        resource_attributes: List[Dict[str, Any]] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.logical_resource_id = logical_resource_id
        self.metadata = metadata
        self.physical_resource_id = physical_resource_id
        self.request_id = request_id
        self.resource_type = resource_type
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.status = status
        self.status_reason = status_reason
        self.update_time = update_time
        self.resource_drift_status = resource_drift_status
        self.drift_detection_time = drift_detection_time
        self.resource_attributes = resource_attributes

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.description, 'description')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')
        self.validate_required(self.metadata, 'metadata')
        self.validate_required(self.physical_resource_id, 'physical_resource_id')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.stack_name, 'stack_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_reason, 'status_reason')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.resource_drift_status, 'resource_drift_status')
        self.validate_required(self.drift_detection_time, 'drift_detection_time')
        self.validate_required(self.resource_attributes, 'resource_attributes')

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.resource_attributes is not None:
            result['ResourceAttributes'] = self.resource_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('ResourceAttributes') is not None:
            self.resource_attributes = m.get('ResourceAttributes')
        return self


class GetResourceTypeTemplateRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetResourceTypeTemplateResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_body: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.template_body = template_body

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.template_body, 'template_body')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        return self


class GetResourceTypeRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetResourceTypeResponse(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        properties: Dict[str, Any] = None,
        request_id: str = None,
        resource_type: str = None,
        support_drift_detection: bool = None,
    ):
        self.attributes = attributes
        self.properties = properties
        self.request_id = request_id
        self.resource_type = resource_type
        self.support_drift_detection = support_drift_detection

    def validate(self):
        self.validate_required(self.attributes, 'attributes')
        self.validate_required(self.properties, 'properties')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.support_drift_detection, 'support_drift_detection')

    def to_map(self):
        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.support_drift_detection is not None:
            result['SupportDriftDetection'] = self.support_drift_detection
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SupportDriftDetection') is not None:
            self.support_drift_detection = m.get('SupportDriftDetection')
        return self


class ListResourceTypesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListResourceTypesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_types: List[str] = None,
    ):
        self.request_id = request_id
        self.resource_types = resource_types

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_types, 'resource_types')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class SignalResourceRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        status: str = None,
        region_id: str = None,
        unique_id: str = None,
        client_token: str = None,
        logical_resource_id: str = None,
    ):
        self.stack_id = stack_id
        self.status = status
        self.region_id = region_id
        self.unique_id = unique_id
        self.client_token = client_token
        self.logical_resource_id = logical_resource_id

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.unique_id, 'unique_id')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.status is not None:
            result['Status'] = self.status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        return self


class SignalResourceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseRegions(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        local_name: str = None,
        region_endpoint: str = None,
    ):
        self.region_id = region_id
        self.local_name = local_name
        self.region_endpoint = region_endpoint

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.local_name, 'local_name')
        self.validate_required(self.region_endpoint, 'region_endpoint')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.regions, 'regions')
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
                temp_model = DescribeRegionsResponseRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class CreateChangeSetRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_value: str = None,
        parameter_key: str = None,
    ):
        self.parameter_value = parameter_value
        self.parameter_key = parameter_key

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = dict()
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        return self


class CreateChangeSetRequestResourcesToImport(TeaModel):
    def __init__(
        self,
        logical_resource_id: str = None,
        resource_type: str = None,
        resource_identifier: str = None,
    ):
        self.logical_resource_id = logical_resource_id
        self.resource_type = resource_type
        self.resource_identifier = resource_identifier

    def validate(self):
        self.validate_required(self.logical_resource_id, 'logical_resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_identifier, 'resource_identifier')

    def to_map(self):
        result = dict()
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_identifier is not None:
            result['ResourceIdentifier'] = self.resource_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceIdentifier') is not None:
            self.resource_identifier = m.get('ResourceIdentifier')
        return self


class CreateChangeSetRequest(TeaModel):
    def __init__(
        self,
        stack_id: str = None,
        parameters: List[CreateChangeSetRequestParameters] = None,
        stack_policy_url: str = None,
        stack_policy_body: str = None,
        stack_name: str = None,
        use_previous_parameters: bool = None,
        change_set_type: str = None,
        description: str = None,
        region_id: str = None,
        client_token: str = None,
        template_url: str = None,
        stack_policy_during_update_url: str = None,
        template_body: str = None,
        timeout_in_minutes: int = None,
        disable_rollback: bool = None,
        change_set_name: str = None,
        stack_policy_during_update_body: str = None,
        notification_urls: List[str] = None,
        ram_role_name: str = None,
        replacement_option: str = None,
        resources_to_import: List[CreateChangeSetRequestResourcesToImport] = None,
        template_id: str = None,
        template_version: str = None,
    ):
        self.stack_id = stack_id
        self.parameters = parameters
        self.stack_policy_url = stack_policy_url
        self.stack_policy_body = stack_policy_body
        self.stack_name = stack_name
        self.use_previous_parameters = use_previous_parameters
        self.change_set_type = change_set_type
        self.description = description
        self.region_id = region_id
        self.client_token = client_token
        self.template_url = template_url
        self.stack_policy_during_update_url = stack_policy_during_update_url
        self.template_body = template_body
        self.timeout_in_minutes = timeout_in_minutes
        self.disable_rollback = disable_rollback
        self.change_set_name = change_set_name
        self.stack_policy_during_update_body = stack_policy_during_update_body
        self.notification_urls = notification_urls
        self.ram_role_name = ram_role_name
        self.replacement_option = replacement_option
        self.resources_to_import = resources_to_import
        self.template_id = template_id
        self.template_version = template_version

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.change_set_name, 'change_set_name')
        if self.resources_to_import:
            for k in self.resources_to_import:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.use_previous_parameters is not None:
            result['UsePreviousParameters'] = self.use_previous_parameters
        if self.change_set_type is not None:
            result['ChangeSetType'] = self.change_set_type
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.stack_policy_during_update_url is not None:
            result['StackPolicyDuringUpdateURL'] = self.stack_policy_during_update_url
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name
        if self.stack_policy_during_update_body is not None:
            result['StackPolicyDuringUpdateBody'] = self.stack_policy_during_update_body
        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.replacement_option is not None:
            result['ReplacementOption'] = self.replacement_option
        result['ResourcesToImport'] = []
        if self.resources_to_import is not None:
            for k in self.resources_to_import:
                result['ResourcesToImport'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateChangeSetRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('UsePreviousParameters') is not None:
            self.use_previous_parameters = m.get('UsePreviousParameters')
        if m.get('ChangeSetType') is not None:
            self.change_set_type = m.get('ChangeSetType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('StackPolicyDuringUpdateURL') is not None:
            self.stack_policy_during_update_url = m.get('StackPolicyDuringUpdateURL')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')
        if m.get('StackPolicyDuringUpdateBody') is not None:
            self.stack_policy_during_update_body = m.get('StackPolicyDuringUpdateBody')
        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('ReplacementOption') is not None:
            self.replacement_option = m.get('ReplacementOption')
        self.resources_to_import = []
        if m.get('ResourcesToImport') is not None:
            for k in m.get('ResourcesToImport'):
                temp_model = CreateChangeSetRequestResourcesToImport()
                self.resources_to_import.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class CreateChangeSetResponse(TeaModel):
    def __init__(
        self,
        change_set_id: str = None,
        request_id: str = None,
        stack_id: str = None,
    ):
        self.change_set_id = change_set_id
        self.request_id = request_id
        self.stack_id = stack_id

    def validate(self):
        self.validate_required(self.change_set_id, 'change_set_id')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_id, 'stack_id')

    def to_map(self):
        result = dict()
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


