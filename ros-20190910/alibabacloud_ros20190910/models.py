# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List, Dict, Any
except ImportError:
    pass


class GenerateTemplatePolicyRequest(TeaModel):
    def __init__(self, template_url=None, template_body=None, template_id=None, template_version=None):
        self.template_url = template_url  # type: str
        self.template_body = template_body  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, map={}):
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        return self


class GenerateTemplatePolicyResponse(TeaModel):
    def __init__(self, request_id=None, policy=None):
        self.request_id = request_id    # type: str
        self.policy = policy            # type: GenerateTemplatePolicyResponsePolicy

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.policy, 'policy')
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Policy') is not None:
            temp_model = GenerateTemplatePolicyResponsePolicy()
            self.policy = temp_model.from_map(map['Policy'])
        return self


class GenerateTemplatePolicyResponsePolicyStatement(TeaModel):
    def __init__(self, resource=None, effect=None, action=None):
        self.resource = resource        # type: str
        self.effect = effect            # type: str
        self.action = action            # type: List[str]

    def validate(self):
        self.validate_required(self.resource, 'resource')
        self.validate_required(self.effect, 'effect')
        self.validate_required(self.action, 'action')

    def to_map(self):
        result = {}
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.action is not None:
            result['Action'] = self.action
        return result

    def from_map(self, map={}):
        if map.get('Resource') is not None:
            self.resource = map.get('Resource')
        if map.get('Effect') is not None:
            self.effect = map.get('Effect')
        if map.get('Action') is not None:
            self.action = map.get('Action')
        return self


class GenerateTemplatePolicyResponsePolicy(TeaModel):
    def __init__(self, version=None, statement=None):
        self.version = version          # type: str
        self.statement = statement      # type: List[GenerateTemplatePolicyResponsePolicyStatement]

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.statement, 'statement')
        if self.statement:
            for k in self.statement:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.version is not None:
            result['Version'] = self.version
        result['Statement'] = []
        if self.statement is not None:
            for k in self.statement:
                result['Statement'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('Version') is not None:
            self.version = map.get('Version')
        self.statement = []
        if map.get('Statement') is not None:
            for k in map.get('Statement'):
                temp_model = GenerateTemplatePolicyResponsePolicyStatement()
                self.statement.append(temp_model.from_map(k))
        return self


class ListTemplateVersionsRequest(TeaModel):
    def __init__(self, next_token=None, max_results=None, template_id=None):
        self.next_token = next_token    # type: str
        self.max_results = max_results  # type: int
        self.template_id = template_id  # type: str

    def validate(self):
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = {}
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, map={}):
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        if map.get('MaxResults') is not None:
            self.max_results = map.get('MaxResults')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        return self


class ListTemplateVersionsResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, versions=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.versions = versions        # type: List[ListTemplateVersionsResponseVersions]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.versions, 'versions')
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        self.versions = []
        if map.get('Versions') is not None:
            for k in map.get('Versions'):
                temp_model = ListTemplateVersionsResponseVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListTemplateVersionsResponseVersions(TeaModel):
    def __init__(self, create_time=None, update_time=None, template_id=None, template_name=None,
                 template_version=None, description=None):
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.template_version = template_version  # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.template_name, 'template_name')
        self.validate_required(self.template_version, 'template_version')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('UpdateTime') is not None:
            self.update_time = map.get('UpdateTime')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateName') is not None:
            self.template_name = map.get('TemplateName')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        return self


class SetTemplatePermissionRequest(TeaModel):
    def __init__(self, share_option=None, version_option=None, account_ids=None, template_version=None,
                 template_id=None):
        self.share_option = share_option  # type: str
        self.version_option = version_option  # type: str
        self.account_ids = account_ids  # type: List[str]
        self.template_version = template_version  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        self.validate_required(self.share_option, 'share_option')
        self.validate_required(self.account_ids, 'account_ids')
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ShareOption') is not None:
            self.share_option = map.get('ShareOption')
        if map.get('VersionOption') is not None:
            self.version_option = map.get('VersionOption')
        if map.get('AccountIds') is not None:
            self.account_ids = map.get('AccountIds')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        return self


class SetTemplatePermissionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ListStackOperationRisksRequest(TeaModel):
    def __init__(self, region_id=None, stack_id=None, operation_type=None, client_token=None, ram_role_name=None,
                 retain_all_resources=None, retain_resources=None):
        self.region_id = region_id      # type: str
        self.stack_id = stack_id        # type: str
        self.operation_type = operation_type  # type: str
        self.client_token = client_token  # type: str
        self.ram_role_name = ram_role_name  # type: str
        self.retain_all_resources = retain_all_resources  # type: bool
        self.retain_resources = retain_resources  # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_id, 'stack_id')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('OperationType') is not None:
            self.operation_type = map.get('OperationType')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('RamRoleName') is not None:
            self.ram_role_name = map.get('RamRoleName')
        if map.get('RetainAllResources') is not None:
            self.retain_all_resources = map.get('RetainAllResources')
        if map.get('RetainResources') is not None:
            self.retain_resources = map.get('RetainResources')
        return self


class ListStackOperationRisksResponse(TeaModel):
    def __init__(self, request_id=None, risk_resources=None):
        self.request_id = request_id    # type: str
        self.risk_resources = risk_resources  # type: List[ListStackOperationRisksResponseRiskResources]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.risk_resources, 'risk_resources')
        if self.risk_resources:
            for k in self.risk_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RiskResources'] = []
        if self.risk_resources is not None:
            for k in self.risk_resources:
                result['RiskResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.risk_resources = []
        if map.get('RiskResources') is not None:
            for k in map.get('RiskResources'):
                temp_model = ListStackOperationRisksResponseRiskResources()
                self.risk_resources.append(temp_model.from_map(k))
        return self


class ListStackOperationRisksResponseRiskResources(TeaModel):
    def __init__(self, logical_resource_id=None, physical_resource_id=None, resource_type=None, reason=None,
                 risk_type=None, code=None, message=None, request_id=None):
        self.logical_resource_id = logical_resource_id  # type: str
        self.physical_resource_id = physical_resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.reason = reason            # type: str
        self.risk_type = risk_type      # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        if map.get('PhysicalResourceId') is not None:
            self.physical_resource_id = map.get('PhysicalResourceId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('Reason') is not None:
            self.reason = map.get('Reason')
        if map.get('RiskType') is not None:
            self.risk_type = map.get('RiskType')
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class GetTemplateSummaryRequest(TeaModel):
    def __init__(self, stack_id=None, template_body=None, region_id=None, template_id=None, template_url=None,
                 change_set_id=None, template_version=None, stack_group_name=None):
        self.stack_id = stack_id        # type: str
        self.template_body = template_body  # type: str
        self.region_id = region_id      # type: str
        self.template_id = template_id  # type: str
        self.template_url = template_url  # type: str
        self.change_set_id = change_set_id  # type: str
        self.template_version = template_version  # type: str
        self.stack_group_name = stack_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('ChangeSetId') is not None:
            self.change_set_id = map.get('ChangeSetId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        return self


class GetTemplateSummaryResponse(TeaModel):
    def __init__(self, request_id=None, description=None, metadata=None, version=None,
                 resource_identifier_summaries=None, parameters=None, resource_types=None):
        self.request_id = request_id    # type: str
        self.description = description  # type: str
        self.metadata = metadata        # type: Dict[str, Any]
        self.version = version          # type: str
        self.resource_identifier_summaries = resource_identifier_summaries  # type: List[GetTemplateSummaryResponseResourceIdentifierSummaries]
        self.parameters = parameters    # type: List[Dict[str, Any]]
        self.resource_types = resource_types  # type: List[str]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('Metadata') is not None:
            self.metadata = map.get('Metadata')
        if map.get('Version') is not None:
            self.version = map.get('Version')
        self.resource_identifier_summaries = []
        if map.get('ResourceIdentifierSummaries') is not None:
            for k in map.get('ResourceIdentifierSummaries'):
                temp_model = GetTemplateSummaryResponseResourceIdentifierSummaries()
                self.resource_identifier_summaries.append(temp_model.from_map(k))
        if map.get('Parameters') is not None:
            self.parameters = map.get('Parameters')
        if map.get('ResourceTypes') is not None:
            self.resource_types = map.get('ResourceTypes')
        return self


class GetTemplateSummaryResponseResourceIdentifierSummaries(TeaModel):
    def __init__(self, resource_type=None, logical_resource_ids=None, resource_identifiers=None):
        self.resource_type = resource_type  # type: str
        self.logical_resource_ids = logical_resource_ids  # type: List[str]
        self.resource_identifiers = resource_identifiers  # type: List[str]

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.logical_resource_ids, 'logical_resource_ids')
        self.validate_required(self.resource_identifiers, 'resource_identifiers')

    def to_map(self):
        result = {}
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.logical_resource_ids is not None:
            result['LogicalResourceIds'] = self.logical_resource_ids
        if self.resource_identifiers is not None:
            result['ResourceIdentifiers'] = self.resource_identifiers
        return result

    def from_map(self, map={}):
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('LogicalResourceIds') is not None:
            self.logical_resource_ids = map.get('LogicalResourceIds')
        if map.get('ResourceIdentifiers') is not None:
            self.resource_identifiers = map.get('ResourceIdentifiers')
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, next_token=None, key=None):
        self.region_id = region_id      # type: str
        self.resource_type = resource_type  # type: str
        self.next_token = next_token    # type: str
        self.key = key                  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.key, 'key')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        if map.get('Key') is not None:
            self.key = map.get('Key')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, values=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.values = values            # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.values, 'values')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        if map.get('Values') is not None:
            self.values = map.get('Values')
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, next_token=None):
        self.region_id = region_id      # type: str
        self.resource_type = resource_type  # type: str
        self.next_token = next_token    # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, keys=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.keys = keys                # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.keys, 'keys')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        if map.get('Keys') is not None:
            self.keys = map.get('Keys')
        return self


class SetDeletionProtectionRequest(TeaModel):
    def __init__(self, stack_id=None, deletion_protection=None, region_id=None):
        self.stack_id = stack_id        # type: str
        self.deletion_protection = deletion_protection  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.deletion_protection, 'deletion_protection')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('DeletionProtection') is not None:
            self.deletion_protection = map.get('DeletionProtection')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        return self


class SetDeletionProtectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class UpdateStackTemplateByResourcesRequest(TeaModel):
    def __init__(self, stack_id=None, dry_run=None, region_id=None, client_token=None, template_format=None,
                 logical_resource_id=None):
        self.stack_id = stack_id        # type: str
        self.dry_run = dry_run          # type: bool
        self.region_id = region_id      # type: str
        self.client_token = client_token  # type: str
        self.template_format = template_format  # type: str
        self.logical_resource_id = logical_resource_id  # type: List[str]

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('DryRun') is not None:
            self.dry_run = map.get('DryRun')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('TemplateFormat') is not None:
            self.template_format = map.get('TemplateFormat')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        return self


class UpdateStackTemplateByResourcesResponse(TeaModel):
    def __init__(self, request_id=None, old_template_body=None, new_template_body=None):
        self.request_id = request_id    # type: str
        self.old_template_body = old_template_body  # type: str
        self.new_template_body = new_template_body  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.old_template_body, 'old_template_body')
        self.validate_required(self.new_template_body, 'new_template_body')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.old_template_body is not None:
            result['OldTemplateBody'] = self.old_template_body
        if self.new_template_body is not None:
            result['NewTemplateBody'] = self.new_template_body
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('OldTemplateBody') is not None:
            self.old_template_body = map.get('OldTemplateBody')
        if map.get('NewTemplateBody') is not None:
            self.new_template_body = map.get('NewTemplateBody')
        return self


class GetStackDriftDetectionStatusRequest(TeaModel):
    def __init__(self, region_id=None, drift_detection_id=None):
        self.region_id = region_id      # type: str
        self.drift_detection_id = drift_detection_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.drift_detection_id, 'drift_detection_id')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('DriftDetectionId') is not None:
            self.drift_detection_id = map.get('DriftDetectionId')
        return self


