# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHbaseHaSlbRequest(DaraModel):
    def __init__(
        self,
        bds_id: str = None,
        ha_id: str = None,
        ha_types: str = None,
    ):
        # The ID of the BDS cluster.
        # 
        # This parameter is required.
        self.bds_id = bds_id
        # The high availability ID in BDS high availability management.
        # 
        # This parameter is required.
        self.ha_id = ha_id
        # The high availability type. Valid values:
        # 1. thrift
        # 2. phoenix.
        # 
        # This parameter is required.
        self.ha_types = ha_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id

        if self.ha_id is not None:
            result['HaId'] = self.ha_id

        if self.ha_types is not None:
            result['HaTypes'] = self.ha_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')

        if m.get('HaId') is not None:
            self.ha_id = m.get('HaId')

        if m.get('HaTypes') is not None:
            self.ha_types = m.get('HaTypes')

        return self

