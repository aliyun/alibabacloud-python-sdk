# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class GetDedicatedIpWarmUpInfoResponseBody(DaraModel):
    def __init__(
        self,
        info: List[main_models.GetDedicatedIpWarmUpInfoResponseBodyInfo] = None,
        request_id: str = None,
    ):
        self.info = info
        self.request_id = request_id

    def validate(self):
        if self.info:
            for v1 in self.info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Info'] = []
        if self.info is not None:
            for k1 in self.info:
                result['Info'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.info = []
        if m.get('Info') is not None:
            for k1 in m.get('Info'):
                temp_model = main_models.GetDedicatedIpWarmUpInfoResponseBodyInfo()
                self.info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDedicatedIpWarmUpInfoResponseBodyInfo(DaraModel):
    def __init__(
        self,
        esp: str = None,
        finished: bool = None,
    ):
        self.esp = esp
        self.finished = finished

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.esp is not None:
            result['Esp'] = self.esp

        if self.finished is not None:
            result['Finished'] = self.finished

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Esp') is not None:
            self.esp = m.get('Esp')

        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        return self

