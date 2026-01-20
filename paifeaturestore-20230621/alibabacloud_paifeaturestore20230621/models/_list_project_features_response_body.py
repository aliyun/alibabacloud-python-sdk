# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListProjectFeaturesResponseBody(DaraModel):
    def __init__(
        self,
        features: List[main_models.ListProjectFeaturesResponseBodyFeatures] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        self.features = features
        self.total_count = total_count
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.features:
            for v1 in self.features:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Features'] = []
        if self.features is not None:
            for k1 in self.features:
                result['Features'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k1 in m.get('Features'):
                temp_model = main_models.ListProjectFeaturesResponseBodyFeatures()
                self.features.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListProjectFeaturesResponseBodyFeatures(DaraModel):
    def __init__(
        self,
        alias_names: str = None,
        feature_view_id: str = None,
        feature_view_name: str = None,
        gmt_create_time: str = None,
        model_feature_count: int = None,
        name: str = None,
        owner: str = None,
        type: str = None,
    ):
        self.alias_names = alias_names
        self.feature_view_id = feature_view_id
        self.feature_view_name = feature_view_name
        self.gmt_create_time = gmt_create_time
        self.model_feature_count = model_feature_count
        self.name = name
        self.owner = owner
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_names is not None:
            result['AliasNames'] = self.alias_names

        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id

        if self.feature_view_name is not None:
            result['FeatureViewName'] = self.feature_view_name

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.model_feature_count is not None:
            result['ModelFeatureCount'] = self.model_feature_count

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasNames') is not None:
            self.alias_names = m.get('AliasNames')

        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')

        if m.get('FeatureViewName') is not None:
            self.feature_view_name = m.get('FeatureViewName')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('ModelFeatureCount') is not None:
            self.model_feature_count = m.get('ModelFeatureCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

