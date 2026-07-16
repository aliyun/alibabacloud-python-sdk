# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDataAgentAccuracyTestRequest(DaraModel):
    def __init__(
        self,
        accuracy_test_ins_id: str = None,
        dms_unit: str = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The accuracy test instance ID.
        self.accuracy_test_ins_id = accuracy_test_ins_id
        # The current DMS unit.
        self.dms_unit = dms_unit
        # The region ID.
        self.region_id = region_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accuracy_test_ins_id is not None:
            result['AccuracyTestInsId'] = self.accuracy_test_ins_id

        if self.dms_unit is not None:
            result['DmsUnit'] = self.dms_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccuracyTestInsId') is not None:
            self.accuracy_test_ins_id = m.get('AccuracyTestInsId')

        if m.get('DmsUnit') is not None:
            self.dms_unit = m.get('DmsUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

