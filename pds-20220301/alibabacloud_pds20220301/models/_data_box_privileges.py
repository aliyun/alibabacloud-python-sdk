# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataBoxPrivileges(DaraModel):
    def __init__(
        self,
        feature_attr_id: str = None,
        feature_id: str = None,
        quota: int = None,
    ):
        self.feature_attr_id = feature_attr_id
        self.feature_id = feature_id
        self.quota = quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_attr_id is not None:
            result['feature_attr_id'] = self.feature_attr_id

        if self.feature_id is not None:
            result['feature_id'] = self.feature_id

        if self.quota is not None:
            result['quota'] = self.quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('feature_attr_id') is not None:
            self.feature_attr_id = m.get('feature_attr_id')

        if m.get('feature_id') is not None:
            self.feature_id = m.get('feature_id')

        if m.get('quota') is not None:
            self.quota = m.get('quota')

        return self

