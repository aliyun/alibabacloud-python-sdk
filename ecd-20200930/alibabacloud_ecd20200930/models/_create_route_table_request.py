# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRouteTableRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        region_id: str = None,
        route_table_name: str = None,
        vpc_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.region_id = region_id
        self.route_table_name = route_table_name
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.route_table_name is not None:
            result['RouteTableName'] = self.route_table_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteTableName') is not None:
            self.route_table_name = m.get('RouteTableName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

