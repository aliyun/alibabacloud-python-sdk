# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPermissionResourceForFrontRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        enterprise_id: str = None,
        operator_id: str = None,
        operator_type: str = None,
        query_type: str = None,
        resource_prefix: str = None,
    ):
        self.action = action
        self.enterprise_id = enterprise_id
        self.operator_id = operator_id
        self.operator_type = operator_type
        self.query_type = query_type
        self.resource_prefix = resource_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.operator_id is not None:
            result['operatorId'] = self.operator_id

        if self.operator_type is not None:
            result['operatorType'] = self.operator_type

        if self.query_type is not None:
            result['queryType'] = self.query_type

        if self.resource_prefix is not None:
            result['resourcePrefix'] = self.resource_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')

        if m.get('operatorType') is not None:
            self.operator_type = m.get('operatorType')

        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')

        if m.get('resourcePrefix') is not None:
            self.resource_prefix = m.get('resourcePrefix')

        return self

