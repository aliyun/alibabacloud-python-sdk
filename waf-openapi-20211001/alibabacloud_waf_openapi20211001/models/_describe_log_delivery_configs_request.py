# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLogDeliveryConfigsRequest(DaraModel):
    def __init__(
        self,
        delivery_name_like: str = None,
        delivery_type: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The name of the delivery configuration to query. You can set this parameter to perform a fuzzy match on a delivery configuration.
        self.delivery_name_like = delivery_name_like
        # The type of the delivery configuration to query. Valid values:
        # 
        # - **syslog**: Delivers logs to a Syslog service.
        # - **kafka**: Delivers logs to a Kafka service.
        self.delivery_type = delivery_type
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to obtain the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries to return per page during paging in a paged query. Valid values: 1 to 50. Default value: 20.
        self.max_results = max_results
        # The pagination token for querying the next page. Set the value to the **NextToken** value returned from the previous API call. This parameter is not required for the first query.
        self.next_token = next_token
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland
        # 
        # - **ap-southeast-1**: outside the Chinese mainland
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_name_like is not None:
            result['DeliveryNameLike'] = self.delivery_name_like

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryNameLike') is not None:
            self.delivery_name_like = m.get('DeliveryNameLike')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

