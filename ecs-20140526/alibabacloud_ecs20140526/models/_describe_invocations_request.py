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
        # The command ID. You can call [DescribeCommands](https://help.aliyun.com/document_detail/64843.html) to query all available command IDs.
        self.command_id = command_id
        # The command name. This parameter does not take effect if the `InstanceId` parameter is also specified.
        self.command_name = command_name
        # The command type. Valid values:
        # 
        # - RunBatScript: Bat script that runs on Windows instances.
        # - RunPowerShellScript: PowerShell script that runs on Windows instances.
        # - RunShellScript: shell script that runs on Linux instances.
        self.command_type = command_type
        # The encoding mode of the `CommandContent` and `Output` fields in the response. Valid values:
        # 
        # - PlainText: returns the original command content and output.
        # - Base64: returns Base64-encoded command content and output.
        # 
        # Default value: Base64.
        self.content_encoding = content_encoding
        # Specifies whether to return the command output in the response.
        # 
        # - true: returns the output. You must specify at least the `InvokeId` or `InstanceId` parameter.
        # - false: does not return the output.
        # 
        # Default value: false.
        self.include_output = include_output
        # The instance ID. If you specify this parameter, all command execution records for the instance are queried.
        self.instance_id = instance_id
        # The command execution ID.
        self.invoke_id = invoke_id
        # The overall execution status of the command. The overall execution status is determined by the combined execution status across one or more instances. Valid values: 
        #          
        # - Running:
        #     - Scheduled execution: the execution status remains Running until you manually stop the scheduled command.
        #     - One-time execution: the overall status is Running if the command process is running on any instance.
        # - Finished:
        #     - Scheduled execution: the status can never be Finished.
        #     - One-time execution: all instances have completed execution, or the command process on some instances was manually stopped while the remaining instances completed execution.
        # - Success: the execution status on each instance is Stopped or Success, and at least one instance has a status of Success.
        #     - Immediate task: the command execution is complete and the exit code is 0.
        #     - Scheduled task: the most recent execution succeeded with an exit code of 0, and all specified execution times have elapsed.
        # - Failed:
        #     - Scheduled execution: the status can never be Failed.
        #     - One-time execution: all instances failed to run the command.
        # - Stopped: the command was stopped.
        # - Stopping: the command is being stopped.
        # - PartialFailed: the command succeeded on some instances but failed on others. This value does not take effect if the `InstanceId` parameter is also specified.
        # - Pending: the system is verifying or sending the command. The overall status is Pending if at least one instance has a status of Pending.
        # - Scheduled: the scheduled command has been sent and is waiting to run. The overall status is Scheduled if at least one instance has a status of Scheduled.
        self.invoke_status = invoke_status
        # The maximum number of entries per page in a paging query.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter is about to be deprecated. Use NextToken and MaxResults to perform paging queries.
        self.page_number = page_number
        # > This parameter is about to be deprecated. Use NextToken and MaxResults to perform paging queries.
        self.page_size = page_size
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The execution mode of the command. This parameter does not take effect if the `InstanceId` parameter is also specified. Valid values:
        # 
        # - Once: runs the command immediately.
        # - Period: runs the command on a schedule.
        # - NextRebootOnly: automatically runs the command the next time the instance starts.
        # - EveryReboot: automatically runs the command every time the instance starts.
        # 
        # Default value: empty, which indicates that all execution modes are queried.
        self.repeat_mode = repeat_mode
        # The ID of the resource group to which the command execution belongs. After you specify this parameter, you must also specify ResourceGroupId when you run the command. This way, the corresponding command execution results can be filtered.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        self.tag = tag
        # Specifies whether to query commands that will be automatically run in the future. Valid values:
        # 
        # - true: queries commands for which the `RepeatMode` parameter is set to `Period`, `NextRebootOnly`, or `EveryReboot` when `RunCommand` or `InvokeCommand` is called.
        # - false: queries commands that meet one of the following conditions:
        #     - The `RepeatMode` parameter is set to `Once` when `RunCommand` or `InvokeCommand` is called.
        #     - The commands have been canceled, stopped, or completed.
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
        # The tag key of the command execution. Valid values of N: 1 to 20. The tag key cannot be an empty string.
        # 
        # If you use a single tag to filter resources, the number of resources with the specified tag cannot exceed 1,000. If you use multiple tags to filter resources, the number of resources that are attached to all specified tags cannot exceed 1,000. If the resource count exceeds 1,000, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to execute the query.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the command execution. Valid values of N: 1 to 20. The tag value can be an empty string.
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

