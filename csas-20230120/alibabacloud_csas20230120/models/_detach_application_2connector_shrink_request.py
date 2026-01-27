# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachApplication2ConnectorShrinkRequest(DaraModel):
    def __init__(
        self,
        application_ids_shrink: str = None,
        connector_id: str = None,
    ):
        # This parameter is required.
        self.application_ids_shrink = application_ids_shrink
        # ConnectorID。
        # 
        # This parameter is required.
        self.connector_id = connector_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_ids_shrink is not None:
            result['ApplicationIds'] = self.application_ids_shrink

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids_shrink = m.get('ApplicationIds')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        return self

