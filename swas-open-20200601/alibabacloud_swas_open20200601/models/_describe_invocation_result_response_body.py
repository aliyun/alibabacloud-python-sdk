# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeInvocationResultResponseBody(DaraModel):
    def __init__(
        self,
        invocation_result: main_models.DescribeInvocationResultResponseBodyInvocationResult = None,
        request_id: str = None,
    ):
        # The command execution result.
        self.invocation_result = invocation_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.invocation_result:
            self.invocation_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invocation_result is not None:
            result['InvocationResult'] = self.invocation_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvocationResult') is not None:
            temp_model = main_models.DescribeInvocationResultResponseBodyInvocationResult()
            self.invocation_result = temp_model.from_map(m.get('InvocationResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInvocationResultResponseBodyInvocationResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_info: str = None,
        exit_code: int = None,
        finished_time: str = None,
        instance_id: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        invoke_record_status: str = None,
        invoke_user: str = None,
        output: str = None,
        start_time: str = None,
    ):
        # The error code for the reason why the command failed to be sent or run. Valid values:
        # 
        # - Empty: The command was run normally.
        # - InstanceNotExists: The specified instance does not exist or has been released.
        # - InstanceReleased: The instance was released during command execution.
        # - InstanceNotRunning: The instance was not in the Running state when the command was run.
        # - CommandNotApplicable: The command is not applicable to the specified instance.
        # - AccountNotExists: The specified account does not exist.
        # - DirectoryNotExists: The specified directory does not exist.
        # - BadCronExpression: The specified cron expression is invalid.
        # - ClientNotRunning: The Cloud Assistant Agent is not running.
        # - ClientNotResponse: The Cloud Assistant Agent is not responding.
        # - ClientIsUpgrading: The Cloud Assistant Agent is being upgraded.
        # - ClientNeedUpgrade: The Cloud Assistant Agent needs to be upgraded.
        # - DeliveryTimeout: The command sending timed out.
        # - ExecutionTimeout: The command execution timed out.
        # - ExecutionException: An exception occurred during command execution.
        # - ExecutionInterrupted: The command execution was interrupted.
        # - ExitCodeNonzero: The command finished running, and the exit code is not 0.
        self.error_code = error_code
        # The details of the reason why the command failed to be sent or run. Valid values:
        # 
        # - Empty: The command was run normally.
        # - the specified instance does not exists: The specified instance does not exist or has been released.
        # - the instance has released when create task: The instance was released during command execution.
        # - the instance is not running when create task: The instance was not in the Running state when the command was run.
        # - the command is not applicable: The command is not applicable to the specified instance.
        # - the specified account does not exists: The specified account does not exist.
        # - the specified directory does not exists: The specified directory does not exist.
        # - the cron job expression is invalid: The specified cron expression is invalid.
        # - the aliyun service is not running on the instance: The Cloud Assistant Agent is not running.
        # - the aliyun service in the instance does not response: The Cloud Assistant Agent is not responding.
        # - the aliyun service in the instance is upgrading now: The Cloud Assistant Agent is being upgraded.
        # - the aliyun service in the instance need upgrade: The Cloud Assistant Agent needs to be upgraded.
        # - the command delivery has been timeout: The command sending timed out.
        # - the command execution has been timeout: The command execution timed out.
        # - the command execution got an exception: An exception occurred during command execution.
        # - the command execution has been interrupted: The command execution was interrupted.
        # - the command execution exit code is not zero: The command finished running, and the exit code is not 0.
        self.error_info = error_info
        # The exit code of the command.
        # 
        # - For Linux instances, the exit code is the exit code of the shell command.
        # - For Windows instances, the exit code is the exit code of the Bat or PowerShell command.
        self.exit_code = exit_code
        # The time when the command finished running on the instance. The time is displayed in UTC (Z) in the YYYY-MM-DDThh:mm:ssZ format.
        self.finished_time = finished_time
        # The instance ID of the simple application server.
        self.instance_id = instance_id
        # The execution status of the command on the instance. Valid values:
        # 
        # - Pending: The system is verifying or sending the command.
        # - Invalid: The specified command type or parameter is invalid.
        # - Aborted: Failed to send the command to the instance. The instance must be in the Running state, and the command must be sent within 1 minute.
        # - Running: The command is being run on the instance.
        # - Success: The command finished running, and the exit code is 0.
        # - Failed: The command finished running, and the exit code is not 0.
        # - Error: An exception occurred during command execution and the command cannot continue.
        # - Timeout: The command execution timed out.
        # - Cancelled: The command execution has been canceled, and the command was never started.
        # - Stopping: The running command is being stopped.
        # - Terminated: The command was terminated during execution.
        self.invocation_status = invocation_status
        # The command execution ID.
        self.invoke_id = invoke_id
        # The command execution status. Valid values:
        # 
        # - Running: Running.
        # - Finished: Finished.
        # - Failed: Failed.
        # - Stopped: Stopped.
        self.invoke_record_status = invoke_record_status
        # The username used to run the command on the simple application server.
        self.invoke_user = invoke_user
        # The output of the command execution. The standard output (stdout) and standard error output (stderr) are merged into a single Output. The capacity is calculated separately for each execution and each instance. The maximum capacity of a single Output is 24 KB. Content that exceeds this limit is truncated and discarded. Even if the ExitCode is 0 or the execution status is Success, the output may still be truncated. The returned output is in UTF-8 plaintext and does not require Base64 decoding.
        self.output = output
        # The time when the command started to be run on the instance. The time is displayed in UTC (Z) in the YYYY-MM-DDThh:mm:ssZ format.
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

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status

        if self.invoke_user is not None:
            result['InvokeUser'] = self.invoke_user

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

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')

        if m.get('InvokeUser') is not None:
            self.invoke_user = m.get('InvokeUser')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

