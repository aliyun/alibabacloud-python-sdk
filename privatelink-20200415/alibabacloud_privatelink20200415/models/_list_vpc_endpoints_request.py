# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class ListVpcEndpointsRequest(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        connection_status: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        endpoint_status: str = None,
        endpoint_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_name: str = None,
        service_region_id: str = None,
        tag: List[main_models.ListVpcEndpointsRequestTag] = None,
        vpc_id: str = None,
    ):
        # The IP version. Valid values:
        # 
        # - **IPv4**: IPv4
        # 
        # - **DualStack**: dual stack
        self.address_ip_version = address_ip_version
        # The connection state of the endpoint. Valid values:
        # 
        # - **Pending**: The endpoint connection is being modified.
        # 
        # - **Connecting**: The endpoint is connecting.
        # 
        # - **Connected**: The endpoint is connected.
        # 
        # - **Disconnecting**: The endpoint is disconnecting.
        # 
        # - **Disconnected**: The endpoint is disconnected.
        # 
        # - **Deleting**: The endpoint is being deleted.
        # 
        # - **ServiceDeleted**: The endpoint service with which the endpoint is associated has been deleted.
        self.connection_status = connection_status
        # The ID of the endpoint.
        self.endpoint_id = endpoint_id
        # The name of the endpoint.
        self.endpoint_name = endpoint_name
        # The status of the endpoint. Valid values:
        # 
        # - **Creating**: The endpoint is being created.
        # 
        # - **Active**: The endpoint is available.
        # 
        # - **Pending**: The endpoint is being modified.
        # 
        # - **Deleting**: The endpoint is being deleted.
        self.endpoint_status = endpoint_status
        # The type of the endpoint. Valid values:
        # 
        # - **Interface**: an interface endpoint
        # 
        # - **Reverse**: a reverse endpoint
        # 
        # - **GatewayLoadBalancer**: a Gateway Load Balancer-type endpoint
        self.endpoint_type = endpoint_type
        # The number of entries to return on each page. Valid values: **1** to **1000**. Default value: **50**.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        # 
        # - If this is your first query or no next page is available, you do not need to specify this parameter.
        # 
        # - If a next page is available, set the value to the **NextToken** value that is returned from the previous call.
        self.next_token = next_token
        # The ID of the region where the endpoint is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The name of the endpoint service with which the endpoint is associated.
        self.service_name = service_name
        # The ID of the region where the endpoint service is deployed.
        self.service_region_id = service_region_id
        # The tags.
        self.tag = tag
        # The ID of the VPC to which the endpoint belongs.
        self.vpc_id = vpc_id

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
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.endpoint_status is not None:
            result['EndpointStatus'] = self.endpoint_status

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('EndpointStatus') is not None:
            self.endpoint_status = m.get('EndpointStatus')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListVpcEndpointsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListVpcEndpointsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify up to 20 tag values. The tag value can be an empty string.
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

