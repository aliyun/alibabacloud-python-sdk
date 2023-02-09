# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CancelStackOperationRequest(TeaModel):
    def __init__(
        self,
        allowed_stack_operations: List[str] = None,
        cancel_type: str = None,
        region_id: str = None,
        stack_id: str = None,
    ):
        # test
        self.allowed_stack_operations = allowed_stack_operations
        self.cancel_type = cancel_type
        self.region_id = region_id
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_stack_operations is not None:
            result['AllowedStackOperations'] = self.allowed_stack_operations
        if self.cancel_type is not None:
            result['CancelType'] = self.cancel_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedStackOperations') is not None:
            self.allowed_stack_operations = m.get('AllowedStackOperations')
        if m.get('CancelType') is not None:
            self.cancel_type = m.get('CancelType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class CancelStackOperationResponseBody(TeaModel):
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


class CancelStackOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelStackOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CancelStackOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelUpdateStackRequest(TeaModel):
    def __init__(
        self,
        cancel_type: str = None,
        region_id: str = None,
        stack_id: str = None,
    ):
        self.cancel_type = cancel_type
        self.region_id = region_id
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cancel_type is not None:
            result['CancelType'] = self.cancel_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelType') is not None:
            self.cancel_type = m.get('CancelType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class CancelUpdateStackResponseBody(TeaModel):
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


class CancelUpdateStackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelUpdateStackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CancelUpdateStackResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        dry_run: bool = None,
        mode: str = None,
        parallelism: int = None,
        parameters: List[ContinueCreateStackRequestParameters] = None,
        ram_role_name: str = None,
        recreating_options: List[str] = None,
        recreating_resources: List[str] = None,
        region_id: str = None,
        stack_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.dry_run = dry_run
        self.mode = mode
        self.parallelism = parallelism
        # test
        self.parameters = parameters
        self.ram_role_name = ram_role_name
        self.recreating_options = recreating_options
        self.recreating_resources = recreating_resources
        self.region_id = region_id
        self.stack_id = stack_id
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version

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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.recreating_options is not None:
            result['RecreatingOptions'] = self.recreating_options
        if self.recreating_resources is not None:
            result['RecreatingResources'] = self.recreating_resources
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ContinueCreateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RecreatingOptions') is not None:
            self.recreating_options = m.get('RecreatingOptions')
        if m.get('RecreatingResources') is not None:
            self.recreating_resources = m.get('RecreatingResources')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class ContinueCreateStackResponseBodyDryRunResult(TeaModel):
    def __init__(
        self,
        parameters_allowed_to_be_modified: List[str] = None,
        parameters_conditionally_allowed_to_be_modified: List[str] = None,
        parameters_not_allowed_to_be_modified: List[str] = None,
    ):
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        self.parameters_not_allowed_to_be_modified = parameters_not_allowed_to_be_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters_allowed_to_be_modified is not None:
            result['ParametersAllowedToBeModified'] = self.parameters_allowed_to_be_modified
        if self.parameters_conditionally_allowed_to_be_modified is not None:
            result['ParametersConditionallyAllowedToBeModified'] = self.parameters_conditionally_allowed_to_be_modified
        if self.parameters_not_allowed_to_be_modified is not None:
            result['ParametersNotAllowedToBeModified'] = self.parameters_not_allowed_to_be_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParametersAllowedToBeModified') is not None:
            self.parameters_allowed_to_be_modified = m.get('ParametersAllowedToBeModified')
        if m.get('ParametersConditionallyAllowedToBeModified') is not None:
            self.parameters_conditionally_allowed_to_be_modified = m.get('ParametersConditionallyAllowedToBeModified')
        if m.get('ParametersNotAllowedToBeModified') is not None:
            self.parameters_not_allowed_to_be_modified = m.get('ParametersNotAllowedToBeModified')
        return self


class ContinueCreateStackResponseBody(TeaModel):
    def __init__(
        self,
        dry_run_result: ContinueCreateStackResponseBodyDryRunResult = None,
        request_id: str = None,
        stack_id: str = None,
    ):
        self.dry_run_result = dry_run_result
        self.request_id = request_id
        self.stack_id = stack_id

    def validate(self):
        if self.dry_run_result:
            self.dry_run_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run_result is not None:
            result['DryRunResult'] = self.dry_run_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRunResult') is not None:
            temp_model = ContinueCreateStackResponseBodyDryRunResult()
            self.dry_run_result = temp_model.from_map(m['DryRunResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class ContinueCreateStackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ContinueCreateStackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ContinueCreateStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChangeSetRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateChangeSetRequestResourcesToImport(TeaModel):
    def __init__(
        self,
        logical_resource_id: str = None,
        resource_identifier: str = None,
        resource_type: str = None,
    ):
        self.logical_resource_id = logical_resource_id
        self.resource_identifier = resource_identifier
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.resource_identifier is not None:
            result['ResourceIdentifier'] = self.resource_identifier
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('ResourceIdentifier') is not None:
            self.resource_identifier = m.get('ResourceIdentifier')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateChangeSetRequest(TeaModel):
    def __init__(
        self,
        change_set_name: str = None,
        change_set_type: str = None,
        client_token: str = None,
        description: str = None,
        disable_rollback: bool = None,
        notification_urls: List[str] = None,
        parallelism: int = None,
        parameters: List[CreateChangeSetRequestParameters] = None,
        ram_role_name: str = None,
        region_id: str = None,
        replacement_option: str = None,
        resources_to_import: List[CreateChangeSetRequestResourcesToImport] = None,
        stack_id: str = None,
        stack_name: str = None,
        stack_policy_body: str = None,
        stack_policy_during_update_body: str = None,
        stack_policy_during_update_url: str = None,
        stack_policy_url: str = None,
        template_body: str = None,
        template_id: str = None,
        template_scratch_id: str = None,
        template_url: str = None,
        template_version: str = None,
        timeout_in_minutes: int = None,
        use_previous_parameters: bool = None,
    ):
        self.change_set_name = change_set_name
        self.change_set_type = change_set_type
        self.client_token = client_token
        self.description = description
        self.disable_rollback = disable_rollback
        self.notification_urls = notification_urls
        self.parallelism = parallelism
        self.parameters = parameters
        self.ram_role_name = ram_role_name
        self.region_id = region_id
        self.replacement_option = replacement_option
        self.resources_to_import = resources_to_import
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.stack_policy_body = stack_policy_body
        self.stack_policy_during_update_body = stack_policy_during_update_body
        self.stack_policy_during_update_url = stack_policy_during_update_url
        self.stack_policy_url = stack_policy_url
        self.template_body = template_body
        self.template_id = template_id
        self.template_scratch_id = template_scratch_id
        self.template_url = template_url
        self.template_version = template_version
        self.timeout_in_minutes = timeout_in_minutes
        self.use_previous_parameters = use_previous_parameters

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.resources_to_import:
            for k in self.resources_to_import:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name
        if self.change_set_type is not None:
            result['ChangeSetType'] = self.change_set_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replacement_option is not None:
            result['ReplacementOption'] = self.replacement_option
        result['ResourcesToImport'] = []
        if self.resources_to_import is not None:
            for k in self.resources_to_import:
                result['ResourcesToImport'].append(k.to_map() if k else None)
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_policy_during_update_body is not None:
            result['StackPolicyDuringUpdateBody'] = self.stack_policy_during_update_body
        if self.stack_policy_during_update_url is not None:
            result['StackPolicyDuringUpdateURL'] = self.stack_policy_during_update_url
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.use_previous_parameters is not None:
            result['UsePreviousParameters'] = self.use_previous_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')
        if m.get('ChangeSetType') is not None:
            self.change_set_type = m.get('ChangeSetType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateChangeSetRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplacementOption') is not None:
            self.replacement_option = m.get('ReplacementOption')
        self.resources_to_import = []
        if m.get('ResourcesToImport') is not None:
            for k in m.get('ResourcesToImport'):
                temp_model = CreateChangeSetRequestResourcesToImport()
                self.resources_to_import.append(temp_model.from_map(k))
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackPolicyDuringUpdateBody') is not None:
            self.stack_policy_during_update_body = m.get('StackPolicyDuringUpdateBody')
        if m.get('StackPolicyDuringUpdateURL') is not None:
            self.stack_policy_during_update_url = m.get('StackPolicyDuringUpdateURL')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('UsePreviousParameters') is not None:
            self.use_previous_parameters = m.get('UsePreviousParameters')
        return self


class CreateChangeSetResponseBody(TeaModel):
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateChangeSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChangeSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateChangeSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStackRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStackRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        client_token: str = None,
        create_option: str = None,
        deletion_protection: str = None,
        disable_rollback: bool = None,
        notification_urls: List[str] = None,
        parallelism: int = None,
        parameters: List[CreateStackRequestParameters] = None,
        ram_role_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        stack_name: str = None,
        stack_policy_body: str = None,
        stack_policy_url: str = None,
        tags: List[CreateStackRequestTags] = None,
        template_body: str = None,
        template_id: str = None,
        template_scratch_id: str = None,
        template_scratch_region_id: str = None,
        template_url: str = None,
        template_version: str = None,
        timeout_in_minutes: int = None,
    ):
        self.client_token = client_token
        self.create_option = create_option
        self.deletion_protection = deletion_protection
        self.disable_rollback = disable_rollback
        self.notification_urls = notification_urls
        self.parallelism = parallelism
        # test
        self.parameters = parameters
        self.ram_role_name = ram_role_name
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.stack_name = stack_name
        self.stack_policy_body = stack_policy_body
        self.stack_policy_url = stack_policy_url
        # test
        self.tags = tags
        self.template_body = template_body
        self.template_id = template_id
        self.template_scratch_id = template_scratch_id
        self.template_scratch_region_id = template_scratch_region_id
        self.template_url = template_url
        self.template_version = template_version
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.create_option is not None:
            result['CreateOption'] = self.create_option
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        if self.template_scratch_region_id is not None:
            result['TemplateScratchRegionId'] = self.template_scratch_region_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CreateOption') is not None:
            self.create_option = m.get('CreateOption')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateStackRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        if m.get('TemplateScratchRegionId') is not None:
            self.template_scratch_region_id = m.get('TemplateScratchRegionId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        return self


class CreateStackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_id: str = None,
    ):
        self.request_id = request_id
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStackGroupRequestAutoDeployment(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        retain_stacks_on_account_removal: bool = None,
    ):
        self.enabled = enabled
        self.retain_stacks_on_account_removal = retain_stacks_on_account_removal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.retain_stacks_on_account_removal is not None:
            result['RetainStacksOnAccountRemoval'] = self.retain_stacks_on_account_removal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RetainStacksOnAccountRemoval') is not None:
            self.retain_stacks_on_account_removal = m.get('RetainStacksOnAccountRemoval')
        return self


class CreateStackGroupRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStackGroupRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStackGroupRequest(TeaModel):
    def __init__(
        self,
        administration_role_name: str = None,
        auto_deployment: CreateStackGroupRequestAutoDeployment = None,
        client_token: str = None,
        description: str = None,
        execution_role_name: str = None,
        parameters: List[CreateStackGroupRequestParameters] = None,
        permission_model: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        stack_group_name: str = None,
        tags: List[CreateStackGroupRequestTags] = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.administration_role_name = administration_role_name
        self.auto_deployment = auto_deployment
        self.client_token = client_token
        self.description = description
        self.execution_role_name = execution_role_name
        # test
        self.parameters = parameters
        self.permission_model = permission_model
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.stack_group_name = stack_group_name
        self.tags = tags
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version

    def validate(self):
        if self.auto_deployment:
            self.auto_deployment.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.auto_deployment is not None:
            result['AutoDeployment'] = self.auto_deployment.to_map()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('AutoDeployment') is not None:
            temp_model = CreateStackGroupRequestAutoDeployment()
            self.auto_deployment = temp_model.from_map(m['AutoDeployment'])
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateStackGroupRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateStackGroupRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class CreateStackGroupShrinkRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStackGroupShrinkRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStackGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        administration_role_name: str = None,
        auto_deployment_shrink: str = None,
        client_token: str = None,
        description: str = None,
        execution_role_name: str = None,
        parameters: List[CreateStackGroupShrinkRequestParameters] = None,
        permission_model: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        stack_group_name: str = None,
        tags: List[CreateStackGroupShrinkRequestTags] = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.administration_role_name = administration_role_name
        self.auto_deployment_shrink = auto_deployment_shrink
        self.client_token = client_token
        self.description = description
        self.execution_role_name = execution_role_name
        # test
        self.parameters = parameters
        self.permission_model = permission_model
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.stack_group_name = stack_group_name
        self.tags = tags
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.auto_deployment_shrink is not None:
            result['AutoDeployment'] = self.auto_deployment_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('AutoDeployment') is not None:
            self.auto_deployment_shrink = m.get('AutoDeployment')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = CreateStackGroupShrinkRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateStackGroupShrinkRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class CreateStackGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_group_id: str = None,
    ):
        self.request_id = request_id
        self.stack_group_id = stack_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStackGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStackGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateStackGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStackInstancesRequestDeploymentTargets(TeaModel):
    def __init__(
        self,
        rd_folder_ids: List[str] = None,
    ):
        self.rd_folder_ids = rd_folder_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        return self


class CreateStackInstancesRequestParameterOverrides(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStackInstancesRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        client_token: str = None,
        deployment_targets: CreateStackInstancesRequestDeploymentTargets = None,
        disable_rollback: bool = None,
        operation_description: str = None,
        operation_preferences: Dict[str, Any] = None,
        parameter_overrides: List[CreateStackInstancesRequestParameterOverrides] = None,
        region_id: str = None,
        region_ids: List[str] = None,
        stack_group_name: str = None,
        timeout_in_minutes: int = None,
    ):
        self.account_ids = account_ids
        self.client_token = client_token
        self.deployment_targets = deployment_targets
        self.disable_rollback = disable_rollback
        self.operation_description = operation_description
        self.operation_preferences = operation_preferences
        # test
        self.parameter_overrides = parameter_overrides
        self.region_id = region_id
        self.region_ids = region_ids
        self.stack_group_name = stack_group_name
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        if self.deployment_targets:
            self.deployment_targets.validate()
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeploymentTargets') is not None:
            temp_model = CreateStackInstancesRequestDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m['DeploymentTargets'])
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = CreateStackInstancesRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        return self


class CreateStackInstancesShrinkRequestParameterOverrides(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStackInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        client_token: str = None,
        deployment_targets_shrink: str = None,
        disable_rollback: bool = None,
        operation_description: str = None,
        operation_preferences_shrink: str = None,
        parameter_overrides: List[CreateStackInstancesShrinkRequestParameterOverrides] = None,
        region_id: str = None,
        region_ids_shrink: str = None,
        stack_group_name: str = None,
        timeout_in_minutes: int = None,
    ):
        self.account_ids_shrink = account_ids_shrink
        self.client_token = client_token
        self.deployment_targets_shrink = deployment_targets_shrink
        self.disable_rollback = disable_rollback
        self.operation_description = operation_description
        self.operation_preferences_shrink = operation_preferences_shrink
        # test
        self.parameter_overrides = parameter_overrides
        self.region_id = region_id
        self.region_ids_shrink = region_ids_shrink
        self.stack_group_name = stack_group_name
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deployment_targets_shrink is not None:
            result['DeploymentTargets'] = self.deployment_targets_shrink
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeploymentTargets') is not None:
            self.deployment_targets_shrink = m.get('DeploymentTargets')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = CreateStackInstancesShrinkRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        return self


class CreateStackInstancesResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateStackInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStackInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateStackInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        resource_group_id: str = None,
        tags: List[CreateTemplateRequestTags] = None,
        template_body: str = None,
        template_name: str = None,
        template_url: str = None,
    ):
        self.description = description
        self.resource_group_id = resource_group_id
        self.tags = tags
        self.template_body = template_body
        self.template_name = template_name
        self.template_url = template_url

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateTemplateRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_id: str = None,
    ):
        self.request_id = request_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateScratchRequestPreferenceParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateTemplateScratchRequestSourceResourceGroup(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_type_filter: List[str] = None,
    ):
        self.resource_group_id = resource_group_id
        self.resource_type_filter = resource_type_filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type_filter is not None:
            result['ResourceTypeFilter'] = self.resource_type_filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTypeFilter') is not None:
            self.resource_type_filter = m.get('ResourceTypeFilter')
        return self


class CreateTemplateScratchRequestSourceResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateTemplateScratchRequestSourceTag(TeaModel):
    def __init__(
        self,
        resource_tags: Dict[str, Any] = None,
        resource_type_filter: List[str] = None,
    ):
        self.resource_tags = resource_tags
        self.resource_type_filter = resource_type_filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_tags is not None:
            result['ResourceTags'] = self.resource_tags
        if self.resource_type_filter is not None:
            result['ResourceTypeFilter'] = self.resource_type_filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTags') is not None:
            self.resource_tags = m.get('ResourceTags')
        if m.get('ResourceTypeFilter') is not None:
            self.resource_type_filter = m.get('ResourceTypeFilter')
        return self


class CreateTemplateScratchRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateTemplateScratchRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        execution_mode: str = None,
        logical_id_strategy: str = None,
        preference_parameters: List[CreateTemplateScratchRequestPreferenceParameters] = None,
        region_id: str = None,
        source_resource_group: CreateTemplateScratchRequestSourceResourceGroup = None,
        source_resources: List[CreateTemplateScratchRequestSourceResources] = None,
        source_tag: CreateTemplateScratchRequestSourceTag = None,
        tags: List[CreateTemplateScratchRequestTags] = None,
        template_scratch_type: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.execution_mode = execution_mode
        self.logical_id_strategy = logical_id_strategy
        self.preference_parameters = preference_parameters
        self.region_id = region_id
        self.source_resource_group = source_resource_group
        self.source_resources = source_resources
        self.source_tag = source_tag
        self.tags = tags
        self.template_scratch_type = template_scratch_type

    def validate(self):
        if self.preference_parameters:
            for k in self.preference_parameters:
                if k:
                    k.validate()
        if self.source_resource_group:
            self.source_resource_group.validate()
        if self.source_resources:
            for k in self.source_resources:
                if k:
                    k.validate()
        if self.source_tag:
            self.source_tag.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.logical_id_strategy is not None:
            result['LogicalIdStrategy'] = self.logical_id_strategy
        result['PreferenceParameters'] = []
        if self.preference_parameters is not None:
            for k in self.preference_parameters:
                result['PreferenceParameters'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_resource_group is not None:
            result['SourceResourceGroup'] = self.source_resource_group.to_map()
        result['SourceResources'] = []
        if self.source_resources is not None:
            for k in self.source_resources:
                result['SourceResources'].append(k.to_map() if k else None)
        if self.source_tag is not None:
            result['SourceTag'] = self.source_tag.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_scratch_type is not None:
            result['TemplateScratchType'] = self.template_scratch_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('LogicalIdStrategy') is not None:
            self.logical_id_strategy = m.get('LogicalIdStrategy')
        self.preference_parameters = []
        if m.get('PreferenceParameters') is not None:
            for k in m.get('PreferenceParameters'):
                temp_model = CreateTemplateScratchRequestPreferenceParameters()
                self.preference_parameters.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceResourceGroup') is not None:
            temp_model = CreateTemplateScratchRequestSourceResourceGroup()
            self.source_resource_group = temp_model.from_map(m['SourceResourceGroup'])
        self.source_resources = []
        if m.get('SourceResources') is not None:
            for k in m.get('SourceResources'):
                temp_model = CreateTemplateScratchRequestSourceResources()
                self.source_resources.append(temp_model.from_map(k))
        if m.get('SourceTag') is not None:
            temp_model = CreateTemplateScratchRequestSourceTag()
            self.source_tag = temp_model.from_map(m['SourceTag'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateTemplateScratchRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateScratchType') is not None:
            self.template_scratch_type = m.get('TemplateScratchType')
        return self


class CreateTemplateScratchShrinkRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateTemplateScratchShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        execution_mode: str = None,
        logical_id_strategy: str = None,
        preference_parameters_shrink: str = None,
        region_id: str = None,
        source_resource_group_shrink: str = None,
        source_resources_shrink: str = None,
        source_tag_shrink: str = None,
        tags: List[CreateTemplateScratchShrinkRequestTags] = None,
        template_scratch_type: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.execution_mode = execution_mode
        self.logical_id_strategy = logical_id_strategy
        self.preference_parameters_shrink = preference_parameters_shrink
        self.region_id = region_id
        self.source_resource_group_shrink = source_resource_group_shrink
        self.source_resources_shrink = source_resources_shrink
        self.source_tag_shrink = source_tag_shrink
        self.tags = tags
        self.template_scratch_type = template_scratch_type

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.logical_id_strategy is not None:
            result['LogicalIdStrategy'] = self.logical_id_strategy
        if self.preference_parameters_shrink is not None:
            result['PreferenceParameters'] = self.preference_parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_resource_group_shrink is not None:
            result['SourceResourceGroup'] = self.source_resource_group_shrink
        if self.source_resources_shrink is not None:
            result['SourceResources'] = self.source_resources_shrink
        if self.source_tag_shrink is not None:
            result['SourceTag'] = self.source_tag_shrink
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_scratch_type is not None:
            result['TemplateScratchType'] = self.template_scratch_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('LogicalIdStrategy') is not None:
            self.logical_id_strategy = m.get('LogicalIdStrategy')
        if m.get('PreferenceParameters') is not None:
            self.preference_parameters_shrink = m.get('PreferenceParameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceResourceGroup') is not None:
            self.source_resource_group_shrink = m.get('SourceResourceGroup')
        if m.get('SourceResources') is not None:
            self.source_resources_shrink = m.get('SourceResources')
        if m.get('SourceTag') is not None:
            self.source_tag_shrink = m.get('SourceTag')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateTemplateScratchShrinkRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateScratchType') is not None:
            self.template_scratch_type = m.get('TemplateScratchType')
        return self


class CreateTemplateScratchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_scratch_id: str = None,
    ):
        self.request_id = request_id
        self.template_scratch_id = template_scratch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        return self


class CreateTemplateScratchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTemplateScratchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateTemplateScratchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChangeSetRequest(TeaModel):
    def __init__(
        self,
        change_set_id: str = None,
        region_id: str = None,
    ):
        self.change_set_id = change_set_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteChangeSetResponseBody(TeaModel):
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


class DeleteChangeSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteChangeSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteChangeSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStackRequest(TeaModel):
    def __init__(
        self,
        ram_role_name: str = None,
        region_id: str = None,
        retain_all_resources: bool = None,
        retain_resources: List[str] = None,
        stack_id: str = None,
    ):
        self.ram_role_name = ram_role_name
        self.region_id = region_id
        self.retain_all_resources = retain_all_resources
        self.retain_resources = retain_resources
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retain_all_resources is not None:
            result['RetainAllResources'] = self.retain_all_resources
        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetainAllResources') is not None:
            self.retain_all_resources = m.get('RetainAllResources')
        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class DeleteStackResponseBody(TeaModel):
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


class DeleteStackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteStackResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DeleteStackGroupResponseBody(TeaModel):
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


class DeleteStackGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStackGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteStackGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStackInstancesRequestDeploymentTargets(TeaModel):
    def __init__(
        self,
        rd_folder_ids: List[str] = None,
    ):
        self.rd_folder_ids = rd_folder_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        return self


class DeleteStackInstancesRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        client_token: str = None,
        deployment_targets: DeleteStackInstancesRequestDeploymentTargets = None,
        operation_description: str = None,
        operation_preferences: Dict[str, Any] = None,
        region_id: str = None,
        region_ids: List[str] = None,
        retain_stacks: bool = None,
        stack_group_name: str = None,
    ):
        self.account_ids = account_ids
        self.client_token = client_token
        self.deployment_targets = deployment_targets
        self.operation_description = operation_description
        self.operation_preferences = operation_preferences
        self.region_id = region_id
        self.region_ids = region_ids
        self.retain_stacks = retain_stacks
        self.stack_group_name = stack_group_name

    def validate(self):
        if self.deployment_targets:
            self.deployment_targets.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.retain_stacks is not None:
            result['RetainStacks'] = self.retain_stacks
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeploymentTargets') is not None:
            temp_model = DeleteStackInstancesRequestDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m['DeploymentTargets'])
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('RetainStacks') is not None:
            self.retain_stacks = m.get('RetainStacks')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class DeleteStackInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        client_token: str = None,
        deployment_targets_shrink: str = None,
        operation_description: str = None,
        operation_preferences_shrink: str = None,
        region_id: str = None,
        region_ids_shrink: str = None,
        retain_stacks: bool = None,
        stack_group_name: str = None,
    ):
        self.account_ids_shrink = account_ids_shrink
        self.client_token = client_token
        self.deployment_targets_shrink = deployment_targets_shrink
        self.operation_description = operation_description
        self.operation_preferences_shrink = operation_preferences_shrink
        self.region_id = region_id
        self.region_ids_shrink = region_ids_shrink
        self.retain_stacks = retain_stacks
        self.stack_group_name = stack_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deployment_targets_shrink is not None:
            result['DeploymentTargets'] = self.deployment_targets_shrink
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.retain_stacks is not None:
            result['RetainStacks'] = self.retain_stacks
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeploymentTargets') is not None:
            self.deployment_targets_shrink = m.get('DeploymentTargets')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('RetainStacks') is not None:
            self.retain_stacks = m.get('RetainStacks')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class DeleteStackInstancesResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteStackInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStackInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteStackInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
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


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateScratchRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_scratch_id: str = None,
    ):
        self.region_id = region_id
        self.template_scratch_id = template_scratch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        return self


class DeleteTemplateScratchResponseBody(TeaModel):
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


class DeleteTemplateScratchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTemplateScratchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteTemplateScratchResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectStackDriftRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        logical_resource_id: List[str] = None,
        region_id: str = None,
        stack_id: str = None,
    ):
        self.client_token = client_token
        self.logical_resource_id = logical_resource_id
        self.region_id = region_id
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class DetectStackDriftResponseBody(TeaModel):
    def __init__(
        self,
        drift_detection_id: str = None,
        request_id: str = None,
    ):
        self.drift_detection_id = drift_detection_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriftDetectionId') is not None:
            self.drift_detection_id = m.get('DriftDetectionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectStackDriftResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectStackDriftResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DetectStackDriftResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectStackGroupDriftRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        operation_preferences: Dict[str, Any] = None,
        region_id: str = None,
        stack_group_name: str = None,
    ):
        self.client_token = client_token
        self.operation_preferences = operation_preferences
        self.region_id = region_id
        self.stack_group_name = stack_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class DetectStackGroupDriftShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        operation_preferences_shrink: str = None,
        region_id: str = None,
        stack_group_name: str = None,
    ):
        self.client_token = client_token
        self.operation_preferences_shrink = operation_preferences_shrink
        self.region_id = region_id
        self.stack_group_name = stack_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class DetectStackGroupDriftResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetectStackGroupDriftResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectStackGroupDriftResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DetectStackGroupDriftResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectStackResourceDriftRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        logical_resource_id: str = None,
        region_id: str = None,
        stack_id: str = None,
    ):
        self.client_token = client_token
        self.logical_resource_id = logical_resource_id
        self.region_id = region_id
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class DetectStackResourceDriftResponseBodyPropertyDifferences(TeaModel):
    def __init__(
        self,
        actual_value: str = None,
        difference_type: str = None,
        expected_value: str = None,
        property_path: str = None,
    ):
        self.actual_value = actual_value
        self.difference_type = difference_type
        self.expected_value = expected_value
        self.property_path = property_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.difference_type is not None:
            result['DifferenceType'] = self.difference_type
        if self.expected_value is not None:
            result['ExpectedValue'] = self.expected_value
        if self.property_path is not None:
            result['PropertyPath'] = self.property_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('DifferenceType') is not None:
            self.difference_type = m.get('DifferenceType')
        if m.get('ExpectedValue') is not None:
            self.expected_value = m.get('ExpectedValue')
        if m.get('PropertyPath') is not None:
            self.property_path = m.get('PropertyPath')
        return self


