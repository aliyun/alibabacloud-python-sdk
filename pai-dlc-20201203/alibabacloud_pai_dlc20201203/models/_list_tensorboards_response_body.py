# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class ListTensorboardsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tensorboards: List[main_models.Tensorboard] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The TensorBoard instances.
        self.tensorboards = tensorboards
        # The total number of data sources that meet the conditions.
        self.total_count = total_count

    def validate(self):
        if self.tensorboards:
            for v1 in self.tensorboards:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tensorboards'] = []
        if self.tensorboards is not None:
            for k1 in self.tensorboards:
                result['Tensorboards'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tensorboards = []
        if m.get('Tensorboards') is not None:
            for k1 in m.get('Tensorboards'):
                temp_model = main_models.Tensorboard()
                self.tensorboards.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

