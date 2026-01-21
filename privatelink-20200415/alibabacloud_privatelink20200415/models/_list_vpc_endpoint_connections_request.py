# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVpcEndpointConnectionsRequest(DaraModel):
    def __init__(
        self,
        connection_status: str = None,
        endpoint_id: str = None,
        endpoint_owner_id: int = None,
        eni_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        replaced_resource_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        service_id: str = None,
    ):
        # The state of the endpoint connection. Valid values:
        # 
        # *   **Pending**: The endpoint connection is being modified.
        # *   **Connecting**: The endpoint connection is being established.
        # *   **Connected**: The endpoint connection is established.
        # *   **Disconnecting**: The endpoint is being disconnected from the endpoint service.
        # *   **Disconnected**: The endpoint is disconnected from the endpoint service.
        # *   **Deleting**: The connection is being deleted.
        # *   **ServiceDeleted**: The corresponding endpoint service has been deleted.
        self.connection_status = connection_status
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The ID of the Alibaba Cloud account to which the endpoint belongs.
        self.endpoint_owner_id = endpoint_owner_id
        # The ID of the endpoint elastic network interface (ENI).
        self.eni_id = eni_id
        # The number of entries to return on each page. Valid values: **1** to **50**. Default value: **50**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If this is your first request and no next requests are to be performed, you do not need to specify this parameter.
        # *   If a next request is to be performed, set the value to the value of **NextToken** that is returned from the last call.
        self.next_token = next_token
        # The region ID of the endpoint connection.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the replaced service resource in smooth migration scenarios.
        self.replaced_resource_id = replaced_resource_id
        # The ID of the resource group to which the endpoint belongs.
        self.resource_group_id = resource_group_id
        # The service resource ID.
        self.resource_id = resource_id
        # The endpoint service ID.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_owner_id is not None:
            result['EndpointOwnerId'] = self.endpoint_owner_id

        if self.eni_id is not None:
            result['EniId'] = self.eni_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replaced_resource_id is not None:
            result['ReplacedResourceId'] = self.replaced_resource_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointOwnerId') is not None:
            self.endpoint_owner_id = m.get('EndpointOwnerId')

        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplacedResourceId') is not None:
            self.replaced_resource_id = m.get('ReplacedResourceId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        return self