class DetectStackResourceDriftResponseBody(TeaModel):
    def __init__(
        self,
        actual_properties: str = None,
        drift_detection_time: str = None,
        expected_properties: str = None,
        logical_resource_id: str = None,
        physical_resource_id: str = None,
        property_differences: List[DetectStackResourceDriftResponseBodyPropertyDifferences] = None,
        request_id: str = None,
        resource_drift_status: str = None,
        resource_type: str = None,
        stack_id: str = None,
    ):
        self.actual_properties = actual_properties
        self.drift_detection_time = drift_detection_time
        self.expected_properties = expected_properties
        self.logical_resource_id = logical_resource_id
        self.physical_resource_id = physical_resource_id
        self.property_differences = property_differences
        self.request_id = request_id
        self.resource_drift_status = resource_drift_status
        self.resource_type = resource_type
        self.stack_id = stack_id

    def validate(self):
        if self.property_differences:
            for k in self.property_differences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_properties is not None:
            result['ActualProperties'] = self.actual_properties
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.expected_properties is not None:
            result['ExpectedProperties'] = self.expected_properties
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        result['PropertyDifferences'] = []
        if self.property_differences is not None:
            for k in self.property_differences:
                result['PropertyDifferences'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualProperties') is not None:
            self.actual_properties = m.get('ActualProperties')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('ExpectedProperties') is not None:
            self.expected_properties = m.get('ExpectedProperties')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        self.property_differences = []
        if m.get('PropertyDifferences') is not None:
            for k in m.get('PropertyDifferences'):
                temp_model = DetectStackResourceDriftResponseBodyPropertyDifferences()
                self.property_differences.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class DetectStackResourceDriftResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectStackResourceDriftResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DetectStackResourceDriftResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteChangeSetRequest(TeaModel):
    def __init__(
        self,
        change_set_id: str = None,
        client_token: str = None,
        region_id: str = None,
    ):
        self.change_set_id = change_set_id
        self.client_token = client_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ExecuteChangeSetResponseBody(TeaModel):
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


class ExecuteChangeSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteChangeSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ExecuteChangeSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateTemplateByScratchRequest(TeaModel):
    def __init__(
        self,
        provision_region_id: str = None,
        region_id: str = None,
        template_scratch_id: str = None,
    ):
        self.provision_region_id = provision_region_id
        self.region_id = region_id
        self.template_scratch_id = template_scratch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provision_region_id is not None:
            result['ProvisionRegionId'] = self.provision_region_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvisionRegionId') is not None:
            self.provision_region_id = m.get('ProvisionRegionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        return self


class GenerateTemplateByScratchResponseBodyResourcesToImport(TeaModel):
    def __init__(
        self,
        logical_resource_id: str = None,
        resource_identifier: Dict[str, Any] = None,
        resource_type: str = None,
    ):
        self.logical_resource_id = logical_resource_id
        self.resource_identifier = resource_identifier
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.resource_identifier is not None:
            result['ResourceIdentifier'] = self.resource_identifier
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('ResourceIdentifier') is not None:
            self.resource_identifier = m.get('ResourceIdentifier')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GenerateTemplateByScratchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resources_to_import: List[GenerateTemplateByScratchResponseBodyResourcesToImport] = None,
        template_body: str = None,
    ):
        self.request_id = request_id
        self.resources_to_import = resources_to_import
        self.template_body = template_body

    def validate(self):
        if self.resources_to_import:
            for k in self.resources_to_import:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourcesToImport'] = []
        if self.resources_to_import is not None:
            for k in self.resources_to_import:
                result['ResourcesToImport'].append(k.to_map() if k else None)
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources_to_import = []
        if m.get('ResourcesToImport') is not None:
            for k in m.get('ResourcesToImport'):
                temp_model = GenerateTemplateByScratchResponseBodyResourcesToImport()
                self.resources_to_import.append(temp_model.from_map(k))
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        return self


class GenerateTemplateByScratchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateTemplateByScratchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GenerateTemplateByScratchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateTemplatePolicyRequest(TeaModel):
    def __init__(
        self,
        operation_types: List[str] = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.operation_types = operation_types
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_types is not None:
            result['OperationTypes'] = self.operation_types
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationTypes') is not None:
            self.operation_types = m.get('OperationTypes')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GenerateTemplatePolicyResponseBodyPolicyStatement(TeaModel):
    def __init__(
        self,
        action: List[str] = None,
        effect: str = None,
        resource: str = None,
    ):
        self.action = action
        self.effect = effect
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.resource is not None:
            result['Resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        return self


class GenerateTemplatePolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        statement: List[GenerateTemplatePolicyResponseBodyPolicyStatement] = None,
        version: str = None,
    ):
        self.statement = statement
        self.version = version

    def validate(self):
        if self.statement:
            for k in self.statement:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Statement'] = []
        if self.statement is not None:
            for k in self.statement:
                result['Statement'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.statement = []
        if m.get('Statement') is not None:
            for k in m.get('Statement'):
                temp_model = GenerateTemplatePolicyResponseBodyPolicyStatement()
                self.statement.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GenerateTemplatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: GenerateTemplatePolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        self.policy = policy
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = GenerateTemplatePolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateTemplatePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateTemplatePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GenerateTemplatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChangeSetRequest(TeaModel):
    def __init__(
        self,
        change_set_id: str = None,
        region_id: str = None,
        show_template: bool = None,
    ):
        self.change_set_id = change_set_id
        self.region_id = region_id
        self.show_template = show_template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show_template is not None:
            result['ShowTemplate'] = self.show_template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShowTemplate') is not None:
            self.show_template = m.get('ShowTemplate')
        return self


class GetChangeSetResponseBodyLogTerraformLogs(TeaModel):
    def __init__(
        self,
        command: str = None,
        content: str = None,
        stream: str = None,
    ):
        self.command = command
        self.content = content
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.content is not None:
            result['Content'] = self.content
        if self.stream is not None:
            result['Stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        return self


class GetChangeSetResponseBodyLog(TeaModel):
    def __init__(
        self,
        terraform_logs: List[GetChangeSetResponseBodyLogTerraformLogs] = None,
    ):
        self.terraform_logs = terraform_logs

    def validate(self):
        if self.terraform_logs:
            for k in self.terraform_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TerraformLogs'] = []
        if self.terraform_logs is not None:
            for k in self.terraform_logs:
                result['TerraformLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.terraform_logs = []
        if m.get('TerraformLogs') is not None:
            for k in m.get('TerraformLogs'):
                temp_model = GetChangeSetResponseBodyLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k))
        return self


class GetChangeSetResponseBodyParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetChangeSetResponseBody(TeaModel):
    def __init__(
        self,
        change_set_id: str = None,
        change_set_name: str = None,
        change_set_type: str = None,
        changes: List[Dict[str, Any]] = None,
        create_time: str = None,
        description: str = None,
        disable_rollback: bool = None,
        execution_status: str = None,
        log: GetChangeSetResponseBodyLog = None,
        parameters: List[GetChangeSetResponseBodyParameters] = None,
        region_id: str = None,
        request_id: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        template_body: str = None,
        timeout_in_minutes: int = None,
    ):
        self.change_set_id = change_set_id
        self.change_set_name = change_set_name
        self.change_set_type = change_set_type
        self.changes = changes
        self.create_time = create_time
        self.description = description
        self.disable_rollback = disable_rollback
        self.execution_status = execution_status
        self.log = log
        self.parameters = parameters
        self.region_id = region_id
        self.request_id = request_id
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.status = status
        self.status_reason = status_reason
        self.template_body = template_body
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        if self.log:
            self.log.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name
        if self.change_set_type is not None:
            result['ChangeSetType'] = self.change_set_type
        if self.changes is not None:
            result['Changes'] = self.changes
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        if self.log is not None:
            result['Log'] = self.log.to_map()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
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
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')
        if m.get('ChangeSetType') is not None:
            self.change_set_type = m.get('ChangeSetType')
        if m.get('Changes') is not None:
            self.changes = m.get('Changes')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        if m.get('Log') is not None:
            temp_model = GetChangeSetResponseBodyLog()
            self.log = temp_model.from_map(m['Log'])
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetChangeSetResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
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
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        return self


class GetChangeSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChangeSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetChangeSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureDetailsRequest(TeaModel):
    def __init__(
        self,
        feature: str = None,
        region_id: str = None,
    ):
        self.feature = feature
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetFeatureDetailsResponseBodyResourceCleanerSupportedResourceTypes(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        side_effects: List[str] = None,
        supported_filters: List[str] = None,
    ):
        self.resource_type = resource_type
        self.side_effects = side_effects
        self.supported_filters = supported_filters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.side_effects is not None:
            result['SideEffects'] = self.side_effects
        if self.supported_filters is not None:
            result['SupportedFilters'] = self.supported_filters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SideEffects') is not None:
            self.side_effects = m.get('SideEffects')
        if m.get('SupportedFilters') is not None:
            self.supported_filters = m.get('SupportedFilters')
        return self


class GetFeatureDetailsResponseBodyResourceCleaner(TeaModel):
    def __init__(
        self,
        supported_resource_types: List[GetFeatureDetailsResponseBodyResourceCleanerSupportedResourceTypes] = None,
    ):
        self.supported_resource_types = supported_resource_types

    def validate(self):
        if self.supported_resource_types:
            for k in self.supported_resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedResourceTypes'] = []
        if self.supported_resource_types is not None:
            for k in self.supported_resource_types:
                result['SupportedResourceTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_resource_types = []
        if m.get('SupportedResourceTypes') is not None:
            for k in m.get('SupportedResourceTypes'):
                temp_model = GetFeatureDetailsResponseBodyResourceCleanerSupportedResourceTypes()
                self.supported_resource_types.append(temp_model.from_map(k))
        return self


class GetFeatureDetailsResponseBodyTemplateParameterConstraintsSupportedResourceTypes(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetFeatureDetailsResponseBodyTemplateParameterConstraints(TeaModel):
    def __init__(
        self,
        supported_resource_types: List[GetFeatureDetailsResponseBodyTemplateParameterConstraintsSupportedResourceTypes] = None,
    ):
        self.supported_resource_types = supported_resource_types

    def validate(self):
        if self.supported_resource_types:
            for k in self.supported_resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedResourceTypes'] = []
        if self.supported_resource_types is not None:
            for k in self.supported_resource_types:
                result['SupportedResourceTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_resource_types = []
        if m.get('SupportedResourceTypes') is not None:
            for k in m.get('SupportedResourceTypes'):
                temp_model = GetFeatureDetailsResponseBodyTemplateParameterConstraintsSupportedResourceTypes()
                self.supported_resource_types.append(temp_model.from_map(k))
        return self


class GetFeatureDetailsResponseBodyTemplateScratchSupportedResourceTypes(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        source_resource_group_supported: bool = None,
        source_resources_supported: bool = None,
        source_supported: bool = None,
        source_tag_supported: bool = None,
    ):
        self.resource_type = resource_type
        self.source_resource_group_supported = source_resource_group_supported
        self.source_resources_supported = source_resources_supported
        self.source_supported = source_supported
        self.source_tag_supported = source_tag_supported

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_resource_group_supported is not None:
            result['SourceResourceGroupSupported'] = self.source_resource_group_supported
        if self.source_resources_supported is not None:
            result['SourceResourcesSupported'] = self.source_resources_supported
        if self.source_supported is not None:
            result['SourceSupported'] = self.source_supported
        if self.source_tag_supported is not None:
            result['SourceTagSupported'] = self.source_tag_supported
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceResourceGroupSupported') is not None:
            self.source_resource_group_supported = m.get('SourceResourceGroupSupported')
        if m.get('SourceResourcesSupported') is not None:
            self.source_resources_supported = m.get('SourceResourcesSupported')
        if m.get('SourceSupported') is not None:
            self.source_supported = m.get('SourceSupported')
        if m.get('SourceTagSupported') is not None:
            self.source_tag_supported = m.get('SourceTagSupported')
        return self


class GetFeatureDetailsResponseBodyTemplateScratch(TeaModel):
    def __init__(
        self,
        supported_resource_types: List[GetFeatureDetailsResponseBodyTemplateScratchSupportedResourceTypes] = None,
    ):
        self.supported_resource_types = supported_resource_types

    def validate(self):
        if self.supported_resource_types:
            for k in self.supported_resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SupportedResourceTypes'] = []
        if self.supported_resource_types is not None:
            for k in self.supported_resource_types:
                result['SupportedResourceTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_resource_types = []
        if m.get('SupportedResourceTypes') is not None:
            for k in m.get('SupportedResourceTypes'):
                temp_model = GetFeatureDetailsResponseBodyTemplateScratchSupportedResourceTypes()
                self.supported_resource_types.append(temp_model.from_map(k))
        return self


class GetFeatureDetailsResponseBodyTerraformSupportedResourceTypesStackOperationRisk(TeaModel):
    def __init__(
        self,
        delete_stack: List[str] = None,
    ):
        self.delete_stack = delete_stack

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_stack is not None:
            result['DeleteStack'] = self.delete_stack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteStack') is not None:
            self.delete_stack = m.get('DeleteStack')
        return self


class GetFeatureDetailsResponseBodyTerraformSupportedResourceTypes(TeaModel):
    def __init__(
        self,
        custom_tag: List[str] = None,
        estimate_cost: List[str] = None,
        resource_group: List[str] = None,
        stack_operation_risk: GetFeatureDetailsResponseBodyTerraformSupportedResourceTypesStackOperationRisk = None,
        system_tag: List[str] = None,
    ):
        self.custom_tag = custom_tag
        self.estimate_cost = estimate_cost
        self.resource_group = resource_group
        self.stack_operation_risk = stack_operation_risk
        self.system_tag = system_tag

    def validate(self):
        if self.stack_operation_risk:
            self.stack_operation_risk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_tag is not None:
            result['CustomTag'] = self.custom_tag
        if self.estimate_cost is not None:
            result['EstimateCost'] = self.estimate_cost
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.stack_operation_risk is not None:
            result['StackOperationRisk'] = self.stack_operation_risk.to_map()
        if self.system_tag is not None:
            result['SystemTag'] = self.system_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomTag') is not None:
            self.custom_tag = m.get('CustomTag')
        if m.get('EstimateCost') is not None:
            self.estimate_cost = m.get('EstimateCost')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('StackOperationRisk') is not None:
            temp_model = GetFeatureDetailsResponseBodyTerraformSupportedResourceTypesStackOperationRisk()
            self.stack_operation_risk = temp_model.from_map(m['StackOperationRisk'])
        if m.get('SystemTag') is not None:
            self.system_tag = m.get('SystemTag')
        return self


class GetFeatureDetailsResponseBodyTerraformSupportedVersionsProviderVersions(TeaModel):
    def __init__(
        self,
        provider_name: str = None,
        supported_versions: List[str] = None,
    ):
        self.provider_name = provider_name
        self.supported_versions = supported_versions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        if self.supported_versions is not None:
            result['SupportedVersions'] = self.supported_versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        if m.get('SupportedVersions') is not None:
            self.supported_versions = m.get('SupportedVersions')
        return self


class GetFeatureDetailsResponseBodyTerraformSupportedVersions(TeaModel):
    def __init__(
        self,
        provider_versions: List[GetFeatureDetailsResponseBodyTerraformSupportedVersionsProviderVersions] = None,
        terraform_version: str = None,
        transform: str = None,
        update_allowed_transforms: List[str] = None,
    ):
        self.provider_versions = provider_versions
        self.terraform_version = terraform_version
        self.transform = transform
        self.update_allowed_transforms = update_allowed_transforms

    def validate(self):
        if self.provider_versions:
            for k in self.provider_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProviderVersions'] = []
        if self.provider_versions is not None:
            for k in self.provider_versions:
                result['ProviderVersions'].append(k.to_map() if k else None)
        if self.terraform_version is not None:
            result['TerraformVersion'] = self.terraform_version
        if self.transform is not None:
            result['Transform'] = self.transform
        if self.update_allowed_transforms is not None:
            result['UpdateAllowedTransforms'] = self.update_allowed_transforms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.provider_versions = []
        if m.get('ProviderVersions') is not None:
            for k in m.get('ProviderVersions'):
                temp_model = GetFeatureDetailsResponseBodyTerraformSupportedVersionsProviderVersions()
                self.provider_versions.append(temp_model.from_map(k))
        if m.get('TerraformVersion') is not None:
            self.terraform_version = m.get('TerraformVersion')
        if m.get('Transform') is not None:
            self.transform = m.get('Transform')
        if m.get('UpdateAllowedTransforms') is not None:
            self.update_allowed_transforms = m.get('UpdateAllowedTransforms')
        return self


class GetFeatureDetailsResponseBodyTerraform(TeaModel):
    def __init__(
        self,
        supported_resource_types: GetFeatureDetailsResponseBodyTerraformSupportedResourceTypes = None,
        supported_versions: List[GetFeatureDetailsResponseBodyTerraformSupportedVersions] = None,
    ):
        self.supported_resource_types = supported_resource_types
        self.supported_versions = supported_versions

    def validate(self):
        if self.supported_resource_types:
            self.supported_resource_types.validate()
        if self.supported_versions:
            for k in self.supported_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_resource_types is not None:
            result['SupportedResourceTypes'] = self.supported_resource_types.to_map()
        result['SupportedVersions'] = []
        if self.supported_versions is not None:
            for k in self.supported_versions:
                result['SupportedVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedResourceTypes') is not None:
            temp_model = GetFeatureDetailsResponseBodyTerraformSupportedResourceTypes()
            self.supported_resource_types = temp_model.from_map(m['SupportedResourceTypes'])
        self.supported_versions = []
        if m.get('SupportedVersions') is not None:
            for k in m.get('SupportedVersions'):
                temp_model = GetFeatureDetailsResponseBodyTerraformSupportedVersions()
                self.supported_versions.append(temp_model.from_map(k))
        return self


class GetFeatureDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_cleaner: GetFeatureDetailsResponseBodyResourceCleaner = None,
        template_parameter_constraints: GetFeatureDetailsResponseBodyTemplateParameterConstraints = None,
        template_scratch: GetFeatureDetailsResponseBodyTemplateScratch = None,
        terraform: GetFeatureDetailsResponseBodyTerraform = None,
    ):
        self.request_id = request_id
        self.resource_cleaner = resource_cleaner
        self.template_parameter_constraints = template_parameter_constraints
        self.template_scratch = template_scratch
        self.terraform = terraform

    def validate(self):
        if self.resource_cleaner:
            self.resource_cleaner.validate()
        if self.template_parameter_constraints:
            self.template_parameter_constraints.validate()
        if self.template_scratch:
            self.template_scratch.validate()
        if self.terraform:
            self.terraform.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_cleaner is not None:
            result['ResourceCleaner'] = self.resource_cleaner.to_map()
        if self.template_parameter_constraints is not None:
            result['TemplateParameterConstraints'] = self.template_parameter_constraints.to_map()
        if self.template_scratch is not None:
            result['TemplateScratch'] = self.template_scratch.to_map()
        if self.terraform is not None:
            result['Terraform'] = self.terraform.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceCleaner') is not None:
            temp_model = GetFeatureDetailsResponseBodyResourceCleaner()
            self.resource_cleaner = temp_model.from_map(m['ResourceCleaner'])
        if m.get('TemplateParameterConstraints') is not None:
            temp_model = GetFeatureDetailsResponseBodyTemplateParameterConstraints()
            self.template_parameter_constraints = temp_model.from_map(m['TemplateParameterConstraints'])
        if m.get('TemplateScratch') is not None:
            temp_model = GetFeatureDetailsResponseBodyTemplateScratch()
            self.template_scratch = temp_model.from_map(m['TemplateScratch'])
        if m.get('Terraform') is not None:
            temp_model = GetFeatureDetailsResponseBodyTerraform()
            self.terraform = temp_model.from_map(m['Terraform'])
        return self


class GetFeatureDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFeatureDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetFeatureDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceTypeRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        entity_type: str = None,
        properties: Dict[str, Any] = None,
        request_id: str = None,
        resource_type: str = None,
        support_drift_detection: bool = None,
        support_scratch_detection: bool = None,
    ):
        self.attributes = attributes
        self.entity_type = entity_type
        self.properties = properties
        self.request_id = request_id
        self.resource_type = resource_type
        self.support_drift_detection = support_drift_detection
        self.support_scratch_detection = support_scratch_detection

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.support_drift_detection is not None:
            result['SupportDriftDetection'] = self.support_drift_detection
        if self.support_scratch_detection is not None:
            result['SupportScratchDetection'] = self.support_scratch_detection
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SupportDriftDetection') is not None:
            self.support_drift_detection = m.get('SupportDriftDetection')
        if m.get('SupportScratchDetection') is not None:
            self.support_scratch_detection = m.get('SupportScratchDetection')
        return self


class GetResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceTypeTemplateRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetResourceTypeTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_body: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.template_body = template_body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetResourceTypeTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceTypeTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetResourceTypeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceProvisionsRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetServiceProvisionsRequestServices(TeaModel):
    def __init__(
        self,
        service_name: str = None,
    ):
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GetServiceProvisionsRequest(TeaModel):
    def __init__(
        self,
        parameters: List[GetServiceProvisionsRequestParameters] = None,
        region_id: str = None,
        services: List[GetServiceProvisionsRequestServices] = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.parameters = parameters
        self.region_id = region_id
        self.services = services
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetServiceProvisionsRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = GetServiceProvisionsRequestServices()
                self.services.append(temp_model.from_map(k))
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRolesApiForCreation(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_product_id: str = None,
        api_type: str = None,
        parameters: Dict[str, Any] = None,
    ):
        self.api_name = api_name
        self.api_product_id = api_product_id
        self.api_type = api_type
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_product_id is not None:
            result['ApiProductId'] = self.api_product_id
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiProductId') is not None:
            self.api_product_id = m.get('ApiProductId')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRoles(TeaModel):
    def __init__(
        self,
        api_for_creation: GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRolesApiForCreation = None,
        created: bool = None,
        function: str = None,
        role_name: str = None,
    ):
        self.api_for_creation = api_for_creation
        self.created = created
        self.function = function
        self.role_name = role_name

    def validate(self):
        if self.api_for_creation:
            self.api_for_creation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_for_creation is not None:
            result['ApiForCreation'] = self.api_for_creation.to_map()
        if self.created is not None:
            result['Created'] = self.created
        if self.function is not None:
            result['Function'] = self.function
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiForCreation') is not None:
            temp_model = GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRolesApiForCreation()
            self.api_for_creation = temp_model.from_map(m['ApiForCreation'])
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Function') is not None:
            self.function = m.get('Function')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetServiceProvisionsResponseBodyServiceProvisionsRoleProvision(TeaModel):
    def __init__(
        self,
        authorization_url: str = None,
        roles: List[GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRoles] = None,
    ):
        self.authorization_url = authorization_url
        self.roles = roles

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_url is not None:
            result['AuthorizationURL'] = self.authorization_url
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationURL') is not None:
            self.authorization_url = m.get('AuthorizationURL')
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRoles()
                self.roles.append(temp_model.from_map(k))
        return self


class GetServiceProvisionsResponseBodyServiceProvisions(TeaModel):
    def __init__(
        self,
        auto_enable_service: bool = None,
        dependent_service_names: List[str] = None,
        enable_url: str = None,
        role_provision: GetServiceProvisionsResponseBodyServiceProvisionsRoleProvision = None,
        service_name: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.auto_enable_service = auto_enable_service
        self.dependent_service_names = dependent_service_names
        self.enable_url = enable_url
        self.role_provision = role_provision
        self.service_name = service_name
        self.status = status
        self.status_reason = status_reason

    def validate(self):
        if self.role_provision:
            self.role_provision.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_enable_service is not None:
            result['AutoEnableService'] = self.auto_enable_service
        if self.dependent_service_names is not None:
            result['DependentServiceNames'] = self.dependent_service_names
        if self.enable_url is not None:
            result['EnableURL'] = self.enable_url
        if self.role_provision is not None:
            result['RoleProvision'] = self.role_provision.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoEnableService') is not None:
            self.auto_enable_service = m.get('AutoEnableService')
        if m.get('DependentServiceNames') is not None:
            self.dependent_service_names = m.get('DependentServiceNames')
        if m.get('EnableURL') is not None:
            self.enable_url = m.get('EnableURL')
        if m.get('RoleProvision') is not None:
            temp_model = GetServiceProvisionsResponseBodyServiceProvisionsRoleProvision()
            self.role_provision = temp_model.from_map(m['RoleProvision'])
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class GetServiceProvisionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_provisions: List[GetServiceProvisionsResponseBodyServiceProvisions] = None,
    ):
        self.request_id = request_id
        self.service_provisions = service_provisions

    def validate(self):
        if self.service_provisions:
            for k in self.service_provisions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceProvisions'] = []
        if self.service_provisions is not None:
            for k in self.service_provisions:
                result['ServiceProvisions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_provisions = []
        if m.get('ServiceProvisions') is not None:
            for k in m.get('ServiceProvisions'):
                temp_model = GetServiceProvisionsResponseBodyServiceProvisions()
                self.service_provisions.append(temp_model.from_map(k))
        return self


class GetServiceProvisionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceProvisionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetServiceProvisionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        log_option: str = None,
        output_option: str = None,
        region_id: str = None,
        show_resource_progress: str = None,
        stack_id: str = None,
    ):
        self.client_token = client_token
        self.log_option = log_option
        self.output_option = output_option
        self.region_id = region_id
        self.show_resource_progress = show_resource_progress
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.log_option is not None:
            result['LogOption'] = self.log_option
        if self.output_option is not None:
            result['OutputOption'] = self.output_option
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show_resource_progress is not None:
            result['ShowResourceProgress'] = self.show_resource_progress
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LogOption') is not None:
            self.log_option = m.get('LogOption')
        if m.get('OutputOption') is not None:
            self.output_option = m.get('OutputOption')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShowResourceProgress') is not None:
            self.show_resource_progress = m.get('ShowResourceProgress')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class GetStackResponseBodyLogResourceLogsLogs(TeaModel):
    def __init__(
        self,
        content: str = None,
        keys: List[str] = None,
    ):
        self.content = content
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class GetStackResponseBodyLogResourceLogs(TeaModel):
    def __init__(
        self,
        logs: List[GetStackResponseBodyLogResourceLogsLogs] = None,
        resource_name: str = None,
    ):
        self.logs = logs
        self.resource_name = resource_name

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = GetStackResponseBodyLogResourceLogsLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class GetStackResponseBodyLogTerraformLogs(TeaModel):
    def __init__(
        self,
        command: str = None,
        content: str = None,
        stream: str = None,
    ):
        self.command = command
        self.content = content
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.content is not None:
            result['Content'] = self.content
        if self.stream is not None:
            result['Stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        return self


class GetStackResponseBodyLog(TeaModel):
    def __init__(
        self,
        resource_logs: List[GetStackResponseBodyLogResourceLogs] = None,
        terraform_logs: List[GetStackResponseBodyLogTerraformLogs] = None,
    ):
        self.resource_logs = resource_logs
        self.terraform_logs = terraform_logs

    def validate(self):
        if self.resource_logs:
            for k in self.resource_logs:
                if k:
                    k.validate()
        if self.terraform_logs:
            for k in self.terraform_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceLogs'] = []
        if self.resource_logs is not None:
            for k in self.resource_logs:
                result['ResourceLogs'].append(k.to_map() if k else None)
        result['TerraformLogs'] = []
        if self.terraform_logs is not None:
            for k in self.terraform_logs:
                result['TerraformLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_logs = []
        if m.get('ResourceLogs') is not None:
            for k in m.get('ResourceLogs'):
                temp_model = GetStackResponseBodyLogResourceLogs()
                self.resource_logs.append(temp_model.from_map(k))
        self.terraform_logs = []
        if m.get('TerraformLogs') is not None:
            for k in m.get('TerraformLogs'):
                temp_model = GetStackResponseBodyLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k))
        return self


class GetStackResponseBodyOperationInfo(TeaModel):
    def __init__(
        self,
        action: str = None,
        code: str = None,
        logical_resource_id: str = None,
        message: str = None,
        request_id: str = None,
        resource_type: str = None,
    ):
        self.action = action
        self.code = code
        self.logical_resource_id = logical_resource_id
        self.message = message
        self.request_id = request_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.code is not None:
            result['Code'] = self.code
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetStackResponseBodyParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetStackResponseBodyResourceProgressInProgressResourceDetails(TeaModel):
    def __init__(
        self,
        progress_target_value: float = None,
        progress_value: float = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.progress_target_value = progress_target_value
        self.progress_value = progress_value
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress_target_value is not None:
            result['ProgressTargetValue'] = self.progress_target_value
        if self.progress_value is not None:
            result['ProgressValue'] = self.progress_value
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProgressTargetValue') is not None:
            self.progress_target_value = m.get('ProgressTargetValue')
        if m.get('ProgressValue') is not None:
            self.progress_value = m.get('ProgressValue')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetStackResponseBodyResourceProgress(TeaModel):
    def __init__(
        self,
        failed_resource_count: int = None,
        in_progress_resource_count: int = None,
        in_progress_resource_details: List[GetStackResponseBodyResourceProgressInProgressResourceDetails] = None,
        pending_resource_count: int = None,
        success_resource_count: int = None,
        total_resource_count: int = None,
    ):
        self.failed_resource_count = failed_resource_count
        self.in_progress_resource_count = in_progress_resource_count
        self.in_progress_resource_details = in_progress_resource_details
        self.pending_resource_count = pending_resource_count
        self.success_resource_count = success_resource_count
        self.total_resource_count = total_resource_count

    def validate(self):
        if self.in_progress_resource_details:
            for k in self.in_progress_resource_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_resource_count is not None:
            result['FailedResourceCount'] = self.failed_resource_count
        if self.in_progress_resource_count is not None:
            result['InProgressResourceCount'] = self.in_progress_resource_count
        result['InProgressResourceDetails'] = []
        if self.in_progress_resource_details is not None:
            for k in self.in_progress_resource_details:
                result['InProgressResourceDetails'].append(k.to_map() if k else None)
        if self.pending_resource_count is not None:
            result['PendingResourceCount'] = self.pending_resource_count
        if self.success_resource_count is not None:
            result['SuccessResourceCount'] = self.success_resource_count
        if self.total_resource_count is not None:
            result['TotalResourceCount'] = self.total_resource_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedResourceCount') is not None:
            self.failed_resource_count = m.get('FailedResourceCount')
        if m.get('InProgressResourceCount') is not None:
            self.in_progress_resource_count = m.get('InProgressResourceCount')
        self.in_progress_resource_details = []
        if m.get('InProgressResourceDetails') is not None:
            for k in m.get('InProgressResourceDetails'):
                temp_model = GetStackResponseBodyResourceProgressInProgressResourceDetails()
                self.in_progress_resource_details.append(temp_model.from_map(k))
        if m.get('PendingResourceCount') is not None:
            self.pending_resource_count = m.get('PendingResourceCount')
        if m.get('SuccessResourceCount') is not None:
            self.success_resource_count = m.get('SuccessResourceCount')
        if m.get('TotalResourceCount') is not None:
            self.total_resource_count = m.get('TotalResourceCount')
        return self


class GetStackResponseBodyTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetStackResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_protection: str = None,
        description: str = None,
        disable_rollback: bool = None,
        drift_detection_time: str = None,
        interface: str = None,
        log: GetStackResponseBodyLog = None,
        notification_urls: List[str] = None,
        operation_info: GetStackResponseBodyOperationInfo = None,
        outputs: List[Dict[str, Any]] = None,
        parameters: List[GetStackResponseBodyParameters] = None,
        parent_stack_id: str = None,
        ram_role_name: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resource_progress: GetStackResponseBodyResourceProgress = None,
        root_stack_id: str = None,
        service_managed: bool = None,
        service_name: str = None,
        stack_drift_status: str = None,
        stack_id: str = None,
        stack_name: str = None,
        stack_type: str = None,
        status: str = None,
        status_reason: str = None,
        tags: List[GetStackResponseBodyTags] = None,
        template_description: str = None,
        template_id: str = None,
        template_scratch_id: str = None,
        template_url: str = None,
        template_version: str = None,
        timeout_in_minutes: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.deletion_protection = deletion_protection
        self.description = description
        self.disable_rollback = disable_rollback
        self.drift_detection_time = drift_detection_time
        self.interface = interface
        self.log = log
        self.notification_urls = notification_urls
        self.operation_info = operation_info
        self.outputs = outputs
        self.parameters = parameters
        self.parent_stack_id = parent_stack_id
        self.ram_role_name = ram_role_name
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.resource_progress = resource_progress
        self.root_stack_id = root_stack_id
        self.service_managed = service_managed
        self.service_name = service_name
        self.stack_drift_status = stack_drift_status
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.stack_type = stack_type
        self.status = status
        self.status_reason = status_reason
        self.tags = tags
        self.template_description = template_description
        self.template_id = template_id
        self.template_scratch_id = template_scratch_id
        self.template_url = template_url
        self.template_version = template_version
        self.timeout_in_minutes = timeout_in_minutes
        self.update_time = update_time

    def validate(self):
        if self.log:
            self.log.validate()
        if self.operation_info:
            self.operation_info.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.resource_progress:
            self.resource_progress.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.interface is not None:
            result['Interface'] = self.interface
        if self.log is not None:
            result['Log'] = self.log.to_map()
        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls
        if self.operation_info is not None:
            result['OperationInfo'] = self.operation_info.to_map()
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_progress is not None:
            result['ResourceProgress'] = self.resource_progress.to_map()
        if self.root_stack_id is not None:
            result['RootStackId'] = self.root_stack_id
        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.stack_type is not None:
            result['StackType'] = self.stack_type
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('Interface') is not None:
            self.interface = m.get('Interface')
        if m.get('Log') is not None:
            temp_model = GetStackResponseBodyLog()
            self.log = temp_model.from_map(m['Log'])
        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')
        if m.get('OperationInfo') is not None:
            temp_model = GetStackResponseBodyOperationInfo()
            self.operation_info = temp_model.from_map(m['OperationInfo'])
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetStackResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceProgress') is not None:
            temp_model = GetStackResponseBodyResourceProgress()
            self.resource_progress = temp_model.from_map(m['ResourceProgress'])
        if m.get('RootStackId') is not None:
            self.root_stack_id = m.get('RootStackId')
        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('StackType') is not None:
            self.stack_type = m.get('StackType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetStackResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetStackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackDriftDetectionStatusRequest(TeaModel):
    def __init__(
        self,
        drift_detection_id: str = None,
        region_id: str = None,
    ):
        self.drift_detection_id = drift_detection_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriftDetectionId') is not None:
            self.drift_detection_id = m.get('DriftDetectionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetStackDriftDetectionStatusResponseBody(TeaModel):
    def __init__(
        self,
        drift_detection_id: str = None,
        drift_detection_status: str = None,
        drift_detection_status_reason: str = None,
        drift_detection_time: str = None,
        drifted_stack_resource_count: int = None,
        request_id: str = None,
        stack_drift_status: str = None,
        stack_id: str = None,
    ):
        self.drift_detection_id = drift_detection_id
        self.drift_detection_status = drift_detection_status
        self.drift_detection_status_reason = drift_detection_status_reason
        self.drift_detection_time = drift_detection_time
        self.drifted_stack_resource_count = drifted_stack_resource_count
        self.request_id = request_id
        self.stack_drift_status = stack_drift_status
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drift_detection_id is not None:
            result['DriftDetectionId'] = self.drift_detection_id
        if self.drift_detection_status is not None:
            result['DriftDetectionStatus'] = self.drift_detection_status
        if self.drift_detection_status_reason is not None:
            result['DriftDetectionStatusReason'] = self.drift_detection_status_reason
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.drifted_stack_resource_count is not None:
            result['DriftedStackResourceCount'] = self.drifted_stack_resource_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriftDetectionId') is not None:
            self.drift_detection_id = m.get('DriftDetectionId')
        if m.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = m.get('DriftDetectionStatus')
        if m.get('DriftDetectionStatusReason') is not None:
            self.drift_detection_status_reason = m.get('DriftDetectionStatusReason')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('DriftedStackResourceCount') is not None:
            self.drifted_stack_resource_count = m.get('DriftedStackResourceCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class GetStackDriftDetectionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStackDriftDetectionStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetStackDriftDetectionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
    ):
        self.region_id = region_id
        self.stack_group_id = stack_group_id
        self.stack_group_name = stack_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class GetStackGroupResponseBodyStackGroupAutoDeployment(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        retain_stacks_on_account_removal: bool = None,
    ):
        self.enabled = enabled
        self.retain_stacks_on_account_removal = retain_stacks_on_account_removal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.retain_stacks_on_account_removal is not None:
            result['RetainStacksOnAccountRemoval'] = self.retain_stacks_on_account_removal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RetainStacksOnAccountRemoval') is not None:
            self.retain_stacks_on_account_removal = m.get('RetainStacksOnAccountRemoval')
        return self


class GetStackGroupResponseBodyStackGroupParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetStackGroupResponseBodyStackGroupStackGroupDriftDetectionDetail(TeaModel):
    def __init__(
        self,
        cancelled_stack_instances_count: int = None,
        drift_detection_status: str = None,
        drift_detection_time: str = None,
        drifted_stack_instances_count: int = None,
        failed_stack_instances_count: int = None,
        in_progress_stack_instances_count: int = None,
        in_sync_stack_instances_count: int = None,
        stack_group_drift_status: str = None,
        total_stack_instances_count: int = None,
    ):
        self.cancelled_stack_instances_count = cancelled_stack_instances_count
        self.drift_detection_status = drift_detection_status
        self.drift_detection_time = drift_detection_time
        self.drifted_stack_instances_count = drifted_stack_instances_count
        self.failed_stack_instances_count = failed_stack_instances_count
        self.in_progress_stack_instances_count = in_progress_stack_instances_count
        self.in_sync_stack_instances_count = in_sync_stack_instances_count
        self.stack_group_drift_status = stack_group_drift_status
        self.total_stack_instances_count = total_stack_instances_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cancelled_stack_instances_count is not None:
            result['CancelledStackInstancesCount'] = self.cancelled_stack_instances_count
        if self.drift_detection_status is not None:
            result['DriftDetectionStatus'] = self.drift_detection_status
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.drifted_stack_instances_count is not None:
            result['DriftedStackInstancesCount'] = self.drifted_stack_instances_count
        if self.failed_stack_instances_count is not None:
            result['FailedStackInstancesCount'] = self.failed_stack_instances_count
        if self.in_progress_stack_instances_count is not None:
            result['InProgressStackInstancesCount'] = self.in_progress_stack_instances_count
        if self.in_sync_stack_instances_count is not None:
            result['InSyncStackInstancesCount'] = self.in_sync_stack_instances_count
        if self.stack_group_drift_status is not None:
            result['StackGroupDriftStatus'] = self.stack_group_drift_status
        if self.total_stack_instances_count is not None:
            result['TotalStackInstancesCount'] = self.total_stack_instances_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelledStackInstancesCount') is not None:
            self.cancelled_stack_instances_count = m.get('CancelledStackInstancesCount')
        if m.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = m.get('DriftDetectionStatus')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('DriftedStackInstancesCount') is not None:
            self.drifted_stack_instances_count = m.get('DriftedStackInstancesCount')
        if m.get('FailedStackInstancesCount') is not None:
            self.failed_stack_instances_count = m.get('FailedStackInstancesCount')
        if m.get('InProgressStackInstancesCount') is not None:
            self.in_progress_stack_instances_count = m.get('InProgressStackInstancesCount')
        if m.get('InSyncStackInstancesCount') is not None:
            self.in_sync_stack_instances_count = m.get('InSyncStackInstancesCount')
        if m.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = m.get('StackGroupDriftStatus')
        if m.get('TotalStackInstancesCount') is not None:
            self.total_stack_instances_count = m.get('TotalStackInstancesCount')
        return self


class GetStackGroupResponseBodyStackGroup(TeaModel):
    def __init__(
        self,
        administration_role_name: str = None,
        auto_deployment: GetStackGroupResponseBodyStackGroupAutoDeployment = None,
        description: str = None,
        execution_role_name: str = None,
        parameters: List[GetStackGroupResponseBodyStackGroupParameters] = None,
        permission_model: str = None,
        rd_folder_ids: List[str] = None,
        resource_group_id: str = None,
        stack_group_drift_detection_detail: GetStackGroupResponseBodyStackGroupStackGroupDriftDetectionDetail = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
        status: str = None,
        template_body: str = None,
    ):
        self.administration_role_name = administration_role_name
        self.auto_deployment = auto_deployment
        self.description = description
        self.execution_role_name = execution_role_name
        self.parameters = parameters
        self.permission_model = permission_model
        self.rd_folder_ids = rd_folder_ids
        self.resource_group_id = resource_group_id
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail
        self.stack_group_id = stack_group_id
        self.stack_group_name = stack_group_name
        self.status = status
        self.template_body = template_body

    def validate(self):
        if self.auto_deployment:
            self.auto_deployment.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.stack_group_drift_detection_detail:
            self.stack_group_drift_detection_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.auto_deployment is not None:
            result['AutoDeployment'] = self.auto_deployment.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.stack_group_drift_detection_detail is not None:
            result['StackGroupDriftDetectionDetail'] = self.stack_group_drift_detection_detail.to_map()
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.status is not None:
            result['Status'] = self.status
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('AutoDeployment') is not None:
            temp_model = GetStackGroupResponseBodyStackGroupAutoDeployment()
            self.auto_deployment = temp_model.from_map(m['AutoDeployment'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetStackGroupResponseBodyStackGroupParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StackGroupDriftDetectionDetail') is not None:
            temp_model = GetStackGroupResponseBodyStackGroupStackGroupDriftDetectionDetail()
            self.stack_group_drift_detection_detail = temp_model.from_map(m['StackGroupDriftDetectionDetail'])
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        return self


class GetStackGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_group: GetStackGroupResponseBodyStackGroup = None,
    ):
        self.request_id = request_id
        self.stack_group = stack_group

    def validate(self):
        if self.stack_group:
            self.stack_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetStackGroupResponseBodyStackGroup()
            self.stack_group = temp_model.from_map(m['StackGroup'])
        return self


class GetStackGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStackGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetStackGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackGroupOperationRequest(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        region_id: str = None,
    ):
        self.operation_id = operation_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetStackGroupOperationResponseBodyStackGroupOperationDeploymentTargets(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        rd_folder_ids: List[str] = None,
    ):
        self.account_ids = account_ids
        # test
        self.rd_folder_ids = rd_folder_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        return self


class GetStackGroupOperationResponseBodyStackGroupOperationOperationPreferences(TeaModel):
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
        # test
        self.region_ids_order = region_ids_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetStackGroupOperationResponseBodyStackGroupOperationStackGroupDriftDetectionDetail(TeaModel):
    def __init__(
        self,
        cancelled_stack_instances_count: int = None,
        drift_detection_status: str = None,
        drift_detection_time: str = None,
        drifted_stack_instances_count: int = None,
        failed_stack_instances_count: int = None,
        in_progress_stack_instances_count: int = None,
        in_sync_stack_instances_count: int = None,
        stack_group_drift_status: str = None,
        total_stack_instances_count: int = None,
    ):
        self.cancelled_stack_instances_count = cancelled_stack_instances_count
        self.drift_detection_status = drift_detection_status
        self.drift_detection_time = drift_detection_time
        self.drifted_stack_instances_count = drifted_stack_instances_count
        self.failed_stack_instances_count = failed_stack_instances_count
        self.in_progress_stack_instances_count = in_progress_stack_instances_count
        self.in_sync_stack_instances_count = in_sync_stack_instances_count
        self.stack_group_drift_status = stack_group_drift_status
        self.total_stack_instances_count = total_stack_instances_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cancelled_stack_instances_count is not None:
            result['CancelledStackInstancesCount'] = self.cancelled_stack_instances_count
        if self.drift_detection_status is not None:
            result['DriftDetectionStatus'] = self.drift_detection_status
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.drifted_stack_instances_count is not None:
            result['DriftedStackInstancesCount'] = self.drifted_stack_instances_count
        if self.failed_stack_instances_count is not None:
            result['FailedStackInstancesCount'] = self.failed_stack_instances_count
        if self.in_progress_stack_instances_count is not None:
            result['InProgressStackInstancesCount'] = self.in_progress_stack_instances_count
        if self.in_sync_stack_instances_count is not None:
            result['InSyncStackInstancesCount'] = self.in_sync_stack_instances_count
        if self.stack_group_drift_status is not None:
            result['StackGroupDriftStatus'] = self.stack_group_drift_status
        if self.total_stack_instances_count is not None:
            result['TotalStackInstancesCount'] = self.total_stack_instances_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelledStackInstancesCount') is not None:
            self.cancelled_stack_instances_count = m.get('CancelledStackInstancesCount')
        if m.get('DriftDetectionStatus') is not None:
            self.drift_detection_status = m.get('DriftDetectionStatus')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('DriftedStackInstancesCount') is not None:
            self.drifted_stack_instances_count = m.get('DriftedStackInstancesCount')
        if m.get('FailedStackInstancesCount') is not None:
            self.failed_stack_instances_count = m.get('FailedStackInstancesCount')
        if m.get('InProgressStackInstancesCount') is not None:
            self.in_progress_stack_instances_count = m.get('InProgressStackInstancesCount')
        if m.get('InSyncStackInstancesCount') is not None:
            self.in_sync_stack_instances_count = m.get('InSyncStackInstancesCount')
        if m.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = m.get('StackGroupDriftStatus')
        if m.get('TotalStackInstancesCount') is not None:
            self.total_stack_instances_count = m.get('TotalStackInstancesCount')
        return self


class GetStackGroupOperationResponseBodyStackGroupOperation(TeaModel):
    def __init__(
        self,
        action: str = None,
        administration_role_name: str = None,
        create_time: str = None,
        deployment_targets: GetStackGroupOperationResponseBodyStackGroupOperationDeploymentTargets = None,
        end_time: str = None,
        execution_role_name: str = None,
        operation_description: str = None,
        operation_id: str = None,
        operation_preferences: GetStackGroupOperationResponseBodyStackGroupOperationOperationPreferences = None,
        retain_stacks: bool = None,
        stack_group_drift_detection_detail: GetStackGroupOperationResponseBodyStackGroupOperationStackGroupDriftDetectionDetail = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
        status: str = None,
    ):
        self.action = action
        self.administration_role_name = administration_role_name
        self.create_time = create_time
        self.deployment_targets = deployment_targets
        self.end_time = end_time
        self.execution_role_name = execution_role_name
        self.operation_description = operation_description
        self.operation_id = operation_id
        self.operation_preferences = operation_preferences
        self.retain_stacks = retain_stacks
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail
        self.stack_group_id = stack_group_id
        self.stack_group_name = stack_group_name
        self.status = status

    def validate(self):
        if self.deployment_targets:
            self.deployment_targets.validate()
        if self.operation_preferences:
            self.operation_preferences.validate()
        if self.stack_group_drift_detection_detail:
            self.stack_group_drift_detection_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences.to_map()
        if self.retain_stacks is not None:
            result['RetainStacks'] = self.retain_stacks
        if self.stack_group_drift_detection_detail is not None:
            result['StackGroupDriftDetectionDetail'] = self.stack_group_drift_detection_detail.to_map()
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeploymentTargets') is not None:
            temp_model = GetStackGroupOperationResponseBodyStackGroupOperationDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m['DeploymentTargets'])
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('OperationPreferences') is not None:
            temp_model = GetStackGroupOperationResponseBodyStackGroupOperationOperationPreferences()
            self.operation_preferences = temp_model.from_map(m['OperationPreferences'])
        if m.get('RetainStacks') is not None:
            self.retain_stacks = m.get('RetainStacks')
        if m.get('StackGroupDriftDetectionDetail') is not None:
            temp_model = GetStackGroupOperationResponseBodyStackGroupOperationStackGroupDriftDetectionDetail()
            self.stack_group_drift_detection_detail = temp_model.from_map(m['StackGroupDriftDetectionDetail'])
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetStackGroupOperationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_group_operation: GetStackGroupOperationResponseBodyStackGroupOperation = None,
    ):
        self.request_id = request_id
        self.stack_group_operation = stack_group_operation

    def validate(self):
        if self.stack_group_operation:
            self.stack_group_operation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetStackGroupOperationResponseBodyStackGroupOperation()
            self.stack_group_operation = temp_model.from_map(m['StackGroupOperation'])
        return self


class GetStackGroupOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStackGroupOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetStackGroupOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetStackInstanceResponseBodyStackInstanceParameterOverrides(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetStackInstanceResponseBodyStackInstance(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        drift_detection_time: str = None,
        parameter_overrides: List[GetStackInstanceResponseBodyStackInstanceParameterOverrides] = None,
        rd_folder_id: str = None,
        region_id: str = None,
        stack_drift_status: str = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
        stack_id: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.account_id = account_id
        self.drift_detection_time = drift_detection_time
        self.parameter_overrides = parameter_overrides
        self.rd_folder_id = rd_folder_id
        self.region_id = region_id
        self.stack_drift_status = stack_drift_status
        self.stack_group_id = stack_group_id
        self.stack_group_name = stack_group_name
        self.stack_id = stack_id
        self.status = status
        self.status_reason = status_reason

    def validate(self):
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.rd_folder_id is not None:
            result['RdFolderId'] = self.rd_folder_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = GetStackInstanceResponseBodyStackInstanceParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('RdFolderId') is not None:
            self.rd_folder_id = m.get('RdFolderId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class GetStackInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_instance: GetStackInstanceResponseBodyStackInstance = None,
    ):
        self.request_id = request_id
        self.stack_instance = stack_instance

    def validate(self):
        if self.stack_instance:
            self.stack_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetStackInstanceResponseBodyStackInstance()
            self.stack_instance = temp_model.from_map(m['StackInstance'])
        return self


class GetStackInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStackInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetStackInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackPolicyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_id: str = None,
    ):
        self.region_id = region_id
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class GetStackPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_policy_body: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.stack_policy_body = stack_policy_body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetStackPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStackPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetStackPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackResourceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        logical_resource_id: str = None,
        region_id: str = None,
        resource_attributes: List[str] = None,
        show_resource_attributes: bool = None,
        stack_id: str = None,
    ):
        self.client_token = client_token
        self.logical_resource_id = logical_resource_id
        self.region_id = region_id
        self.resource_attributes = resource_attributes
        self.show_resource_attributes = show_resource_attributes
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_attributes is not None:
            result['ResourceAttributes'] = self.resource_attributes
        if self.show_resource_attributes is not None:
            result['ShowResourceAttributes'] = self.show_resource_attributes
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceAttributes') is not None:
            self.resource_attributes = m.get('ResourceAttributes')
        if m.get('ShowResourceAttributes') is not None:
            self.show_resource_attributes = m.get('ShowResourceAttributes')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class GetStackResourceResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        drift_detection_time: str = None,
        logical_resource_id: str = None,
        metadata: Dict[str, Any] = None,
        physical_resource_id: str = None,
        request_id: str = None,
        resource_attributes: List[Dict[str, Any]] = None,
        resource_drift_status: str = None,
        resource_type: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.drift_detection_time = drift_detection_time
        self.logical_resource_id = logical_resource_id
        self.metadata = metadata
        self.physical_resource_id = physical_resource_id
        self.request_id = request_id
        self.resource_attributes = resource_attributes
        self.resource_drift_status = resource_drift_status
        self.resource_type = resource_type
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.status = status
        self.status_reason = status_reason
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_attributes is not None:
            result['ResourceAttributes'] = self.resource_attributes
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceAttributes') is not None:
            self.resource_attributes = m.get('ResourceAttributes')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
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
        return self


class GetStackResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStackResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetStackResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        change_set_id: str = None,
        include_permission: str = None,
        include_tags: str = None,
        region_id: str = None,
        stack_group_name: str = None,
        stack_id: str = None,
        template_id: str = None,
        template_stage: str = None,
        template_version: str = None,
    ):
        self.change_set_id = change_set_id
        self.include_permission = include_permission
        self.include_tags = include_tags
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.stack_id = stack_id
        self.template_id = template_id
        self.template_stage = template_stage
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.include_permission is not None:
            result['IncludePermission'] = self.include_permission
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_stage is not None:
            result['TemplateStage'] = self.template_stage
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('IncludePermission') is not None:
            self.include_permission = m.get('IncludePermission')
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateStage') is not None:
            self.template_stage = m.get('TemplateStage')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetTemplateResponseBodyPermissions(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        share_option: str = None,
        share_source: str = None,
        template_version: str = None,
        version_option: str = None,
    ):
        self.account_id = account_id
        self.share_option = share_option
        self.share_source = share_source
        self.template_version = template_version
        self.version_option = version_option

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.share_option is not None:
            result['ShareOption'] = self.share_option
        if self.share_source is not None:
            result['ShareSource'] = self.share_source
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.version_option is not None:
            result['VersionOption'] = self.version_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ShareOption') is not None:
            self.share_option = m.get('ShareOption')
        if m.get('ShareSource') is not None:
            self.share_source = m.get('ShareSource')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('VersionOption') is not None:
            self.version_option = m.get('VersionOption')
        return self


class GetTemplateResponseBodyTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        change_set_id: str = None,
        create_time: str = None,
        description: str = None,
        interface: str = None,
        owner_id: str = None,
        permissions: List[GetTemplateResponseBodyPermissions] = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        stack_group_name: str = None,
        stack_id: str = None,
        tags: List[GetTemplateResponseBodyTags] = None,
        template_arn: str = None,
        template_body: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        update_time: str = None,
    ):
        self.change_set_id = change_set_id
        self.create_time = create_time
        self.description = description
        self.interface = interface
        self.owner_id = owner_id
        self.permissions = permissions
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.share_type = share_type
        self.stack_group_name = stack_group_name
        self.stack_id = stack_id
        self.tags = tags
        self.template_arn = template_arn
        self.template_body = template_body
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.update_time = update_time

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.interface is not None:
            result['Interface'] = self.interface
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_arn is not None:
            result['TemplateARN'] = self.template_arn
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Interface') is not None:
            self.interface = m.get('Interface')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = GetTemplateResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetTemplateResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateARN') is not None:
            self.template_arn = m.get('TemplateARN')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateEstimateCostRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetTemplateEstimateCostRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        parameters: List[GetTemplateEstimateCostRequestParameters] = None,
        region_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_scratch_id: str = None,
        template_scratch_region_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.client_token = client_token
        self.parameters = parameters
        self.region_id = region_id
        self.template_body = template_body
        self.template_id = template_id
        self.template_scratch_id = template_scratch_id
        self.template_scratch_region_id = template_scratch_region_id
        self.template_url = template_url
        self.template_version = template_version

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        if self.template_scratch_region_id is not None:
            result['TemplateScratchRegionId'] = self.template_scratch_region_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetTemplateEstimateCostRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        if m.get('TemplateScratchRegionId') is not None:
            self.template_scratch_region_id = m.get('TemplateScratchRegionId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetTemplateEstimateCostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resources: Dict[str, Any] = None,
    ):
        self.request_id = request_id
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetTemplateEstimateCostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateEstimateCostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTemplateEstimateCostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateParameterConstraintsRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetTemplateParameterConstraintsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        parameters: List[GetTemplateParameterConstraintsRequestParameters] = None,
        parameters_key_filter: List[str] = None,
        parameters_order: List[str] = None,
        region_id: str = None,
        stack_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.client_token = client_token
        self.parameters = parameters
        self.parameters_key_filter = parameters_key_filter
        self.parameters_order = parameters_order
        self.region_id = region_id
        self.stack_id = stack_id
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.parameters_key_filter is not None:
            result['ParametersKeyFilter'] = self.parameters_key_filter
        if self.parameters_order is not None:
            result['ParametersOrder'] = self.parameters_order
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetTemplateParameterConstraintsRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('ParametersKeyFilter') is not None:
            self.parameters_key_filter = m.get('ParametersKeyFilter')
        if m.get('ParametersOrder') is not None:
            self.parameters_order = m.get('ParametersOrder')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetTemplateParameterConstraintsShrinkRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetTemplateParameterConstraintsShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        parameters: List[GetTemplateParameterConstraintsShrinkRequestParameters] = None,
        parameters_key_filter_shrink: str = None,
        parameters_order_shrink: str = None,
        region_id: str = None,
        stack_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.client_token = client_token
        self.parameters = parameters
        self.parameters_key_filter_shrink = parameters_key_filter_shrink
        self.parameters_order_shrink = parameters_order_shrink
        self.region_id = region_id
        self.stack_id = stack_id
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.parameters_key_filter_shrink is not None:
            result['ParametersKeyFilter'] = self.parameters_key_filter_shrink
        if self.parameters_order_shrink is not None:
            result['ParametersOrder'] = self.parameters_order_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetTemplateParameterConstraintsShrinkRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('ParametersKeyFilter') is not None:
            self.parameters_key_filter_shrink = m.get('ParametersKeyFilter')
        if m.get('ParametersOrder') is not None:
            self.parameters_order_shrink = m.get('ParametersOrder')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetTemplateParameterConstraintsResponseBodyParameterConstraintsNotSupportResources(TeaModel):
    def __init__(
        self,
        property_name: str = None,
        resource_type: str = None,
    ):
        self.property_name = property_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetTemplateParameterConstraintsResponseBodyParameterConstraintsQueryErrors(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.error_message = error_message
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetTemplateParameterConstraintsResponseBodyParameterConstraints(TeaModel):
    def __init__(
        self,
        allowed_values: List[str] = None,
        association_parameter_names: List[str] = None,
        behavior: str = None,
        behavior_reason: str = None,
        illegal_value_by_parameter_constraints: List[Any] = None,
        illegal_value_by_rules: List[Any] = None,
        not_support_resources: List[GetTemplateParameterConstraintsResponseBodyParameterConstraintsNotSupportResources] = None,
        parameter_key: str = None,
        query_errors: List[GetTemplateParameterConstraintsResponseBodyParameterConstraintsQueryErrors] = None,
        type: str = None,
    ):
        self.allowed_values = allowed_values
        self.association_parameter_names = association_parameter_names
        self.behavior = behavior
        self.behavior_reason = behavior_reason
        self.illegal_value_by_parameter_constraints = illegal_value_by_parameter_constraints
        self.illegal_value_by_rules = illegal_value_by_rules
        self.not_support_resources = not_support_resources
        self.parameter_key = parameter_key
        self.query_errors = query_errors
        self.type = type

    def validate(self):
        if self.not_support_resources:
            for k in self.not_support_resources:
                if k:
                    k.validate()
        if self.query_errors:
            for k in self.query_errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values
        if self.association_parameter_names is not None:
            result['AssociationParameterNames'] = self.association_parameter_names
        if self.behavior is not None:
            result['Behavior'] = self.behavior
        if self.behavior_reason is not None:
            result['BehaviorReason'] = self.behavior_reason
        if self.illegal_value_by_parameter_constraints is not None:
            result['IllegalValueByParameterConstraints'] = self.illegal_value_by_parameter_constraints
        if self.illegal_value_by_rules is not None:
            result['IllegalValueByRules'] = self.illegal_value_by_rules
        result['NotSupportResources'] = []
        if self.not_support_resources is not None:
            for k in self.not_support_resources:
                result['NotSupportResources'].append(k.to_map() if k else None)
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        result['QueryErrors'] = []
        if self.query_errors is not None:
            for k in self.query_errors:
                result['QueryErrors'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')
        if m.get('AssociationParameterNames') is not None:
            self.association_parameter_names = m.get('AssociationParameterNames')
        if m.get('Behavior') is not None:
            self.behavior = m.get('Behavior')
        if m.get('BehaviorReason') is not None:
            self.behavior_reason = m.get('BehaviorReason')
        if m.get('IllegalValueByParameterConstraints') is not None:
            self.illegal_value_by_parameter_constraints = m.get('IllegalValueByParameterConstraints')
        if m.get('IllegalValueByRules') is not None:
            self.illegal_value_by_rules = m.get('IllegalValueByRules')
        self.not_support_resources = []
        if m.get('NotSupportResources') is not None:
            for k in m.get('NotSupportResources'):
                temp_model = GetTemplateParameterConstraintsResponseBodyParameterConstraintsNotSupportResources()
                self.not_support_resources.append(temp_model.from_map(k))
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        self.query_errors = []
        if m.get('QueryErrors') is not None:
            for k in m.get('QueryErrors'):
                temp_model = GetTemplateParameterConstraintsResponseBodyParameterConstraintsQueryErrors()
                self.query_errors.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetTemplateParameterConstraintsResponseBody(TeaModel):
    def __init__(
        self,
        parameter_constraints: List[GetTemplateParameterConstraintsResponseBodyParameterConstraints] = None,
        request_id: str = None,
    ):
        self.parameter_constraints = parameter_constraints
        self.request_id = request_id

    def validate(self):
        if self.parameter_constraints:
            for k in self.parameter_constraints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ParameterConstraints'] = []
        if self.parameter_constraints is not None:
            for k in self.parameter_constraints:
                result['ParameterConstraints'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter_constraints = []
        if m.get('ParameterConstraints') is not None:
            for k in m.get('ParameterConstraints'):
                temp_model = GetTemplateParameterConstraintsResponseBodyParameterConstraints()
                self.parameter_constraints.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTemplateParameterConstraintsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateParameterConstraintsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTemplateParameterConstraintsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateScratchRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        show_data_option: str = None,
        template_scratch_id: str = None,
    ):
        self.region_id = region_id
        self.show_data_option = show_data_option
        self.template_scratch_id = template_scratch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show_data_option is not None:
            result['ShowDataOption'] = self.show_data_option
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShowDataOption') is not None:
            self.show_data_option = m.get('ShowDataOption')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        return self


class GetTemplateScratchResponseBodyTemplateScratchPreferenceParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetTemplateScratchResponseBodyTemplateScratchSourceResourceGroup(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_type_filter: List[str] = None,
    ):
        self.resource_group_id = resource_group_id
        self.resource_type_filter = resource_type_filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type_filter is not None:
            result['ResourceTypeFilter'] = self.resource_type_filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTypeFilter') is not None:
            self.resource_type_filter = m.get('ResourceTypeFilter')
        return self


class GetTemplateScratchResponseBodyTemplateScratchSourceResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetTemplateScratchResponseBodyTemplateScratchSourceTag(TeaModel):
    def __init__(
        self,
        resource_tags: Dict[str, Any] = None,
        resource_type_filter: List[str] = None,
    ):
        self.resource_tags = resource_tags
        self.resource_type_filter = resource_type_filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_tags is not None:
            result['ResourceTags'] = self.resource_tags
        if self.resource_type_filter is not None:
            result['ResourceTypeFilter'] = self.resource_type_filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTags') is not None:
            self.resource_tags = m.get('ResourceTags')
        if m.get('ResourceTypeFilter') is not None:
            self.resource_type_filter = m.get('ResourceTypeFilter')
        return self


class GetTemplateScratchResponseBodyTemplateScratchStackProvision(TeaModel):
    def __init__(
        self,
        creatable: bool = None,
        importable: bool = None,
    ):
        self.creatable = creatable
        self.importable = importable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creatable is not None:
            result['Creatable'] = self.creatable
        if self.importable is not None:
            result['Importable'] = self.importable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creatable') is not None:
            self.creatable = m.get('Creatable')
        if m.get('Importable') is not None:
            self.importable = m.get('Importable')
        return self


class GetTemplateScratchResponseBodyTemplateScratchStacks(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_id: str = None,
        usage_type: str = None,
    ):
        self.region_id = region_id
        self.stack_id = stack_id
        self.usage_type = usage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.usage_type is not None:
            result['UsageType'] = self.usage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')
        return self


class GetTemplateScratchResponseBodyTemplateScratch(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        failed_code: str = None,
        logical_id_strategy: str = None,
        preference_parameters: List[GetTemplateScratchResponseBodyTemplateScratchPreferenceParameters] = None,
        source_resource_group: GetTemplateScratchResponseBodyTemplateScratchSourceResourceGroup = None,
        source_resources: List[GetTemplateScratchResponseBodyTemplateScratchSourceResources] = None,
        source_tag: GetTemplateScratchResponseBodyTemplateScratchSourceTag = None,
        stack_provision: GetTemplateScratchResponseBodyTemplateScratchStackProvision = None,
        stacks: List[GetTemplateScratchResponseBodyTemplateScratchStacks] = None,
        status: str = None,
        status_reason: str = None,
        template_scratch_data: Dict[str, Any] = None,
        template_scratch_id: str = None,
        template_scratch_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.failed_code = failed_code
        self.logical_id_strategy = logical_id_strategy
        self.preference_parameters = preference_parameters
        self.source_resource_group = source_resource_group
        self.source_resources = source_resources
        self.source_tag = source_tag
        self.stack_provision = stack_provision
        self.stacks = stacks
        self.status = status
        self.status_reason = status_reason
        self.template_scratch_data = template_scratch_data
        self.template_scratch_id = template_scratch_id
        self.template_scratch_type = template_scratch_type
        self.update_time = update_time

    def validate(self):
        if self.preference_parameters:
            for k in self.preference_parameters:
                if k:
                    k.validate()
        if self.source_resource_group:
            self.source_resource_group.validate()
        if self.source_resources:
            for k in self.source_resources:
                if k:
                    k.validate()
        if self.source_tag:
            self.source_tag.validate()
        if self.stack_provision:
            self.stack_provision.validate()
        if self.stacks:
            for k in self.stacks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.failed_code is not None:
            result['FailedCode'] = self.failed_code
        if self.logical_id_strategy is not None:
            result['LogicalIdStrategy'] = self.logical_id_strategy
        result['PreferenceParameters'] = []
        if self.preference_parameters is not None:
            for k in self.preference_parameters:
                result['PreferenceParameters'].append(k.to_map() if k else None)
        if self.source_resource_group is not None:
            result['SourceResourceGroup'] = self.source_resource_group.to_map()
        result['SourceResources'] = []
        if self.source_resources is not None:
            for k in self.source_resources:
                result['SourceResources'].append(k.to_map() if k else None)
        if self.source_tag is not None:
            result['SourceTag'] = self.source_tag.to_map()
        if self.stack_provision is not None:
            result['StackProvision'] = self.stack_provision.to_map()
        result['Stacks'] = []
        if self.stacks is not None:
            for k in self.stacks:
                result['Stacks'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.template_scratch_data is not None:
            result['TemplateScratchData'] = self.template_scratch_data
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        if self.template_scratch_type is not None:
            result['TemplateScratchType'] = self.template_scratch_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FailedCode') is not None:
            self.failed_code = m.get('FailedCode')
        if m.get('LogicalIdStrategy') is not None:
            self.logical_id_strategy = m.get('LogicalIdStrategy')
        self.preference_parameters = []
        if m.get('PreferenceParameters') is not None:
            for k in m.get('PreferenceParameters'):
                temp_model = GetTemplateScratchResponseBodyTemplateScratchPreferenceParameters()
                self.preference_parameters.append(temp_model.from_map(k))
        if m.get('SourceResourceGroup') is not None:
            temp_model = GetTemplateScratchResponseBodyTemplateScratchSourceResourceGroup()
            self.source_resource_group = temp_model.from_map(m['SourceResourceGroup'])
        self.source_resources = []
        if m.get('SourceResources') is not None:
            for k in m.get('SourceResources'):
                temp_model = GetTemplateScratchResponseBodyTemplateScratchSourceResources()
                self.source_resources.append(temp_model.from_map(k))
        if m.get('SourceTag') is not None:
            temp_model = GetTemplateScratchResponseBodyTemplateScratchSourceTag()
            self.source_tag = temp_model.from_map(m['SourceTag'])
        if m.get('StackProvision') is not None:
            temp_model = GetTemplateScratchResponseBodyTemplateScratchStackProvision()
            self.stack_provision = temp_model.from_map(m['StackProvision'])
        self.stacks = []
        if m.get('Stacks') is not None:
            for k in m.get('Stacks'):
                temp_model = GetTemplateScratchResponseBodyTemplateScratchStacks()
                self.stacks.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('TemplateScratchData') is not None:
            self.template_scratch_data = m.get('TemplateScratchData')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        if m.get('TemplateScratchType') is not None:
            self.template_scratch_type = m.get('TemplateScratchType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetTemplateScratchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_scratch: GetTemplateScratchResponseBodyTemplateScratch = None,
    ):
        self.request_id = request_id
        self.template_scratch = template_scratch

    def validate(self):
        if self.template_scratch:
            self.template_scratch.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_scratch is not None:
            result['TemplateScratch'] = self.template_scratch.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateScratch') is not None:
            temp_model = GetTemplateScratchResponseBodyTemplateScratch()
            self.template_scratch = temp_model.from_map(m['TemplateScratch'])
        return self


class GetTemplateScratchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateScratchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTemplateScratchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateSummaryRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetTemplateSummaryRequest(TeaModel):
    def __init__(
        self,
        change_set_id: str = None,
        client_token: str = None,
        parameters: List[GetTemplateSummaryRequestParameters] = None,
        region_id: str = None,
        stack_group_name: str = None,
        stack_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.change_set_id = change_set_id
        self.client_token = client_token
        # test
        self.parameters = parameters
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.stack_id = stack_id
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version

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
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetTemplateSummaryRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetTemplateSummaryResponseBodyResourceIdentifierSummaries(TeaModel):
    def __init__(
        self,
        logical_resource_ids: List[str] = None,
        resource_identifiers: List[str] = None,
        resource_type: str = None,
    ):
        self.logical_resource_ids = logical_resource_ids
        self.resource_identifiers = resource_identifiers
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_resource_ids is not None:
            result['LogicalResourceIds'] = self.logical_resource_ids
        if self.resource_identifiers is not None:
            result['ResourceIdentifiers'] = self.resource_identifiers
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceIds') is not None:
            self.logical_resource_ids = m.get('LogicalResourceIds')
        if m.get('ResourceIdentifiers') is not None:
            self.resource_identifiers = m.get('ResourceIdentifiers')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetTemplateSummaryResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        metadata: Dict[str, Any] = None,
        parameters: List[Dict[str, Any]] = None,
        request_id: str = None,
        resource_identifier_summaries: List[GetTemplateSummaryResponseBodyResourceIdentifierSummaries] = None,
        resource_types: List[str] = None,
        version: str = None,
    ):
        self.description = description
        self.metadata = metadata
        self.parameters = parameters
        self.request_id = request_id
        self.resource_identifier_summaries = resource_identifier_summaries
        self.resource_types = resource_types
        self.version = version

    def validate(self):
        if self.resource_identifier_summaries:
            for k in self.resource_identifier_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceIdentifierSummaries'] = []
        if self.resource_identifier_summaries is not None:
            for k in self.resource_identifier_summaries:
                result['ResourceIdentifierSummaries'].append(k.to_map() if k else None)
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_identifier_summaries = []
        if m.get('ResourceIdentifierSummaries') is not None:
            for k in m.get('ResourceIdentifierSummaries'):
                temp_model = GetTemplateSummaryResponseBodyResourceIdentifierSummaries()
                self.resource_identifier_summaries.append(temp_model.from_map(k))
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetTemplateSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetTemplateSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChangeSetsRequest(TeaModel):
    def __init__(
        self,
        change_set_id: str = None,
        change_set_name: List[str] = None,
        execution_status: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        stack_id: str = None,
        status: List[str] = None,
    ):
        self.change_set_id = change_set_id
        self.change_set_name = change_set_name
        self.execution_status = execution_status
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.stack_id = stack_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListChangeSetsResponseBodyChangeSets(TeaModel):
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListChangeSetsResponseBody(TeaModel):
    def __init__(
        self,
        change_sets: List[ListChangeSetsResponseBodyChangeSets] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.change_sets = change_sets
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.change_sets:
            for k in self.change_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChangeSets'] = []
        if self.change_sets is not None:
            for k in self.change_sets:
                result['ChangeSets'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_sets = []
        if m.get('ChangeSets') is not None:
            for k in m.get('ChangeSets'):
                temp_model = ListChangeSetsResponseBodyChangeSets()
                self.change_sets.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChangeSetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChangeSetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListChangeSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTypesRequest(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
    ):
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        return self


class ListResourceTypesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_types: List[str] = None,
    ):
        self.request_id = request_id
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListResourceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceTypesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackEventsRequest(TeaModel):
    def __init__(
        self,
        logical_resource_id: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_type: List[str] = None,
        stack_id: str = None,
        status: List[str] = None,
    ):
        self.logical_resource_id = logical_resource_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_type = resource_type
        self.stack_id = stack_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListStackEventsResponseBodyEvents(TeaModel):
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListStackEventsResponseBody(TeaModel):
    def __init__(
        self,
        events: List[ListStackEventsResponseBodyEvents] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.events = events
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = ListStackEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListStackEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStackEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListStackEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackGroupOperationResultsRequest(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.operation_id = operation_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListStackGroupOperationResultsResponseBodyStackGroupOperationResults(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        rd_folder_id: str = None,
        region_id: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.account_id = account_id
        self.rd_folder_id = rd_folder_id
        self.region_id = region_id
        self.status = status
        self.status_reason = status_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.rd_folder_id is not None:
            result['RdFolderId'] = self.rd_folder_id
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
        if m.get('RdFolderId') is not None:
            self.rd_folder_id = m.get('RdFolderId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class ListStackGroupOperationResultsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stack_group_operation_results: List[ListStackGroupOperationResultsResponseBodyStackGroupOperationResults] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.stack_group_operation_results = stack_group_operation_results
        self.total_count = total_count

    def validate(self):
        if self.stack_group_operation_results:
            for k in self.stack_group_operation_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StackGroupOperationResults'] = []
        if self.stack_group_operation_results is not None:
            for k in self.stack_group_operation_results:
                result['StackGroupOperationResults'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stack_group_operation_results = []
        if m.get('StackGroupOperationResults') is not None:
            for k in m.get('StackGroupOperationResults'):
                temp_model = ListStackGroupOperationResultsResponseBodyStackGroupOperationResults()
                self.stack_group_operation_results.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListStackGroupOperationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStackGroupOperationResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListStackGroupOperationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackGroupOperationsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        stack_group_name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.stack_group_name = stack_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        return self


class ListStackGroupOperationsResponseBodyStackGroupOperations(TeaModel):
    def __init__(
        self,
        action: str = None,
        create_time: str = None,
        end_time: str = None,
        operation_description: str = None,
        operation_id: str = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
        status: str = None,
    ):
        self.action = action
        self.create_time = create_time
        self.end_time = end_time
        self.operation_description = operation_description
        self.operation_id = operation_id
        self.stack_group_id = stack_group_id
        self.stack_group_name = stack_group_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListStackGroupOperationsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stack_group_operations: List[ListStackGroupOperationsResponseBodyStackGroupOperations] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.stack_group_operations = stack_group_operations
        self.total_count = total_count

    def validate(self):
        if self.stack_group_operations:
            for k in self.stack_group_operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StackGroupOperations'] = []
        if self.stack_group_operations is not None:
            for k in self.stack_group_operations:
                result['StackGroupOperations'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stack_group_operations = []
        if m.get('StackGroupOperations') is not None:
            for k in m.get('StackGroupOperations'):
                temp_model = ListStackGroupOperationsResponseBodyStackGroupOperations()
                self.stack_group_operations.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListStackGroupOperationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStackGroupOperationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListStackGroupOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackGroupsRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListStackGroupsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[ListStackGroupsRequestTags] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.status = status
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListStackGroupsRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListStackGroupsResponseBodyStackGroupsAutoDeployment(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        retain_stacks_on_account_removal: bool = None,
    ):
        self.enabled = enabled
        self.retain_stacks_on_account_removal = retain_stacks_on_account_removal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.retain_stacks_on_account_removal is not None:
            result['RetainStacksOnAccountRemoval'] = self.retain_stacks_on_account_removal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RetainStacksOnAccountRemoval') is not None:
            self.retain_stacks_on_account_removal = m.get('RetainStacksOnAccountRemoval')
        return self


class ListStackGroupsResponseBodyStackGroupsTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListStackGroupsResponseBodyStackGroups(TeaModel):
    def __init__(
        self,
        auto_deployment: ListStackGroupsResponseBodyStackGroupsAutoDeployment = None,
        description: str = None,
        drift_detection_time: str = None,
        permission_model: str = None,
        resource_group_id: str = None,
        stack_group_drift_status: str = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
        status: str = None,
        tags: List[ListStackGroupsResponseBodyStackGroupsTags] = None,
    ):
        self.auto_deployment = auto_deployment
        self.description = description
        self.drift_detection_time = drift_detection_time
        self.permission_model = permission_model
        self.resource_group_id = resource_group_id
        self.stack_group_drift_status = stack_group_drift_status
        self.stack_group_id = stack_group_id
        self.stack_group_name = stack_group_name
        self.status = status
        self.tags = tags

    def validate(self):
        if self.auto_deployment:
            self.auto_deployment.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_deployment is not None:
            result['AutoDeployment'] = self.auto_deployment.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.stack_group_drift_status is not None:
            result['StackGroupDriftStatus'] = self.stack_group_drift_status
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDeployment') is not None:
            temp_model = ListStackGroupsResponseBodyStackGroupsAutoDeployment()
            self.auto_deployment = temp_model.from_map(m['AutoDeployment'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StackGroupDriftStatus') is not None:
            self.stack_group_drift_status = m.get('StackGroupDriftStatus')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListStackGroupsResponseBodyStackGroupsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListStackGroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stack_groups: List[ListStackGroupsResponseBodyStackGroups] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.stack_groups = stack_groups
        self.total_count = total_count

    def validate(self):
        if self.stack_groups:
            for k in self.stack_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StackGroups'] = []
        if self.stack_groups is not None:
            for k in self.stack_groups:
                result['StackGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stack_groups = []
        if m.get('StackGroups') is not None:
            for k in m.get('StackGroups'):
                temp_model = ListStackGroupsResponseBodyStackGroups()
                self.stack_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListStackGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStackGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListStackGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackInstancesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        stack_group_name: str = None,
        stack_instance_account_id: str = None,
        stack_instance_region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.stack_group_name = stack_group_name
        self.stack_instance_account_id = stack_instance_account_id
        self.stack_instance_region_id = stack_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackInstanceAccountId') is not None:
            self.stack_instance_account_id = m.get('StackInstanceAccountId')
        if m.get('StackInstanceRegionId') is not None:
            self.stack_instance_region_id = m.get('StackInstanceRegionId')
        return self


class ListStackInstancesResponseBodyStackInstances(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        drift_detection_time: str = None,
        rd_folder_id: str = None,
        region_id: str = None,
        stack_drift_status: str = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
        stack_id: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        self.account_id = account_id
        self.drift_detection_time = drift_detection_time
        self.rd_folder_id = rd_folder_id
        self.region_id = region_id
        self.stack_drift_status = stack_drift_status
        self.stack_group_id = stack_group_id
        self.stack_group_name = stack_group_name
        self.stack_id = stack_id
        self.status = status
        self.status_reason = status_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.rd_folder_id is not None:
            result['RdFolderId'] = self.rd_folder_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('RdFolderId') is not None:
            self.rd_folder_id = m.get('RdFolderId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class ListStackInstancesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stack_instances: List[ListStackInstancesResponseBodyStackInstances] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.stack_instances = stack_instances
        self.total_count = total_count

    def validate(self):
        if self.stack_instances:
            for k in self.stack_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StackInstances'] = []
        if self.stack_instances is not None:
            for k in self.stack_instances:
                result['StackInstances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stack_instances = []
        if m.get('StackInstances') is not None:
            for k in m.get('StackInstances'):
                temp_model = ListStackInstancesResponseBodyStackInstances()
                self.stack_instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListStackInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStackInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListStackInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackOperationRisksRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        operation_type: str = None,
        ram_role_name: str = None,
        region_id: str = None,
        retain_all_resources: bool = None,
        retain_resources: List[str] = None,
        stack_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.client_token = client_token
        self.operation_type = operation_type
        self.ram_role_name = ram_role_name
        self.region_id = region_id
        self.retain_all_resources = retain_all_resources
        self.retain_resources = retain_resources
        self.stack_id = stack_id
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retain_all_resources is not None:
            result['RetainAllResources'] = self.retain_all_resources
        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetainAllResources') is not None:
            self.retain_all_resources = m.get('RetainAllResources')
        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class ListStackOperationRisksResponseBodyRiskResources(TeaModel):
    def __init__(
        self,
        code: str = None,
        logical_resource_id: str = None,
        message: str = None,
        physical_resource_id: str = None,
        reason: str = None,
        request_id: str = None,
        resource_type: str = None,
        risk_type: str = None,
    ):
        self.code = code
        self.logical_resource_id = logical_resource_id
        self.message = message
        self.physical_resource_id = physical_resource_id
        self.reason = reason
        self.request_id = request_id
        self.resource_type = resource_type
        self.risk_type = risk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.message is not None:
            result['Message'] = self.message
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.risk_type is not None:
            result['RiskType'] = self.risk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')
        return self


class ListStackOperationRisksResponseBody(TeaModel):
    def __init__(
        self,
        missing_policy_actions: List[str] = None,
        request_id: str = None,
        risk_resources: List[ListStackOperationRisksResponseBodyRiskResources] = None,
    ):
        self.missing_policy_actions = missing_policy_actions
        self.request_id = request_id
        self.risk_resources = risk_resources

    def validate(self):
        if self.risk_resources:
            for k in self.risk_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.missing_policy_actions is not None:
            result['MissingPolicyActions'] = self.missing_policy_actions
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RiskResources'] = []
        if self.risk_resources is not None:
            for k in self.risk_resources:
                result['RiskResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MissingPolicyActions') is not None:
            self.missing_policy_actions = m.get('MissingPolicyActions')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.risk_resources = []
        if m.get('RiskResources') is not None:
            for k in m.get('RiskResources'):
                temp_model = ListStackOperationRisksResponseBodyRiskResources()
                self.risk_resources.append(temp_model.from_map(k))
        return self


class ListStackOperationRisksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStackOperationRisksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListStackOperationRisksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackResourceDriftsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_drift_status: List[str] = None,
        stack_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.resource_drift_status = resource_drift_status
        self.stack_id = stack_id

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
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences(TeaModel):
    def __init__(
        self,
        actual_value: str = None,
        difference_type: str = None,
        expected_value: str = None,
        property_path: str = None,
    ):
        self.actual_value = actual_value
        self.difference_type = difference_type
        self.expected_value = expected_value
        self.property_path = property_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.difference_type is not None:
            result['DifferenceType'] = self.difference_type
        if self.expected_value is not None:
            result['ExpectedValue'] = self.expected_value
        if self.property_path is not None:
            result['PropertyPath'] = self.property_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('DifferenceType') is not None:
            self.difference_type = m.get('DifferenceType')
        if m.get('ExpectedValue') is not None:
            self.expected_value = m.get('ExpectedValue')
        if m.get('PropertyPath') is not None:
            self.property_path = m.get('PropertyPath')
        return self


class ListStackResourceDriftsResponseBodyResourceDrifts(TeaModel):
    def __init__(
        self,
        actual_properties: str = None,
        drift_detection_time: str = None,
        expected_properties: str = None,
        logical_resource_id: str = None,
        physical_resource_id: str = None,
        property_differences: List[ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences] = None,
        resource_drift_status: str = None,
        resource_type: str = None,
        stack_id: str = None,
    ):
        self.actual_properties = actual_properties
        self.drift_detection_time = drift_detection_time
        self.expected_properties = expected_properties
        self.logical_resource_id = logical_resource_id
        self.physical_resource_id = physical_resource_id
        self.property_differences = property_differences
        self.resource_drift_status = resource_drift_status
        self.resource_type = resource_type
        self.stack_id = stack_id

    def validate(self):
        if self.property_differences:
            for k in self.property_differences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_properties is not None:
            result['ActualProperties'] = self.actual_properties
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.expected_properties is not None:
            result['ExpectedProperties'] = self.expected_properties
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        result['PropertyDifferences'] = []
        if self.property_differences is not None:
            for k in self.property_differences:
                result['PropertyDifferences'].append(k.to_map() if k else None)
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualProperties') is not None:
            self.actual_properties = m.get('ActualProperties')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('ExpectedProperties') is not None:
            self.expected_properties = m.get('ExpectedProperties')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        self.property_differences = []
        if m.get('PropertyDifferences') is not None:
            for k in m.get('PropertyDifferences'):
                temp_model = ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences()
                self.property_differences.append(temp_model.from_map(k))
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class ListStackResourceDriftsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_drifts: List[ListStackResourceDriftsResponseBodyResourceDrifts] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.resource_drifts = resource_drifts

    def validate(self):
        if self.resource_drifts:
            for k in self.resource_drifts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceDrifts'] = []
        if self.resource_drifts is not None:
            for k in self.resource_drifts:
                result['ResourceDrifts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_drifts = []
        if m.get('ResourceDrifts') is not None:
            for k in m.get('ResourceDrifts'):
                temp_model = ListStackResourceDriftsResponseBodyResourceDrifts()
                self.resource_drifts.append(temp_model.from_map(k))
        return self


class ListStackResourceDriftsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStackResourceDriftsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListStackResourceDriftsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStackResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_id: str = None,
    ):
        self.region_id = region_id
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class ListStackResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        drift_detection_time: str = None,
        logical_resource_id: str = None,
        physical_resource_id: str = None,
        resource_drift_status: str = None,
        resource_type: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.drift_detection_time = drift_detection_time
        self.logical_resource_id = logical_resource_id
        self.physical_resource_id = physical_resource_id
        self.resource_drift_status = resource_drift_status
        self.resource_type = resource_type
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.status = status
        self.status_reason = status_reason
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.resource_drift_status is not None:
            result['ResourceDriftStatus'] = self.resource_drift_status
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('ResourceDriftStatus') is not None:
            self.resource_drift_status = m.get('ResourceDriftStatus')
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
        return self


class ListStackResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[ListStackResourcesResponseBodyResources] = None,
    ):
        self.request_id = request_id
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListStackResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListStackResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStackResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListStackResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        page_number: int = None,
        page_size: int = None,
        parent_stack_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        show_nested_stack: bool = None,
        stack_id: str = None,
        stack_ids: List[str] = None,
        stack_name: List[str] = None,
        status: List[str] = None,
        tag: List[ListStacksRequestTag] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.parent_stack_id = parent_stack_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.show_nested_stack = show_nested_stack
        self.stack_id = stack_id
        self.stack_ids = stack_ids
        self.stack_name = stack_name
        self.status = status
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.show_nested_stack is not None:
            result['ShowNestedStack'] = self.show_nested_stack
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_ids is not None:
            result['StackIds'] = self.stack_ids
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShowNestedStack') is not None:
            self.show_nested_stack = m.get('ShowNestedStack')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackIds') is not None:
            self.stack_ids = m.get('StackIds')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListStacksRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListStacksResponseBodyStacksOperationInfo(TeaModel):
    def __init__(
        self,
        action: str = None,
        code: str = None,
        logical_resource_id: str = None,
        message: str = None,
        request_id: str = None,
        resource_type: str = None,
    ):
        self.action = action
        self.code = code
        self.logical_resource_id = logical_resource_id
        self.message = message
        self.request_id = request_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.code is not None:
            result['Code'] = self.code
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListStacksResponseBodyStacksTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListStacksResponseBodyStacks(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        disable_rollback: bool = None,
        drift_detection_time: str = None,
        operation_info: ListStacksResponseBodyStacksOperationInfo = None,
        parent_stack_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_managed: bool = None,
        service_name: str = None,
        stack_drift_status: str = None,
        stack_id: str = None,
        stack_name: str = None,
        stack_type: str = None,
        status: str = None,
        status_reason: str = None,
        tags: List[ListStacksResponseBodyStacksTags] = None,
        timeout_in_minutes: int = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.disable_rollback = disable_rollback
        self.drift_detection_time = drift_detection_time
        self.operation_info = operation_info
        self.parent_stack_id = parent_stack_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.service_managed = service_managed
        self.service_name = service_name
        self.stack_drift_status = stack_drift_status
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.stack_type = stack_type
        self.status = status
        self.status_reason = status_reason
        self.tags = tags
        self.timeout_in_minutes = timeout_in_minutes
        self.update_time = update_time

    def validate(self):
        if self.operation_info:
            self.operation_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.drift_detection_time is not None:
            result['DriftDetectionTime'] = self.drift_detection_time
        if self.operation_info is not None:
            result['OperationInfo'] = self.operation_info.to_map()
        if self.parent_stack_id is not None:
            result['ParentStackId'] = self.parent_stack_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.stack_drift_status is not None:
            result['StackDriftStatus'] = self.stack_drift_status
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.stack_type is not None:
            result['StackType'] = self.stack_type
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('DriftDetectionTime') is not None:
            self.drift_detection_time = m.get('DriftDetectionTime')
        if m.get('OperationInfo') is not None:
            temp_model = ListStacksResponseBodyStacksOperationInfo()
            self.operation_info = temp_model.from_map(m['OperationInfo'])
        if m.get('ParentStackId') is not None:
            self.parent_stack_id = m.get('ParentStackId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StackDriftStatus') is not None:
            self.stack_drift_status = m.get('StackDriftStatus')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('StackType') is not None:
            self.stack_type = m.get('StackType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListStacksResponseBodyStacksTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListStacksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stacks: List[ListStacksResponseBodyStacks] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.stacks = stacks
        self.total_count = total_count

    def validate(self):
        if self.stacks:
            for k in self.stacks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Stacks'] = []
        if self.stacks is not None:
            for k in self.stacks:
                result['Stacks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stacks = []
        if m.get('Stacks') is not None:
            for k in m.get('Stacks'):
                temp_model = ListStacksResponseBodyStacks()
                self.stacks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListStacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStacksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListStacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        keys: List[str] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.keys = keys
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTagKeysResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
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
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        self.key = key
        self.next_token = next_token
        self.region_id = region_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        values: List[str] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagValuesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplateScratchesRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListTemplateScratchesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        status: str = None,
        tags: List[ListTemplateScratchesRequestTags] = None,
        template_scratch_id: str = None,
        template_scratch_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.status = status
        self.tags = tags
        self.template_scratch_id = template_scratch_id
        self.template_scratch_type = template_scratch_type

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        if self.template_scratch_type is not None:
            result['TemplateScratchType'] = self.template_scratch_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTemplateScratchesRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        if m.get('TemplateScratchType') is not None:
            self.template_scratch_type = m.get('TemplateScratchType')
        return self


class ListTemplateScratchesResponseBodyTemplateScratchesPreferenceParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListTemplateScratchesResponseBodyTemplateScratchesSourceResourceGroup(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_type_filter: List[str] = None,
    ):
        self.resource_group_id = resource_group_id
        self.resource_type_filter = resource_type_filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type_filter is not None:
            result['ResourceTypeFilter'] = self.resource_type_filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTypeFilter') is not None:
            self.resource_type_filter = m.get('ResourceTypeFilter')
        return self


class ListTemplateScratchesResponseBodyTemplateScratchesSourceResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTemplateScratchesResponseBodyTemplateScratchesSourceTag(TeaModel):
    def __init__(
        self,
        resource_tags: Dict[str, Any] = None,
        resource_type_filter: List[str] = None,
    ):
        self.resource_tags = resource_tags
        self.resource_type_filter = resource_type_filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_tags is not None:
            result['ResourceTags'] = self.resource_tags
        if self.resource_type_filter is not None:
            result['ResourceTypeFilter'] = self.resource_type_filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTags') is not None:
            self.resource_tags = m.get('ResourceTags')
        if m.get('ResourceTypeFilter') is not None:
            self.resource_type_filter = m.get('ResourceTypeFilter')
        return self


class ListTemplateScratchesResponseBodyTemplateScratchesTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListTemplateScratchesResponseBodyTemplateScratches(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        failed_code: str = None,
        logical_id_strategy: str = None,
        preference_parameters: List[ListTemplateScratchesResponseBodyTemplateScratchesPreferenceParameters] = None,
        source_resource_group: ListTemplateScratchesResponseBodyTemplateScratchesSourceResourceGroup = None,
        source_resources: List[ListTemplateScratchesResponseBodyTemplateScratchesSourceResources] = None,
        source_tag: ListTemplateScratchesResponseBodyTemplateScratchesSourceTag = None,
        status: str = None,
        status_reason: str = None,
        tags: List[ListTemplateScratchesResponseBodyTemplateScratchesTags] = None,
        template_scratch_id: str = None,
        template_scratch_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.failed_code = failed_code
        self.logical_id_strategy = logical_id_strategy
        self.preference_parameters = preference_parameters
        self.source_resource_group = source_resource_group
        self.source_resources = source_resources
        self.source_tag = source_tag
        self.status = status
        self.status_reason = status_reason
        self.tags = tags
        self.template_scratch_id = template_scratch_id
        self.template_scratch_type = template_scratch_type
        self.update_time = update_time

    def validate(self):
        if self.preference_parameters:
            for k in self.preference_parameters:
                if k:
                    k.validate()
        if self.source_resource_group:
            self.source_resource_group.validate()
        if self.source_resources:
            for k in self.source_resources:
                if k:
                    k.validate()
        if self.source_tag:
            self.source_tag.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.failed_code is not None:
            result['FailedCode'] = self.failed_code
        if self.logical_id_strategy is not None:
            result['LogicalIdStrategy'] = self.logical_id_strategy
        result['PreferenceParameters'] = []
        if self.preference_parameters is not None:
            for k in self.preference_parameters:
                result['PreferenceParameters'].append(k.to_map() if k else None)
        if self.source_resource_group is not None:
            result['SourceResourceGroup'] = self.source_resource_group.to_map()
        result['SourceResources'] = []
        if self.source_resources is not None:
            for k in self.source_resources:
                result['SourceResources'].append(k.to_map() if k else None)
        if self.source_tag is not None:
            result['SourceTag'] = self.source_tag.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        if self.template_scratch_type is not None:
            result['TemplateScratchType'] = self.template_scratch_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FailedCode') is not None:
            self.failed_code = m.get('FailedCode')
        if m.get('LogicalIdStrategy') is not None:
            self.logical_id_strategy = m.get('LogicalIdStrategy')
        self.preference_parameters = []
        if m.get('PreferenceParameters') is not None:
            for k in m.get('PreferenceParameters'):
                temp_model = ListTemplateScratchesResponseBodyTemplateScratchesPreferenceParameters()
                self.preference_parameters.append(temp_model.from_map(k))
        if m.get('SourceResourceGroup') is not None:
            temp_model = ListTemplateScratchesResponseBodyTemplateScratchesSourceResourceGroup()
            self.source_resource_group = temp_model.from_map(m['SourceResourceGroup'])
        self.source_resources = []
        if m.get('SourceResources') is not None:
            for k in m.get('SourceResources'):
                temp_model = ListTemplateScratchesResponseBodyTemplateScratchesSourceResources()
                self.source_resources.append(temp_model.from_map(k))
        if m.get('SourceTag') is not None:
            temp_model = ListTemplateScratchesResponseBodyTemplateScratchesSourceTag()
            self.source_tag = temp_model.from_map(m['SourceTag'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTemplateScratchesResponseBodyTemplateScratchesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        if m.get('TemplateScratchType') is not None:
            self.template_scratch_type = m.get('TemplateScratchType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListTemplateScratchesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        template_scratches: List[ListTemplateScratchesResponseBodyTemplateScratches] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.template_scratches = template_scratches
        self.total_count = total_count

    def validate(self):
        if self.template_scratches:
            for k in self.template_scratches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TemplateScratches'] = []
        if self.template_scratches is not None:
            for k in self.template_scratches:
                result['TemplateScratches'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.template_scratches = []
        if m.get('TemplateScratches') is not None:
            for k in m.get('TemplateScratches'):
                temp_model = ListTemplateScratchesResponseBodyTemplateScratches()
                self.template_scratches.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplateScratchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTemplateScratchesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTemplateScratchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplateVersionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        template_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.template_id = template_id

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
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListTemplateVersionsResponseBodyVersions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
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
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListTemplateVersionsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        versions: List[ListTemplateVersionsResponseBodyVersions] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListTemplateVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListTemplateVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTemplateVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTemplateVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        include_tags: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tag: List[ListTemplatesRequestTag] = None,
        template_name: str = None,
    ):
        self.include_tags = include_tags
        self.page_number = page_number
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.share_type = share_type
        self.tag = tag
        self.template_name = template_name

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTemplatesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListTemplatesResponseBodyTemplatesTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        owner_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: List[ListTemplatesResponseBodyTemplatesTags] = None,
        template_arn: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.owner_id = owner_id
        self.resource_group_id = resource_group_id
        self.share_type = share_type
        self.tags = tags
        self.template_arn = template_arn
        self.template_id = template_id
        self.template_name = template_name
        self.template_version = template_version
        self.update_time = update_time

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_arn is not None:
            result['TemplateARN'] = self.template_arn
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTemplatesResponseBodyTemplatesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateARN') is not None:
            self.template_arn = m.get('TemplateARN')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        templates: List[ListTemplatesResponseBodyTemplates] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.templates = templates
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.new_resource_group_id = new_resource_group_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class MoveResourceGroupResponseBody(TeaModel):
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreviewStackRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class PreviewStackRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        disable_rollback: bool = None,
        enable_pre_config: bool = None,
        parallelism: int = None,
        parameters: List[PreviewStackRequestParameters] = None,
        region_id: str = None,
        stack_id: str = None,
        stack_name: str = None,
        stack_policy_body: str = None,
        stack_policy_url: str = None,
        template_body: str = None,
        template_id: str = None,
        template_scratch_id: str = None,
        template_scratch_region_id: str = None,
        template_url: str = None,
        template_version: str = None,
        timeout_in_minutes: int = None,
    ):
        self.client_token = client_token
        self.disable_rollback = disable_rollback
        self.enable_pre_config = enable_pre_config
        self.parallelism = parallelism
        # test
        self.parameters = parameters
        self.region_id = region_id
        self.stack_id = stack_id
        self.stack_name = stack_name
        self.stack_policy_body = stack_policy_body
        self.stack_policy_url = stack_policy_url
        self.template_body = template_body
        self.template_id = template_id
        self.template_scratch_id = template_scratch_id
        self.template_scratch_region_id = template_scratch_region_id
        self.template_url = template_url
        self.template_version = template_version
        self.timeout_in_minutes = timeout_in_minutes

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.enable_pre_config is not None:
            result['EnablePreConfig'] = self.enable_pre_config
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        if self.template_scratch_region_id is not None:
            result['TemplateScratchRegionId'] = self.template_scratch_region_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('EnablePreConfig') is not None:
            self.enable_pre_config = m.get('EnablePreConfig')
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = PreviewStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        if m.get('TemplateScratchRegionId') is not None:
            self.template_scratch_region_id = m.get('TemplateScratchRegionId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        return self


class PreviewStackResponseBodyStackLogTerraformLogs(TeaModel):
    def __init__(
        self,
        command: str = None,
        content: str = None,
        stream: str = None,
    ):
        self.command = command
        self.content = content
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.content is not None:
            result['Content'] = self.content
        if self.stream is not None:
            result['Stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        return self


class PreviewStackResponseBodyStackLog(TeaModel):
    def __init__(
        self,
        terraform_logs: List[PreviewStackResponseBodyStackLogTerraformLogs] = None,
    ):
        self.terraform_logs = terraform_logs

    def validate(self):
        if self.terraform_logs:
            for k in self.terraform_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TerraformLogs'] = []
        if self.terraform_logs is not None:
            for k in self.terraform_logs:
                result['TerraformLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.terraform_logs = []
        if m.get('TerraformLogs') is not None:
            for k in m.get('TerraformLogs'):
                temp_model = PreviewStackResponseBodyStackLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k))
        return self


class PreviewStackResponseBodyStackParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class PreviewStackResponseBodyStackResources(TeaModel):
    def __init__(
        self,
        acs_resource_type: str = None,
        action: str = None,
        description: str = None,
        logical_resource_id: str = None,
        physical_resource_id: str = None,
        properties: Dict[str, Any] = None,
        replacement: str = None,
        required_by: List[str] = None,
        resource_type: str = None,
        stack: Dict[str, Any] = None,
    ):
        self.acs_resource_type = acs_resource_type
        self.action = action
        self.description = description
        self.logical_resource_id = logical_resource_id
        self.physical_resource_id = physical_resource_id
        self.properties = properties
        self.replacement = replacement
        self.required_by = required_by
        self.resource_type = resource_type
        self.stack = stack

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acs_resource_type is not None:
            result['AcsResourceType'] = self.acs_resource_type
        if self.action is not None:
            result['Action'] = self.action
        if self.description is not None:
            result['Description'] = self.description
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.replacement is not None:
            result['Replacement'] = self.replacement
        if self.required_by is not None:
            result['RequiredBy'] = self.required_by
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.stack is not None:
            result['Stack'] = self.stack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcsResourceType') is not None:
            self.acs_resource_type = m.get('AcsResourceType')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Replacement') is not None:
            self.replacement = m.get('Replacement')
        if m.get('RequiredBy') is not None:
            self.required_by = m.get('RequiredBy')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Stack') is not None:
            self.stack = m.get('Stack')
        return self


class PreviewStackResponseBodyStack(TeaModel):
    def __init__(
        self,
        description: str = None,
        disable_rollback: bool = None,
        log: PreviewStackResponseBodyStackLog = None,
        parameters: List[PreviewStackResponseBodyStackParameters] = None,
        region_id: str = None,
        resources: List[PreviewStackResponseBodyStackResources] = None,
        stack_name: str = None,
        stack_policy_body: Dict[str, Any] = None,
        template_description: str = None,
        timeout_in_minutes: int = None,
    ):
        self.description = description
        self.disable_rollback = disable_rollback
        self.log = log
        self.parameters = parameters
        self.region_id = region_id
        self.resources = resources
        self.stack_name = stack_name
        self.stack_policy_body = stack_policy_body
        self.template_description = template_description
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        if self.log:
            self.log.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.log is not None:
            result['Log'] = self.log.to_map()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.stack_name is not None:
            result['StackName'] = self.stack_name
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.template_description is not None:
            result['TemplateDescription'] = self.template_description
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('Log') is not None:
            temp_model = PreviewStackResponseBodyStackLog()
            self.log = temp_model.from_map(m['Log'])
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = PreviewStackResponseBodyStackParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = PreviewStackResponseBodyStackResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('TemplateDescription') is not None:
            self.template_description = m.get('TemplateDescription')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        return self


class PreviewStackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack: PreviewStackResponseBodyStack = None,
    ):
        self.request_id = request_id
        self.stack = stack

    def validate(self):
        if self.stack:
            self.stack.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = PreviewStackResponseBodyStack()
            self.stack = temp_model.from_map(m['Stack'])
        return self


class PreviewStackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PreviewStackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = PreviewStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeletionProtectionRequest(TeaModel):
    def __init__(
        self,
        deletion_protection: str = None,
        region_id: str = None,
        stack_id: str = None,
    ):
        self.deletion_protection = deletion_protection
        self.region_id = region_id
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class SetDeletionProtectionResponseBody(TeaModel):
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


class SetDeletionProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDeletionProtectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetDeletionProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetStackPolicyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stack_id: str = None,
        stack_policy_body: str = None,
        stack_policy_url: str = None,
    ):
        self.region_id = region_id
        self.stack_id = stack_id
        self.stack_policy_body = stack_policy_body
        self.stack_policy_url = stack_policy_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        return self


class SetStackPolicyResponseBody(TeaModel):
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


class SetStackPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetStackPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetStackPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetTemplatePermissionRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        share_option: str = None,
        template_id: str = None,
        template_version: str = None,
        version_option: str = None,
    ):
        self.account_ids = account_ids
        self.share_option = share_option
        self.template_id = template_id
        self.template_version = template_version
        self.version_option = version_option

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.share_option is not None:
            result['ShareOption'] = self.share_option
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.version_option is not None:
            result['VersionOption'] = self.version_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('ShareOption') is not None:
            self.share_option = m.get('ShareOption')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('VersionOption') is not None:
            self.version_option = m.get('VersionOption')
        return self


class SetTemplatePermissionResponseBody(TeaModel):
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


class SetTemplatePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetTemplatePermissionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SetTemplatePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SignalResourceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        logical_resource_id: str = None,
        region_id: str = None,
        stack_id: str = None,
        status: str = None,
        unique_id: str = None,
    ):
        self.client_token = client_token
        self.logical_resource_id = logical_resource_id
        self.region_id = region_id
        self.stack_id = stack_id
        self.status = status
        self.unique_id = unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.status is not None:
            result['Status'] = self.status
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        return self


class SignalResourceResponseBody(TeaModel):
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


class SignalResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SignalResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = SignalResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopStackGroupOperationRequest(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        region_id: str = None,
    ):
        self.operation_id = operation_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopStackGroupOperationResponseBody(TeaModel):
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


class StopStackGroupOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopStackGroupOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = StopStackGroupOperationResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class TagResourcesResponseBody(TeaModel):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStackRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateStackRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        client_token: str = None,
        disable_rollback: bool = None,
        dry_run: bool = None,
        parallelism: int = None,
        parameters: List[UpdateStackRequestParameters] = None,
        ram_role_name: str = None,
        region_id: str = None,
        replacement_option: str = None,
        resource_group_id: str = None,
        stack_id: str = None,
        stack_policy_body: str = None,
        stack_policy_during_update_body: str = None,
        stack_policy_during_update_url: str = None,
        stack_policy_url: str = None,
        tags: List[UpdateStackRequestTags] = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
        timeout_in_minutes: int = None,
        use_previous_parameters: bool = None,
    ):
        self.client_token = client_token
        self.disable_rollback = disable_rollback
        self.dry_run = dry_run
        self.parallelism = parallelism
        self.parameters = parameters
        self.ram_role_name = ram_role_name
        self.region_id = region_id
        self.replacement_option = replacement_option
        self.resource_group_id = resource_group_id
        self.stack_id = stack_id
        self.stack_policy_body = stack_policy_body
        self.stack_policy_during_update_body = stack_policy_during_update_body
        self.stack_policy_during_update_url = stack_policy_during_update_url
        self.stack_policy_url = stack_policy_url
        self.tags = tags
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version
        self.timeout_in_minutes = timeout_in_minutes
        self.use_previous_parameters = use_previous_parameters

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replacement_option is not None:
            result['ReplacementOption'] = self.replacement_option
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body
        if self.stack_policy_during_update_body is not None:
            result['StackPolicyDuringUpdateBody'] = self.stack_policy_during_update_body
        if self.stack_policy_during_update_url is not None:
            result['StackPolicyDuringUpdateURL'] = self.stack_policy_during_update_url
        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        if self.use_previous_parameters is not None:
            result['UsePreviousParameters'] = self.use_previous_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplacementOption') is not None:
            self.replacement_option = m.get('ReplacementOption')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')
        if m.get('StackPolicyDuringUpdateBody') is not None:
            self.stack_policy_during_update_body = m.get('StackPolicyDuringUpdateBody')
        if m.get('StackPolicyDuringUpdateURL') is not None:
            self.stack_policy_during_update_url = m.get('StackPolicyDuringUpdateURL')
        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UpdateStackRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        if m.get('UsePreviousParameters') is not None:
            self.use_previous_parameters = m.get('UsePreviousParameters')
        return self


class UpdateStackResponseBodyDryRunResult(TeaModel):
    def __init__(
        self,
        parameters_allowed_to_be_modified: List[str] = None,
        parameters_cause_interruption_if_modified: List[str] = None,
        parameters_conditionally_allowed_to_be_modified: List[str] = None,
        parameters_conditionally_cause_interruption_if_modified: List[str] = None,
        parameters_not_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_cause_interruption_if_modified: List[str] = None,
    ):
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        self.parameters_cause_interruption_if_modified = parameters_cause_interruption_if_modified
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        self.parameters_conditionally_cause_interruption_if_modified = parameters_conditionally_cause_interruption_if_modified
        self.parameters_not_allowed_to_be_modified = parameters_not_allowed_to_be_modified
        self.parameters_uncertainly_allowed_to_be_modified = parameters_uncertainly_allowed_to_be_modified
        self.parameters_uncertainly_cause_interruption_if_modified = parameters_uncertainly_cause_interruption_if_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters_allowed_to_be_modified is not None:
            result['ParametersAllowedToBeModified'] = self.parameters_allowed_to_be_modified
        if self.parameters_cause_interruption_if_modified is not None:
            result['ParametersCauseInterruptionIfModified'] = self.parameters_cause_interruption_if_modified
        if self.parameters_conditionally_allowed_to_be_modified is not None:
            result['ParametersConditionallyAllowedToBeModified'] = self.parameters_conditionally_allowed_to_be_modified
        if self.parameters_conditionally_cause_interruption_if_modified is not None:
            result['ParametersConditionallyCauseInterruptionIfModified'] = self.parameters_conditionally_cause_interruption_if_modified
        if self.parameters_not_allowed_to_be_modified is not None:
            result['ParametersNotAllowedToBeModified'] = self.parameters_not_allowed_to_be_modified
        if self.parameters_uncertainly_allowed_to_be_modified is not None:
            result['ParametersUncertainlyAllowedToBeModified'] = self.parameters_uncertainly_allowed_to_be_modified
        if self.parameters_uncertainly_cause_interruption_if_modified is not None:
            result['ParametersUncertainlyCauseInterruptionIfModified'] = self.parameters_uncertainly_cause_interruption_if_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParametersAllowedToBeModified') is not None:
            self.parameters_allowed_to_be_modified = m.get('ParametersAllowedToBeModified')
        if m.get('ParametersCauseInterruptionIfModified') is not None:
            self.parameters_cause_interruption_if_modified = m.get('ParametersCauseInterruptionIfModified')
        if m.get('ParametersConditionallyAllowedToBeModified') is not None:
            self.parameters_conditionally_allowed_to_be_modified = m.get('ParametersConditionallyAllowedToBeModified')
        if m.get('ParametersConditionallyCauseInterruptionIfModified') is not None:
            self.parameters_conditionally_cause_interruption_if_modified = m.get('ParametersConditionallyCauseInterruptionIfModified')
        if m.get('ParametersNotAllowedToBeModified') is not None:
            self.parameters_not_allowed_to_be_modified = m.get('ParametersNotAllowedToBeModified')
        if m.get('ParametersUncertainlyAllowedToBeModified') is not None:
            self.parameters_uncertainly_allowed_to_be_modified = m.get('ParametersUncertainlyAllowedToBeModified')
        if m.get('ParametersUncertainlyCauseInterruptionIfModified') is not None:
            self.parameters_uncertainly_cause_interruption_if_modified = m.get('ParametersUncertainlyCauseInterruptionIfModified')
        return self


class UpdateStackResponseBody(TeaModel):
    def __init__(
        self,
        dry_run_result: UpdateStackResponseBodyDryRunResult = None,
        request_id: str = None,
        stack_id: str = None,
    ):
        self.dry_run_result = dry_run_result
        self.request_id = request_id
        self.stack_id = stack_id

    def validate(self):
        if self.dry_run_result:
            self.dry_run_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run_result is not None:
            result['DryRunResult'] = self.dry_run_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRunResult') is not None:
            temp_model = UpdateStackResponseBodyDryRunResult()
            self.dry_run_result = temp_model.from_map(m['DryRunResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        return self


class UpdateStackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStackGroupRequestAutoDeployment(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        retain_stacks_on_account_removal: bool = None,
    ):
        self.enabled = enabled
        self.retain_stacks_on_account_removal = retain_stacks_on_account_removal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.retain_stacks_on_account_removal is not None:
            result['RetainStacksOnAccountRemoval'] = self.retain_stacks_on_account_removal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('RetainStacksOnAccountRemoval') is not None:
            self.retain_stacks_on_account_removal = m.get('RetainStacksOnAccountRemoval')
        return self


class UpdateStackGroupRequestDeploymentTargets(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        rd_folder_ids: List[str] = None,
    ):
        self.account_ids = account_ids
        # test
        self.rd_folder_ids = rd_folder_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        return self


class UpdateStackGroupRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateStackGroupRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        administration_role_name: str = None,
        auto_deployment: UpdateStackGroupRequestAutoDeployment = None,
        client_token: str = None,
        deployment_targets: UpdateStackGroupRequestDeploymentTargets = None,
        description: str = None,
        execution_role_name: str = None,
        operation_description: str = None,
        operation_preferences: Dict[str, Any] = None,
        parameters: List[UpdateStackGroupRequestParameters] = None,
        permission_model: str = None,
        region_id: str = None,
        region_ids: List[str] = None,
        stack_group_name: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.account_ids = account_ids
        self.administration_role_name = administration_role_name
        self.auto_deployment = auto_deployment
        self.client_token = client_token
        self.deployment_targets = deployment_targets
        self.description = description
        self.execution_role_name = execution_role_name
        self.operation_description = operation_description
        self.operation_preferences = operation_preferences
        # test
        self.parameters = parameters
        self.permission_model = permission_model
        self.region_id = region_id
        self.region_ids = region_ids
        self.stack_group_name = stack_group_name
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version

    def validate(self):
        if self.auto_deployment:
            self.auto_deployment.validate()
        if self.deployment_targets:
            self.deployment_targets.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.auto_deployment is not None:
            result['AutoDeployment'] = self.auto_deployment.to_map()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('AutoDeployment') is not None:
            temp_model = UpdateStackGroupRequestAutoDeployment()
            self.auto_deployment = temp_model.from_map(m['AutoDeployment'])
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeploymentTargets') is not None:
            temp_model = UpdateStackGroupRequestDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m['DeploymentTargets'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateStackGroupRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class UpdateStackGroupShrinkRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateStackGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        administration_role_name: str = None,
        auto_deployment_shrink: str = None,
        client_token: str = None,
        deployment_targets_shrink: str = None,
        description: str = None,
        execution_role_name: str = None,
        operation_description: str = None,
        operation_preferences_shrink: str = None,
        parameters: List[UpdateStackGroupShrinkRequestParameters] = None,
        permission_model: str = None,
        region_id: str = None,
        region_ids_shrink: str = None,
        stack_group_name: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.account_ids_shrink = account_ids_shrink
        self.administration_role_name = administration_role_name
        self.auto_deployment_shrink = auto_deployment_shrink
        self.client_token = client_token
        self.deployment_targets_shrink = deployment_targets_shrink
        self.description = description
        self.execution_role_name = execution_role_name
        self.operation_description = operation_description
        self.operation_preferences_shrink = operation_preferences_shrink
        # test
        self.parameters = parameters
        self.permission_model = permission_model
        self.region_id = region_id
        self.region_ids_shrink = region_ids_shrink
        self.stack_group_name = stack_group_name
        self.template_body = template_body
        self.template_id = template_id
        self.template_url = template_url
        self.template_version = template_version

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
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name
        if self.auto_deployment_shrink is not None:
            result['AutoDeployment'] = self.auto_deployment_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deployment_targets_shrink is not None:
            result['DeploymentTargets'] = self.deployment_targets_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')
        if m.get('AutoDeployment') is not None:
            self.auto_deployment_shrink = m.get('AutoDeployment')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeploymentTargets') is not None:
            self.deployment_targets_shrink = m.get('DeploymentTargets')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateStackGroupShrinkRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class UpdateStackGroupResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateStackGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStackGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateStackGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStackInstancesRequestDeploymentTargets(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        rd_folder_ids: List[str] = None,
    ):
        self.account_ids = account_ids
        # test
        self.rd_folder_ids = rd_folder_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.rd_folder_ids is not None:
            result['RdFolderIds'] = self.rd_folder_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('RdFolderIds') is not None:
            self.rd_folder_ids = m.get('RdFolderIds')
        return self


class UpdateStackInstancesRequestParameterOverrides(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateStackInstancesRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        client_token: str = None,
        deployment_targets: UpdateStackInstancesRequestDeploymentTargets = None,
        operation_description: str = None,
        operation_preferences: Dict[str, Any] = None,
        parameter_overrides: List[UpdateStackInstancesRequestParameterOverrides] = None,
        region_id: str = None,
        region_ids: List[str] = None,
        stack_group_name: str = None,
        timeout_in_minutes: int = None,
    ):
        self.account_ids = account_ids
        self.client_token = client_token
        self.deployment_targets = deployment_targets
        self.operation_description = operation_description
        self.operation_preferences = operation_preferences
        # test
        self.parameter_overrides = parameter_overrides
        self.region_id = region_id
        self.region_ids = region_ids
        self.stack_group_name = stack_group_name
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        if self.deployment_targets:
            self.deployment_targets.validate()
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deployment_targets is not None:
            result['DeploymentTargets'] = self.deployment_targets.to_map()
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences is not None:
            result['OperationPreferences'] = self.operation_preferences
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeploymentTargets') is not None:
            temp_model = UpdateStackInstancesRequestDeploymentTargets()
            self.deployment_targets = temp_model.from_map(m['DeploymentTargets'])
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences = m.get('OperationPreferences')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = UpdateStackInstancesRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        return self


class UpdateStackInstancesShrinkRequestParameterOverrides(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateStackInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        client_token: str = None,
        deployment_targets_shrink: str = None,
        operation_description: str = None,
        operation_preferences_shrink: str = None,
        parameter_overrides: List[UpdateStackInstancesShrinkRequestParameterOverrides] = None,
        region_id: str = None,
        region_ids_shrink: str = None,
        stack_group_name: str = None,
        timeout_in_minutes: int = None,
    ):
        self.account_ids_shrink = account_ids_shrink
        self.client_token = client_token
        self.deployment_targets_shrink = deployment_targets_shrink
        self.operation_description = operation_description
        self.operation_preferences_shrink = operation_preferences_shrink
        # test
        self.parameter_overrides = parameter_overrides
        self.region_id = region_id
        self.region_ids_shrink = region_ids_shrink
        self.stack_group_name = stack_group_name
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        if self.parameter_overrides:
            for k in self.parameter_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deployment_targets_shrink is not None:
            result['DeploymentTargets'] = self.deployment_targets_shrink
        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description
        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink
        result['ParameterOverrides'] = []
        if self.parameter_overrides is not None:
            for k in self.parameter_overrides:
                result['ParameterOverrides'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink
        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeploymentTargets') is not None:
            self.deployment_targets_shrink = m.get('DeploymentTargets')
        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')
        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')
        self.parameter_overrides = []
        if m.get('ParameterOverrides') is not None:
            for k in m.get('ParameterOverrides'):
                temp_model = UpdateStackInstancesShrinkRequestParameterOverrides()
                self.parameter_overrides.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')
        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')
        return self


class UpdateStackInstancesResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateStackInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStackInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateStackInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStackTemplateByResourcesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        logical_resource_id: List[str] = None,
        region_id: str = None,
        stack_id: str = None,
        template_format: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.logical_resource_id = logical_resource_id
        self.region_id = region_id
        self.stack_id = stack_id
        self.template_format = template_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        return self


class UpdateStackTemplateByResourcesResponseBody(TeaModel):
    def __init__(
        self,
        new_template_body: str = None,
        old_template_body: str = None,
        request_id: str = None,
    ):
        self.new_template_body = new_template_body
        self.old_template_body = old_template_body
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_template_body is not None:
            result['NewTemplateBody'] = self.new_template_body
        if self.old_template_body is not None:
            result['OldTemplateBody'] = self.old_template_body
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewTemplateBody') is not None:
            self.new_template_body = m.get('NewTemplateBody')
        if m.get('OldTemplateBody') is not None:
            self.old_template_body = m.get('OldTemplateBody')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateStackTemplateByResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStackTemplateByResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateStackTemplateByResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        template_body: str = None,
        template_id: str = None,
        template_name: str = None,
        template_url: str = None,
    ):
        self.description = description
        self.template_body = template_body
        self.template_id = template_id
        self.template_name = template_name
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_id: str = None,
    ):
        self.request_id = request_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateScratchRequestPreferenceParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateTemplateScratchRequestSourceResourceGroup(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_type_filter: List[str] = None,
    ):
        self.resource_group_id = resource_group_id
        self.resource_type_filter = resource_type_filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type_filter is not None:
            result['ResourceTypeFilter'] = self.resource_type_filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceTypeFilter') is not None:
            self.resource_type_filter = m.get('ResourceTypeFilter')
        return self


class UpdateTemplateScratchRequestSourceResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class UpdateTemplateScratchRequestSourceTag(TeaModel):
    def __init__(
        self,
        resource_tags: Dict[str, Any] = None,
        resource_type_filter: List[str] = None,
    ):
        self.resource_tags = resource_tags
        self.resource_type_filter = resource_type_filter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_tags is not None:
            result['ResourceTags'] = self.resource_tags
        if self.resource_type_filter is not None:
            result['ResourceTypeFilter'] = self.resource_type_filter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTags') is not None:
            self.resource_tags = m.get('ResourceTags')
        if m.get('ResourceTypeFilter') is not None:
            self.resource_type_filter = m.get('ResourceTypeFilter')
        return self


class UpdateTemplateScratchRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        execution_mode: str = None,
        logical_id_strategy: str = None,
        preference_parameters: List[UpdateTemplateScratchRequestPreferenceParameters] = None,
        region_id: str = None,
        source_resource_group: UpdateTemplateScratchRequestSourceResourceGroup = None,
        source_resources: List[UpdateTemplateScratchRequestSourceResources] = None,
        source_tag: UpdateTemplateScratchRequestSourceTag = None,
        template_scratch_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.execution_mode = execution_mode
        self.logical_id_strategy = logical_id_strategy
        self.preference_parameters = preference_parameters
        self.region_id = region_id
        self.source_resource_group = source_resource_group
        self.source_resources = source_resources
        self.source_tag = source_tag
        self.template_scratch_id = template_scratch_id

    def validate(self):
        if self.preference_parameters:
            for k in self.preference_parameters:
                if k:
                    k.validate()
        if self.source_resource_group:
            self.source_resource_group.validate()
        if self.source_resources:
            for k in self.source_resources:
                if k:
                    k.validate()
        if self.source_tag:
            self.source_tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.logical_id_strategy is not None:
            result['LogicalIdStrategy'] = self.logical_id_strategy
        result['PreferenceParameters'] = []
        if self.preference_parameters is not None:
            for k in self.preference_parameters:
                result['PreferenceParameters'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_resource_group is not None:
            result['SourceResourceGroup'] = self.source_resource_group.to_map()
        result['SourceResources'] = []
        if self.source_resources is not None:
            for k in self.source_resources:
                result['SourceResources'].append(k.to_map() if k else None)
        if self.source_tag is not None:
            result['SourceTag'] = self.source_tag.to_map()
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('LogicalIdStrategy') is not None:
            self.logical_id_strategy = m.get('LogicalIdStrategy')
        self.preference_parameters = []
        if m.get('PreferenceParameters') is not None:
            for k in m.get('PreferenceParameters'):
                temp_model = UpdateTemplateScratchRequestPreferenceParameters()
                self.preference_parameters.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceResourceGroup') is not None:
            temp_model = UpdateTemplateScratchRequestSourceResourceGroup()
            self.source_resource_group = temp_model.from_map(m['SourceResourceGroup'])
        self.source_resources = []
        if m.get('SourceResources') is not None:
            for k in m.get('SourceResources'):
                temp_model = UpdateTemplateScratchRequestSourceResources()
                self.source_resources.append(temp_model.from_map(k))
        if m.get('SourceTag') is not None:
            temp_model = UpdateTemplateScratchRequestSourceTag()
            self.source_tag = temp_model.from_map(m['SourceTag'])
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        return self


class UpdateTemplateScratchShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        execution_mode: str = None,
        logical_id_strategy: str = None,
        preference_parameters_shrink: str = None,
        region_id: str = None,
        source_resource_group_shrink: str = None,
        source_resources_shrink: str = None,
        source_tag_shrink: str = None,
        template_scratch_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.execution_mode = execution_mode
        self.logical_id_strategy = logical_id_strategy
        self.preference_parameters_shrink = preference_parameters_shrink
        self.region_id = region_id
        self.source_resource_group_shrink = source_resource_group_shrink
        self.source_resources_shrink = source_resources_shrink
        self.source_tag_shrink = source_tag_shrink
        self.template_scratch_id = template_scratch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.logical_id_strategy is not None:
            result['LogicalIdStrategy'] = self.logical_id_strategy
        if self.preference_parameters_shrink is not None:
            result['PreferenceParameters'] = self.preference_parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_resource_group_shrink is not None:
            result['SourceResourceGroup'] = self.source_resource_group_shrink
        if self.source_resources_shrink is not None:
            result['SourceResources'] = self.source_resources_shrink
        if self.source_tag_shrink is not None:
            result['SourceTag'] = self.source_tag_shrink
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('LogicalIdStrategy') is not None:
            self.logical_id_strategy = m.get('LogicalIdStrategy')
        if m.get('PreferenceParameters') is not None:
            self.preference_parameters_shrink = m.get('PreferenceParameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceResourceGroup') is not None:
            self.source_resource_group_shrink = m.get('SourceResourceGroup')
        if m.get('SourceResources') is not None:
            self.source_resources_shrink = m.get('SourceResources')
        if m.get('SourceTag') is not None:
            self.source_tag_shrink = m.get('SourceTag')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        return self


class UpdateTemplateScratchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_scratch_id: str = None,
    ):
        self.request_id = request_id
        self.template_scratch_id = template_scratch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        return self


class UpdateTemplateScratchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTemplateScratchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateTemplateScratchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateTemplateRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        template_body: str = None,
        template_url: str = None,
        validation_option: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.template_body = template_body
        self.template_url = template_url
        self.validation_option = validation_option

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.validation_option is not None:
            result['ValidationOption'] = self.validation_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('ValidationOption') is not None:
            self.validation_option = m.get('ValidationOption')
        return self


class ValidateTemplateResponseBodyOutputs(TeaModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        output_key: str = None,
    ):
        self.description = description
        self.label = label
        self.output_key = output_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.output_key is not None:
            result['OutputKey'] = self.output_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('OutputKey') is not None:
            self.output_key = m.get('OutputKey')
        return self


class ValidateTemplateResponseBodyResourceTypes(TeaModel):
    def __init__(
        self,
        data_sources: List[str] = None,
        resources: List[str] = None,
    ):
        self.data_sources = data_sources
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_sources is not None:
            result['DataSources'] = self.data_sources
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSources') is not None:
            self.data_sources = m.get('DataSources')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class ValidateTemplateResponseBodyResources(TeaModel):
    def __init__(
        self,
        logical_resource_id_pattern: str = None,
        resource_path: str = None,
        resource_type: str = None,
    ):
        self.logical_resource_id_pattern = logical_resource_id_pattern
        self.resource_path = resource_path
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_resource_id_pattern is not None:
            result['LogicalResourceIdPattern'] = self.logical_resource_id_pattern
        if self.resource_path is not None:
            result['ResourcePath'] = self.resource_path
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceIdPattern') is not None:
            self.logical_resource_id_pattern = m.get('LogicalResourceIdPattern')
        if m.get('ResourcePath') is not None:
            self.resource_path = m.get('ResourcePath')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ValidateTemplateResponseBodyUpdateInfo(TeaModel):
    def __init__(
        self,
        parameters_allowed_to_be_modified: List[str] = None,
        parameters_cause_interruption_if_modified: List[str] = None,
        parameters_conditionally_allowed_to_be_modified: List[str] = None,
        parameters_conditionally_cause_interruption_if_modified: List[str] = None,
        parameters_not_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_cause_interruption_if_modified: List[str] = None,
    ):
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        self.parameters_cause_interruption_if_modified = parameters_cause_interruption_if_modified
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        self.parameters_conditionally_cause_interruption_if_modified = parameters_conditionally_cause_interruption_if_modified
        self.parameters_not_allowed_to_be_modified = parameters_not_allowed_to_be_modified
        self.parameters_uncertainly_allowed_to_be_modified = parameters_uncertainly_allowed_to_be_modified
        self.parameters_uncertainly_cause_interruption_if_modified = parameters_uncertainly_cause_interruption_if_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters_allowed_to_be_modified is not None:
            result['ParametersAllowedToBeModified'] = self.parameters_allowed_to_be_modified
        if self.parameters_cause_interruption_if_modified is not None:
            result['ParametersCauseInterruptionIfModified'] = self.parameters_cause_interruption_if_modified
        if self.parameters_conditionally_allowed_to_be_modified is not None:
            result['ParametersConditionallyAllowedToBeModified'] = self.parameters_conditionally_allowed_to_be_modified
        if self.parameters_conditionally_cause_interruption_if_modified is not None:
            result['ParametersConditionallyCauseInterruptionIfModified'] = self.parameters_conditionally_cause_interruption_if_modified
        if self.parameters_not_allowed_to_be_modified is not None:
            result['ParametersNotAllowedToBeModified'] = self.parameters_not_allowed_to_be_modified
        if self.parameters_uncertainly_allowed_to_be_modified is not None:
            result['ParametersUncertainlyAllowedToBeModified'] = self.parameters_uncertainly_allowed_to_be_modified
        if self.parameters_uncertainly_cause_interruption_if_modified is not None:
            result['ParametersUncertainlyCauseInterruptionIfModified'] = self.parameters_uncertainly_cause_interruption_if_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParametersAllowedToBeModified') is not None:
            self.parameters_allowed_to_be_modified = m.get('ParametersAllowedToBeModified')
        if m.get('ParametersCauseInterruptionIfModified') is not None:
            self.parameters_cause_interruption_if_modified = m.get('ParametersCauseInterruptionIfModified')
        if m.get('ParametersConditionallyAllowedToBeModified') is not None:
            self.parameters_conditionally_allowed_to_be_modified = m.get('ParametersConditionallyAllowedToBeModified')
        if m.get('ParametersConditionallyCauseInterruptionIfModified') is not None:
            self.parameters_conditionally_cause_interruption_if_modified = m.get('ParametersConditionallyCauseInterruptionIfModified')
        if m.get('ParametersNotAllowedToBeModified') is not None:
            self.parameters_not_allowed_to_be_modified = m.get('ParametersNotAllowedToBeModified')
        if m.get('ParametersUncertainlyAllowedToBeModified') is not None:
            self.parameters_uncertainly_allowed_to_be_modified = m.get('ParametersUncertainlyAllowedToBeModified')
        if m.get('ParametersUncertainlyCauseInterruptionIfModified') is not None:
            self.parameters_uncertainly_cause_interruption_if_modified = m.get('ParametersUncertainlyCauseInterruptionIfModified')
        return self


class ValidateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        outputs: List[ValidateTemplateResponseBodyOutputs] = None,
        parameters: List[Dict[str, Any]] = None,
        request_id: str = None,
        resource_types: ValidateTemplateResponseBodyResourceTypes = None,
        resources: List[ValidateTemplateResponseBodyResources] = None,
        update_info: ValidateTemplateResponseBodyUpdateInfo = None,
    ):
        self.description = description
        self.outputs = outputs
        self.parameters = parameters
        self.request_id = request_id
        self.resource_types = resource_types
        self.resources = resources
        self.update_info = update_info

    def validate(self):
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        if self.resource_types:
            self.resource_types.validate()
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()
        if self.update_info:
            self.update_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types.to_map()
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.update_info is not None:
            result['UpdateInfo'] = self.update_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = ValidateTemplateResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k))
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceTypes') is not None:
            temp_model = ValidateTemplateResponseBodyResourceTypes()
            self.resource_types = temp_model.from_map(m['ResourceTypes'])
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ValidateTemplateResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('UpdateInfo') is not None:
            temp_model = ValidateTemplateResponseBodyUpdateInfo()
            self.update_info = temp_model.from_map(m['UpdateInfo'])
        return self


class ValidateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ValidateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


