# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListProjectFeatureViewsResponseBody(DaraModel):
    def __init__(
        self,
        feature_views: List[main_models.ListProjectFeatureViewsResponseBodyFeatureViews] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.feature_views = feature_views
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.feature_views:
            for v1 in self.feature_views:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FeatureViews'] = []
        if self.feature_views is not None:
            for k1 in self.feature_views:
                result['FeatureViews'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_views = []
        if m.get('FeatureViews') is not None:
            for k1 in m.get('FeatureViews'):
                temp_model = main_models.ListProjectFeatureViewsResponseBodyFeatureViews()
                self.feature_views.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProjectFeatureViewsResponseBodyFeatureViews(DaraModel):
    def __init__(
        self,
        feature_view_id: str = None,
        features: List[main_models.ListProjectFeatureViewsResponseBodyFeatureViewsFeatures] = None,
        join_id: str = None,
        name: str = None,
        parent_join_id: str = None,
        type: str = None,
    ):
        self.feature_view_id = feature_view_id
        self.features = features
        self.join_id = join_id
        self.name = name
        self.parent_join_id = parent_join_id
        self.type = type

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
        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id

        result['Features'] = []
        if self.features is not None:
            for k1 in self.features:
                result['Features'].append(k1.to_map() if k1 else None)

        if self.join_id is not None:
            result['JoinId'] = self.join_id

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_join_id is not None:
            result['ParentJoinId'] = self.parent_join_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')

        self.features = []
        if m.get('Features') is not None:
            for k1 in m.get('Features'):
                temp_model = main_models.ListProjectFeatureViewsResponseBodyFeatureViewsFeatures()
                self.features.append(temp_model.from_map(k1))

        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentJoinId') is not None:
            self.parent_join_id = m.get('ParentJoinId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListProjectFeatureViewsResponseBodyFeatureViewsFeatures(DaraModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        type: str = None,
    ):
        self.attributes = attributes
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

