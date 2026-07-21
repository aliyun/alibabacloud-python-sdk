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
        # The array of script execution records.
        self.invocations = invocations
        # The pagination token returned in this call.
        self.next_token = next_token
        # The request ID.
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
        desktop_scenario: str = None,
        end_user_id: str = None,
        invocation_status: str = None,
        invoke_desktop_count: int = None,
        invoke_desktop_succeed_count: int = None,
        invoke_desktops: List[main_models.DescribeInvocationsResponseBodyInvocationsInvokeDesktops] = None,
        invoke_id: str = None,
    ):
        # The script content, transmitted in Base64 encoding.
        self.command_content = command_content
        # The script type.
        self.command_type = command_type
        # The creation time of the task.
        self.creation_time = creation_time
        self.desktop_scenario = desktop_scenario
        # The end user ID.
        self.end_user_id = end_user_id
        # The overall execution status of the script. The overall execution status depends on the combined execution status of all cloud desktops in this call. Valid values:
        # 
        # - Pending: The system is validating or sending the command. If the script execution status on at least one cloud desktop is Pending, the overall execution status is Pending.
        # - Running: The command is running on the cloud desktop. If the script execution status on at least one cloud desktop is Running, the overall execution status is Running.
        # - Success: The script execution status on each cloud desktop is Stopped or Success, and the script execution status on at least one cloud desktop is Success. The overall execution status is Success.
        # - Failed: The script execution status on each cloud desktop is Stopped or Failed. The overall execution status is Failed. The return value is Failed when one or more of the following statuses occur on a cloud desktop:
        #     - Command validation failed (Invalid).
        #     - Command delivery failed (Aborted).
        #     - Command execution completed but the exit code is non-zero (Failed).
        #     - Command execution timed out (Timeout).
        #     - Command execution encountered an exception (Error).
        # - Stopping: The task is being stopped. If the script execution status on at least one instance is Stopping, the overall execution status is Stopping.
        # - Stopped: The task has been stopped. If the script execution status on all instances is Stopped, the overall execution status is Stopped. The return value is Stopped when the script execution status on an instance is one of the following:
        #     - Task cancelled (Cancelled).
        #     - Task terminated (Terminated).
        # - PartialFailed: Some instances succeeded and some instances failed. If the script execution status on each instance is Success, Failed, or Stopped, the overall execution status is PartialFailed.
        self.invocation_status = invocation_status
        # The total number of cloud desktops on which the script was run.
        self.invoke_desktop_count = invoke_desktop_count
        # The total number of cloud desktops on which the script was run successfully.
        self.invoke_desktop_succeed_count = invoke_desktop_succeed_count
        # The list of target cloud desktops for execution.
        self.invoke_desktops = invoke_desktops
        # The execution ID.
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

        if self.desktop_scenario is not None:
            result['DesktopScenario'] = self.desktop_scenario

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

        if m.get('DesktopScenario') is not None:
            self.desktop_scenario = m.get('DesktopScenario')

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
        jvs_agent_id: str = None,
        output: str = None,
        repeats: int = None,
        start_time: str = None,
        stop_time: str = None,
        update_time: str = None,
    ):
        # The creation time of the script process.
        self.creation_time = creation_time
        # The cloud desktop ID.
        self.desktop_id = desktop_id
        # The cloud desktop name.
        self.desktop_name = desktop_name
        # The length of the truncated and discarded text after the text length in the Output field exceeds 24 KB.
        self.dropped = dropped
        # The error code for the command delivery failure or execution failure. Valid values:
        # 
        # - Empty: The command ran normally.
        # - InstanceNotExists: The specified cloud desktop does not exist or has been released.
        # - InstanceReleased: The cloud desktop was released during task execution.
        # - InstanceNotRunning: The cloud desktop was not running when the task was created.
        # - CommandNotApplicable: The command is not applicable to the specified cloud desktop.
        # - ClientNotRunning: The Cloud Assistant client is not running.
        # - ClientNotResponse: The Cloud Assistant client is not responding.
        # - ClientIsUpgrading: The Cloud Assistant client is being upgraded.
        # - ClientNeedUpgrade: The Cloud Assistant client needs to be upgraded.
        # - DeliveryTimeout: Command delivery timed out.
        # - ExecutionTimeout: Command execution timed out.
        # - ExecutionException: An exception occurred during command execution.
        # - ExecutionInterrupted: Command execution was interrupted.
        # - ExitCodeNonzero: Command execution completed with a non-zero exit code.
        self.error_code = error_code
        # The detailed information about the command delivery failure or execution failure. Valid values:
        # 
        # - Empty: The command ran normally.
        # - the specified instance does not exists: The specified cloud desktop does not exist or has been released.
        # - the instance has released when create task: The cloud desktop was released during task execution.
        # - the instance is not running when create task: The cloud desktop was not running when the task was created.
        # - the command is not applicable: The command is not applicable to the specified cloud desktop.
        # - the aliyun service is not running on the instance: The Cloud Assistant client is not running.
        # - the aliyun service in the instance does not response: The Cloud Assistant client is not responding.
        # - the aliyun service in the instance is upgrading now: The Cloud Assistant client is being upgraded.
        # - the aliyun service in the instance need upgrade: The Cloud Assistant client needs to be upgraded.
        # - the command delivery has been timeout: Command delivery timed out.
        # - the command execution has been timeout: Command execution timed out.
        # - the command execution got an exception: An exception occurred during command execution.
        # - the command execution has been interrupted: Command execution was interrupted.
        # - the command execution exit code is not zero: Command execution completed with a non-zero exit code.
        self.error_info = error_info
        # The exit code of the script process.
        self.exit_code = exit_code
        # The end time of the script process.
        self.finish_time = finish_time
        # The script execution status on a single cloud desktop.
        self.invocation_status = invocation_status
        self.jvs_agent_id = jvs_agent_id
        # The output of the script process.
        # 
        # - If the request parameter `IncludeOutput` is set to false, Output is not returned.
        # - If the request parameter `ContentEncoding` is set to Base64, Output is the Base64-encoded output.
        self.output = output
        # The number of times the command was run on the cloud desktop.
        self.repeats = repeats
        # The time when the script process started running on the cloud desktop.
        self.start_time = start_time
        # The time when execution was stopped, if StopInvocation was called.
        self.stop_time = stop_time
        # The update time of the task status.
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

        if self.jvs_agent_id is not None:
            result['JvsAgentId'] = self.jvs_agent_id

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

        if m.get('JvsAgentId') is not None:
            self.jvs_agent_id = m.get('JvsAgentId')

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

