# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDataLevelPermissionWhiteListRequest(DaraModel):
    def __init__(
        self,
        cube_id: str = None,
        operate_type: str = None,
        rule_type: str = None,
        target_ids: str = None,
        target_type: str = None,
    ):
        # The ID of the training dataset that you want to remove from the specified custom linguistic model.
        # 
        # This parameter is required.
        self.cube_id = cube_id
        # Operation Type: You can set this parameter to one of the following values.
        # 
        # *   ADD: Add a whitelist
        # *   DELETE: deletes a whitelist.
        self.operate_type = operate_type
        # The type of row-level permissions.
        # 
        # *   ROW_LEVEL: row-level permissions,
        # *   COLUMN_LEVEL: column-level permissions
        self.rule_type = rule_type
        self.target_ids = target_ids
        # Modify the type of the whitelist:
        # 
        # *   1: user
        # *   2: user group
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

