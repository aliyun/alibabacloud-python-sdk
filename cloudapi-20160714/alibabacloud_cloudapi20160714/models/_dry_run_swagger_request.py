# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DryRunSwaggerRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        data_format: str = None,
        global_condition: Dict[str, Any] = None,
        group_id: str = None,
        overwrite: bool = None,
        security_token: str = None,
    ):
        # The Swagger text content.
        # 
        # This parameter is required.
        self.data = data
        # The Swagger text format:
        # 
        # *   json
        # *   yaml
        # 
        # This parameter is required.
        self.data_format = data_format
        # The global condition.
        self.global_condition = global_condition
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # Specifies whether to overwrite the existing API.
        # 
        # APIs with the same HTTP request type and backend request path are considered the same.
        # 
        # This parameter is required.
        self.overwrite = overwrite
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.data_format is not None:
            result['DataFormat'] = self.data_format

        if self.global_condition is not None:
            result['GlobalCondition'] = self.global_condition

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')

        if m.get('GlobalCondition') is not None:
            self.global_condition = m.get('GlobalCondition')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

