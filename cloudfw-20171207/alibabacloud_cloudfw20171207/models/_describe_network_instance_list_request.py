# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNetworkInstanceListRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        connect_type: str = None,
        lang: str = None,
    ):
        self.cen_id = cen_id
        self.connect_type = connect_type
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

