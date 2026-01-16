# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DiagnoseInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        diagnose_items: List[str] = None,
        indices: List[str] = None,
        type: str = None,
        lang: str = None,
    ):
        # The timestamp when the diagnostic report was generated.
        self.client_token = client_token
        self.diagnose_items = diagnose_items
        self.indices = indices
        self.type = type
        # The returned data.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.diagnose_items is not None:
            result['diagnoseItems'] = self.diagnose_items

        if self.indices is not None:
            result['indices'] = self.indices

        if self.type is not None:
            result['type'] = self.type

        if self.lang is not None:
            result['lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('diagnoseItems') is not None:
            self.diagnose_items = m.get('diagnoseItems')

        if m.get('indices') is not None:
            self.indices = m.get('indices')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        return self

