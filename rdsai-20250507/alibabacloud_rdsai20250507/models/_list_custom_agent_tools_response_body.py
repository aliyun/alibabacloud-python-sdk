# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListCustomAgentToolsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListCustomAgentToolsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListCustomAgentToolsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCustomAgentToolsResponseBodyData(DaraModel):
    def __init__(
        self,
        en: str = None,
        ja: str = None,
        name: str = None,
        tc: str = None,
        type: str = None,
        zh: str = None,
    ):
        self.en = en
        self.ja = ja
        self.name = name
        self.tc = tc
        self.type = type
        self.zh = zh

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.en is not None:
            result['En'] = self.en

        if self.ja is not None:
            result['Ja'] = self.ja

        if self.name is not None:
            result['Name'] = self.name

        if self.tc is not None:
            result['Tc'] = self.tc

        if self.type is not None:
            result['Type'] = self.type

        if self.zh is not None:
            result['Zh'] = self.zh

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('En') is not None:
            self.en = m.get('En')

        if m.get('Ja') is not None:
            self.ja = m.get('Ja')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Tc') is not None:
            self.tc = m.get('Tc')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Zh') is not None:
            self.zh = m.get('Zh')

        return self

