# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class GetBotSessionDataResponseBody(DaraModel):
    def __init__(
        self,
        cost_time: str = None,
        datas: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.cost_time = cost_time
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time

        if self.datas is not None:
            result['Datas'] = self.datas

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')

        if m.get('Datas') is not None:
            self.datas = m.get('Datas')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

