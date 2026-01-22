# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceMaintainTimeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_name: str = None,
        maintain_time: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.maintain_time = maintain_time
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

