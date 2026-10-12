# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeAndroidInstanceGroupsRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        charge_type: str = None,
        instance_group_ids: List[str] = None,
        instance_group_name: str = None,
        instance_version: str = None,
        key_pair_id: str = None,
        max_results: int = None,
        next_token: str = None,
        policy_group_id: str = None,
        sale_mode: str = None,
        sort_key: str = None,
        sort_type: str = None,
        status: str = None,
        tags: List[main_models.DescribeAndroidInstanceGroupsRequestTags] = None,
    ):
        # The region ID.
        self.biz_region_id = biz_region_id
        # The billing method.
        # [_single.params.ChargeType.enum. PrePaid]Subscription.
        self.charge_type = charge_type
        # The IDs of the instance groups.
        self.instance_group_ids = instance_group_ids
        # The name of the instance group. Fuzzy match is supported.
        self.instance_group_name = instance_group_name
        # The instance version. A value of basic indicates a Wuying Cloud Phone instance, and a value of EnterpriseAi indicates a JVS Mobile instance.
        self.instance_version = instance_version
        # The ID of the key pair.
        self.key_pair_id = key_pair_id
        # The maximum number of entries to return on each page in a paging query. Valid values: 1 to 100. Default value: 100.
        self.max_results = max_results
        # The token that indicates the starting position for the query. If this parameter is left empty, the query starts from the beginning.
        self.next_token = next_token
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The purchase mode of the cloud phone.
        self.sale_mode = sale_mode
        # The sort field. A value of CreationTime indicates the creation time, and a value of ExpiredTime indicates the expiration time.
        self.sort_key = sort_key
        # The sort order. A value of ASC indicates ascending order, and a value of DESC indicates descending order.
        self.sort_type = sort_type
        # The status of the instance group.
        self.status = status
        # The tags of the instance group. You can add up to 20 tags to each instance.
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
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.instance_group_ids is not None:
            result['InstanceGroupIds'] = self.instance_group_ids

        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name

        if self.instance_version is not None:
            result['InstanceVersion'] = self.instance_version

        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        if self.sort_key is not None:
            result['SortKey'] = self.sort_key

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('InstanceGroupIds') is not None:
            self.instance_group_ids = m.get('InstanceGroupIds')

        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')

        if m.get('InstanceVersion') is not None:
            self.instance_version = m.get('InstanceVersion')

        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeAndroidInstanceGroupsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeAndroidInstanceGroupsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify 1 to 20 tag keys.
        # >Notice: A tag key can be up to 128 characters in length. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        self.key = key
        # The tag value.
        # >Notice: A tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

