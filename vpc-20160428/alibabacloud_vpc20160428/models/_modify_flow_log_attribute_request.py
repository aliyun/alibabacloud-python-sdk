# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyFlowLogAttributeRequest(DaraModel):
    def __init__(
        self,
        aggregation_interval: int = None,
        description: str = None,
        flow_log_id: str = None,
        flow_log_name: str = None,
        ip_version: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The new sampling interval of the flow log. Unit: minutes. Valid values: **1**, **5**, and **10**.
        self.aggregation_interval = aggregation_interval
        # The new description of the flow log.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The ID of the flow log.
        # 
        # This parameter is required.
        self.flow_log_id = flow_log_id
        # The new name of the flow log.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.flow_log_name = flow_log_name
        # The version of the IP address. Valid values:
        # 
        # *   **IPV4**: the IPv4 address.
        # *   **DualStack**: includes IPv4 and IPv6 address
        self.ip_version = ip_version
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the flow log is created.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregation_interval is not None:
            result['AggregationInterval'] = self.aggregation_interval

        if self.description is not None:
            result['Description'] = self.description

        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregationInterval') is not None:
            self.aggregation_interval = m.get('AggregationInterval')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

