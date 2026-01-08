# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EnableSdlProtectedAssetRequest(DaraModel):
    def __init__(
        self,
        ip_list: List[str] = None,
        lang: str = None,
    ):
        self.ip_list = ip_list
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

