# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeInvocationsResponseBody(DaraModel):
    def __init__(
        self,
        invocations: List[main_models.DescribeInvocationsResponseBodyInvocations] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The command execution records.
        self.invocations = invocations
        # The query token that is returned from this call.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.invocations:
            for v1 in self.invocations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Invocations'] = []
        if self.invocations is not None:
            for k1 in self.invocations:
                result['Invocations'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocations = []
        if m.get('Invocations') is not None:
            for k1 in m.get('Invocations'):
                temp_model = main_models.DescribeInvocationsResponseBodyInvocations()
                self.invocations.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInvocationsResponseBodyInvocations(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        command_type: str = None,
        creation_time: str = None,
        end_user_id: str = None,
        invocation_status: str = None,
        invoke_desktop_count: int = None,
        invoke_desktop_succeed_count: int = None,
        invoke_desktops: List[main_models.DescribeInvocationsResponseBodyInvocationsInvokeDesktops] = None,
        invoke_id: str = None,
    ):
        # The Base64-encoded command content.
        self.command_content = command_content
        # The type of the command.
        self.command_type = command_type
        # The time when the execution task is created.
        self.creation_time = creation_time
        # The ID of the end user.
        self.end_user_id = end_user_id
        # The overall execution status of the command. The value of this parameter depends on the execution status of the command on all the involved cloud computers. Valid values:
        # 
        # *   Pending: The command is being verified or sent. If the execution status is Pending on at least one cloud computer, the overall status is considered Pending.
        # 
        # *   Running: The command is being executed on cloud computers. If the execution status is Running on at least one cloud computer, the overall status is considered Running.
        # 
        # *   Success: If the execution status is Success on at least one cloud computer and either Success or Stopped on all other cloud computers, the overall status is considered Success.
        # 
        # *   Failed: If the execution status is Stopped or Failed on all cloud computers, the overall status is considered Failed. If any execution status on cloud computers matches one of the following values, Failed is returned.
        # 
        #     *   Invalid: The command is invalid.
        #     *   Aborted: The command failed to be sent.
        #     *   Failed: The command is executed, but the exit code is not 0.
        #     *   Timeout: The command execution timed out.
        #     *   Error: An error occurred when the command is being executed.
        # 
        # *   Stopping: The command execution is being stopped. If the execution status is Stopping on at least one cloud computer, the overall status is considered Stopping.
        # 
        # *   Stopped: The command execution stops. If the execution status is Stopped on at least one cloud computer, the overall status is considered Stopped. If any execution status on cloud computers matches one of the following values, Stopped is returned.
        # 
        #     *   Cancelled: The command execution is canceled.
        #     *   Terminated: The command execution is terminated.
        # 
        # *   PartialFailed: The command execution succeeded on some cloud computers but failed on others. If the execution status on any cloud computer is Success, Failed, or Stopped, the overall status is considered PartialFailed.
        self.invocation_status = invocation_status
        # The total number of cloud computers on which the command is executed.
        self.invoke_desktop_count = invoke_desktop_count
        # The total number of cloud computers on which the command execution succeeds.
        self.invoke_desktop_succeed_count = invoke_desktop_succeed_count
        # The cloud computers on which the command is executed.
        self.invoke_desktops = invoke_desktops
        # The ID of the execution.
        self.invoke_id = invoke_id

    def validate(self):
        if self.invoke_desktops:
            for v1 in self.invoke_desktops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.command_type is not None:
            result['CommandType'] = self.command_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.invoke_desktop_count is not None:
            result['InvokeDesktopCount'] = self.invoke_desktop_count

        if self.invoke_desktop_succeed_count is not None:
            result['InvokeDesktopSucceedCount'] = self.invoke_desktop_succeed_count

        result['InvokeDesktops'] = []
        if self.invoke_desktops is not None:
            for k1 in self.invoke_desktops:
                result['InvokeDesktops'].append(k1.to_map() if k1 else None)

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('InvokeDesktopCount') is not None:
            self.invoke_desktop_count = m.get('InvokeDesktopCount')

        if m.get('InvokeDesktopSucceedCount') is not None:
            self.invoke_desktop_succeed_count = m.get('InvokeDesktopSucceedCount')

        self.invoke_desktops = []
        if m.get('InvokeDesktops') is not None:
            for k1 in m.get('InvokeDesktops'):
                temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvokeDesktops()
                self.invoke_desktops.append(temp_model.from_map(k1))

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        return self

class DescribeInvocationsResponseBodyInvocationsInvokeDesktops(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        dropped: int = None,
        error_code: str = None,
        error_info: str = None,
        exit_code: int = None,
        finish_time: str = None,
        invocation_status: str = None,
        output: str = None,
        repeats: int = None,
        start_time: str = None,
        stop_time: str = None,
        update_time: str = None,
    ):
        # The time when the command execution was performed.
        self.creation_time = creation_time
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The cloud computer name.
        self.desktop_name = desktop_name
        # The size of the text that is truncated and discarded when the Output value exceeds 24 KB in size.
        self.dropped = dropped
        # The code explaining why the command failed to be sent or executed. Valid values:
        # 
        # *   Null: The command is executed successfully.
        # *   InstanceNotExists: The specified cloud computer does not exist or is released.
        # *   InstanceReleased: The cloud computer is released during the execution.
        # *   InstanceNotRunning: The cloud computer is not running during the execution.
        # *   CommandNotApplicable: The command cannot be executed on the specified cloud computer.
        # *   ClientNotRunning: The Cloud Assistant agent is not running.
        # *   ClientNotResponse: The Cloud Assistant agent does not respond.
        # *   ClientIsUpgrading: The Cloud Assistant agent is being updated.
        # *   ClientNeedUpgrade: The Cloud Assistant agent needs to be updated.
        # *   DeliveryTimeout: The command sending times out.
        # *   ExecutionTimeout: The command execution times out.
        # *   ExecutionException: An exception occurs when the command is being executed.
        # *   ExecutionInterrupted: The command execution is interrupted.
        # *   ExitCodeNonzero: The command execution completes, but the exit code is not 0.
        self.error_code = error_code
        # The message explaining why the command failed to be sent or executed. Valid values:
        # 
        # *   Null: The command is executed successfully.
        # *   the specified instance does not exists: The specified cloud computer does not exist or is released.
        # *   the instance has released when create task: The cloud computer is released during the execution.
        # *   the instance is not running when create task: The cloud computer is not running during the execution.
        # *   the command is not applicable: The command cannot be executed on the specified cloud computer.
        # *   the aliyun service is not running on the instance: The Cloud Assistant agent is not running.
        # *   the aliyun service in the instance does not response: The Cloud Assistant agent does not respond.
        # *   the aliyun service in the instance is upgrading now: The Cloud Assistant agent is being updated.
        # *   the aliyun service in the instance need upgrade: The Cloud Assistant agent needs to be updated.
        # *   the command delivery has been timeout: The command sending times out.
        # *   the command execution has been timeout: The command execution times out.
        # *   the command execution got an exception: An exception occurs when the command is being executed.
        # *   the command execution has been interrupted: The command execution is interrupted.
        # *   the command execution exit code is not zero: The command execution completes, but the exit code is not 0.
        self.error_info = error_info
        # The exit code of the execution.
        self.exit_code = exit_code
        # The time when the command execution ended.
        self.finish_time = finish_time
        # The execution progress of the command on a single cloud computer.
        self.invocation_status = invocation_status
        # The command output.
        # 
        # *   When the `IncludeOutput` parameter is set to false, the output is not returned.
        # *   When the `ContentEncoding` parameter is set to Base64, the output is returned as a Base64-encoded string.
        self.output = output
        # The number of times the command has been executed on the cloud computer.
        self.repeats = repeats
        # The start time of the command execution.
        self.start_time = start_time
        # The stop time of the command execution (StopInvocatio).
        self.stop_time = stop_time
        # The time when the execution status was updated.
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

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

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

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.output is not None:
            result['Output'] = self.output

        if self.repeats is not None:
            result['Repeats'] = self.repeats

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

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

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Repeats') is not None:
            self.repeats = m.get('Repeats')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

