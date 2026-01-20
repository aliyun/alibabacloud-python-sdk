# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFeatureEntityResponseBody(DaraModel):
    def __init__(
        self,
        feature_entity_id: str = None,
        request_id: str = None,
    ):
        self.feature_entity_id = feature_entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

