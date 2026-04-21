# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HiMarketHmacConfig(DaraModel):
    def __init__(
        self,
        credentials: List[main_models.HiMarketHmacConfigCredentials] = None,
    ):
        self.credentials = credentials

    def validate(self):
        if self.credentials:
            for v1 in self.credentials:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['credentials'] = []
        if self.credentials is not None:
            for k1 in self.credentials:
                result['credentials'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.credentials = []
        if m.get('credentials') is not None:
            for k1 in m.get('credentials'):
                temp_model = main_models.HiMarketHmacConfigCredentials()
                self.credentials.append(temp_model.from_map(k1))

        return self

class HiMarketHmacConfigCredentials(DaraModel):
    def __init__(
        self,
        ak: str = None,
        mode: str = None,
        sk: str = None,
    ):
        self.ak = ak
        self.mode = mode
        self.sk = sk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ak is not None:
            result['ak'] = self.ak

        if self.mode is not None:
            result['mode'] = self.mode

        if self.sk is not None:
            result['sk'] = self.sk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ak') is not None:
            self.ak = m.get('ak')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('sk') is not None:
            self.sk = m.get('sk')

        return self

