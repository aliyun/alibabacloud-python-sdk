# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListModelsResponseBody(DaraModel):
    def __init__(
        self,
        models: List[main_models.Model] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The models.
        self.models = models
        # The request ID.
        self.request_id = request_id
        # The total number of models.
        self.total_count = total_count

    def validate(self):
        if self.models:
            for v1 in self.models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['Models'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.models = []
        if m.get('Models') is not None:
            for k1 in m.get('Models'):
                temp_model = main_models.Model()
                self.models.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

