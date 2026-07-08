# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBotRuleLabelsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        label_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        sub_scene: str = None,
    ):
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of your WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of bot rule label to query.
        self.label_type = label_type
        # The number of entries to return on each page. Valid values: 1 to 200. Default value: 20.
        self.max_results = max_results
        # The token to retrieve the next page of results. This parameter is returned if a next page exists.
        # 
        # > If a value is returned for this parameter, it indicates that more results are available. Use the returned **NextToken** value in the next request to retrieve the next page of results. Repeat this process until no value is returned for this parameter. This indicates that all results have been retrieved.
        self.next_token = next_token
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The type of bot management scenario. Valid values:
        # 
        # - **web**: web protection.
        # 
        # - **app**: app protection.
        self.sub_scene = sub_scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.label_type is not None:
            result['LabelType'] = self.label_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.sub_scene is not None:
            result['SubScene'] = self.sub_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LabelType') is not None:
            self.label_type = m.get('LabelType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('SubScene') is not None:
            self.sub_scene = m.get('SubScene')

        return self

