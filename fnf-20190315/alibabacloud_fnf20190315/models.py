# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateFlowRequest(TeaModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        execution_mode: str = None,
        external_storage_location: str = None,
        name: str = None,
        request_id: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        self.definition = definition
        self.description = description
        self.execution_mode = execution_mode
        self.external_storage_location = external_storage_location
        self.name = name
        self.request_id = request_id
        self.role_arn = role_arn
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
        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode
        if self.external_storage_location is not None:
            result['ExternalStorageLocation'] = self.external_storage_location
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
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')
        if m.get('ExternalStorageLocation') is not None:
            self.external_storage_location = m.get('ExternalStorageLocation')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        definition: str = None,
        description: str = None,
        execution_mode: str = None,
        id: str = None,
        last_modified_time: str = None,
        name: str = None,
        request_id: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        self.created_time = created_time
        self.definition = definition
        self.description = description
        self.execution_mode = execution_mode
        self.id = id
        self.last_modified_time = last_modified_time
        self.name = name
        self.request_id = request_id
        self.role_arn = role_arn
        self.type = type

    def validate(self):
        pass

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
            temp_model = CreateFlowResponseBody()
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
        request_id: str = None,
        schedule_name: str = None,
    ):
        self.cron_expression = cron_expression
        self.description = description
        self.enable = enable
        self.flow_name = flow_name
        self.payload = payload
        self.request_id = request_id
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
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
        self.created_time = created_time
        self.cron_expression = cron_expression
        self.description = description
        self.enable = enable
        self.last_modified_time = last_modified_time
        self.payload = payload
        self.request_id = request_id
        self.schedule_id = schedule_id
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
            temp_model = CreateScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
    ):
        self.name = name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFlowResponseBody(TeaModel):
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
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduleRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        request_id: str = None,
        schedule_name: str = None,
    ):
        self.flow_name = flow_name
        self.request_id = request_id
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')
        return self


class DeleteScheduleResponseBody(TeaModel):
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
            temp_model = DeleteScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExecutionRequest(TeaModel):
    def __init__(
        self,
        execution_name: str = None,
        flow_name: str = None,
        request_id: str = None,
        wait_time_seconds: int = None,
    ):
        self.execution_name = execution_name
        self.flow_name = flow_name
        self.request_id = request_id
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.wait_time_seconds is not None:
            result['WaitTimeSeconds'] = self.wait_time_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WaitTimeSeconds') is not None:
            self.wait_time_seconds = m.get('WaitTimeSeconds')
        return self


