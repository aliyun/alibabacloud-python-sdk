# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSendFileResultsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeSendFileResultsRequestTag] = None,
    ):
        # The instance ID. If you specify this parameter, all file delivery records of the instance are queried.
        self.instance_id = instance_id
        # The overall delivery status of the file. The overall status depends on the combined execution status of all instances involved in the delivery task. Valid values:
        # 
        # - Pending: The system is verifying or delivering the file. If the file delivery status of at least one instance is Pending, the overall execution status is Pending.
        # - Running: The file is being delivered to the instances. If the file delivery status of at least one instance is Running, the overall execution status is Running.
        # - Success: The file is delivered successfully. If the file delivery status of all instances is Success, the overall execution status is Success.
        # - Failed: The file fails to be delivered. If the file delivery status of all instances is Failed, the overall execution status is Failed.
        # - PartialFailed: The file is delivered to some instances but fails to be delivered to others. If the file delivery status of all instances is either Success or Failed, the overall execution status is PartialFailed.
        self.invocation_status = invocation_status
        # The execution ID.
        self.invoke_id = invoke_id
        # The maximum number of entries per page for a paged query.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The name of the file. If you specify this parameter, all delivery records of the file with the specified name are queried.
        self.name = name
        # The query token. Set the value to the NextToken value returned from the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter will soon be deprecated. We recommend that you use NextToken and MaxResults for paging.
        self.page_number = page_number
        # > This parameter will soon be deprecated. We recommend that you use NextToken and MaxResults for paging.
        self.page_size = page_size
        # The region ID of the ECS instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the file delivery task belongs. If you specify this parameter, you must also specify ResourceGroupId when you deliver the file. This allows you to filter the corresponding file delivery results.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

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
                temp_model = main_models.DescribeSendFileResultsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeSendFileResultsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the file delivery task. Valid values of N: 1 to 20. If you specify this parameter, it cannot be an empty string.
        # 
        # If you use a single tag to filter resources, the resource count queried under the tag cannot exceed 1,000. If you use multiple tags to filter resources, the resource count of resources attached with multiple tags at the same time cannot exceed 1,000. If the resource count exceeds 1,000, you must call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query the resources.
        # 
        # The tag key can be up to 64 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the file delivery task. Valid values of N: 1 to 20. This parameter can be an empty string.
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

