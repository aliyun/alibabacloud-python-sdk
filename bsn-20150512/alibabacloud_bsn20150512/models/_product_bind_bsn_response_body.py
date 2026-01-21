# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bsn20150512 import models as main_models
from darabonba.model import DaraModel

class ProductBindBsnResponseBody(DaraModel):
    def __init__(
        self,
        datas: main_models.ProductBindBsnResponseBodyDatas = None,
        request_id: str = None,
    ):
        self.datas = datas
        self.request_id = request_id

    def validate(self):
        if self.datas:
            self.datas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datas is not None:
            result['datas'] = self.datas.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datas') is not None:
            temp_model = main_models.ProductBindBsnResponseBodyDatas()
            self.datas = temp_model.from_map(m.get('datas'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ProductBindBsnResponseBodyDatas(DaraModel):
    def __init__(
        self,
        bsn_do: List[str] = None,
    ):
        self.bsn_do = bsn_do

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bsn_do is not None:
            result['bsnDO'] = self.bsn_do

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bsnDO') is not None:
            self.bsn_do = m.get('bsnDO')

        return self

