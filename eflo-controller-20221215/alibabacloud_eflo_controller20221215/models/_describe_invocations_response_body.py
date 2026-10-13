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
        # The script execution records.
        self.invocations = invocations
        # The request ID.
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
        # The file delivery record.
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
        # The command content.
        # 
        # - If ContentEncoding is set to PlainText, the original script content is returned.
        # - If ContentEncoding is set to Base64, the Base64-encoded script content is returned.
        self.command_content = command_content
        # The command description.
        self.command_description = command_description
        # The command name.
        self.command_name = command_name
        # The time when the task was created. The time is displayed in ISO 8601 format. Z in the example indicates UTC.
        self.creation_time = creation_time
        # The execution time of the scheduled command.
        self.frequency = frequency
        # The overall execution status of the command. The overall execution status depends on the common execution status across all instances in this invocation. Valid values:
        # - Pending: The system is validating or sending the command. When the command execution status on at least one instance is Pending, the overall execution status is Pending.
        # - Scheduled: The scheduled command has been sent and is waiting to run. When the command execution status on at least one instance is Scheduled, the overall execution status is Scheduled.
        # - Running: The command is running on the instance. When the command execution status on at least one instance is Running, the overall execution status is Running.
        # - Success: The command execution status on each instance is Stopped or Success, and the command execution status on at least one instance is Success. The overall execution status is Success.
        #     - One-time task: The command execution is complete and the exit code is 0.
        #     - Scheduled task: The last execution was successful with an exit code of 0, and all specified schedules have been completed.
        # - Failed: The command execution status on each instance is Stopped or Failed. The overall execution status is Failed. The return value is Failed when the command execution status on an instance is one or more of the following:
        #     - Command validation failed (Invalid).
        #     - Command delivery failed (Aborted).
        #     - Command execution completed with a non-zero exit code (Failed).
        #     - Command execution timed out (Timeout).
        #     - Command execution encountered an exception (Error).
        # - Stopping: The task is being stopped. When the command execution status on at least one instance is Stopping, the overall execution status is Stopping.
        # - Stopped: The task has been stopped. When the command execution status on all instances is Stopped, the overall execution status is Stopped. The return value is Stopped when the command execution status on an instance is one of the following:
        #     - The task was canceled (Cancelled).
        #     - The task was terminated (Terminated).
        # - PartialFailed: Some instances executed successfully while others failed. When the command execution status on each instance is Success, Failed, or Stopped, the overall execution status is PartialFailed.
        # 
        # > The InvokeStatus parameter in the response has a similar meaning, but we recommend that you check this parameter instead.
        self.invocation_status = invocation_status
        # The command execution ID.
        self.invoke_id = invoke_id
        # The command execution records.
        self.invoke_nodes = invoke_nodes
        # The overall execution status of the command. The overall execution status depends on the common execution status of one or more instances in the invocation. Valid values: 
        #          
        # - Running:
        #     - Scheduled execution: The execution status remains Running until you manually stop the scheduled command.
        #     - One-time execution: The overall execution status is Running if the command process is running on any instance.
        # - Finished:
        #     - Scheduled execution: The command process cannot have a status of Finished.
        #     - One-time execution: All instances have completed execution, or the command process was manually stopped on some instances while the remaining instances completed execution.
        # - Failed:
        #     - Scheduled execution: The command process cannot have a status of Failed.
        #     - One-time execution: All instances failed to execute the command.
        # - Stopped: The command was stopped.
        # - Stopping: The command is being stopped.
        # - PartialFailed: Partial failure. This value does not take effect if the InstanceId parameter is also specified.
        self.invoke_status = invoke_status
        # The custom parameters in the command.
        self.parameters = parameters
        # The execution mode of the command. Valid values:
        # - Once: Immediately executes the command.
        # - Period: Executes the command on a schedule.
        # - NextRebootOnly: Automatically executes the command the next time the instance starts.
        # - EveryReboot: Automatically executes the command every time the instance starts.
        self.repeat_mode = repeat_mode
        # The timeout period for the command execution. Unit: seconds.
        self.timeout = timeout
        # The username used to execute the command.
        self.username = username
        # The working directory of the command on the instance.
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
        # The command execution record on a node.
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
        # The start time of the command execution. The time is displayed in ISO 8601 format. Z in the example indicates UTC.
        self.creation_time = creation_time
        # The length of the truncated and discarded text after the text length in the Output field exceeds 24 KB.
        self.dropped = dropped
        # The error code for the file delivery failure. Valid values:
        # 
        # - Empty: The file was delivered normally.
        # - NodeNotExists: The specified instance does not exist or has been released.
        # - NodeReleased: The instance was released during file delivery.
        # - NodeNotRunning: The instance was not running when the file delivery task was created.
        # - AccountNotExists: The specified account does not exist.
        # - ClientNotRunning: The Cloud Assistant Agent is not running.
        # - ClientNotResponse: The Cloud Assistant Agent is not responding.
        # - ClientIsUpgrading: The Cloud Assistant Agent is being upgraded.
        # - ClientNeedUpgrade: The Cloud Assistant Agent needs to be upgraded.
        # - DeliveryTimeout: The file delivery timed out.
        # - FileCreateFail: The file creation failed.
        # - FileAlreadyExists: A file with the same name already exists in the same path.
        # - FileContentInvalid: The file content is invalid.
        # - FileNameInvalid: The file name is invalid.
        # - FilePathInvalid: The file path is invalid.
        # - FileAuthorityInvalid: The file permissions are invalid.
        # - UserGroupNotExists: The user group specified during file delivery does not exist.
        self.error_code = error_code
        # The details of the command delivery failure or execution failure. Valid values:
        # - Empty: The command executed normally.
        # - the specified node does not exists: The specified instance does not exist or has been released.
        # - the node has node when create task: The instance was released during command execution.
        # - the node is not running when create task: The instance was not running when the command was executed.
        # - the command is not applicable: The command is not applicable to the specified instance.
        # - the specified account does not exists: The specified account does not exist.
        # - the specified directory does not exists: The specified directory does not exist.
        # - the cron job expression is invalid: The specified execution schedule expression is invalid.
        # - the aliyun service is not running on the instance: The Cloud Assistant Agent is not running.
        # - the aliyun service in the instance does not response: The Cloud Assistant Agent is not responding.
        # - the aliyun service in the node is upgrading now: The Cloud Assistant Agent is being upgraded.
        # - the aliyun service in the node need upgrade: The Cloud Assistant Agent needs to be upgraded.
        # - the command delivery has been timeout: The command delivery timed out.
        # - the command execution has been timeout: The command execution timed out.
        # - the command execution got an exception: An exception occurred during command execution.
        # - the command execution has been interrupted: The command execution was interrupted.
        # - the command execution exit code is not zero: The command execution completed with a non-zero exit code.
        # - the specified node has been released: The instance was released during file delivery.
        self.error_info = error_info
        # The exit code of the command process. Valid values:
        # 
        # - For Linux instances, the value is the exit code of the Shell process.
        # - For Windows instances, the value is the exit code of the Bat or PowerShell process.
        self.exit_code = exit_code
        # The completion time. The time is displayed in ISO 8601 format. Z in the example indicates UTC.
        self.finish_time = finish_time
        # The command execution status on a single instance. Valid values:
        # -  Pending: The system is validating or sending the command.
        # -  Invalid: The specified command type or parameters are invalid.
        # -  Aborted: Failed to send the command to the instance. The instance must be running, and the command must be deliverable within one minute.
        # -  Running: The command is running on the instance.
        # -  Success:
        #     -  One-time command: The command execution is complete and the exit code is 0.
        #     -  Scheduled command: The last execution was successful with an exit code of 0, and the specified schedule has ended.
        # -  Failed:
        #     -  One-time command: The command execution is complete and the exit code is non-zero.
        #     -  Scheduled command: The last execution was successful with a non-zero exit code, and the specified schedule will be aborted.
        # -  Error: An exception occurred during command execution and the command cannot continue.
        # -  Timeout: The command execution timed out.
        # -  Cancelled: The command execution action was canceled and the command was never started.
        # -  Stopping: The task is being stopped.
        # -  Terminated: The command was terminated during execution.
        # -  Scheduled:
        #     -  One-time command: Not applicable. This status does not occur.
        #     -  Scheduled command: Waiting to run.
        self.invocation_status = invocation_status
        # The node ID.
        self.node_id = node_id
        # The command execution status on a single instance.
        self.node_invoke_status = node_invoke_status
        # The command output.
        # 
        # - If ContentEncoding is set to PlainText, the original output is returned.
        # - If ContentEncoding is set to Base64, the Base64-encoded output is returned.
        self.output = output
        # The number of times the command was executed on the instance.
        # -  If the execution mode is one-time execution, the value is 0 or 1.
        # -  If the execution mode is scheduled execution, the value is the number of times the command has been executed.
        self.repeats = repeats
        # The start time. The time is displayed in ISO 8601 format. Z in the example indicates UTC.
        self.start_time = start_time
        # The time when StopInvocation was called to stop the command execution. The time is displayed in ISO 8601 format. Z in the example indicates UTC.
        self.stop_time = stop_time
        # Indicates whether the queried command will be automatically executed in the future. Valid values:
        # 
        # - true: The command was executed by calling RunCommand or InvokeCommand with the RepeatMode parameter set to Period, NextRebootOnly, or EveryReboot.
        # - false (default): The queried command is in one of the following states:
        #     - The command was executed by calling RunCommand or InvokeCommand with the RepeatMode parameter set to Once.
        #     - The command has been canceled, stopped, or has completed execution.
        self.timed = timed
        # The update time. The time is displayed in ISO 8601 format. Z in the example indicates UTC.
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

