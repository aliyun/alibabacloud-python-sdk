# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class CreateCollectorResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.CreateCollectorResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.CreateCollectorResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CreateCollectorResponseBodyResult(DaraModel):
    def __init__(
        self,
        res_id: str = None,
    ):
        self.res_id = res_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.res_id is not None:
            result['resId'] = self.res_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resId') is not None:
            self.res_id = m.get('resId')

        return self

