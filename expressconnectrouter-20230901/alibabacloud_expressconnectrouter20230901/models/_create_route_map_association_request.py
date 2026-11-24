# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateRouteMapAssociationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        region_id_list: List[str] = None,
        route_map_id: str = None,
        version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the value from your client and ensure that the value is unique across different requests. The client token supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # Specifies whether it is a dry run only. Valid values:
        # 
        # - **true**: sends a dry run request without modifying EPS resources.
        # 
        # - **false** (default): sends a normal request.
        self.dry_run = dry_run
        # The Express Connect Router (ECR) instance ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The list of region IDs of the Express Connect Router (ECR) where the routing policy is distributed and takes effect.
        # 
        # > If this parameter is left empty, the routing policy is not distributed to any region.
        self.region_id_list = region_id_list
        # The ID of the route map in the Cloud Enterprise Network (CEN).
        # 
        # This parameter is required.
        self.route_map_id = route_map_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.region_id_list is not None:
            result['RegionIdList'] = self.region_id_list

        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('RegionIdList') is not None:
            self.region_id_list = m.get('RegionIdList')

        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