class GetStackDriftDetectionStatusResponse(TeaModel):
    def __init__(self, request_id=None, drift_detection_id=None, drift_detection_time=None,
                 drift_detection_status=None, drift_detection_status_reason=None, stack_drift_status=None, stack_id=None,
                 drifted_stack_resource_count=None):
        self.request_id = request_id    # type: str
        self.drift_detection_id = drift_detection_id  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.drift_detection_status = drift_detection_status  # type: str
        self.drift_detection_status_reason = drift_detection_status_reason  # type: str
        self.stack_drift_status = stack_drift_status  # type: str
        self.stack_id = stack_id        # type: str
        self.drifted_stack_resource_count = drifted_stack_resource_count  # type: int

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('DriftDetectionId') is not None:
            self.drift_detection_id = map.get('DriftDetectionId')
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        if map.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = map.get('DriftDetectionStatus')
        if map.get('DriftDetectionStatusReason') is not None:
            self.drift_detection_status_reason = map.get('DriftDetectionStatusReason')
        if map.get('StackDriftStatus') is not None:
            self.stack_drift_status = map.get('StackDriftStatus')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('DriftedStackResourceCount') is not None:
            self.drifted_stack_resource_count = map.get('DriftedStackResourceCount')
        return self


class DetectStackGroupDriftRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, stack_group_name=None, operation_preferences=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.operation_preferences = operation_preferences  # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = {}
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        return result

    def from_map(self, map={}):
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('OperationPreferences') is not None:
            self.operation_preferences = map.get('OperationPreferences')
        return self


class DetectStackGroupDriftShrinkRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, stack_group_name=None, operation_preferences_shrink=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.operation_preferences_shrink = operation_preferences_shrink  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = {}
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        return result

    def from_map(self, map={}):
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = map.get('OperationPreferences')
        return self


class DetectStackGroupDriftResponse(TeaModel):
    def __init__(self, request_id=None, operation_id=None):
        self.request_id = request_id    # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('OperationId') is not None:
            self.operation_id = map.get('OperationId')
        return self


class ListStackResourceDriftsRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, max_results=None, resource_drift_status=None, next_token=None):
        self.stack_id = stack_id        # type: str
        self.region_id = region_id      # type: str
        self.max_results = max_results  # type: int
        self.resource_drift_status = resource_drift_status  # type: List[str]
        self.next_token = next_token    # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('MaxResults') is not None:
            self.max_results = map.get('MaxResults')
        if map.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = map.get('ResourceDriftStatus')
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        return self


class ListStackResourceDriftsResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, resource_drifts=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.resource_drifts = resource_drifts  # type: List[ListStackResourceDriftsResponseResourceDrifts]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.resource_drifts, 'resource_drifts')
        if self.resource_drifts:
            for k in self.resource_drifts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ResourceDrifts'] = []
        if self.resource_drifts is not None:
            for k in self.resource_drifts:
                result['ResourceDrifts'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        self.resource_drifts = []
        if map.get('ResourceDrifts') is not None:
            for k in map.get('ResourceDrifts'):
                temp_model = ListStackResourceDriftsResponseResourceDrifts()
                self.resource_drifts.append(temp_model.from_map(k))
        return self


class ListStackResourceDriftsResponseResourceDriftsPropertyDifferences(TeaModel):
    def __init__(self, property_path=None, actual_value=None, expected_value=None, difference_type=None):
        self.property_path = property_path  # type: str
        self.actual_value = actual_value  # type: str
        self.expected_value = expected_value  # type: str
        self.difference_type = difference_type  # type: str

    def validate(self):
        self.validate_required(self.property_path, 'property_path')
        self.validate_required(self.actual_value, 'actual_value')
        self.validate_required(self.expected_value, 'expected_value')
        self.validate_required(self.difference_type, 'difference_type')

    def to_map(self):
        result = {}
        if self.property_path is not None:
            result['PropertyPath'] = self.property_path
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.expected_value is not None:
            result['ExpectedValue'] = self.expected_value
        if self.difference_type is not None:
            result['DifferenceType'] = self.difference_type
        return result

    def from_map(self, map={}):
        if map.get('PropertyPath') is not None:
            self.property_path = map.get('PropertyPath')
        if map.get('ActualValue') is not None:
            self.actual_value = map.get('ActualValue')
        if map.get('ExpectedValue') is not None:
            self.expected_value = map.get('ExpectedValue')
        if map.get('DifferenceType') is not None:
            self.difference_type = map.get('DifferenceType')
        return self


class ListStackResourceDriftsResponseResourceDrifts(TeaModel):
    def __init__(self, drift_detection_time=None, resource_drift_status=None, stack_id=None, resource_type=None,
                 physical_resource_id=None, logical_resource_id=None, actual_properties=None, expected_properties=None,
                 property_differences=None):
        self.drift_detection_time = drift_detection_time  # type: str
        self.resource_drift_status = resource_drift_status  # type: str
        self.stack_id = stack_id        # type: str
        self.resource_type = resource_type  # type: str
        self.physical_resource_id = physical_resource_id  # type: str
        self.logical_resource_id = logical_resource_id  # type: str
        self.actual_properties = actual_properties  # type: str
        self.expected_properties = expected_properties  # type: str
        self.property_differences = property_differences  # type: List[ListStackResourceDriftsResponseResourceDriftsPropertyDifferences]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        if map.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = map.get('ResourceDriftStatus')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('PhysicalResourceId') is not None:
            self.physical_resource_id = map.get('PhysicalResourceId')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        if map.get('ActualProperties') is not None:
            self.actual_properties = map.get('ActualProperties')
        if map.get('ExpectedProperties') is not None:
            self.expected_properties = map.get('ExpectedProperties')
        self.property_differences = []
        if map.get('PropertyDifferences') is not None:
            for k in map.get('PropertyDifferences'):
                temp_model = ListStackResourceDriftsResponseResourceDriftsPropertyDifferences()
                self.property_differences.append(temp_model.from_map(k))
        return self


class DetectStackResourceDriftRequest(TeaModel):
    def __init__(self, stack_id=None, client_token=None, region_id=None, logical_resource_id=None):
        self.stack_id = stack_id        # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.logical_resource_id = logical_resource_id  # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')

    def to_map(self):
        result = {}
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        return result

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        return self


class DetectStackResourceDriftResponse(TeaModel):
    def __init__(self, request_id=None, drift_detection_time=None, resource_drift_status=None, stack_id=None,
                 resource_type=None, physical_resource_id=None, logical_resource_id=None, actual_properties=None,
                 expected_properties=None, property_differences=None):
        self.request_id = request_id    # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.resource_drift_status = resource_drift_status  # type: str
        self.stack_id = stack_id        # type: str
        self.resource_type = resource_type  # type: str
        self.physical_resource_id = physical_resource_id  # type: str
        self.logical_resource_id = logical_resource_id  # type: str
        self.actual_properties = actual_properties  # type: str
        self.expected_properties = expected_properties  # type: str
        self.property_differences = property_differences  # type: List[DetectStackResourceDriftResponsePropertyDifferences]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        if map.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = map.get('ResourceDriftStatus')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('PhysicalResourceId') is not None:
            self.physical_resource_id = map.get('PhysicalResourceId')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        if map.get('ActualProperties') is not None:
            self.actual_properties = map.get('ActualProperties')
        if map.get('ExpectedProperties') is not None:
            self.expected_properties = map.get('ExpectedProperties')
        self.property_differences = []
        if map.get('PropertyDifferences') is not None:
            for k in map.get('PropertyDifferences'):
                temp_model = DetectStackResourceDriftResponsePropertyDifferences()
                self.property_differences.append(temp_model.from_map(k))
        return self


class DetectStackResourceDriftResponsePropertyDifferences(TeaModel):
    def __init__(self, property_path=None, actual_value=None, expected_value=None, difference_type=None):
        self.property_path = property_path  # type: str
        self.actual_value = actual_value  # type: str
        self.expected_value = expected_value  # type: str
        self.difference_type = difference_type  # type: str

    def validate(self):
        self.validate_required(self.property_path, 'property_path')
        self.validate_required(self.actual_value, 'actual_value')
        self.validate_required(self.expected_value, 'expected_value')
        self.validate_required(self.difference_type, 'difference_type')

    def to_map(self):
        result = {}
        if self.property_path is not None:
            result['PropertyPath'] = self.property_path
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.expected_value is not None:
            result['ExpectedValue'] = self.expected_value
        if self.difference_type is not None:
            result['DifferenceType'] = self.difference_type
        return result

    def from_map(self, map={}):
        if map.get('PropertyPath') is not None:
            self.property_path = map.get('PropertyPath')
        if map.get('ActualValue') is not None:
            self.actual_value = map.get('ActualValue')
        if map.get('ExpectedValue') is not None:
            self.expected_value = map.get('ExpectedValue')
        if map.get('DifferenceType') is not None:
            self.difference_type = map.get('DifferenceType')
        return self


class DetectStackDriftRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, logical_resource_id=None, client_token=None):
        self.stack_id = stack_id        # type: str
        self.region_id = region_id      # type: str
        self.logical_resource_id = logical_resource_id  # type: List[str]
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        return self


class DetectStackDriftResponse(TeaModel):
    def __init__(self, request_id=None, drift_detection_id=None):
        self.request_id = request_id    # type: str
        self.drift_detection_id = drift_detection_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.drift_detection_id, 'drift_detection_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('DriftDetectionId') is not None:
            self.drift_detection_id = map.get('DriftDetectionId')
        return self


class UpdateStackInstancesRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, parameter_overrides=None, account_ids=None,
                 region_ids=None, client_token=None, operation_description=None, operation_preferences=None,
                 timeout_in_minutes=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.parameter_overrides = parameter_overrides  # type: List[UpdateStackInstancesRequestParameterOverrides]
        self.account_ids = account_ids  # type: Dict[str, Any]
        self.region_ids = region_ids    # type: Dict[str, Any]
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences = operation_preferences  # type: Dict[str, Any]
        self.timeout_in_minutes = timeout_in_minutes  # type: int

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        self.parameter_overrides = []
        if map.get('ParameterOverrides') is not None:
            for k in map.get('ParameterOverrides'):
                temp_model = UpdateStackInstancesRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if map.get('AccountIds') is not None:
            self.account_ids = map.get('AccountIds')
        if map.get('RegionIds') is not None:
            self.region_ids = map.get('RegionIds')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('OperationDescription') is not None:
            self.operation_description = map.get('OperationDescription')
        if map.get('OperationPreferences') is not None:
            self.operation_preferences = map.get('OperationPreferences')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        return self


class UpdateStackInstancesRequestParameterOverrides(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class UpdateStackInstancesShrinkRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, parameter_overrides=None, account_ids_shrink=None,
                 region_ids_shrink=None, client_token=None, operation_description=None, operation_preferences_shrink=None,
                 timeout_in_minutes=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.parameter_overrides = parameter_overrides  # type: List[UpdateStackInstancesShrinkRequestParameterOverrides]
        self.account_ids_shrink = account_ids_shrink  # type: str
        self.region_ids_shrink = region_ids_shrink  # type: str
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences_shrink = operation_preferences_shrink  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        self.parameter_overrides = []
        if map.get('ParameterOverrides') is not None:
            for k in map.get('ParameterOverrides'):
                temp_model = UpdateStackInstancesShrinkRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if map.get('AccountIds') is not None:
            self.account_ids_shrink = map.get('AccountIds')
        if map.get('RegionIds') is not None:
            self.region_ids_shrink = map.get('RegionIds')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('OperationDescription') is not None:
            self.operation_description = map.get('OperationDescription')
        if map.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = map.get('OperationPreferences')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        return self


class UpdateStackInstancesShrinkRequestParameterOverrides(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class UpdateStackInstancesResponse(TeaModel):
    def __init__(self, request_id=None, operation_id=None):
        self.request_id = request_id    # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('OperationId') is not None:
            self.operation_id = map.get('OperationId')
        return self


class ListStackGroupOperationsRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, page_size=None, page_number=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        return self


class ListStackGroupOperationsResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None,
                 stack_group_operations=None):
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.stack_group_operations = stack_group_operations  # type: List[ListStackGroupOperationsResponseStackGroupOperations]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.stack_group_operations = []
        if map.get('StackGroupOperations') is not None:
            for k in map.get('StackGroupOperations'):
                temp_model = ListStackGroupOperationsResponseStackGroupOperations()
                self.stack_group_operations.append(temp_model.from_map(k))
        return self


class ListStackGroupOperationsResponseStackGroupOperations(TeaModel):
    def __init__(self, stack_group_name=None, stack_group_id=None, operation_id=None, operation_description=None,
                 create_time=None, end_time=None, action=None, status=None):
        self.stack_group_name = stack_group_name  # type: str
        self.stack_group_id = stack_group_id  # type: str
        self.operation_id = operation_id  # type: str
        self.operation_description = operation_description  # type: str
        self.create_time = create_time  # type: str
        self.end_time = end_time        # type: str
        self.action = action            # type: str
        self.status = status            # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('StackGroupId') is not None:
            self.stack_group_id = map.get('StackGroupId')
        if map.get('OperationId') is not None:
            self.operation_id = map.get('OperationId')
        if map.get('OperationDescription') is not None:
            self.operation_description = map.get('OperationDescription')
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Action') is not None:
            self.action = map.get('Action')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class GetStackGroupRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        return self


class GetStackGroupResponse(TeaModel):
    def __init__(self, request_id=None, stack_group=None):
        self.request_id = request_id    # type: str
        self.stack_group = stack_group  # type: GetStackGroupResponseStackGroup

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_group, 'stack_group')
        if self.stack_group:
            self.stack_group.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_group is not None:
            result['StackGroup'] = self.stack_group.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StackGroup') is not None:
            temp_model = GetStackGroupResponseStackGroup()
            self.stack_group = temp_model.from_map(map['StackGroup'])
        return self


class GetStackGroupResponseStackGroupParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = {}
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, map={}):
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        return self


class GetStackGroupResponseStackGroupStackGroupDriftDetectionDetail(TeaModel):
    def __init__(self, drift_detection_time=None, stack_group_drift_status=None, drift_detection_status=None,
                 drifted_stack_instances_count=None, failed_stack_instances_count=None, cancelled_stack_instances_count=None,
                 in_progress_stack_instances_count=None, in_sync_stack_instances_count=None, total_stack_instances_count=None):
        self.drift_detection_time = drift_detection_time  # type: str
        self.stack_group_drift_status = stack_group_drift_status  # type: str
        self.drift_detection_status = drift_detection_status  # type: str
        self.drifted_stack_instances_count = drifted_stack_instances_count  # type: int
        self.failed_stack_instances_count = failed_stack_instances_count  # type: int
        self.cancelled_stack_instances_count = cancelled_stack_instances_count  # type: int
        self.in_progress_stack_instances_count = in_progress_stack_instances_count  # type: int
        self.in_sync_stack_instances_count = in_sync_stack_instances_count  # type: int
        self.total_stack_instances_count = total_stack_instances_count  # type: int

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        if map.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = map.get('StackGroupDriftStatus')
        if map.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = map.get('DriftDetectionStatus')
        if map.get('DriftedStackInstancesCount') is not None:
            self.drifted_stack_instances_count = map.get('DriftedStackInstancesCount')
        if map.get('FailedStackInstancesCount') is not None:
            self.failed_stack_instances_count = map.get('FailedStackInstancesCount')
        if map.get('CancelledStackInstancesCount') is not None:
            self.cancelled_stack_instances_count = map.get('CancelledStackInstancesCount')
        if map.get('InProgressStackInstancesCount') is not None:
            self.in_progress_stack_instances_count = map.get('InProgressStackInstancesCount')
        if map.get('InSyncStackInstancesCount') is not None:
            self.in_sync_stack_instances_count = map.get('InSyncStackInstancesCount')
        if map.get('TotalStackInstancesCount') is not None:
            self.total_stack_instances_count = map.get('TotalStackInstancesCount')
        return self


class GetStackGroupResponseStackGroup(TeaModel):
    def __init__(self, stack_group_name=None, stack_group_id=None, status=None, description=None,
                 template_body=None, execution_role_name=None, administration_role_name=None, parameters=None,
                 stack_group_drift_detection_detail=None):
        self.stack_group_name = stack_group_name  # type: str
        self.stack_group_id = stack_group_id  # type: str
        self.status = status            # type: str
        self.description = description  # type: str
        self.template_body = template_body  # type: str
        self.execution_role_name = execution_role_name  # type: str
        self.administration_role_name = administration_role_name  # type: str
        self.parameters = parameters    # type: List[GetStackGroupResponseStackGroupParameters]
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail  # type: GetStackGroupResponseStackGroupStackGroupDriftDetectionDetail

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('StackGroupId') is not None:
            self.stack_group_id = map.get('StackGroupId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('ExecutionRoleName') is not None:
            self.execution_role_name = map.get('ExecutionRoleName')
        if map.get('AdministrationRoleName') is not None:
            self.administration_role_name = map.get('AdministrationRoleName')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = GetStackGroupResponseStackGroupParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('StackGroupDriftDetectionDetail') is not None:
            temp_model = GetStackGroupResponseStackGroupStackGroupDriftDetectionDetail()
            self.stack_group_drift_detection_detail = temp_model.from_map(map['StackGroupDriftDetectionDetail'])
        return self


class GetStackGroupOperationRequest(TeaModel):
    def __init__(self, region_id=None, operation_id=None):
        self.region_id = region_id      # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('OperationId') is not None:
            self.operation_id = map.get('OperationId')
        return self


class GetStackGroupOperationResponse(TeaModel):
    def __init__(self, request_id=None, stack_group_operation=None):
        self.request_id = request_id    # type: str
        self.stack_group_operation = stack_group_operation  # type: GetStackGroupOperationResponseStackGroupOperation

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_group_operation, 'stack_group_operation')
        if self.stack_group_operation:
            self.stack_group_operation.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_group_operation is not None:
            result['StackGroupOperation'] = self.stack_group_operation.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StackGroupOperation') is not None:
            temp_model = GetStackGroupOperationResponseStackGroupOperation()
            self.stack_group_operation = temp_model.from_map(map['StackGroupOperation'])
        return self


class GetStackGroupOperationResponseStackGroupOperationOperationPreferences(TeaModel):
    def __init__(self, failure_tolerance_count=None, failure_tolerance_percentage=None, max_concurrent_count=None,
                 max_concurrent_percentage=None, region_ids_order=None):
        self.failure_tolerance_count = failure_tolerance_count  # type: int
        self.failure_tolerance_percentage = failure_tolerance_percentage  # type: int
        self.max_concurrent_count = max_concurrent_count  # type: int
        self.max_concurrent_percentage = max_concurrent_percentage  # type: int
        self.region_ids_order = region_ids_order  # type: List[str]

    def validate(self):
        self.validate_required(self.failure_tolerance_count, 'failure_tolerance_count')
        self.validate_required(self.failure_tolerance_percentage, 'failure_tolerance_percentage')
        self.validate_required(self.max_concurrent_count, 'max_concurrent_count')
        self.validate_required(self.max_concurrent_percentage, 'max_concurrent_percentage')
        self.validate_required(self.region_ids_order, 'region_ids_order')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('FailureToleranceCount') is not None:
            self.failure_tolerance_count = map.get('FailureToleranceCount')
        if map.get('FailureTolerancePercentage') is not None:
            self.failure_tolerance_percentage = map.get('FailureTolerancePercentage')
        if map.get('MaxConcurrentCount') is not None:
            self.max_concurrent_count = map.get('MaxConcurrentCount')
        if map.get('MaxConcurrentPercentage') is not None:
            self.max_concurrent_percentage = map.get('MaxConcurrentPercentage')
        if map.get('RegionIdsOrder') is not None:
            self.region_ids_order = map.get('RegionIdsOrder')
        return self


class GetStackGroupOperationResponseStackGroupOperationStackGroupDriftDetectionDetail(TeaModel):
    def __init__(self, drift_detection_time=None, stack_group_drift_status=None, drift_detection_status=None,
                 drifted_stack_instances_count=None, failed_stack_instances_count=None, cancelled_stack_instances_count=None,
                 in_progress_stack_instances_count=None, in_sync_stack_instances_count=None, total_stack_instances_count=None):
        self.drift_detection_time = drift_detection_time  # type: str
        self.stack_group_drift_status = stack_group_drift_status  # type: str
        self.drift_detection_status = drift_detection_status  # type: str
        self.drifted_stack_instances_count = drifted_stack_instances_count  # type: int
        self.failed_stack_instances_count = failed_stack_instances_count  # type: int
        self.cancelled_stack_instances_count = cancelled_stack_instances_count  # type: int
        self.in_progress_stack_instances_count = in_progress_stack_instances_count  # type: int
        self.in_sync_stack_instances_count = in_sync_stack_instances_count  # type: int
        self.total_stack_instances_count = total_stack_instances_count  # type: int

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        if map.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = map.get('StackGroupDriftStatus')
        if map.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = map.get('DriftDetectionStatus')
        if map.get('DriftedStackInstancesCount') is not None:
            self.drifted_stack_instances_count = map.get('DriftedStackInstancesCount')
        if map.get('FailedStackInstancesCount') is not None:
            self.failed_stack_instances_count = map.get('FailedStackInstancesCount')
        if map.get('CancelledStackInstancesCount') is not None:
            self.cancelled_stack_instances_count = map.get('CancelledStackInstancesCount')
        if map.get('InProgressStackInstancesCount') is not None:
            self.in_progress_stack_instances_count = map.get('InProgressStackInstancesCount')
        if map.get('InSyncStackInstancesCount') is not None:
            self.in_sync_stack_instances_count = map.get('InSyncStackInstancesCount')
        if map.get('TotalStackInstancesCount') is not None:
            self.total_stack_instances_count = map.get('TotalStackInstancesCount')
        return self


class GetStackGroupOperationResponseStackGroupOperation(TeaModel):
    def __init__(self, stack_group_name=None, stack_group_id=None, operation_id=None, operation_description=None,
                 create_time=None, end_time=None, action=None, status=None, retain_stacks=None, administrator_role_name=None,
                 execution_role_name=None, operation_preferences=None, stack_group_drift_detection_detail=None):
        self.stack_group_name = stack_group_name  # type: str
        self.stack_group_id = stack_group_id  # type: str
        self.operation_id = operation_id  # type: str
        self.operation_description = operation_description  # type: str
        self.create_time = create_time  # type: str
        self.end_time = end_time        # type: str
        self.action = action            # type: str
        self.status = status            # type: str
        self.retain_stacks = retain_stacks  # type: bool
        self.administrator_role_name = administrator_role_name  # type: str
        self.execution_role_name = execution_role_name  # type: str
        self.operation_preferences = operation_preferences  # type: GetStackGroupOperationResponseStackGroupOperationOperationPreferences
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail  # type: GetStackGroupOperationResponseStackGroupOperationStackGroupDriftDetectionDetail

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('StackGroupId') is not None:
            self.stack_group_id = map.get('StackGroupId')
        if map.get('OperationId') is not None:
            self.operation_id = map.get('OperationId')
        if map.get('OperationDescription') is not None:
            self.operation_description = map.get('OperationDescription')
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Action') is not None:
            self.action = map.get('Action')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('RetainStacks') is not None:
            self.retain_stacks = map.get('RetainStacks')
        if map.get('AdministratorRoleName') is not None:
            self.administrator_role_name = map.get('AdministratorRoleName')
        if map.get('ExecutionRoleName') is not None:
            self.execution_role_name = map.get('ExecutionRoleName')
        if map.get('OperationPreferences') is not None:
            temp_model = GetStackGroupOperationResponseStackGroupOperationOperationPreferences()
            self.operation_preferences = temp_model.from_map(map['OperationPreferences'])
        if map.get('StackGroupDriftDetectionDetail') is not None:
            temp_model = GetStackGroupOperationResponseStackGroupOperationStackGroupDriftDetectionDetail()
            self.stack_group_drift_detection_detail = temp_model.from_map(map['StackGroupDriftDetectionDetail'])
        return self


class ListStackGroupsRequest(TeaModel):
    def __init__(self, region_id=None, status=None, page_size=None, page_number=None):
        self.region_id = region_id      # type: str
        self.status = status            # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        return self


class ListStackGroupsResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, stack_groups=None):
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.stack_groups = stack_groups  # type: List[ListStackGroupsResponseStackGroups]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.stack_groups = []
        if map.get('StackGroups') is not None:
            for k in map.get('StackGroups'):
                temp_model = ListStackGroupsResponseStackGroups()
                self.stack_groups.append(temp_model.from_map(k))
        return self


