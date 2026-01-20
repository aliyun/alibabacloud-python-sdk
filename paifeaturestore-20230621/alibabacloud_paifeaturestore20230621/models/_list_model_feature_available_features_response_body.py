# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListModelFeatureAvailableFeaturesResponseBody(DaraModel):
    def __init__(
        self,
        avaliable_features: List[main_models.ListModelFeatureAvailableFeaturesResponseBodyAvaliableFeatures] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.avaliable_features = avaliable_features
        self.total_count = total_count
        self.request_id = request_id

    def validate(self):
        if self.avaliable_features:
            for v1 in self.avaliable_features:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvaliableFeatures'] = []
        if self.avaliable_features is not None:
            for k1 in self.avaliable_features:
                result['AvaliableFeatures'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.avaliable_features = []
        if m.get('AvaliableFeatures') is not None:
            for k1 in m.get('AvaliableFeatures'):
                temp_model = main_models.ListModelFeatureAvailableFeaturesResponseBodyAvaliableFeatures()
                self.avaliable_features.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListModelFeatureAvailableFeaturesResponseBodyAvaliableFeatures(DaraModel):
    def __init__(
        self,
        name: str = None,
        source_name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.name = name
        self.source_name = source_name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

