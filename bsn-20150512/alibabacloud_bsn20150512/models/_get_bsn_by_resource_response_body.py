# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bsn20150512 import models as main_models
from darabonba.model import DaraModel

class GetBsnByResourceResponseBody(DaraModel):
    def __init__(
        self,
        datas: main_models.GetBsnByResourceResponseBodyDatas = None,
    ):
        self.datas = datas

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datas') is not None:
            temp_model = main_models.GetBsnByResourceResponseBodyDatas()
            self.datas = temp_model.from_map(m.get('datas'))

        return self



class GetBsnByResourceResponseBodyDatas(DaraModel):
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

