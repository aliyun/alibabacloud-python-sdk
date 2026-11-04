# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryFaceUserGroupAndDeviceGroupRelationRequest(DaraModel):
    def __init__(
        self,
        control_id: str = None,
        isolation_id: str = None,
    ):
        # The control ID for the face synchronization relationship between user groups and device groups.
        # 
        # This parameter is required.
        self.control_id = control_id
        # The isolation ID.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_id is not None:
            result['ControlId'] = self.control_id

        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')

        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        return self

