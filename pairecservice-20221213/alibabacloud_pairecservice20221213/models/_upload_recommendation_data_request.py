# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class UploadRecommendationDataRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        content: List[main_models.UploadRecommendationDataRequestContent] = None,
        data_type: str = None,
    ):
        self.region_id = region_id
        self.content = content
        self.data_type = data_type

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.data_type is not None:
            result['DataType'] = self.data_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.UploadRecommendationDataRequestContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        return self

class UploadRecommendationDataRequestContent(DaraModel):
    def __init__(
        self,
        fields: str = None,
        operation_type: str = None,
    ):
        self.fields = fields
        self.operation_type = operation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fields is not None:
            result['Fields'] = self.fields

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        return self

