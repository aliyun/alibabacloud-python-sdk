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
        # The operations that you want to cancel on the stack.
        self.allowed_stack_operations = allowed_stack_operations
        # The method that you want to use to cancel the operations. Valid values:
        # 
        # *   Quick: cancels the operations on the stack at the earliest opportunity. In this case, Resource Orchestration Service (ROS) stops scheduling new resources and stops running resources at the earliest opportunity. If you use this method, the resource status may become invalid and subsequent stack operations may be affected.
        # *   Safe (default): cancels the operations on the stack in a secure manner. In this case, ROS stops scheduling new resources and waits for running resources to be stopped.
        self.cancel_type = cancel_type
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The stack ID.
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
        # The request ID.
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
        # The method to cancel the update operation. Valid values:
        # 
        # *   Quick: cancels the update of a stack as soon as possible.
        # *   Safe: cancels the update of a stack as safely as possible.
        self.cancel_type = cancel_type
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the stack.
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
        # The ID of the request.
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
        # The name of template parameter N that you want to use to override a specific parameter. If you do not specify the name and value of a template parameter, ROS uses the name and value specified in the previous operation that was performed to create the stack. Maximum value of N: 200.
        # 
        # > This parameter takes effect only when Mode is set to Recreate.
        self.parameter_key = parameter_key
        # The value of template parameter N that you want to use to override a specific parameter. Maximum value of N: 200.
        # 
        # For ROS stacks, the template parameters that you use to override specific parameters are subject to the following limits:
        # 
        # *   You cannot change the condition values in the Conditions section of a template from true to false or from false to true.
        # *   The template parameters can be referenced only by resources that ROS continues to create.
        # 
        # > This parameter takes effect only when Mode is set to Recreate.
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
        # Specifies whether only to validate the stack in the request. Valid values:
        # 
        # *   true: only validates the stack.
        # *   false (default): validates and continues to create the stack.
        self.dry_run = dry_run
        # The mode in which ROS continues to create the stack. Valid values:
        # 
        # *   Recreate (default)
        # 
        #     If you set this parameter to Recreate, ROS continues to create only the following types of resources:
        # 
        #     *   Resources that fail to be created
        #     *   Resources that you specify for RecreatingResources.N
        #     *   Dependencies of the resources that you specify for RecreatingResources.N
        #     *   Resources that you have not created
        # 
        # > RecreatingResources.N, TemplateBody, TemplateURL, and Parameters take effect only when Mode is set to Recreate.
        # 
        # *   Ignore
        # 
        #     *   ROS ignores and discards resources that fail to be created and you have not created, and considers that the stack is successfully created.
        #     *   The body of the template that you use to create the stack is changed.
        # 
        # > This mode is available only for ROS stacks.
        self.mode = mode
        # The maximum number of concurrent operations that can be performed on resources.
        # 
        # By default, this parameter is empty. You can set this parameter to an integer that is greater than or equal to 0.
        # 
        # > - If you set this parameter to an integer that is greater than 0, the integer is used.
        # > - If you set this parameter to 0, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # > - If you leave this parameter empty, the value that you specified for this parameter in the previous request is used. If you left this parameter empty in the previous request, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # > - If you set this parameter to a specific value, ROS associates the value with the stack. The value affects subsequent operations on the stack.
        self.parallelism = parallelism
        # The template parameters that you want to use to override specific parameters.
        self.parameters = parameters
        # The name of the RAM role. Resource Orchestration Service (ROS) assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.\
        # ROS assumes the RAM role to perform operations on the stack. If you have permissions to perform operations on the stack but do not have permissions to use the RAM role, ROS still assumes the RAM role. You must make sure that the least privileges are granted to the RAM role.\
        # If you do not specify this parameter, ROS assumes the existing role that is associated with the stack. If no roles are available, ROS uses a temporary credential that is generated from the credentials of your account.\
        # The name of the RAM role can be up to 64 bytes in length.
        self.ram_role_name = ram_role_name
        # The options that ROS adopts when ROS continues to create the stack.
        self.recreating_options = recreating_options
        # The resources that ROS continues to create after the resources failed to be created. You can add new resources to the resources that ROS continues to create. ROS continues to create all dependencies of the new resources.
        # 
        # > This parameter is available only for ROS stacks.
        self.recreating_resources = recreating_resources
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The stack ID.
        self.stack_id = stack_id
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length.\
        # If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # A ROS template is subject to the following limits:
        # 
        # *   You can modify only the following sections in the template: Description, Metadata, Resources, and Outputs.
        # 
        # *   You cannot add sections to or remove sections from the template.
        # 
        # *   The Resources section is subject to the following limits:
        # 
        #     *   You cannot delete the resources or change the template body for the resources that you do not want to continue to create.
        #     *   You can delete the resources or change the template body for the resources that you want to continue to create.
        #     *   You can add resources to this section.
        # 
        #  
        # 
        # > - This parameter takes effect only when Mode is set to Recreate.
        # > - You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId. If you do not specify the parameters, the existing template is used.
        self.template_body = template_body
        # The template ID. This parameter applies to shared and private templates.
        # 
        # > - This parameter takes effect when `Mode` is set to `Recreate`. When you specify TemplateId of a template, the template is subject to the limits that are described for `TemplateBody` in this topic.
        # > - You can specify only one of the following parameters: `TemplateBody`, `TemplateURL`, and `TemplateId`. If you do not specify the parameters, the existing template is used.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length.
        # 
        # If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > - This parameter takes effect only when Mode is set to Recreate. When you specify TemplateURL of a template, the template is subject to the limits that are described for TemplateBody in this topic.
        # > - You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId. If you do not specify the parameters, the existing template is used.
        self.template_url = template_url
        # The version of the template. This parameter takes effect only when TemplateId is specified.
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
        # The parameters that can be modified.
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        # The parameters that can be modified under specific conditions.
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        # The parameters that cannot be modified.
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
        # The validation result.
        self.dry_run_result = dry_run_result
        # The request ID.
        self.request_id = request_id
        # The stack ID.
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
        # The key of parameter N that is defined in the template. If you do not specify the key and value of a parameter, ROS uses the default name and value that are defined in the template. Maximum value of N: 200.
        # 
        # >  Parameters is optional. If you specify Parameters, you must also specify Parameters.N.ParameterKey.
        self.parameter_key = parameter_key
        # The value of parameter N that is defined in the template. Maximum value of N: 200.
        # 
        # >  Parameters is optional. If you specify Parameters, you must also specify Parameters.N.ParameterValue.
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
        # The logical ID of resource N that you want to import. The logical ID specifies the name of resource N that is defined in the template.
        # 
        # > This parameter takes effect only if you set ChangeSetType to IMPORT. ResourcesToImport is optional. If you specify ResourcesToImport, you must also specify ResourcesToImport.N.LogicalResourceId.
        self.logical_resource_id = logical_resource_id
        # The key-value mapping between strings. The value is a JSON string that identifies resource N that you want to import.\
        # A key is an identifier for a resource and a value is an assignment of data to the key. For example, VpcId is a key that indicates the ID of a virtual private cloud (VPC), and `vpc-2zevx9ios****` is a value that is assigned to VpcId. You can call the [GetTemplateSummary](~~172485~~) operation to obtain the key of a resource.
        # 
        # > This parameter takes effect only if you set ChangeSetType to IMPORT. ResourcesToImport is optional. If you specify ResourcesToImport, you must also specify ResourcesToImport.N.ResourceIdentifier.
        self.resource_identifier = resource_identifier
        # The type of resource N that you want to import. The resource type must be the same as the resource type that is defined in the template.
        # 
        # > This parameter takes effect only if you set ChangeSetType to IMPORT. ResourcesToImport is optional. If you specify ResourcesToImport, you must also specify ResourcesToImport.N.ResourceType.
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
        # The name of the change set.\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). The name must start with a digit or a letter.
        # 
        # > Make sure that the name is unique among all names of change sets that are associated with the specified stack.
        self.change_set_name = change_set_name
        # The type of the change set. Valid values:
        # 
        # *   CREATE: creates a change set for a new stack.
        # *   UPDATE (default): creates a change set for an existing stack.
        # *   IMPORT: creates a change set for a new stack or an existing stack to import resources that are not managed by ROS.
        # 
        # If you create a change set for a new stack, ROS generates a unique stack ID for the stack. The stack remains in the REVIEW_IN_PROGRESS state until you execute the change set.\
        # If you want to create a change set for a new stack, do not set ChangeSetType to UPDATE. If you want to create a change set for an existing stack, do not set ChangeSetType to CREATE.
        self.change_set_type = change_set_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests.\
        # The token can contain letters, digits, hyphens (-), and underscores (\_) and cannot exceed 64 characters in length.\
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The description of the change set. The description can be up to 1,024 bytes in length.
        self.description = description
        # Specifies whether to disable rollback when the stack fails to be created.\
        # Valid values:
        # 
        # *   true: disables rollback for the stack when the stack fails to be created.
        # *   false (default): enables rollback for the stack when the stack fails to be created.
        # 
        # > This parameter takes effect only if you set ChangeSetType to CREATE or IMPORT.
        self.disable_rollback = disable_rollback
        # The callback URLs that are used to receive stack events.
        self.notification_urls = notification_urls
        # The maximum number of concurrent operations that can be performed on resources. By default, this parameter is empty. You can set this parameter to an integer that is greater than or equal to 0. If you set this parameter to a specific value, ROS associates the value with the stack. The value can affect subsequent operations on the stack.
        # 
        # This parameter takes effect only if you set ChangeSetType to CREATE or UPDATE.
        # 
        # *   Valid values for change sets of the CREATE type:
        # 
        #     *   If you set this parameter to an integer that is greater than 0, the integer is used.
        #     *   If you set this parameter to 0 or leave this parameter empty, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # 
        # *   Valid values for change sets of the UPDATE type:
        # 
        #     *   If you set this parameter to an integer that is greater than 0, the integer is used.
        #     *   If you set this parameter to 0, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        #     *   If you leave this parameter empty, the value that you specified for this parameter in the previous request is used. If you left this parameter empty in the previous request, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        self.parallelism = parallelism
        # The parameters that are defined in the template.
        self.parameters = parameters
        # The name of the Resource Access Management (RAM) role. Resource Orchestration Service (ROS) assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.\
        # ROS assumes the role to perform operations on the stack. If you have permissions to perform operations on the stack but do not have permissions to use the RAM role, ROS still assumes the RAM role. You must make sure that the least privileges are granted to the RAM role.\
        # If you do not specify this parameter, ROS uses the existing role that is associated with the stack. If no roles are available for ROS to assume, ROS uses a temporary credential that is generated from the credentials of your Alibaba Cloud account.\
        # The name of the RAM role can be up to 64 bytes in length.
        self.ram_role_name = ram_role_name
        # The region ID of the change set. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # Specifies whether to enable replacement update if a resource property is changed and you cannot modify the new resource property. For a change, the physical ID of the resource remains unchanged. For a replacement update, the existing resource is deleted, a new resource is created, and the physical ID of the resource is changed. Valid values:
        # 
        # *   Enabled
        # *   Disabled (default)
        # 
        # > Operations that you perform to modify the resource properties for an update take precedence over operations you perform to replace the resource properties for an update. This parameter takes effect only if you set ChangeSetType to UPDATE.
        self.replacement_option = replacement_option
        # The resources that you want to import into the stack.
        self.resources_to_import = resources_to_import
        # The ID of the stack for which you want to create a change set. ROS compares the stack information with the information that you submit, such as a modified template or a changed parameter value, to generate the change set.
        # 
        # > This parameter takes effect only for change sets of the UPDATE or IMPORT.
        self.stack_id = stack_id
        # The name of the stack for which you want to create the change set.\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). The name must start with a digit or a letter.
        # 
        # > This parameter takes effect only if you set ChangeSetType to CREATE or IMPORT.
        self.stack_name = stack_name
        # The structure of the stack policy body. The policy body must be 1 to 16,384 bytes in length. If you set ChangeSetType to CREATE, you can specify StackPolicyBody or StackPolicyURL. If you set ChangeSetType to UPDATE, you can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_body = stack_policy_body
        # The structure of the temporary overriding stack policy. The policy body must be 1 to 16,384 bytes in length.\
        # If you need to update protected resources, specify a temporary overriding stack policy for the resources during the update. If you do not specify a temporary overriding stack policy, the existing stack policy that is associated with the stack is used.\
        # This parameter takes effect only if you set ChangeSetType to UPDATE. You can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_during_update_body = stack_policy_during_update_body
        # The URL of the stack policy based on which the stack is updated. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an OSS bucket, such as oss://ros/stack-policy/demo and oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length.
        # 
        # > If you do not specify the region of the OSS bucket, the value of RegionId is used.
        # 
        # The URL can be up to 1,350 bytes in length.\
        # If you need to update protected resources, specify a temporary overriding stack policy for the resources during the update. If you do not specify a stack policy, the existing policy that is associated with the stack is used. This parameter takes effect only if you set ChangeSetType to UPDATE. You can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_during_update_url = stack_policy_during_update_url
        # The URL of the file that contains the stack policy. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo and oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length.
        # 
        # > If you do not specify the region of the OSS bucket, the value of RegionId is used.
        # 
        # You can specify only one of the following parameters: StackPolicyBody and StackPolicyURL.\
        # The URL can be up to 1,350 bytes in length.
        # 
        # If you set ChangeSetType to CREATE, you can specify StackPolicyBody or StackPolicyURL. If you set ChangeSetType to UPDATE, you can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_url = stack_policy_url
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The ID of the scenario template.
        self.template_scratch_id = template_scratch_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an OSS bucket, such as oss://ros/template/demo and oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length.
        # 
        # > If you do not specify the region of the OSS bucket, the value of RegionId is used.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        # 
        # The URL can be up to 1,024 bytes in length.
        self.template_url = template_url
        # The version of the template.
        # 
        # > This parameter takes effect only if you specify TemplateId.
        self.template_version = template_version
        # The amount of time that can elapse before the stack enters the CREATE_FAILED or UPDATE_FAILED state.\
        # If you set ChangeSetType to CREATE, this parameter is required. If you set ChangeSetType to UPDATE, this parameter is optional.
        # 
        # *   Unit: minutes.
        # *   Valid values: 10 to 1440.
        # *   Default value: 60.
        self.timeout_in_minutes = timeout_in_minutes
        # Specifies whether to use the values that were passed last time for the parameters that you do not specify in the current request. Valid values:
        # 
        # *   true
        # *   false (default)
        # 
        # > This parameter takes effect only if you set ChangeSetType to UPDATE or IMPORT.
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
        # The ID of the change set.
        self.change_set_id = change_set_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the stack.
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


