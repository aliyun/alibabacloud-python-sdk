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
        # The command execution record.
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
        # The file sending records.
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
        # The executed command.
        # 
        # *   If ContentEncoding is set to PlainText in the request, the original command content is returned.
        # *   If ContentEncoding is set to Base64 in the request, the Base64-encoded command content is returned.
        self.command_content = command_content
        # The command description.
        self.command_description = command_description
        # The command name.
        self.command_name = command_name
        # The time when the command task was created.
        self.creation_time = creation_time
        # The schedule on which the command was run.
        self.frequency = frequency
        # The overall execution state of the command task. The value of this parameter depends on the execution states of the command task on all the involved instances. Valid values:
        # 
        # *   Pending: The command was being verified or sent. If the execution state on at least one instance is Pending, the overall execution state is Pending.
        # 
        # *   Scheduled: The command that is set to run on a schedule is sent and waiting to be run. If the execution state on at least one instance is Scheduled, the overall execution state is Scheduled.
        # 
        # *   Running: The command is being run on the instance. When the execution state on at least one instance is Running, the overall execution state is Running.
        # 
        # *   Success: When the execution state on at least one instance is Success and the execution state on the other instances is Stopped or Success, the overall execution state is Success.
        # 
        #     *   One-time task: The execution is complete, and the exit code is 0.
        #     *   Scheduled task: The last execution was complete, the exit code was 0, and the specified period ended.
        # 
        # *   Failed: When the execution state on all instances is Stopped or Failed, the overall execution state is Failed. When the execution state on an instance is one of the following values, Failed is returned as the overall execution state:
        # 
        #     *   Invalid: The command is invalid.
        #     *   Aborted: The command failed to be sent.
        #     *   Failed: The execution was complete, but the exit code was not 0.
        #     *   Timeout: The execution timed out.
        #     *   Error: An error occurred while the command was being run.
        # 
        # *   Stopping: The command task is being stopped. When the execution state on at least one instance is Stopping, the overall execution state is Stopping.
        # 
        # *   Stopped: The task was stopped. When the execution state on all instances is Stopped, the overall execution state is Stopped. When the execution state on an instance is one of the following values, Stopped is returned as the overall execution state:
        # 
        #     *   Cancelled: The task was canceled.
        #     *   Terminated: The task was terminated.
        # 
        # *   PartialFailed: The execution was complete on some instances and failed on other instances. When the execution state is Success on some instances and is Failed or Stopped on the other instances, the overall execution state is PartialFailed.
        # 
        # >  The value of the `InvokeStatus` response parameter is similar to the value of InvocationStatus. We recommend that you ignore InvokeStatus and check the value of InvocationStatus.
        self.invocation_status = invocation_status
        # The execution ID.
        self.invoke_id = invoke_id
        # The command execution records.
        self.invoke_nodes = invoke_nodes
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
        self.invoke_status = invoke_status
        # The custom parameters in the command.
        self.parameters = parameters
        # The execution mode of the command. Valid values:
        # 
        # *   Once: The command is run immediately.
        # *   Period: The command is run on a schedule.
        # *   NextRebootOnly: The command is run the next time the instances start.
        # *   EveryReboot: runs the command every time the instances start.
        self.repeat_mode = repeat_mode
        # The timeout period for the command execution. Unit: seconds.
        self.timeout = timeout
        # The username that is used to run the command.
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
        # The command execution records of the node.
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
        # The start time of the execution.
        self.creation_time = creation_time
        # The size of the Output text that was truncated and discarded because the Output value exceeded 24 KB in size.
        self.dropped = dropped
        # The error code returned when the file failed to be sent to the instance. Valid values:
        # 
        # *   Null: The file is sent to the instance.
        # *   NodeNotExists: The specified instance does not exist or has been released.
        # *   NodeReleased: The instance was released while the file was being sent.
        # *   NodeNotRunning: The instance was not running while the file sending task was being created.
        # *   AccountNotExists: The specified account does not exist.
        # *   ClientNotRunning: Cloud Assistant Agent is not running.
        # *   ClientNotResponse: Cloud Assistant Agent does not respond.
        # *   ClientIsUpgrading: Cloud Assistant Agent is being upgraded.
        # *   ClientNeedUpgrade: Cloud Assistant Agent needs to be upgraded.
        # *   DeliveryTimeout: The file sending task timed out.
        # *   FileCreateFail: The file failed to be created.
        # *   FileAlreadyExists: A file with the same name exists in the specified directory.
        # *   FileContentInvalid: The file content is invalid.
        # *   FileNameInvalid: The file name is invalid.
        # *   FilePathInvalid: The specified directory is invalid.
        # *   FileAuthorityInvalid: The specified permissions on the file are invalid.
        # *   UserGroupNotExists: The specified user group does not exist.
        self.error_code = error_code
        # The error message returned when the command cannot be sent or run.
        # 
        # *   If this parameter is empty, the command was run as expected.
        # *   the specified node does not exists: The specified instance does not exist or is released.
        # *   the node has node when create task: The instance is released when the command is being run.
        # *   the node is not running when create task: The instance is not in the Running state while the command is being run.
        # *   the command is not applicable: The command is not applicable to the specified instance.
        # *   the specified account does not exists: The specified account does not exist.
        # *   the specified directory does not exists: The specified directory does not exist.
        # *   the cron job expression is invalid: The cron expression that specifies the execution time is invalid.
        # *   the aliyun service is not running on the instance: Cloud Assistant Agent is not running.
        # *   the aliyun service in the instance does not response: Cloud Assistant Agent does not respond.
        # *   the aliyun service in the node is upgrading now: Cloud Assistant Agent is being upgraded.
        # *   the aliyun service in the node need upgrade: Cloud Assistant Agent needs to be upgraded.
        # *   the command delivery has been timeout: The request to send the command timed out.
        # *   the command execution has been timeout: The command execution timed out.
        # *   the command execution got an exception: An exception occurred when the command is being run.
        # *   the command execution has been interrupted: The command execution is interrupted.
        # *   the command execution exit code is not zero: The command execution completes, but the exit code is not 0.
        # *   the specified node has been released: The instance is released while the file is being sent.
        self.error_info = error_info
        # The exit code of the execution. Valid values:
        # 
        # *   For Linux instances, the value is the exit code of the shell process.
        # *   For Windows instances, the value is the exit code of the batch or PowerShell process.
        self.exit_code = exit_code
        # The end time of the execution.
        self.finish_time = finish_time
        # The execution status of the command on a single instance. Valid values:
        # 
        # *   Pending: The command was being verified or sent.
        # 
        # *   Invalid: The specified command type or parameter is invalid.
        # 
        # *   Aborted: The command failed to be sent to the instance. To send a command to an instance, make sure that the instance is in the Running state and the command can be sent to the instance within 1 minute.
        # 
        # *   Running: The command is being run on the instance.
        # 
        # *   Success:
        # 
        #     *   One-time task: The execution was complete, and the exit code was 0.
        #     *   Recurring execution: The previous occurrence of the execution is complete, and the exit code is 0. The specified recurring period during which the command is run ends.
        # 
        # *   Failed:
        # 
        #     *   One-time task: The execution was complete, but the exit code was not 0.
        #     *   Recurring execution: The previous occurrence of the execution is complete, but the exit code is not 0. The specified recurring period during which the command is run is about to end.
        # 
        # *   Error: The execution cannot proceed due to an exception.
        # 
        # *   Timeout: The execution timed out.
        # 
        # *   Cancelled: The execution was canceled before it started.
        # 
        # *   Stopping: The command task is being stopped.
        # 
        # *   Terminated: The execution was terminated before completion.
        # 
        # *   Scheduled:
        # 
        #     *   One-time task: The execution state can never be Scheduled.
        #     *   Recurring execution: The command is waiting to be run.
        self.invocation_status = invocation_status
        # The node ID.
        self.node_id = node_id
        # The execution status of the command on a single instance.
        self.node_invoke_status = node_invoke_status
        # The command output.
        # 
        # *   If ContentEncoding is set to PlainText in the request, the original command output is returned.
        # *   If ContentEncoding is set to Base64 in the request, the Base64-encoded command output is returned.
        self.output = output
        # The number of times that the command was run on the instance.
        # 
        # *   If the command is set to run only once, the value is 0 or 1.
        # *   If the command is set to run on a schedule, the value is the number of times that the command has been run on the instance.
        self.repeats = repeats
        # The start time.
        self.start_time = start_time
        # The time when the command task was stopped. If you call the StopInvocation operation to stop the command task, the value of this parameter is the time when the operation is called.
        self.stop_time = stop_time
        # Indicates whether the command is to be automatically run. Valid values:
        # 
        # *   true: The command is run by calling the `RunCommand` or `InvokeCommand` operation with `RepeatMode` set to `Period`, `NextRebootOnly`, or `EveryReboot`.
        # 
        # *   false (default): The command meets the following requirements.
        # 
        #     *   The command is run by calling the `RunCommand` or `InvokeCommand` operation with `RepeatMode` set to `Once`.
        #     *   The command task is canceled, stopped, or completed.
        self.timed = timed
        # The update time of the execution.
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

