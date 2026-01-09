# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class IndexKey(DaraModel):
    def __init__(
        self,
        alias: str = None,
        case_sensitive: bool = None,
        chn: bool = None,
        doc_value: bool = None,
        index_all: bool = None,
        json_keys: Dict[str, main_models.IndexJsonKey] = None,
        max_depth: int = None,
        token: List[str] = None,
        type: str = None,
    ):
        self.alias = alias
        self.case_sensitive = case_sensitive
        self.chn = chn
        self.doc_value = doc_value
        self.index_all = index_all
        self.json_keys = json_keys
        self.max_depth = max_depth
        self.token = token
        # This parameter is required.
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
        if self.alias is not None:
            result['alias'] = self.alias

        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive

        if self.chn is not None:
            result['chn'] = self.chn

        if self.doc_value is not None:
            result['doc_value'] = self.doc_value

        if self.index_all is not None:
            result['index_all'] = self.index_all

        result['json_keys'] = {}
        if self.json_keys is not None:
            for k1, v1 in self.json_keys.items():
                result['json_keys'][k1] = v1.to_map() if v1 else None

        if self.max_depth is not None:
            result['max_depth'] = self.max_depth

        if self.token is not None:
            result['token'] = self.token

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')

        if m.get('chn') is not None:
            self.chn = m.get('chn')

        if m.get('doc_value') is not None:
            self.doc_value = m.get('doc_value')

        if m.get('index_all') is not None:
            self.index_all = m.get('index_all')

        self.json_keys = {}
        if m.get('json_keys') is not None:
            for k1, v1 in m.get('json_keys').items():
                temp_model = main_models.IndexJsonKey()
                self.json_keys[k1] = temp_model.from_map(v1)

        if m.get('max_depth') is not None:
            self.max_depth = m.get('max_depth')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