class ListStackGroupsResponseStackGroups(TeaModel):
    def __init__(self, stack_group_name=None, stack_group_id=None, status=None, description=None,
                 drift_detection_time=None, stack_group_drift_status=None):
        self.stack_group_name = stack_group_name  # type: str
        self.stack_group_id = stack_group_id  # type: str
        self.status = status            # type: str
        self.description = description  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.stack_group_drift_status = stack_group_drift_status  # type: str

    def validate(self):
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.stack_group_id, 'stack_group_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.description, 'description')
        self.validate_required(self.drift_detection_time, 'drift_detection_time')
        self.validate_required(self.stack_group_drift_status, 'stack_group_drift_status')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('StackGroupId') is not None:
            self.stack_group_id = map.get('StackGroupId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        if map.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = map.get('StackGroupDriftStatus')
        return self


class CreateStackInstancesRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, parameter_overrides=None, account_ids=None,
                 region_ids=None, client_token=None, operation_description=None, operation_preferences=None,
                 timeout_in_minutes=None, disable_rollback=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.parameter_overrides = parameter_overrides  # type: List[CreateStackInstancesRequestParameterOverrides]
        self.account_ids = account_ids  # type: Dict[str, Any]
        self.region_ids = region_ids    # type: Dict[str, Any]
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences = operation_preferences  # type: Dict[str, Any]
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.disable_rollback = disable_rollback  # type: bool

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        self.parameter_overrides = []
        if map.get('ParameterOverrides') is not None:
            for k in map.get('ParameterOverrides'):
                temp_model = CreateStackInstancesRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if map.get('AccountIds') is not None:
            self.account_ids = map.get('AccountIds')
        if map.get('RegionIds') is not None:
            self.region_ids = map.get('RegionIds')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('OperationDescription') is not None:
            self.operation_description = map.get('OperationDescription')
        if map.get('OperationPreferences') is not None:
            self.operation_preferences = map.get('OperationPreferences')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        if map.get('DisableRollback') is not None:
            self.disable_rollback = map.get('DisableRollback')
        return self


class CreateStackInstancesRequestParameterOverrides(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class CreateStackInstancesShrinkRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, parameter_overrides=None, account_ids_shrink=None,
                 region_ids_shrink=None, client_token=None, operation_description=None, operation_preferences_shrink=None,
                 timeout_in_minutes=None, disable_rollback=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.parameter_overrides = parameter_overrides  # type: List[CreateStackInstancesShrinkRequestParameterOverrides]
        self.account_ids_shrink = account_ids_shrink  # type: str
        self.region_ids_shrink = region_ids_shrink  # type: str
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences_shrink = operation_preferences_shrink  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.disable_rollback = disable_rollback  # type: bool

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        self.parameter_overrides = []
        if map.get('ParameterOverrides') is not None:
            for k in map.get('ParameterOverrides'):
                temp_model = CreateStackInstancesShrinkRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if map.get('AccountIds') is not None:
            self.account_ids_shrink = map.get('AccountIds')
        if map.get('RegionIds') is not None:
            self.region_ids_shrink = map.get('RegionIds')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('OperationDescription') is not None:
            self.operation_description = map.get('OperationDescription')
        if map.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = map.get('OperationPreferences')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        if map.get('DisableRollback') is not None:
            self.disable_rollback = map.get('DisableRollback')
        return self


class CreateStackInstancesShrinkRequestParameterOverrides(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class CreateStackInstancesResponse(TeaModel):
    def __init__(self, request_id=None, operation_id=None):
        self.request_id = request_id    # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('OperationId') is not None:
            self.operation_id = map.get('OperationId')
        return self


class CreateStackGroupRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, description=None, parameters=None, template_body=None,
                 template_url=None, client_token=None, administration_role_name=None, execution_role_name=None,
                 template_id=None, template_version=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.description = description  # type: str
        self.parameters = parameters    # type: List[CreateStackGroupRequestParameters]
        self.template_body = template_body  # type: str
        self.template_url = template_url  # type: str
        self.client_token = client_token  # type: str
        self.administration_role_name = administration_role_name  # type: str
        self.execution_role_name = execution_role_name  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = CreateStackGroupRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('AdministrationRoleName') is not None:
            self.administration_role_name = map.get('AdministrationRoleName')
        if map.get('ExecutionRoleName') is not None:
            self.execution_role_name = map.get('ExecutionRoleName')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        return self


class CreateStackGroupRequestParameters(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class CreateStackGroupResponse(TeaModel):
    def __init__(self, request_id=None, stack_group_id=None):
        self.request_id = request_id    # type: str
        self.stack_group_id = stack_group_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_group_id, 'stack_group_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StackGroupId') is not None:
            self.stack_group_id = map.get('StackGroupId')
        return self


class GetStackInstanceRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, stack_instance_account_id=None,
                 stack_instance_region_id=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.stack_instance_account_id = stack_instance_account_id  # type: str
        self.stack_instance_region_id = stack_instance_region_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.stack_instance_account_id, 'stack_instance_account_id')
        self.validate_required(self.stack_instance_region_id, 'stack_instance_region_id')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_instance_account_id is not None:
            result['StackInstanceAccountId'] = self.stack_instance_account_id
        if self.stack_instance_region_id is not None:
            result['StackInstanceRegionId'] = self.stack_instance_region_id
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('StackInstanceAccountId') is not None:
            self.stack_instance_account_id = map.get('StackInstanceAccountId')
        if map.get('StackInstanceRegionId') is not None:
            self.stack_instance_region_id = map.get('StackInstanceRegionId')
        return self


class GetStackInstanceResponse(TeaModel):
    def __init__(self, request_id=None, stack_instance=None):
        self.request_id = request_id    # type: str
        self.stack_instance = stack_instance  # type: GetStackInstanceResponseStackInstance

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_instance, 'stack_instance')
        if self.stack_instance:
            self.stack_instance.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_instance is not None:
            result['StackInstance'] = self.stack_instance.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StackInstance') is not None:
            temp_model = GetStackInstanceResponseStackInstance()
            self.stack_instance = temp_model.from_map(map['StackInstance'])
        return self


class GetStackInstanceResponseStackInstanceParameterOverrides(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = {}
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, map={}):
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        return self


class GetStackInstanceResponseStackInstance(TeaModel):
    def __init__(self, stack_group_name=None, stack_group_id=None, stack_id=None, account_id=None, region_id=None,
                 status=None, status_reason=None, stack_drift_status=None, drift_detection_time=None,
                 parameter_overrides=None):
        self.stack_group_name = stack_group_name  # type: str
        self.stack_group_id = stack_group_id  # type: str
        self.stack_id = stack_id        # type: str
        self.account_id = account_id    # type: str
        self.region_id = region_id      # type: str
        self.status = status            # type: str
        self.status_reason = status_reason  # type: str
        self.stack_drift_status = stack_drift_status  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.parameter_overrides = parameter_overrides  # type: List[GetStackInstanceResponseStackInstanceParameterOverrides]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('StackGroupId') is not None:
            self.stack_group_id = map.get('StackGroupId')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('AccountId') is not None:
            self.account_id = map.get('AccountId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('StatusReason') is not None:
            self.status_reason = map.get('StatusReason')
        if map.get('StackDriftStatus') is not None:
            self.stack_drift_status = map.get('StackDriftStatus')
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        self.parameter_overrides = []
        if map.get('ParameterOverrides') is not None:
            for k in map.get('ParameterOverrides'):
                temp_model = GetStackInstanceResponseStackInstanceParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        return self


class UpdateStackGroupRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, description=None, parameters=None, account_ids=None,
                 region_ids=None, template_body=None, template_url=None, client_token=None, operation_description=None,
                 operation_preferences=None, administration_role_name=None, execution_role_name=None, template_id=None,
                 template_version=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.description = description  # type: str
        self.parameters = parameters    # type: List[UpdateStackGroupRequestParameters]
        self.account_ids = account_ids  # type: Dict[str, Any]
        self.region_ids = region_ids    # type: Dict[str, Any]
        self.template_body = template_body  # type: str
        self.template_url = template_url  # type: str
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences = operation_preferences  # type: Dict[str, Any]
        self.administration_role_name = administration_role_name  # type: str
        self.execution_role_name = execution_role_name  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = UpdateStackGroupRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('AccountIds') is not None:
            self.account_ids = map.get('AccountIds')
        if map.get('RegionIds') is not None:
            self.region_ids = map.get('RegionIds')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('OperationDescription') is not None:
            self.operation_description = map.get('OperationDescription')
        if map.get('OperationPreferences') is not None:
            self.operation_preferences = map.get('OperationPreferences')
        if map.get('AdministrationRoleName') is not None:
            self.administration_role_name = map.get('AdministrationRoleName')
        if map.get('ExecutionRoleName') is not None:
            self.execution_role_name = map.get('ExecutionRoleName')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        return self


class UpdateStackGroupRequestParameters(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class UpdateStackGroupShrinkRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, description=None, parameters=None,
                 account_ids_shrink=None, region_ids_shrink=None, template_body=None, template_url=None, client_token=None,
                 operation_description=None, operation_preferences_shrink=None, administration_role_name=None, execution_role_name=None,
                 template_id=None, template_version=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.description = description  # type: str
        self.parameters = parameters    # type: List[UpdateStackGroupShrinkRequestParameters]
        self.account_ids_shrink = account_ids_shrink  # type: str
        self.region_ids_shrink = region_ids_shrink  # type: str
        self.template_body = template_body  # type: str
        self.template_url = template_url  # type: str
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences_shrink = operation_preferences_shrink  # type: str
        self.administration_role_name = administration_role_name  # type: str
        self.execution_role_name = execution_role_name  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = UpdateStackGroupShrinkRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('AccountIds') is not None:
            self.account_ids_shrink = map.get('AccountIds')
        if map.get('RegionIds') is not None:
            self.region_ids_shrink = map.get('RegionIds')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('OperationDescription') is not None:
            self.operation_description = map.get('OperationDescription')
        if map.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = map.get('OperationPreferences')
        if map.get('AdministrationRoleName') is not None:
            self.administration_role_name = map.get('AdministrationRoleName')
        if map.get('ExecutionRoleName') is not None:
            self.execution_role_name = map.get('ExecutionRoleName')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        return self


class UpdateStackGroupShrinkRequestParameters(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class UpdateStackGroupResponse(TeaModel):
    def __init__(self, request_id=None, operation_id=None):
        self.request_id = request_id    # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('OperationId') is not None:
            self.operation_id = map.get('OperationId')
        return self


class ListStackInstancesRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, stack_instance_account_id=None,
                 stack_instance_region_id=None, page_size=None, page_number=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.stack_instance_account_id = stack_instance_account_id  # type: str
        self.stack_instance_region_id = stack_instance_region_id  # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('StackInstanceAccountId') is not None:
            self.stack_instance_account_id = map.get('StackInstanceAccountId')
        if map.get('StackInstanceRegionId') is not None:
            self.stack_instance_region_id = map.get('StackInstanceRegionId')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        return self


class ListStackInstancesResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, stack_instances=None):
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.stack_instances = stack_instances  # type: List[ListStackInstancesResponseStackInstances]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.stack_instances = []
        if map.get('StackInstances') is not None:
            for k in map.get('StackInstances'):
                temp_model = ListStackInstancesResponseStackInstances()
                self.stack_instances.append(temp_model.from_map(k))
        return self


class ListStackInstancesResponseStackInstances(TeaModel):
    def __init__(self, stack_group_name=None, stack_group_id=None, stack_id=None, account_id=None, region_id=None,
                 status=None, status_reason=None, stack_drift_status=None, drift_detection_time=None):
        self.stack_group_name = stack_group_name  # type: str
        self.stack_group_id = stack_group_id  # type: str
        self.stack_id = stack_id        # type: str
        self.account_id = account_id    # type: str
        self.region_id = region_id      # type: str
        self.status = status            # type: str
        self.status_reason = status_reason  # type: str
        self.stack_drift_status = stack_drift_status  # type: str
        self.drift_detection_time = drift_detection_time  # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('StackGroupId') is not None:
            self.stack_group_id = map.get('StackGroupId')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('AccountId') is not None:
            self.account_id = map.get('AccountId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('StatusReason') is not None:
            self.status_reason = map.get('StatusReason')
        if map.get('StackDriftStatus') is not None:
            self.stack_drift_status = map.get('StackDriftStatus')
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        return self


class ListStackGroupOperationResultsRequest(TeaModel):
    def __init__(self, region_id=None, operation_id=None, page_size=None, page_number=None):
        self.region_id = region_id      # type: str
        self.operation_id = operation_id  # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('OperationId') is not None:
            self.operation_id = map.get('OperationId')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        return self


class ListStackGroupOperationResultsResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None,
                 stack_group_operation_results=None):
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.stack_group_operation_results = stack_group_operation_results  # type: List[ListStackGroupOperationResultsResponseStackGroupOperationResults]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.stack_group_operation_results = []
        if map.get('StackGroupOperationResults') is not None:
            for k in map.get('StackGroupOperationResults'):
                temp_model = ListStackGroupOperationResultsResponseStackGroupOperationResults()
                self.stack_group_operation_results.append(temp_model.from_map(k))
        return self


class ListStackGroupOperationResultsResponseStackGroupOperationResults(TeaModel):
    def __init__(self, account_id=None, region_id=None, status=None, status_reason=None):
        self.account_id = account_id    # type: str
        self.region_id = region_id      # type: str
        self.status = status            # type: str
        self.status_reason = status_reason  # type: str

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.status_reason, 'status_reason')

    def to_map(self):
        result = {}
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, map={}):
        if map.get('AccountId') is not None:
            self.account_id = map.get('AccountId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('StatusReason') is not None:
            self.status_reason = map.get('StatusReason')
        return self


class StopStackGroupOperationRequest(TeaModel):
    def __init__(self, region_id=None, operation_id=None):
        self.region_id = region_id      # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('OperationId') is not None:
            self.operation_id = map.get('OperationId')
        return self


class StopStackGroupOperationResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DeleteStackGroupRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        return self


class DeleteStackGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DeleteStackInstancesRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, account_ids=None, region_ids=None, retain_stacks=None,
                 client_token=None, operation_description=None, operation_preferences=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.account_ids = account_ids  # type: Dict[str, Any]
        self.region_ids = region_ids    # type: Dict[str, Any]
        self.retain_stacks = retain_stacks  # type: bool
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences = operation_preferences  # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.account_ids, 'account_ids')
        self.validate_required(self.region_ids, 'region_ids')
        self.validate_required(self.retain_stacks, 'retain_stacks')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('AccountIds') is not None:
            self.account_ids = map.get('AccountIds')
        if map.get('RegionIds') is not None:
            self.region_ids = map.get('RegionIds')
        if map.get('RetainStacks') is not None:
            self.retain_stacks = map.get('RetainStacks')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('OperationDescription') is not None:
            self.operation_description = map.get('OperationDescription')
        if map.get('OperationPreferences') is not None:
            self.operation_preferences = map.get('OperationPreferences')
        return self


class DeleteStackInstancesShrinkRequest(TeaModel):
    def __init__(self, region_id=None, stack_group_name=None, account_ids_shrink=None, region_ids_shrink=None,
                 retain_stacks=None, client_token=None, operation_description=None, operation_preferences_shrink=None):
        self.region_id = region_id      # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.account_ids_shrink = account_ids_shrink  # type: str
        self.region_ids_shrink = region_ids_shrink  # type: str
        self.retain_stacks = retain_stacks  # type: bool
        self.client_token = client_token  # type: str
        self.operation_description = operation_description  # type: str
        self.operation_preferences_shrink = operation_preferences_shrink  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_group_name, 'stack_group_name')
        self.validate_required(self.account_ids_shrink, 'account_ids_shrink')
        self.validate_required(self.region_ids_shrink, 'region_ids_shrink')
        self.validate_required(self.retain_stacks, 'retain_stacks')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('AccountIds') is not None:
            self.account_ids_shrink = map.get('AccountIds')
        if map.get('RegionIds') is not None:
            self.region_ids_shrink = map.get('RegionIds')
        if map.get('RetainStacks') is not None:
            self.retain_stacks = map.get('RetainStacks')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('OperationDescription') is not None:
            self.operation_description = map.get('OperationDescription')
        if map.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = map.get('OperationPreferences')
        return self


class DeleteStackInstancesResponse(TeaModel):
    def __init__(self, request_id=None, operation_id=None):
        self.request_id = request_id    # type: str
        self.operation_id = operation_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.operation_id, 'operation_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('OperationId') is not None:
            self.operation_id = map.get('OperationId')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_id=None, resource_type=None, tag=None, next_token=None):
        self.region_id = region_id      # type: str
        self.resource_id = resource_id  # type: List[str]
        self.resource_type = resource_type  # type: str
        self.tag = tag                  # type: List[ListTagResourcesRequestTag]
        self.next_token = next_token    # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ResourceId') is not None:
            self.resource_id = map.get('ResourceId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('Key') is not None:
            self.key = map.get('Key')
        if map.get('Value') is not None:
            self.value = map.get('Value')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, tag_resources=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.tag_resources = tag_resources  # type: List[ListTagResourcesResponseTagResources]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.tag_resources, 'tag_resources')
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('NextToken') is not None:
            self.next_token = map.get('NextToken')
        self.tag_resources = []
        if map.get('TagResources') is not None:
            for k in map.get('TagResources'):
                temp_model = ListTagResourcesResponseTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseTagResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key          # type: str
        self.tag_value = tag_value      # type: str

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        result = {}
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, map={}):
        if map.get('ResourceId') is not None:
            self.resource_id = map.get('ResourceId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('TagKey') is not None:
            self.tag_key = map.get('TagKey')
        if map.get('TagValue') is not None:
            self.tag_value = map.get('TagValue')
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_id=None, resource_type=None, tag_key=None, all=None):
        self.region_id = region_id      # type: str
        self.resource_id = resource_id  # type: List[str]
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key          # type: List[str]
        self.all = all                  # type: bool

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ResourceId') is not None:
            self.resource_id = map.get('ResourceId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('TagKey') is not None:
            self.tag_key = map.get('TagKey')
        if map.get('All') is not None:
            self.all = map.get('All')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_id=None, resource_type=None, tag=None):
        self.region_id = region_id      # type: str
        self.resource_id = resource_id  # type: List[str]
        self.resource_type = resource_type  # type: str
        self.tag = tag                  # type: List[TagResourcesRequestTag]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ResourceId') is not None:
            self.resource_id = map.get('ResourceId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('Key') is not None:
            self.key = map.get('Key')
        if map.get('Value') is not None:
            self.value = map.get('Value')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = template_id  # type: str

    def validate(self):
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = {}
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, map={}):
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(self, template_url=None, template_name=None, description=None, template_body=None,
                 template_id=None):
        self.template_url = template_url  # type: str
        self.template_name = template_name  # type: str
        self.description = description  # type: str
        self.template_body = template_body  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('TemplateName') is not None:
            self.template_name = map.get('TemplateName')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id    # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, template_name=None, tag=None, share_type=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.template_name = template_name  # type: str
        self.tag = tag                  # type: List[ListTemplatesRequestTag]
        self.share_type = share_type    # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('TemplateName') is not None:
            self.template_name = map.get('TemplateName')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = ListTemplatesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if map.get('ShareType') is not None:
            self.share_type = map.get('ShareType')
        return self


class ListTemplatesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('Key') is not None:
            self.key = map.get('Key')
        if map.get('Value') is not None:
            self.value = map.get('Value')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, templates=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.templates = templates      # type: List[ListTemplatesResponseTemplates]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.templates = []
        if map.get('Templates') is not None:
            for k in map.get('Templates'):
                temp_model = ListTemplatesResponseTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListTemplatesResponseTemplates(TeaModel):
    def __init__(self, create_time=None, description=None, template_id=None, template_name=None, update_time=None,
                 template_version=None, share_type=None, owner_id=None, template_arn=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.update_time = update_time  # type: str
        self.template_version = template_version  # type: str
        self.share_type = share_type    # type: str
        self.owner_id = owner_id        # type: str
        self.template_arn = template_arn  # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateName') is not None:
            self.template_name = map.get('TemplateName')
        if map.get('UpdateTime') is not None:
            self.update_time = map.get('UpdateTime')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        if map.get('ShareType') is not None:
            self.share_type = map.get('ShareType')
        if map.get('OwnerId') is not None:
            self.owner_id = map.get('OwnerId')
        if map.get('TemplateARN') is not None:
            self.template_arn = map.get('TemplateARN')
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(self, template_url=None, description=None, template_body=None, template_name=None):
        self.template_url = template_url  # type: str
        self.description = description  # type: str
        self.template_body = template_body  # type: str
        self.template_name = template_name  # type: str

    def validate(self):
        self.validate_required(self.template_name, 'template_name')

    def to_map(self):
        result = {}
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.description is not None:
            result['Description'] = self.description
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, map={}):
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('TemplateName') is not None:
            self.template_name = map.get('TemplateName')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id    # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        return self


class CreateStackRequest(TeaModel):
    def __init__(self, disable_rollback=None, template_body=None, parameters=None, stack_policy_url=None,
                 timeout_in_minutes=None, stack_policy_body=None, stack_name=None, region_id=None, client_token=None,
                 template_url=None, notification_urls=None, ram_role_name=None, deletion_protection=None, create_option=None,
                 template_id=None, template_version=None):
        self.disable_rollback = disable_rollback  # type: bool
        self.template_body = template_body  # type: str
        self.parameters = parameters    # type: List[CreateStackRequestParameters]
        self.stack_policy_url = stack_policy_url  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.stack_policy_body = stack_policy_body  # type: str
        self.stack_name = stack_name    # type: str
        self.region_id = region_id      # type: str
        self.client_token = client_token  # type: str
        self.template_url = template_url  # type: str
        self.notification_urls = notification_urls  # type: List[str]
        self.ram_role_name = ram_role_name  # type: str
        self.deletion_protection = deletion_protection  # type: str
        self.create_option = create_option  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        self.validate_required(self.stack_name, 'stack_name')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
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
        return result

    def from_map(self, map={}):
        if map.get('DisableRollback') is not None:
            self.disable_rollback = map.get('DisableRollback')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = CreateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('StackPolicyURL') is not None:
            self.stack_policy_url = map.get('StackPolicyURL')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        if map.get('StackPolicyBody') is not None:
            self.stack_policy_body = map.get('StackPolicyBody')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('NotificationURLs') is not None:
            self.notification_urls = map.get('NotificationURLs')
        if map.get('RamRoleName') is not None:
            self.ram_role_name = map.get('RamRoleName')
        if map.get('DeletionProtection') is not None:
            self.deletion_protection = map.get('DeletionProtection')
        if map.get('CreateOption') is not None:
            self.create_option = map.get('CreateOption')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        return self


class CreateStackRequestParameters(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class CreateStackResponse(TeaModel):
    def __init__(self, request_id=None, stack_id=None):
        self.request_id = request_id    # type: str
        self.stack_id = stack_id        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_id, 'stack_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        return self


class GetStackRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, client_token=None):
        self.stack_id = stack_id        # type: str
        self.region_id = region_id      # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        return self


class GetStackResponse(TeaModel):
    def __init__(self, create_time=None, description=None, disable_rollback=None, region_id=None, request_id=None,
                 stack_id=None, stack_name=None, status=None, status_reason=None, template_description=None,
                 timeout_in_minutes=None, update_time=None, parent_stack_id=None, stack_drift_status=None, drift_detection_time=None,
                 ram_role_name=None, deletion_protection=None, root_stack_id=None, stack_type=None, parameters=None, outputs=None,
                 notification_urls=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.disable_rollback = disable_rollback  # type: bool
        self.region_id = region_id      # type: str
        self.request_id = request_id    # type: str
        self.stack_id = stack_id        # type: str
        self.stack_name = stack_name    # type: str
        self.status = status            # type: str
        self.status_reason = status_reason  # type: str
        self.template_description = template_description  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.update_time = update_time  # type: str
        self.parent_stack_id = parent_stack_id  # type: str
        self.stack_drift_status = stack_drift_status  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.ram_role_name = ram_role_name  # type: str
        self.deletion_protection = deletion_protection  # type: str
        self.root_stack_id = root_stack_id  # type: str
        self.stack_type = stack_type    # type: str
        self.parameters = parameters    # type: List[GetStackResponseParameters]
        self.outputs = outputs          # type: List[Dict[str, Any]]
        self.notification_urls = notification_urls  # type: List[str]

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
        self.validate_required(self.outputs, 'outputs')
        self.validate_required(self.notification_urls, 'notification_urls')

    def to_map(self):
        result = {}
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
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls
        return result

    def from_map(self, map={}):
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('DisableRollback') is not None:
            self.disable_rollback = map.get('DisableRollback')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('StatusReason') is not None:
            self.status_reason = map.get('StatusReason')
        if map.get('TemplateDescription') is not None:
            self.template_description = map.get('TemplateDescription')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        if map.get('UpdateTime') is not None:
            self.update_time = map.get('UpdateTime')
        if map.get('ParentStackId') is not None:
            self.parent_stack_id = map.get('ParentStackId')
        if map.get('StackDriftStatus') is not None:
            self.stack_drift_status = map.get('StackDriftStatus')
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        if map.get('RamRoleName') is not None:
            self.ram_role_name = map.get('RamRoleName')
        if map.get('DeletionProtection') is not None:
            self.deletion_protection = map.get('DeletionProtection')
        if map.get('RootStackId') is not None:
            self.root_stack_id = map.get('RootStackId')
        if map.get('StackType') is not None:
            self.stack_type = map.get('StackType')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = GetStackResponseParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('Outputs') is not None:
            self.outputs = map.get('Outputs')
        if map.get('NotificationURLs') is not None:
            self.notification_urls = map.get('NotificationURLs')
        return self


class GetStackResponseParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = {}
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, map={}):
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        return self


