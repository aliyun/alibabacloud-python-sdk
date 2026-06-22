# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class AddDatasetDataRequest(DaraModel):
    def __init__(
        self,
        data_array: List[Dict[str, Any]] = None,
        client_token: str = None,
    ):
        self.data_array = data_array
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_array is not None:
            result['dataArray'] = self.data_array

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataArray') is not None:
            self.data_array = m.get('dataArray')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

