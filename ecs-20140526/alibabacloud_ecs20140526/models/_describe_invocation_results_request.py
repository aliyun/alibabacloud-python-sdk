# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInvocationResultsRequest(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        content_encoding: str = None,
        include_history: bool = None,
        instance_id: str = None,
        invoke_id: str = None,
        invoke_record_status: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeInvocationResultsRequestTag] = None,
    ):
        # The command ID.
        self.command_id = command_id
        # The encoding method of the `CommandContent` and `Output` fields in the response. Valid values:
        # - PlainText: Returns the original command content and output.
        # - Base64: Returns the Base64-encoded command content and output.
        # 
        # Default value: Base64.
        self.content_encoding = content_encoding
        # Specifies whether to return the execution history of scheduled commands. Valid values:
        # 
        #  - true: Returns the execution results of scheduled commands. When this parameter is set to true, the InvokeId parameter is required and must be the execution ID of a scheduled command (RepeatMode is Period) or a command that runs at each system startup (RepeatMode is EveryReboot).
        #  - false: Does not return the execution history.
        # 
        # Default value: false.
        self.include_history = include_history
        # The instance ID.
        self.instance_id = instance_id
        # The command execution ID. You can call [DescribeInvocations](https://help.aliyun.com/document_detail/64840.html) to query the InvokeId.
        self.invoke_id = invoke_id
        # The execution status of the command. Valid values:
        # 
        # - Running: The command is running.
        #     - Scheduled execution: The execution status remains running until you manually stop the scheduled command.
        #     - One-time execution: The overall execution status is running as long as any command process is running.
        # - Finished: The command execution is complete.
        #     - Scheduled execution: The command process cannot have a status of finished.
        #     - One-time execution: All instances have completed execution, or you manually stopped the command process on some instances and the remaining instances have completed execution.
        # - Success:
        #     - One-time execution: The command execution is complete and the exit code is 0.
        #     - Scheduled execution: The last execution succeeded with an exit code of 0, and the specified execution time has ended.
        # - Failed: The command execution failed.
        #     - Scheduled execution: The command process cannot have a status of failed.
        #     - One-time execution: The command execution failed on all instances.
        # - PartialFailed: The command execution partially failed.
        #     - Scheduled execution: The command process cannot have a status of partially failed.
        #     - One-time execution: The command execution failed on some instances, so the overall execution status is partially failed.
        # - Stopped: The command execution has been stopped.
        # - Stopping: The command execution is being stopped.
        self.invoke_record_status = invoke_record_status
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
        # > This parameter is about to go offline. Use NextToken and MaxResults to complete paging query operations.
        self.page_number = page_number
        # > This parameter is about to go offline. Use NextToken and MaxResults to complete paging query operations.
        self.page_size = page_size
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the command execution. After you specify this parameter, the resource group ID must also be specified when you run the command. This parameter filters the corresponding command execution results.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        self.tag = tag

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

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.include_history is not None:
            result['IncludeHistory'] = self.include_history

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('IncludeHistory') is not None:
            self.include_history = m.get('IncludeHistory')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInvocationResultsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInvocationResultsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the command execution. Valid values of N: 1 to 20. The tag key cannot be an empty string.
        # 
        # If you use a single tag to filter resources, the number of resources with this tag cannot exceed 1,000. If you use multiple tags to filter resources, the number of resources with all specified tags attached cannot exceed 1,000. If the number of resources exceeds 1,000, call [ListTagResources](https://help.aliyun.com/document_detail/110425.html) to execute the query.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the command execution. Valid values of N: 1 to 20. The tag value can be an empty string.
        # 
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