class DeleteStackRequest(TeaModel):
    def __init__(self, stack_id=None, retain_all_resources=None, region_id=None, retain_resources=None,
                 ram_role_name=None):
        self.stack_id = stack_id        # type: str
        self.retain_all_resources = retain_all_resources  # type: bool
        self.region_id = region_id      # type: str
        self.retain_resources = retain_resources  # type: List[str]
        self.ram_role_name = ram_role_name  # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('RetainAllResources') is not None:
            self.retain_all_resources = map.get('RetainAllResources')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('RetainResources') is not None:
            self.retain_resources = map.get('RetainResources')
        if map.get('RamRoleName') is not None:
            self.ram_role_name = map.get('RamRoleName')
        return self


class DeleteStackResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class UpdateStackRequest(TeaModel):
    def __init__(self, stack_id=None, client_token=None, stack_policy_during_update_body=None,
                 timeout_in_minutes=None, template_body=None, parameters=None, stack_policy_url=None,
                 stack_policy_during_update_url=None, stack_policy_body=None, use_previous_parameters=None, region_id=None, disable_rollback=None,
                 template_url=None, ram_role_name=None, replacement_option=None, template_id=None, template_version=None):
        self.stack_id = stack_id        # type: str
        self.client_token = client_token  # type: str
        self.stack_policy_during_update_body = stack_policy_during_update_body  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.template_body = template_body  # type: str
        self.parameters = parameters    # type: List[UpdateStackRequestParameters]
        self.stack_policy_url = stack_policy_url  # type: str
        self.stack_policy_during_update_url = stack_policy_during_update_url  # type: str
        self.stack_policy_body = stack_policy_body  # type: str
        self.use_previous_parameters = use_previous_parameters  # type: bool
        self.region_id = region_id      # type: str
        self.disable_rollback = disable_rollback  # type: bool
        self.template_url = template_url  # type: str
        self.ram_role_name = ram_role_name  # type: str
        self.replacement_option = replacement_option  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
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
        return result

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('StackPolicyDuringUpdateBody') is not None:
            self.stack_policy_during_update_body = map.get('StackPolicyDuringUpdateBody')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = UpdateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('StackPolicyURL') is not None:
            self.stack_policy_url = map.get('StackPolicyURL')
        if map.get('StackPolicyDuringUpdateURL') is not None:
            self.stack_policy_during_update_url = map.get('StackPolicyDuringUpdateURL')
        if map.get('StackPolicyBody') is not None:
            self.stack_policy_body = map.get('StackPolicyBody')
        if map.get('UsePreviousParameters') is not None:
            self.use_previous_parameters = map.get('UsePreviousParameters')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('DisableRollback') is not None:
            self.disable_rollback = map.get('DisableRollback')
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('RamRoleName') is not None:
            self.ram_role_name = map.get('RamRoleName')
        if map.get('ReplacementOption') is not None:
            self.replacement_option = map.get('ReplacementOption')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        return self


class UpdateStackRequestParameters(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class UpdateStackResponse(TeaModel):
    def __init__(self, request_id=None, stack_id=None):
        self.request_id = request_id    # type: str
        self.stack_id = stack_id        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_id, 'stack_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        return self


class ListStacksRequest(TeaModel):
    def __init__(self, status=None, page_size=None, parent_stack_id=None, region_id=None, stack_name=None,
                 page_number=None, show_nested_stack=None, tag=None, stack_id=None):
        self.status = status            # type: List[str]
        self.page_size = page_size      # type: int
        self.parent_stack_id = parent_stack_id  # type: str
        self.region_id = region_id      # type: str
        self.stack_name = stack_name    # type: List[str]
        self.page_number = page_number  # type: int
        self.show_nested_stack = show_nested_stack  # type: bool
        self.tag = tag                  # type: List[ListStacksRequestTag]
        self.stack_id = stack_id        # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('ParentStackId') is not None:
            self.parent_stack_id = map.get('ParentStackId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('ShowNestedStack') is not None:
            self.show_nested_stack = map.get('ShowNestedStack')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = ListStacksRequestTag()
                self.tag.append(temp_model.from_map(k))
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        return self


class ListStacksRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('Key') is not None:
            self.key = map.get('Key')
        if map.get('Value') is not None:
            self.value = map.get('Value')
        return self


class ListStacksResponse(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, stacks=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.stacks = stacks            # type: List[ListStacksResponseStacks]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.stacks = []
        if map.get('Stacks') is not None:
            for k in map.get('Stacks'):
                temp_model = ListStacksResponseStacks()
                self.stacks.append(temp_model.from_map(k))
        return self


class ListStacksResponseStacks(TeaModel):
    def __init__(self, create_time=None, disable_rollback=None, region_id=None, stack_id=None, stack_name=None,
                 status=None, status_reason=None, timeout_in_minutes=None, parent_stack_id=None, update_time=None,
                 stack_drift_status=None, drift_detection_time=None, stack_type=None):
        self.create_time = create_time  # type: str
        self.disable_rollback = disable_rollback  # type: bool
        self.region_id = region_id      # type: str
        self.stack_id = stack_id        # type: str
        self.stack_name = stack_name    # type: str
        self.status = status            # type: str
        self.status_reason = status_reason  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.parent_stack_id = parent_stack_id  # type: str
        self.update_time = update_time  # type: str
        self.stack_drift_status = stack_drift_status  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.stack_type = stack_type    # type: str

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

    def to_map(self):
        result = {}
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
        return result

    def from_map(self, map={}):
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('DisableRollback') is not None:
            self.disable_rollback = map.get('DisableRollback')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('StatusReason') is not None:
            self.status_reason = map.get('StatusReason')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        if map.get('ParentStackId') is not None:
            self.parent_stack_id = map.get('ParentStackId')
        if map.get('UpdateTime') is not None:
            self.update_time = map.get('UpdateTime')
        if map.get('StackDriftStatus') is not None:
            self.stack_drift_status = map.get('StackDriftStatus')
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        if map.get('StackType') is not None:
            self.stack_type = map.get('StackType')
        return self


class PreviewStackRequest(TeaModel):
    def __init__(self, disable_rollback=None, timeout_in_minutes=None, parameters=None, template_body=None,
                 stack_policy_url=None, region_id=None, stack_policy_body=None, stack_name=None, client_token=None,
                 template_url=None, template_id=None, template_version=None):
        self.disable_rollback = disable_rollback  # type: bool
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.parameters = parameters    # type: List[PreviewStackRequestParameters]
        self.template_body = template_body  # type: str
        self.stack_policy_url = stack_policy_url  # type: str
        self.region_id = region_id      # type: str
        self.stack_policy_body = stack_policy_body  # type: str
        self.stack_name = stack_name    # type: str
        self.client_token = client_token  # type: str
        self.template_url = template_url  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.stack_name, 'stack_name')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('DisableRollback') is not None:
            self.disable_rollback = map.get('DisableRollback')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = PreviewStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('StackPolicyURL') is not None:
            self.stack_policy_url = map.get('StackPolicyURL')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackPolicyBody') is not None:
            self.stack_policy_body = map.get('StackPolicyBody')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        return self


class PreviewStackRequestParameters(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class PreviewStackResponse(TeaModel):
    def __init__(self, request_id=None, stack=None):
        self.request_id = request_id    # type: str
        self.stack = stack              # type: PreviewStackResponseStack

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack, 'stack')
        if self.stack:
            self.stack.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack is not None:
            result['Stack'] = self.stack.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Stack') is not None:
            temp_model = PreviewStackResponseStack()
            self.stack = temp_model.from_map(map['Stack'])
        return self


class PreviewStackResponseStackParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = {}
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, map={}):
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        return self


class PreviewStackResponseStackResources(TeaModel):
    def __init__(self, description=None, logical_resource_id=None, properties=None, resource_type=None, stack=None,
                 required_by=None):
        self.description = description  # type: str
        self.logical_resource_id = logical_resource_id  # type: str
        self.properties = properties    # type: Dict[str, Any]
        self.resource_type = resource_type  # type: str
        self.stack = stack              # type: Dict[str, Any]
        self.required_by = required_by  # type: List[str]

    def validate(self):
        self.validate_required(self.description, 'description')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')
        self.validate_required(self.properties, 'properties')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.stack, 'stack')
        self.validate_required(self.required_by, 'required_by')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        if map.get('Properties') is not None:
            self.properties = map.get('Properties')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('Stack') is not None:
            self.stack = map.get('Stack')
        if map.get('RequiredBy') is not None:
            self.required_by = map.get('RequiredBy')
        return self


class PreviewStackResponseStack(TeaModel):
    def __init__(self, description=None, disable_rollback=None, region_id=None, stack_name=None,
                 stack_policy_body=None, template_description=None, timeout_in_minutes=None, parameters=None, resources=None):
        self.description = description  # type: str
        self.disable_rollback = disable_rollback  # type: bool
        self.region_id = region_id      # type: str
        self.stack_name = stack_name    # type: str
        self.stack_policy_body = stack_policy_body  # type: Dict[str, Any]
        self.template_description = template_description  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.parameters = parameters    # type: List[PreviewStackResponseStackParameters]
        self.resources = resources      # type: List[PreviewStackResponseStackResources]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('DisableRollback') is not None:
            self.disable_rollback = map.get('DisableRollback')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('StackPolicyBody') is not None:
            self.stack_policy_body = map.get('StackPolicyBody')
        if map.get('TemplateDescription') is not None:
            self.template_description = map.get('TemplateDescription')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = PreviewStackResponseStackParameters()
                self.parameters.append(temp_model.from_map(k))
        self.resources = []
        if map.get('Resources') is not None:
            for k in map.get('Resources'):
                temp_model = PreviewStackResponseStackResources()
                self.resources.append(temp_model.from_map(k))
        return self


class GetTemplateEstimateCostRequest(TeaModel):
    def __init__(self, template_url=None, region_id=None, parameters=None, template_body=None, client_token=None,
                 template_id=None, template_version=None):
        self.template_url = template_url  # type: str
        self.region_id = region_id      # type: str
        self.parameters = parameters    # type: List[GetTemplateEstimateCostRequestParameters]
        self.template_body = template_body  # type: str
        self.client_token = client_token  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = GetTemplateEstimateCostRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        return self


class GetTemplateEstimateCostRequestParameters(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class GetTemplateEstimateCostResponse(TeaModel):
    def __init__(self, request_id=None, resources=None):
        self.request_id = request_id    # type: str
        self.resources = resources      # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resources, 'resources')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Resources') is not None:
            self.resources = map.get('Resources')
        return self


class CancelUpdateStackRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, cancel_type=None):
        self.stack_id = stack_id        # type: str
        self.region_id = region_id      # type: str
        self.cancel_type = cancel_type  # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cancel_type is not None:
            result['CancelType'] = self.cancel_type
        return result

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('CancelType') is not None:
            self.cancel_type = map.get('CancelType')
        return self


class CancelUpdateStackResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ContinueCreateStackRequest(TeaModel):
    def __init__(self, stack_id=None, recreating_resources=None, region_id=None, ram_role_name=None, mode=None,
                 template_body=None, template_url=None, parameters=None, dry_run=None, template_id=None, template_version=None):
        self.stack_id = stack_id        # type: str
        self.recreating_resources = recreating_resources  # type: List[str]
        self.region_id = region_id      # type: str
        self.ram_role_name = ram_role_name  # type: str
        self.mode = mode                # type: str
        self.template_body = template_body  # type: str
        self.template_url = template_url  # type: str
        self.parameters = parameters    # type: List[ContinueCreateStackRequestParameters]
        self.dry_run = dry_run          # type: bool
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('RecreatingResources') is not None:
            self.recreating_resources = map.get('RecreatingResources')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('RamRoleName') is not None:
            self.ram_role_name = map.get('RamRoleName')
        if map.get('Mode') is not None:
            self.mode = map.get('Mode')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = ContinueCreateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('DryRun') is not None:
            self.dry_run = map.get('DryRun')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        return self


class ContinueCreateStackRequestParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = {}
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, map={}):
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        return self


class ContinueCreateStackResponse(TeaModel):
    def __init__(self, request_id=None, stack_id=None):
        self.request_id = request_id    # type: str
        self.stack_id = stack_id        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_id, 'stack_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        return self


class SetStackPolicyRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, stack_policy_body=None, stack_policy_url=None):
        self.stack_id = stack_id        # type: str
        self.region_id = region_id      # type: str
        self.stack_policy_body = stack_policy_body  # type: str
        self.stack_policy_url = stack_policy_url  # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        return result

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackPolicyBody') is not None:
            self.stack_policy_body = map.get('StackPolicyBody')
        if map.get('StackPolicyURL') is not None:
            self.stack_policy_url = map.get('StackPolicyURL')
        return self


class SetStackPolicyResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class GetStackPolicyRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None):
        self.stack_id = stack_id        # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        return self


