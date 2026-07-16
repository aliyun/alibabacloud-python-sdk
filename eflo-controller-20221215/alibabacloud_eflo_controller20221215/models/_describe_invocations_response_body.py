# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class DescribeInvocationsResponseBody(DaraModel):
    def __init__(
        self,
        invocations: main_models.DescribeInvocationsResponseBodyInvocations = None,
        request_id: str = None,
    ):
        # The object that contains the script execution records.
        self.invocations = invocations
        # The ID of the request.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Invocations') is not None:
            temp_model = main_models.DescribeInvocationsResponseBodyInvocations()
            self.invocations = temp_model.from_map(m.get('Invocations'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInvocationsResponseBodyInvocations(DaraModel):
    def __init__(
        self,
        invocation: List[main_models.DescribeInvocationsResponseBodyInvocationsInvocation] = None,
    ):
        # The command execution records.
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
        command_name: str = None,
        creation_time: str = None,
        frequency: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        invoke_nodes: main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodes = None,
        invoke_status: str = None,
        parameters: str = None,
        repeat_mode: str = None,
        timeout: int = None,
        username: str = None,
        working_dir: str = None,
    ):
        # The content of the command.
        # 
        # - If \\`ContentEncoding\\` is set to \\`PlainText\\`, the original script content is returned.
        # 
        # - If \\`ContentEncoding\\` is set to \\`Base64\\`, the Base64-encoded script content is returned.
        self.command_content = command_content
        # The description of the command.
        self.command_description = command_description
        # The name of the command.
        self.command_name = command_name
        # The time when the task was created.
        self.creation_time = creation_time
        # The cron expression for the scheduled command.
        self.frequency = frequency
        # The overall execution status of the command. This status is determined by the execution status on all involved instances. Valid values:
        # 
        # - Pending: The system is verifying or sending the command. If the command is in the Pending state on at least one instance, the overall status is Pending.
        # 
        # - Scheduled: The scheduled command is sent and is waiting to run. If the command is in the Scheduled state on at least one instance, the overall status is Scheduled.
        # 
        # - Running: The command is running on the instances. If the command is in the Running state on at least one instance, the overall status is Running.
        # 
        # - Success: The command was successfully executed. The command status on each instance is Stopped or Success, and the status on at least one instance is Success.
        # 
        #   - For one-time tasks: The command execution is complete and the exit code is 0.
        # 
        #   - For scheduled tasks: The last execution was successful with an exit code of 0, and all scheduled executions are complete.
        # 
        # - Failed: The command execution failed. The command status on each instance is Stopped or Failed. The overall status is Failed if the command status on one or more instances is one of the following:
        # 
        #   - The command failed to be verified (Invalid).
        # 
        #   - The command failed to be sent (Aborted).
        # 
        #   - The command execution is complete, but the exit code is not 0 (Failed).
        # 
        #   - The command timed out (Timeout).
        # 
        #   - An error occurred during the command execution (Error).
        # 
        # - Stopping: The task is being stopped. If the command is in the Stopping state on at least one instance, the overall status is Stopping.
        # 
        # - Stopped: The task was stopped. The overall status is Stopped if the command is in the Stopped state on all instances. The overall status is Stopped if the command status on the instances is one of the following:
        # 
        #   - The task was canceled (Cancelled).
        # 
        #   - The task was terminated (Terminated).
        # 
        # - PartialFailed: The command was successfully executed on some instances but failed on others. The overall status is PartialFailed if the command status on the instances is Success, Failed, or Stopped.
        # 
        # > The `InvokeStatus` parameter has a similar meaning. However, check the value of this parameter.
        self.invocation_status = invocation_status
        # The ID of the command execution.
        self.invoke_id = invoke_id
        # The command execution records.
        self.invoke_nodes = invoke_nodes
        # The overall execution status of the command. This status is determined by the execution status on one or more instances. Valid values:
        # 
        # - Running:
        # 
        #   - Scheduled execution: The status is always Running before you manually stop the scheduled command.
        # 
        #   - One-time execution: The overall status is Running if a command process is in progress.
        # 
        # - Finished:
        # 
        #   - Scheduled execution: A command process cannot be in the Finished state.
        # 
        #   - One-time execution: The execution is complete on all instances. Alternatively, the command process is manually stopped on some instances and the execution is complete on the other instances.
        # 
        # - Failed:
        # 
        #   - Scheduled execution: A command process cannot be in the Failed state.
        # 
        #   - One-time execution: The execution failed on all instances.
        # 
        # - Stopped: The command is stopped.
        # 
        # - Stopping: The command is being stopped.
        # 
        # - PartialFailed: The execution failed on some instances. This value is not returned if you specify the `NodeId` parameter.
        self.invoke_status = invoke_status
        # The custom parameters in the command.
        self.parameters = parameters
        # The execution mode of the command. Valid values:
        # 
        # - Once: The command is immediately executed.
        # 
        # - Period: The command is executed on a schedule.
        # 
        # - NextRebootOnly: The command is automatically executed the next time the instance starts.
        # 
        # - EveryReboot: The command is automatically executed every time the instance starts.
        self.repeat_mode = repeat_mode
        # The timeout period for the command execution. Unit: seconds.
        self.timeout = timeout
        # The name of the user who runs the command.
        self.username = username
        # The directory where the command is run on the instance.
        self.working_dir = working_dir

    def validate(self):
        if self.invoke_nodes:
            self.invoke_nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.command_description is not None:
            result['CommandDescription'] = self.command_description

        if self.command_name is not None:
            result['CommandName'] = self.command_name

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.invoke_nodes is not None:
            result['InvokeNodes'] = self.invoke_nodes.to_map()

        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode

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

        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('InvokeNodes') is not None:
            temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodes()
            self.invoke_nodes = temp_model.from_map(m.get('InvokeNodes'))

        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodes(DaraModel):
    def __init__(
        self,
        invoke_node: List[main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodesInvokeNode] = None,
    ):
        # The command execution records on the nodes.
        self.invoke_node = invoke_node

    def validate(self):
        if self.invoke_node:
            for v1 in self.invoke_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InvokeNode'] = []
        if self.invoke_node is not None:
            for k1 in self.invoke_node:
                result['InvokeNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invoke_node = []
        if m.get('InvokeNode') is not None:
            for k1 in m.get('InvokeNode'):
                temp_model = main_models.DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodesInvokeNode()
                self.invoke_node.append(temp_model.from_map(k1))

        return self

class DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodesInvokeNode(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        dropped: int = None,
        error_code: str = None,
        error_info: str = None,
        exit_code: int = None,
        finish_time: str = None,
        invocation_status: str = None,
        node_id: str = None,
        node_invoke_status: str = None,
        output: str = None,
        repeats: int = None,
        start_time: str = None,
        stop_time: str = None,
        timed: str = None,
        update_time: str = None,
    ):
        # The start time of the command execution.
        self.creation_time = creation_time
        # The number of characters that are truncated and discarded because the \\`Output\\` value exceeds 24 KB in size.
        self.dropped = dropped
        # The error code for a file sending failure. Valid values:
        # 
        # - Empty: The file was sent as expected.
        # 
        # - NodeNotExists: The specified instance does not exist or has been released.
        # 
        # - NodeReleased: The instance was released while the file was being sent.
        # 
        # - NodeNotRunning: The instance was not in the Running state when the file sending task was created.
        # 
        # - AccountNotExists: The specified account does not exist.
        # 
        # - ClientNotRunning: Cloud Assistant Agent is not running.
        # 
        # - ClientNotResponse: Cloud Assistant Agent is not responding.
        # 
        # - ClientIsUpgrading: Cloud Assistant Agent is being upgraded.
        # 
        # - ClientNeedUpgrade: Cloud Assistant Agent needs to be upgraded.
        # 
        # - DeliveryTimeout: The file failed to be sent due to a timeout.
        # 
        # - FileCreateFail: The file failed to be created.
        # 
        # - FileAlreadyExists: A file with the same name exists in the same path.
        # 
        # - FileContentInvalid: The file content is invalid.
        # 
        # - FileNameInvalid: The file name is invalid.
        # 
        # - FilePathInvalid: The file path is invalid.
        # 
        # - FileAuthorityInvalid: The file permissions are invalid.
        # 
        # - UserGroupNotExists: The user group specified for sending the file does not exist.
        self.error_code = error_code
        # The details about the cause of a command sending or execution failure. Valid values:
        # 
        # - Empty: The command was executed as expected.
        # 
        # - the specified node does not exist: The specified instance does not exist or has been released.
        # 
        # - the instance was released during the command execution: The instance was released during the command execution.
        # 
        # - the instance is not running when create task: The instance was not in the Running state during the command execution.
        # 
        # - the command is not applicable: The command is not applicable to the specified instance.
        # 
        # - the specified account does not exist: The specified account does not exist.
        # 
        # - the specified directory does not exist: The specified directory does not exist.
        # 
        # - the cron job expression is invalid: The specified cron expression is invalid.
        # 
        # - Cloud Assistant Agent is not running: Cloud Assistant Agent is not running.
        # 
        # - Cloud Assistant Agent is not responding: Cloud Assistant Agent is not responding.
        # 
        # - Cloud Assistant Agent is being upgraded: Cloud Assistant Agent is being upgraded.
        # 
        # - Cloud Assistant Agent needs to be upgraded: Cloud Assistant Agent needs to be upgraded.
        # 
        # - The command failed to be sent due to a timeout: The command failed to be sent due to a timeout.
        # 
        # - The command execution timed out: The command execution timed out.
        # 
        # - An exception occurred during the command execution: An exception occurred during the command execution.
        # 
        # - The command execution was interrupted: The command execution was interrupted.
        # 
        # - The command execution is complete, but the exit code is not 0: The command execution is complete, but the exit code is not 0.
        # 
        # - The instance was released while the file was being sent: The instance was released while the file was being sent.
        self.error_info = error_info
        # The exit code of the command process. Valid values:
        # 
        # - On a Linux instance, this is the exit code of the Shell process.
        # 
        # - On a Windows instance, this is the exit code of the Batch or PowerShell process.
        self.exit_code = exit_code
        # The time when the execution was complete.
        self.finish_time = finish_time
        # The execution status of the command on a single instance. Valid values:
        # 
        # - Pending: The system is verifying or sending the command.
        # 
        # - Invalid: The specified command type or parameter is incorrect.
        # 
        # - Aborted: Failed to send the command to the instance. The instance must be in the Running state and the command must be sent within 1 minute.
        # 
        # - Running: The command is running on the instance.
        # 
        # - Success:
        # 
        #   - For a one-time command: The execution is complete and the exit code is 0.
        # 
        #   - For a scheduled command: The last execution was successful with an exit code of 0, and the specified period is over.
        # 
        # - Failed:
        # 
        #   - For a one-time command: The execution is complete, but the exit code is not 0.
        # 
        #   - For a scheduled command: The last execution was successful, but the exit code was not 0. The scheduled execution will be aborted.
        # 
        # - Error: An exception occurred during the command execution and the execution cannot continue.
        # 
        # - Timeout: The command execution timed out.
        # 
        # - Cancelled: The command execution was canceled. The command was not started.
        # 
        # - Stopping: The task is being stopped.
        # 
        # - Terminated: The command was terminated during execution.
        # 
        # - Scheduled:
        # 
        #   - For a one-time command: This status is not applicable and will not occur.
        # 
        #   - For a scheduled command: The command is waiting to run.
        self.invocation_status = invocation_status
        # The ID of the node.
        self.node_id = node_id
        # The execution status of the command on a single instance.
        self.node_invoke_status = node_invoke_status
        # The output of the command.
        # 
        # - If \\`ContentEncoding\\` is set to \\`PlainText\\`, the original output is returned.
        # 
        # - If \\`ContentEncoding\\` is set to \\`Base64\\`, the Base64-encoded output is returned.
        self.output = output
        # The number of times the command has been executed on the instance.
        # 
        # - If the command is a one-time execution, the value is 0 or 1.
        # 
        # - If the command is a scheduled execution, the value is the number of times the command has been executed.
        self.repeats = repeats
        # The start time.
        self.start_time = start_time
        # The time when \\`StopInvocation\\` was called to stop the command execution.
        self.stop_time = stop_time
        # Indicates whether the command will be automatically run in the future. Valid values:
        # 
        # - true: The command is a scheduled command. The `RepeatMode` parameter was set to `Period`, `NextRebootOnly`, or `EveryReboot` when `RunCommand` or `InvokeCommand` was called.
        # 
        # - false (default): The command is a one-time command or has finished.
        # 
        #   - The `RepeatMode` parameter was set to `Once` when `RunCommand` or `InvokeCommand` was called.
        # 
        #   - The command was canceled, stopped, or has finished running.
        self.timed = timed
        # The time when the record was updated.
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

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_invoke_status is not None:
            result['NodeInvokeStatus'] = self.node_invoke_status

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

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeInvokeStatus') is not None:
            self.node_invoke_status = m.get('NodeInvokeStatus')

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

