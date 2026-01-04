# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class PublishVpcRouteEntriesRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_entries: List[main_models.PublishVpcRouteEntriesRequestRouteEntries] = None,
        target_instance_id: str = None,
        target_type: str = None,
    ):
        # Indicates whether to perform a dry run of this request. Values:
        # 
        # - **true**: Sends a check request without publishing the route. The checks include whether the AccessKey is valid, the authorization status of the RAM user, and if all required parameters are filled out. If the check fails, the corresponding error is returned. If the check passes, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): Sends a normal request. After passing the check, it returns a 2xx HTTP status code and directly queries the resource status.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the instance is located. You can obtain the region ID by calling the DescribeRegions interface.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # List of route entries to be published, supporting up to 50 routes at most.
        self.route_entries = route_entries
        # The ID of the target instance for route publication.
        # 
        # This parameter is required.
        self.target_instance_id = target_instance_id
        # The type of the target for route publication.
        # 
        # This parameter is required.
        self.target_type = target_type

    def validate(self):
        if self.route_entries:
            for v1 in self.route_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        result['RouteEntries'] = []
        if self.route_entries is not None:
            for k1 in self.route_entries:
                result['RouteEntries'].append(k1.to_map() if k1 else None)

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

        self.route_entries = []
        if m.get('RouteEntries') is not None:
            for k1 in m.get('RouteEntries'):
                temp_model = main_models.PublishVpcRouteEntriesRequestRouteEntries()
                self.route_entries.append(temp_model.from_map(k1))

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class PublishVpcRouteEntriesRequestRouteEntries(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        route_table_id: str = None,
    ):
        # The destination CIDR block for the route entry.
        # 
        # This parameter is required.
        self.destination_cidr_block = destination_cidr_block
        # The ID of the route table for the route entry.
        # 
        # This parameter is required.
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

