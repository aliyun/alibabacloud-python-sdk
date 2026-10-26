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
        # The command ID. You can call the [DescribeCommands](https://help.aliyun.com/document_detail/64843.html) operation to query all available command IDs.
        self.command_id = command_id
        # The command name. This parameter does not take effect if the InstanceId parameter is also specified.
        self.command_name = command_name
        # The command type. Valid values:
        # 
        # - RunBatScript: The command is a batch script that runs on a Windows instance.
        # - RunPowerShellScript: The command is a PowerShell script that runs on a Windows instance.
        # - RunShellScript: The command is a shell script that runs on a Linux instance.
        self.command_type = command_type
        # The encoding method of the CommandContent and Output fields in the response. Valid values:
        # 
        # - PlainText: returns the original command content and output.
        # - Base64: returns the Base64-encoded command content and output.
        # 
        # Default value: Base64.
        self.content_encoding = content_encoding
        # Specifies whether to return the output of the command execution in the response. Valid values:
        # 
        # - true: The output is returned. In this case, you must specify at least the InvokeId or InstanceId parameter.
        # - false: The output is not returned.
        # 
        # Default value: false.
        self.include_output = include_output
        # The instance ID. If you specify this parameter, the system queries all command execution records of the instance.
        self.instance_id = instance_id
        # The execution ID of the command.
        self.invoke_id = invoke_id
        # The overall execution status of the command. The overall execution status depends on the combined execution status of one or more instances involved in the execution. Valid values: 
        #          
        # - Running:
        #     - Scheduled execution: The execution status remains Running until the scheduled command is manually stopped.
        #     - One-time execution: The overall execution status is Running as long as a command process is running.
        # - Finished:
        #     - Scheduled execution: The command process cannot be finished.
        #     - One-time execution: All instances have completed the execution. Alternatively, the command processes on some instances are manually stopped, and the execution on the remaining instances is completed.
        # - Success: The command execution status on each instance is Stopped or Success, and the command execution status on at least one instance is Success.
        #     - Immediately run tasks: The command execution is completed, and the exit code is 0.
        #     - Scheduled tasks: The most recent execution is successful, the exit code is 0, and the specified schedule has ended.
        # - Failed:
        #     - Scheduled execution: The command process cannot fail.
        #     - One-time execution: The execution fails on all instances.
        # - Stopped: The command is stopped.
        # - Stopping: The command is being stopped.
        # - PartialFailed: The execution partially fails. This value does not take effect if the InstanceId parameter is also specified.
        # - Pending: The system is verifying or sending the command. The overall execution status is Pending if the command execution status on at least one instance is Pending.
        # - Scheduled: The scheduled command has been sent and is waiting to be run. The overall execution status is Scheduled if the command execution status on at least one instance is Scheduled.
        self.invoke_status = invoke_status
        # The maximum number of entries per page for paging.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token. Set the value to the NextToken value returned from the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter will soon be taken offline. We recommend that you use NextToken and MaxResults for paging and paged query operations.
        self.page_number = page_number
        # > This parameter will soon be taken offline. We recommend that you use NextToken and MaxResults for paging and paged query operations.
        self.page_size = page_size
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The execution mode of the command. This parameter does not take effect if the InstanceId parameter is also specified. Valid values:
        # 
        # - Once: runs the command immediately.
        # - Period: runs the command on a schedule.
        # - NextRebootOnly: automatically runs the command the next time the instance starts.
        # - EveryReboot: automatically runs the command every time the instance starts.
        # 
        # Default value: empty. An empty value indicates that all execution modes are queried.
        self.repeat_mode = repeat_mode
        # The ID of the resource group to which the command execution belongs. If you specify this parameter, you must also specify ResourceGroupId when you run the command. This allows you to filter the corresponding command execution results.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        self.tag = tag
        # Specifies whether the queried command will be automatically run in the future. Valid values:
        # 
        # - true: Queries commands for which the RepeatMode parameter is set to Period, NextRebootOnly, or EveryReboot when you call RunCommand or InvokeCommand to run the commands.
        # - false: Queries commands in the following states:
        #     - Commands for which the RepeatMode parameter is set to Once when you call RunCommand or InvokeCommand to run the commands.
        #     - Commands that have been canceled, stopped, or completed.
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
        # The tag key of the command to execute. Valid values of N: 1 to 20. The tag key cannot be an empty string.
        # 
        # If you use a single tag to filter resources, the resource count returned cannot exceed 1,000. If you use multiple tags to filter resources, the resource count of resources that have all the specified tags attached cannot exceed 1,000. If the resource count exceeds 1,000, use the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query the resources.
        # 
        # The tag key can be up to 64 characters in length. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        self.key = key
        # The tag value of the command execution. Valid values of N: 1 to 20. The tag value can be an empty string.
        # The tag value can be up to 128 characters in length and cannot contain http:// or https://.
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

