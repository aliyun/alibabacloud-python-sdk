# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNetworkAccessEndpointsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        network_access_endpoint_status: str = None,
        network_access_endpoint_type: str = None,
        next_token: str = None,
        vpc_id: str = None,
        vpc_region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum number of entries per page for a paged query. Maximum value: 100.
        self.max_results = max_results
        # The status of the network access endpoint. Valid values:
        #  
        # - pending: Pending initialization.
        # - creating: Being created.
        # - running: Running.
        # - deleting: Being deleted.
        # 
        # This parameter does not take effect when NetworkAccessEndpointType is set to shared.
        self.network_access_endpoint_status = network_access_endpoint_status
        # The type of the network access endpoint. Valid values:
        # 
        # - shared: shared network access endpoint.
        # - private: dedicated network access endpoint.
        # 
        # Default value: private.
        self.network_access_endpoint_type = network_access_endpoint_type
        # The pagination token. Set this parameter to the NextToken value returned in the previous API call. Leave this parameter empty for the first query.
        self.next_token = next_token
        # The VPC ID of the dedicated network access endpoint. This parameter does not take effect when NetworkAccessEndpointType is set to shared.
        self.vpc_id = vpc_id
        # The region of the VPC for the dedicated network access endpoint. The region must be one of the regions returned by the ListNetworkAccessEndpointAvailableRegions operation. This parameter does not take effect when NetworkAccessEndpointType is set to shared.
        self.vpc_region_id = vpc_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.network_access_endpoint_status is not None:
            result['NetworkAccessEndpointStatus'] = self.network_access_endpoint_status

        if self.network_access_endpoint_type is not None:
            result['NetworkAccessEndpointType'] = self.network_access_endpoint_type

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NetworkAccessEndpointStatus') is not None:
            self.network_access_endpoint_status = m.get('NetworkAccessEndpointStatus')

        if m.get('NetworkAccessEndpointType') is not None:
            self.network_access_endpoint_type = m.get('NetworkAccessEndpointType')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        return self

