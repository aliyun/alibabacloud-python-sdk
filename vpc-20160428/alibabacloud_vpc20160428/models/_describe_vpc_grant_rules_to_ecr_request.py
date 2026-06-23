# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcGrantRulesToEcrRequest(DaraModel):
    def __init__(
        self,
        ecr_instance_id: str = None,
        ecr_owner_id: int = None,
        instance_id: str = None,
        instance_type: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[main_models.DescribeVpcGrantRulesToEcrRequestTags] = None,
    ):
        # The ID of the Express Connect Router.
        self.ecr_instance_id = ecr_instance_id
        # The ID of the Alibaba Cloud account (main account) that owns the Express Connect Router.
        # 
        # > This parameter is required when querying a cross-account network instance.
        self.ecr_owner_id = ecr_owner_id
        # The ID of the network instance.
        self.instance_id = instance_id
        # The type of instance whose authorization rules you want to query. Valid values:
        # 
        # - **VBR**: Set the value to **VBR** to query the Virtual Private Cloud (VPC) instances authorized to connect to the specified virtual border router (VBR).
        # 
        # - **VPC**: Set the value to **VPC** to query the VBRs to which the specified VPC has granted authorization.
        self.instance_type = instance_type
        # The number of entries to return per page. Valid values: **1** to **100**. Default value: **100**.
        self.max_results = max_results
        # The token used to retrieve the next page of results. Valid values:
        # 
        # - Omit this parameter for the first request.
        # 
        # - For subsequent requests, set this to the **NextToken** value from the previous response.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the network instance is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the network instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags. You can specify up to 20 tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecr_instance_id is not None:
            result['EcrInstanceId'] = self.ecr_instance_id

        if self.ecr_owner_id is not None:
            result['EcrOwnerId'] = self.ecr_owner_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcrInstanceId') is not None:
            self.ecr_instance_id = m.get('EcrInstanceId')

        if m.get('EcrOwnerId') is not None:
            self.ecr_owner_id = m.get('EcrOwnerId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeVpcGrantRulesToEcrRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeVpcGrantRulesToEcrRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

