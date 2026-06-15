# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInvocationsRequest(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        command_name: str = None,
        command_type: str = None,
        content_encoding: str = None,
        include_output: bool = None,
        instance_id: str = None,
        invoke_id: str = None,
        invoke_status: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        repeat_mode: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeInvocationsRequestTag] = None,
        timed: bool = None,
    ):
        # The command ID. You can call the [DescribeCommands](https://help.aliyun.com/document_detail/64843.html) API to query all available CommandId values.
        self.command_id = command_id
        # The command name. If the `InstanceId` parameter is also specified, this parameter does not take effect.
        self.command_name = command_name
        # The command type. Valid values:
        # 
        # - RunBatScript: The command is a Bat script that runs on a Windows instance.
        # 
        # - RunPowerShellScript: The command is a PowerShell script that runs on a Windows instance.
        # 
        # - RunShellScript: The command is a Shell script that runs on a Linux instance.
        self.command_type = command_type
        # The codec for the `CommandContent` and `Output` fields in the returned data. Valid values:
        # 
        # - PlainText: Returns the original command content and output information.
        # 
        # - Base64: Returns Base64-encoded command content and output information.
        # 
        # Default value: Base64.
        self.content_encoding = content_encoding
        # Indicates whether to return the command execution output in the results.
        # 
        # - true: Returns the output. In this case, you must specify at least one of the `InvokeId` or `InstanceId` parameters.
        # 
        # - false: Does not return the output.
        # 
        # Default value: false.
        self.include_output = include_output
        # The instance ID. If you specify this parameter, all command execution records for this instance will be queried.
        self.instance_id = instance_id
        # The command execution ID.
        self.invoke_id = invoke_id
        # The overall execution status of the command. The overall status depends on the combined execution statuses of one or more instances involved in the command execution. Valid values:
        # 
        # - Running:
        # 
        #   - Periodic execution: The status remains Running until the periodic execution is manually stopped.
        # 
        #   - One-time execution: The overall status is Running as long as any instance has a running command process.
        # 
        # - Finished:
        # 
        #   - Periodic execution: The command process cannot reach a Finished state.
        # 
        #   - One-time execution: All instances have completed execution, or some instances were manually stopped while the rest completed execution.
        # 
        # - Success: All instances have a command execution status of either Stopped or Success, and at least one instance has a status of Success. Specifically:
        # 
        #   - For immediate jobs: The command completed successfully with an exit code of 0.
        # 
        #   - For scheduled jobs: The most recent execution succeeded with an exit code of 0, and all scheduled times have been completed.
        # 
        # - Failed:
        # 
        #   - Periodic execution: The command process cannot reach a Failed state.
        # 
        #   - One-time execution: All instances failed execution.
        # 
        # - Stopped: The command was stopped.
        # 
        # - Stopping: The command is being stopped.
        # 
        # - PartialFailed: Partial failure. This value does not take effect if the `InstanceId` parameter is also specified.
        # 
        # - Pending: The system is validating or sending the command. If at least one instance has a Pending execution status, the overall status is Pending.
        # 
        # - Scheduled: The scheduled command has been sent and is waiting to run. If at least one instance has a Scheduled execution status, the overall status is Scheduled.
        self.invoke_status = invoke_status
        # The maximum number of entries per page for paged queries.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The query credential (Token). Set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter will be unpublished soon. We recommend that you use NextToken and MaxResults to perform paged queries.
        self.page_number = page_number
        # > This parameter will be unpublished soon. We recommend that you use NextToken and MaxResults to perform paged query operations.
        self.page_size = page_size
        # The Region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to view the latest Alibaba Cloud region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The execution mode of the command. This parameter does not take effect if the `InstanceId` parameter is also specified. Valid values:
        # 
        # - Once: Executes the command immediately.
        # 
        # - Period: Executes the command periodically.
        # 
        # - NextRebootOnly: Automatically executes the command the next time the instance starts.
        # 
        # - EveryReboot: Automatically executes the command every time the instance starts.
        # 
        # Default value: empty, which indicates that all modes are queried.
        self.repeat_mode = repeat_mode
        # The resource group ID of the command execution. After you specify this parameter, you must also specify ResourceGroupId when executing the command. This enables filtering to retrieve the corresponding command execution results.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag list.
        self.tag = tag
        # Indicates whether the queried command will be automatically executed in the future. Valid values:
        # 
        # - true: The command is queried when the `RepeatMode` parameter is set to `Period`, `NextRebootOnly`, or `EveryReboot` during a call to `RunCommand` or `InvokeCommand`.
        # 
        # - false: The command is queried under either of the following conditions:
        # 
        #   - The `RepeatMode` parameter is set to `Once` during a call to `RunCommand` or `InvokeCommand`.
        # 
        #   - The command has been canceled, stopped, or has finished execution.
        # 
        # Default value: false.
        self.timed = timed

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
        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.command_name is not None:
            result['CommandName'] = self.command_name

        if self.command_type is not None:
            result['CommandType'] = self.command_type

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.include_output is not None:
            result['IncludeOutput'] = self.include_output

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.timed is not None:
            result['Timed'] = self.timed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')

        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('IncludeOutput') is not None:
            self.include_output = m.get('IncludeOutput')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInvocationsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Timed') is not None:
            self.timed = m.get('Timed')

        return self

class DescribeInvocationsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key for command execution. Valid values for N are 1 to 20. If this value is specified, it cannot be an empty string.
        # 
        # When you use one tag to filter resources, the number of resources under this tag cannot exceed 1,000. When you use multiple tags to filter resources, the number of resources bound to all specified tags simultaneously cannot exceed 1,000. If the number of resources exceeds 1,000, you must use the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) API to query them.
        # 
        # The key can contain up to 64 characters, must not start with `aliyun` or `acs:`, and must not contain `http://` or `https://`.
        self.key = key
        # The tag value for command execution. Valid values for N are 1 to 20. This value can be an empty string.
        # 
        # The value can contain up to 128 characters and must not contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

