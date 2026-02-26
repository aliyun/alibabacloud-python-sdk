# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DetectImageCarsResponseBody(DaraModel):
    def __init__(
        self,
        cars: List[main_models.Car] = None,
        request_id: str = None,
    ):
        # The vehicles.
        # 
        # This parameter is required.
        self.cars = cars
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cars:
            for v1 in self.cars:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cars'] = []
        if self.cars is not None:
            for k1 in self.cars:
                result['Cars'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cars = []
        if m.get('Cars') is not None:
            for k1 in m.get('Cars'):
                temp_model = main_models.Car()
                self.cars.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

