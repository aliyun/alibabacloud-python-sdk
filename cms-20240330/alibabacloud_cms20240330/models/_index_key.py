# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IndexKey(DaraModel):
    def __init__(
        self,
        chn: bool = None,
        embedding: str = None,
        json_keys: Dict[str, main_models.IndexJsonKey] = None,
        type: str = None,
    ):
        self.chn = chn
        self.embedding = embedding
        self.json_keys = json_keys
        self.type = type

    def validate(self):
        if self.json_keys:
            for v1 in self.json_keys.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chn is not None:
            result['chn'] = self.chn

        if self.embedding is not None:
            result['embedding'] = self.embedding

        result['jsonKeys'] = {}
        if self.json_keys is not None:
            for k1, v1 in self.json_keys.items():
                result['jsonKeys'][k1] = v1.to_map() if v1 else None

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chn') is not None:
            self.chn = m.get('chn')

        if m.get('embedding') is not None:
            self.embedding = m.get('embedding')

        self.json_keys = {}
        if m.get('jsonKeys') is not None:
            for k1, v1 in m.get('jsonKeys').items():
                temp_model = main_models.IndexJsonKey()
                self.json_keys[k1] = temp_model.from_map(v1)

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

