# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCustomEndpointRequest(DaraModel):
    def __init__(
        self,
        custom_endpoint_id: str = None,
        dbinstance_name: str = None,
        name: str = None,
        node_auto_enter: bool = None,
        node_ids: str = None,
        node_role: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.custom_endpoint_id = custom_endpoint_id
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.name = name
        self.node_auto_enter = node_auto_enter
        # node ids
        self.node_ids = node_ids
        self.node_role = node_role
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_endpoint_id is not None:
            result['CustomEndpointId'] = self.custom_endpoint_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.name is not None:
            result['Name'] = self.name

        if self.node_auto_enter is not None:
            result['NodeAutoEnter'] = self.node_auto_enter

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.node_role is not None:
            result['NodeRole'] = self.node_role

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomEndpointId') is not None:
            self.custom_endpoint_id = m.get('CustomEndpointId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeAutoEnter') is not None:
            self.node_auto_enter = m.get('NodeAutoEnter')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('NodeRole') is not None:
            self.node_role = m.get('NodeRole')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

