# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class CreateFlowRequestEnvironmentVariables(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
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
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateFlowRequestEnvironment(TeaModel):
    def __init__(
        self,
        variables: List[CreateFlowRequestEnvironmentVariables] = None,
    ):
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = CreateFlowRequestEnvironmentVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class CreateFlowRequest(TeaModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        environment: CreateFlowRequestEnvironment = None,
        execution_mode: str = None,
        external_storage_location: str = None,
        name: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # The definition of the workflow. The definition must comply with the flow definition language (FDL) syntax. Considering compatibility, the system supports two flow definition specifications.
        # 
        # >  In the preceding flow definition example, Name:my_flow_name is the workflow name, which must be consistent with the input parameter Name
        # 
        # This parameter is required.
        self.definition = definition
        # The description of the flow.
        # 
        # This parameter is required.
        self.description = description
        self.environment = environment
        # The execution mode. Valid values: Express and Standard. Considering compatibility, an empty string is equivalent to the Standard execution mode.
        self.execution_mode = execution_mode
        # The path of the external storage.
        self.external_storage_location = external_storage_location
        # The name of the flow. The name is unique within the same region and cannot be modified after the flow is created. Set this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The Alibaba Cloud resource name (ARN) of the authorized role on which the execution of the flow relies. During the execution of the flow, CloudFlow assumes the role to call API operations of relevant services.
        self.role_arn = role_arn
        # The type of the flow. Set this parameter to **FDL**.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment.to_map()
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.external_storage_location is not None:
            result['ExternalStorageLocation'] = self.external_storage_location
        if self.name is not None:
            result['Name'] = self.name
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            temp_model = CreateFlowRequestEnvironment()
            self.environment = temp_model.from_map(m['Environment'])
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('ExternalStorageLocation') is not None:
            self.external_storage_location = m.get('ExternalStorageLocation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        environment_shrink: str = None,
        execution_mode: str = None,
        external_storage_location: str = None,
        name: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # The definition of the workflow. The definition must comply with the flow definition language (FDL) syntax. Considering compatibility, the system supports two flow definition specifications.
        # 
        # >  In the preceding flow definition example, Name:my_flow_name is the workflow name, which must be consistent with the input parameter Name
        # 
        # This parameter is required.
        self.definition = definition
        # The description of the flow.
        # 
        # This parameter is required.
        self.description = description
        self.environment_shrink = environment_shrink
        # The execution mode. Valid values: Express and Standard. Considering compatibility, an empty string is equivalent to the Standard execution mode.
        self.execution_mode = execution_mode
        # The path of the external storage.
        self.external_storage_location = external_storage_location
        # The name of the flow. The name is unique within the same region and cannot be modified after the flow is created. Set this parameter based on the following rules:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The Alibaba Cloud resource name (ARN) of the authorized role on which the execution of the flow relies. During the execution of the flow, CloudFlow assumes the role to call API operations of relevant services.
        self.role_arn = role_arn
        # The type of the flow. Set this parameter to **FDL**.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.environment_shrink is not None:
            result['Environment'] = self.environment_shrink
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.external_storage_location is not None:
            result['ExternalStorageLocation'] = self.external_storage_location
        if self.name is not None:
            result['Name'] = self.name
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment_shrink = m.get('Environment')
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('ExternalStorageLocation') is not None:
            self.external_storage_location = m.get('ExternalStorageLocation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFlowResponseBodyEnvironmentVariables(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
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
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateFlowResponseBodyEnvironment(TeaModel):
    def __init__(
        self,
        variables: List[CreateFlowResponseBodyEnvironmentVariables] = None,
    ):
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = CreateFlowResponseBodyEnvironmentVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        definition: str = None,
        description: str = None,
        environment: CreateFlowResponseBodyEnvironment = None,
        execution_mode: str = None,
        id: str = None,
        last_modified_time: str = None,
        name: str = None,
        request_id: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # The time when the flow was created.
        self.created_time = created_time
        # Considering compatibility, the system supports two flow definition specifications.
        self.definition = definition
        # The description of the flow.
        self.description = description
        self.environment = environment
        # The execution mode. Valid values: Express and Standard. Considering compatibility, an empty string is equivalent to the Standard execution mode.
        self.execution_mode = execution_mode
        # The unique ID of the flow.
        self.id = id
        # The time when the flow was last modified.
        self.last_modified_time = last_modified_time
        # The name of the flow.
        self.name = name
        # The request ID. Each time an `HTTP status code` is returned, Serverless Workflow returns a value for the parameter.
        self.request_id = request_id
        # The Alibaba Cloud resource name (ARN) of the authorized role on which the execution of the flow relies. During the execution of the flow, CloudFlow assumes the role to call API operations of relevant services.
        self.role_arn = role_arn
        # The type of the flow.
        # 
        # Valid value:
        # 
        # *   FDL
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.type = type

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment.to_map()
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            temp_model = CreateFlowResponseBodyEnvironment()
            self.environment = temp_model.from_map(m['Environment'])
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowResponseBody = None,
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
            temp_model = CreateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowAliasRequestRoutingConfigurations(TeaModel):
    def __init__(
        self,
        version: str = None,
        weight: int = None,
    ):
        # This parameter is required.
        self.version = version
        # This parameter is required.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateFlowAliasRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        flow_name: str = None,
        name: str = None,
        routing_configurations: List[CreateFlowAliasRequestRoutingConfigurations] = None,
    ):
        self.description = description
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.routing_configurations = routing_configurations

    def validate(self):
        if self.routing_configurations:
            for k in self.routing_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.name is not None:
            result['Name'] = self.name
        result['RoutingConfigurations'] = []
        if self.routing_configurations is not None:
            for k in self.routing_configurations:
                result['RoutingConfigurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.routing_configurations = []
        if m.get('RoutingConfigurations') is not None:
            for k in m.get('RoutingConfigurations'):
                temp_model = CreateFlowAliasRequestRoutingConfigurations()
                self.routing_configurations.append(temp_model.from_map(k))
        return self


class CreateFlowAliasShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        flow_name: str = None,
        name: str = None,
        routing_configurations_shrink: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.routing_configurations_shrink = routing_configurations_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.name is not None:
            result['Name'] = self.name
        if self.routing_configurations_shrink is not None:
            result['RoutingConfigurations'] = self.routing_configurations_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RoutingConfigurations') is not None:
            self.routing_configurations_shrink = m.get('RoutingConfigurations')
        return self


class CreateFlowAliasResponseBodyRoutingConfigurations(TeaModel):
    def __init__(
        self,
        version: str = None,
        weight: int = None,
    ):
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateFlowAliasResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        flow_name: str = None,
        name: str = None,
        request_id: str = None,
        routing_configurations: List[CreateFlowAliasResponseBodyRoutingConfigurations] = None,
    ):
        self.created_time = created_time
        self.description = description
        self.flow_name = flow_name
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.routing_configurations = routing_configurations

    def validate(self):
        if self.routing_configurations:
            for k in self.routing_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RoutingConfigurations'] = []
        if self.routing_configurations is not None:
            for k in self.routing_configurations:
                result['RoutingConfigurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.routing_configurations = []
        if m.get('RoutingConfigurations') is not None:
            for k in m.get('RoutingConfigurations'):
                temp_model = CreateFlowAliasResponseBodyRoutingConfigurations()
                self.routing_configurations.append(temp_model.from_map(k))
        return self


class CreateFlowAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowAliasResponseBody = None,
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
            temp_model = CreateFlowAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduleRequest(TeaModel):
    def __init__(
        self,
        cron_expression: str = None,
        description: str = None,
        enable: bool = None,
        flow_name: str = None,
        payload: str = None,
        schedule_name: str = None,
        signature_version: str = None,
    ):
        # The CRON expression.
        # 
        # This parameter is required.
        self.cron_expression = cron_expression
        # The description of the time-based schedule.
        self.description = description
        # Specifies whether to enable the time-based schedule. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable
        # The name of the workflow that is associated with the time-based schedule.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The trigger message of the time-based schedule. Specify the value in the JSON format.
        self.payload = payload
        # The name of the time-based schedule. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   It is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.schedule_name = schedule_name
        self.signature_version = signature_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        if self.signature_version is not None:
            result['SignatureVersion'] = self.signature_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        if m.get('SignatureVersion') is not None:
            self.signature_version = m.get('SignatureVersion')
        return self


class CreateScheduleResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        cron_expression: str = None,
        description: str = None,
        enable: bool = None,
        last_modified_time: str = None,
        payload: str = None,
        request_id: str = None,
        schedule_id: str = None,
        schedule_name: str = None,
    ):
        # The time when the time-based schedule was created.
        self.created_time = created_time
        # The CRON expression.
        self.cron_expression = cron_expression
        # The description of the time-based schedule.
        self.description = description
        # Indicates whether the time-based schedule is enabled.
        self.enable = enable
        # The time when the time-based schedule was last modified.
        self.last_modified_time = last_modified_time
        # The trigger message of the time-based schedule.
        self.payload = payload
        # The request ID.
        self.request_id = request_id
        # The ID of the time-based schedule.
        self.schedule_id = schedule_id
        # The name of the time-based schedule.
        self.schedule_name = schedule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class CreateScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScheduleResponseBody = None,
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
            temp_model = CreateScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRequest(TeaModel):
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


class DeleteFlowResponseBody(TeaModel):
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


class DeleteFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowResponseBody = None,
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
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowAliasRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteFlowAliasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteFlowAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowAliasResponseBody = None,
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
            temp_model = DeleteFlowAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowVersionRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        flow_version: str = None,
    ):
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.flow_version = flow_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        return self


class DeleteFlowVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
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


class DeleteFlowVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowVersionResponseBody = None,
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
            temp_model = DeleteFlowVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduleRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        schedule_name: str = None,
    ):
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.schedule_name = schedule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class DeleteScheduleResponseBody(TeaModel):
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


class DeleteScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScheduleResponseBody = None,
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
            temp_model = DeleteScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExecutionRequest(TeaModel):
    def __init__(
        self,
        execution_name: str = None,
        flow_name: str = None,
        wait_time_seconds: int = None,
    ):
        # The name of the execution.
        # 
        # This parameter is required.
        self.execution_name = execution_name
        # The name of the workflow.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The maximum period of time for long polling waits. Valid values: 0 to 60. Unit: seconds. Configure this parameter based on the following rules:
        # 
        # *   If the value is 0, the system immediately returns the current execution status.
        # *   If the value is greater than 0, the long polling request waits until the execution ends or the specified period elapses.
        self.wait_time_seconds = wait_time_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.wait_time_seconds is not None:
            result['WaitTimeSeconds'] = self.wait_time_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('WaitTimeSeconds') is not None:
            self.wait_time_seconds = m.get('WaitTimeSeconds')
        return self


class DescribeExecutionResponseBodyEnvironmentVariables(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
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
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeExecutionResponseBodyEnvironment(TeaModel):
    def __init__(
        self,
        variables: List[DescribeExecutionResponseBodyEnvironmentVariables] = None,
    ):
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = DescribeExecutionResponseBodyEnvironmentVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class DescribeExecutionResponseBody(TeaModel):
    def __init__(
        self,
        environment: DescribeExecutionResponseBodyEnvironment = None,
        flow_definition: str = None,
        flow_name: str = None,
        input: str = None,
        name: str = None,
        output: str = None,
        request_id: str = None,
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
    ):
        self.environment = environment
        # The definition of the flow.
        self.flow_definition = flow_definition
        # The name of the flow.
        self.flow_name = flow_name
        # The input of the execution, which is in the JSON format.
        self.input = input
        # The name of the execution.
        self.name = name
        # The execution result, which is in the JSON format.
        self.output = output
        # The request ID.
        self.request_id = request_id
        # The time when the execution started.
        self.started_time = started_time
        # The execution status. Valid values:
        # 
        # *   **Starting**\
        # *   **Running**\
        # *   **Stopped**\
        # *   **Succeeded**\
        # *   **Failed**\
        # *   **TimedOut**\
        self.status = status
        # The time when the execution stopped.
        self.stopped_time = stopped_time

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment.to_map()
        if self.flow_definition is not None:
            result['FlowDefinition'] = self.flow_definition
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.name is not None:
            result['Name'] = self.name
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            temp_model = DescribeExecutionResponseBodyEnvironment()
            self.environment = temp_model.from_map(m['Environment'])
        if m.get('FlowDefinition') is not None:
            self.flow_definition = m.get('FlowDefinition')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')
        return self


class DescribeExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExecutionResponseBody = None,
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
            temp_model = DescribeExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowRequest(TeaModel):
    def __init__(
        self,
        flow_version: str = None,
        name: str = None,
    ):
        self.flow_version = flow_version
        # The name of the flow.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeFlowResponseBodyEnvironmentVariables(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
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
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeFlowResponseBodyEnvironment(TeaModel):
    def __init__(
        self,
        variables: List[DescribeFlowResponseBodyEnvironmentVariables] = None,
    ):
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = DescribeFlowResponseBodyEnvironmentVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class DescribeFlowResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        definition: str = None,
        description: str = None,
        environment: DescribeFlowResponseBodyEnvironment = None,
        execution_mode: str = None,
        id: str = None,
        last_modified_time: str = None,
        name: str = None,
        request_id: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # The time when the flow was created.
        self.created_time = created_time
        # The definition of the workflow. The definition must comply with the flow definition language (FDL) syntax. Considering compatibility, the system supports the flow definition specifications of the old version and new version.
        self.definition = definition
        # The description of the flow.
        self.description = description
        self.environment = environment
        # The execution mode or the enumeration type. Valid values: Express and Standard. A value of Standard indicates an empty string.
        self.execution_mode = execution_mode
        # The unique ID of the flow.
        self.id = id
        # The time when the flow was last modified.
        self.last_modified_time = last_modified_time
        # The name of the flow.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The Alibaba Cloud resource name (ARN) of the authorized role on which the execution of the flow relies. During the execution of the flow, CloudFlow assumes the role to call API operations of relevant services.
        self.role_arn = role_arn
        # The type of the workflow.
        self.type = type

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment.to_map()
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            temp_model = DescribeFlowResponseBodyEnvironment()
            self.environment = temp_model.from_map(m['Environment'])
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFlowResponseBody = None,
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
            temp_model = DescribeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowAliasRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeFlowAliasResponseBodyAliasRoutingConfigurations(TeaModel):
    def __init__(
        self,
        version: str = None,
        weight: int = None,
    ):
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeFlowAliasResponseBodyAlias(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        name: str = None,
        routing_configurations: List[DescribeFlowAliasResponseBodyAliasRoutingConfigurations] = None,
    ):
        self.created_time = created_time
        self.description = description
        self.name = name
        self.routing_configurations = routing_configurations

    def validate(self):
        if self.routing_configurations:
            for k in self.routing_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['RoutingConfigurations'] = []
        if self.routing_configurations is not None:
            for k in self.routing_configurations:
                result['RoutingConfigurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.routing_configurations = []
        if m.get('RoutingConfigurations') is not None:
            for k in m.get('RoutingConfigurations'):
                temp_model = DescribeFlowAliasResponseBodyAliasRoutingConfigurations()
                self.routing_configurations.append(temp_model.from_map(k))
        return self


class DescribeFlowAliasResponseBody(TeaModel):
    def __init__(
        self,
        alias: DescribeFlowAliasResponseBodyAlias = None,
        request_id: str = None,
    ):
        self.alias = alias
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.alias:
            self.alias.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            temp_model = DescribeFlowAliasResponseBodyAlias()
            self.alias = temp_model.from_map(m['Alias'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFlowAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFlowAliasResponseBody = None,
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
            temp_model = DescribeFlowAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMapRunRequest(TeaModel):
    def __init__(
        self,
        execution_name: str = None,
        flow_name: str = None,
        map_run_name: str = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.execution_name = execution_name
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.map_run_name = map_run_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.map_run_name is not None:
            result['MapRunName'] = self.map_run_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('MapRunName') is not None:
            self.map_run_name = m.get('MapRunName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMapRunResponseBodyItemCounts(TeaModel):
    def __init__(
        self,
        aborted: int = None,
        failed: int = None,
        pending: int = None,
        running: int = None,
        succeed: int = None,
        total: int = None,
    ):
        self.aborted = aborted
        self.failed = failed
        self.pending = pending
        self.running = running
        self.succeed = succeed
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aborted is not None:
            result['Aborted'] = self.aborted
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.pending is not None:
            result['Pending'] = self.pending
        if self.running is not None:
            result['Running'] = self.running
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aborted') is not None:
            self.aborted = m.get('Aborted')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Pending') is not None:
            self.pending = m.get('Pending')
        if m.get('Running') is not None:
            self.running = m.get('Running')
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeMapRunResponseBody(TeaModel):
    def __init__(
        self,
        concurrency: int = None,
        execution_name: str = None,
        item_counts: DescribeMapRunResponseBodyItemCounts = None,
        map_run_name: str = None,
        request_id: str = None,
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
        tolerated_failed_count: int = None,
        tolerated_failed_percentage: float = None,
    ):
        self.concurrency = concurrency
        self.execution_name = execution_name
        self.item_counts = item_counts
        self.map_run_name = map_run_name
        self.request_id = request_id
        self.started_time = started_time
        self.status = status
        self.stopped_time = stopped_time
        self.tolerated_failed_count = tolerated_failed_count
        self.tolerated_failed_percentage = tolerated_failed_percentage

    def validate(self):
        if self.item_counts:
            self.item_counts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.item_counts is not None:
            result['ItemCounts'] = self.item_counts.to_map()
        if self.map_run_name is not None:
            result['MapRunName'] = self.map_run_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time
        if self.tolerated_failed_count is not None:
            result['ToleratedFailedCount'] = self.tolerated_failed_count
        if self.tolerated_failed_percentage is not None:
            result['ToleratedFailedPercentage'] = self.tolerated_failed_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('ItemCounts') is not None:
            temp_model = DescribeMapRunResponseBodyItemCounts()
            self.item_counts = temp_model.from_map(m['ItemCounts'])
        if m.get('MapRunName') is not None:
            self.map_run_name = m.get('MapRunName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')
        if m.get('ToleratedFailedCount') is not None:
            self.tolerated_failed_count = m.get('ToleratedFailedCount')
        if m.get('ToleratedFailedPercentage') is not None:
            self.tolerated_failed_percentage = m.get('ToleratedFailedPercentage')
        return self


class DescribeMapRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMapRunResponseBody = None,
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
            temp_model = DescribeMapRunResponseBody()
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


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
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


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
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


class DescribeScheduleRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        schedule_name: str = None,
    ):
        # The name of the flow that is associated with the time-based schedule. The name must be unique within the region and cannot be modified after the time-based schedule is created. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The name of the time-based schedule. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.schedule_name = schedule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class DescribeScheduleResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        cron_expression: str = None,
        description: str = None,
        enable: bool = None,
        last_modified_time: str = None,
        payload: str = None,
        request_id: str = None,
        schedule_id: str = None,
        schedule_name: str = None,
    ):
        # The time when the time-based schedule was created.
        self.created_time = created_time
        # The CRON expression.
        self.cron_expression = cron_expression
        # The description of the time-based schedule.
        self.description = description
        # Indicates whether the time-based schedule is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable
        # The time when the time-based schedule was last modified.
        self.last_modified_time = last_modified_time
        # The trigger message of the time-based schedule.
        self.payload = payload
        # The request ID.
        self.request_id = request_id
        # The ID of the time-based schedule.
        self.schedule_id = schedule_id
        # The name of the time-based schedule.
        self.schedule_name = schedule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class DescribeScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScheduleResponseBody = None,
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
            temp_model = DescribeScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExecutionHistoryRequest(TeaModel):
    def __init__(
        self,
        execution_name: str = None,
        flow_name: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # The name of the execution.
        # 
        # This parameter is required.
        self.execution_name = execution_name
        # The name of the workflow.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The number of workflows that you want to query. Valid values: 1-999. Default value: 60.
        self.limit = limit
        # The name of the event to start the query. You can obtain the value from the response data.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetExecutionHistoryResponseBodyEvents(TeaModel):
    def __init__(
        self,
        event_detail: str = None,
        event_id: int = None,
        schedule_event_id: int = None,
        step_name: str = None,
        time: str = None,
        type: str = None,
    ):
        # The details about the execution step.
        self.event_detail = event_detail
        # The ID of the execution step.
        self.event_id = event_id
        # The ID of the scheduling step.
        self.schedule_event_id = schedule_event_id
        # The name of the execution step.
        self.step_name = step_name
        # The time when the event was updated.
        self.time = time
        # The type of the execution step. Valid values:
        # 
        # *   **StepEntered**\
        # *   **StepStarted**\
        # *   **StepSucceeded**\
        # *   **StepFailed**\
        # *   **StepExited**\
        # *   **BranchEntered**\
        # *   **BranchExited**\
        # *   **IterationEntered**\
        # *   **IterationExited**\
        # *   **TaskScheduled**\
        # *   **TaskStarted**\
        # *   **TaskSubmitted**\
        # *   **TaskSubmitFailed**\
        # *   **TaskSucceeded**\
        # *   **TaskFailed**\
        # *   **TaskTimedOut**\
        # *   **ExecutionStarted**\
        # *   **ExecutionStopped**\
        # *   **ExecutionSucceeded**\
        # *   **ExecutionFailed**\
        # *   **ExecutionTimedOut**\
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_detail is not None:
            result['EventDetail'] = self.event_detail
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.schedule_event_id is not None:
            result['ScheduleEventId'] = self.schedule_event_id
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.time is not None:
            result['Time'] = self.time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventDetail') is not None:
            self.event_detail = m.get('EventDetail')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('ScheduleEventId') is not None:
            self.schedule_event_id = m.get('ScheduleEventId')
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetExecutionHistoryResponseBody(TeaModel):
    def __init__(
        self,
        events: List[GetExecutionHistoryResponseBodyEvents] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The events.
        self.events = events
        # You do not need to specify this parameter for the first request. The returned value of **ScheduleEventId** is used as the token for the next query. No value is returned for the last query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = GetExecutionHistoryResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExecutionHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExecutionHistoryResponseBody = None,
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
            temp_model = GetExecutionHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionsRequest(TeaModel):
    def __init__(
        self,
        execution_name_prefix: str = None,
        flow_name: str = None,
        limit: int = None,
        map_run_name: str = None,
        metadata_only: bool = None,
        next_token: str = None,
        qualifier: str = None,
        started_time_begin: str = None,
        started_time_end: str = None,
        status: str = None,
    ):
        # The name prefix of the execution.
        self.execution_name_prefix = execution_name_prefix
        # The name of the flow. The name must be unique within the region and cannot be modified after the flow is created. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The number of executions that you want to query. Valid values: 1-99. Default value: 60.
        self.limit = limit
        self.map_run_name = map_run_name
        self.metadata_only = metadata_only
        # The name of the execution to start the query. You can obtain the value from the response data. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        self.qualifier = qualifier
        # The beginning of the time range to query executions. Specify the value in the UTC RFC3339 format.
        self.started_time_begin = started_time_begin
        # The end of the time range to query executions. Specify the value in the UTC RFC3339 format.
        self.started_time_end = started_time_end
        # The status of the execution that you want to filter. Valid values:
        # 
        # *   **Starting**\
        # *   **Running**\
        # *   **Stopped**\
        # *   **Succeeded**\
        # *   **Failed**\
        # *   **TimedOut**\
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name_prefix is not None:
            result['ExecutionNamePrefix'] = self.execution_name_prefix
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.map_run_name is not None:
            result['MapRunName'] = self.map_run_name
        if self.metadata_only is not None:
            result['MetadataOnly'] = self.metadata_only
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier
        if self.started_time_begin is not None:
            result['StartedTimeBegin'] = self.started_time_begin
        if self.started_time_end is not None:
            result['StartedTimeEnd'] = self.started_time_end
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionNamePrefix') is not None:
            self.execution_name_prefix = m.get('ExecutionNamePrefix')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MapRunName') is not None:
            self.map_run_name = m.get('MapRunName')
        if m.get('MetadataOnly') is not None:
            self.metadata_only = m.get('MetadataOnly')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')
        if m.get('StartedTimeBegin') is not None:
            self.started_time_begin = m.get('StartedTimeBegin')
        if m.get('StartedTimeEnd') is not None:
            self.started_time_end = m.get('StartedTimeEnd')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListExecutionsResponseBodyExecutionsEnvironmentVariables(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
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
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListExecutionsResponseBodyExecutionsEnvironment(TeaModel):
    def __init__(
        self,
        variables: List[ListExecutionsResponseBodyExecutionsEnvironmentVariables] = None,
    ):
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = ListExecutionsResponseBodyExecutionsEnvironmentVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListExecutionsResponseBodyExecutions(TeaModel):
    def __init__(
        self,
        environment: ListExecutionsResponseBodyExecutionsEnvironment = None,
        flow_definition: str = None,
        flow_name: str = None,
        input: str = None,
        name: str = None,
        output: str = None,
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
    ):
        self.environment = environment
        # The definition of the flow.
        self.flow_definition = flow_definition
        # The name of the flow.
        self.flow_name = flow_name
        # The input of the execution, which is in the JSON format.
        self.input = input
        # The name of the execution.
        self.name = name
        # The output of the execution, which is in the JSON format
        self.output = output
        # The time when the execution started.
        self.started_time = started_time
        # The status of the execution.
        self.status = status
        # The time when the execution stopped.
        self.stopped_time = stopped_time

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment.to_map()
        if self.flow_definition is not None:
            result['FlowDefinition'] = self.flow_definition
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.name is not None:
            result['Name'] = self.name
        if self.output is not None:
            result['Output'] = self.output
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            temp_model = ListExecutionsResponseBodyExecutionsEnvironment()
            self.environment = temp_model.from_map(m['Environment'])
        if m.get('FlowDefinition') is not None:
            self.flow_definition = m.get('FlowDefinition')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')
        return self


class ListExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        executions: List[ListExecutionsResponseBodyExecutions] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about executions.
        self.executions = executions
        # The start key for the next query. This parameter is not returned if this is the last query.
        # 
        # >  This parameter may not be displayed in the response because no next page exists.
        self.next_token = next_token
        # The request ID.
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
                temp_model = ListExecutionsResponseBodyExecutions()
                self.executions.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExecutionsResponseBody = None,
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
            temp_model = ListExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowAliasesRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # This parameter is required.
        self.flow_name = flow_name
        self.limit = limit
        # list token
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListFlowAliasesResponseBodyAliasesRoutingConfigurations(TeaModel):
    def __init__(
        self,
        version: str = None,
        weight: str = None,
    ):
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ListFlowAliasesResponseBodyAliases(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        name: str = None,
        routing_configurations: List[ListFlowAliasesResponseBodyAliasesRoutingConfigurations] = None,
    ):
        self.created_time = created_time
        self.description = description
        self.name = name
        self.routing_configurations = routing_configurations

    def validate(self):
        if self.routing_configurations:
            for k in self.routing_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['RoutingConfigurations'] = []
        if self.routing_configurations is not None:
            for k in self.routing_configurations:
                result['RoutingConfigurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.routing_configurations = []
        if m.get('RoutingConfigurations') is not None:
            for k in m.get('RoutingConfigurations'):
                temp_model = ListFlowAliasesResponseBodyAliasesRoutingConfigurations()
                self.routing_configurations.append(temp_model.from_map(k))
        return self


class ListFlowAliasesResponseBody(TeaModel):
    def __init__(
        self,
        aliases: List[ListFlowAliasesResponseBodyAliases] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.aliases = aliases
        # list token
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.aliases:
            for k in self.aliases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Aliases'] = []
        if self.aliases is not None:
            for k in self.aliases:
                result['Aliases'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aliases = []
        if m.get('Aliases') is not None:
            for k in m.get('Aliases'):
                temp_model = ListFlowAliasesResponseBodyAliases()
                self.aliases.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowAliasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowAliasesResponseBody = None,
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
            temp_model = ListFlowAliasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowVersionsRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        limit: str = None,
        next_token: str = None,
    ):
        # This parameter is required.
        self.flow_name = flow_name
        self.limit = limit
        # list token
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListFlowVersionsResponseBodyFlowVersions(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        version: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListFlowVersionsResponseBody(TeaModel):
    def __init__(
        self,
        flow_versions: List[ListFlowVersionsResponseBodyFlowVersions] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.flow_versions = flow_versions
        # list token
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.flow_versions:
            for k in self.flow_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FlowVersions'] = []
        if self.flow_versions is not None:
            for k in self.flow_versions:
                result['FlowVersions'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_versions = []
        if m.get('FlowVersions') is not None:
            for k in m.get('FlowVersions'):
                temp_model = ListFlowVersionsResponseBodyFlowVersions()
                self.flow_versions.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowVersionsResponseBody = None,
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
            temp_model = ListFlowVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
    ):
        # The number of workflows that you want to query. Valid values: 1 - 999. Default value: 60.
        self.limit = limit
        # The token to start the query.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListFlowsResponseBodyFlowsEnvironmentVariables(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
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
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListFlowsResponseBodyFlowsEnvironment(TeaModel):
    def __init__(
        self,
        variables: List[ListFlowsResponseBodyFlowsEnvironmentVariables] = None,
    ):
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = ListFlowsResponseBodyFlowsEnvironmentVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListFlowsResponseBodyFlows(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        definition: str = None,
        description: str = None,
        environment: ListFlowsResponseBodyFlowsEnvironment = None,
        execution_mode: str = None,
        id: str = None,
        last_modified_time: str = None,
        name: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # The time when the flow was created.
        self.created_time = created_time
        # The definition of the flow. The definition must comply with the Flow Definition Language (FDL) syntax.
        self.definition = definition
        # The description of the flow.
        self.description = description
        self.environment = environment
        # The execution mode or the enumeration type. Valid values: Express and Standard. A value of Standard indicates an empty string.
        self.execution_mode = execution_mode
        # The unique ID of the flow.
        self.id = id
        # The time when the flow was last modified.
        self.last_modified_time = last_modified_time
        # The name of the flow.
        self.name = name
        # The Alibaba Cloud resource name (ARN) of the specified Resource Access Management (RAM) role that Serverless Workflow assumes to invoke resources when the flow is executed.
        self.role_arn = role_arn
        # The type of the flow.
        self.type = type

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment.to_map()
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            temp_model = ListFlowsResponseBodyFlowsEnvironment()
            self.environment = temp_model.from_map(m['Environment'])
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowsResponseBody(TeaModel):
    def __init__(
        self,
        flows: List[ListFlowsResponseBodyFlows] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details of flows.
        self.flows = flows
        # The start key for the next query. This parameter is not returned if all results have been returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = ListFlowsResponseBodyFlows()
                self.flows.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFlowsResponseBody = None,
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
            temp_model = ListFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchedulesRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # The name of the flow that is associated with the time-based schedules. The name is unique within the region and cannot be modified after the flow is created. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The number of schedules that you want to query. Valid values: 1 to 1000.
        self.limit = limit
        # For the first query, you do not need to specify this parameter. The system uses the value of the **FlowName** parameter as the value of the **NextToken** parameter. When the query ends, no value is returned for this parameter.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListSchedulesResponseBodySchedules(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        cron_expression: str = None,
        description: str = None,
        enable: bool = None,
        last_modified_time: str = None,
        payload: str = None,
        schedule_id: str = None,
        schedule_name: str = None,
    ):
        # The time when the time-based schedule was created.
        self.created_time = created_time
        # The cron expression of the scheduled task.
        self.cron_expression = cron_expression
        # The description of the time-based schedule.
        self.description = description
        # Indicates whether the time-based schedule is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable
        # The time when the time-based schedule was last modified.
        self.last_modified_time = last_modified_time
        # The trigger message of the time-based schedule.
        self.payload = payload
        # The ID of the time-based schedule.
        self.schedule_id = schedule_id
        # The name of the time-based schedule.
        self.schedule_name = schedule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class ListSchedulesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        schedules: List[ListSchedulesResponseBodySchedules] = None,
    ):
        # The token for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The time-based schedules that are queried.
        self.schedules = schedules

    def validate(self):
        if self.schedules:
            for k in self.schedules:
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
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = ListSchedulesResponseBodySchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class ListSchedulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSchedulesResponseBody = None,
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
            temp_model = ListSchedulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishFlowVersionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        flow_name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class PublishFlowVersionResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        flow_name: str = None,
        request_id: str = None,
        version: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.flow_name = flow_name
        # Id of the request
        self.request_id = request_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PublishFlowVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishFlowVersionResponseBody = None,
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
            temp_model = PublishFlowVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportTaskFailedRequest(TeaModel):
    def __init__(
        self,
        cause: str = None,
        error: str = None,
        task_token: str = None,
    ):
        # The cause of the failure. The value must be 1 to 4,096 characters in length.
        self.cause = cause
        # The error code for the failed task. The error code must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.error = error
        # The token of the task whose execution you want to report. The task token is passed to the called service, such as Message Service (MNS) or Function Compute. For MNS, the value of this parameter can be obtained from a message. For Function Compute, the value of this parameter can be obtained from an event. For more information, see [Service integration modes](https://help.aliyun.com/document_detail/2592915.html).
        # 
        # This parameter is required.
        self.task_token = task_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.error is not None:
            result['Error'] = self.error
        if self.task_token is not None:
            result['TaskToken'] = self.task_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('TaskToken') is not None:
            self.task_token = m.get('TaskToken')
        return self


class ReportTaskFailedResponseBody(TeaModel):
    def __init__(
        self,
        event_id: int = None,
        request_id: str = None,
    ):
        # The ID of the event.
        self.event_id = event_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportTaskFailedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportTaskFailedResponseBody = None,
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
            temp_model = ReportTaskFailedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportTaskSucceededRequest(TeaModel):
    def __init__(
        self,
        output: str = None,
        task_token: str = None,
    ):
        # The output information of the task whose execution success you want to report.
        # 
        # This parameter is required.
        self.output = output
        # The token of the task whose execution you want to report. The task token is passed to the called service, such as Message Service (MNS) or Function Compute. For MNS, the value of this parameter can be obtained from a message. For Function Compute, the value of this parameter can be obtained from an event. For more information, see [Service integration modes](https://help.aliyun.com/document_detail/2592915.html).
        # 
        # This parameter is required.
        self.task_token = task_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output
        if self.task_token is not None:
            result['TaskToken'] = self.task_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('TaskToken') is not None:
            self.task_token = m.get('TaskToken')
        return self


class ReportTaskSucceededResponseBody(TeaModel):
    def __init__(
        self,
        event_id: int = None,
        request_id: str = None,
    ):
        # The ID of the event.
        self.event_id = event_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportTaskSucceededResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReportTaskSucceededResponseBody = None,
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
            temp_model = ReportTaskSucceededResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartExecutionRequest(TeaModel):
    def __init__(
        self,
        callback_fn_ftask_token: str = None,
        execution_name: str = None,
        flow_name: str = None,
        input: str = None,
        qualifier: str = None,
    ):
        # Specifies that the **TaskToken**-related tasks are called back after the execution in the flow ends.
        self.callback_fn_ftask_token = callback_fn_ftask_token
        # The name of the execution. The execution name is unique within a workflow. Configure this parameter based on the following rules:
        # 
        # *   The name must start with a letter or an underscore (_).
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        self.execution_name = execution_name
        # The name of the workflow to be executed.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The input of the execution, which is in the JSON format.
        self.input = input
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_fn_ftask_token is not None:
            result['CallbackFnFTaskToken'] = self.callback_fn_ftask_token
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackFnFTaskToken') is not None:
            self.callback_fn_ftask_token = m.get('CallbackFnFTaskToken')
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')
        return self


class StartExecutionResponseBody(TeaModel):
    def __init__(
        self,
        flow_definition: str = None,
        flow_name: str = None,
        input: str = None,
        name: str = None,
        output: str = None,
        request_id: str = None,
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
    ):
        # The definition of the flow.
        self.flow_definition = flow_definition
        # The name of the workflow.
        self.flow_name = flow_name
        # The input of the execution, which is in the JSON format.
        self.input = input
        # The name of the execution.
        self.name = name
        # The execution result, which is in the JSON format.
        self.output = output
        # The request ID.
        self.request_id = request_id
        # The time when the execution started.
        self.started_time = started_time
        # The execution status. Valid values:
        # 
        # *   **Starting**\
        # *   **Running**\
        # *   **Stopped**\
        # *   **Succeeded**\
        # *   **Failed**\
        # *   **TimedOut**\
        self.status = status
        # The time when the execution stopped.
        self.stopped_time = stopped_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_definition is not None:
            result['FlowDefinition'] = self.flow_definition
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.name is not None:
            result['Name'] = self.name
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowDefinition') is not None:
            self.flow_definition = m.get('FlowDefinition')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')
        return self


class StartExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartExecutionResponseBody = None,
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
            temp_model = StartExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSyncExecutionRequest(TeaModel):
    def __init__(
        self,
        execution_name: str = None,
        flow_name: str = None,
        input: str = None,
        qualifier: str = None,
    ):
        # The name of the execution that you want to start. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # Different from the StartExecution operation, in the synchronous execution mode, the execution name is no longer required to be unique within a flow. You can choose to provide an execution name to identify the current execution. In this case, the system adds a UUID to the current execution name. The used format is {ExecutionName}:{UUID}. If you do not specify the execution name, the system automatically generates an execution name.
        self.execution_name = execution_name
        # The name of the workflow to be executed.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The input of the execution, which is in the JSON format.
        self.input = input
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')
        return self


class StartSyncExecutionResponseBodyEnvironmentVariables(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
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
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class StartSyncExecutionResponseBodyEnvironment(TeaModel):
    def __init__(
        self,
        variables: List[StartSyncExecutionResponseBodyEnvironmentVariables] = None,
    ):
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = StartSyncExecutionResponseBodyEnvironmentVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class StartSyncExecutionResponseBody(TeaModel):
    def __init__(
        self,
        environment: StartSyncExecutionResponseBodyEnvironment = None,
        error_code: str = None,
        error_message: str = None,
        flow_name: str = None,
        name: str = None,
        output: str = None,
        request_id: str = None,
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
    ):
        self.environment = environment
        # The error code that is returned if the execution failed.
        self.error_code = error_code
        # The error message that indicates the execution timed out.
        self.error_message = error_message
        # The name of the flow.
        self.flow_name = flow_name
        # The name of the execution.
        self.name = name
        # The output of the execution, which is in the JSON format.
        self.output = output
        # The request ID.
        self.request_id = request_id
        # The time when the execution started.
        self.started_time = started_time
        # The status of the execution. Valid values:
        # 
        # *   **Starting**\
        # *   **Running**\
        # *   **Stopped**\
        # *   **Succeeded**\
        # *   **Failed**\
        # *   **TimedOut**\
        self.status = status
        # The time when the execution stopped.
        self.stopped_time = stopped_time

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['Environment'] = self.environment.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.name is not None:
            result['Name'] = self.name
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            temp_model = StartSyncExecutionResponseBodyEnvironment()
            self.environment = temp_model.from_map(m['Environment'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')
        return self


class StartSyncExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartSyncExecutionResponseBody = None,
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
            temp_model = StartSyncExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopExecutionRequest(TeaModel):
    def __init__(
        self,
        cause: str = None,
        error: str = None,
        execution_name: str = None,
        flow_name: str = None,
    ):
        # The reason for stopping the execution. The value must be 1 to 4,096 characters in length.
        self.cause = cause
        # The error code for stopping the execution. The error code must be 1 to 128 characters in length.
        self.error = error
        # The name of the execution to be stopped. You can call the **ListExecutions** operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.execution_name = execution_name
        # The name of the workflow to be stopped. You can call the **ListFlows** operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.flow_name = flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cause is not None:
            result['Cause'] = self.cause
        if self.error is not None:
            result['Error'] = self.error
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        return self


class StopExecutionResponseBody(TeaModel):
    def __init__(
        self,
        flow_definition: str = None,
        flow_name: str = None,
        input: str = None,
        name: str = None,
        output: str = None,
        request_id: str = None,
        role_arn: str = None,
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
    ):
        # The definition of the flow.
        self.flow_definition = flow_definition
        # The name of the flow.
        self.flow_name = flow_name
        # The input of the execution, which is in the JSON format.
        self.input = input
        # The name of the execution.
        self.name = name
        # The execution result, which is in the JSON format.
        self.output = output
        # The request ID.
        self.request_id = request_id
        # The Alibaba Cloud resource name (ARN) of the role that executed the flow. If the RoleArn in the flow definition is changed during the execution of the flow, the system records and returns a snapshot of the original RoleArn.
        # 
        # >  If you do not specify the RoleArn parameter in the request parameters, the response parameters do not contain the RoleArn parameter.
        self.role_arn = role_arn
        # The time when the execution started.
        self.started_time = started_time
        # The execution status. Valid values:
        # 
        # *   **Starting**\
        # *   **Running**\
        # *   **Stopped**\
        # *   **Succeeded**\
        # *   **Failed**\
        # *   **TimedOut**\
        self.status = status
        # The time when the execution stopped.
        self.stopped_time = stopped_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_definition is not None:
            result['FlowDefinition'] = self.flow_definition
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.input is not None:
            result['Input'] = self.input
        if self.name is not None:
            result['Name'] = self.name
        if self.output is not None:
            result['Output'] = self.output
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.started_time is not None:
            result['StartedTime'] = self.started_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowDefinition') is not None:
            self.flow_definition = m.get('FlowDefinition')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')
        return self


class StopExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopExecutionResponseBody = None,
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
            temp_model = StopExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlowRequestEnvironmentVariables(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
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
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateFlowRequestEnvironment(TeaModel):
    def __init__(
        self,
        variables: List[UpdateFlowRequestEnvironmentVariables] = None,
    ):
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = UpdateFlowRequestEnvironmentVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class UpdateFlowRequest(TeaModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        environment: UpdateFlowRequestEnvironment = None,
        name: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # The definition of the workflow. The definition must comply with the flow definition language (FDL) syntax. Considering compatibility, the system supports the two workflow definition specifications.
        # 
        # >  In the preceding workflow definition example, Name:my_flow_name is the workflow name, which must be consistent with the input parameter Name
        self.definition = definition
        # The description of the flow.
        self.description = description
        self.environment = environment
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The Alibaba Cloud resource name (ARN) of the authorized role on which the execution of the flow relies. During the execution of the flow, the flow execution engine assumes the role to call API operations of relevant services.
        self.role_arn = role_arn
        # The type of the flow. Valid value: **FDL**.
        self.type = type

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            temp_model = UpdateFlowRequestEnvironment()
            self.environment = temp_model.from_map(m['Environment'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateFlowShrinkRequest(TeaModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        environment_shrink: str = None,
        name: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # The definition of the workflow. The definition must comply with the flow definition language (FDL) syntax. Considering compatibility, the system supports the two workflow definition specifications.
        # 
        # >  In the preceding workflow definition example, Name:my_flow_name is the workflow name, which must be consistent with the input parameter Name
        self.definition = definition
        # The description of the flow.
        self.description = description
        self.environment_shrink = environment_shrink
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The Alibaba Cloud resource name (ARN) of the authorized role on which the execution of the flow relies. During the execution of the flow, the flow execution engine assumes the role to call API operations of relevant services.
        self.role_arn = role_arn
        # The type of the flow. Valid value: **FDL**.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.environment_shrink is not None:
            result['Environment'] = self.environment_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            self.environment_shrink = m.get('Environment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateFlowResponseBodyEnvironmentVariables(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
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
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateFlowResponseBodyEnvironment(TeaModel):
    def __init__(
        self,
        variables: List[UpdateFlowResponseBodyEnvironmentVariables] = None,
    ):
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = UpdateFlowResponseBodyEnvironmentVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class UpdateFlowResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        definition: str = None,
        description: str = None,
        environment: UpdateFlowResponseBodyEnvironment = None,
        external_storage_location: str = None,
        id: str = None,
        last_modified_time: str = None,
        name: str = None,
        request_id: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # The time when the flow was created.
        self.created_time = created_time
        # The flow definition, which follows the FDL syntax standard. Considering compatibility, the system supports the two flow definition specifications.
        self.definition = definition
        # The description of the flow.
        self.description = description
        self.environment = environment
        # The path of the external storage.
        self.external_storage_location = external_storage_location
        # The unique ID of the flow.
        self.id = id
        # The time when the flow was last modified.
        self.last_modified_time = last_modified_time
        # The name of the flow.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The Alibaba Cloud resource name (ARN) of the authorized role on which the execution of the flow relies. During the execution of the flow, the flow execution engine assumes the role to call API operations of relevant services.
        self.role_arn = role_arn
        # The type of the flow.
        self.type = type

    def validate(self):
        if self.environment:
            self.environment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.description is not None:
            result['Description'] = self.description
        if self.environment is not None:
            result['Environment'] = self.environment.to_map()
        if self.external_storage_location is not None:
            result['ExternalStorageLocation'] = self.external_storage_location
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Environment') is not None:
            temp_model = UpdateFlowResponseBodyEnvironment()
            self.environment = temp_model.from_map(m['Environment'])
        if m.get('ExternalStorageLocation') is not None:
            self.external_storage_location = m.get('ExternalStorageLocation')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFlowResponseBody = None,
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
            temp_model = UpdateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlowAliasRequestRoutingConfigurations(TeaModel):
    def __init__(
        self,
        version: str = None,
        weight: int = None,
    ):
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateFlowAliasRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        flow_name: str = None,
        name: str = None,
        routing_configurations: List[UpdateFlowAliasRequestRoutingConfigurations] = None,
    ):
        self.description = description
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.name = name
        self.routing_configurations = routing_configurations

    def validate(self):
        if self.routing_configurations:
            for k in self.routing_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.name is not None:
            result['Name'] = self.name
        result['RoutingConfigurations'] = []
        if self.routing_configurations is not None:
            for k in self.routing_configurations:
                result['RoutingConfigurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.routing_configurations = []
        if m.get('RoutingConfigurations') is not None:
            for k in m.get('RoutingConfigurations'):
                temp_model = UpdateFlowAliasRequestRoutingConfigurations()
                self.routing_configurations.append(temp_model.from_map(k))
        return self


class UpdateFlowAliasShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        flow_name: str = None,
        name: str = None,
        routing_configurations_shrink: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.name = name
        self.routing_configurations_shrink = routing_configurations_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.name is not None:
            result['Name'] = self.name
        if self.routing_configurations_shrink is not None:
            result['RoutingConfigurations'] = self.routing_configurations_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RoutingConfigurations') is not None:
            self.routing_configurations_shrink = m.get('RoutingConfigurations')
        return self


class UpdateFlowAliasResponseBodyAliasRoutingConfigurations(TeaModel):
    def __init__(
        self,
        version: str = None,
        weight: int = None,
    ):
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateFlowAliasResponseBodyAlias(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        name: str = None,
        routing_configurations: List[UpdateFlowAliasResponseBodyAliasRoutingConfigurations] = None,
    ):
        self.created_time = created_time
        self.description = description
        self.name = name
        self.routing_configurations = routing_configurations

    def validate(self):
        if self.routing_configurations:
            for k in self.routing_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['RoutingConfigurations'] = []
        if self.routing_configurations is not None:
            for k in self.routing_configurations:
                result['RoutingConfigurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.routing_configurations = []
        if m.get('RoutingConfigurations') is not None:
            for k in m.get('RoutingConfigurations'):
                temp_model = UpdateFlowAliasResponseBodyAliasRoutingConfigurations()
                self.routing_configurations.append(temp_model.from_map(k))
        return self


class UpdateFlowAliasResponseBody(TeaModel):
    def __init__(
        self,
        alias: UpdateFlowAliasResponseBodyAlias = None,
        request_id: str = None,
    ):
        self.alias = alias
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.alias:
            self.alias.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            temp_model = UpdateFlowAliasResponseBodyAlias()
            self.alias = temp_model.from_map(m['Alias'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFlowAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFlowAliasResponseBody = None,
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
            temp_model = UpdateFlowAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMapRunRequest(TeaModel):
    def __init__(
        self,
        concurrency: int = None,
        execution_name: str = None,
        flow_name: str = None,
        map_run_name: str = None,
        request_id: str = None,
        tolerated_failed_count: int = None,
        tolerated_failed_percentage: float = None,
    ):
        self.concurrency = concurrency
        # This parameter is required.
        self.execution_name = execution_name
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.map_run_name = map_run_name
        self.request_id = request_id
        self.tolerated_failed_count = tolerated_failed_count
        self.tolerated_failed_percentage = tolerated_failed_percentage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.map_run_name is not None:
            result['MapRunName'] = self.map_run_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tolerated_failed_count is not None:
            result['ToleratedFailedCount'] = self.tolerated_failed_count
        if self.tolerated_failed_percentage is not None:
            result['ToleratedFailedPercentage'] = self.tolerated_failed_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('MapRunName') is not None:
            self.map_run_name = m.get('MapRunName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ToleratedFailedCount') is not None:
            self.tolerated_failed_count = m.get('ToleratedFailedCount')
        if m.get('ToleratedFailedPercentage') is not None:
            self.tolerated_failed_percentage = m.get('ToleratedFailedPercentage')
        return self


class UpdateMapRunResponseBody(TeaModel):
    def __init__(
        self,
        concurrency: int = None,
        execution_name: str = None,
        flow_name: str = None,
        map_run_name: str = None,
        request_id: str = None,
        tolerated_failed_count: int = None,
        tolerated_failed_percentage: float = None,
    ):
        self.concurrency = concurrency
        self.execution_name = execution_name
        self.flow_name = flow_name
        self.map_run_name = map_run_name
        # Id of the request
        self.request_id = request_id
        self.tolerated_failed_count = tolerated_failed_count
        self.tolerated_failed_percentage = tolerated_failed_percentage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.map_run_name is not None:
            result['MapRunName'] = self.map_run_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tolerated_failed_count is not None:
            result['ToleratedFailedCount'] = self.tolerated_failed_count
        if self.tolerated_failed_percentage is not None:
            result['ToleratedFailedPercentage'] = self.tolerated_failed_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('MapRunName') is not None:
            self.map_run_name = m.get('MapRunName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ToleratedFailedCount') is not None:
            self.tolerated_failed_count = m.get('ToleratedFailedCount')
        if m.get('ToleratedFailedPercentage') is not None:
            self.tolerated_failed_percentage = m.get('ToleratedFailedPercentage')
        return self


class UpdateMapRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMapRunResponseBody = None,
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
            temp_model = UpdateMapRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateScheduleRequest(TeaModel):
    def __init__(
        self,
        cron_expression: str = None,
        description: str = None,
        enable: bool = None,
        flow_name: str = None,
        payload: str = None,
        schedule_name: str = None,
    ):
        # The CRON expression.
        self.cron_expression = cron_expression
        # The description of the time-based schedule.
        self.description = description
        # Specifies whether to enable the time-based schedule. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable
        # The name of the flow that is associated with the time-based schedule. The name must be unique within the region and cannot be modified after the time-based schedule is created. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The trigger message of the time-based schedule. It must be in the JSON format.
        self.payload = payload
        # The name of the time-based schedule. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.schedule_name = schedule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class UpdateScheduleResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        cron_expression: str = None,
        description: str = None,
        enable: bool = None,
        last_modified_time: str = None,
        payload: str = None,
        request_id: str = None,
        schedule_id: str = None,
        schedule_name: str = None,
    ):
        # The time when the time-based schedule was created.
        self.created_time = created_time
        # The CRON expression.
        self.cron_expression = cron_expression
        # The description of the time-based schedule.
        self.description = description
        # Indicates whether the time-based schedule is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable = enable
        # The time when the time-based schedule was last updated.
        self.last_modified_time = last_modified_time
        # The trigger message of the time-based schedule.
        self.payload = payload
        # The request ID.
        self.request_id = request_id
        # The ID of the time-based schedule.
        self.schedule_id = schedule_id
        # The name of the time-based schedule.
        self.schedule_name = schedule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.description is not None:
            result['Description'] = self.description
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class UpdateScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateScheduleResponseBody = None,
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
            temp_model = UpdateScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