class GetStackPolicyResponse(TeaModel):
    def __init__(self, request_id=None, stack_policy_body=None):
        self.request_id = request_id    # type: str
        self.stack_policy_body = stack_policy_body  # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_policy_body, 'stack_policy_body')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StackPolicyBody') is not None:
            self.stack_policy_body = map.get('StackPolicyBody')
        return self


class ValidateTemplateRequest(TeaModel):
    def __init__(self, template_url=None, region_id=None, template_body=None):
        self.template_url = template_url  # type: str
        self.region_id = region_id      # type: str
        self.template_body = template_body  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        return result

    def from_map(self, map={}):
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        return self


class ValidateTemplateResponse(TeaModel):
    def __init__(self, description=None, request_id=None, parameters=None):
        self.description = description  # type: str
        self.request_id = request_id    # type: str
        self.parameters = parameters    # type: List[Dict[str, Any]]

    def validate(self):
        self.validate_required(self.description, 'description')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.parameters, 'parameters')

    def to_map(self):
        result = {}
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, map={}):
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Parameters') is not None:
            self.parameters = map.get('Parameters')
        return self


class GetTemplateRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None, change_set_id=None, template_id=None, template_version=None,
                 template_stage=None, include_permission=None, stack_group_name=None):
        self.stack_id = stack_id        # type: str
        self.region_id = region_id      # type: str
        self.change_set_id = change_set_id  # type: str
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str
        self.template_stage = template_stage  # type: str
        self.include_permission = include_permission  # type: str
        self.stack_group_name = stack_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ChangeSetId') is not None:
            self.change_set_id = map.get('ChangeSetId')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        if map.get('TemplateStage') is not None:
            self.template_stage = map.get('TemplateStage')
        if map.get('IncludePermission') is not None:
            self.include_permission = map.get('IncludePermission')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(self, request_id=None, template_body=None, stack_id=None, template_id=None, stack_group_name=None,
                 change_set_id=None, region_id=None, create_time=None, description=None, template_name=None, update_time=None,
                 template_version=None, share_type=None, owner_id=None, template_arn=None, permissions=None):
        self.request_id = request_id    # type: str
        self.template_body = template_body  # type: str
        self.stack_id = stack_id        # type: str
        self.template_id = template_id  # type: str
        self.stack_group_name = stack_group_name  # type: str
        self.change_set_id = change_set_id  # type: str
        self.region_id = region_id      # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.template_name = template_name  # type: str
        self.update_time = update_time  # type: str
        self.template_version = template_version  # type: str
        self.share_type = share_type    # type: str
        self.owner_id = owner_id        # type: str
        self.template_arn = template_arn  # type: str
        self.permissions = permissions  # type: List[GetTemplateResponsePermissions]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('StackGroupName') is not None:
            self.stack_group_name = map.get('StackGroupName')
        if map.get('ChangeSetId') is not None:
            self.change_set_id = map.get('ChangeSetId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('TemplateName') is not None:
            self.template_name = map.get('TemplateName')
        if map.get('UpdateTime') is not None:
            self.update_time = map.get('UpdateTime')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        if map.get('ShareType') is not None:
            self.share_type = map.get('ShareType')
        if map.get('OwnerId') is not None:
            self.owner_id = map.get('OwnerId')
        if map.get('TemplateARN') is not None:
            self.template_arn = map.get('TemplateARN')
        self.permissions = []
        if map.get('Permissions') is not None:
            for k in map.get('Permissions'):
                temp_model = GetTemplateResponsePermissions()
                self.permissions.append(temp_model.from_map(k))
        return self


class GetTemplateResponsePermissions(TeaModel):
    def __init__(self, share_option=None, version_option=None, template_version=None, account_id=None):
        self.share_option = share_option  # type: str
        self.version_option = version_option  # type: str
        self.template_version = template_version  # type: str
        self.account_id = account_id    # type: str

    def validate(self):
        self.validate_required(self.share_option, 'share_option')
        self.validate_required(self.version_option, 'version_option')
        self.validate_required(self.template_version, 'template_version')
        self.validate_required(self.account_id, 'account_id')

    def to_map(self):
        result = {}
        if self.share_option is not None:
            result['ShareOption'] = self.share_option
        if self.version_option is not None:
            result['VersionOption'] = self.version_option
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, map={}):
        if map.get('ShareOption') is not None:
            self.share_option = map.get('ShareOption')
        if map.get('VersionOption') is not None:
            self.version_option = map.get('VersionOption')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        if map.get('AccountId') is not None:
            self.account_id = map.get('AccountId')
        return self


class GetChangeSetRequest(TeaModel):
    def __init__(self, show_template=None, region_id=None, change_set_id=None):
        self.show_template = show_template  # type: bool
        self.region_id = region_id      # type: str
        self.change_set_id = change_set_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.change_set_id, 'change_set_id')

    def to_map(self):
        result = {}
        if self.show_template is not None:
            result['ShowTemplate'] = self.show_template
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        return result

    def from_map(self, map={}):
        if map.get('ShowTemplate') is not None:
            self.show_template = map.get('ShowTemplate')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ChangeSetId') is not None:
            self.change_set_id = map.get('ChangeSetId')
        return self


class GetChangeSetResponse(TeaModel):
    def __init__(self, change_set_id=None, change_set_name=None, change_set_type=None, create_time=None,
                 description=None, disable_rollback=None, execution_status=None, region_id=None, request_id=None, stack_id=None,
                 stack_name=None, status=None, template_body=None, timeout_in_minutes=None, status_reason=None,
                 parameters=None, changes=None):
        self.change_set_id = change_set_id  # type: str
        self.change_set_name = change_set_name  # type: str
        self.change_set_type = change_set_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.disable_rollback = disable_rollback  # type: bool
        self.execution_status = execution_status  # type: str
        self.region_id = region_id      # type: str
        self.request_id = request_id    # type: str
        self.stack_id = stack_id        # type: str
        self.stack_name = stack_name    # type: str
        self.status = status            # type: str
        self.template_body = template_body  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.status_reason = status_reason  # type: str
        self.parameters = parameters    # type: List[GetChangeSetResponseParameters]
        self.changes = changes          # type: List[Dict[str, Any]]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('ChangeSetId') is not None:
            self.change_set_id = map.get('ChangeSetId')
        if map.get('ChangeSetName') is not None:
            self.change_set_name = map.get('ChangeSetName')
        if map.get('ChangeSetType') is not None:
            self.change_set_type = map.get('ChangeSetType')
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('DisableRollback') is not None:
            self.disable_rollback = map.get('DisableRollback')
        if map.get('ExecutionStatus') is not None:
            self.execution_status = map.get('ExecutionStatus')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        if map.get('StatusReason') is not None:
            self.status_reason = map.get('StatusReason')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = GetChangeSetResponseParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('Changes') is not None:
            self.changes = map.get('Changes')
        return self


class GetChangeSetResponseParameters(TeaModel):
    def __init__(self, parameter_key=None, parameter_value=None):
        self.parameter_key = parameter_key  # type: str
        self.parameter_value = parameter_value  # type: str

    def validate(self):
        self.validate_required(self.parameter_key, 'parameter_key')
        self.validate_required(self.parameter_value, 'parameter_value')

    def to_map(self):
        result = {}
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, map={}):
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        return self


class ListChangeSetsRequest(TeaModel):
    def __init__(self, stack_id=None, status=None, change_set_name=None, page_size=None, region_id=None,
                 page_number=None, execution_status=None, change_set_id=None):
        self.stack_id = stack_id        # type: str
        self.status = status            # type: List[str]
        self.change_set_name = change_set_name  # type: List[str]
        self.page_size = page_size      # type: int
        self.region_id = region_id      # type: str
        self.page_number = page_number  # type: int
        self.execution_status = execution_status  # type: List[str]
        self.change_set_id = change_set_id  # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('ChangeSetName') is not None:
            self.change_set_name = map.get('ChangeSetName')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('ExecutionStatus') is not None:
            self.execution_status = map.get('ExecutionStatus')
        if map.get('ChangeSetId') is not None:
            self.change_set_id = map.get('ChangeSetId')
        return self


class ListChangeSetsResponse(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, change_sets=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.change_sets = change_sets  # type: List[ListChangeSetsResponseChangeSets]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.change_sets = []
        if map.get('ChangeSets') is not None:
            for k in map.get('ChangeSets'):
                temp_model = ListChangeSetsResponseChangeSets()
                self.change_sets.append(temp_model.from_map(k))
        return self


class ListChangeSetsResponseChangeSets(TeaModel):
    def __init__(self, change_set_id=None, change_set_name=None, change_set_type=None, create_time=None,
                 description=None, execution_status=None, region_id=None, stack_id=None, stack_name=None, status=None,
                 status_reason=None):
        self.change_set_id = change_set_id  # type: str
        self.change_set_name = change_set_name  # type: str
        self.change_set_type = change_set_type  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.execution_status = execution_status  # type: str
        self.region_id = region_id      # type: str
        self.stack_id = stack_id        # type: str
        self.stack_name = stack_name    # type: str
        self.status = status            # type: str
        self.status_reason = status_reason  # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('ChangeSetId') is not None:
            self.change_set_id = map.get('ChangeSetId')
        if map.get('ChangeSetName') is not None:
            self.change_set_name = map.get('ChangeSetName')
        if map.get('ChangeSetType') is not None:
            self.change_set_type = map.get('ChangeSetType')
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('ExecutionStatus') is not None:
            self.execution_status = map.get('ExecutionStatus')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('StatusReason') is not None:
            self.status_reason = map.get('StatusReason')
        return self


class ExecuteChangeSetRequest(TeaModel):
    def __init__(self, region_id=None, change_set_id=None, client_token=None):
        self.region_id = region_id      # type: str
        self.change_set_id = change_set_id  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.change_set_id, 'change_set_id')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ChangeSetId') is not None:
            self.change_set_id = map.get('ChangeSetId')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        return self


class ExecuteChangeSetResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DeleteChangeSetRequest(TeaModel):
    def __init__(self, region_id=None, change_set_id=None):
        self.region_id = region_id      # type: str
        self.change_set_id = change_set_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.change_set_id, 'change_set_id')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ChangeSetId') is not None:
            self.change_set_id = map.get('ChangeSetId')
        return self


class DeleteChangeSetResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ListStackEventsRequest(TeaModel):
    def __init__(self, stack_id=None, status=None, page_size=None, resource_type=None, region_id=None,
                 page_number=None, logical_resource_id=None):
        self.stack_id = stack_id        # type: str
        self.status = status            # type: List[str]
        self.page_size = page_size      # type: int
        self.resource_type = resource_type  # type: List[str]
        self.region_id = region_id      # type: str
        self.page_number = page_number  # type: int
        self.logical_resource_id = logical_resource_id  # type: List[str]

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        return self


