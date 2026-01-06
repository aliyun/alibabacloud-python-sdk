# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListModelVersionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        versions: List[main_models.ModelVersion] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of model versions.
        self.total_count = total_count
        # The model versions.
        self.versions = versions

    def validate(self):
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.ModelVersion()
                self.versions.append(temp_model.from_map(k1))

        return self

