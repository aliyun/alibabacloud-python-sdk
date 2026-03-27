# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInvocationsResponseBody(DaraModel):
    def __init__(
        self,
        invocations: main_models.DescribeInvocationsResponseBodyInvocations = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.invocations = invocations
        # The overall execution status of the command task. The value of this parameter depends on the execution states of the command task on all involved instances. Valid values:
        # 
        # *   Running:
        # 
        #     *   Scheduled task: Before you stop the scheduled execution of the command, the overall execution state is always Running.
        #     *   One-time task: If the command is being run on instances, the overall execution state is Running.
        # 
        # *   Finished:
        # 
        #     *   Scheduled task: The overall execution state can never be Finished.
        #     *   One-time task: The execution is complete on all instances, or the execution is stopped on some instances and is complete on the other instances.
        # 
        # *   Success: If the execution state on at least one instance is Success and the execution state on the other instances is Stopped or Success, the overall execution state is Success.
        # 
        #     *   One-time task: The execution is complete, and the exit code is 0.
        #     *   Scheduled task: The last execution is complete, the exit code is 0, and the specified period ends.
        # 
        # *   Failed:
        # 
        #     *   Scheduled task: The overall execution state can never be Failed.
        #     *   One-time task: The execution failed on all instances.
        # 
        # *   Stopped: The task is stopped.
        # 
        # *   Stopping: The task is being stopped.
        # 
        # *   PartialFailed: The task fails on some instances. If you specify both this parameter and `InstanceId`, this parameter does not take effect.
        # 
        # *   Pending: The command is being verified or sent. If the execution state on at least one instance is Pending, the overall execution state is Pending.
        # 
        # *   Scheduled: The command that is set to run on a schedule is sent and waiting to be run. If the execution state on at least one instance is Scheduled, the overall execution state is Scheduled.
        self.next_token = next_token
        # The command type. Valid values:
        # 
        # *   RunBatScript: batch command, applicable to Windows instances.
        # *   RunPowerShellScript: PowerShell command, applicable to Windows instances.
        # *   RunShellScript: shell command, applicable to Linux instances.
        self.page_number = page_number
        # The command ID. You can call the [DescribeCommands](https://help.aliyun.com/document_detail/64843.html) operation to query all available command IDs.
        self.page_size = page_size
        # The command name. If you specify both this parameter and `InstanceId`, this parameter does not take effect.
        self.request_id = request_id
        # Specifies whether the command is to be automatically run. Valid values:
        # 
        # *   true: The command is run by calling the `RunCommand` or `InvokeCommand` operation with `RepeatMode` set to `Period`, `NextRebootOnly`, or `EveryReboot`.
        # 
        # *   false: The command meets one of the following requirements:
        # 
        #     *   The command is run by calling the `RunCommand` or `InvokeCommand` operation with `RepeatMode` set to `Once`.
        #     *   The command task is canceled, stopped, or completed.
        # 
        # Default value: false.
        self.total_count = total_count

    def validate(self):
        if self.invocations:
            self.invocations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invocations is not None:
            result['Invocations'] = self.invocations.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        if m.get('Invocations') is not None:
            temp_model = main_models.DescribeInvocationsResponseBodyInvocations()
            self.invocations = temp_model.from_map(m.get('Invocations'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInvocationsResponseBodyInvocations(DaraModel):
    def __init__(
        self,
        invocation: List[main_models.DescribeInvocationsResponseBodyInvocationsInvocation] = None,
    ):
        self.invocation = invocation

    def validate(self):
        if self.invocation:
            for v1 in self.invocation:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Invocation'] = []
        if self.invocation is not None:
            for k1 in self.invocation:
                result['Invocation'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocation = []
        if m.get('Invocation') is not None:
            for k1 in m.get('Invocation'):
                temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocation()
                self.invocation.append(temp_model.from_map(k1))

        return self

class DescribeInvocationsResponseBodyInvocationsInvocation(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        command_description: str = None,
        command_id: str = None,
        command_name: str = None,
        command_type: str = None,
        container_id: str = None,
        container_name: str = None,
        creation_time: str = None,
        frequency: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        invoke_instances: main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstances = None,
        invoke_status: str = None,
        launcher: str = None,
        oss_output_delivery: str = None,
        parameters: str = None,
        repeat_mode: str = None,
        tags: main_models.DescribeInvocationsResponseBodyInvocationsInvocationTags = None,
        termination_mode: str = None,
        timed: bool = None,
        timeout: int = None,
        username: str = None,
        working_dir: str = None,
    ):
        self.command_content = command_content
        self.command_description = command_description
        self.command_id = command_id
        self.command_name = command_name
        self.command_type = command_type
        self.container_id = container_id
        self.container_name = container_name
        self.creation_time = creation_time
        self.frequency = frequency
        self.invocation_status = invocation_status
        self.invoke_id = invoke_id
        self.invoke_instances = invoke_instances
        self.invoke_status = invoke_status
        self.launcher = launcher
        self.oss_output_delivery = oss_output_delivery
        self.parameters = parameters
        self.repeat_mode = repeat_mode
        self.tags = tags
        self.termination_mode = termination_mode
        self.timed = timed
        self.timeout = timeout
        self.username = username
        self.working_dir = working_dir

    def validate(self):
        if self.invoke_instances:
            self.invoke_instances.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.command_description is not None:
            result['CommandDescription'] = self.command_description

        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.command_name is not None:
            result['CommandName'] = self.command_name

        if self.command_type is not None:
            result['CommandType'] = self.command_type

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.invoke_instances is not None:
            result['InvokeInstances'] = self.invoke_instances.to_map()

        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status

        if self.launcher is not None:
            result['Launcher'] = self.launcher

        if self.oss_output_delivery is not None:
            result['OssOutputDelivery'] = self.oss_output_delivery

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.termination_mode is not None:
            result['TerminationMode'] = self.termination_mode

        if self.timed is not None:
            result['Timed'] = self.timed

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.username is not None:
            result['Username'] = self.username

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('CommandDescription') is not None:
            self.command_description = m.get('CommandDescription')

        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')

        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('InvokeInstances') is not None:
            temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstances()
            self.invoke_instances = temp_model.from_map(m.get('InvokeInstances'))

        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')

        if m.get('Launcher') is not None:
            self.launcher = m.get('Launcher')

        if m.get('OssOutputDelivery') is not None:
            self.oss_output_delivery = m.get('OssOutputDelivery')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocationTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TerminationMode') is not None:
            self.termination_mode = m.get('TerminationMode')

        if m.get('Timed') is not None:
            self.timed = m.get('Timed')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class DescribeInvocationsResponseBodyInvocationsInvocationTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeInvocationsResponseBodyInvocationsInvocationTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocationTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInvocationsResponseBodyInvocationsInvocationTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstances(DaraModel):
    def __init__(
        self,
        invoke_instance: List[main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstancesInvokeInstance] = None,
    ):
        self.invoke_instance = invoke_instance

    def validate(self):
        if self.invoke_instance:
            for v1 in self.invoke_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InvokeInstance'] = []
        if self.invoke_instance is not None:
            for k1 in self.invoke_instance:
                result['InvokeInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invoke_instance = []
        if m.get('InvokeInstance') is not None:
            for k1 in m.get('InvokeInstance'):
                temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstancesInvokeInstance()
                self.invoke_instance.append(temp_model.from_map(k1))

        return self

class DescribeInvocationsResponseBodyInvocationsInvocationInvokeInstancesInvokeInstance(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        dropped: int = None,
        error_code: str = None,
        error_info: str = None,
        exit_code: int = None,
        finish_time: str = None,
        instance_id: str = None,
        instance_invoke_status: str = None,
        invocation_status: str = None,
        oss_output_error_code: str = None,
        oss_output_error_info: str = None,
        oss_output_status: str = None,
        oss_output_uri: str = None,
        output: str = None,
        repeats: int = None,
        start_time: str = None,
        stop_time: str = None,
        timed: bool = None,
        update_time: str = None,
    ):
        self.creation_time = creation_time
        self.dropped = dropped
        self.error_code = error_code
        self.error_info = error_info
        self.exit_code = exit_code
        self.finish_time = finish_time
        self.instance_id = instance_id
        self.instance_invoke_status = instance_invoke_status
        self.invocation_status = invocation_status
        self.oss_output_error_code = oss_output_error_code
        self.oss_output_error_info = oss_output_error_info
        self.oss_output_status = oss_output_status
        self.oss_output_uri = oss_output_uri
        self.output = output
        self.repeats = repeats
        self.start_time = start_time
        self.stop_time = stop_time
        self.timed = timed
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dropped is not None:
            result['Dropped'] = self.dropped

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info

        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_invoke_status is not None:
            result['InstanceInvokeStatus'] = self.instance_invoke_status

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.oss_output_error_code is not None:
            result['OssOutputErrorCode'] = self.oss_output_error_code

        if self.oss_output_error_info is not None:
            result['OssOutputErrorInfo'] = self.oss_output_error_info

        if self.oss_output_status is not None:
            result['OssOutputStatus'] = self.oss_output_status

        if self.oss_output_uri is not None:
            result['OssOutputUri'] = self.oss_output_uri

        if self.output is not None:
            result['Output'] = self.output

        if self.repeats is not None:
            result['Repeats'] = self.repeats

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        if self.timed is not None:
            result['Timed'] = self.timed

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Dropped') is not None:
            self.dropped = m.get('Dropped')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')

        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceInvokeStatus') is not None:
            self.instance_invoke_status = m.get('InstanceInvokeStatus')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('OssOutputErrorCode') is not None:
            self.oss_output_error_code = m.get('OssOutputErrorCode')

        if m.get('OssOutputErrorInfo') is not None:
            self.oss_output_error_info = m.get('OssOutputErrorInfo')

        if m.get('OssOutputStatus') is not None:
            self.oss_output_status = m.get('OssOutputStatus')

        if m.get('OssOutputUri') is not None:
            self.oss_output_uri = m.get('OssOutputUri')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Repeats') is not None:
            self.repeats = m.get('Repeats')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        if m.get('Timed') is not None:
            self.timed = m.get('Timed')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

