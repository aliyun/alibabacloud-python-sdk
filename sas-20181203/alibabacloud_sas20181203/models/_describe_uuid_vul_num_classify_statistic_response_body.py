# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeUuidVulNumClassifyStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: Dict[str, main_models.DataValue] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = {}
        if self.data is not None:
            for k1, v1 in self.data.items():
                result['Data'][k1] = v1.to_map() if v1 else None

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = {}
        if m.get('Data') is not None:
            for k1, v1 in m.get('Data').items():
                temp_model = main_models.DataValue()
                self.data[k1] = temp_model.from_map(v1)

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

