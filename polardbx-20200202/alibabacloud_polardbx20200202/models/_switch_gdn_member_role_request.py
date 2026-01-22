# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchGdnMemberRoleRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
        switch_mode: str = None,
        task_timeout: int = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.switch_mode = switch_mode
        self.task_timeout = task_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        if self.task_timeout is not None:
            result['TaskTimeout'] = self.task_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        if m.get('TaskTimeout') is not None:
            self.task_timeout = m.get('TaskTimeout')

        return self