class DescribeExecutionResponseBody(TeaModel):
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
        self.flow_definition = flow_definition
        self.flow_name = flow_name
        self.input = input
        self.name = name
        self.output = output
        self.request_id = request_id
        self.started_time = started_time
        self.status = status
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
            temp_model = DescribeExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
    ):
        self.name = name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFlowResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        definition: str = None,
        description: str = None,
        execution_mode: str = None,
        id: str = None,
        last_modified_time: str = None,
        name: str = None,
        request_id: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        self.created_time = created_time
        self.definition = definition
        self.description = description
        self.execution_mode = execution_mode
        self.id = id
        self.last_modified_time = last_modified_time
        self.name = name
        self.request_id = request_id
        self.role_arn = role_arn
        self.type = type

    def validate(self):
        pass

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
            temp_model = DescribeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScheduleRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        request_id: str = None,
        schedule_name: str = None,
    ):
        self.flow_name = flow_name
        self.request_id = request_id
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.created_time = created_time
        self.cron_expression = cron_expression
        self.description = description
        self.enable = enable
        self.last_modified_time = last_modified_time
        self.payload = payload
        self.request_id = request_id
        self.schedule_id = schedule_id
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
        request_id: str = None,
    ):
        self.execution_name = execution_name
        self.flow_name = flow_name
        self.limit = limit
        self.next_token = next_token
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
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.event_detail = event_detail
        self.event_id = event_id
        self.schedule_event_id = schedule_event_id
        self.step_name = step_name
        self.time = time
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
        self.events = events
        self.next_token = next_token
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
            temp_model = GetExecutionHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionsRequest(TeaModel):
    def __init__(
        self,
        execution_name_prefix: str = None,
        flow_name: str = None,
        limit: int = None,
        next_token: str = None,
        request_id: str = None,
        started_time_begin: str = None,
        started_time_end: str = None,
        status: str = None,
    ):
        self.execution_name_prefix = execution_name_prefix
        self.flow_name = flow_name
        self.limit = limit
        self.next_token = next_token
        self.request_id = request_id
        self.started_time_begin = started_time_begin
        self.started_time_end = started_time_end
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartedTimeBegin') is not None:
            self.started_time_begin = m.get('StartedTimeBegin')
        if m.get('StartedTimeEnd') is not None:
            self.started_time_end = m.get('StartedTimeEnd')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListExecutionsResponseBodyExecutions(TeaModel):
    def __init__(
        self,
        flow_definition: str = None,
        flow_name: str = None,
        input: str = None,
        name: str = None,
        output: str = None,
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
    ):
        self.flow_definition = flow_definition
        self.flow_name = flow_name
        self.input = input
        self.name = name
        self.output = output
        self.started_time = started_time
        self.status = status
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
        self.executions = executions
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
            temp_model = ListExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.limit = limit
        self.next_token = next_token
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowsResponseBodyFlows(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        definition: str = None,
        description: str = None,
        execution_mode: str = None,
        id: str = None,
        last_modified_time: str = None,
        name: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        self.created_time = created_time
        self.definition = definition
        self.description = description
        self.execution_mode = execution_mode
        self.id = id
        self.last_modified_time = last_modified_time
        self.name = name
        self.role_arn = role_arn
        self.type = type

    def validate(self):
        pass

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
        self.flows = flows
        self.next_token = next_token
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
            temp_model = ListFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchedulesRequest(TeaModel):
    def __init__(
        self,
        flow_name: str = None,
        limit: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.flow_name = flow_name
        self.limit = limit
        self.next_token = next_token
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.created_time = created_time
        self.cron_expression = cron_expression
        self.description = description
        self.enable = enable
        self.last_modified_time = last_modified_time
        self.payload = payload
        self.schedule_id = schedule_id
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
        self.next_token = next_token
        self.request_id = request_id
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
            temp_model = ListSchedulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportTaskFailedRequest(TeaModel):
    def __init__(
        self,
        cause: str = None,
        error: str = None,
        request_id: str = None,
        task_token: str = None,
    ):
        self.cause = cause
        self.error = error
        self.request_id = request_id
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_token is not None:
            result['TaskToken'] = self.task_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskToken') is not None:
            self.task_token = m.get('TaskToken')
        return self


class ReportTaskFailedResponseBody(TeaModel):
    def __init__(
        self,
        event_id: int = None,
        request_id: str = None,
    ):
        self.event_id = event_id
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
            temp_model = ReportTaskFailedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportTaskSucceededRequest(TeaModel):
    def __init__(
        self,
        output: str = None,
        request_id: str = None,
        task_token: str = None,
    ):
        self.output = output
        self.request_id = request_id
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_token is not None:
            result['TaskToken'] = self.task_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskToken') is not None:
            self.task_token = m.get('TaskToken')
        return self


class ReportTaskSucceededResponseBody(TeaModel):
    def __init__(
        self,
        event_id: int = None,
        request_id: str = None,
    ):
        self.event_id = event_id
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
        request_id: str = None,
    ):
        self.callback_fn_ftask_token = callback_fn_ftask_token
        self.execution_name = execution_name
        self.flow_name = flow_name
        self.input = input
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.flow_definition = flow_definition
        self.flow_name = flow_name
        self.input = input
        self.name = name
        self.output = output
        self.request_id = request_id
        self.started_time = started_time
        self.status = status
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
            temp_model = StartExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopExecutionRequest(TeaModel):
    def __init__(
        self,
        cause: str = None,
        error: str = None,
        execution_name: str = None,
        flow_name: str = None,
        request_id: str = None,
    ):
        self.cause = cause
        self.error = error
        self.execution_name = execution_name
        self.flow_name = flow_name
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
    ):
        self.flow_definition = flow_definition
        self.flow_name = flow_name
        self.input = input
        self.name = name
        self.output = output
        self.request_id = request_id
        self.started_time = started_time
        self.status = status
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
            temp_model = StopExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlowRequest(TeaModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        name: str = None,
        request_id: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        self.definition = definition
        self.description = description
        self.name = name
        self.request_id = request_id
        self.role_arn = role_arn
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
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateFlowResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        definition: str = None,
        description: str = None,
        external_storage_location: str = None,
        id: str = None,
        last_modified_time: str = None,
        name: str = None,
        request_id: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        self.created_time = created_time
        self.definition = definition
        self.description = description
        self.external_storage_location = external_storage_location
        self.id = id
        self.last_modified_time = last_modified_time
        self.name = name
        self.request_id = request_id
        self.role_arn = role_arn
        self.type = type

    def validate(self):
        pass

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
            temp_model = UpdateFlowResponseBody()
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
        request_id: str = None,
        schedule_name: str = None,
    ):
        self.cron_expression = cron_expression
        self.description = description
        self.enable = enable
        self.flow_name = flow_name
        self.payload = payload
        self.request_id = request_id
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.created_time = created_time
        self.cron_expression = cron_expression
        self.description = description
        self.enable = enable
        self.last_modified_time = last_modified_time
        self.payload = payload
        self.request_id = request_id
        self.schedule_id = schedule_id
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
            temp_model = UpdateScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


