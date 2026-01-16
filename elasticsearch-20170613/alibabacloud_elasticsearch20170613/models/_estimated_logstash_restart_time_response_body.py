# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class EstimatedLogstashRestartTimeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.EstimatedLogstashRestartTimeResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
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
            temp_model = main_models.EstimatedLogstashRestartTimeResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class EstimatedLogstashRestartTimeResponseBodyResult(DaraModel):
    def __init__(
        self,
        unit: str = None,
        value: int = None,
    ):
        # The unit.
        self.unit = unit
        # The estimated restart time.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.unit is not None:
            result['unit'] = self.unit

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

