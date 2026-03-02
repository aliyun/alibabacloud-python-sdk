# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PermissionCheckCmd(DaraModel):
    def __init__(
        self,
        action: str = None,
        operator_id: str = None,
        operator_type: str = None,
        resource: str = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.operator_id = operator_id
        # This parameter is required.
        self.operator_type = operator_type
        # This parameter is required.
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.operator_id is not None:
            result['operatorId'] = self.operator_id

        if self.operator_type is not None:
            result['operatorType'] = self.operator_type

        if self.resource is not None:
            result['resource'] = self.resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')

        if m.get('operatorType') is not None:
            self.operator_type = m.get('operatorType')

        if m.get('resource') is not None:
            self.resource = m.get('resource')

        return self

