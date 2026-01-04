# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateFlowLogRequest(DaraModel):
    def __init__(
        self,
        aggregation_interval: int = None,
        description: str = None,
        flow_log_name: str = None,
        ip_version: str = None,
        log_store_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        project_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[main_models.CreateFlowLogRequestTag] = None,
        traffic_path: List[str] = None,
        traffic_type: str = None,
    ):
        # The sampling interval of the flow log. Unit: seconds. Valid values: **1**, **5**, and **10** (default).
        self.aggregation_interval = aggregation_interval
        # The description of the flow log.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the flow log.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.flow_log_name = flow_log_name
        self.ip_version = ip_version
        # The name of the Logstore that stores the captured traffic data.
        # 
        # *   The name can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        self.log_store_name = log_store_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the project that stores the captured traffic data.
        # 
        # *   The name can contain only lowercase letters, digits, and hyphens (-).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        self.project_name = project_name
        # The ID of the region where you want to create the flow log. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the resource whose traffic you want to capture.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource whose traffic you want to capture. Valid values:
        # 
        # *   **NetworkInterface**: elastic network interface (ENI)
        # *   **VSwitch**: all ENIs in a vSwitch
        # *   **VPC**: all ENIs in a virtual private cloud (VPC)
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag of the resource.
        self.tag = tag
        # The scope of the traffic that you want to capture. Valid values:
        # 
        # *   **all**: all traffic.
        # *   **internetGateway**: Internet traffic.
        self.traffic_path = traffic_path
        # The type of traffic that you want to capture. Valid values:
        # 
        # *   **All**: all traffic
        # *   **Allow**: traffic that is allowed
        # *   **Drop**: traffic that is rejected
        # 
        # This parameter is required.
        self.traffic_type = traffic_type

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
        if self.aggregation_interval is not None:
            result['AggregationInterval'] = self.aggregation_interval

        if self.description is not None:
            result['Description'] = self.description

        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.traffic_path is not None:
            result['TrafficPath'] = self.traffic_path

        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregationInterval') is not None:
            self.aggregation_interval = m.get('AggregationInterval')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateFlowLogRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TrafficPath') is not None:
            self.traffic_path = m.get('TrafficPath')

        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')

        return self

class CreateFlowLogRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be at most 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N to add to the resource. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `aliyun` or `acs:`.
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

