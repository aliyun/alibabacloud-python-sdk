# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetResourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetResourcesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['request_id'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetResourcesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        return self

class GetResourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        total: float = None,
        unit: str = None,
        usage: float = None,
    ):
        self.total = total
        self.unit = unit
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total is not None:
            result['total'] = self.total

        if self.unit is not None:
            result['unit'] = self.unit

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

