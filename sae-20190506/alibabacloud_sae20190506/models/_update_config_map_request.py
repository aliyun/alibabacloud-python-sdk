# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConfigMapRequest(DaraModel):
    def __init__(
        self,
        config_map_id: int = None,
        data: str = None,
        description: str = None,
    ):
        # The ID of the request.
        # 
        # This parameter is required.
        self.config_map_id = config_map_id
        # This parameter is required.
        self.data = data
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id

        if self.data is not None:
            result['Data'] = self.data

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

