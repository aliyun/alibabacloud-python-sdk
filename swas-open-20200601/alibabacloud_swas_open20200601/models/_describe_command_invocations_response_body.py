# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeCommandInvocationsResponseBody(DaraModel):
    def __init__(
        self,
        command_invocations: List[main_models.DescribeCommandInvocationsResponseBodyCommandInvocations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of command executions.
        self.command_invocations = command_invocations
        # The page number of the query result.
        self.page_number = page_number
        # The number of entries per page settings for a paged query. This is the paging size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.command_invocations:
            for v1 in self.command_invocations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommandInvocations'] = []
        if self.command_invocations is not None:
            for k1 in self.command_invocations:
                result['CommandInvocations'].append(k1.to_map() if k1 else None)

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
        self.command_invocations = []
        if m.get('CommandInvocations') is not None:
            for k1 in m.get('CommandInvocations'):
                temp_model = main_models.DescribeCommandInvocationsResponseBodyCommandInvocations()
                self.command_invocations.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCommandInvocationsResponseBodyCommandInvocations(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        command_description: str = None,
        command_id: str = None,
        command_name: str = None,
        command_type: str = None,
        creation_time: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        invoke_instances: List[main_models.DescribeCommandInvocationsResponseBodyCommandInvocationsInvokeInstances] = None,
        parameters: str = None,
        timeout: int = None,
        username: str = None,
        working_dir: str = None,
    ):
        # The command content.
        self.command_content = command_content
        # The command description.
        self.command_description = command_description
        # The command ID.
        self.command_id = command_id
        # The command name.
        self.command_name = command_name
        # The command type.
        self.command_type = command_type
        # The time when the command was created, in the format of YYYY-MM-DDThh:mm:ss.
        self.creation_time = creation_time
        # The execution status of the command. Valid values:
        # 
        # - Pending: The system is validating or sending the command.
        # - Invalid: The specified command type or parameter is invalid.
        # - Aborted: Failed to send the command to the instance. The instance must be running and the command must be delivered within 1 minute.
        # - Running: The command is running on the instance.
        # - Success: The command execution is complete and the exit code is 0.
        # - Failed: The command execution is complete and the exit code is not 0.
        # - Error: An exception occurred during command execution and the command cannot continue.
        # - Timeout: The command execution timed out.
        # - Cancelled: The command execution action has been canceled and the command was never started.
        # - Stopping: The command execution is being stopped.
        # - Terminated: The command was terminated during execution.
        self.invocation_status = invocation_status
        # The command execution ID.
        self.invoke_id = invoke_id
        # The list of target instances for execution.
        self.invoke_instances = invoke_instances
        # The custom parameters included in the command. If no parameters exist, the default value is {}.
        self.parameters = parameters
        # The timeout period, in seconds.
        self.timeout = timeout
        # The username used to run the command.
        self.username = username
        # The path in which the command was executed.
        self.working_dir = working_dir

    def validate(self):
        if self.invoke_instances:
            for v1 in self.invoke_instances:
                 if v1:
                    v1.validate()

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

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        result['InvokeInstances'] = []
        if self.invoke_instances is not None:
            for k1 in self.invoke_instances:
                result['InvokeInstances'].append(k1.to_map() if k1 else None)

        if self.parameters is not None:
            result['Parameters'] = self.parameters

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

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        self.invoke_instances = []
        if m.get('InvokeInstances') is not None:
            for k1 in m.get('InvokeInstances'):
                temp_model = main_models.DescribeCommandInvocationsResponseBodyCommandInvocationsInvokeInstances()
                self.invoke_instances.append(temp_model.from_map(k1))

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class DescribeCommandInvocationsResponseBodyCommandInvocationsInvokeInstances(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_info: str = None,
        exit_code: int = None,
        finish_time: str = None,
        instance_id: str = None,
        invocation_status: str = None,
        output: str = None,
        start_time: str = None,
    ):
        # The error code for the command delivery failure or execution failure. Valid values:
        # 
        # - Empty: The command executed normally.
        # - InstanceNotExists: The specified instance does not exist or has been released.
        # - InstanceReleased: The instance was released during command execution.
        # - InstanceNotRunning: The instance was not running when the command was executed.
        # - CommandNotApplicable: The command is not applicable to the specified instance.
        # - AccountNotExists: The specified account does not exist.
        # - DirectoryNotExists: The specified directory does not exist.
        # - BadCronExpression: The specified cron expression is invalid.
        # - ClientNotRunning: The Cloud Assistant Agent is not running.
        # - ClientNotResponse: The Cloud Assistant Agent is not responding.
        # - ClientIsUpgrading: The Cloud Assistant Agent is being upgraded.
        # - ClientNeedUpgrade: The Cloud Assistant Agent needs to be upgraded.
        # - DeliveryTimeout: Command delivery timed out.
        # - ExecutionTimeout: Command execution timed out.
        # - ExecutionException: An exception occurred during command execution.
        # - ExecutionInterrupted: Command execution was interrupted.
        # - ExitCodeNonzero: Command execution completed with a non-zero exit code.
        self.error_code = error_code
        # The details of the command delivery failure or execution failure. Valid values:
        # 
        # - Empty: The command executed normally.
        # - the specified instance does not exists: The specified instance does not exist or has been released.
        # - the instance has released when create task: The instance was released during command execution.
        # - the instance is not running when create task: The instance was not running when the command was executed.
        # - the command is not applicable: The command is not applicable to the specified instance.
        # - the specified account does not exists: The specified account does not exist.
        # - the specified directory does not exists: The specified directory does not exist.
        # - the cron job expression is invalid: The specified cron expression is invalid.
        # - the aliyun service is not running on the instance: The Cloud Assistant Agent is not running.
        # - the aliyun service in the instance does not response: The Cloud Assistant Agent is not responding.
        # - the aliyun service in the instance is upgrading now: The Cloud Assistant Agent is being upgraded.
        # - the aliyun service in the instance need upgrade: The Cloud Assistant Agent needs to be upgraded.
        # - the command delivery has been timeout: Command delivery timed out.
        # - the command execution has been timeout: Command execution timed out.
        # - the command execution got an exception: An exception occurred during command execution.
        # - the command execution has been interrupted: Command execution was interrupted.
        # - the command execution exit code is not zero: Command execution completed with a non-zero exit code.
        self.error_info = error_info
        # The exit code of the command.
        # 
        # - For Linux instances, this is the exit code of the Shell command.
        # - For Windows instances, this is the exit code of the Bat or PowerShell command.
        self.exit_code = exit_code
        # The time when the command process ended. The time is displayed in UTC (Z) in the format of YYYY-MM-DDThh:mm:ssZ.
        self.finish_time = finish_time
        # The instance ID of the simple application server.
        self.instance_id = instance_id
        # The command execution status on a single instance. Valid values:
        # - Pending: The system is validating or sending the command.
        # - Invalid: The specified command type or parameter is invalid.
        # - Aborted: Failed to send the command to the instance. The instance must be running and the command must be delivered within 1 minute.
        # - Running: The command is running on the instance.
        # - Success:
        #     - One-time task: The command execution is complete and the exit code is 0.
        #     - Scheduled task: The last execution succeeded with an exit code of 0, and the specified schedule has ended.
        # - Failed:
        #     -  One-time task: The command execution is complete and the exit code is not 0.
        #     -  Scheduled task: The last execution succeeded with an exit code that is not 0, and the specified schedule will be aborted.
        # - Error: An exception occurred during command execution and the command cannot continue.
        # - Timeout: The command execution timed out.
        # - Cancelled: The command execution action has been canceled and the command was never started.
        # - Stopping: The task is being stopped.
        # - Terminated: The command was terminated during execution.
        self.invocation_status = invocation_status
        # The output information of the command execution.
        self.output = output
        # The time when the command started running on the instance. The time is displayed in UTC (Z) in the format of YYYY-MM-DDThh:mm:ssZ.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.output is not None:
            result['Output'] = self.output

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

