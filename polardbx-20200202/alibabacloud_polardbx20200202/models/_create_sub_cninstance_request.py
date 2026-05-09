# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSubCNInstanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        is_auto_create: bool = None,
        read_type: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.is_auto_create = is_auto_create
        self.read_type = read_type
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.is_auto_create is not None:
            result['IsAutoCreate'] = self.is_auto_create

        if self.read_type is not None:
            result['ReadType'] = self.read_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('IsAutoCreate') is not None:
            self.is_auto_create = m.get('IsAutoCreate')

        if m.get('ReadType') is not None:
            self.read_type = m.get('ReadType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