class CreateDiagnosticRequest(TeaModel):
    def __init__(
        self,
        diagnostic_key: str = None,
        diagnostic_type: str = None,
        lang: str = None,
        product: str = None,
    ):
        # The keyword in the diagnosis.
        self.diagnostic_key = diagnostic_key
        # The type of the item that is diagnosed. Set the value to Stack, which specifies that the stack is diagnosed.
        self.diagnostic_type = diagnostic_type
        self.lang = lang
        # The name of the product that is diagonosed.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnostic_key is not None:
            result['DiagnosticKey'] = self.diagnostic_key
        if self.diagnostic_type is not None:
            result['DiagnosticType'] = self.diagnostic_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosticKey') is not None:
            self.diagnostic_key = m.get('DiagnosticKey')
        if m.get('DiagnosticType') is not None:
            self.diagnostic_type = m.get('DiagnosticType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class CreateDiagnosticResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        diagnostic_type: str = None,
        http_status_code: int = None,
        message: str = None,
        report_id: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code returned.
        self.code = code
        # The type of the item that is diagnosed.
        self.diagnostic_type = diagnostic_type
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The ID of the diagnostic report.
        self.report_id = report_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.diagnostic_type is not None:
            result['DiagnosticType'] = self.diagnostic_type
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DiagnosticType') is not None:
            self.diagnostic_type = m.get('DiagnosticType')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDiagnosticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDiagnosticResponseBody = None,
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
            temp_model = CreateDiagnosticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStackRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The key of parameter N that is defined in the template. If you do not specify the name and value of a parameter, ROS uses the default name and value that are specified in the template.
        # 
        # Maximum value of N: 200.\
        # The name must be 1 to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify Parameters.N.ParameterKey and Parameters.N.ParameterValue.
        self.parameter_key = parameter_key
        # The value of parameter N that is defined in the template.
        # 
        # Maximum value of N: 200.\
        # The value can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify Parameters.N.ParameterKey and Parameters.N.ParameterValue.
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
        # The key of tag N that you want to add to the stack.
        # 
        # Valid values of N: 1 to 20.
        # 
        # > - The Tags parameter is optional. If you specify Tags, you must specify Tags.N.Key.
        # > -  The tag of a stack is propagated to each resource that supports the tag feature in the stack. For more information, see [Propagate tags](~~201421~~).
        self.key = key
        # The value of tag N that you want to add to the stack.
        # 
        # Valid values of N: 1 to 20.
        # 
        # > The tag of a stack is propagated to each resource that supports the tag feature in the stack. For more information, see [Propagate tags](~~201421~~).
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
        create_options: List[str] = None,
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [Ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The creation option for the stack. Valid values:
        # 
        # *   KeepStackOnCreationComplete (default): After the stack is created, the stack and its resources are retained. The quota for the maximum number of stacks that can be created in ROS is consumed.
        # *   AbandonStackOnCreationComplete: After the stack is created, the stack is deleted, but its resources are retained. The quota for the maximum number of stacks that can be created in ROS is not consumed. If the stack fails to be created, the stack is retained.
        # *   AbandonStackOnCreationRollbackComplete: When the resources of the stack are rolled back after the stack fails to be created, the stack is deleted. The quota for the maximum number of stacks that can be created in ROS is not consumed. In other rollback scenarios, the stack is retained.
        # *   ManuallyPay: When you create the stack, you must manually pay for the subscription resources that are used. The following resource types support manual payment: `ALIYUN::ECS::InstanceGroup`, `ALIYUN::RDS::DBInstance`, `ALIYUN::SLB::LoadBalancer`, `ALIYUN::VPC::EIP`, and `ALIYUN::VPC::VpnGateway`.
        # 
        # >  You can specify only one of CreateOption and CreateOptions.
        self.create_option = create_option
        # The creation options for the stack.
        self.create_options = create_options
        # Specifies whether to enable deletion protection for the stack. Valid values:
        # 
        # *   Enabled.
        # *   Disabled (default). If deletion protection is disabled, you can delete the stack by using the ROS console or by calling the DeleteStack operation.
        # 
        # > The value of DeletionProtection that you specify for the root stack applies to its nested stacks.
        self.deletion_protection = deletion_protection
        # Specifies whether to disable rollback for the resources when the stack fails to be created.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (default)
        self.disable_rollback = disable_rollback
        # The callback URLs that are used to receive stack events. Valid values:
        # 
        # *   HTTP POST URL
        # 
        # Each URL can be up to 1,024 bytes in length.
        # 
        # *   eventbridge
        # 
        # When the status of a stack changes, ROS sends notifications to the EventBridge service. You can view the event information in the [EventBridge](https://eventbridge.console.aliyun.com) console.
        # 
        # > This feature is supported in the China (Hangzhou), China (Shanghai), China (Beijing), China (Hong Kong), and China (Zhangjiakou) regions.
        # 
        # Maximum value of N: 5. When the status of a stack changes, ROS sends a notification to the specified URL. When rollback is enabled for the stack, notifications are sent if the stack is in the CREATE_ROLLBACK or ROLLBACK state, but are not sent if the stack is in the CREATE_FAILED, UPDATE_FAILED, or IN_PROGRESS state.\
        # ROS sends notifications regardless of whether you specify the Outputs section. The following sample code provides an example on the content of a notification:
        # 
        #     {
        #        "Outputs": [
        #            {
        #                "Description": "No description given",
        #                "OutputKey": "InstanceId",
        #                "OutputValue": "i-xxx"
        #            }
        #        ],
        #        "StackId": "80bd6b6c-e888-4573-ae3b-93d29113****",
        #        "StackName": "test-notification-url",
        #        "Status": "CREATE_COMPLETE"
        #     }
        self.notification_urls = notification_urls
        # The maximum number of concurrent operations that can be performed on resources.
        # 
        # By default, this parameter is empty. You can set this parameter to an integer that is greater than or equal to 0.
        # 
        # 
        # 
        # > -  If you set this parameter to an integer that is greater than 0, the integer is used. If you set this parameter to 0 or leave this parameter empty, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # > -  If you set this parameter to a specific value, ROS associates the value with the stack. The value affects subsequent operations on the stack, such as an update operation.
        self.parallelism = parallelism
        # The parameters that are defined in the template.
        self.parameters = parameters
        # The name of the RAM role. ROS assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.\
        # ROS assumes the RAM role to perform operations on the stack. If you have permissions to perform operations on the stack but do not have permissions to use the RAM role, ROS still assumes the RAM role. You must make sure that the least privileges are granted to the RAM role.
        # 
        # If you do not specify this parameter, ROS assumes the existing role that is associated with the stack. If no roles are available, ROS uses a temporary credential that is generated from the credentials of your account.
        # 
        # The RAM role name can be up to 64 characters in length.
        self.ram_role_name = ram_role_name
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group. If you leave this parameter empty, the stack is added to the default resource group.
        # 
        # For more information about resource groups, see the "Resource group" section of the [What is Resource Management?](~~94475~~) topic.
        self.resource_group_id = resource_group_id
        # The name of the stack.\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a letter.
        self.stack_name = stack_name
        # The structure that contains the stack policy body. The policy body must be 1 to 16,384 bytes in length.
        # 
        # > You can specify only one of StackPolicyBody and StackPolicyURL.
        self.stack_policy_body = stack_policy_body
        # The URL of the file that contains the stack policy. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > You can specify only one of StackPolicyBody and StackPolicyURL.
        # 
        # The URL can be up to 1,350 bytes in length.
        self.stack_policy_url = stack_policy_url
        # The tags that you want to add to the stack.
        self.tags = tags
        self.template_body = template_body
        # The template ID. This parameter applies to shared templates and private templates.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_id = template_id
        # The scenario ID.
        # 
        # For more information about how to query the scenario ID, see [ListTemplateScratches](~~363050~~).
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_scratch_id = template_scratch_id
        # The region ID of the scenario. The default value is the same as the value of RegionId.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.template_scratch_region_id = template_scratch_region_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an OSS bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_url = template_url
        # The version of the template. This parameter takes effect only when TemplateId is specified.
        self.template_version = template_version
        # The timeout period for creating the stack.
        # 
        # *   Default value: 60.
        # *   Unit: minutes.
        # *   Valid values: 10 to 1440.
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
        if self.create_options is not None:
            result['CreateOptions'] = self.create_options
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
        if m.get('CreateOptions') is not None:
            self.create_options = m.get('CreateOptions')
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
        # The request ID.
        self.request_id = request_id
        # The stack ID.
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
        # Indicates whether automatic deployment is enabled.
        # 
        # Valid values:
        # 
        # *   true: Automatic deployment is enabled. If you add a member account to the folder to which the stack group belongs after you enable automatic deployment, ROS automatically adds the stacks in the stack group to the member account. If you remove a member account from the folder, ROS automatically deletes the stacks from the member account.
        # *   false: Automatic deployment is disabled. After you disable automatic deployment, the stacks remain unchanged when you add member accounts to or remove member accounts from the folder.
        self.enabled = enabled
        # Indicates whether the stacks within a member account are retained when you remove the member account from the folder.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # > You must specify RetainStacksOnAccountRemoval if Enabled is set to true.
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
        # The key of parameter N. If you do not specify the key and value of a parameter, ROS uses the default name and value that are defined in the template.
        # 
        # Maximum value of N: 200.
        # 
        # > Parameters is optional. If you specify Parameters, you must also specify Parameters.N.ParameterKey.
        self.parameter_key = parameter_key
        # The value of parameter N.
        # 
        # Maximum value of N: 200.
        # 
        # > Parameters is optional. If you specify Parameters, you must also specify Parameters.N.ParameterValue.
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
        # The tag key of the stack group.
        # 
        # > Tags is optional. If you want to specify Tags, you must also specify Tags.N.Key.
        self.key = key
        # The tag value of the stack group.
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
        capabilities: List[str] = None,
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
        # The name of the RAM role that you specify for the administrator account when you create a self-managed stack group. ROS assumes the administrator role to perform operations. If you do not specify this parameter, AliyunROSStackGroupAdministrationRole is used as the default value. ROS uses the administrator role to assume the execution role AliyunROSStackGroupExecutionRole to perform operations on the stacks in the stack group.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, and hyphens (-).
        self.administration_role_name = administration_role_name
        # The information about automatic deployment settings.
        # 
        # > You must specify this parameter if PermissionModel is set to SERVICE_MANAGED.
        self.auto_deployment = auto_deployment
        # The options for the stack group. You can specify up to one option.
        self.capabilities = capabilities
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can contain letters, digits, underscores (\_), and hyphens (-) and cannot exceed 64 characters in length.\
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The description of the stack group.\
        # The description must be 1 to 256 characters in length.
        self.description = description
        # The name of the RAM role that you specify for the execution account when you create a self-managed stack group. The administrator role AliyunROSStackGroupAdministrationRole assumes the execution role to perform operations. If you do not specify this parameter, AliyunROSStackGroupExecutionRole is used as the default value. ROS assumes the execution role to perform operations on the stacks in the stack group.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, and hyphens (-).
        self.execution_role_name = execution_role_name
        # The parameters of the stack group.
        self.parameters = parameters
        # The permission model of the stack group.
        # 
        # Valid values:
        # 
        # *   SELF_MANAGED (default): the self-managed permission model. If you create a self-managed stack group, you must create RAM roles within the administrator and execution accounts and establish a trust relationship between the accounts. Then, you can deploy stacks within the execution account.
        # *   SERVICE_MANAGED: the service-managed permission model. If you create a service-managed stack group, ROS creates service-linked roles for the administrator and execution accounts, and the administrator account uses its role to deploy stacks within the execution account.
        # 
        # > If you want to use the service-managed permission model to deploy stacks, your account must be the management account or a delegated administrator account of your resource directory and the trusted access feature is enabled for the account. For more information, see [Manage a delegated administrator account](~~308253~~) and [Enable trusted access](~~298229~~).
        self.permission_model = permission_model
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group. If you do not specify this parameter, the stack group is added to the default resource group.\
        # For more information about resource groups, see [Resource groups](~~94475~~).
        self.resource_group_id = resource_group_id
        # The name of the stack group. The name must be unique within a region.\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or a letter.
        self.stack_group_name = stack_group_name
        # The tags of the stack group.
        self.tags = tags
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Alibaba Cloud Object Storage Service (OSS) bucket. The template body must be 1 to 524,288 bytes in length. Examples: oss://ros/template/demo and oss://ros/template/demo?RegionId=cn-hangzhou. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_url = template_url
        # The version of the template. If you do not specify this parameter, the latest version is used.
        # 
        # > TemplateVersion takes effect only if you specify TemplateId.
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
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities
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
        if m.get('Capabilities') is not None:
            self.capabilities = m.get('Capabilities')
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
        # The key of parameter N. If you do not specify the key and value of a parameter, ROS uses the default name and value that are defined in the template.
        # 
        # Maximum value of N: 200.
        # 
        # > Parameters is optional. If you specify Parameters, you must also specify Parameters.N.ParameterKey.
        self.parameter_key = parameter_key
        # The value of parameter N.
        # 
        # Maximum value of N: 200.
        # 
        # > Parameters is optional. If you specify Parameters, you must also specify Parameters.N.ParameterValue.
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
        # The tag key of the stack group.
        # 
        # > Tags is optional. If you want to specify Tags, you must also specify Tags.N.Key.
        self.key = key
        # The tag value of the stack group.
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
        capabilities: List[str] = None,
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
        # The name of the RAM role that you specify for the administrator account when you create a self-managed stack group. ROS assumes the administrator role to perform operations. If you do not specify this parameter, AliyunROSStackGroupAdministrationRole is used as the default value. ROS uses the administrator role to assume the execution role AliyunROSStackGroupExecutionRole to perform operations on the stacks in the stack group.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, and hyphens (-).
        self.administration_role_name = administration_role_name
        # The information about automatic deployment settings.
        # 
        # > You must specify this parameter if PermissionModel is set to SERVICE_MANAGED.
        self.auto_deployment_shrink = auto_deployment_shrink
        # The options for the stack group. You can specify up to one option.
        self.capabilities = capabilities
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can contain letters, digits, underscores (\_), and hyphens (-) and cannot exceed 64 characters in length.\
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The description of the stack group.\
        # The description must be 1 to 256 characters in length.
        self.description = description
        # The name of the RAM role that you specify for the execution account when you create a self-managed stack group. The administrator role AliyunROSStackGroupAdministrationRole assumes the execution role to perform operations. If you do not specify this parameter, AliyunROSStackGroupExecutionRole is used as the default value. ROS assumes the execution role to perform operations on the stacks in the stack group.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, and hyphens (-).
        self.execution_role_name = execution_role_name
        # The parameters of the stack group.
        self.parameters = parameters
        # The permission model of the stack group.
        # 
        # Valid values:
        # 
        # *   SELF_MANAGED (default): the self-managed permission model. If you create a self-managed stack group, you must create RAM roles within the administrator and execution accounts and establish a trust relationship between the accounts. Then, you can deploy stacks within the execution account.
        # *   SERVICE_MANAGED: the service-managed permission model. If you create a service-managed stack group, ROS creates service-linked roles for the administrator and execution accounts, and the administrator account uses its role to deploy stacks within the execution account.
        # 
        # > If you want to use the service-managed permission model to deploy stacks, your account must be the management account or a delegated administrator account of your resource directory and the trusted access feature is enabled for the account. For more information, see [Manage a delegated administrator account](~~308253~~) and [Enable trusted access](~~298229~~).
        self.permission_model = permission_model
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group. If you do not specify this parameter, the stack group is added to the default resource group.\
        # For more information about resource groups, see [Resource groups](~~94475~~).
        self.resource_group_id = resource_group_id
        # The name of the stack group. The name must be unique within a region.\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or a letter.
        self.stack_group_name = stack_group_name
        # The tags of the stack group.
        self.tags = tags
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Alibaba Cloud Object Storage Service (OSS) bucket. The template body must be 1 to 524,288 bytes in length. Examples: oss://ros/template/demo and oss://ros/template/demo?RegionId=cn-hangzhou. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_url = template_url
        # The version of the template. If you do not specify this parameter, the latest version is used.
        # 
        # > TemplateVersion takes effect only if you specify TemplateId.
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
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities
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
        if m.get('Capabilities') is not None:
            self.capabilities = m.get('Capabilities')
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
        # The ID of the request.
        self.request_id = request_id
        # The ID of the stack group.
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
        # The folder IDs of the resource directory. You can add up to five folder IDs.
        # 
        # You can create stacks within all the member accounts in the specified folders. If you create stacks in the Root folder, the stacks are created within all member accounts in the resource directory.
        # 
        # > To view the folder IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the basic information about a folder](~~111223~~).
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
        # The key of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the name that you specified when you created the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # >-   ParameterOverrides is optional.
        # >-   If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
        self.parameter_key = parameter_key
        # The value of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the value that you specify when you create the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # >-  ParameterOverrides is optional.
        # >-  If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
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
        # The IDs of the execution accounts within which you want to deploy stacks in self-managed mode. You can specify up to 20 execution account IDs.
        # 
        # > You must specify one of the following parameters: `AccountIds` and `DeploymentTargets`.
        self.account_ids = account_ids
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can contain letters, digits, hyphens (-), and underscores (\_), and cannot exceed 64 characters in length.\
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The folders in which ROS deploy stacks in service-managed permission model.
        # 
        # > You must specify one of the following parameters: `AccountIds` and `DeploymentTargets`.
        self.deployment_targets = deployment_targets
        # Specifies whether to disable rollback when the stack fails to be created.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (default)
        self.disable_rollback = disable_rollback
        # The description of the stack creation operation.
        # 
        # The description must be 1 to 256 characters in length.
        self.operation_description = operation_description
        # The preference settings of the stack creation operation.
        # 
        # The following parameters are available:
        # 
        # -  {"FailureToleranceCount": N}
        # 
        #     The number of accounts within which stack operation failures are allowed in each region. If the value of this parameter is exceeded in a region, Resource Orchestration Service (ROS) stops the operation in the region. If ROS stops the operation in one region, ROS stops the operation in other regions.
        # 
        #     Valid values of N: 0 to 20.
        # 
        #     If you do not specify FailureToleranceCount, 0 is used as the default value.
        # 
        # -  {"FailureTolerancePercentage": N}
        # 
        #     The percentage of the number of accounts within which stack operation failures are allowed to the total number of accounts in each region. If the value of this parameter is exceeded, ROS stops the operation in the region.
        # 
        #     Valid values of N: 0 to 100. If the numeric value in the percentage is not an integer, ROS rounds the value down to the nearest integer.
        # 
        #     If you do not specify FailureTolerancePercentage, 0 is used as the default value.
        # 
        # -  {"MaxConcurrentCount": N}
        # 
        #    The maximum number of accounts within which multiple stacks are deployed at the same time in each region.
        # 
        #    Valid values of N: 1 to 20.
        # 
        #    If you do not specify MaxConcurrentCount, 1 is used as the default value.
        # 
        # -  {"MaxConcurrentPercentage": N}
        # 
        #     The percentage of the maximum number of accounts within which multiple stacks are deployed at the same time to the total number of accounts in each region.
        # 
        #     Valid values: 1 to 100. If the numeric value in the percentage is not an integer, ROS rounds the number down to the nearest integer.
        # 
        #     If you do not specify MaxConcurrentPercentage, 1 is used as the default value.
        # 
        # -  {"RegionConcurrencyType": N}\
        #     The mode that you want to use to deploy stacks across regions. Valid values: 
        #    - SEQUENTIAL (default): deploys stacks in each specified region based on the specified sequence of regions. ROS deploys stacks in one region at a time. 
        #    - PARALLEL: deploys stacks in parallel across all specified regions.
        # 
        # Separate multiple parameters with commas (,).
        # 
        # >-  You can specify only one of the following parameters: MaxConcurrentCount and MaxConcurrentPercentage.
        # >-  You can specify only one of the following parameters: FailureToleranceCount and FailureTolerancePercentage.
        self.operation_preferences = operation_preferences
        # The parameters that are used to override specific parameters.
        self.parameter_overrides = parameter_overrides
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The IDs of the regions where you want to create the stacks. You can specify up to 20 region IDs.
        self.region_ids = region_ids
        # The name of the stack group. The name must be unique within a region.\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or a letter.
        self.stack_group_name = stack_group_name
        # The timeout period within which you can create the stack.
        # 
        # *   Default value: 60.
        # *   Unit: minutes.
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
        # The key of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the name that you specified when you created the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # >-   ParameterOverrides is optional.
        # >-   If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
        self.parameter_key = parameter_key
        # The value of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the value that you specify when you create the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # >-  ParameterOverrides is optional.
        # >-  If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
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
        # The IDs of the execution accounts within which you want to deploy stacks in self-managed mode. You can specify up to 20 execution account IDs.
        # 
        # > You must specify one of the following parameters: `AccountIds` and `DeploymentTargets`.
        self.account_ids_shrink = account_ids_shrink
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can contain letters, digits, hyphens (-), and underscores (\_), and cannot exceed 64 characters in length.\
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The folders in which ROS deploy stacks in service-managed permission model.
        # 
        # > You must specify one of the following parameters: `AccountIds` and `DeploymentTargets`.
        self.deployment_targets_shrink = deployment_targets_shrink
        # Specifies whether to disable rollback when the stack fails to be created.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (default)
        self.disable_rollback = disable_rollback
        # The description of the stack creation operation.
        # 
        # The description must be 1 to 256 characters in length.
        self.operation_description = operation_description
        # The preference settings of the stack creation operation.
        # 
        # The following parameters are available:
        # 
        # -  {"FailureToleranceCount": N}
        # 
        #     The number of accounts within which stack operation failures are allowed in each region. If the value of this parameter is exceeded in a region, Resource Orchestration Service (ROS) stops the operation in the region. If ROS stops the operation in one region, ROS stops the operation in other regions.
        # 
        #     Valid values of N: 0 to 20.
        # 
        #     If you do not specify FailureToleranceCount, 0 is used as the default value.
        # 
        # -  {"FailureTolerancePercentage": N}
        # 
        #     The percentage of the number of accounts within which stack operation failures are allowed to the total number of accounts in each region. If the value of this parameter is exceeded, ROS stops the operation in the region.
        # 
        #     Valid values of N: 0 to 100. If the numeric value in the percentage is not an integer, ROS rounds the value down to the nearest integer.
        # 
        #     If you do not specify FailureTolerancePercentage, 0 is used as the default value.
        # 
        # -  {"MaxConcurrentCount": N}
        # 
        #    The maximum number of accounts within which multiple stacks are deployed at the same time in each region.
        # 
        #    Valid values of N: 1 to 20.
        # 
        #    If you do not specify MaxConcurrentCount, 1 is used as the default value.
        # 
        # -  {"MaxConcurrentPercentage": N}
        # 
        #     The percentage of the maximum number of accounts within which multiple stacks are deployed at the same time to the total number of accounts in each region.
        # 
        #     Valid values: 1 to 100. If the numeric value in the percentage is not an integer, ROS rounds the number down to the nearest integer.
        # 
        #     If you do not specify MaxConcurrentPercentage, 1 is used as the default value.
        # 
        # -  {"RegionConcurrencyType": N}\
        #     The mode that you want to use to deploy stacks across regions. Valid values: 
        #    - SEQUENTIAL (default): deploys stacks in each specified region based on the specified sequence of regions. ROS deploys stacks in one region at a time. 
        #    - PARALLEL: deploys stacks in parallel across all specified regions.
        # 
        # Separate multiple parameters with commas (,).
        # 
        # >-  You can specify only one of the following parameters: MaxConcurrentCount and MaxConcurrentPercentage.
        # >-  You can specify only one of the following parameters: FailureToleranceCount and FailureTolerancePercentage.
        self.operation_preferences_shrink = operation_preferences_shrink
        # The parameters that are used to override specific parameters.
        self.parameter_overrides = parameter_overrides
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The IDs of the regions where you want to create the stacks. You can specify up to 20 region IDs.
        self.region_ids_shrink = region_ids_shrink
        # The name of the stack group. The name must be unique within a region.\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or a letter.
        self.stack_group_name = stack_group_name
        # The timeout period within which you can create the stack.
        # 
        # *   Default value: 60.
        # *   Unit: minutes.
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
        # The ID of the operation.
        self.operation_id = operation_id
        # The ID of the request.
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
        # The tag key of the template.
        # 
        # > Tags is optional. If you need to specify Tags, you must also specify Key.
        self.key = key
        # The tag value of the template.
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
        # The description of the template. The description can be up to 256 characters in length.
        self.description = description
        # The ID of the resource group.\
        # For more information about resource groups, see [Resource groups](~~94475~~).
        self.resource_group_id = resource_group_id
        # The tags of the template.
        self.tags = tags
        self.template_body = template_body
        # The name of the template.\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or a letter.
        self.template_name = template_name
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Alibaba Cloud Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The template body must be 1 to 1,024 bytes in length. If you do not specify the region of the OSS bucket, the value of RegionId is used.
        # 
        # > You must specify TemplateBody or TemplateURL.
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
        # The ID of the request.
        self.request_id = request_id
        # The ID of the template.
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
        # The key of the parameter.
        # 
        # For information about the valid values of ParameterKey, see the **Additional information about request parameters** section of this topic.
        # > - PreferenceParameters is optional. If you want to specify PreferenceParameters, you must specify ParameterKey and ParameterValue.
        # > -  If you set TemplateScratchType to ResourceImport, you must set ParameterKey to DeletionPolicy.
        self.parameter_key = parameter_key
        # The value of the parameter. The value of ParameterValue varies based on the value of ParameterKey.
        # 
        # For information about the valid values of ParameterValue, see the **Additional information about request parameters** section of this topic.
        # 
        # > PreferenceParameters is optional. If you want to specify PreferenceParameters, you must specify ParameterKey and ParameterValue.
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
        # The ID of the source resource group.
        self.resource_group_id = resource_group_id
        # The resource types.
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
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        pass

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        # The source tags that consist of key-value pairs. If you want to specify only the tag key, you must leave the tag value empty. Example: `{"TagKey": ""}`.
        # 
        # You can add up to 10 source tags.
        self.resource_tags = resource_tags
        # The resource types.
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
        # The tag key of the scenario.
        # 
        # > Tags is optional. If you want to specify Tags, you must specify Key.
        self.key = key
        # The tag value of the scenario.
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
        resource_group_id: str = None,
        source_resource_group: CreateTemplateScratchRequestSourceResourceGroup = None,
        source_resources: List[CreateTemplateScratchRequestSourceResources] = None,
        source_tag: CreateTemplateScratchRequestSourceTag = None,
        tags: List[CreateTemplateScratchRequestTags] = None,
        template_scratch_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The description of the scenario.
        self.description = description
        # The execution mode. Valid values:
        # 
        # *   Async (default)
        # *   Sync
        # 
        # > If you have a wide scope of resources, Sync takes longer. If you set ExecutionMode to Sync, we recommend that you specify ClientToken to prevent the execution timeout.
        self.execution_mode = execution_mode
        # The policy based on which the logical ID is generated. Valid values:
        # 
        # *   LongTypePrefixAndIndexSuffix (default): long-type prefix + index-type suffix
        # *   LongTypePrefixAndHashSuffix: long-type prefix + hash-type suffix
        # *   ShortTypePrefixAndHashSuffix: short-type prefix + hash-type suffix
        self.logical_id_strategy = logical_id_strategy
        # The preference parameters of the scenario.
        self.preference_parameters = preference_parameters
        # The region ID of the scenario.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The source resource group.
        self.source_resource_group = source_resource_group
        # The source resources.
        self.source_resources = source_resources
        # The source tag.
        self.source_tag = source_tag
        # The tags of the scenario.
        self.tags = tags
        # The type of the scenario. Valid values:
        # 
        # *   ResourceImport: resource management
        # *   ArchitectureReplication: resource replication
        # *   ResourceMigration: resource migration
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        # The tag key of the scenario.
        # 
        # > Tags is optional. If you want to specify Tags, you must specify Key.
        self.key = key
        # The tag value of the scenario.
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
        resource_group_id: str = None,
        source_resource_group_shrink: str = None,
        source_resources_shrink: str = None,
        source_tag_shrink: str = None,
        tags: List[CreateTemplateScratchShrinkRequestTags] = None,
        template_scratch_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The description of the scenario.
        self.description = description
        # The execution mode. Valid values:
        # 
        # *   Async (default)
        # *   Sync
        # 
        # > If you have a wide scope of resources, Sync takes longer. If you set ExecutionMode to Sync, we recommend that you specify ClientToken to prevent the execution timeout.
        self.execution_mode = execution_mode
        # The policy based on which the logical ID is generated. Valid values:
        # 
        # *   LongTypePrefixAndIndexSuffix (default): long-type prefix + index-type suffix
        # *   LongTypePrefixAndHashSuffix: long-type prefix + hash-type suffix
        # *   ShortTypePrefixAndHashSuffix: short-type prefix + hash-type suffix
        self.logical_id_strategy = logical_id_strategy
        # The preference parameters of the scenario.
        self.preference_parameters_shrink = preference_parameters_shrink
        # The region ID of the scenario.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The source resource group.
        self.source_resource_group_shrink = source_resource_group_shrink
        # The source resources.
        self.source_resources_shrink = source_resources_shrink
        # The source tag.
        self.source_tag_shrink = source_tag_shrink
        # The tags of the scenario.
        self.tags = tags
        # The type of the scenario. Valid values:
        # 
        # *   ResourceImport: resource management
        # *   ArchitectureReplication: resource replication
        # *   ResourceMigration: resource migration
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        # The ID of the request.
        self.request_id = request_id
        # The ID of the scenario.
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
        # The ID of the change set.
        self.change_set_id = change_set_id
        # The region ID of the change set. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
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
        # The ID of the request.
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


class DeleteDiagnosticRequest(TeaModel):
    def __init__(
        self,
        report_id: str = None,
    ):
        # The report ID. You can troubleshoot issues based on the report.
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        return self


class DeleteDiagnosticResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The error code returned.
        self.code = code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDiagnosticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDiagnosticResponseBody = None,
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
            temp_model = DeleteDiagnosticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStackRequest(TeaModel):
    def __init__(
        self,
        delete_options: List[str] = None,
        ram_role_name: str = None,
        region_id: str = None,
        retain_all_resources: bool = None,
        retain_resources: List[str] = None,
        stack_id: str = None,
    ):
        # The options for deleting the stack.
        self.delete_options = delete_options
        # The name of the RAM role. Resource Orchestration Service (ROS) assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.\
        # ROS assumes the role to perform operations on the stack. If you have permissions to perform operations on the stack but do not have permissions to use the RAM role, ROS still assumes the RAM role. You must make sure that the least privileges are granted to the RAM role.\
        # If you leave this parameter empty when you call the DeleteStack operation, ROS cannot assume the existing RAM role that is associated with the stack. If you want ROS to assume a RAM role, you must specify this parameter. If no RAM roles are available, ROS uses a temporary credential that is generated from the credentials of your account.\
        # The name of the RAM role can be up to 64 bytes in length.
        self.ram_role_name = ram_role_name
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # Specifies whether to retain all resources in the stack.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (default)
        self.retain_all_resources = retain_all_resources
        # The resources that you want to retain.
        self.retain_resources = retain_resources
        # The ID of the stack.
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_options is not None:
            result['DeleteOptions'] = self.delete_options
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
        if m.get('DeleteOptions') is not None:
            self.delete_options = m.get('DeleteOptions')
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
        # The ID of the request.
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
        # The ID of the region to which the stack group belongs. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The name of the stack group. The name must be unique in a region.
        # 
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). The name must start with a digit or a letter.
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
        # The ID of the request.
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
        account_ids: List[str] = None,
        rd_folder_ids: List[str] = None,
    ):
        # The IDs of the execution accounts within which you want to deploy stacks in self-managed mode. You can specify up to 20 execution account IDs.
        # 
        # > To view the folder IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the basic information about a folder](~~111223~~).
        self.account_ids = account_ids
        # The IDs of the folders in the resource directory. You can add up to five folder IDs.
        # 
        # You can create stacks within all the member accounts in the specified folders. If you create stacks in the Root folder, the stacks are created within all member accounts in the resource directory.
        # 
        # > To view the folder IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the basic information about a folder](~~111223~~).
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
        # The IDs of the execution accounts within which you want to deploy stacks in self-managed mode. You can specify up to 20 execution account IDs.
        self.account_ids = account_ids
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can contain letters, digits, hyphens (-), and underscores (\_), and cannot exceed 64 characters in length.\
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The folders in which you want to deploy stacks in service-managed mode.
        self.deployment_targets = deployment_targets
        # The description of the delete operation.
        # 
        # The description must be 1 to 256 characters in length.
        self.operation_description = operation_description
        # The preference settings of the delete operation.
        # 
        # The following parameters are available:
        # 
        # -  {"FailureToleranceCount": N}
        # 
        #     The number of accounts within which stack operation failures are allowed in each region. If the value of this parameter is exceeded in a region, ROS stops the operation in the region. If ROS stops the operation in one region, ROS stops the operation in other regions.
        # 
        #     Valid values of N: 0 to 20.
        # 
        #     If you do not specify FailureToleranceCount, 0 is used as the default value.
        # 
        # -  {"FailureTolerancePercentage": N}
        # 
        #     The percentage of the number of accounts within which stack operation failures are allowed to the total number of accounts in each region. If the value of this parameter is exceeded, ROS stops the operation in the region.
        # 
        #     Valid values of N: 0 to 100. If the numeric value in the percentage is not an integer, ROS rounds the value down to the nearest integer.
        # 
        #     If you do not specify FailureTolerancePercentage, 0 is used as the default value.
        # 
        # -  {"MaxConcurrentCount": N}
        # 
        #     The maximum number of accounts within which multiple stacks are deployed at the same time in each region.
        # 
        #     Valid values of N: 1 to 20.
        # 
        #     If you do not specify MaxConcurrentCount, 1 is used as the default value.
        # 
        # -  {"MaxConcurrentPercentage": N}
        # 
        #     The percentage of the maximum number of accounts within which stacks are deployed at the same time to the total number of accounts in each region.
        # 
        #     Valid values of N: 1 to 100. If the numeric value in the percentage is not an integer, ROS rounds the number down to the nearest integer.
        # 
        #     If you do not specify MaxConcurrentPercentage, 1 is used as the default value.
        # 
        # -   {"RegionConcurrencyType": N}
        # 
        #     The mode that you want to use to deploy stacks across regions. Valid values:
        #     - SEQUENTIAL (default): deploys stacks in the specified regions one by one in sequence. This way, ROS deploys stacks in only one region at a time. 
        # 
        #      - PARALLEL: deploys stacks in all the specified regions in parallel. 
        # 
        # Separate multiple parameters with commas (,).
        # 
        # > - You can specify only one of the following parameters: MaxConcurrentCount and MaxConcurrentPercentage.
        # > - You can specify only one of the following parameters: FailureToleranceCount and FailureTolerancePercentage.
        self.operation_preferences = operation_preferences
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The IDs of the regions where you want to delete the stacks. You can specify up to 20 region IDs.
        self.region_ids = region_ids
        # Specifies whether to delete the stacks.
        # 
        # Valid values:
        # 
        # *   true: retains the stacks.
        # *   false: deletes the stacks.
        self.retain_stacks = retain_stacks
        # The name of the stack group. The name must be unique within a region.\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or a letter.
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
        # The IDs of the execution accounts within which you want to deploy stacks in self-managed mode. You can specify up to 20 execution account IDs.
        self.account_ids_shrink = account_ids_shrink
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can contain letters, digits, hyphens (-), and underscores (\_), and cannot exceed 64 characters in length.\
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The folders in which you want to deploy stacks in service-managed mode.
        self.deployment_targets_shrink = deployment_targets_shrink
        # The description of the delete operation.
        # 
        # The description must be 1 to 256 characters in length.
        self.operation_description = operation_description
        # The preference settings of the delete operation.
        # 
        # The following parameters are available:
        # 
        # -  {"FailureToleranceCount": N}
        # 
        #     The number of accounts within which stack operation failures are allowed in each region. If the value of this parameter is exceeded in a region, ROS stops the operation in the region. If ROS stops the operation in one region, ROS stops the operation in other regions.
        # 
        #     Valid values of N: 0 to 20.
        # 
        #     If you do not specify FailureToleranceCount, 0 is used as the default value.
        # 
        # -  {"FailureTolerancePercentage": N}
        # 
        #     The percentage of the number of accounts within which stack operation failures are allowed to the total number of accounts in each region. If the value of this parameter is exceeded, ROS stops the operation in the region.
        # 
        #     Valid values of N: 0 to 100. If the numeric value in the percentage is not an integer, ROS rounds the value down to the nearest integer.
        # 
        #     If you do not specify FailureTolerancePercentage, 0 is used as the default value.
        # 
        # -  {"MaxConcurrentCount": N}
        # 
        #     The maximum number of accounts within which multiple stacks are deployed at the same time in each region.
        # 
        #     Valid values of N: 1 to 20.
        # 
        #     If you do not specify MaxConcurrentCount, 1 is used as the default value.
        # 
        # -  {"MaxConcurrentPercentage": N}
        # 
        #     The percentage of the maximum number of accounts within which stacks are deployed at the same time to the total number of accounts in each region.
        # 
        #     Valid values of N: 1 to 100. If the numeric value in the percentage is not an integer, ROS rounds the number down to the nearest integer.
        # 
        #     If you do not specify MaxConcurrentPercentage, 1 is used as the default value.
        # 
        # -   {"RegionConcurrencyType": N}
        # 
        #     The mode that you want to use to deploy stacks across regions. Valid values:
        #     - SEQUENTIAL (default): deploys stacks in the specified regions one by one in sequence. This way, ROS deploys stacks in only one region at a time. 
        # 
        #      - PARALLEL: deploys stacks in all the specified regions in parallel. 
        # 
        # Separate multiple parameters with commas (,).
        # 
        # > - You can specify only one of the following parameters: MaxConcurrentCount and MaxConcurrentPercentage.
        # > - You can specify only one of the following parameters: FailureToleranceCount and FailureTolerancePercentage.
        self.operation_preferences_shrink = operation_preferences_shrink
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The IDs of the regions where you want to delete the stacks. You can specify up to 20 region IDs.
        self.region_ids_shrink = region_ids_shrink
        # Specifies whether to delete the stacks.
        # 
        # Valid values:
        # 
        # *   true: retains the stacks.
        # *   false: deletes the stacks.
        self.retain_stacks = retain_stacks
        # The name of the stack group. The name must be unique within a region.\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or a letter.
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
        # The ID of the operation.
        self.operation_id = operation_id
        # The ID of the request.
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
        # The ID of the template. This parameter applies to only private templates.
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
        # The ID of the request.
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
        # The region ID of the scenario.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the scenario.
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
        # The ID of the request.
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


class DeregisterResourceTypeRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        version_id: str = None,
    ):
        # The resource type.
        self.resource_type = resource_type
        # The version ID. If you want to delete a version of the resource type, you must specify this parameter.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DeregisterResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeregisterResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeregisterResourceTypeResponseBody = None,
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
            temp_model = DeregisterResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # The language in which you want to display the results. Valid values:
        # 
        # *   zh-CN (default): Chinese
        # *   en-US: English
        # *   ja: Japanese
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
        # The name of the region.
        self.local_name = local_name
        # The endpoint of the region.
        self.region_endpoint = region_endpoint
        # The region ID.
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
        # The regions.
        self.regions = regions
        # The request ID.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests.
        # 
        # The value can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The logical ID of resource.
        self.logical_resource_id = logical_resource_id
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the stack.
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
        # The ID of the drift detection.
        self.drift_detection_id = drift_detection_id
        # The ID of the request.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests.
        # 
        # The value can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The operation settings, in JSON format. The following fields are supported:
        # 
        # *   FailureToleranceCount
        # 
        # The maximum number of stack group operation failures that can occur. In a stack group operation, if the total number of failures does not exceed the FailureToleranceCount value, the operation succeeds. Otherwise, the operation fails.
        # 
        # If FailureToleranceCount is not specified, the default value 0 is used. You can specify one of FailureToleranceCount or FailureTolerancePercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 0 to 20.
        # 
        # *   FailureTolerancePercentage
        # 
        # The percentage of stack group operation failures that can occur. In a stack group operation, if the percentage of failures does not exceed the FailureTolerancePercentage value, the operation succeeds. Otherwise, the operation fails.
        # 
        # You can specify one of FailureToleranceCount or FailureTolerancePercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 0 to 100.
        # 
        # *   MaxConcurrentCount
        # 
        # The maximum number of target accounts in which a drift detection operation can be performed at a time.
        # 
        # You can specify one of MaxConcurrentCount or MaxConcurrentPercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 1 to 20.
        # 
        # *   MaxConcurrentPercentage
        # 
        # The maximum percentage of target accounts in which a drift detection operation can be performed at a time.
        # 
        # You can specify one of MaxConcurrentCount or MaxConcurrentPercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 1 to 100.
        self.operation_preferences = operation_preferences
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035#doc-api-ROS-DescribeRegions~~ "Queries the DescribeRegions list of a region.") operation to query the most recent region list.
        self.region_id = region_id
        # The name of the stack group. The name must be unique in a region.
        # 
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or letter.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests.
        # 
        # The value can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The operation settings, in JSON format. The following fields are supported:
        # 
        # *   FailureToleranceCount
        # 
        # The maximum number of stack group operation failures that can occur. In a stack group operation, if the total number of failures does not exceed the FailureToleranceCount value, the operation succeeds. Otherwise, the operation fails.
        # 
        # If FailureToleranceCount is not specified, the default value 0 is used. You can specify one of FailureToleranceCount or FailureTolerancePercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 0 to 20.
        # 
        # *   FailureTolerancePercentage
        # 
        # The percentage of stack group operation failures that can occur. In a stack group operation, if the percentage of failures does not exceed the FailureTolerancePercentage value, the operation succeeds. Otherwise, the operation fails.
        # 
        # You can specify one of FailureToleranceCount or FailureTolerancePercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 0 to 100.
        # 
        # *   MaxConcurrentCount
        # 
        # The maximum number of target accounts in which a drift detection operation can be performed at a time.
        # 
        # You can specify one of MaxConcurrentCount or MaxConcurrentPercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 1 to 20.
        # 
        # *   MaxConcurrentPercentage
        # 
        # The maximum percentage of target accounts in which a drift detection operation can be performed at a time.
        # 
        # You can specify one of MaxConcurrentCount or MaxConcurrentPercentage parameters, but you cannot specify both of them.
        # 
        # Valid values: 1 to 100.
        self.operation_preferences_shrink = operation_preferences_shrink
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035#doc-api-ROS-DescribeRegions~~ "Queries the DescribeRegions list of a region.") operation to query the most recent region list.
        self.region_id = region_id
        # The name of the stack group. The name must be unique in a region.
        # 
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or letter.
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
        # The ID of the operation.
        self.operation_id = operation_id
        # The ID of the request.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests.
        # 
        # The value can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The name of the resource.
        self.logical_resource_id = logical_resource_id
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the stack.
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
        # The actual value of the resource property.
        self.actual_value = actual_value
        # The drift type of the resource property. Valid values:
        # 
        # *   ADD: The property value has been added to a resource property whose data type was Array or List.
        # *   REMOVE: The property has been deleted from the current resource configuration.
        # *   NOT_EQUAL: The current property value differs from the expected value defined in the stack template.
        self.difference_type = difference_type
        # The expected value of the resource property that is defined in the template.
        self.expected_value = expected_value
        # The path of the resource property.
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
        # The actual JSON-formatted resource properties.
        self.actual_properties = actual_properties
        # The time when the resource drift detection was initiated.
        self.drift_detection_time = drift_detection_time
        # The JSON-formatted resource properties that are defined in the template.
        self.expected_properties = expected_properties
        # The logical ID of the resource that is defined in the template.
        self.logical_resource_id = logical_resource_id
        # The physical ID of the resource.
        self.physical_resource_id = physical_resource_id
        # The property drifts of the resource.
        self.property_differences = property_differences
        # The ID of the request.
        self.request_id = request_id
        # The drift status of the resource. Valid values:
        # 
        # *   DELETED: The actual configuration of the resource differs from its expected template configuration because the resource is deleted.
        # *   MODIFIED: The actual configuration of the resource differs from its expected template configuration.
        # *   NOT_CHECKED: Resource Orchestration Service (ROS) has not checked whether the actual configuration of the resource differs from its expected template configuration.
        # *   IN_SYNC: The actual configuration of the resource matches its expected template configuration.
        self.resource_drift_status = resource_drift_status
        # The type of the resource.
        self.resource_type = resource_type
        # The ID of the stack.
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
        # The ID of the change set.
        self.change_set_id = change_set_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests.
        # 
        # The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The region ID of the change set. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
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
        # The ID of the request.
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
        template_type: str = None,
    ):
        # The region ID of the new node.
        self.provision_region_id = provision_region_id
        # The region ID of the scenario.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the scenario.
        # 
        # For more information about how to query the IDs of scenarios, see [ListTemplateScratches](~~363050~~).
        self.template_scratch_id = template_scratch_id
        # The type of the template that Resource Orchestration Service (ROS) generates. ROS can generate templates of the ROS and Terraform types. Default value: ROS.
        self.template_type = template_type

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
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvisionRegionId') is not None:
            self.provision_region_id = m.get('ProvisionRegionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GenerateTemplateByScratchResponseBodyResourcesToImport(TeaModel):
    def __init__(
        self,
        logical_resource_id: str = None,
        resource_identifier: Dict[str, Any] = None,
        resource_type: str = None,
    ):
        # The logical ID of the resource.
        self.logical_resource_id = logical_resource_id
        # The key-value mapping between strings. The value is a JSON string that identifies the resource that you want to import into a stack.\
        # A key is an identifier for a resource, and a value is an assignment of data to the key. For example, VpcId is a key that indicates the ID of a virtual private cloud (VPC), and `vpc-bp1m6fww66xbntjyc****"` is a value that is assigned to VpcId.
        self.resource_identifier = resource_identifier
        # The type of the resource.
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
        # The ID of the request.
        self.request_id = request_id
        # The resources that you want to import into a stack in the scenario.
        # 
        # > This parameter is returned only if the scenario is of the Resource Management type.
        self.resources_to_import = resources_to_import
        # The template content of the scenario.
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
        # The type of operation N for which you want to generate the policy information.
        # 
        # Valid values:
        # 
        # *   CreateStack: creates a stack by calling the CreateStack operation.
        # *   UpdateStack: updates a stack by calling the UpdateStack operation.
        # *   DeleteStack: deletes a stack by calling the DeleteStack operation.
        # *   DetectStackDrift: detects drifts on a stack by calling the DelectStackDrift operation.
        # *   ListStackOperationRisks: lists the risks of a deletion operation on a stack by setting the OperationType parameter to DeleteStack in the ListStackOperationRisks operation.
        # *   GetTemplateEstimateCost: queries the estimated prices of resources that you want to use in the template by calling the GetTemplateEstimateCost operation.
        # *   GetTemplateParameterConstraints: queries the values of parameters in the template by calling the GetTemplateParameterConstraints operation.
        # *   ImportResourcesToStack: imports resources to a stack by setting the ChangeSetType parameter to IMPORT in the CreateChangeSet operation.
        # *   SignalResource: sends a signal to a stack.
        # 
        # >  The default value is the combination of all valid values.
        self.operation_types = operation_types
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length.
        # 
        # If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared templates and private templates.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length.
        # 
        # >  If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        # 
        # The URL can be up to 1,024 bytes in length.
        self.template_url = template_url
        # The version of the template. This parameter takes effect only when the TemplateId parameter is specified.
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
        condition: Dict[str, Any] = None,
        effect: str = None,
        resource: str = None,
    ):
        # The operations that are performed on the specified resource.
        self.action = action
        # The condition that is required for the policy to take effect.
        self.condition = condition
        # The effect of the statement. Valid values:
        # 
        # *   Allow
        # *   Deny
        self.effect = effect
        # The objects that the statement covers. An asterisk (\*) indicates all resources.
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
        if self.condition is not None:
            result['Condition'] = self.condition
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.resource is not None:
            result['Resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
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
        # The statements that are contained in the policy.
        self.statement = statement
        # The version number.
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
        # The information about the policy.
        self.policy = policy
        # The ID of the request.
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
        # The ID of the change set.
        self.change_set_id = change_set_id
        # The region ID of the change set. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # Specifies whether to obtain the template. Valid values:
        # 
        # *   true
        # *   false (default)
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
        # The name of the Terraform command that is run. Valid values:
        # 
        # *   apply
        # *   plan
        # *   destroy
        # *   version
        # 
        # For more information about Terraform commands, see [Command](https://www.terraform.io/cli/commands).
        self.command = command
        # The content of the output stream that is returned after the command is run.
        self.content = content
        # The output stream. Valid values:
        # 
        # *   stdout: standard output stream
        # *   stderr: standard error stream
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
        # The Terraform logs. This parameter is returned only for change sets of Terraform stacks.
        # 
        # > This parameter is not returned for change sets that are in the Creating state. This parameter indicates the logs of the change set creation operation for Terraform stacks.
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
        # The key of the parameter.
        self.parameter_key = parameter_key
        # The value of the parameter.
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
        # The ID of the change set.
        self.change_set_id = change_set_id
        # The name of the change set.
        self.change_set_name = change_set_name
        # The type of the change set.
        self.change_set_type = change_set_type
        # The changes of the change set.
        self.changes = changes
        # The time when the change set was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the change set.
        self.description = description
        # Indicates whether rollback was performed when the stack failed to be created or updated.
        self.disable_rollback = disable_rollback
        # The execution status of the change set.
        self.execution_status = execution_status
        # The output logs of the change set.
        self.log = log
        # The parameters of the stack.
        self.parameters = parameters
        # The region ID of the change set.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the stack with which the change set is associated.
        self.stack_id = stack_id
        # The name of the stack with which the change set is associated.
        self.stack_name = stack_name
        # The status of the change set.
        self.status = status
        # The reason why the change set is in its current state.
        self.status_reason = status_reason
        # The template body of the change set.
        # 
        # > This parameter takes effect only if you set ShowTemplate to true.
        self.template_body = template_body
        # The timeout period that is specified for the stack creation or update operation.
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


class GetDiagnosticRequest(TeaModel):
    def __init__(
        self,
        report_id: str = None,
    ):
        # The ID of the diagnostic report.
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        return self


class GetDiagnosticResponseBodyDiagnosticResult(TeaModel):
    def __init__(
        self,
        failed_resources: Dict[str, Any] = None,
        ros_action_messages: Dict[str, Any] = None,
        stack_messages: Dict[str, Any] = None,
    ):
        # The resources that failed to be diagnosed.
        self.failed_resources = failed_resources
        # The information about Resource Orchestration Service (ROS) calling.
        self.ros_action_messages = ros_action_messages
        # The stack information.
        self.stack_messages = stack_messages

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_resources is not None:
            result['FailedResources'] = self.failed_resources
        if self.ros_action_messages is not None:
            result['RosActionMessages'] = self.ros_action_messages
        if self.stack_messages is not None:
            result['StackMessages'] = self.stack_messages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedResources') is not None:
            self.failed_resources = m.get('FailedResources')
        if m.get('RosActionMessages') is not None:
            self.ros_action_messages = m.get('RosActionMessages')
        if m.get('StackMessages') is not None:
            self.stack_messages = m.get('StackMessages')
        return self


class GetDiagnosticResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        diagnostic_key: str = None,
        diagnostic_product: str = None,
        diagnostic_result: GetDiagnosticResponseBodyDiagnosticResult = None,
        diagnostic_time: str = None,
        http_code: str = None,
        http_status_code: int = None,
        message: str = None,
        recommends: Dict[str, Any] = None,
        report_id: str = None,
        request_id: str = None,
        status: str = None,
        status_reason: str = None,
        success: str = None,
    ):
        # The error code returned.
        self.code = code
        # The keyword in the diagnosis.
        self.diagnostic_key = diagnostic_key
        # The name of the diagnostic item.
        self.diagnostic_product = diagnostic_product
        # The diagnosis result.
        self.diagnostic_result = diagnostic_result
        # The time when the diagnosis was performed.
        self.diagnostic_time = diagnostic_time
        # The HTTP status code
        self.http_code = http_code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The suggestion for the diagnosis.
        self.recommends = recommends
        # The ID of the diagnostic report.
        self.report_id = report_id
        # The request ID.
        self.request_id = request_id
        # The diagnosis status. Valid values:
        # 
        # *   Running: The diagnosis is in progress.
        # *   Complete: The diagnosis is complete.
        # *   Failed: The diagnosis failed.
        self.status = status
        # The reason for the diagnosis status.
        self.status_reason = status_reason
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.diagnostic_result:
            self.diagnostic_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.diagnostic_key is not None:
            result['DiagnosticKey'] = self.diagnostic_key
        if self.diagnostic_product is not None:
            result['DiagnosticProduct'] = self.diagnostic_product
        if self.diagnostic_result is not None:
            result['DiagnosticResult'] = self.diagnostic_result.to_map()
        if self.diagnostic_time is not None:
            result['DiagnosticTime'] = self.diagnostic_time
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.recommends is not None:
            result['Recommends'] = self.recommends
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DiagnosticKey') is not None:
            self.diagnostic_key = m.get('DiagnosticKey')
        if m.get('DiagnosticProduct') is not None:
            self.diagnostic_product = m.get('DiagnosticProduct')
        if m.get('DiagnosticResult') is not None:
            temp_model = GetDiagnosticResponseBodyDiagnosticResult()
            self.diagnostic_result = temp_model.from_map(m['DiagnosticResult'])
        if m.get('DiagnosticTime') is not None:
            self.diagnostic_time = m.get('DiagnosticTime')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Recommends') is not None:
            self.recommends = m.get('Recommends')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDiagnosticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDiagnosticResponseBody = None,
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
            temp_model = GetDiagnosticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFeatureDetailsRequest(TeaModel):
    def __init__(
        self,
        feature: str = None,
        region_id: str = None,
    ):
        # The one or more features that you want to query. Valid values:
        # 
        # *   Terraform: the Terraform hosting feature.
        # *   ResourceCleaner: the resource cleaner feature. You can use ALIYUN::ROS::ResourceCleaner to create a resource cleaner.
        # *   TemplateScratch: the scenario feature.
        # *   All: all features that are supported by ROS.
        self.feature = feature
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
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


class GetFeatureDetailsResponseBodyDriftDetection(TeaModel):
    def __init__(
        self,
        supported_resource_types: List[str] = None,
    ):
        # The resource types that are supported by the drift detection feature.
        self.supported_resource_types = supported_resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.supported_resource_types is not None:
            result['SupportedResourceTypes'] = self.supported_resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedResourceTypes') is not None:
            self.supported_resource_types = m.get('SupportedResourceTypes')
        return self


class GetFeatureDetailsResponseBodyResourceCleanerSupportedResourceTypes(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        side_effects: List[str] = None,
        supported_filters: List[str] = None,
    ):
        # The resource type that supports the resource cleaner feature.
        self.resource_type = resource_type
        # The names of the side effects that may be caused by the cleanup operation performed on the resources of the specified type.
        self.side_effects = side_effects
        # The names of the filters that are supported by the resource type.
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
        # The resource types that can be cleaned up.
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


class GetFeatureDetailsResponseBodyResourceImportSupportedResourceTypes(TeaModel):
    def __init__(
        self,
        resource_identifiers: List[str] = None,
        resource_type: str = None,
    ):
        # The resource identifiers.
        self.resource_identifiers = resource_identifiers
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_identifiers is not None:
            result['ResourceIdentifiers'] = self.resource_identifiers
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceIdentifiers') is not None:
            self.resource_identifiers = m.get('ResourceIdentifiers')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetFeatureDetailsResponseBodyResourceImport(TeaModel):
    def __init__(
        self,
        supported_resource_types: List[GetFeatureDetailsResponseBodyResourceImportSupportedResourceTypes] = None,
    ):
        # The resource types that are supported by the resource import feature.
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
                temp_model = GetFeatureDetailsResponseBodyResourceImportSupportedResourceTypes()
                self.supported_resource_types.append(temp_model.from_map(k))
        return self


class GetFeatureDetailsResponseBodyTemplateParameterConstraintsSupportedResourceTypes(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        # The names of properties that are supported by the resource type.
        self.properties = properties
        # The resource type.
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
        # The resource types that support the template parameter constraint feature.
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
        supported_template_scratch_types: List[str] = None,
    ):
        # The resource type.
        self.resource_type = resource_type
        # Indicates whether the resource scope can be specified by source resource group. Valid values:
        # 
        # *   true
        # *   false
        self.source_resource_group_supported = source_resource_group_supported
        # Indicates whether the resource scope can be specified by source resource. Valid values:
        # 
        # *   true
        # *   false
        self.source_resources_supported = source_resources_supported
        # Indicates whether the resource scope can be specified by source tag, resource group, or resource. Valid values:
        # 
        # *   true
        # *   false
        self.source_supported = source_supported
        # Indicates whether the resource scope can be specified by source tag. Valid values:
        # 
        # *   true
        # *   false
        self.source_tag_supported = source_tag_supported
        # The scenario types that are supported.
        self.supported_template_scratch_types = supported_template_scratch_types

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
        if self.supported_template_scratch_types is not None:
            result['SupportedTemplateScratchTypes'] = self.supported_template_scratch_types
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
        if m.get('SupportedTemplateScratchTypes') is not None:
            self.supported_template_scratch_types = m.get('SupportedTemplateScratchTypes')
        return self


class GetFeatureDetailsResponseBodyTemplateScratch(TeaModel):
    def __init__(
        self,
        supported_resource_types: List[GetFeatureDetailsResponseBodyTemplateScratchSupportedResourceTypes] = None,
    ):
        # The resource types that are supported by the scenario feature.
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
        # The resource types that support the risk check performed to detect risks caused by a stack deletion operation.
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
        # The resource types that support the custom tag feature.
        self.custom_tag = custom_tag
        # The resource types that support the price inquiry feature.
        self.estimate_cost = estimate_cost
        # The resource types that support the resource group feature.
        self.resource_group = resource_group
        # The resource type that support the risk check feature.
        self.stack_operation_risk = stack_operation_risk
        # The resource types that support the system tag `acs:ros:stackId`.
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
        # The name of the provider.
        self.provider_name = provider_name
        # The provider versions.
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
        # The names and versions of the providers that correspond to the Terraform versions.
        self.provider_versions = provider_versions
        # The Terraform version.
        self.terraform_version = terraform_version
        # The Terraform version that is supported by ROS. The parameter value is the same as the value of the Transform parameter in a Terraform template.
        self.transform = transform
        # The Terraform versions that can be updated in ROS.
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
        # The resource types that support the scenario feature.
        self.supported_resource_types = supported_resource_types
        # The Terraform versions.
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
        drift_detection: GetFeatureDetailsResponseBodyDriftDetection = None,
        request_id: str = None,
        resource_cleaner: GetFeatureDetailsResponseBodyResourceCleaner = None,
        resource_import: GetFeatureDetailsResponseBodyResourceImport = None,
        template_parameter_constraints: GetFeatureDetailsResponseBodyTemplateParameterConstraints = None,
        template_scratch: GetFeatureDetailsResponseBodyTemplateScratch = None,
        terraform: GetFeatureDetailsResponseBodyTerraform = None,
    ):
        # Details of the drift detection feature.
        self.drift_detection = drift_detection
        # The ID of the request.
        self.request_id = request_id
        # Details of the resource cleaner feature.
        self.resource_cleaner = resource_cleaner
        # Details of the resource import feature.
        self.resource_import = resource_import
        # Details of the template parameter constraint feature.
        self.template_parameter_constraints = template_parameter_constraints
        # Details of the scenario feature.
        self.template_scratch = template_scratch
        # Details of the Terraform hosting feature.
        self.terraform = terraform

    def validate(self):
        if self.drift_detection:
            self.drift_detection.validate()
        if self.resource_cleaner:
            self.resource_cleaner.validate()
        if self.resource_import:
            self.resource_import.validate()
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
        if self.drift_detection is not None:
            result['DriftDetection'] = self.drift_detection.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_cleaner is not None:
            result['ResourceCleaner'] = self.resource_cleaner.to_map()
        if self.resource_import is not None:
            result['ResourceImport'] = self.resource_import.to_map()
        if self.template_parameter_constraints is not None:
            result['TemplateParameterConstraints'] = self.template_parameter_constraints.to_map()
        if self.template_scratch is not None:
            result['TemplateScratch'] = self.template_scratch.to_map()
        if self.terraform is not None:
            result['Terraform'] = self.terraform.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriftDetection') is not None:
            temp_model = GetFeatureDetailsResponseBodyDriftDetection()
            self.drift_detection = temp_model.from_map(m['DriftDetection'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceCleaner') is not None:
            temp_model = GetFeatureDetailsResponseBodyResourceCleaner()
            self.resource_cleaner = temp_model.from_map(m['ResourceCleaner'])
        if m.get('ResourceImport') is not None:
            temp_model = GetFeatureDetailsResponseBodyResourceImport()
            self.resource_import = temp_model.from_map(m['ResourceImport'])
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
        version_id: str = None,
    ):
        # The ID of the request.
        self.resource_type = resource_type
        # The version ID. If you want to query a specific version of the resource type, you must specify this parameter. If you do not specify this parameter, only the resource type is queried.
        # 
        # > This parameter is supported only for modules.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        create_time: str = None,
        default_version_id: str = None,
        description: str = None,
        entity_type: str = None,
        is_default_version: bool = None,
        latest_version_id: str = None,
        properties: Dict[str, Any] = None,
        provider: str = None,
        request_id: str = None,
        resource_type: str = None,
        support_drift_detection: bool = None,
        support_scratch_detection: bool = None,
        template_body: str = None,
        total_version_count: int = None,
        update_time: str = None,
    ):
        # The type of the resource.
        self.attributes = attributes
        # The creation time. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The default version ID.
        # 
        # > This parameter is returned only if the resource type is queried.
        self.default_version_id = default_version_id
        # The description of the resource type.
        self.description = description
        # The entity type. Valid values:
        # 
        # *   Resource: regular resource. For more information, see [Resources](~~28863~~).
        # *   DataSource: DataSource resource. For more information, see [DataSource resources](~~404753~~).
        # *   module: module.
        self.entity_type = entity_type
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   true
        # *   false
        # 
        # > This parameter is returned only if a specific version of the resource type is queried.
        self.is_default_version = is_default_version
        # The latest version ID.
        # 
        # > This parameter is returned only if the resource type is queried.
        self.latest_version_id = latest_version_id
        # Indicates whether the resource supports drift detection. Default value: false. Valid values:
        # 
        # *   true: Drift detection is supported.
        # *   false: Drift detection is not supported.
        self.properties = properties
        # The provider of the resource type. Valid values:
        # 
        # *   ROS: The resource type is provided by Resource Orchestration Service (ROS).
        # *   Self: The resource type is provided by you.
        self.provider = provider
        # The attributes of the resource.
        self.request_id = request_id
        # The properties of the resource.
        self.resource_type = resource_type
        # Indicates whether the resource supports scratch detection. Default value: false. Valid values:
        # 
        # *   true: Scratch detection is supported.
        # *   false: Scratch detection is not supported.
        self.support_drift_detection = support_drift_detection
        # The entity type. Valid values:
        # 
        # *   Resource: resources other than DataSource resources. For more information, see [Resources](~~28863~~).
        # *   DataSource: DataSource resources.
        self.support_scratch_detection = support_scratch_detection
        # The template content in the module.
        # 
        # > This parameter is returned only if a specific version of the resource type is queried.
        self.template_body = template_body
        # The total number of versions.
        # 
        # > This parameter is returned only if the resource type is queried.
        self.total_version_count = total_version_count
        # The update time. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_version_id is not None:
            result['DefaultVersionId'] = self.default_version_id
        if self.description is not None:
            result['Description'] = self.description
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.latest_version_id is not None:
            result['LatestVersionId'] = self.latest_version_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.support_drift_detection is not None:
            result['SupportDriftDetection'] = self.support_drift_detection
        if self.support_scratch_detection is not None:
            result['SupportScratchDetection'] = self.support_scratch_detection
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.total_version_count is not None:
            result['TotalVersionCount'] = self.total_version_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultVersionId') is not None:
            self.default_version_id = m.get('DefaultVersionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('LatestVersionId') is not None:
            self.latest_version_id = m.get('LatestVersionId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SupportDriftDetection') is not None:
            self.support_drift_detection = m.get('SupportDriftDetection')
        if m.get('SupportScratchDetection') is not None:
            self.support_scratch_detection = m.get('SupportScratchDetection')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TotalVersionCount') is not None:
            self.total_version_count = m.get('TotalVersionCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
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
        version_id: str = None,
    ):
        # The resource type.
        self.resource_type = resource_type
        # The version ID. If you want to query a specific version of the resource type, you must specify this parameter. If you do not specify this parameter, only the resource type is queried.
        # 
        # > This parameter is supported only for modules.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetResourceTypeTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_body: Dict[str, Any] = None,
        template_content: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The structure that contains the template body. The template body must be 1 to 51,200 bytes in length. For more information, see [Template syntax](~~28857~~).
        # 
        # > We recommend that use TemplateContent instead of TemplateBody.
        self.template_body = template_body
        # The JSON-formatted structure of the template body. For more information, see [Template syntax](~~28857~~).
        self.template_content = template_content

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
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
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
        # The name of the parameter. If you do not specify the name and value of a parameter, Resource Orchestration Service (ROS) uses the default name and value that are specified in the template.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify ParameterKey.
        self.parameter_key = parameter_key
        # The value of the parameter.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify ParameterValue.
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
        # The service or feature name. Valid values:
        # 
        # *   AHAS: Application High Availability Service
        # *   ARMS: Application Real-Time Monitoring Service (ARMS)
        # *   ApiGateway: API Gateway
        # *   BatchCompute: Batch Compute
        # *   BrainIndustrial: Industrial Brain
        # *   CloudStorageGateway: Cloud Storage Gateway (CSG)
        # *   CMS: CloudMonitor
        # *   CR: Container Registry
        # *   CS: Container Service for Kubernetes (ACK)
        # *   DCDN: Dynamic Content Delivery Network (DCDN)
        # *   DataHub: DataHub
        # *   DataWorks: DataWorks
        # *   EDAS: Enterprise Distributed Application Service (EDAS)
        # *   EHPC: Elastic High Performance Computing (E-HPC)
        # *   EMAS: Enterprise Mobile Application Studio (EMAS)
        # *   FC: Function Compute
        # *   FNF: Serverless Workflow (SWF)
        # *   MaxCompute: MaxCompute
        # *   MNS: Message Service (MNS)
        # *   HBR: Hybrid Backup Recovery (HBR)
        # *   IMM: Intelligent Media Management
        # *   IOT: IoT Platform
        # *   KMS: Key Management Service (KMS)
        # *   NAS: Apsara File Storage NAS (NAS)
        # *   NLP: Natural Language Processing (NLP)
        # *   OSS: OSS
        # *   OTS: Tablestore
        # *   PrivateLink: PrivateLink
        # *   PrivateZone: Alibaba Cloud DNS PrivateZone
        # *   RocketMQ: ApsaraMQ for RocketMQ
        # *   SAE: Serverless App Engine (SAE)
        # *   SLS: Log Service
        # *   TrafficMirror: the traffic mirroring feature
        # *   VS: Video Surveillance System
        # *   Xtrace: Managed Service for OpenTelemetry
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
        # The parameters.
        self.parameters = parameters
        # The region ID. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The services.
        self.services = services
        self.template_body = template_body
        # The template ID. This parameter applies to shared and private templates.
        # 
        # You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and Services.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body must be 1 to 524,288 bytes in length. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and Services.
        self.template_url = template_url
        # The version of the template. If you do not specify this parameter, the latest version is used.
        # 
        # This parameter takes effect only when TemplateId is specified.
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
        # The name of the API operation.
        self.api_name = api_name
        # The ID of the Alibaba Cloud service to which the API operation belongs.
        self.api_product_id = api_product_id
        # The type of the API operation. Valid values:
        # 
        # *   Open: public
        # *   Inner: private
        self.api_type = api_type
        # The parameters of the API operation. If a parameter is a variable, use the ${Variable name} format. Only the following variable is supported: ${RegionId}.
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
        # The information about the API operation that is used to create the RAM role.
        self.api_for_creation = api_for_creation
        # Indicates whether the RAM role is created. Valid values:
        # 
        # *   true
        # *   false
        self.created = created
        # The purpose for which the RAM role is used. Default value: Default. A value of Default indicates that the RAM role is the default role of the service.
        self.function = function
        # The name of the role.
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
        # The authorization URL of the RAM role.
        # 
        # > This parameter is returned if Created is set to false.
        self.authorization_url = authorization_url
        # The RAM roles of the service.
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
        # Indicates whether automatic activation for the service is defined in the template. Valid values:
        # 
        # *   true: Automatic activation for the service is defined in the template.
        # *   false: Manual activation for the service is defined in the template.
        self.auto_enable_service = auto_enable_service
        # The names of the services on which the service that is queried depends.
        self.dependent_service_names = dependent_service_names
        # The URL that points to the activation page of the service.
        # 
        # > This parameter is returned if Status is set to Disabled.
        self.enable_url = enable_url
        # The information about the RAM roles of the service. If this parameter is empty, no RAM role is associated with the service.
        self.role_provision = role_provision
        # The service name.
        self.service_name = service_name
        # The activation status of the service. Valid values:
        # 
        # *   Enabled: The service is activated.
        # *   Disabled: The service is not activated.
        # *   Unknown: The activation status of the service is unknown.
        self.status = status
        # The reason why the service is in the Disabled or Unknown state.
        # 
        # > This parameter is returned if Status is set to Disabled or Unknown.
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
        # The request ID.
        self.request_id = request_id
        # The information about the services.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can be up to 64 characters in length.\
        # For more information, see [Ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The option for returning logs. Valid values:
        # 
        # *   None: does not return logs.
        # *   Stack (default): returns the logs of the stack.
        # *   Resource: returns the logs of resources in the stack.
        # *   All: returns all logs.
        self.log_option = log_option
        # Specifies whether to return Outputs. Valid values:
        # 
        # *   Enabled (default)
        # *   Disabled
        # 
        # >  The Outputs parameter requires a long period of time to calculate. If you do not require Outputs of the stack, we recommend that you set OutputOption to Disabled to improve the response speed of the GetStack operation.
        self.output_option = output_option
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # Specifies whether to return information about ResourceProgress. Valid values:
        # 
        # *   Disabled (default): does not return information about ResourceProgress.
        # *   PercentageOnly: returns StackOperationProgress and StackActionProgress of ResourceProgress.
        # 
        # >  ROS and Terraform stacks are supported. Creation, resumed creation, update, deletion, import, and rollback operations on stacks are supported.
        # 
        # *   EnabledIfCreateStack (not recommend): returns \*Count and InProgressResourceDetails of ResourceProgress only during a stack creation operation.
        # 
        # >  During a creation operation, a stack is in one of the following states: CREATE_IN_PROGRESS, CREATE_COMPLETE, CREATE_FAILED, CREATE_ROLLBACK_IN_PROGRESS, CREATE_ROLLBACK_COMPLETE, and CREATE_ROLLBACK_FAILED.
        self.show_resource_progress = show_resource_progress
        # The stack ID.
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
        # The content of a resource log.
        self.content = content
        # The keywords of a resource log.
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
        # All the logs that are associated with the resources.
        self.logs = logs
        # The name of the resource that is defined in the template.
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
        # The name of the Terraform command that is run. Valid values:
        # 
        # *   apply
        # *   plan
        # *   destroy
        # *   version
        # 
        # For more information about Terraform commands, see [Basic CLI Features](https://www.terraform.io/cli/commands).
        self.command = command
        # The content of the output stream that is returned after the command is run.
        self.content = content
        # The output stream. Valid values:
        # 
        # *   stdout: standard output stream
        # *   stderr: standard error stream
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
        # The logs of resources in the stack. This parameter is returned if LogOption is set to Resource or All.
        # 
        # >  The logs are returned only for resources of specific types, such as the `ALIYUN::ROS::ResourceCleaner` type.
        self.resource_logs = resource_logs
        # The logs generated when the Terraform stack is run. This parameter is returned only for a Terraform stack. This parameter is returned if LogOption is left empty or set to Stack or All.
        # 
        # >  This parameter is not returned for a running stack. The logs are generated from the most recent operation on the stack, such as the creation, resumed creation, update, or deletion operation.
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
        # The name of the API operation that belongs to another Alibaba Cloud service.
        self.action = action
        # The error code.
        self.code = code
        # The logical ID of the resource on which the operation error occurs.
        self.logical_resource_id = logical_resource_id
        # The error message.
        self.message = message
        # The ID of the request that is initiated to call the API operation of another Alibaba Cloud service.
        self.request_id = request_id
        # The type of the resource on which the operation error occurs.
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
        # The parameter name.
        self.parameter_key = parameter_key
        # The parameter value.
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
        # The desired progress value of the resource.
        self.progress_target_value = progress_target_value
        # The current progress value of the resource.
        self.progress_value = progress_value
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
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
        stack_action_progress: float = None,
        stack_operation_progress: float = None,
        success_resource_count: int = None,
        total_resource_count: int = None,
    ):
        # The number of resources that failed to be created.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
        self.failed_resource_count = failed_resource_count
        # The number of resources that are being created.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
        self.in_progress_resource_count = in_progress_resource_count
        # The progress details of resources that are being created.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
        self.in_progress_resource_details = in_progress_resource_details
        # The number of resources to be created.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
        self.pending_resource_count = pending_resource_count
        # The creation or rollback progress of the stack, in percentage. Valid values: 0 to 100.
        # 
        # The value progressively increases from 0 to 100 during a stack creation operation. If the stack is created, the value reaches 100. If the stack fails to be created, a rollback is started for the stack resources, and the value progressively increases from the percentage of the remaining progress (100 - Progress value generated when the stack fails to be created). The value increases to 100 when the stack resources are rolled back. This parameter indicates the creation progress during a stack creation operation and indicates the rollback progress during a stack rollback operation.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `PercentageOnly`.
        self.stack_action_progress = stack_action_progress
        # The overall creation progress of the stack, in percentage. Valid values: 0 to 100.
        # 
        # The value progressively increases from 0 to 100 during a stack creation operation. If the stack is created, the value reaches 100. If the stack fails to be created, a rollback is started for the stack resources, and the value progressively decreases. The value decreases to 0 when the stack resources are rolled back. This parameter indicates only the overall creation progress, regardless of whether during a stack creation or rollback operation.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `PercentageOnly`.
        self.stack_operation_progress = stack_operation_progress
        # The number of resources that are created.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
        self.success_resource_count = success_resource_count
        # The total number of resources.
        # 
        # >  This parameter is returned only if `ShowResourceProgress` is set to `EnabledIfCreateStack`.
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
        if self.stack_action_progress is not None:
            result['StackActionProgress'] = self.stack_action_progress
        if self.stack_operation_progress is not None:
            result['StackOperationProgress'] = self.stack_operation_progress
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
        if m.get('StackActionProgress') is not None:
            self.stack_action_progress = m.get('StackActionProgress')
        if m.get('StackOperationProgress') is not None:
            self.stack_operation_progress = m.get('StackOperationProgress')
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
        # The tag key of the stack.
        self.key = key
        # The tag value of the stack.
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
        checked_stack_resource_count: int = None,
        create_time: str = None,
        deletion_protection: str = None,
        description: str = None,
        disable_rollback: bool = None,
        drift_detection_time: str = None,
        interface: str = None,
        log: GetStackResponseBodyLog = None,
        not_checked_stack_resource_count: int = None,
        notification_urls: List[str] = None,
        operation_info: GetStackResponseBodyOperationInfo = None,
        order_ids: List[str] = None,
        outputs: List[Dict[str, Any]] = None,
        parameters: List[GetStackResponseBodyParameters] = None,
        parent_stack_id: str = None,
        ram_role_name: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resource_progress: GetStackResponseBodyResourceProgress = None,
        rollback_failed_root_reason: str = None,
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
        # The number of resources on which drift detection was performed.
        # 
        # >  This parameter is returned only if the most recent drift detection on the stack was successful.
        self.checked_stack_resource_count = checked_stack_resource_count
        # The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # Indicates whether deletion protection is enabled for the stack. Valid values:
        # 
        # *   Enabled: Deletion protection is enabled for the stack.
        # *   Disabled: Deletion protection is disabled for the stack. You can delete the stack by using the ROS console or by calling the DeleteStack operation.
        # 
        # >  Deletion protection of a nested stack is the same as deletion protection of its root stack.
        self.deletion_protection = deletion_protection
        # The description of the stack.
        self.description = description
        # Indicates whether rollback is disabled when the stack fails to be created. Valid values:
        # 
        # *   true
        # *   false (default)
        self.disable_rollback = disable_rollback
        # The time when the most recent successful drift detection was performed on the stack.
        self.drift_detection_time = drift_detection_time
        # The description of the console user interface (UI).
        self.interface = interface
        # The log of the stack.
        self.log = log
        # The number of resources on which drift detection was not performed.
        # 
        # >  This parameter is returned only if the most recent drift detection on the stack was successful.
        self.not_checked_stack_resource_count = not_checked_stack_resource_count
        # The callback URLs for receiving stack events.
        self.notification_urls = notification_urls
        # The supplementary information that is returned if an error occurs on a stack operation.
        # 
        # >  This parameter is returned together with at least one sub-parameter and only under specific conditions. For example, the supplementary information is returned when an API operation of another Alibaba Cloud service fails to be called.
        self.operation_info = operation_info
        # The order IDs. This parameter is returned only if you configured manual payment when you created a subscription stack.
        self.order_ids = order_ids
        # The outputs of the stack.
        self.outputs = outputs
        # The parameters of the stack.
        self.parameters = parameters
        # The ID of the parent stack.
        self.parent_stack_id = parent_stack_id
        # The name of the Resource Access Management (RAM) role. ROS assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.\
        # ROS assumes the RAM role to perform operations on the stack. If you have permissions to perform operations on the stack, ROS assumes the RAM role even if you do not have permissions to use the RAM role. You must make sure that permissions are granted to the RAM role based on the principle of least privilege.\
        # If this parameter is not specified, ROS uses the existing role that is associated with the stack. If no roles are available, ROS uses a temporary credential that is generated from the credentials of your account.\
        # The RAM role name can be up to 64 characters in length.
        self.ram_role_name = ram_role_name
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The resource creation progress.
        self.resource_progress = resource_progress
        # 当资源栈状态为回滚失败时，该字段展示导致回滚的前一阶段执行失败的原因。
        self.rollback_failed_root_reason = rollback_failed_root_reason
        # The ID of the root stack. This parameter is returned if the specified stack is a nested stack.
        self.root_stack_id = root_stack_id
        # Indicates whether the stack is a managed stack. Valid values:
        # 
        # *   true
        # *   false
        self.service_managed = service_managed
        # The name of the service to which the managed stack belongs.
        self.service_name = service_name
        # The state of the stack on which the most recent successful drift detection was performed. Valid values:
        # 
        # *   DRIFTED: The stack has drifted.
        # *   NOT_CHECKED: No successful drift detection is performed on the stack.
        # *   IN_SYNC: The stack is being synchronized.
        self.stack_drift_status = stack_drift_status
        # The stack ID.
        self.stack_id = stack_id
        # The stack name.\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (\_). The name must start with a digit or letter.
        self.stack_name = stack_name
        # The stack type. Valid values:
        # 
        # *   ROS: ROS stack. The stack is created by using a ROS template.
        # *   Terraform: Terraform stack. The stack is created by using a Terraform template.
        self.stack_type = stack_type
        # The state of the stack. Valid values:
        # 
        # *   CREATE_IN_PROGRESS: The stack is being created.
        # *   CREATE_FAILED: The stack failed to be created.
        # *   CREATE_COMPLETE: The stack is created.
        # *   UPDATE_IN_PROGRESS: The stack is being updated.
        # *   UPDATE_FAILED: The stack failed to be updated.
        # *   UPDATE_COMPLETE: The stack is updated.
        # *   DELETE_IN_PROGRESS: The stack is being deleted.
        # *   DELETE_FAILED: The stack failed to be deleted.
        # *   CREATE_ROLLBACK_IN_PROGRESS: The resources are being rolled back after the stack failed to be created.
        # *   CREATE_ROLLBACK_FAILED: The resources failed to be rolled back after the stack failed to be created.
        # *   CREATE_ROLLBACK_COMPLETE: The resources are rolled back after the stack failed to be created.
        # *   ROLLBACK_IN_PROGRESS: The resources of the stack are being rolled back.
        # *   ROLLBACK_FAILED: The resources of the stack failed to be rolled back.
        # *   ROLLBACK_COMPLETE: The resources of the stack are rolled back.
        # *   CHECK_IN_PROGRESS: The stack is being validated.
        # *   CHECK_FAILED: The stack failed to be validated.
        # *   CHECK_COMPLETE: The stack is validated.
        # *   REVIEW_IN_PROGRESS: The stack is being reviewed.
        # *   IMPORT_CREATE_IN_PROGRESS: The stack is being created by using imported resources.
        # *   IMPORT_CREATE_FAILED: The stack failed to be created by using imported resources.
        # *   IMPORT_CREATE_COMPLETE: The stack is created by using imported resources.
        # *   IMPORT_CREATE_ROLLBACK_IN_PROGRESS: The resources are being rolled back after the stack failed to be created by using imported resources.
        # *   IMPORT_CREATE_ROLLBACK_FAILED: The resources failed to be rolled back after the stack failed to be created by using imported resources.
        # *   IMPORT_CREATE_ROLLBACK_COMPLETE: The resources are rolled back after the stack failed to be created by using imported resources.
        # *   IMPORT_UPDATE_IN_PROGRESS: The stack is being updated by using imported resources.
        # *   IMPORT_UPDATE_FAILED: The stack failed to be updated by using imported resources.
        # *   IMPORT_UPDATE_COMPLETE: The stack is updated by using imported resources.
        # *   IMPORT_UPDATE_ROLLBACK_IN_PROGRESS: The resources are being rolled back after the stack failed to be updated by using imported resources.
        # *   IMPORT_UPDATE_ROLLBACK_FAILED: The resources failed to be rolled back after the stack failed to be updated by using imported resources.
        # *   IMPORT_UPDATE_ROLLBACK_COMPLETE: The resources are rolled back after the stack failed to be updated by using imported resources.
        self.status = status
        # The reason why the stack is in its current state.
        self.status_reason = status_reason
        # The tags of the stack.
        self.tags = tags
        # The description of the template.
        self.template_description = template_description
        # The template ID. This parameter is returned only if the current stack template is a custom template or shared template.
        # 
        # If the template is a shared template, the value of this parameter is the same as the value of TemplateARN.
        self.template_id = template_id
        # The ID of the resource scenario. This parameter is returned only if the current template of the stack is generated from a resource scenario.
        self.template_scratch_id = template_scratch_id
        # The URL of the file that contains the template body. This parameter is returned only if the current template of the stack is from a URL. The URL can point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket.
        self.template_url = template_url
        # The version of the template. This parameter is returned only if the current stack template is a custom template or shared template.
        # 
        # If the template is a shared template, this parameter is returned only if VersionOption is set to AllVersions.
        # 
        # Valid values: v1 to v100.
        self.template_version = template_version
        # The timeout period for creating the stack. Unit: minutes.
        self.timeout_in_minutes = timeout_in_minutes
        # The time when the stack was updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
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
        if self.checked_stack_resource_count is not None:
            result['CheckedStackResourceCount'] = self.checked_stack_resource_count
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
        if self.not_checked_stack_resource_count is not None:
            result['NotCheckedStackResourceCount'] = self.not_checked_stack_resource_count
        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls
        if self.operation_info is not None:
            result['OperationInfo'] = self.operation_info.to_map()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
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
        if self.rollback_failed_root_reason is not None:
            result['RollbackFailedRootReason'] = self.rollback_failed_root_reason
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
        if m.get('CheckedStackResourceCount') is not None:
            self.checked_stack_resource_count = m.get('CheckedStackResourceCount')
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
        if m.get('NotCheckedStackResourceCount') is not None:
            self.not_checked_stack_resource_count = m.get('NotCheckedStackResourceCount')
        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')
        if m.get('OperationInfo') is not None:
            temp_model = GetStackResponseBodyOperationInfo()
            self.operation_info = temp_model.from_map(m['OperationInfo'])
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
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
        if m.get('RollbackFailedRootReason') is not None:
            self.rollback_failed_root_reason = m.get('RollbackFailedRootReason')
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
        # The ID of the drift detection operation.
        # 
        # You can call the [ListStackResourceDrifts](~~155098~~) operation to obtain the ID of the drift detection operation.
        self.drift_detection_id = drift_detection_id
        # The region ID of the stack to be detected for drift.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
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
        # The ID of the drift detection operation.
        self.drift_detection_id = drift_detection_id
        # The drift detection status. Valid values:
        # 
        # *   DETECTION_COMPLETE: The drift detection operation has been completed for all resources that support drift detection in the stack.
        # *   DETECTION_FAILED: The stack drift detection operation has failed for at least one resource in the stack.
        # *   DETECTION_IN_PROGRESS: The stack drift detection operation is in progress.
        self.drift_detection_status = drift_detection_status
        # The reason why the stack drift detection operation has its current status.
        self.drift_detection_status_reason = drift_detection_status_reason
        # The time when the stack drift detection operation was initiated.
        self.drift_detection_time = drift_detection_time
        # The total number of stack resources that have drifted.
        self.drifted_stack_resource_count = drifted_stack_resource_count
        # The ID of the request.
        self.request_id = request_id
        # The drift status of the stack. Valid values:
        # 
        # *   DRIFTED: The actual configuration of the stack differs, or has drifted, from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.
        # *   NOT_CHECKED: Resource Orchestration Service (ROS) has not checked whether the actual configuration of the resource differs from its expected template configuration.
        # *   IN_SYNC: The current configuration of each supported resource matches its expected template configuration. A stack with no resources that support drift detection also has a status of IN_SYNC.
        self.stack_drift_status = stack_drift_status
        # The ID of the stack.
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
        # The name of the stack group. The name must be unique within a region.
        # 
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or letter.
        # 
        # >  You must specify one of the StackGroupName and StackGroupId parameters.
        self.region_id = region_id
        # The ID of the request.
        self.stack_group_id = stack_group_id
        # The ID of the stack group.
        # 
        # >  You must specify one of the StackGroupName and StackGroupId parameters.
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
        # Indicates whether stacks in the member account are retained when the member account is deleted from the folder.
        # 
        # Valid values:
        # 
        # *   true: The stacks are retained.
        # *   false: The stacks are deleted.
        # 
        # >  This parameter is returned only when the Enabled parameter is set to true.
        self.enabled = enabled
        # The folder IDs of the resource directory. This parameter is used to deploy stack instances within all the accounts in the folders.
        # 
        # >  This parameter is returned only when the PermissionModel parameter is set to SERVICE_MANAGED.
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
        # The name of the parameter.
        self.parameter_key = parameter_key
        # The value of the parameter.
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
        # The number of stack instances that have drifted.
        self.cancelled_stack_instances_count = cancelled_stack_instances_count
        # The drift status of the stack group.
        # 
        # Valid values:
        # 
        # *   DRIFTED: At least one stack instance in the stack group has drifted.
        # *   NOT_CHECKED: No drift detection is completed on the stack group.
        # *   IN_SYNC: All the stack instances in the stack group are being synchronized.
        self.drift_detection_status = drift_detection_status
        # The number of stack instances.
        self.drift_detection_time = drift_detection_time
        # The ID of the resource group. This parameter is specified when you create the stack group.
        self.drifted_stack_instances_count = drifted_stack_instances_count
        # The status of drift detection on the stack group.
        # 
        # Valid values:
        # 
        # *   COMPLETED: Drift detection is performed and completed on all stack instances.
        # *   FAILED: Drift detection is performed. The number of stack instances that failed the drift detection exceeds the specified threshold.
        # *   PARTIAL_SUCCESS: Drift detection is performed. The number of stack instances that failed the drift detection does not exceed the specified threshold.
        # *   IN_PROGRESS: Drift detection is being performed on the stack group.
        # *   STOPPED: Drift detection is canceled for the stack group.
        self.failed_stack_instances_count = failed_stack_instances_count
        # The number of stack instances that were being synchronized.
        self.in_progress_stack_instances_count = in_progress_stack_instances_count
        # The number of stack instances for which drift detection was canceled.
        self.in_sync_stack_instances_count = in_sync_stack_instances_count
        # The number of stack instances on which drift detection was being performed.
        self.stack_group_drift_status = stack_group_drift_status
        # The number of stack instances that failed drift detection.
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
        template_content: str = None,
    ):
        # The parameters of the stack group.
        self.administration_role_name = administration_role_name
        # Indicates whether automatic deployment is enabled.
        # 
        # Valid values:
        # 
        # *   true: Automatic deployment is enabled. If a member account is added to the folder to which the stack group belongs after automatic deployment is enabled, the stack group deploys its stack instances in the specified region where the added account is deployed. If the account is deleted from the folder, the stack instances in the specified region are deleted from the stack group.
        # *   false: Automatic deployment is disabled. After automatic deployment is disabled, the stack instances remain unchanged when the member account in the folder is changed.
        self.auto_deployment = auto_deployment
        # The name of the stack group.
        self.description = description
        # The template body.
        self.execution_role_name = execution_role_name
        # The key of the parameter.
        self.parameters = parameters
        # The information about automatic deployment settings.
        # 
        # >  This parameter is returned only when the PermissionModel parameter is set to SERVICE_MANAGED.
        self.permission_model = permission_model
        # The folder IDs of the resource directory. This parameter is used to deploy stack instances within all the accounts in the folders.
        # 
        # >  This parameter is returned only when the PermissionModel parameter is set to SERVICE_MANAGED.
        self.rd_folder_ids = rd_folder_ids
        # The permission model.
        # 
        # Valid values:
        # 
        # *   SELF_MANAGED: the self-managed permission model
        # *   SERVICE_MANAGED: the service-managed permission model
        # 
        # >  For more information about the permission models of stack groups, see [Overview](~~154578~~).
        self.resource_group_id = resource_group_id
        # The time when drift detection was performed on the stack group.
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail
        # The status of the stack group.
        # 
        # Valid values:
        # 
        # *   ACTIVE
        # *   DELETED
        self.stack_group_id = stack_group_id
        # The name of the RAM role that is specified for the execution account when you create the self-managed stack group. The administrator role AliyunROSStackGroupAdministrationRole assumes the execution role. If this parameter is not specified, the default value AliyunROSStackGroupExecutionRole is returned.
        self.stack_group_name = stack_group_name
        # The name of the RAM role that is specified for the administrator account in Resource Orchestration Service (ROS) when you create the self-managed stack group. If this parameter is not specified, the default value AliyunROSStackGroupAdministrationRole is returned.
        self.status = status
        # The structure that contains the template body.
        # 
        # > We recommend that you use TemplateContent instead of TemplateBody.
        self.template_body = template_body
        # The JSON-formatted structure that contains the template body. For more information, see [Template syntax](~~28857~~).
        self.template_content = template_content

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
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
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
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        return self


class GetStackGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_group: GetStackGroupResponseBodyStackGroup = None,
    ):
        # The details of the stack group.
        self.request_id = request_id
        # Details of the stack group.
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
        # The operation ID. You can call the [ListStackGroupOperations](~~151342~~) operation to query the operation ID.
        self.operation_id = operation_id
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
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
        # The IDs of the members in the resource directory.
        # 
        # > This parameter is returned only if AccountIds is specified when the [UpdateStackInstances](~~151716~~) operation is called to update stack instances.
        self.account_ids = account_ids
        # The IDs of the folders in the resource directory.
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
        # The number of accounts within which stack operation failures are allowed to occur in each region. If the value of this parameter is exceeded in a region, Resource Orchestration Service (ROS) stops the operation in the region. If the operation is stopped in one region, the operation is no longer performed in other regions.
        # 
        # Valid values: 0 to 20.
        # 
        # > Only one of FailureToleranceCount and FailureTolerancePercentage can be returned.
        self.failure_tolerance_count = failure_tolerance_count
        # The percentage of the number of accounts within which stack operation failures are allowed to occur to the total number of accounts in each region. If the value of this parameter is exceeded in a region, ROS stops the operation in the region.
        # 
        # Valid values: 0 to 100.
        # 
        # > Only one of FailureToleranceCount and FailureTolerancePercentage can be returned.
        self.failure_tolerance_percentage = failure_tolerance_percentage
        # The maximum number of accounts within which stacks are deployed at the same time in each region.
        # 
        # Valid values: 1 to 20.
        # 
        # > Only one of MaxConcurrentCount and MaxConcurrentPercentage can be returned.
        self.max_concurrent_count = max_concurrent_count
        # The percentage of the maximum number of accounts within which stacks are deployed at the same time to the total number of accounts in each region.
        # 
        # Valid values: 1 to 100.
        # 
        # > Only one of MaxConcurrentCount and MaxConcurrentPercentage can be returned.
        self.max_concurrent_percentage = max_concurrent_percentage
        # The regions in the order of operation execution.
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
        # The number of stack instances for which drift detection was canceled.
        self.cancelled_stack_instances_count = cancelled_stack_instances_count
        # The drift detection state.
        # 
        # Valid values:
        # 
        # *   COMPLETED: Drift detection is performed on the stack group and all stack instances passed the drift detection.
        # *   FAILED: Drift detection is performed on the stack group. The number of stack instances that failed the drift detection exceeds the specified threshold.
        # *   PARTIAL_SUCCESS: Drift detection is performed on the stack group. The number of stack instances that failed the drift detection does not exceed the specified threshold.
        # *   IN_PROGRESS: Drift detection is being performed on the stack group.
        # *   STOPPED: Drift detection is canceled for the stack group.
        self.drift_detection_status = drift_detection_status
        # The time when drift detection was performed.
        self.drift_detection_time = drift_detection_time
        # The number of stack instances that have drifted.
        self.drifted_stack_instances_count = drifted_stack_instances_count
        # The number of stack instances that failed drift detection.
        self.failed_stack_instances_count = failed_stack_instances_count
        # The number of stack instances on which drift detection was being performed.
        self.in_progress_stack_instances_count = in_progress_stack_instances_count
        # The number of stack instances that were being synchronized.
        self.in_sync_stack_instances_count = in_sync_stack_instances_count
        # The drift state of the stack group.
        # 
        # Valid values:
        # 
        # *   DRIFTED: At least one stack instance in the stack group has drifted.
        # *   NOT_CHECKED: No successful drift detection is performed in the stack group.
        # *   IN_SYNC: All the stack instances in the stack group are being synchronized.
        self.stack_group_drift_status = stack_group_drift_status
        # The number of stack instances.
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
        # The operation type.
        # 
        # Valid values:
        # 
        # *   CREATE
        # *   UPDATE
        # *   DELETE
        # *   DETECT_DRIFT
        self.action = action
        # The name of the RAM role that you specify for the administrator account when you create the self-managed stack group. ROS assumes the administrator role to perform operations. If this parameter is not specified, the default value AliyunROSStackGroupAdministrationRole is returned.
        self.administration_role_name = administration_role_name
        # The time when the operation was initiated.
        self.create_time = create_time
        # The destinations to deploy stack instances when the stack is granted service-managed permissions.
        self.deployment_targets = deployment_targets
        # The time when the operation ended.
        self.end_time = end_time
        # The name of the RAM role that you specify for the execution account when you create the self-managed stack group. The administrator role AliyunROSStackGroupAdministrationRole assumes the execution role to perform operations. If this parameter is not specified, the default value AliyunROSStackGroupExecutionRole is returned.
        self.execution_role_name = execution_role_name
        # The description of the operation.
        # 
        # > This parameter is returned only if OperationDescription is specified when the [CreateStackInstances](~~151338~~) operation is called to create stack instances.
        self.operation_description = operation_description
        # The operation ID.
        self.operation_id = operation_id
        # The operation settings.
        self.operation_preferences = operation_preferences
        # Indicates whether stacks are retained when the associated stack instances are deleted. When you delete a stack instance, you can choose to delete or retain the stack with which the stack instance is associated.
        # 
        # Valid values:
        # 
        # *   true: Stacks are retained when the associated stack instances are deleted.
        # *   false: Stacks are deleted when the associated stack instances are deleted. Proceed with caution.
        # 
        # > This parameter is returned only if you delete stack instances.
        self.retain_stacks = retain_stacks
        # The information about drift detection.
        # 
        # > This parameter is returned only if drift detection is performed.
        self.stack_group_drift_detection_detail = stack_group_drift_detection_detail
        # The ID of the stack group.
        self.stack_group_id = stack_group_id
        # The name of the stack group.
        self.stack_group_name = stack_group_name
        # The state of the operation.
        # 
        # Valid values:
        # 
        # *   RUNNING
        # *   SUCCEEDED
        # *   FAILED
        # *   STOPPING
        # *   STOPPED
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
        # The request ID.
        self.request_id = request_id
        # The information about the stack group operation.
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
        output_option: str = None,
        region_id: str = None,
        stack_group_name: str = None,
        stack_instance_account_id: str = None,
        stack_instance_region_id: str = None,
    ):
        self.output_option = output_option
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The name of the stack group. The name must be unique within a region.\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or letter.
        self.stack_group_name = stack_group_name
        # The ID of the destination account to which the stack belongs.
        # 
        # *   If the stack group is granted self-managed permissions, the stack belongs to an Alibaba Cloud account.
        # *   If the stack group is granted service-managed permissions, the stack belongs to a member in a resource directory.
        # 
        # > For more information about the destination account, see [Overview](~~154578~~).
        self.stack_instance_account_id = stack_instance_account_id
        # The region ID of the stack.
        self.stack_instance_region_id = stack_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_option is not None:
            result['OutputOption'] = self.output_option
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
        if m.get('OutputOption') is not None:
            self.output_option = m.get('OutputOption')
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
        # The name of the parameter that is used to override a specific parameter.
        self.parameter_key = parameter_key
        # The value of the parameter that is used to override a specific parameter.
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
        outputs: List[Dict[str, Any]] = None,
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
        # The ID of the destination account to which the stack belongs.
        self.account_id = account_id
        # The time when the most recent successful drift detection was performed on the stack group.
        # 
        # > This parameter is returned only if drift detection is performed on the stack group.
        self.drift_detection_time = drift_detection_time
        self.outputs = outputs
        # The parameters that are used to override specific parameters.
        self.parameter_overrides = parameter_overrides
        # The ID of the folder in the resource directory.
        # 
        # > This parameter is returned only if the stack group is granted service-managed permissions.
        self.rd_folder_id = rd_folder_id
        # The region ID of the stack.
        self.region_id = region_id
        # The state of the stack when the most recent successful drift detection was performed on the stack group.
        # 
        # Valid values:
        # 
        # *   DRIFTED: The stack has drifted.
        # *   NOT_CHECKED: No successful drift detection is performed on the stack.
        # *   IN_SYNC: The stack is being synchronized.
        # 
        # > This parameter is returned only if drift detection is performed on the stack group.
        self.stack_drift_status = stack_drift_status
        # The ID of the stack group.
        self.stack_group_id = stack_group_id
        # The name of the stack group.
        self.stack_group_name = stack_group_name
        # The stack ID.
        # 
        # > This parameter is returned only if the stack is in the CURRENT state.
        self.stack_id = stack_id
        # The state of the stack.
        # 
        # Valid values:
        # 
        # *   CURRENT: The stack is up-to-date with the stack group.
        # 
        # *   OUTDATED: The stack is not up-to-date with the stack group. Stacks are in the OUTDATED state due to the following possible reasons:
        # 
        #     *   When the CreateStackInstances operation is called to create stacks, the stacks fail to be created.
        #     *   When the UpdateStackInstances or UpdateStackGroup operation is called to update stacks, the stacks fail to be updated, or only specific stacks are updated.
        #     *   The creation or update operation is not complete.
        self.status = status
        # The reason why the stack instance is in the OUTDATED state.
        # 
        # > This parameter is returned only if the stack instance is in the OUTDATED state.
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
        if self.outputs is not None:
            result['Outputs'] = self.outputs
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
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
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
        # The request ID.
        self.request_id = request_id
        # The information about the stack.
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
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the stack.
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
        # The ID of the request.
        self.request_id = request_id
        # The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length.
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
        # Specifies whether to query the resource properties. Valid values:
        # 
        # *   true
        # *   false
        self.client_token = client_token
        # The name of resource property N that you want to query.
        # 
        # >  Maximum value of N: 20.
        self.logical_resource_id = logical_resource_id
        # The logical ID of the resource defined in the template.
        self.region_id = region_id
        # The status of the resource. Valid values:
        # 
        # *   CREATE_COMPLETE
        # *   CREATE_FAILED
        # *   CREATE_IN_PROGRESS
        # *   UPDATE_IN_PROGRESS
        # *   UPDATE_FAILED
        # *   UPDATE_COMPLETE
        # *   DELETE_IN_PROGRESS
        # *   DELETE_FAILED
        # *   CHECK_IN_PROGRESS
        # *   CHECK_FAILED
        # *   CHECK_COMPLETE
        # *   IMPORT_IN_PROGRESS
        # *   IMPORT_FAILED
        # *   IMPORT_COMPLETE
        self.resource_attributes = resource_attributes
        # The name of resource property N that you want to query.
        self.show_resource_attributes = show_resource_attributes
        # The ID of the region to which the stack belongs. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
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


class GetStackResourceResponseBodyModuleInfo(TeaModel):
    def __init__(
        self,
        logical_id_hierarchy: str = None,
        type_hierarchy: str = None,
    ):
        # The concatenated logical IDs of one or more modules that contain the resource. The modules are listed from the outermost layer and separated by forward slashes (`/`).
        # 
        # In the following example, the resource is created from Module B nested within Parent Module A:
        # 
        # `moduleA/moduleB`
        self.logical_id_hierarchy = logical_id_hierarchy
        # The concatenated types of one or more modules that contain the resource. The module types are listed from the outermost layer and separated by forward slashes (`/`).
        # 
        # In the following example, the resource is created from a module of the `MODULE::ROS::Child::Example` type that is nested within a parent module of the `MODULE::ROS::Parent::Example` type:
        # 
        # `MODULE::ROS::Parent::Example/MODULE::ROS::Child::Example`
        self.type_hierarchy = type_hierarchy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_id_hierarchy is not None:
            result['LogicalIdHierarchy'] = self.logical_id_hierarchy
        if self.type_hierarchy is not None:
            result['TypeHierarchy'] = self.type_hierarchy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalIdHierarchy') is not None:
            self.logical_id_hierarchy = m.get('LogicalIdHierarchy')
        if m.get('TypeHierarchy') is not None:
            self.type_hierarchy = m.get('TypeHierarchy')
        return self


class GetStackResourceResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        drift_detection_time: str = None,
        logical_resource_id: str = None,
        metadata: Dict[str, Any] = None,
        module_info: GetStackResourceResponseBodyModuleInfo = None,
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
        # The resource type.
        self.create_time = create_time
        # The reason why the resource is in its current state.
        self.description = description
        # The ID of the stack.
        self.drift_detection_time = drift_detection_time
        # The time when the resource was updated.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.logical_resource_id = logical_resource_id
        # The list of the resource properties.
        self.metadata = metadata
        # The information about the modules from which the resource is created. This parameter is returned only if the resource is created from modules.
        self.module_info = module_info
        # The metadata.
        self.physical_resource_id = physical_resource_id
        # The physical ID of the resource.
        self.request_id = request_id
        # The status of the resource in the last successful drift detection. Valid values:
        # 
        # *   DELETED: The actual configuration of the resource differs from its expected template configuration because the resource is deleted.
        # *   MODIFIED: The actual configuration of the resource differs from its expected template configuration.
        # *   NOT_CHECKED: ROS has not checked whether the actual configuration of the resource differs from its expected template configuration.
        # *   IN_SYNC: The actual configuration of the resource matches its expected template configuration.
        self.resource_attributes = resource_attributes
        # The time when the last successful drift detection was performed on the stack.
        self.resource_drift_status = resource_drift_status
        # The logical ID of the resource defined in the template.
        self.resource_type = resource_type
        # The ID of the stack.
        self.stack_id = stack_id
        # The name of the stack.
        self.stack_name = stack_name
        # The ID of the request.
        self.status = status
        # The time when the resource was created.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.status_reason = status_reason
        # The name of the stack.
        # 
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (\_). The name must start with a digit or letter.
        self.update_time = update_time

    def validate(self):
        if self.module_info:
            self.module_info.validate()

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
        if self.module_info is not None:
            result['ModuleInfo'] = self.module_info.to_map()
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
        if m.get('ModuleInfo') is not None:
            temp_model = GetStackResourceResponseBodyModuleInfo()
            self.module_info = temp_model.from_map(m['ModuleInfo'])
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
        # The ID of the change set.
        # 
        # > You must specify one of the following parameters: StackId, ChangeSetId, StackGroupName, and TemplateId.
        self.change_set_id = change_set_id
        # Specifies whether to query the shared information about the template. Valid values:
        # 
        # *   Enabled
        # *   Disabled (default)
        # 
        # > Only the template owner can query the shared information of a template.
        self.include_permission = include_permission
        # Specifies whether to query the information about tags. Valid values:
        # 
        # *   Enabled
        # *   Disabled (default)
        # 
        # > This parameter takes effect only if you specify TemplateId.
        self.include_tags = include_tags
        # The region ID of the stack or stack group that uses the template. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The name of the stack group.
        # 
        # > You must specify one of the following parameters: StackId, ChangeSetId, StackGroupName, and TemplateId.
        self.stack_group_name = stack_group_name
        # The ID of the stack.
        # 
        # > You must specify one of the following parameters: StackId, ChangeSetId, StackGroupName, and TemplateId.
        self.stack_id = stack_id
        # The ID of the template.
        # 
        # This parameter applies to shared and private templates. If the template is a shared template, the value of TemplateId is the same as the value of TemplateARN. You can use the template ID to query a shared template.
        # 
        # > You must specify one of the following parameters: StackId, ChangeSetId, StackGroupName, and TemplateId.
        self.template_id = template_id
        # The stage of the template. This parameter takes effect only if you specify StackId, ChangeSetId, or StackGroupName.
        # 
        # Valid values:
        # 
        # *   Processed (default): returns the processed template.
        # *   Original: returns the original template.
        self.template_stage = template_stage
        # The version of the template. This parameter takes effect only if you specify TemplateId.\
        # If the template is a shared template, you can specify this parameter only if VersionOption is set to AllVersions. For more information, see [SetTemplatePermission](~~194768~~).
        # 
        # Valid values: v1 to v100.
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
        # The ID of the Alibaba Cloud account with which the template is shared.
        self.account_id = account_id
        # The sharing option.
        # 
        # The value ShareToAccounts indicates that the template is shared with one or more Alibaba Cloud accounts.
        self.share_option = share_option
        # The service that is used for resource sharing. Valid values:
        # 
        # - ROS: Resources are shared from ROS by using the ROS console or calling the ROS API.
        # - ResourceDirectory: Resources are shared with accounts in a resource directory from Resource Management by using the resource sharing feature.
        # > -  The number of accounts with which resources are shared from ROS is independent of the number of accounts with which resources are shared from the resource directory.
        # > -  The shared resources from ROS cannot override or overwrite the shared resources from the resource directory.
        # > -  The shared resources from the resource directory can overwrite the shared resources from ROS.
        self.share_source = share_source
        # The version of the shared template. This parameter is returned only if you set ShareOption to ShareToAccounts and set VersionOption to Specified or Current.
        # 
        # Valid values: v1 to v100.
        self.template_version = template_version
        # The version option for the shared template. This parameter is returned only if you set ShareOption to ShareToAccounts.
        # 
        # Valid values:
        # 
        # *   AllVersions: All template versions are shared.
        # *   Latest: Only the latest template version is shared. When the version of the template is updated, Resource Orchestration Service (ROS) updates the shared version to the latest version.
        # *   Current: Only the latest template version is shared. When the version of the template is updated, ROS does not update the shared version.
        # *   Specified: Only the specified template version is shared.
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
        # The tag key of the template.
        self.key = key
        # The tag value of the template.
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
        # The ID of the change set. This parameter is returned only if you specify ChangeSetId.
        self.change_set_id = change_set_id
        # The time when the template was created. This parameter is returned only if you specify TemplateId.
        # 
        # > - If you specify TemplateVersion, the creation time of the template whose version is specified by TemplateVersion is returned.
        # > - If you do not specify TemplateVersion, the creation time of the template whose version is the default version is returned.
        self.create_time = create_time
        # The description of the template. This parameter is returned only if you specify TemplateId.
        self.description = description
        # The description of the web UI in the ROS console.
        self.interface = interface
        # The ID of the Alibaba Cloud account to which the template belongs. This parameter is returned only if you specify TemplateId.
        self.owner_id = owner_id
        # Details of the sharing status of the template. This parameter is returned only if you specify TemplateId and set IncludePermission to Enabled.
        # 
        # > - If TemplateVersion is not specified or does not take effect, the details of the sharing status of the template whose version is the default version is returned.
        # > - If TemplateVersion is specified and takes effect, the details of the sharing status of the template whose version is specified by TemplateVersion is returned.
        self.permissions = permissions
        # The region ID of the stack or stack group that uses the template. This parameter is returned only if you specify StackId, ChangeSetId, or StackGroupName.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The sharing type of the template. This parameter is returned only if you specify TemplateId.
        # 
        # Valid values:
        # 
        # *   Private: The template belongs to the template owner.
        # *   Shared: The template is shared by other users.
        self.share_type = share_type
        # The name of the stack group. This parameter is returned only if you specify StackGroupName.
        self.stack_group_name = stack_group_name
        # The ID of the stack. This parameter is returned only if you specify StackId.
        self.stack_id = stack_id
        # The tags of the template.
        self.tags = tags
        # The Alibaba Cloud Resource Name (ARN) of the template. This parameter is returned only if you specify TemplateId.
        self.template_arn = template_arn
        # The content of the template.
        self.template_body = template_body
        # The ID of the template. This parameter is returned only if you specify TemplateId.
        # 
        # If the template is a shared template, the value of this parameter is the same as the value of TemplateARN.
        self.template_id = template_id
        # The name of the template. This parameter is returned only if you specify TemplateId.
        # 
        # > -   If you specify TemplateVersion, the name of the template whose version is specified by TemplateVersion is returned.
        # > -  If you not specify TemplateVersion, the name of the template whose version is the default version is returned.
        self.template_name = template_name
        # The version of the template. This parameter is returned only if you specify TemplateId.\
        # If TemplateVersion is not specified or does not take effect, the default version is used.
        # 
        # If the template is a shared template, this parameter is returned only if you set VersionOption to AllVersions.
        self.template_version = template_version
        # The time when the template was last updated. This parameter is returned only if you specify TemplateId.
        # 
        # > - If you specify TemplateVersion, the last update time of the template whose version is specified by TemplateVersion is returned.
        # > - If you do not specify TemplateVersion, the last update time of the template whose version is the default version is returned.
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
        # The ID of the request.
        self.parameter_key = parameter_key
        # Details of the resource.
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
        stack_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_scratch_id: str = None,
        template_scratch_region_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        # The name of parameter N. If you do not specify the name and value of a parameter, ROS uses the default name and value that are specified in the template.
        # 
        # Maximum value of N: 200.
        # 
        # Examples:
        # 
        # *   Parameters.1.ParameterKey: `Name`
        # *   Parameters.2.ParameterKey: `Netmode`
        # 
        # >  The Parameters parameter is optional. If you want to specify Parameters, you must specify both Parameters.N.ParameterKey and Parameters.N.ParameterValue.
        self.client_token = client_token
        # The region ID of the scenario. The default value is the same as the value of the RegionId parameter.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.parameters = parameters
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.region_id = region_id
        # The stack ID.
        # 
        # This parameter is used to query the estimated price in a configuration change scenario.
        # 
        # Assume that the specified stack contains only one Elastic Compute Service (ECS) instance and the instance type is ecs.s6-c1m2.large. You downgrade the instance type to ecs.s6-c1m1.small and specify a new ApsaraDB RDS instance in the template that is used for the price inquiry. The queried result is the sum of the downgrade refund of the ECS instance and the price of the new ApsaraDB RDS instance.
        self.stack_id = stack_id
        self.template_body = template_body
        # The value of parameter N.
        # 
        # Maximum value of N: 200.
        # 
        # Examples:
        # 
        # *   Parameters.1.ParameterValue: `DemoEip`
        # *   Parameters.2.ParameterValue: `public`
        # 
        # >  The Parameters parameter is optional. If you want to specify Parameters, you must specify both Parameters.N.ParameterKey and Parameters.N.ParameterValue.
        self.template_id = template_id
        # The ID of the scenario.
        self.template_scratch_id = template_scratch_id
        # The region ID of the scenario. The default value is the same as the value of the RegionId parameter.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.template_scratch_region_id = template_scratch_region_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests.
        # 
        # The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [Ensure idempotence](~~134212~~).
        self.template_url = template_url
        # The ID of the scenario.
        # 
        # For more information about how to query the IDs of scenarios, see [ListTemplateScratches](~~363050~~).
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
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
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
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
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
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
        # The ID of the request.
        self.request_id = request_id
        # The resource details.
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
        # The name of parameter N in the template.
        # 
        # >  The Parameters parameter is optional. If you specify the Parameters parameter, you must specify the Parameters.N.ParameterKey parameter.
        self.parameter_key = parameter_key
        # The value of parameter N in the template.
        # 
        # >  The Parameters parameter is optional. If you specify the Parameters parameter, you must specify the Parameters.N.ParameterValue parameter.
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
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [Ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The name of parameter N in the template.
        self.parameters = parameters
        # The parameters whose values you want to query.
        self.parameters_key_filter = parameters_key_filter
        # The order in which associated parameters are arranged.
        # 
        # >  By default, the order of the associated parameters specified in the `Metadata` section of the template is used.
        self.parameters_order = parameters_order
        # The region ID of the template.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the stack.
        self.stack_id = stack_id
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length. If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_url = template_url
        # The version of the template. If you do not specify this parameter, the latest version is used.
        # 
        # >  This parameter takes effect only if the TemplateId parameter is specified.
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
        # The name of parameter N in the template.
        # 
        # >  The Parameters parameter is optional. If you specify the Parameters parameter, you must specify the Parameters.N.ParameterKey parameter.
        self.parameter_key = parameter_key
        # The value of parameter N in the template.
        # 
        # >  The Parameters parameter is optional. If you specify the Parameters parameter, you must specify the Parameters.N.ParameterValue parameter.
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
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [Ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The name of parameter N in the template.
        self.parameters = parameters
        # The parameters whose values you want to query.
        self.parameters_key_filter_shrink = parameters_key_filter_shrink
        # The order in which associated parameters are arranged.
        # 
        # >  By default, the order of the associated parameters specified in the `Metadata` section of the template is used.
        self.parameters_order_shrink = parameters_order_shrink
        # The region ID of the template.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the stack.
        self.stack_id = stack_id
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length. If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_url = template_url
        # The version of the template. If you do not specify this parameter, the latest version is used.
        # 
        # >  This parameter takes effect only if the TemplateId parameter is specified.
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
        # The name of the resource property.
        self.property_name = property_name
        # The resource type.
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


class GetTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints(TeaModel):
    def __init__(
        self,
        allowed_values: List[Any] = None,
        property_name: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The values of the parameter.
        self.allowed_values = allowed_values
        # The name of the resource property.
        self.property_name = property_name
        # The name of the resource that is defined in the template.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
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
        # The error message.
        self.error_message = error_message
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
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
        original_constraints: List[GetTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints] = None,
        parameter_key: str = None,
        query_errors: List[GetTemplateParameterConstraintsResponseBodyParameterConstraintsQueryErrors] = None,
        type: str = None,
    ):
        # The values of the parameter.
        self.allowed_values = allowed_values
        # The names of the associated parameters.
        self.association_parameter_names = association_parameter_names
        # The behavior of the parameter. Valid values:
        # 
        # *   NoLimit: No limit is imposed on the value of this parameter.
        # *   NotSupport: The value of this parameter cannot be queried.
        # *   QueryError: This parameter failed to be queried.
        # 
        # > If AllowedValues is not returned, Behavior and BehaviorReason are returned.
        self.behavior = behavior
        # The reason why the behavior of the parameter is returned.
        self.behavior_reason = behavior_reason
        # The values that do not conform to the parameter constraints.
        # 
        # > If AllowedValues is returned, IllegalValueByParameterConstraints and IllegalValueByRules are returned at the same time.
        self.illegal_value_by_parameter_constraints = illegal_value_by_parameter_constraints
        # The values that do not match the rules in the template.
        # 
        # > If AllowedValues is returned, IllegalValueByParameterConstraints and IllegalValueByRules are returned at the same time.
        self.illegal_value_by_rules = illegal_value_by_rules
        # The unsupported resource in the template.
        self.not_support_resources = not_support_resources
        # The original constraint information.
        self.original_constraints = original_constraints
        # The name of the parameter.
        self.parameter_key = parameter_key
        # The error that is returned when the request fails.
        self.query_errors = query_errors
        # The data type of the parameter.
        self.type = type

    def validate(self):
        if self.not_support_resources:
            for k in self.not_support_resources:
                if k:
                    k.validate()
        if self.original_constraints:
            for k in self.original_constraints:
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
        result['OriginalConstraints'] = []
        if self.original_constraints is not None:
            for k in self.original_constraints:
                result['OriginalConstraints'].append(k.to_map() if k else None)
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
        self.original_constraints = []
        if m.get('OriginalConstraints') is not None:
            for k in m.get('OriginalConstraints'):
                temp_model = GetTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints()
                self.original_constraints.append(temp_model.from_map(k))
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
        # The constraints of the parameters.
        self.parameter_constraints = parameter_constraints
        # The ID of the request.
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


class GetTemplateRecommendParametersRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_candidate_values: List[str] = None,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_candidate_values = parameter_candidate_values
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_candidate_values is not None:
            result['ParameterCandidateValues'] = self.parameter_candidate_values
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterCandidateValues') is not None:
            self.parameter_candidate_values = m.get('ParameterCandidateValues')
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetTemplateRecommendParametersRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        parameters: List[GetTemplateRecommendParametersRequestParameters] = None,
        region_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.client_token = client_token
        self.parameters = parameters
        self.region_id = region_id
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
                temp_model = GetTemplateRecommendParametersRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetTemplateRecommendParametersResponseBodyRecommendParameterValues(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        recommend_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.recommend_value = recommend_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.recommend_value is not None:
            result['RecommendValue'] = self.recommend_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('RecommendValue') is not None:
            self.recommend_value = m.get('RecommendValue')
        return self


class GetTemplateRecommendParametersResponseBody(TeaModel):
    def __init__(
        self,
        recommend_parameter_values: List[GetTemplateRecommendParametersResponseBodyRecommendParameterValues] = None,
        request_id: str = None,
    ):
        self.recommend_parameter_values = recommend_parameter_values
        self.request_id = request_id

    def validate(self):
        if self.recommend_parameter_values:
            for k in self.recommend_parameter_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RecommendParameterValues'] = []
        if self.recommend_parameter_values is not None:
            for k in self.recommend_parameter_values:
                result['RecommendParameterValues'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recommend_parameter_values = []
        if m.get('RecommendParameterValues') is not None:
            for k in m.get('RecommendParameterValues'):
                temp_model = GetTemplateRecommendParametersResponseBodyRecommendParameterValues()
                self.recommend_parameter_values.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTemplateRecommendParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateRecommendParametersResponseBody = None,
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
            temp_model = GetTemplateRecommendParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateScratchRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        show_data_option: str = None,
        template_scratch_id: str = None,
    ):
        # The region ID of the scenario.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The data display option. Valid values:
        # 
        # *   Sources: displays only the data of source nodes. This setting takes effect only when TemplateScratchType is set to ArchitectureDetection.
        # *   Source: displays only the data of the source node. This setting takes effect only when TemplateScratchType is not set to ArchitectureDetection.
        # *   Provisions: displays only the data of new nodes. This setting takes effect only when TemplateScratchType is not set to ArchitectureDetection.
        # *   All: displays all data.
        # 
        # For more information about source nodes and new nodes, see [Overview](~~352074~~).
        # 
        # >  If you do not specify this parameter, the node data is not displayed.
        self.show_data_option = show_data_option
        # The ID of the scenario.
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
        # The parameter name.
        self.parameter_key = parameter_key
        # The parameter value.
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
        # The ID of the source resource group.
        self.resource_group_id = resource_group_id
        # The resource types.
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
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
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
        # The source tags.
        self.resource_tags = resource_tags
        # The resource types.
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
        # Indicates whether the resource is replicated by calling the [CreateStack](~~132086~~) operation. Valid values:
        # 
        # *   true
        # *   false
        self.creatable = creatable
        # Indicates whether the resource is managed by calling the [CreateChangeSet](~~131051~~) operation. Valid values:
        # 
        # *   true
        # *   false
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
        # The region ID of the stack.
        self.region_id = region_id
        # The stack ID.
        self.stack_id = stack_id
        # The purpose of the stack. Valid values:
        # 
        # *   ResourceImport: resource management
        # *   ArchitectureReplication: resource replication
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
        resource_group_id: str = None,
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
        # The time at which the scenario was created.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the scenario.
        self.description = description
        # The status code of the scenario that fails to be created.
        # 
        # > This parameter is returned only if you set Status to GENERATE_FAILED.
        self.failed_code = failed_code
        # The policy based on which the logical ID is generated. Valid values:
        # 
        # *   LongTypePrefixAndIndexSuffix (default): long-type prefix + index-type suffix
        # *   LongTypePrefixAndHashSuffix: long-type prefix + hash-type suffix
        # *   ShortTypePrefixAndHashSuffix: short-type prefix + hash-type suffix
        self.logical_id_strategy = logical_id_strategy
        # The preference parameters of the scenario.
        self.preference_parameters = preference_parameters
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The source resource group.
        self.source_resource_group = source_resource_group
        # The source resources.
        self.source_resources = source_resources
        # The source tag.
        self.source_tag = source_tag
        # The preset information of the stack.
        self.stack_provision = stack_provision
        # The stacks that are associated with the scenario.
        self.stacks = stacks
        # The state of the scenario. Valid values:
        # 
        # *   GENERATE_IN_PROGRESS: The scenario is being created.
        # *   GENERATE_COMPLETE: The scenario is created.
        # *   GENERATE_FAILED: The scenario fails to be created.
        self.status = status
        # The reason why the scenario fails to be created.
        # 
        # > This parameter is returned only if you set Status to GENERATE_FAILED.
        self.status_reason = status_reason
        # The scenario data.
        self.template_scratch_data = template_scratch_data
        # The ID of the scenario.
        self.template_scratch_id = template_scratch_id
        # The type of the scenario. Valid values:
        # 
        # *   ResourceImport: resource management
        # *   ArchitectureReplication: resource replication
        self.template_scratch_type = template_scratch_type
        # The time at which the scenario was updated.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        # The ID of the request.
        self.request_id = request_id
        # The resource scenario.
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
        # The name of parameter N that is defined in the template. If you do not specify the name and value of a parameter, Resource Orchestration Service (ROS) uses the default name and value that are defined in the template.
        # 
        # Maximum value of N: 200.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify both Parameters.N.ParameterKey and Parameters.N.ParameterValue.
        self.parameter_key = parameter_key
        # The value of parameter N that is defined in the template.
        # 
        # Maximum value of N: 200.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify both Parameters.N.ParameterKey and Parameters.N.ParameterValue.
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
        # The ID of the change set.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        self.change_set_id = change_set_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).\
        # For more information, see [Ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The parameters that are defined in the template.
        self.parameters = parameters
        # The region ID of the stack or stack group that uses the template. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        # 
        # This parameter takes effect only when one of the following parameters are specified: StackId, ChangeSetId, and StackGroupName.
        self.region_id = region_id
        # The name of the stack group.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        self.stack_group_name = stack_group_name
        # The stack ID.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        self.stack_id = stack_id
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length.\
        # If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.\
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        self.template_body = template_body
        # The template ID. This parameter applies to shared and private templates.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length.
        # 
        # > If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        # 
        # The URL can be up to 1,024 bytes in length.
        self.template_url = template_url
        # The version of the template. This parameter takes effect when TemplateId is specified.
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
        # The logical IDs of all resources of the type that is specified by ResouceType in the template.
        self.logical_resource_ids = logical_resource_ids
        # The resource properties. You can use a resource property to identify the resource that you want to manage. For example, VpcId is an identifier property of ALIYUN::ECS::VPC.
        self.resource_identifiers = resource_identifiers
        # The resource type.
        # 
        # > The resource import feature is supported for the resource type.
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
        # The description of the stack template.
        self.description = description
        # The metadata that is defined in the template.
        self.metadata = metadata
        # The declarations of the parameters in the template.
        self.parameters = parameters
        # The request ID.
        self.request_id = request_id
        # The resource identifier summaries.\
        # A summary describes the resource that you want to import and the properties that are used to identify the resource during the import. For example, VpcId is an identifier property of ALIYUN::ECS::VPC.
        self.resource_identifier_summaries = resource_identifier_summaries
        # All resource types that are used in the template.
        self.resource_types = resource_types
        # The version of the template.
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
        # The ID of the change set. If detailed information about the change set is not required, you can use this parameter to replace the GetChangeSet operation.
        self.change_set_id = change_set_id
        # The name of change set N. Maximum value of N: 5. You can use an asterisk (\*) as a wildcard for fuzzy search.
        self.change_set_name = change_set_name
        # The execution status of change set N. Maximum value of N: 5. Valid values:
        # 
        # *   UNAVAILABLE
        # *   AVAILABLE
        # *   EXECUTE_IN_PROGRESS
        # *   EXECUTE_COMPLETE
        # *   EXECUTE_FAILED
        # *   OBSOLETE
        self.execution_status = execution_status
        # The page number.\
        # Pages start from page 1.\
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.\
        # Valid values: 1 to 50.\
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the change set. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the stack.
        self.stack_id = stack_id
        # The status of change set N. Maximum value of N: 5. Valid values:
        # 
        # *   CREATE_PENDING
        # *   CREATE_IN_PROGRESS
        # *   CREATE_COMPLETE
        # *   CREATE_FAILED
        # *   DELETE_FAILED
        # *   DELETE_COMPLETE
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
        # The ID of the change set.
        self.change_set_id = change_set_id
        # The name of the change set.
        self.change_set_name = change_set_name
        # The type of the change set.
        self.change_set_type = change_set_type
        # The time when the change set was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the change set.
        self.description = description
        # The execution status of the change set.
        self.execution_status = execution_status
        # The region ID of the change set.
        self.region_id = region_id
        # The ID of the stack with which the change set is associated.
        self.stack_id = stack_id
        # The name of the stack with which the change set is associated.
        self.stack_name = stack_name
        # The status of the change set.
        self.status = status
        # The reason why the change set is in its current state.
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
        # The change sets.
        self.change_sets = change_sets
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of change sets returned.
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


class ListDiagnosticsRequest(TeaModel):
    def __init__(
        self,
        diagnostic_key: str = None,
        diagnostic_product: str = None,
        max_results: str = None,
        next_token: str = None,
        status: str = None,
    ):
        # The keyword in the diagnosis.
        self.diagnostic_key = diagnostic_key
        # The product that is diagnosed.
        self.diagnostic_product = diagnostic_product
        # The maximum number of results to be returned in a single call when NextToken is used for the query.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The diagnosis status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnostic_key is not None:
            result['DiagnosticKey'] = self.diagnostic_key
        if self.diagnostic_product is not None:
            result['DiagnosticProduct'] = self.diagnostic_product
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosticKey') is not None:
            self.diagnostic_key = m.get('DiagnosticKey')
        if m.get('DiagnosticProduct') is not None:
            self.diagnostic_product = m.get('DiagnosticProduct')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDiagnosticsResponseBodyDiagnostics(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        diagnostic_key: str = None,
        diagnostic_product: str = None,
        report_id: str = None,
        status: str = None,
    ):
        # The time when the diagnostic report was generated.
        self.create_time = create_time
        # The keyword in the diagnosis.
        self.diagnostic_key = diagnostic_key
        # The product that is diagnosed.
        self.diagnostic_product = diagnostic_product
        # The ID of the diagnostic report.
        self.report_id = report_id
        # The diagnosis status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.diagnostic_key is not None:
            result['DiagnosticKey'] = self.diagnostic_key
        if self.diagnostic_product is not None:
            result['DiagnosticProduct'] = self.diagnostic_product
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DiagnosticKey') is not None:
            self.diagnostic_key = m.get('DiagnosticKey')
        if m.get('DiagnosticProduct') is not None:
            self.diagnostic_product = m.get('DiagnosticProduct')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDiagnosticsResponseBody(TeaModel):
    def __init__(
        self,
        diagnostics: List[ListDiagnosticsResponseBodyDiagnostics] = None,
        http_status_code: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The items that are diagnosed.
        self.diagnostics = diagnostics
        # The HTTP status code returned. The value 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.diagnostics:
            for k in self.diagnostics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Diagnostics'] = []
        if self.diagnostics is not None:
            for k in self.diagnostics:
                result['Diagnostics'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.diagnostics = []
        if m.get('Diagnostics') is not None:
            for k in m.get('Diagnostics'):
                temp_model = ListDiagnosticsResponseBodyDiagnostics()
                self.diagnostics.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDiagnosticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDiagnosticsResponseBody = None,
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
            temp_model = ListDiagnosticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTypeRegistrationsRequest(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
        page_number: int = None,
        page_size: int = None,
        registration_id: str = None,
        resource_type: str = None,
        status: str = None,
    ):
        # The entity type. Set the value to Module.
        self.entity_type = entity_type
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50. Default value: 10.
        self.page_size = page_size
        # The ID of the registration record.
        self.registration_id = registration_id
        # The resource type. The resource type can contain letters, digits, colons (:), and asterisks (\*). You can use an asterisk (\*) to perform a fuzzy match.
        self.resource_type = resource_type
        # The registration state. Valid values:
        # 
        # *   IN_PROGRESS
        # *   COMPLETE
        # *   FAILED
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListResourceTypeRegistrationsResponseBodyRegistrations(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        entity_type: str = None,
        registration_id: str = None,
        resource_type: str = None,
        status: str = None,
        status_reason: str = None,
        version_id: str = None,
    ):
        # The time when the version was created. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.create_time = create_time
        # The entity type. Only Module may be returned.
        self.entity_type = entity_type
        # The ID of the registration record.
        self.registration_id = registration_id
        # The resource type.
        self.resource_type = resource_type
        # The registration state. Valid values:
        # 
        # *   IN_PROGRESS
        # *   COMPLETE
        # *   FAILED
        self.status = status
        # The reason for the state.
        self.status_reason = status_reason
        # The version ID.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ListResourceTypeRegistrationsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        registrations: List[ListResourceTypeRegistrationsResponseBodyRegistrations] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The registration records.
        self.registrations = registrations
        # The request ID.
        self.request_id = request_id
        # The total number of registration records.
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Registrations'] = []
        if self.registrations is not None:
            for k in self.registrations:
                result['Registrations'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.registrations = []
        if m.get('Registrations') is not None:
            for k in m.get('Registrations'):
                temp_model = ListResourceTypeRegistrationsResponseBodyRegistrations()
                self.registrations.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceTypeRegistrationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceTypeRegistrationsResponseBody = None,
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
            temp_model = ListResourceTypeRegistrationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTypeVersionsRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        # The resource type.
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


class ListResourceTypeVersionsResponseBodyResourceTypeVersions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        entity_type: str = None,
        is_default_version: bool = None,
        provider: str = None,
        resource_type: str = None,
        update_time: str = None,
        version_id: str = None,
    ):
        # The time when the version was created. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.create_time = create_time
        # The description of the version.
        self.description = description
        # The entity type. Only Module may be returned.
        self.entity_type = entity_type
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   true
        # *   false
        self.is_default_version = is_default_version
        # The provider of the resource type. Valid values:
        # 
        # *   ROS: ROS
        # *   Self: yourself
        self.provider = provider
        # The resource type.
        self.resource_type = resource_type
        # The time when the version was updated. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.update_time = update_time
        # The version ID.
        self.version_id = version_id

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
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.is_default_version is not None:
            result['IsDefaultVersion'] = self.is_default_version
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('IsDefaultVersion') is not None:
            self.is_default_version = m.get('IsDefaultVersion')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ListResourceTypeVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type_versions: List[ListResourceTypeVersionsResponseBodyResourceTypeVersions] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The versions of the resource types.
        self.resource_type_versions = resource_type_versions

    def validate(self):
        if self.resource_type_versions:
            for k in self.resource_type_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceTypeVersions'] = []
        if self.resource_type_versions is not None:
            for k in self.resource_type_versions:
                result['ResourceTypeVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_type_versions = []
        if m.get('ResourceTypeVersions') is not None:
            for k in m.get('ResourceTypeVersions'):
                temp_model = ListResourceTypeVersionsResponseBodyResourceTypeVersions()
                self.resource_type_versions.append(temp_model.from_map(k))
        return self


class ListResourceTypeVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceTypeVersionsResponseBody = None,
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
            temp_model = ListResourceTypeVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTypesRequest(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
        provider: str = None,
        resource_type: str = None,
    ):
        # The entity type. Valid values:
        # 
        # *   All: all types of resources.
        # *   Resource (default): regular resources. For more information, see [Resources](~~28863~~).
        # *   DataSource: DataSource resources. For more information, see [DataSource resources](~~404753~~).
        # *   Module: modules.
        self.entity_type = entity_type
        # The provider of the resource type. Valid values:
        # 
        # *   ROS (default): The resource type is provided by Resource Orchestration Service (ROS).
        # *   Self: The resource type is provided by you.
        self.provider = provider
        # The resource type. The resource type can contain letters, digits, colons (:), and asterisks (\*). You can use an asterisk (\*) to perform a fuzzy match.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListResourceTypesResponseBodyResourceTypeSummaries(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        default_version_id: str = None,
        description: str = None,
        entity_type: str = None,
        latest_version_id: str = None,
        provider: str = None,
        resource_type: str = None,
        total_version_count: int = None,
        update_time: str = None,
    ):
        # The creation time. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.create_time = create_time
        # The ID of the default version.
        self.default_version_id = default_version_id
        # The description of the resource type.
        self.description = description
        # The entity type. Valid values:
        # 
        # *   Resource: regular resources.
        # *   DataSource: DataSource resources.
        # *   Module: modules.
        self.entity_type = entity_type
        # The ID of the latest version.
        self.latest_version_id = latest_version_id
        # The provider of the resource type. Valid values:
        # 
        # *   ROS: The resource type is provided by ROS.
        # *   Self: The resource type is provided by you.
        self.provider = provider
        # The resource type.
        self.resource_type = resource_type
        # The number of versions.
        self.total_version_count = total_version_count
        # The update time. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
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
        if self.default_version_id is not None:
            result['DefaultVersionId'] = self.default_version_id
        if self.description is not None:
            result['Description'] = self.description
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.latest_version_id is not None:
            result['LatestVersionId'] = self.latest_version_id
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.total_version_count is not None:
            result['TotalVersionCount'] = self.total_version_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultVersionId') is not None:
            self.default_version_id = m.get('DefaultVersionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('LatestVersionId') is not None:
            self.latest_version_id = m.get('LatestVersionId')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TotalVersionCount') is not None:
            self.total_version_count = m.get('TotalVersionCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListResourceTypesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type_summaries: List[ListResourceTypesResponseBodyResourceTypeSummaries] = None,
        resource_types: List[str] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The resource type summaries.
        self.resource_type_summaries = resource_type_summaries
        # The array of resource types.
        self.resource_types = resource_types

    def validate(self):
        if self.resource_type_summaries:
            for k in self.resource_type_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceTypeSummaries'] = []
        if self.resource_type_summaries is not None:
            for k in self.resource_type_summaries:
                result['ResourceTypeSummaries'].append(k.to_map() if k else None)
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_type_summaries = []
        if m.get('ResourceTypeSummaries') is not None:
            for k in m.get('ResourceTypeSummaries'):
                temp_model = ListResourceTypesResponseBodyResourceTypeSummaries()
                self.resource_type_summaries.append(temp_model.from_map(k))
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
        # The logical IDs of the resources.
        self.logical_resource_id = logical_resource_id
        # The number of the page to return.\
        # Pages start from page 1.\
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.\
        # Maximum value: 50.\
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The resource types.
        self.resource_type = resource_type
        # The stack ID.
        self.stack_id = stack_id
        # The status of the resource.
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
        # The time when the event was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The event ID.
        self.event_id = event_id
        # The logical ID of the resource. The logical ID indicates the name of the resource that is defined in the template.
        self.logical_resource_id = logical_resource_id
        # The physical ID of the resource.
        self.physical_resource_id = physical_resource_id
        # The resource type.
        self.resource_type = resource_type
        # The stack ID.
        self.stack_id = stack_id
        # The stack name.
        self.stack_name = stack_name
        # The state of the resource.
        self.status = status
        # The reason why the resource is in the current state.
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
        # The events.
        self.events = events
        # The page number of the returned page.\
        # Pages start from page 1.\
        # Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page.\
        # Maximum value: 50.\
        # Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of returned events.
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
        # The ID of the operation.
        # 
        # You can call the [ListStackGroupOperations](~~151342~~) operation to query the operation ID.
        self.operation_id = operation_id
        # The number of the page to return.
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # *   Valid values: 1 to 50.
        # *   Default value: 10.
        self.page_size = page_size
        # The region ID of the stack group.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
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
        # The ID of the account to which the stack instance belongs.
        # 
        # *   If the stack group has self-managed permissions, the stack instance belongs to an Alibaba Cloud account.
        # *   If the stack group has service-managed permissions, the stack instance belongs to a member account in the resource directory.
        # 
        # >  For more information about the account, see [Overview](~~154578~~).
        self.account_id = account_id
        # The folder ID of the resource directory.
        # 
        # >  This parameter is returned only when the stack group is granted service-managed permissions.
        self.rd_folder_id = rd_folder_id
        # The region ID of the stack instance.
        self.region_id = region_id
        # The status of the operation.
        # 
        # Valid values:
        # 
        # *   RUNNING: The operation is being performed.
        # *   SUCCEEDED: The operation succeeded.
        # *   FAILED: The operation failed.
        # *   STOPPING: The operation is being stopped.
        # *   STOPPED: The operation is stopped.
        self.status = status
        # The reason why the operation is in a specific state.
        # 
        # >  This parameter is returned only when stack instances are in the OUTDATED state.
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
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The details of the results of the operation.
        self.stack_group_operation_results = stack_group_operation_results
        # The total number of results.
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
        # The number of the page to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The name of the stack group. The name must be unique within a region.
        # 
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or letter.
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
        # The operation type.
        # 
        # Valid values:
        # 
        # *   CREATE
        # *   UPDATE
        # *   DELETE
        # *   DETECT_DRIFT
        self.action = action
        # The time when the operation was initiated.
        self.create_time = create_time
        # The time when the operation ended.
        self.end_time = end_time
        # The description of the operation.
        self.operation_description = operation_description
        # The operation ID.
        self.operation_id = operation_id
        # The ID of the stack group.
        self.stack_group_id = stack_group_id
        # The name of the stack group.
        self.stack_group_name = stack_group_name
        # The state of the operation.
        # 
        # Valid values:
        # 
        # *   RUNNING
        # *   SUCCEEDED
        # *   FAILED
        # *   STOPPING
        # *   STOPPED
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
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The stack group operations.
        self.stack_group_operations = stack_group_operations
        # The total number of stack group operations.
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
        # The key of the tag that is added to the stack group.
        # 
        # > Tags is optional. If you specify Tags, you must specify Tags.N.Key.
        self.key = key
        # The value of the tag that is added to the stack group.
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
        # The number of the page to return.
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # *   Valid values: 1 to 50.
        # *   Default value: 10.
        self.page_size = page_size
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group. If you do not specify this parameter, the stack groups in all the resource groups are queried.
        # 
        # > To obtain the resource group ID, go to the **Resource Group** page in the **Resource Management** console. For more information, see [View the basic information about a resource group](~~151181~~).
        self.resource_group_id = resource_group_id
        # The state of the stack group. If you do not specify this parameter, the stack groups in all states in the specified region are queried.
        # 
        # Valid values:
        # 
        # *   ACTIVE
        # *   DELETED
        self.status = status
        # The tags that are added to the stack group.
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
        # Indicates whether automatic deployment is enabled.
        # 
        # Valid values:
        # 
        # *   true: Automatic deployment is enabled. If you add a member to the folder to which the stack group belongs after automatic deployment is enabled, Resource Orchestration Service (ROS) automatically adds the stack instances in the stack group to the specified region of the member. If you delete the member from the folder, ROS automatically deletes the stack instances in the stack group from the specified region of the member.
        # *   false: Automatic deployment is disabled. After you disable automatic deployment, the stack instances remain unchanged when you change the member in the folder.
        self.enabled = enabled
        # Indicates whether the stacks within a member are retained when you delete the member from the folder.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # > This parameter is returned only if Enabled is set to true.
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
        # The key of the tag that is added to the stack group.
        self.key = key
        # The value of the tag that is added to the stack group.
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
        # The information about automatic deployment settings.
        self.auto_deployment = auto_deployment
        # The description of the stack group.
        self.description = description
        # The time when the most recent successful drift detection was performed on the stack group.
        self.drift_detection_time = drift_detection_time
        # The permission model of the stack group.
        # 
        # Valid values:
        # 
        # *   SELF_MANAGED
        # *   SERVICE_MANAGED
        # 
        # > For more information about the permission models of stack groups, see [Overview](~~154578~~).
        self.permission_model = permission_model
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The drift state of the stack group on which the most recent successful drift detection was performed.
        # 
        # Valid values:
        # 
        # *   DRIFTED: The stack group has drifted.
        # *   NOT_CHECKED: No drift detection is performed on the stack group.
        # *   IN_SYNC: No drifts are detected on the stack group.
        self.stack_group_drift_status = stack_group_drift_status
        # The ID of the stack group.
        self.stack_group_id = stack_group_id
        # The name of the stack group.
        self.stack_group_name = stack_group_name
        # The state of the stack group.
        # 
        # Valid values:
        # 
        # *   ACTIVE
        # *   DELETED
        self.status = status
        # The tags that are added to the stack group.
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
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The stack groups.
        self.stack_groups = stack_groups
        # The total number of stack groups.
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
        # The number of the page to return.
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # *   Valid values: 1 to 50.
        # *   Default value: 10.
        self.page_size = page_size
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The name of the stack group. The name must be unique within a region.\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or letter.
        self.stack_group_name = stack_group_name
        # The ID of the destination account to which the stack belongs.
        # 
        # *   If the stack group is granted self-managed permissions, the stack belongs to an Alibaba Cloud account.
        # *   If the stack group is granted service-managed permissions, the stack belongs to a member in a resource directory.
        # 
        # > For more information about the destination account, see [Overview](~~154578~~).
        self.stack_instance_account_id = stack_instance_account_id
        # The region ID of the stack.
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
        # The ID of the destination account to which the stack belongs.
        self.account_id = account_id
        # The time when the last successful drift detection was performed on the stack.
        # 
        # > This parameter is returned only if drift detection is performed on the stack group.
        self.drift_detection_time = drift_detection_time
        # The ID of the folder in the resource directory.
        # 
        # > This parameter is returned only if the stack group is granted service-managed permissions.
        self.rd_folder_id = rd_folder_id
        # The region ID of the stack.
        self.region_id = region_id
        # The state of the stack when the last successful drift detection was performed on the stack group.
        # 
        # Valid values:
        # 
        # *   DRIFTED: The stack has drifted.
        # *   NOT_CHECKED: No successful drift detection is performed on the stack.
        # *   IN_SYNC: The stack is being synchronized.
        # 
        # > This parameter is returned only if drift detection is performed on the stack group.
        self.stack_drift_status = stack_drift_status
        # The ID of the stack group.
        self.stack_group_id = stack_group_id
        # The name of the stack group.
        self.stack_group_name = stack_group_name
        # The stack ID.
        # 
        # > This parameter is returned only if the stack is in the CURRENT state.
        self.stack_id = stack_id
        # The state of the stack.
        # 
        # Valid values:
        # 
        # *   CURRENT: The stack is up-to-date with the stack group.
        # 
        # *   OUTDATED: The stack is not up-to-date with the stack group. Stacks are in the OUTDATED state due to the following possible reasons:
        # 
        #     *   When the CreateStackInstances operation is called to create stacks, the stacks fail to be created.
        #     *   When the UpdateStackInstances or UpdateStackGroup operation is called to update stacks, the stacks fail to be updated, or only specific stacks are updated.
        #     *   The creation or update operation is not complete.
        self.status = status
        # The reason why the stack instance is in the OUTDATED state.
        # 
        # > This parameter is returned only if the stack instance is in the OUTDATED state.
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
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The stacks.
        self.stack_instances = stack_instances
        # The total number of stacks.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The type of the operation of which you want to detect risks. Valid values:
        # 
        # *   DeleteStack: detects high risks that may arise in resources when you delete a stack.
        # *   CreateStack: detects the missing permissions when you fail to create a stack.
        self.operation_type = operation_type
        # The name of the RAM role.
        # 
        # *   If you specify a RAM role, ROS creates stacks based on the permissions that are granted to the RAM role and uses the credentials of the RAM role to call the API operations of Alibaba Cloud services.
        # *   If you do not specify a RAM role, ROS creates stacks based on the permissions of your Alibaba Cloud account.
        # 
        # The name of the RAM role can be up to 64 bytes in length.
        self.ram_role_name = ram_role_name
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # Specifies whether to retain all resources in the stack. Valid values:
        # 
        # *   true
        # *   false (default)
        # 
        # > This parameter takes effect only if you set OperationType to DeleteStack.
        self.retain_all_resources = retain_all_resources
        # The list of resources to retain.
        # 
        # > This parameter takes effect only if you set OperationType to DeleteStack.
        self.retain_resources = retain_resources
        # The ID of the stack.
        self.stack_id = stack_id
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # > You must specify one of TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo and oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length. If you do not specify RegionId in the URL, the region ID of the stack is used.
        # 
        # > You must specify one of TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_url = template_url
        # The version of the template.
        # 
        # > This parameter takes effect only if you specify TemplateId.
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
        # The error code that is returned when the risk detection fails.
        # 
        # >  This parameter is not returned if the risk detection is successful.
        self.code = code
        # The logical ID of the resource. The logical ID is the resource name that is defined in the template.
        self.logical_resource_id = logical_resource_id
        # The error message that is returned when the risk detection fails.
        # 
        # >  This parameter is not returned if the risk detection is successful.
        self.message = message
        # The physical ID of the resource. The physical ID is the actual ID of the resource.
        self.physical_resource_id = physical_resource_id
        # The cause of the risk.
        self.reason = reason
        # The ID of the request when the risk detection fails.
        # 
        # >  This parameter is not returned if the risk detection is successful.
        self.request_id = request_id
        # The type of the resource.
        self.resource_type = resource_type
        # The type of the risk. Valid values:
        # 
        # *   Referenced: The resource is referenced by other resources.
        # *   MaybeReferenced: The resource may be referenced by other resources.
        # *   AdditionalRiskCheckRequired: An additional risk detection is required for a nested stack.
        # *   OperationIgnored: The operation does not take effect for the resource.
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
        # The operations on which the permissions are not granted to the Alibaba Cloud account of the caller.
        self.missing_policy_actions = missing_policy_actions
        # The ID of the request.
        self.request_id = request_id
        # The resources that are at risk.
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
        # The time when the resource drift detection operation was initiated.
        self.max_results = max_results
        # The type of the resource.
        self.next_token = next_token
        # The physical ID of the resource.
        self.region_id = region_id
        # The resource properties as defined in the template, in JSON format.
        self.resource_drift_status = resource_drift_status
        # The ID of the stack.
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


class ListStackResourceDriftsResponseBodyResourceDriftsModuleInfo(TeaModel):
    def __init__(
        self,
        logical_id_hierarchy: str = None,
        type_hierarchy: str = None,
    ):
        # The concatenated logical IDs of one or more modules that contain the resource. The modules are listed from the outermost layer and separated by forward slashes (`/`).
        # 
        # In the following example, the resource is created from Module B nested within Parent Module A:
        # 
        # `moduleA/moduleB`
        self.logical_id_hierarchy = logical_id_hierarchy
        # The concatenated types of one or more modules that contain the resource. The module types are listed from the outermost layer and separated by forward slashes (`/`).
        # 
        # In the following example, the resource is created from a module of the `MODULE::ROS::Child::Example` type that is nested within a parent module of the `MODULE::ROS::Parent::Example` type:
        # 
        # `MODULE::ROS::Parent::Example/MODULE::ROS::Child::Example`
        self.type_hierarchy = type_hierarchy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_id_hierarchy is not None:
            result['LogicalIdHierarchy'] = self.logical_id_hierarchy
        if self.type_hierarchy is not None:
            result['TypeHierarchy'] = self.type_hierarchy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalIdHierarchy') is not None:
            self.logical_id_hierarchy = m.get('LogicalIdHierarchy')
        if m.get('TypeHierarchy') is not None:
            self.type_hierarchy = m.get('TypeHierarchy')
        return self


class ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences(TeaModel):
    def __init__(
        self,
        actual_value: str = None,
        difference_type: str = None,
        expected_value: str = None,
        property_path: str = None,
    ):
        # The actual value of the resource property.
        self.actual_value = actual_value
        # The drift type of the resource property. Valid values:
        # 
        # *   ADD: The value is added to a resource property whose data type is Array or List.
        # *   REMOVE: The property is deleted from the current resource configuration.
        # *   NOT_EQUAL: The current property value differs from the expected value that is defined in the stack template.
        self.difference_type = difference_type
        # The expected value of the resource property that is defined in the template.
        self.expected_value = expected_value
        # The path of the resource property.
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
        module_info: ListStackResourceDriftsResponseBodyResourceDriftsModuleInfo = None,
        physical_resource_id: str = None,
        property_differences: List[ListStackResourceDriftsResponseBodyResourceDriftsPropertyDifferences] = None,
        resource_drift_status: str = None,
        resource_type: str = None,
        stack_id: str = None,
    ):
        # The actual JSON-formatted resource properties.
        self.actual_properties = actual_properties
        # The time when the drift detection operation was performed on the resource.
        self.drift_detection_time = drift_detection_time
        # The JSON-formatted resource properties that are defined in the template.
        self.expected_properties = expected_properties
        # The logical ID of the resource. The logical ID indicates the name of the resource that is defined in the template.
        self.logical_resource_id = logical_resource_id
        # The information about the modules from which the resource was created. This parameter is returned only if the resource is created from modules.
        self.module_info = module_info
        # The physical ID of the resource.
        self.physical_resource_id = physical_resource_id
        # The property drifts of the resource.
        self.property_differences = property_differences
        # The drift state of the resource. Valid values:
        # 
        # *   DELETED: The actual configuration of the resource differs from its expected template configuration because the resource is deleted.
        # *   MODIFIED: The actual configuration of the resource differs from its expected template configuration.
        # *   NOT_CHECKED: Resource Orchestration Service (ROS) has not checked whether the actual configuration of the resource differs from its expected template configuration.
        # *   IN_SYNC: The actual configuration of the resource matches its expected template configuration.
        self.resource_drift_status = resource_drift_status
        # The resource type.
        self.resource_type = resource_type
        # The stack ID.
        self.stack_id = stack_id

    def validate(self):
        if self.module_info:
            self.module_info.validate()
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
        if self.module_info is not None:
            result['ModuleInfo'] = self.module_info.to_map()
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
        if m.get('ModuleInfo') is not None:
            temp_model = ListStackResourceDriftsResponseBodyResourceDriftsModuleInfo()
            self.module_info = temp_model.from_map(m['ModuleInfo'])
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
        # The query token returned in this call.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The resource drifts.
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
        # The ID of the request.
        self.region_id = region_id
        # The ID of the region to which the stack belongs. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
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


class ListStackResourcesResponseBodyResourcesModuleInfo(TeaModel):
    def __init__(
        self,
        logical_id_hierarchy: str = None,
        type_hierarchy: str = None,
    ):
        # The concatenated logical IDs of one or more modules that contain the resource. The modules are listed from the outermost layer and separated by forward slashes (`/`).
        # 
        # In the following example, the resource is created from Module B nested within Parent Module A:
        # 
        # `moduleA/moduleB`
        self.logical_id_hierarchy = logical_id_hierarchy
        # The concatenated types of one or more modules that contain the resource. The module types are listed from the outermost layer and separated by forward slashes (`/`).
        # 
        # In the following example, the resource is created from a module of the `MODULE::ROS::Child::Example` type that is nested within a parent module of the `MODULE::ROS::Parent::Example` type:
        # 
        # `MODULE::ROS::Parent::Example/MODULE::ROS::Child::Example`
        self.type_hierarchy = type_hierarchy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logical_id_hierarchy is not None:
            result['LogicalIdHierarchy'] = self.logical_id_hierarchy
        if self.type_hierarchy is not None:
            result['TypeHierarchy'] = self.type_hierarchy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalIdHierarchy') is not None:
            self.logical_id_hierarchy = m.get('LogicalIdHierarchy')
        if m.get('TypeHierarchy') is not None:
            self.type_hierarchy = m.get('TypeHierarchy')
        return self


class ListStackResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        drift_detection_time: str = None,
        logical_resource_id: str = None,
        module_info: ListStackResourcesResponseBodyResourcesModuleInfo = None,
        physical_resource_id: str = None,
        resource_drift_status: str = None,
        resource_type: str = None,
        stack_id: str = None,
        stack_name: str = None,
        status: str = None,
        status_reason: str = None,
        update_time: str = None,
    ):
        # The time when the resource was created. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.create_time = create_time
        # The time when the most recent successful drift detection was performed on the stack.
        self.drift_detection_time = drift_detection_time
        # The logical ID of the resource. The logical ID is the resource name that is defined in the template.
        self.logical_resource_id = logical_resource_id
        # The information about the modules from which the resource is created. This parameter is returned only if the resource is created from modules.
        self.module_info = module_info
        # The physical ID of the resource.
        self.physical_resource_id = physical_resource_id
        # The drift state of the resource in the most recent successful drift detection. Valid values:
        # 
        # *   DELETED: The actual configuration of the resource differs from its expected template configuration because the resource is deleted.
        # *   MODIFIED: The actual configuration of the resource differs from its expected template configuration.
        # *   NOT_CHECKED: Resource Orchestration Service (ROS) has not checked whether the actual configuration of the resource differs from its expected template configuration.
        # *   IN_SYNC: The actual configuration of the resource matches its expected template configuration.
        self.resource_drift_status = resource_drift_status
        # The resource type.
        self.resource_type = resource_type
        # The stack ID.
        self.stack_id = stack_id
        # The stack name.\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or letter.
        self.stack_name = stack_name
        # The state of the resource. Valid values:
        # 
        # *   INIT_COMPLETE: The resource is pending to be created.
        # *   CREATE_COMPLETE: The resource is created.
        # *   CREATE_FAILED: The resource failed to be created.
        # *   CREATE_IN_PROGRESS: The resource is being created.
        # *   UPDATE_IN_PROGRESS: The resource is being updated.
        # *   UPDATE_FAILED: The resource failed to be updated.
        # *   UPDATE_COMPLETE: The resource is updated.
        # *   DELETE_IN_PROGRESS: The resource is being deleted.
        # *   DELETE_FAILED: The resource failed to be deleted.
        # *   DELETE_COMPLETE: The resource is deleted.
        # *   CHECK_IN_PROGRESS: The resource is being validated.
        # *   CHECK_FAILED: The resource failed to be validated.
        # *   CHECK_COMPLETE: The resource is validated.
        # *   IMPORT_IN_PROGRESS: The resource is being imported.
        # *   IMPORT_FAILED: The resource failed to be imported.
        # *   IMPORT_COMPLETE: The resource is imported.
        self.status = status
        # The reason why the resource is in its current state.
        self.status_reason = status_reason
        # The time when the resource was updated. The time is displayed in UTC. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format.
        self.update_time = update_time

    def validate(self):
        if self.module_info:
            self.module_info.validate()

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
        if self.module_info is not None:
            result['ModuleInfo'] = self.module_info.to_map()
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
        if m.get('ModuleInfo') is not None:
            temp_model = ListStackResourcesResponseBodyResourcesModuleInfo()
            self.module_info = temp_model.from_map(m['ModuleInfo'])
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
        # Details about resources.
        self.request_id = request_id
        # The resources.
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
        # The key of tag N.\
        # Valid values of N: 1 to 20.
        self.key = key
        # The value of tag N.\
        # Valid values of N: 1 to 20.
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
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_stack_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        show_nested_stack: bool = None,
        stack_id: str = None,
        stack_ids: List[str] = None,
        stack_name: List[str] = None,
        start_time: str = None,
        status: List[str] = None,
        tag: List[ListStacksRequestTag] = None,
    ):
        # The end of the time range during which data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The ID of the parent stack.
        self.parent_stack_id = parent_stack_id
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.\
        # For more information about resource groups, see the "Resource Group" section of the [What is Resource Management?](~~94475~~) topic.
        self.resource_group_id = resource_group_id
        # Specifies whether to return nested stacks. Valid values:
        # 
        # *   true
        # *   false (default)
        # 
        # > If you specify ParentStackId, you must set ShowNestedStack to true.
        self.show_nested_stack = show_nested_stack
        # The stack ID. You can specify this parameter to query only the stack ID. If you want to query the detailed information about the stack, call the GetStack operation.
        self.stack_id = stack_id
        # The IDs of the stacks.
        self.stack_ids = stack_ids
        # The names of the stacks.
        self.stack_name = stack_name
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.start_time = start_time
        # The status of the stack.
        self.status = status
        # The tags of the stack.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
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
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
        # The name of the API operation that belongs to another Alibaba Cloud service.
        self.action = action
        # The error code.
        self.code = code
        # The logical ID of the resource on which the operation error occurred.
        self.logical_resource_id = logical_resource_id
        # The error message.
        self.message = message
        # The ID of the request that is initiated to call the API operation of another Alibaba Cloud service.
        self.request_id = request_id
        # The type of the resource on which the operation error occurred.
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
        # The tag key of the stack.
        self.key = key
        # The tag value of the stack.
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
        deletion_protection: str = None,
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
        # The time when the stack was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # Indicates whether deletion protection is enabled for the stack. Valid values:
        # 
        # *   Enabled: Deletion protection is enabled for the stack.
        # *   Disabled: Deletion protection is disabled for the stack. In this case, you can delete the stack by using the console or calling the [DeleteStack](~~610812~~) operation.
        # 
        # >  Deletion protection of a nested stack is the same as that of its root stack.
        self.deletion_protection = deletion_protection
        # Indicates whether rollback is disabled when the stack fails to be created. Valid values:
        # 
        # *   true
        # *   false (default)
        self.disable_rollback = disable_rollback
        # The time when the most recent successful drift detection was performed on the stack.
        self.drift_detection_time = drift_detection_time
        # The supplementary information that is returned if an error occurs on a stack operation.
        # 
        # >  This parameter is returned only under specific conditions, and is returned together with at least one sub-parameter. For example, an error occurred when an API operation of another Alibaba Cloud service was called.
        self.operation_info = operation_info
        # The ID of the parent stack.
        self.parent_stack_id = parent_stack_id
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether the stack is a managed stack. Valid values:
        # 
        # *   true
        # *   false
        self.service_managed = service_managed
        # The name of the service to which the managed stack belongs.
        self.service_name = service_name
        # The state of the stack on which the most recent successful drift detection was performed. Valid values:
        # 
        # *   DRIFTED: The stack has drifted.
        # *   NOT_CHECKED: No successful drift detection is performed on the stack.
        # *   IN_SYNC: The stack is being synchronized.
        self.stack_drift_status = stack_drift_status
        # The stack ID.
        self.stack_id = stack_id
        # The stack name.
        self.stack_name = stack_name
        # The stack type. Valid values:
        # 
        # *   ROS: ROS stack. The stack is created by using a ROS template.
        # *   Terraform: Terraform stack. The stack is created by using a Terraform template.
        self.stack_type = stack_type
        # The state of the stack.
        self.status = status
        # The reason why the stack is in its current state.
        self.status_reason = status_reason
        # The tags of the stack.
        self.tags = tags
        # The timeout period for creating the stack. Unit: minutes.
        self.timeout_in_minutes = timeout_in_minutes
        # The time when the stack was updated. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
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
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
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
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
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
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Details of the stacks.
        self.stacks = stacks
        # The total number of stacks.
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
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID of the tag key. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The type of the resource. Valid values:
        # 
        # *   stack: stack
        # *   stackgroup: stack group
        # *   template: template
        # *   templatescratch: scenario
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
        # The tag keys.
        self.keys = keys
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
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
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.\
        # The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.\
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. The tag value cannot start with `aliyun` or `acs:`.
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
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID of the tag. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The IDs of the resources.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   stack: stack
        # *   stackgroup: stack group
        # *   template: template
        # *   templatescratch: scenario
        self.resource_type = resource_type
        # The tags of the resources. You can specify up to 20 tags.
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
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type
        # The tag key of the resource.
        self.tag_key = tag_key
        # The tag value of the resource.
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
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information about the tags that are added to the resources.
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
        # The key of the tag.
        self.key = key
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID of the tag value. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The type of the resource. Valid values:
        # 
        # *   stack: stack
        # *   stackgroup: stack group
        # *   template: template
        # *   templatescratch: scenario
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
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tag values.
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
        # The tag key of the scenario.
        # 
        # > Tags is optional. If you want to specify Tags, you must specify Key.
        self.key = key
        # The tag value of the scenario.
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
        resource_group_id: str = None,
        status: str = None,
        tags: List[ListTemplateScratchesRequestTags] = None,
        template_scratch_id: str = None,
        template_scratch_type: str = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the scenario.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the scenario. Valid values:
        # 
        # *   GENERATE_IN_PROGRESS: The scenario is being created.
        # *   GENERATE_COMPLETE: The scenario is created.
        # *   GENERATE_FAILED: The scenario fails to be created.
        self.status = status
        # The tags of the scenario.
        self.tags = tags
        # The ID of the scenario.
        self.template_scratch_id = template_scratch_id
        # The type of the resource scenario. Valid values:
        # 
        # *   ArchitectureReplication: resource replication
        # *   ArchitectureDetection: resource detection
        # *   ResourceImport: resource management
        # *   ResourceMigration: resource migration
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        # The parameter name.
        self.parameter_key = parameter_key
        # The parameter value.
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
        # The ID of the source resource group.
        self.resource_group_id = resource_group_id
        # The resource types for filtering resources.
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
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
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
        # The source tags.
        self.resource_tags = resource_tags
        # The resource types for filtering resources.
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
        # The tag key of the resource scenario.
        self.key = key
        # The tag value of the resource scenario.
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
        resource_group_id: str = None,
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
        # The time when the resource scenario was created.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the resource scenario.
        self.description = description
        # The status code of the resource scenario that failed to be generated.
        # 
        # >  This parameter is returned only if the value of Status is GENERATE_FAILED.
        self.failed_code = failed_code
        # The policy based on which the logical ID is generated. Valid values:
        # 
        # *   LongTypePrefixAndIndexSuffix (default): long-type prefix + index-type suffix
        # *   LongTypePrefixAndHashSuffix: long-type prefix + hash-type suffix
        # *   ShortTypePrefixAndHashSuffix: short-type prefix + hash-type suffix
        self.logical_id_strategy = logical_id_strategy
        # The preference parameters of the resource scenario.
        self.preference_parameters = preference_parameters
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The source resource group.
        self.source_resource_group = source_resource_group
        # The source resources.
        self.source_resources = source_resources
        # The source tag.
        self.source_tag = source_tag
        # The state of the resource scenario.
        self.status = status
        # The reason why the resource scenario failed to be generated.
        # 
        # >  This parameter is returned only if the value of Status is GENERATE_FAILED.
        self.status_reason = status_reason
        # The tags of the resource scenario.
        self.tags = tags
        # The ID of the resource scenario.
        self.template_scratch_id = template_scratch_id
        # The type of the resource scenario. Valid values:
        # 
        # *   ResourceImport: resource management
        # *   ArchitectureReplication: resource replication
        self.template_scratch_type = template_scratch_type
        # The time when the resource scenario was updated.
        # 
        # The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The resource scenarios.
        self.template_scratches = template_scratches
        # The total number of scenarios.
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
        # The maximum number of results to be returned in a single call when NextToken is used for the query.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The template ID. This parameter applies to shared and private templates.
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
        # The time when the version was created.
        self.create_time = create_time
        # The description of the version.
        self.description = description
        # The template ID. This parameter applies to shared and private templates. For a shared template, the template ID is the same as the Alibaba Cloud Resource Name (ARN) of the template.
        self.template_id = template_id
        # The template name that corresponds to the specified version.
        self.template_name = template_name
        # The version number.
        # 
        # For a shared template, this parameter is returned only if VersionOption is set to AllVersions.
        # 
        # Valid values: v1 to v100.
        self.template_version = template_version
        # The time when the version was last updated.
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
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The versions.
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
        # The key of the tag. This parameter takes effect only when ShareType is set to Private.
        # 
        # You can specify up to 20 tag keys.
        self.key = key
        # The value of the tag. This parameter takes effect only when ShareType is set to Private.
        # 
        # You can specify up to 20 tag values.
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
        # Specifies whether to query the tag information. Valid values:
        # 
        # *   Enabled
        # *   Disabled (default)
        self.include_tags = include_tags
        # The page number.\
        # Pages start from page 1.\
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.\
        # Valid values: 1 to 50.\
        # Default value: 10.
        self.page_size = page_size
        # The ID of the resource group.\
        # For more information about resource groups, see the "Resource Group" section of [What is Resource Management?](~~94475~~)
        self.resource_group_id = resource_group_id
        # The sharing type of the template.
        # 
        # Valid values:
        # 
        # *   Private (default): The template belongs to the template owner.
        # *   Shared: The template is shared with other users.
        # *   Official: The template is the shared template of the official version.
        self.share_type = share_type
        # The tags. You can specify up to 20 tags.
        self.tag = tag
        # The template name. This parameter takes effect only when ShareType is set to Private. The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (\_). The name must start with a digit or letter.
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
        # The key of the tag.
        self.key = key
        # The value of the tag.
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
        # The time when the template was created.
        self.create_time = create_time
        # The description of the template.
        self.description = description
        # The ID of the Alibaba Cloud account to which the template belongs.
        self.owner_id = owner_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The sharing type of the template.
        # 
        # Valid values:
        # 
        # *   Private: The template belongs to the template owner.
        # *   Shared: The template is shared with other users.
        self.share_type = share_type
        # The tags of the template.
        self.tags = tags
        # The Alibaba Cloud Resource Name (ARN) of the template.
        self.template_arn = template_arn
        # The template ID.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The latest version of the template.
        self.template_version = template_version
        # The time when the template was last updated.
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
        # The page number.\
        # Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The templates.
        self.templates = templates
        # The total number of templates.
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
        # The ID of the resource group to which you want to move the resource. For more information about resource groups, see the "Resource Group" section of the [What is Resource Management?](~~94475~~) topic.
        self.new_resource_group_id = new_resource_group_id
        # The region ID of the resource.\
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   stack: stack
        # *   stackgroup: stack group
        # *   template: template
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
        # The ID of the request.
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
        # The name of the parameter N. If you do not specify the name and value of a parameter, Resource Orchestration Service (ROS) uses the default name and value that are specified in the template. Maximum value of N: 200.
        # 
        # > If you specify Parameters, you must specify Parameters.N.ParameterKey.
        self.parameter_key = parameter_key
        # The value of parameter N. Maximum value of N: 200.
        # 
        # > If you specify Parameters, you must specify Parameters.N.ParameterValue.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can be up to 64 characters in length, and can contain letters, digits, underscores (\_), and hyphens (-).\
        # For more information, see [Ensure idempotence](~~134212~~).
        self.client_token = client_token
        # Specifies whether to disable rollback for the resources when the stack fails to be created. Valid values:
        # 
        # *   true
        # *   false (default)
        self.disable_rollback = disable_rollback
        # Specifies whether to query the parameters that you want to use in compliance precheck.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (default)
        self.enable_pre_config = enable_pre_config
        # The maximum number of concurrent operations that can be performed on resources. This parameter takes effect only for Terraform stacks.
        # 
        # By default, this parameter is empty. You can set this parameter to an integer that is greater than or equal to 0.
        # 
        # > If you set this parameter to an integer greater than 0, the integer is used. If you set this parameter to 0 or leave this parameter empty, the default value of Terraform is used. In most cases, the default value of Terraform is 10.
        self.parallelism = parallelism
        # The parameters of the stack.
        self.parameters = parameters
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The stack ID. You can use this parameter to preview a stack that you want to update.
        # 
        # 
        # 
        # > -  You must and can specify only one of StackName and StackId.
        # > - In the scenario in which you preview a stack that you want to create or update, you cannot preview the resources in its nested stacks.
        self.stack_id = stack_id
        # The stack name. You can use this parameter to preview the stack that you want to create. The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or letter.
        # 
        # > You must and can specify only one of StackName and StackId.
        self.stack_name = stack_name
        # The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length.
        # 
        # > You can specify only one of StackPolicyBody and StackPolicyURL.
        self.stack_policy_body = stack_policy_body
        # The URL of the file that contains the stack policy. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > You can specify only one of StackPolicyBody and StackPolicyURL.
        # 
        # The URL can be up to 1,350 bytes in length.
        self.stack_policy_url = stack_policy_url
        self.template_body = template_body
        # The template ID. This parameter applies to shared and private templates.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_id = template_id
        # The scenario ID.
        # 
        # For more information about how to query the scenario ID, see [ListTemplateScratches](~~363050~~).
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_scratch_id = template_scratch_id
        # The region ID of the scenario. The default value is the same as the value of RegionId.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.template_scratch_region_id = template_scratch_region_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an OSS bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_url = template_url
        # The version of the template. This parameter takes effect only when TemplateId is specified.
        self.template_version = template_version
        # The timeout period for creating the stack.
        # 
        # Unit: minutes.
        # 
        # Default value: 60.
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
        # The name of the Terraform command that is run. Valid values:
        # 
        # *   apply
        # *   plan
        # *   destroy
        # *   version
        # 
        # For more information about Terraform commands, see [Basic CLI Features](https://www.terraform.io/cli/commands).
        self.command = command
        # The content of the output stream that is returned after the command is run.
        self.content = content
        # The output stream. Valid values:
        # 
        # *   stdout: standard output stream
        # *   stderr: standard error stream
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
        # The Terraform logs. This parameter is returned only if the stack is a Terraform stack.
        # 
        # > This parameter contains the logs of previewing the stack.
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
        # The name of the parameter.
        self.parameter_key = parameter_key
        # The value of the parameter.
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
        # The resource type of an Alibaba Cloud service.
        self.acs_resource_type = acs_resource_type
        # The action that is performed on the resource. Valid values:
        # 
        # *   Add
        # *   Modify
        # *   Remove
        # *   None
        self.action = action
        # The description of the resource.
        self.description = description
        # The logical ID of the resource.
        self.logical_resource_id = logical_resource_id
        # The physical ID of the resource.
        # 
        # This parameter is returned only if Action is set to Modify or Remove.
        self.physical_resource_id = physical_resource_id
        # The resource properties.
        self.properties = properties
        # Indicates whether a replacement update is performed on the template. Valid values:
        # 
        # *   True: A replacement update is performed on the template.
        # *   False: A change is made on the template.
        # *   Conditional: A replacement update may be performed on the template. You can check whether a replacement update is performed when the template is in use.
        # 
        # > This parameter is returned only if Action is set to Modify.
        self.replacement = replacement
        # The resources on which the stack depends.
        self.required_by = required_by
        # The resource type.
        self.resource_type = resource_type
        # The information about the nested stack. The data structure of the value is the same as the data structure of the entire response.
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
        # The description of the stack.
        self.description = description
        # Indicates whether rollback is disabled for the resources when the stack fails to be created.
        self.disable_rollback = disable_rollback
        # The log that is generated when the stack is run.
        self.log = log
        # The parameters of the stack.
        self.parameters = parameters
        # The region where the stack resides.
        self.region_id = region_id
        # The resources in the stack.
        self.resources = resources
        # The stack name.
        self.stack_name = stack_name
        # The structure that contains the stack policy body.
        self.stack_policy_body = stack_policy_body
        # The description of the template.
        self.template_description = template_description
        # The timeout period for creating the stack.
        # 
        # Unit: minutes.
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
        # The request ID.
        self.request_id = request_id
        # The information about the stack that is previewed.
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


class RegisterResourceTypeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        entity_type: str = None,
        resource_type: str = None,
        template_body: str = None,
        template_url: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).\
        # For more information, see [Ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The description of the resource type. The description can be up to 512 characters in length.
        self.description = description
        # The entity type. Set the value to Module.
        self.entity_type = entity_type
        # The resource type.
        self.resource_type = resource_type
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. The template body is used as the module content. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # 
        # > - This parameter takes effect only when EntityType is set to Module.
        # > - You can specify only one of the TemplateBody and TemplateURL parameters.
        self.template_body = template_body
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length. The template body is used as the module content.
        # 
        # > - If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # > -  This parameter takes effect only when EntityType is set to Module.
        # > -  You can specify only one of the TemplateBody and TemplateURL parameters.
        # 
        # The URL can be up to 1,024 bytes in length.
        self.template_url = template_url

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
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        return self


class RegisterResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        registration_id: str = None,
        request_id: str = None,
    ):
        # The ID of the registration record. You can call the [ListResourceTypeRegistrations](~~2330740~~) operation to query registration records.
        self.registration_id = registration_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterResourceTypeResponseBody = None,
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
            temp_model = RegisterResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeletionProtectionRequest(TeaModel):
    def __init__(
        self,
        deletion_protection: str = None,
        region_id: str = None,
        stack_id: str = None,
    ):
        # Indicates whether stack deletion protection is enabled. Valid values:
        # 
        # *   Enabled: enables the stack deletion protection.
        # *   Disabled (default): Resource stack deletion protection is Disabled. You can use the console or API(DeleteStack) to release the stack resources.
        # 
        # >  The deletion of nested stacks is the same as the root stack.
        self.deletion_protection = deletion_protection
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the stack.
        # 
        # The delete protection attribute of a nested stack is determined by the root stack and remains unchanged from the root stack.
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
        # The ID of the request.
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


class SetResourceTypeRequest(TeaModel):
    def __init__(
        self,
        default_version_id: str = None,
        description: str = None,
        resource_type: str = None,
        version_id: str = None,
    ):
        # The ID of the default version. You can use this parameter to specify the default version of the resource type.
        # 
        # > You can specify only one of the VersionId and DefaultVersionId parameters.
        self.default_version_id = default_version_id
        # The description of the resource type or resource type version. The description can be up to 512 characters in length.
        self.description = description
        # The resource type.
        self.resource_type = resource_type
        # The version ID. If you want to modify a version of the resource type, you must specify this parameter. If you do not specify this parameter, only the resource type is modified.
        # 
        # > You can specify only one of the VersionId and DefaultVersionId parameters.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_version_id is not None:
            result['DefaultVersionId'] = self.default_version_id
        if self.description is not None:
            result['Description'] = self.description
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersionId') is not None:
            self.default_version_id = m.get('DefaultVersionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class SetResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class SetResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetResourceTypeResponseBody = None,
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
            temp_model = SetResourceTypeResponseBody()
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
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the stack.
        self.stack_id = stack_id
        # The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length.
        # 
        # You can specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them.
        self.stack_policy_body = stack_policy_body
        # The URL for the file that contains the stack policy. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo?RegionId=cn-hangzhou. The template can be up to 16,384 bytes in length, and the URL can be up to 1,350 bytes in length.
        # 
        # >  If the region of the OSS bucket is not specified, the RegionId value is used.
        # 
        # You can specify one of the StackPolicyBody and StackPolicyURL parameters, but you cannot specify both of them.
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
        # The ID of the request.
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
        # The Alibaba Cloud accounts with or from which you want to share or unshare the template.\
        # Valid values of N: 1, 2, 3, 4, and 5.
        # 
        # > - This parameter cannot be set to the ID of the Alibaba Cloud account that owns the template, or the RAM users of this Alibaba Cloud account.
        # > - When ShareOption is set to CancelSharing, you can unshare the template from all the specified Alibaba Cloud accounts by using an asterisk (\*).
        self.account_ids = account_ids
        # The sharing option.
        # 
        # Valid values:
        # 
        # *   ShareToAccounts: shares the template with other Alibaba Cloud accounts.
        # *   CancelSharing: unshares the template.
        self.share_option = share_option
        # The ID of the template.
        self.template_id = template_id
        # The version of the shared template. This parameter takes effect only if you set ShareOption to ShareToAccounts and set VersionOption to Specified.
        # 
        # Valid values: v1 to v100.
        self.template_version = template_version
        # The version option for the shared template. This parameter takes effect only if you set ShareOption to ShareToAccounts.
        # 
        # Valid values:
        # 
        # *   AllVersions (default): shares all versions of the template.
        # *   Latest: shares only the latest version of template. When the version of the template is updated, ROS updates the shared version to the latest version.
        # *   Current: shares only the current version of the template. When the version of the template is updated, ROS does not update the shared version.
        # *   Specified: shares only the specified version of the template.
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
        # The ID of the request.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests.
        # 
        # The token can be up to 64 characters in length and can contain letters, digits, hyphens (-) and underscores (\_).
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The logical ID of the resource as defined in the template.
        self.logical_resource_id = logical_resource_id
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the stack.
        self.stack_id = stack_id
        # The status of the signal. Failure signals can cause stack creation or update to fail. If all signals are warnings, the stack cannot be created or updated. Valid values:
        # 
        # *   SUCCESS
        # *   FAILURE
        # *   WARNING
        self.status = status
        # The unique ID of the signal. The ID must be 1 to 64 characters in length. If multiple signals are sent to a single resource, each signal must have a unique ID.
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
        # The request ID.
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
        # The ID of the operation.
        # 
        # You can call the [ListStackGroupOperations](~~151342~~) operation to obtain the operation ID.
        self.operation_id = operation_id
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
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
        # The ID of the request.
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
        # The tag key of the resource. You can specify up to 20 tag keys.
        # 
        # The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `aliyun` or `acs:`.
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
        # The region ID of the tag that you want to create. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The IDs of the resources.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   stack: stack
        # *   stackgroup: stack group
        # *   template: template
        # *   templatescratch: scenario
        self.resource_type = resource_type
        # The tags of the resource. You can specify up to 20 tags.
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
        # The ID of the request.
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
        # Specifies whether to remove all tags from the resource. This parameter takes effect when TagKey is not specified in the request. Valid values:
        # 
        # *   true
        # *   false (default)
        self.all = all
        # The region ID of the tag. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The IDs of the resource.
        # 
        # > If you set ResourceType to stackgroup, you must set ResourceId to the name of the stack group.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   stack: stack
        # *   stackgroup: stack group
        # *   template: template
        # *   templatescratch: scenario
        self.resource_type = resource_type
        # The tag keys of the resource. You can specify up to 20 tag keys.
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
        # The ID of the request.
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
        # The name of parameter N. If you do not specify the name and value of a parameter, ROS uses the default name and value in the template.
        # 
        # Maximum value of N: 200.
        # 
        # >  The Parameters parameter is optional. If you specify Parameters, you must specify both Parameters.N.ParameterKey and Parameters.N.ParameterValue.
        self.parameter_key = parameter_key
        # The value of parameter N. Maximum value of N: 200.
        # 
        # >  The Parameters parameter is optional. If you specify Parameters, you must specify both Parameters.N.ParameterKey and Parameters.N.ParameterValue.
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
        # The key of tag N that you want to add to the stack.
        # 
        # Valid values of N: 1 to 20.
        # 
        # > - The Tags parameter is optional. If you specify Tags, you must specify Tags.N.Key.
        # > - The tag of a stack is propagated to each resource that supports the tag feature in the stack. For more information, see [Propagate tags](~~201421~~).
        self.key = key
        # The value of tag N that you want to add to the stack.
        # 
        # Valid values of N: 1 to 20.
        # 
        # >  The tag of a stack is propagated to each resource that supports the tag feature in the stack. For more information, see [Propagate tags](~~201421~~).
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
        dry_run_options: List[str] = None,
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests.
        # 
        # The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [Ensure idempotence](~~134212~~).
        self.client_token = client_token
        # Specifies whether to roll back the resources in the stack when the stack fails to be updated.
        # 
        # Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.disable_rollback = disable_rollback
        # Specifies whether only to validate the stack in the request. Default value: false. Valid values:
        # 
        # *   true: only validates the stack.
        # *   false: validates and updates the stack.
        # 
        # >  When no changes are made during the update, the following rules apply: If you set the DryRun parameter to false, the NotSupported error code is returned. If you set the DryRun parameter to true, no error is reported.
        self.dry_run = dry_run
        # The dry run option in the list format. You can specify only one dry run option.
        # 
        # > This parameter takes effect only when DryRun is set to true.
        self.dry_run_options = dry_run_options
        # The maximum number of concurrent operations that can be performed on resources.
        # 
        # By default, this parameter is empty. You can set this parameter to an integer that is greater than or equal to 0.
        # 
        # > - If you set this parameter to an integer that is greater than 0, the integer is used.
        # > -  If you set this parameter to 0, no limit is imposed on Resource Orchestration Service (ROS) stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # > -  If you leave this parameter empty, the value that you specified for this parameter in the previous request is used. If you left this parameter empty in the previous request, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # > - If you set this parameter to a specific value, ROS associates the value with the stack. The value affects subsequent operations on the stack.
        self.parallelism = parallelism
        # The parameters.
        self.parameters = parameters
        # The name of the RAM role. Resource Orchestration Service (ROS) assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.
        # 
        # ROS assumes the RAM role to perform operations on the stack. If you have permissions to perform operations on the stack but do not have permissions to use the RAM role, ROS still assumes the RAM role. You must make sure that the least privileges are granted to the RAM role.
        # 
        # If you do not specify this parameter, ROS assumes the existing RAM role that is associated with the stack. If no RAM roles are available, ROS uses a temporary credential that is generated from the credentials of your account.
        # 
        # The name of the RAM role can be up to 64 bytes in length.
        self.ram_role_name = ram_role_name
        # The ID of the region in which the stack is deployed. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # Specifies whether to enable the replacement update feature. If you cannot change resource properties, you can enable the replacement update feature to replace the resource properties. If the replacement update feature is used, the existing resource is deleted and a new resource is created. The physical ID of the new resource is different from the physical ID of the deleted resource.
        # 
        # Default value: Disabled. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        # 
        # >  Changes have higher priorities than replacement updates.
        self.replacement_option = replacement_option
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the stack.
        self.stack_id = stack_id
        # The structure that contains the stack policy body. The policy body must be 1 to 16,384 bytes in length.
        # 
        # >  You can specify only one of the StackPolicyBody and StackPolicyURL parameters.
        self.stack_policy_body = stack_policy_body
        # The structure that contains the body of the temporary overriding stack policy. The policy body must be 1 to 16,384 bytes in length.
        # 
        # If you want to update protected resources, you must specify a temporary overriding stack policy during the update. If you do not specify a temporary overriding stack policy, the existing policy that is associated with the stack is used.
        # 
        # This parameter takes effect only when the ChangeSetType parameter is set to UPDATE. You can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_during_update_body = stack_policy_during_update_body
        # The URL of the file that contains the temporary overriding stack policy. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an OSS bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length.
        # 
        # >  If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # The URL can be up to 1,350 bytes in length.
        # 
        # If you want to update protected resources, you must specify a temporary overriding stack policy during the update. If you do not specify a temporary overriding stack policy, the existing policy that is associated with the stack is used. This parameter takes effect only when the ChangeSetType parameter is set to UPDATE. You can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_during_update_url = stack_policy_during_update_url
        # The URL of the file that contains the stack policy. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length. If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # >  You can specify only one of the StackPolicyBody and StackPolicyURL parameters.
        # 
        # The URL can be up to 1,350 bytes in length.
        self.stack_policy_url = stack_policy_url
        # The value of tag N that you want to add to the template.
        self.tags = tags
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared templates and private templates.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an OSS bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body must be 1 to 524,288 bytes in length. If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_url = template_url
        # The version of the template. This parameter takes effect only when the TemplateId parameter is specified.
        self.template_version = template_version
        # The timeout period for the update operation on the stack.
        # 
        # *   Default value: 60.
        # *   Unit: minutes.
        self.timeout_in_minutes = timeout_in_minutes
        # Specifies whether to use the values specified in the previous request for the parameters that you do not specify in the current request.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
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
        if self.dry_run_options is not None:
            result['DryRunOptions'] = self.dry_run_options
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
        if m.get('DryRunOptions') is not None:
            self.dry_run_options = m.get('DryRunOptions')
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
        parameters_cause_replacement_if_modified: List[str] = None,
        parameters_conditionally_allowed_to_be_modified: List[str] = None,
        parameters_conditionally_cause_interruption_if_modified: List[str] = None,
        parameters_conditionally_cause_replacement_if_modified: List[str] = None,
        parameters_not_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_cause_interruption_if_modified: List[str] = None,
        parameters_uncertainly_cause_replacement_if_modified: List[str] = None,
    ):
        # The parameters that can be modified. If you change only values of the parameters in a stack template and use the template to update the stack, no validation errors are caused.
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        # The parameters whose changes cause service interruptions.
        # > - This parameter is supported only for a small number of resource types.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_cause_interruption_if_modified = parameters_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources.
        # 
        # > -  This parameter can be returned only if ReplacementOption is set to Enabled.
        # > -  This parameter is valid only for updates on ROS stacks.
        self.parameters_cause_replacement_if_modified = parameters_cause_replacement_if_modified
        # The parameters that can be modified under specific conditions. If you change only values of the parameters in a stack template and use the template to update the stack, the new values of the parameters determine whether validation errors are caused.
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        # The parameters whose changes cause service interruptions under specific conditions.
        # 
        # > - This parameter is supported only for a small number of resource types.
        # > -  This parameter is valid only for updates on ROS stacks.
        self.parameters_conditionally_cause_interruption_if_modified = parameters_conditionally_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources under specific conditions.
        # 
        # > - This parameter can be returned only if ReplacementOption is set to Enabled.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_conditionally_cause_replacement_if_modified = parameters_conditionally_cause_replacement_if_modified
        # The parameters that cannot be modified. If you change only values of the parameters in a stack template and use the template to update the stack, validation errors are caused.
        self.parameters_not_allowed_to_be_modified = parameters_not_allowed_to_be_modified
        # The parameters that can be modified under uncertain conditions. If you change only values of the parameters in a stack template and use the template to update the stack, the actual running environment determines whether validation errors are caused.
        self.parameters_uncertainly_allowed_to_be_modified = parameters_uncertainly_allowed_to_be_modified
        # The parameters whose changes cause service interruptions under uncertain conditions.
        # 
        # > - This parameter is supported only for a small number of resource types.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_uncertainly_cause_interruption_if_modified = parameters_uncertainly_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources under uncertain conditions.
        # 
        # > - This parameter can be returned only if ReplacementOption is set to Enabled.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_uncertainly_cause_replacement_if_modified = parameters_uncertainly_cause_replacement_if_modified

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
        if self.parameters_cause_replacement_if_modified is not None:
            result['ParametersCauseReplacementIfModified'] = self.parameters_cause_replacement_if_modified
        if self.parameters_conditionally_allowed_to_be_modified is not None:
            result['ParametersConditionallyAllowedToBeModified'] = self.parameters_conditionally_allowed_to_be_modified
        if self.parameters_conditionally_cause_interruption_if_modified is not None:
            result['ParametersConditionallyCauseInterruptionIfModified'] = self.parameters_conditionally_cause_interruption_if_modified
        if self.parameters_conditionally_cause_replacement_if_modified is not None:
            result['ParametersConditionallyCauseReplacementIfModified'] = self.parameters_conditionally_cause_replacement_if_modified
        if self.parameters_not_allowed_to_be_modified is not None:
            result['ParametersNotAllowedToBeModified'] = self.parameters_not_allowed_to_be_modified
        if self.parameters_uncertainly_allowed_to_be_modified is not None:
            result['ParametersUncertainlyAllowedToBeModified'] = self.parameters_uncertainly_allowed_to_be_modified
        if self.parameters_uncertainly_cause_interruption_if_modified is not None:
            result['ParametersUncertainlyCauseInterruptionIfModified'] = self.parameters_uncertainly_cause_interruption_if_modified
        if self.parameters_uncertainly_cause_replacement_if_modified is not None:
            result['ParametersUncertainlyCauseReplacementIfModified'] = self.parameters_uncertainly_cause_replacement_if_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParametersAllowedToBeModified') is not None:
            self.parameters_allowed_to_be_modified = m.get('ParametersAllowedToBeModified')
        if m.get('ParametersCauseInterruptionIfModified') is not None:
            self.parameters_cause_interruption_if_modified = m.get('ParametersCauseInterruptionIfModified')
        if m.get('ParametersCauseReplacementIfModified') is not None:
            self.parameters_cause_replacement_if_modified = m.get('ParametersCauseReplacementIfModified')
        if m.get('ParametersConditionallyAllowedToBeModified') is not None:
            self.parameters_conditionally_allowed_to_be_modified = m.get('ParametersConditionallyAllowedToBeModified')
        if m.get('ParametersConditionallyCauseInterruptionIfModified') is not None:
            self.parameters_conditionally_cause_interruption_if_modified = m.get('ParametersConditionallyCauseInterruptionIfModified')
        if m.get('ParametersConditionallyCauseReplacementIfModified') is not None:
            self.parameters_conditionally_cause_replacement_if_modified = m.get('ParametersConditionallyCauseReplacementIfModified')
        if m.get('ParametersNotAllowedToBeModified') is not None:
            self.parameters_not_allowed_to_be_modified = m.get('ParametersNotAllowedToBeModified')
        if m.get('ParametersUncertainlyAllowedToBeModified') is not None:
            self.parameters_uncertainly_allowed_to_be_modified = m.get('ParametersUncertainlyAllowedToBeModified')
        if m.get('ParametersUncertainlyCauseInterruptionIfModified') is not None:
            self.parameters_uncertainly_cause_interruption_if_modified = m.get('ParametersUncertainlyCauseInterruptionIfModified')
        if m.get('ParametersUncertainlyCauseReplacementIfModified') is not None:
            self.parameters_uncertainly_cause_replacement_if_modified = m.get('ParametersUncertainlyCauseReplacementIfModified')
        return self


class UpdateStackResponseBody(TeaModel):
    def __init__(
        self,
        dry_run_result: UpdateStackResponseBodyDryRunResult = None,
        request_id: str = None,
        stack_id: str = None,
    ):
        # The dry run result. This parameter is returned only if DryRun is set to true.
        self.dry_run_result = dry_run_result
        # The ID of the request.
        self.request_id = request_id
        # The ID of the stack.
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
        # The IDs of the members in the resource directory. You can specify a maximum of 20 member IDs.
        # 
        # >  To view the member IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the detailed information of a member](~~111624~~).
        self.enabled = enabled
        # The IDs of the members in the resource directory. You can specify a maximum of 20 member IDs.
        # 
        # >  To view the member IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the detailed information of a member](~~111624~~).
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
        # The list of one or more Alibaba Cloud accounts with which you want to share or unshare the template.
        self.account_ids = account_ids
        # The ID of the operation.
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
        # Specifies whether to retain stacks in a member when you remove the member from the folder.
        # 
        # Valid values:
        # 
        # *   true: retains the stacks.
        # *   false: deletes the stacks.
        # 
        # >  This parameter is required if the Enabled parameter is set to true.
        self.parameter_key = parameter_key
        # The folders in which you want to use service-managed permissions to update stacks.
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
        capabilities: List[str] = None,
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
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Alibaba Cloud Object Storage Service (OSS) bucket. The template body must be 1 to 524,288 bytes in length. Examples: oss://ros/template/demo and oss://ros/template/demo?RegionId=cn-hangzhou. If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # >  You must specify only one of the TemplateBody, TemplateURL, and TemplateId parameters.
        self.account_ids = account_ids
        # The key of parameter N. If you do not specify the key and value of the parameter, ROS uses the default key and value in the template.
        # 
        # Maximum value of N: 200.
        # 
        # >  The Parameters parameter is optional. If you set the Parameters parameter, you must set the Parameters.N.ParameterKey parameter.
        self.administration_role_name = administration_role_name
        # The IDs of the folders in the resource directory. You can specify up to five folder IDs.
        # 
        # You can create stacks within all members in the specified folders. If you create stacks in the Root folder, the stacks are created within all members in the resource directory.
        # 
        # >  To view the folder IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the basic information of a folder](~~111223~~).
        self.auto_deployment = auto_deployment
        # The option for the stack group. You can specify up to one option.
        self.capabilities = capabilities
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # >  You must specify only one of the TemplateBody, TemplateURL, and TemplateId parameters.
        self.client_token = client_token
        # The ID of the request.
        self.deployment_targets = deployment_targets
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # >  You must specify only one of the TemplateBody, TemplateURL, and TemplateId parameters.
        self.description = description
        # The value of parameter N.
        # 
        # Maximum value of N: 200.
        # 
        # >  The Parameters parameter is optional. If you set the Parameters parameter, you must set the Parameters.N.ParameterValue parameter.
        self.execution_role_name = execution_role_name
        # The version of the template. If you do not specify a version, the latest version is used.
        # 
        # >  This parameter takes effect only if the TemplateId parameter is set.
        self.operation_description = operation_description
        # The list of parameters.
        self.operation_preferences = operation_preferences
        # Specifies whether to enable automatic deployment.
        # 
        # Valid values:
        # 
        # *   true: enables automatic deployment. If you add a member to the folder to which the stack group belongs after you enable automatic deployment, the stack group deploys its stack instances within the member. If you remove a member from the folder, the stack group deletes stack instances that are deployed within the member.
        # *   false: disables automatic deployment. After you disable automatic deployment, the stack instances remain unchanged even if members in the folder change.
        self.parameters = parameters
        # The folder IDs in the resource directory. You can specify a maximum of five folder IDs.
        # 
        # You must set at least one of the RdFolderIds and AccountIds parameters. The parameters are subject to the following items:
        # 
        # *   If you set only the RdFolderIds parameter, stacks are deployed within all the members in the specified folders. If you specify the Root folder, ROS deploys the stacks within all the members in the resource directory.
        # *   If you set only the AccountIds parameter, stacks are deployed within the specified members.
        # *   If you set both parameters, the accounts specified by AccountIds must be contained in the folders specified by RdFolderIds.
        # 
        # >  To view the folder IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the basic information of a folder](~~111223~~).
        self.permission_model = permission_model
        # The region IDs of stack instances. You can specify a maximum of 20 region IDs.
        self.region_id = region_id
        # The description of the operation to update the stack group.
        self.region_ids = region_ids
        # The region IDs of stack instances. You can specify a maximum of 20 region IDs.
        self.stack_group_name = stack_group_name
        self.template_body = template_body
        # The permission model.
        # 
        # Valid values:
        # 
        # *   SELF_MANAGED: the self-managed permission model. This is the default value. If you use the self-managed model for the stack group, you must create RAM roles for the administrator and execution accounts, and establish a trust relationship between the accounts to deploy stacks within the execution account.
        # *   SERVICE_MANAGED: the service-managed permission model. If you use the service-managed model for the stack group, ROS creates service-linked roles for the administrator and execution accounts, and the administrator account uses its role to deploy stacks within the execution account.
        # 
        # >- If stack instances have been created in the stack group, you cannot switch the permission mode of the stack group.
        # >- If you want to use the service-managed permission model to deploy stacks, your account must be the management account or a delegated administrator account of your resource directory and the trusted access feature is enabled for the account. For more information, see [Step 1: (Optional) Create a delegated administrator account](~~308253~~) and [Step 2: Enable trusted access](~~298229~~).
        self.template_id = template_id
        # The name of the RAM role to be assumed by the administrator role AliyunROSStackGroupAdministrationRole. This parameter is required if you want to grant self-managed permissions to the stack group. If you do not specify a value for this parameter, the default value AliyunROSStackGroupExecutionRole is used. You can use this role in ROS to perform operations on the stacks that correspond to stack instances in the stack group.
        # 
        # The name must be 1 to 64 characters in length, and can contain letters, digits, and hyphens (-).
        self.template_url = template_url
        # The information about automatic deployment settings.
        # 
        # >  This parameter is required only if the PermissionModel parameter is set to SERVICE_MANAGED.
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
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities
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
        if m.get('Capabilities') is not None:
            self.capabilities = m.get('Capabilities')
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
        # Specifies whether to retain stacks in a member when you remove the member from the folder.
        # 
        # Valid values:
        # 
        # *   true: retains the stacks.
        # *   false: deletes the stacks.
        # 
        # >  This parameter is required if the Enabled parameter is set to true.
        self.parameter_key = parameter_key
        # The folders in which you want to use service-managed permissions to update stacks.
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
        capabilities: List[str] = None,
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
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Alibaba Cloud Object Storage Service (OSS) bucket. The template body must be 1 to 524,288 bytes in length. Examples: oss://ros/template/demo and oss://ros/template/demo?RegionId=cn-hangzhou. If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # >  You must specify only one of the TemplateBody, TemplateURL, and TemplateId parameters.
        self.account_ids_shrink = account_ids_shrink
        # The key of parameter N. If you do not specify the key and value of the parameter, ROS uses the default key and value in the template.
        # 
        # Maximum value of N: 200.
        # 
        # >  The Parameters parameter is optional. If you set the Parameters parameter, you must set the Parameters.N.ParameterKey parameter.
        self.administration_role_name = administration_role_name
        # The IDs of the folders in the resource directory. You can specify up to five folder IDs.
        # 
        # You can create stacks within all members in the specified folders. If you create stacks in the Root folder, the stacks are created within all members in the resource directory.
        # 
        # >  To view the folder IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the basic information of a folder](~~111223~~).
        self.auto_deployment_shrink = auto_deployment_shrink
        # The option for the stack group. You can specify up to one option.
        self.capabilities = capabilities
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # >  You must specify only one of the TemplateBody, TemplateURL, and TemplateId parameters.
        self.client_token = client_token
        # The ID of the request.
        self.deployment_targets_shrink = deployment_targets_shrink
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # >  You must specify only one of the TemplateBody, TemplateURL, and TemplateId parameters.
        self.description = description
        # The value of parameter N.
        # 
        # Maximum value of N: 200.
        # 
        # >  The Parameters parameter is optional. If you set the Parameters parameter, you must set the Parameters.N.ParameterValue parameter.
        self.execution_role_name = execution_role_name
        # The version of the template. If you do not specify a version, the latest version is used.
        # 
        # >  This parameter takes effect only if the TemplateId parameter is set.
        self.operation_description = operation_description
        # The list of parameters.
        self.operation_preferences_shrink = operation_preferences_shrink
        # Specifies whether to enable automatic deployment.
        # 
        # Valid values:
        # 
        # *   true: enables automatic deployment. If you add a member to the folder to which the stack group belongs after you enable automatic deployment, the stack group deploys its stack instances within the member. If you remove a member from the folder, the stack group deletes stack instances that are deployed within the member.
        # *   false: disables automatic deployment. After you disable automatic deployment, the stack instances remain unchanged even if members in the folder change.
        self.parameters = parameters
        # The folder IDs in the resource directory. You can specify a maximum of five folder IDs.
        # 
        # You must set at least one of the RdFolderIds and AccountIds parameters. The parameters are subject to the following items:
        # 
        # *   If you set only the RdFolderIds parameter, stacks are deployed within all the members in the specified folders. If you specify the Root folder, ROS deploys the stacks within all the members in the resource directory.
        # *   If you set only the AccountIds parameter, stacks are deployed within the specified members.
        # *   If you set both parameters, the accounts specified by AccountIds must be contained in the folders specified by RdFolderIds.
        # 
        # >  To view the folder IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the basic information of a folder](~~111223~~).
        self.permission_model = permission_model
        # The region IDs of stack instances. You can specify a maximum of 20 region IDs.
        self.region_id = region_id
        # The description of the operation to update the stack group.
        self.region_ids_shrink = region_ids_shrink
        # The region IDs of stack instances. You can specify a maximum of 20 region IDs.
        self.stack_group_name = stack_group_name
        self.template_body = template_body
        # The permission model.
        # 
        # Valid values:
        # 
        # *   SELF_MANAGED: the self-managed permission model. This is the default value. If you use the self-managed model for the stack group, you must create RAM roles for the administrator and execution accounts, and establish a trust relationship between the accounts to deploy stacks within the execution account.
        # *   SERVICE_MANAGED: the service-managed permission model. If you use the service-managed model for the stack group, ROS creates service-linked roles for the administrator and execution accounts, and the administrator account uses its role to deploy stacks within the execution account.
        # 
        # >- If stack instances have been created in the stack group, you cannot switch the permission mode of the stack group.
        # >- If you want to use the service-managed permission model to deploy stacks, your account must be the management account or a delegated administrator account of your resource directory and the trusted access feature is enabled for the account. For more information, see [Step 1: (Optional) Create a delegated administrator account](~~308253~~) and [Step 2: Enable trusted access](~~298229~~).
        self.template_id = template_id
        # The name of the RAM role to be assumed by the administrator role AliyunROSStackGroupAdministrationRole. This parameter is required if you want to grant self-managed permissions to the stack group. If you do not specify a value for this parameter, the default value AliyunROSStackGroupExecutionRole is used. You can use this role in ROS to perform operations on the stacks that correspond to stack instances in the stack group.
        # 
        # The name must be 1 to 64 characters in length, and can contain letters, digits, and hyphens (-).
        self.template_url = template_url
        # The information about automatic deployment settings.
        # 
        # >  This parameter is required only if the PermissionModel parameter is set to SERVICE_MANAGED.
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
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities
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
        if m.get('Capabilities') is not None:
            self.capabilities = m.get('Capabilities')
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
        # The ID of the operation.
        self.operation_id = operation_id
        # The ID of the request.
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
        # The IDs of the member accounts in the resource directory. You can specify up to 20 member account IDs.
        # 
        # > To view the member account IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the details of a member](~~111624~~).
        self.account_ids = account_ids
        # The folder IDs of the resource directory.
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
        # The key of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the name that you specified when you created the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # > -  ParameterOverrides is optional.
        # > - If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
        self.parameter_key = parameter_key
        # The value of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the value that you specified when you created the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # > -  ParameterOverrides is optional.
        # > - If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
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
        # The IDs of the execution accounts within which you want to deploy stacks in self-managed mode. You can specify up to 20 execution account IDs.
        # 
        # > If you want to update stacks in self-managed permission mode, you must specify this parameter.
        self.account_ids = account_ids
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can contain letters, digits, hyphens (-), and underscores (\_), and cannot exceed 64 characters in length.\
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The folders in which you want to deploy stacks in service-managed mode.
        # 
        # > If you want to update stacks in service-managed permission mode, you must specify this parameter.
        self.deployment_targets = deployment_targets
        # The description of the update operation.
        # 
        # The description must be 1 to 256 characters in length.
        self.operation_description = operation_description
        # The preference settings of the update operation.
        # 
        # The following parameters are available:
        # -  {"FailureToleranceCount": N}
        # 
        #     The number of accounts within which stack operation failures are allowed in each region. If the value of this parameter is exceeded in a region, ROS stops the operation in the region. If ROS stops the operation in one region, ROS stops the operation in other regions.
        # 
        #     Valid values of N: 0 to 20.
        # 
        #     If you do not specify FailureToleranceCount, 0 is used as the default value.
        # 
        # -  {"FailureTolerancePercentage": N}
        # 
        #     The percentage of the number of accounts within which stack operation failures are allowed to the total number of accounts in each region. If the value of this parameter is exceeded, ROS stops the operation in the region.
        # 
        #     Valid values of N: 0 to 100. If the numeric value in the percentage is not an integer, ROS rounds the value down to the nearest integer.
        # 
        #     If you do not specify FailureTolerancePercentage, 0 is used as the default value.
        # 
        # -  {"MaxConcurrentCount": N}
        # 
        #     The maximum number of accounts within which multiple stacks are deployed at the same time in each region.
        # 
        #     Valid values of N: 1 to 20.
        # 
        #     If you do not specify MaxConcurrentCount, 1 is used as the default value.
        # 
        # - {"MaxConcurrentPercentage": N}
        # 
        #     The percentage of the maximum number of accounts within which stacks are deployed at the same time to the total number of accounts in each region.
        # 
        #     Valid values: 1 to 100. If the numeric value in the percentage is not an integer, ROS rounds the value down to the nearest integer.
        # 
        #     If you do not specify MaxConcurrentPercentage, 1 is used as the default value.
        # 
        # - {"RegionConcurrencyType": N}
        # 
        #   The mode that you want to use to deploy stacks across regions. Valid values:
        #   - SEQUENTIAL (default): deploys stacks in the specified regions one by one in sequence. This way, ROS deploys stacks in only one region at a time. 
        # 
        #    - PARALLEL: deploys stacks in all the specified regions in parallel. 
        # 
        # Separate multiple parameters with commas (,).
        # 
        # > - You can specify only one of the following parameters: MaxConcurrentCount and MaxConcurrentPercentage.
        # > - You can specify only one of the following parameters: FailureToleranceCount and FailureTolerancePercentage.
        self.operation_preferences = operation_preferences
        # The parameters that are used to override specific parameters.
        self.parameter_overrides = parameter_overrides
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The IDs of the regions where you want to update the stacks. You can specify up to 20 region IDs.
        self.region_ids = region_ids
        # The name of the stack group. The name must be unique within a region.\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or a letter.
        self.stack_group_name = stack_group_name
        # The timeout period for the update operation.
        # 
        # *   Default value: 60.
        # *   Unit: minutes.
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
        # The key of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the name that you specified when you created the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # > -  ParameterOverrides is optional.
        # > - If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
        self.parameter_key = parameter_key
        # The value of parameter N that you want to use to override a specific parameter. If you do not specify this parameter, ROS uses the value that you specified when you created the stack group.
        # 
        # Maximum value of N: 200.
        # 
        # > -  ParameterOverrides is optional.
        # > - If you specify ParameterOverrides, you must specify ParameterOverrides.N.ParameterKey and ParameterOverrides.N.ParameterValue.
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
        # The IDs of the execution accounts within which you want to deploy stacks in self-managed mode. You can specify up to 20 execution account IDs.
        # 
        # > If you want to update stacks in self-managed permission mode, you must specify this parameter.
        self.account_ids_shrink = account_ids_shrink
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\
        # The token can contain letters, digits, hyphens (-), and underscores (\_), and cannot exceed 64 characters in length.\
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The folders in which you want to deploy stacks in service-managed mode.
        # 
        # > If you want to update stacks in service-managed permission mode, you must specify this parameter.
        self.deployment_targets_shrink = deployment_targets_shrink
        # The description of the update operation.
        # 
        # The description must be 1 to 256 characters in length.
        self.operation_description = operation_description
        # The preference settings of the update operation.
        # 
        # The following parameters are available:
        # -  {"FailureToleranceCount": N}
        # 
        #     The number of accounts within which stack operation failures are allowed in each region. If the value of this parameter is exceeded in a region, ROS stops the operation in the region. If ROS stops the operation in one region, ROS stops the operation in other regions.
        # 
        #     Valid values of N: 0 to 20.
        # 
        #     If you do not specify FailureToleranceCount, 0 is used as the default value.
        # 
        # -  {"FailureTolerancePercentage": N}
        # 
        #     The percentage of the number of accounts within which stack operation failures are allowed to the total number of accounts in each region. If the value of this parameter is exceeded, ROS stops the operation in the region.
        # 
        #     Valid values of N: 0 to 100. If the numeric value in the percentage is not an integer, ROS rounds the value down to the nearest integer.
        # 
        #     If you do not specify FailureTolerancePercentage, 0 is used as the default value.
        # 
        # -  {"MaxConcurrentCount": N}
        # 
        #     The maximum number of accounts within which multiple stacks are deployed at the same time in each region.
        # 
        #     Valid values of N: 1 to 20.
        # 
        #     If you do not specify MaxConcurrentCount, 1 is used as the default value.
        # 
        # - {"MaxConcurrentPercentage": N}
        # 
        #     The percentage of the maximum number of accounts within which stacks are deployed at the same time to the total number of accounts in each region.
        # 
        #     Valid values: 1 to 100. If the numeric value in the percentage is not an integer, ROS rounds the value down to the nearest integer.
        # 
        #     If you do not specify MaxConcurrentPercentage, 1 is used as the default value.
        # 
        # - {"RegionConcurrencyType": N}
        # 
        #   The mode that you want to use to deploy stacks across regions. Valid values:
        #   - SEQUENTIAL (default): deploys stacks in the specified regions one by one in sequence. This way, ROS deploys stacks in only one region at a time. 
        # 
        #    - PARALLEL: deploys stacks in all the specified regions in parallel. 
        # 
        # Separate multiple parameters with commas (,).
        # 
        # > - You can specify only one of the following parameters: MaxConcurrentCount and MaxConcurrentPercentage.
        # > - You can specify only one of the following parameters: FailureToleranceCount and FailureTolerancePercentage.
        self.operation_preferences_shrink = operation_preferences_shrink
        # The parameters that are used to override specific parameters.
        self.parameter_overrides = parameter_overrides
        # The region ID of the stack group. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The IDs of the regions where you want to update the stacks. You can specify up to 20 region IDs.
        self.region_ids_shrink = region_ids_shrink
        # The name of the stack group. The name must be unique within a region.\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or a letter.
        self.stack_group_name = stack_group_name
        # The timeout period for the update operation.
        # 
        # *   Default value: 60.
        # *   Unit: minutes.
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
        # The ID of the operation.
        self.operation_id = operation_id
        # The ID of the request.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests.
        # 
        # The token can be up to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # Specifies whether to only preview the corrected template in this request. Default value: false. Valid values:
        # 
        # *   true: returns the content of the corrected template and does not correct the template. After Resource Orchestration Service (ROS) compares the corrected template with the original template, ROS determines whether to execute the correction.
        # *   false: corrects the template to eliminate drift.
        # 
        # >  We recommend that you set the DryRun parameter to true to preview the corrected template. If the template content meets expectations, set the DryRun parameter to false to execute the correction.
        self.dry_run = dry_run
        # The logical ID of resource.
        self.logical_resource_id = logical_resource_id
        # The region ID of the stack. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the stack.
        self.stack_id = stack_id
        # The format of the returned template. Default value: JSON. Valid values:
        # 
        # *   JSON
        # *   YAML
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
        # The template content after correction.
        self.new_template_body = new_template_body
        # The template content before correction.
        self.old_template_body = old_template_body
        # The ID of the request.
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
        # The description of the template. It can be up to 256 characters in length.
        self.description = description
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared and private templates.
        self.template_id = template_id
        # The name of the template.
        # 
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\_). It must start with a digit or letter.
        self.template_name = template_name
        # The URL of the file that contains the template body. The URL must point to a template located in an HTTP or HTTPS web server or an Alibaba Cloud OSS bucket. Examples: oss://ros/template/demo and oss://ros/template/demo?RegionId=cn-hangzhou. The template can be up to 524,288 bytes in length, and the URL can be up to 1,024 bytes in length.
        # 
        # >  If the region of the OSS bucket is not specified, the RegionId value is used.
        # 
        # You can specify only one of the TemplateBody and TemplateURL parameters.
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
        # The ID of the request.
        self.request_id = request_id
        # The ID of the template.
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
        # The parameter name.
        # 
        # For more information about the valid values of ParameterKey, see the "**Additional information about request parameters**" section of this topic.
        # 
        # >- PreferenceParameters is optional. If you specify PreferenceParameters, you must specify both ParameterKey and ParameterValue.
        # > - If you set TemplateScratchType to ResourceImport, you must set ParameterKey to DeletionPolicy.
        self.parameter_key = parameter_key
        # The parameter value. The value of ParameterValue varies based on the value of ParameterKey.
        # 
        # For more information about the valid values of ParameterKey, see the "**Additional information about request parameters**" section of this topic.
        # 
        # >  PreferenceParameters is optional. If you specify PreferenceParameters, you must specify both ParameterKey and ParameterValue.
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
        # The ID of the source resource group.
        self.resource_group_id = resource_group_id
        # The resource types.
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
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
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
        # The source tags that consist of key-value pairs.
        # 
        # If you want to specify only the tag key, you must set the tag value to an empty string. Example: {"TagKey": ""}.
        # 
        # If you set TemplateScratchType to ArchitectureDetection, you can add up to five source tags. In other cases, you can add up to 10 source tags.
        self.resource_tags = resource_tags
        # The resource types for filtering resources.
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
        resource_group_id: str = None,
        source_resource_group: UpdateTemplateScratchRequestSourceResourceGroup = None,
        source_resources: List[UpdateTemplateScratchRequestSourceResources] = None,
        source_tag: UpdateTemplateScratchRequestSourceTag = None,
        template_scratch_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The description of the scenario.
        self.description = description
        # The execution mode. Valid values:
        # 
        # *   Async (default)
        # *   Sync
        # 
        # > If you have a wide scope of resources, Sync takes longer. If you set ExecutionMode to Sync, we recommend that you specify ClientToken to prevent the execution timeout.
        self.execution_mode = execution_mode
        # The policy based on which the logical ID is generated. Valid values:
        # 
        # *   LongTypePrefixAndIndexSuffix: long-type prefix + index-type suffix
        # *   LongTypePrefixAndHashSuffix: long-type prefix + hash-type suffix
        # *   ShortTypePrefixAndHashSuffix: short-type prefix + hash-type suffix
        # 
        # >  If you set TemplateScratchType to ArchitectureDetection, the default value of LogicalIdStrategy is LongTypePrefixAndHashSuffix. In other cases, the default value of LogicalIdStrategy is LongTypePrefixAndIndexSuffix.
        self.logical_id_strategy = logical_id_strategy
        # The preference parameters of the resource scenario.
        self.preference_parameters = preference_parameters
        # The region ID of the scenario.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The source resource group.
        self.source_resource_group = source_resource_group
        # The source resources.
        # 
        # If you specify SourceResources when TemplateScratchType is set to ArchitectureDetection, the system detects the architecture of all resources that are associated with the specified source resources. For example, if you set the value of SourceResources to an ID of a Classic Load Balancer (CLB) instance, the system detects the architecture of resources, such as Elastic Compute Service (ECS) instances, vSwitches, and virtual private clouds (VPCs), that are associated with the CLB instance.
        # 
        # If you set TemplateScratchType to ArchitectureDetection, you can specify up to 20 source resources for SourceResources. In other cases, you can specify up to 200 source resources.
        self.source_resources = source_resources
        # The source tag.
        self.source_tag = source_tag
        # The ID of the scenario.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        resource_group_id: str = None,
        source_resource_group_shrink: str = None,
        source_resources_shrink: str = None,
        source_tag_shrink: str = None,
        template_scratch_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # For more information, see [How to ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The description of the scenario.
        self.description = description
        # The execution mode. Valid values:
        # 
        # *   Async (default)
        # *   Sync
        # 
        # > If you have a wide scope of resources, Sync takes longer. If you set ExecutionMode to Sync, we recommend that you specify ClientToken to prevent the execution timeout.
        self.execution_mode = execution_mode
        # The policy based on which the logical ID is generated. Valid values:
        # 
        # *   LongTypePrefixAndIndexSuffix: long-type prefix + index-type suffix
        # *   LongTypePrefixAndHashSuffix: long-type prefix + hash-type suffix
        # *   ShortTypePrefixAndHashSuffix: short-type prefix + hash-type suffix
        # 
        # >  If you set TemplateScratchType to ArchitectureDetection, the default value of LogicalIdStrategy is LongTypePrefixAndHashSuffix. In other cases, the default value of LogicalIdStrategy is LongTypePrefixAndIndexSuffix.
        self.logical_id_strategy = logical_id_strategy
        # The preference parameters of the resource scenario.
        self.preference_parameters_shrink = preference_parameters_shrink
        # The region ID of the scenario.
        # 
        # You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The source resource group.
        self.source_resource_group_shrink = source_resource_group_shrink
        # The source resources.
        # 
        # If you specify SourceResources when TemplateScratchType is set to ArchitectureDetection, the system detects the architecture of all resources that are associated with the specified source resources. For example, if you set the value of SourceResources to an ID of a Classic Load Balancer (CLB) instance, the system detects the architecture of resources, such as Elastic Compute Service (ECS) instances, vSwitches, and virtual private clouds (VPCs), that are associated with the CLB instance.
        # 
        # If you set TemplateScratchType to ArchitectureDetection, you can specify up to 20 source resources for SourceResources. In other cases, you can specify up to 200 source resources.
        self.source_resources_shrink = source_resources_shrink
        # The source tag.
        self.source_tag_shrink = source_tag_shrink
        # The ID of the scenario.
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        # The ID of the request.
        self.request_id = request_id
        # The ID of the scenario.
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
        update_info_options: List[str] = None,
        validation_option: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        # 
        # For more information, see [Ensure idempotence](~~134212~~).
        self.client_token = client_token
        # The region ID of the template. You can call the [DescribeRegions](~~131035~~) operation to query the most recent region list.
        self.region_id = region_id
        self.template_body = template_body
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length.
        # 
        # > If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # You can specify one of TemplateBody and TemplateURL, but not both of them. The URL can be up to 1,024 bytes in length.\
        self.template_url = template_url
        # The options that are used to control the generation of information about the stack update. You can specify up to two options.
        self.update_info_options = update_info_options
        # Specifies whether to enable additional validation for the template. Valid values:
        # 
        # *   None (default): does not enable additional validation.
        # *   EnableTerraformValidation: runs the `terraform validate` command in the Terraform CLI to enable additional validation for a Terraform template.
        # *   EnableFastTerraformValidation: runs a command that is similar to the `terraform validate` command in the Terraform CLI to enable additional validation for a Terraform template.
        # 
        # > Compared with the EnableTerraformValidation method, the EnableFastTerraformValidation method validates a template at a faster speed but a lower integrity level.
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
        if self.update_info_options is not None:
            result['UpdateInfoOptions'] = self.update_info_options
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
        if m.get('UpdateInfoOptions') is not None:
            self.update_info_options = m.get('UpdateInfoOptions')
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
        # The description of the template output.
        self.description = description
        # The alias of the template output.
        self.label = label
        # The name of the template output.
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
        # The DataSource resource types that are used in the template. The value is deduplicated.
        self.data_sources = data_sources
        # The regular resource types that are used in the template. The value is deduplicated.
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
        # The pattern in which the logical IDs of regular resources are formed.
        # 
        # If resources are defined in a ROS template, the following rules apply:
        # 
        # *   Resource whose definition does not contain `Count`: If the resource name defined in the template is `server`, the values of LogicalResourceIdPattern and `ResourcePath` are both `server`.``
        # *   Resource whose definition contains `Count`: If the resource name defined in the template is `server`, the value of LogicalResourceIdPattern is `server[*]`, and the value of `ResourcePath` is `server`.
        # 
        # If resources and [modules](https://www.terraform.io/language/modules) are defined in a Terraform template, the following rules apply:
        # 
        # *   Resource and module whose definitions do not contain [`count`](https://www.terraform.io/language/meta-arguments/count) or [`for_each`](https://www.terraform.io/language/meta-arguments/for_each): If the resource name defined in the template is `server`, the values of LogicalResourceIdPattern and `ResourcePath` are both `server`.``
        # *   Resource and module whose definitions contain [`count`](https://www.terraform.io/language/meta-arguments/count) or [`for_each`](https://www.terraform.io/language/meta-arguments/for_each): If the resource name defined in the template is `server`, the value of LogicalResourceIdPattern is `server[*]`, and the value of `ResourcePath` is `server`.
        # 
        # Examples of LogicalResourceIdPattern for resources in a Terraform template:
        # 
        # *   Valid values of LogicalResourceIdPattern if a resource belongs to the root module:
        # 
        #     *   `server`: In this case, `count` and `for_each` are not contained in the resource. The value of `ResourcePath` is `server`.
        #     *   `server[*]`: In this case, `count` or `for_each` is contained in the resource. The value of `ResourcePath` is `server`.
        # 
        # *   Valid values of LogicalResourceIdPattern if a resource belongs to a child module:
        # 
        #     *   `app.server`: In this case, `count` and `for_each` are not contained in the `app` module and the `server` resource. The value of `ResourcePath` is `app.server`.````
        #     *   `app.server[*]`: In this case, `count` or `for_each` is contained in the `server` resource, but `count` and `for_each` are not contained in the `app` module. The value of `ResourcePath` is `app.server`.
        #     *   `app[*].server`: In this case, `count` or `for_each` is contained in the `app` module, but `count` and `for_each` are not contained in the `server` resource. The value of `ResourcePath` is `app.server`.
        #     *   `app[*].server[*]`: In this case, `count` or `for_each` is contained in the `app` module and the `server` resource. The value of `ResourcePath` is `app.server`.````
        #     *   `app.app_group[*].server`: In this case, `count` or `for_each` is contained in the `app_group` module, but `count` and `for_each` are not contained in the `app` module and the `server` resource. The value of `ResourcePath` is `app.app_group.server`. The `app_group` module is a child module of the `app` module.````
        self.logical_resource_id_pattern = logical_resource_id_pattern
        # The path of the regular resource. In most cases, the path of a regular resource is the same as the resource name.
        self.resource_path = resource_path
        # The regular resource type.
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
        parameters_cause_replacement_if_modified: List[str] = None,
        parameters_conditionally_allowed_to_be_modified: List[str] = None,
        parameters_conditionally_cause_interruption_if_modified: List[str] = None,
        parameters_conditionally_cause_replacement_if_modified: List[str] = None,
        parameters_not_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_allowed_to_be_modified: List[str] = None,
        parameters_uncertainly_cause_interruption_if_modified: List[str] = None,
        parameters_uncertainly_cause_replacement_if_modified: List[str] = None,
    ):
        # The parameters that can be modified.
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        # The parameters whose changes cause service interruptions.
        # 
        # > - This parameter is supported only for a small number of resource types.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_cause_interruption_if_modified = parameters_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources.
        # 
        # > -  This parameter can be returned only if the value of UpdateInfoOptions contains EnableReplacement.
        # > -  This parameter is valid only for updates on ROS stacks.
        self.parameters_cause_replacement_if_modified = parameters_cause_replacement_if_modified
        # The parameters that can be modified under specific conditions.
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        # The parameters whose changes cause service interruptions under specific conditions.
        # 
        # > - This parameter is supported only for a small number of resource types.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_conditionally_cause_interruption_if_modified = parameters_conditionally_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources under specific conditions.
        # 
        # > - This parameter can be returned only if the value of UpdateInfoOptions contains EnableReplacement.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_conditionally_cause_replacement_if_modified = parameters_conditionally_cause_replacement_if_modified
        # The parameters that cannot be modified.
        self.parameters_not_allowed_to_be_modified = parameters_not_allowed_to_be_modified
        # The parameters that can be modified under uncertain conditions.
        self.parameters_uncertainly_allowed_to_be_modified = parameters_uncertainly_allowed_to_be_modified
        # The parameters whose changes cause service interruptions under uncertain conditions.
        # 
        # > - This parameter is supported only for a small number of resource types.
        # > - This parameter is valid only for updates on ROS stacks.
        self.parameters_uncertainly_cause_interruption_if_modified = parameters_uncertainly_cause_interruption_if_modified
        # The parameters whose changes trigger replacement updates for resources under uncertain conditions.
        # 
        # > -  This parameter can be returned only if the value of UpdateInfoOptions contains EnableReplacement.
        # > -  This parameter is valid only for updates on ROS stacks.
        self.parameters_uncertainly_cause_replacement_if_modified = parameters_uncertainly_cause_replacement_if_modified

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
        if self.parameters_cause_replacement_if_modified is not None:
            result['ParametersCauseReplacementIfModified'] = self.parameters_cause_replacement_if_modified
        if self.parameters_conditionally_allowed_to_be_modified is not None:
            result['ParametersConditionallyAllowedToBeModified'] = self.parameters_conditionally_allowed_to_be_modified
        if self.parameters_conditionally_cause_interruption_if_modified is not None:
            result['ParametersConditionallyCauseInterruptionIfModified'] = self.parameters_conditionally_cause_interruption_if_modified
        if self.parameters_conditionally_cause_replacement_if_modified is not None:
            result['ParametersConditionallyCauseReplacementIfModified'] = self.parameters_conditionally_cause_replacement_if_modified
        if self.parameters_not_allowed_to_be_modified is not None:
            result['ParametersNotAllowedToBeModified'] = self.parameters_not_allowed_to_be_modified
        if self.parameters_uncertainly_allowed_to_be_modified is not None:
            result['ParametersUncertainlyAllowedToBeModified'] = self.parameters_uncertainly_allowed_to_be_modified
        if self.parameters_uncertainly_cause_interruption_if_modified is not None:
            result['ParametersUncertainlyCauseInterruptionIfModified'] = self.parameters_uncertainly_cause_interruption_if_modified
        if self.parameters_uncertainly_cause_replacement_if_modified is not None:
            result['ParametersUncertainlyCauseReplacementIfModified'] = self.parameters_uncertainly_cause_replacement_if_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParametersAllowedToBeModified') is not None:
            self.parameters_allowed_to_be_modified = m.get('ParametersAllowedToBeModified')
        if m.get('ParametersCauseInterruptionIfModified') is not None:
            self.parameters_cause_interruption_if_modified = m.get('ParametersCauseInterruptionIfModified')
        if m.get('ParametersCauseReplacementIfModified') is not None:
            self.parameters_cause_replacement_if_modified = m.get('ParametersCauseReplacementIfModified')
        if m.get('ParametersConditionallyAllowedToBeModified') is not None:
            self.parameters_conditionally_allowed_to_be_modified = m.get('ParametersConditionallyAllowedToBeModified')
        if m.get('ParametersConditionallyCauseInterruptionIfModified') is not None:
            self.parameters_conditionally_cause_interruption_if_modified = m.get('ParametersConditionallyCauseInterruptionIfModified')
        if m.get('ParametersConditionallyCauseReplacementIfModified') is not None:
            self.parameters_conditionally_cause_replacement_if_modified = m.get('ParametersConditionallyCauseReplacementIfModified')
        if m.get('ParametersNotAllowedToBeModified') is not None:
            self.parameters_not_allowed_to_be_modified = m.get('ParametersNotAllowedToBeModified')
        if m.get('ParametersUncertainlyAllowedToBeModified') is not None:
            self.parameters_uncertainly_allowed_to_be_modified = m.get('ParametersUncertainlyAllowedToBeModified')
        if m.get('ParametersUncertainlyCauseInterruptionIfModified') is not None:
            self.parameters_uncertainly_cause_interruption_if_modified = m.get('ParametersUncertainlyCauseInterruptionIfModified')
        if m.get('ParametersUncertainlyCauseReplacementIfModified') is not None:
            self.parameters_uncertainly_cause_replacement_if_modified = m.get('ParametersUncertainlyCauseReplacementIfModified')
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
        # The description of the template.
        self.description = description
        # The outputs of the template.
        self.outputs = outputs
        # The parameters that are defined in the Parameters section of the template.
        self.parameters = parameters
        # The request ID.
        self.request_id = request_id
        # The resource types that are used in the template.
        self.resource_types = resource_types
        # The regular resources that are defined in the template.
        # 
        # > - For a Resource Orchestration Service (ROS) template, the resource whose definition contains `Count` is not displayed as a list.
        # > -  For a Terraform template, the resource whose definition contains `count` or `for_each` is not displayed as a list.
        self.resources = resources
        # The information about the stack update. This parameter cannot be returned if the value of UpdateInfoOptions contains Disabled.
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


