# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExpressConnectRouterRouteEntriesRequest(DaraModel):
    def __init__(
        self,
        as_path: str = None,
        client_token: str = None,
        community: str = None,
        destination_cidr_block: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        max_results: int = None,
        next_token: str = None,
        nexthop_instance_id: str = None,
        query_region_id: str = None,
        version: str = None,
    ):
        # The AS path traversed by the route entry.
        self.as_path = as_path
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the parameter value from your client to ensure that the value is unique across different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # The community value carried by the BGP route entry.
        self.community = community
        # The destination CIDR block of the route entry to query.
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether it is a dry run for this request. Valid values:
        # 
        # - **true**: sends a check request and does not modify EPS resources.
        # 
        # - **false** (default): sends a normal request.
        self.dry_run = dry_run
        # The instance ID of the Express Connect Router (ECR).
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The maximum number of entries to return. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # - For the first query or when no subsequent query is required, leave this parameter empty.
        # - If a subsequent query is required, set the value to the NextToken value returned from the previous API call.
        self.next_token = next_token
        # The next hop instance ID.
        self.nexthop_instance_id = nexthop_instance_id
        # The region where the Express Connect Router (ECR) instance resides.
        self.query_region_id = query_region_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.as_path is not None:
            result['AsPath'] = self.as_path

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.community is not None:
            result['Community'] = self.community

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id

        if self.query_region_id is not None:
            result['QueryRegionId'] = self.query_region_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Community') is not None:
            self.community = m.get('Community')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')

        if m.get('QueryRegionId') is not None:
            self.query_region_id = m.get('QueryRegionId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