class ListStackEventsResponse(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, total_count=None, events=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.events = events            # type: List[ListStackEventsResponseEvents]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('PageNumber') is not None:
            self.page_number = map.get('PageNumber')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.events = []
        if map.get('Events') is not None:
            for k in map.get('Events'):
                temp_model = ListStackEventsResponseEvents()
                self.events.append(temp_model.from_map(k))
        return self


class ListStackEventsResponseEvents(TeaModel):
    def __init__(self, create_time=None, event_id=None, logical_resource_id=None, physical_resource_id=None,
                 resource_type=None, stack_id=None, stack_name=None, status=None, status_reason=None):
        self.create_time = create_time  # type: str
        self.event_id = event_id        # type: str
        self.logical_resource_id = logical_resource_id  # type: str
        self.physical_resource_id = physical_resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.stack_id = stack_id        # type: str
        self.stack_name = stack_name    # type: str
        self.status = status            # type: str
        self.status_reason = status_reason  # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('EventId') is not None:
            self.event_id = map.get('EventId')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        if map.get('PhysicalResourceId') is not None:
            self.physical_resource_id = map.get('PhysicalResourceId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('StatusReason') is not None:
            self.status_reason = map.get('StatusReason')
        return self


class ListStackResourcesRequest(TeaModel):
    def __init__(self, stack_id=None, region_id=None):
        self.stack_id = stack_id        # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        return self


class ListStackResourcesResponse(TeaModel):
    def __init__(self, request_id=None, resources=None):
        self.request_id = request_id    # type: str
        self.resources = resources      # type: List[ListStackResourcesResponseResources]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resources, 'resources')
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.resources = []
        if map.get('Resources') is not None:
            for k in map.get('Resources'):
                temp_model = ListStackResourcesResponseResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListStackResourcesResponseResources(TeaModel):
    def __init__(self, create_time=None, logical_resource_id=None, physical_resource_id=None, resource_type=None,
                 stack_id=None, stack_name=None, status=None, status_reason=None, update_time=None,
                 resource_drift_status=None, drift_detection_time=None):
        self.create_time = create_time  # type: str
        self.logical_resource_id = logical_resource_id  # type: str
        self.physical_resource_id = physical_resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.stack_id = stack_id        # type: str
        self.stack_name = stack_name    # type: str
        self.status = status            # type: str
        self.status_reason = status_reason  # type: str
        self.update_time = update_time  # type: str
        self.resource_drift_status = resource_drift_status  # type: str
        self.drift_detection_time = drift_detection_time  # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        if map.get('PhysicalResourceId') is not None:
            self.physical_resource_id = map.get('PhysicalResourceId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('StatusReason') is not None:
            self.status_reason = map.get('StatusReason')
        if map.get('UpdateTime') is not None:
            self.update_time = map.get('UpdateTime')
        if map.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = map.get('ResourceDriftStatus')
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        return self


class GetStackResourceRequest(TeaModel):
    def __init__(self, stack_id=None, client_token=None, region_id=None, show_resource_attributes=None,
                 logical_resource_id=None):
        self.stack_id = stack_id        # type: str
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.show_resource_attributes = show_resource_attributes  # type: bool
        self.logical_resource_id = logical_resource_id  # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ShowResourceAttributes') is not None:
            self.show_resource_attributes = map.get('ShowResourceAttributes')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        return self


class GetStackResourceResponse(TeaModel):
    def __init__(self, create_time=None, description=None, logical_resource_id=None, metadata=None,
                 physical_resource_id=None, request_id=None, resource_type=None, stack_id=None, stack_name=None, status=None,
                 status_reason=None, update_time=None, resource_drift_status=None, drift_detection_time=None,
                 resource_attributes=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.logical_resource_id = logical_resource_id  # type: str
        self.metadata = metadata        # type: Dict[str, Any]
        self.physical_resource_id = physical_resource_id  # type: str
        self.request_id = request_id    # type: str
        self.resource_type = resource_type  # type: str
        self.stack_id = stack_id        # type: str
        self.stack_name = stack_name    # type: str
        self.status = status            # type: str
        self.status_reason = status_reason  # type: str
        self.update_time = update_time  # type: str
        self.resource_drift_status = resource_drift_status  # type: str
        self.drift_detection_time = drift_detection_time  # type: str
        self.resource_attributes = resource_attributes  # type: List[Dict[str, Any]]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('CreateTime') is not None:
            self.create_time = map.get('CreateTime')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        if map.get('Metadata') is not None:
            self.metadata = map.get('Metadata')
        if map.get('PhysicalResourceId') is not None:
            self.physical_resource_id = map.get('PhysicalResourceId')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('StatusReason') is not None:
            self.status_reason = map.get('StatusReason')
        if map.get('UpdateTime') is not None:
            self.update_time = map.get('UpdateTime')
        if map.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = map.get('ResourceDriftStatus')
        if map.get('DriftDetectionTime') is not None:
            self.drift_detection_time = map.get('DriftDetectionTime')
        if map.get('ResourceAttributes') is not None:
            self.resource_attributes = map.get('ResourceAttributes')
        return self


class GetResourceTypeTemplateRequest(TeaModel):
    def __init__(self, resource_type=None):
        self.resource_type = resource_type  # type: str

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = {}
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, map={}):
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        return self


class GetResourceTypeTemplateResponse(TeaModel):
    def __init__(self, request_id=None, template_body=None):
        self.request_id = request_id    # type: str
        self.template_body = template_body  # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.template_body, 'template_body')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        return self


class GetResourceTypeRequest(TeaModel):
    def __init__(self, resource_type=None):
        self.resource_type = resource_type  # type: str

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = {}
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, map={}):
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        return self


class GetResourceTypeResponse(TeaModel):
    def __init__(self, attributes=None, properties=None, request_id=None, resource_type=None,
                 support_drift_detection=None):
        self.attributes = attributes    # type: Dict[str, Any]
        self.properties = properties    # type: Dict[str, Any]
        self.request_id = request_id    # type: str
        self.resource_type = resource_type  # type: str
        self.support_drift_detection = support_drift_detection  # type: bool

    def validate(self):
        self.validate_required(self.attributes, 'attributes')
        self.validate_required(self.properties, 'properties')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.support_drift_detection, 'support_drift_detection')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('Attributes') is not None:
            self.attributes = map.get('Attributes')
        if map.get('Properties') is not None:
            self.properties = map.get('Properties')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('SupportDriftDetection') is not None:
            self.support_drift_detection = map.get('SupportDriftDetection')
        return self


class ListResourceTypesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class ListResourceTypesResponse(TeaModel):
    def __init__(self, request_id=None, resource_types=None):
        self.request_id = request_id    # type: str
        self.resource_types = resource_types  # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_types, 'resource_types')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('ResourceTypes') is not None:
            self.resource_types = map.get('ResourceTypes')
        return self


class SignalResourceRequest(TeaModel):
    def __init__(self, stack_id=None, status=None, region_id=None, unique_id=None, client_token=None,
                 logical_resource_id=None):
        self.stack_id = stack_id        # type: str
        self.status = status            # type: str
        self.region_id = region_id      # type: str
        self.unique_id = unique_id      # type: str
        self.client_token = client_token  # type: str
        self.logical_resource_id = logical_resource_id  # type: str

    def validate(self):
        self.validate_required(self.stack_id, 'stack_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.unique_id, 'unique_id')
        self.validate_required(self.logical_resource_id, 'logical_resource_id')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('UniqueId') is not None:
            self.unique_id = map.get('UniqueId')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        return self


class SignalResourceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, map={}):
        if map.get('AcceptLanguage') is not None:
            self.accept_language = map.get('AcceptLanguage')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id    # type: str
        self.regions = regions          # type: List[DescribeRegionsResponseRegions]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.regions, 'regions')
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.regions = []
        if map.get('Regions') is not None:
            for k in map.get('Regions'):
                temp_model = DescribeRegionsResponseRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseRegions(TeaModel):
    def __init__(self, region_id=None, local_name=None, region_endpoint=None):
        self.region_id = region_id      # type: str
        self.local_name = local_name    # type: str
        self.region_endpoint = region_endpoint  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.local_name, 'local_name')
        self.validate_required(self.region_endpoint, 'region_endpoint')

    def to_map(self):
        result = {}
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('LocalName') is not None:
            self.local_name = map.get('LocalName')
        if map.get('RegionEndpoint') is not None:
            self.region_endpoint = map.get('RegionEndpoint')
        return self


class CreateChangeSetRequest(TeaModel):
    def __init__(self, stack_id=None, parameters=None, stack_policy_url=None, stack_policy_body=None,
                 stack_name=None, use_previous_parameters=None, change_set_type=None, description=None, region_id=None,
                 client_token=None, template_url=None, stack_policy_during_update_url=None, template_body=None,
                 timeout_in_minutes=None, disable_rollback=None, change_set_name=None, stack_policy_during_update_body=None,
                 notification_urls=None, ram_role_name=None, replacement_option=None, resources_to_import=None, template_id=None,
                 template_version=None):
        self.stack_id = stack_id        # type: str
        self.parameters = parameters    # type: List[CreateChangeSetRequestParameters]
        self.stack_policy_url = stack_policy_url  # type: str
        self.stack_policy_body = stack_policy_body  # type: str
        self.stack_name = stack_name    # type: str
        self.use_previous_parameters = use_previous_parameters  # type: bool
        self.change_set_type = change_set_type  # type: str
        self.description = description  # type: str
        self.region_id = region_id      # type: str
        self.client_token = client_token  # type: str
        self.template_url = template_url  # type: str
        self.stack_policy_during_update_url = stack_policy_during_update_url  # type: str
        self.template_body = template_body  # type: str
        self.timeout_in_minutes = timeout_in_minutes  # type: int
        self.disable_rollback = disable_rollback  # type: bool
        self.change_set_name = change_set_name  # type: str
        self.stack_policy_during_update_body = stack_policy_during_update_body  # type: str
        self.notification_urls = notification_urls  # type: List[str]
        self.ram_role_name = ram_role_name  # type: str
        self.replacement_option = replacement_option  # type: str
        self.resources_to_import = resources_to_import  # type: List[CreateChangeSetRequestResourcesToImport]
        self.template_id = template_id  # type: str
        self.template_version = template_version  # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        self.parameters = []
        if map.get('Parameters') is not None:
            for k in map.get('Parameters'):
                temp_model = CreateChangeSetRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if map.get('StackPolicyURL') is not None:
            self.stack_policy_url = map.get('StackPolicyURL')
        if map.get('StackPolicyBody') is not None:
            self.stack_policy_body = map.get('StackPolicyBody')
        if map.get('StackName') is not None:
            self.stack_name = map.get('StackName')
        if map.get('UsePreviousParameters') is not None:
            self.use_previous_parameters = map.get('UsePreviousParameters')
        if map.get('ChangeSetType') is not None:
            self.change_set_type = map.get('ChangeSetType')
        if map.get('Description') is not None:
            self.description = map.get('Description')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ClientToken') is not None:
            self.client_token = map.get('ClientToken')
        if map.get('TemplateURL') is not None:
            self.template_url = map.get('TemplateURL')
        if map.get('StackPolicyDuringUpdateURL') is not None:
            self.stack_policy_during_update_url = map.get('StackPolicyDuringUpdateURL')
        if map.get('TemplateBody') is not None:
            self.template_body = map.get('TemplateBody')
        if map.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = map.get('TimeoutInMinutes')
        if map.get('DisableRollback') is not None:
            self.disable_rollback = map.get('DisableRollback')
        if map.get('ChangeSetName') is not None:
            self.change_set_name = map.get('ChangeSetName')
        if map.get('StackPolicyDuringUpdateBody') is not None:
            self.stack_policy_during_update_body = map.get('StackPolicyDuringUpdateBody')
        if map.get('NotificationURLs') is not None:
            self.notification_urls = map.get('NotificationURLs')
        if map.get('RamRoleName') is not None:
            self.ram_role_name = map.get('RamRoleName')
        if map.get('ReplacementOption') is not None:
            self.replacement_option = map.get('ReplacementOption')
        self.resources_to_import = []
        if map.get('ResourcesToImport') is not None:
            for k in map.get('ResourcesToImport'):
                temp_model = CreateChangeSetRequestResourcesToImport()
                self.resources_to_import.append(temp_model.from_map(k))
        if map.get('TemplateId') is not None:
            self.template_id = map.get('TemplateId')
        if map.get('TemplateVersion') is not None:
            self.template_version = map.get('TemplateVersion')
        return self


class CreateChangeSetRequestParameters(TeaModel):
    def __init__(self, parameter_value=None, parameter_key=None):
        self.parameter_value = parameter_value  # type: str
        self.parameter_key = parameter_key  # type: str

    def validate(self):
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_key, 'parameter_key')

    def to_map(self):
        result = {}
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        return result

    def from_map(self, map={}):
        if map.get('ParameterValue') is not None:
            self.parameter_value = map.get('ParameterValue')
        if map.get('ParameterKey') is not None:
            self.parameter_key = map.get('ParameterKey')
        return self


class CreateChangeSetRequestResourcesToImport(TeaModel):
    def __init__(self, logical_resource_id=None, resource_type=None, resource_identifier=None):
        self.logical_resource_id = logical_resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_identifier = resource_identifier  # type: str

    def validate(self):
        self.validate_required(self.logical_resource_id, 'logical_resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_identifier, 'resource_identifier')

    def to_map(self):
        result = {}
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_identifier is not None:
            result['ResourceIdentifier'] = self.resource_identifier
        return result

    def from_map(self, map={}):
        if map.get('LogicalResourceId') is not None:
            self.logical_resource_id = map.get('LogicalResourceId')
        if map.get('ResourceType') is not None:
            self.resource_type = map.get('ResourceType')
        if map.get('ResourceIdentifier') is not None:
            self.resource_identifier = map.get('ResourceIdentifier')
        return self


class CreateChangeSetResponse(TeaModel):
    def __init__(self, change_set_id=None, request_id=None, stack_id=None):
        self.change_set_id = change_set_id  # type: str
        self.request_id = request_id    # type: str
        self.stack_id = stack_id        # type: str

    def validate(self):
        self.validate_required(self.change_set_id, 'change_set_id')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stack_id, 'stack_id')

    def to_map(self):
        result = {}
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, map={}):
        if map.get('ChangeSetId') is not None:
            self.change_set_id = map.get('ChangeSetId')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StackId') is not None:
            self.stack_id = map.get('StackId')
        return self
