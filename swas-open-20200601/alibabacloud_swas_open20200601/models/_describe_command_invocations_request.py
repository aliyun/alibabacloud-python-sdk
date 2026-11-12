# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCommandInvocationsRequest(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        command_name: str = None,
        command_type: str = None,
        instance_id: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        # The command ID. You can call [DescribeCommands](https://help.aliyun.com/document_detail/64843.html) to query all available command IDs.
        self.command_id = command_id
        # The command name. If the InstanceId parameter is also specified, this parameter does not take effect.
        self.command_name = command_name
        # The command type. Valid values:
        # 
        # - RunBatScript: Bat command for Windows instances.
        # - RunPowerShellScript: PowerShell command for Windows instances.
        # - RunShellScript: Shell command for Linux instances.
        self.command_type = command_type
        # The instance ID of the simple application server.
        self.instance_id = instance_id
        # The overall execution status of the command. The overall execution status depends on the common execution status across all instances in this invocation. Valid values:
        # -  Pending: The system is validating or sending the command. If the command execution status on at least one instance is Pending, the overall execution status is Pending.
        # -  Running: The command is running on instances. If the command execution status on at least one instance is Running, the overall execution status is Running.
        # -  Success: The command execution status on each instance is Stopped or Success, and the command execution status on at least one instance is Success. In this case, the overall execution status is Success.
        #     -  One-time task: The command execution is complete and the exit code is 0.
        # -  Failed: The command execution status on each instance is Stopped or Failed. In this case, the overall execution status is Failed. The overall execution status is Failed when the command execution status on an instance is one or more of the following values:
        #     - Command validation failed (Invalid).
        #     - Command sending failed (Aborted).
        #     - Command execution is complete but the exit code is not 0 (Failed).
        #     - Command execution timed out (Timeout).
        #     - Command execution encountered an exception (Error).
        # -  Stopping: The task is being stopped. If the command execution status on at least one instance is Stopping, the overall execution status is Stopping.
        # -  Stopped: The task is stopped. If the command execution status on all instances is Stopped, the overall execution status is Stopped. The overall execution status is Stopped when the command execution status on an instance is one of the following values:
        #     - Task canceled (Cancelled).
        #     - Task terminated (Terminated).
        # -  PartialFailed: The command execution succeeded on some instances and failed on others. If the command execution status on each instance is Success, Failed, or Stopped, the overall execution status is PartialFailed.
        # > The `InvokeStatus` response parameter has a similar meaning, but we recommend that you check the value of this parameter.
        self.invocation_status = invocation_status
        # The command execution ID.
        self.invoke_id = invoke_id
        # The page number. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page for a paged query.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID. You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.command_name is not None:
            result['CommandName'] = self.command_name

        if self.command_type is not None:
            result['CommandType'] = self.command_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')

        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

