# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataLevelPermissionWhiteListRequest(DaraModel):
    def __init__(
        self,
        cube_id: str = None,
        rule_type: str = None,
    ):
        # Dataset ID.
        # 
        # This parameter is required.
        self.cube_id = cube_id
        # Type of row and column permission that the whitelist belongs to:
        # 
        # - ROW_LEVEL: Row-level permission
        # - COLUMN_LEVEL: Column-level permission
        # 
        # This parameter is required.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

