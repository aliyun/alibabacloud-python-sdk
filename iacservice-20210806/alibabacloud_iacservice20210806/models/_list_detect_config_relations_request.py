# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDetectConfigRelationsRequest(DaraModel):
    def __init__(
        self,
        detect_config_id: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.detect_config_id = detect_config_id
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detect_config_id is not None:
            result['detectConfigId'] = self.detect_config_id

        if self.target_id is not None:
            result['targetId'] = self.target_id

        if self.target_type is not None:
            result['targetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detectConfigId') is not None:
            self.detect_config_id = m.get('detectConfigId')

        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        return self

