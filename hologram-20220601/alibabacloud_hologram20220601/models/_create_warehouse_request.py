# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWarehouseRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        config: str = None,
        cpu: str = None,
        warehouse_name: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The configuration information.
        self.config = config
        # The number of vCPUs.
        self.cpu = cpu
        # The name of the virtual warehouse.
        self.warehouse_name = warehouse_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.config is not None:
            result['config'] = self.config

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.warehouse_name is not None:
            result['warehouseName'] = self.warehouse_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('warehouseName') is not None:
            self.warehouse_name = m.get('warehouseName')

        return self

