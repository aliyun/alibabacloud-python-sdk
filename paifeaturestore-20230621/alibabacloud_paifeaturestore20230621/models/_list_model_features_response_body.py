# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListModelFeaturesResponseBody(DaraModel):
    def __init__(
        self,
        model_features: List[main_models.ListModelFeaturesResponseBodyModelFeatures] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.model_features = model_features
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.model_features:
            for v1 in self.model_features:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModelFeatures'] = []
        if self.model_features is not None:
            for k1 in self.model_features:
                result['ModelFeatures'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_features = []
        if m.get('ModelFeatures') is not None:
            for k1 in m.get('ModelFeatures'):
                temp_model = main_models.ListModelFeaturesResponseBodyModelFeatures()
                self.model_features.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListModelFeaturesResponseBodyModelFeatures(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        label_table_name: str = None,
        model_feature_id: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.label_table_name = label_table_name
        self.model_feature_id = model_feature_id
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.label_table_name is not None:
            result['LabelTableName'] = self.label_table_name

        if self.model_feature_id is not None:
            result['ModelFeatureId'] = self.model_feature_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('LabelTableName') is not None:
            self.label_table_name = m.get('LabelTableName')

        if m.get('ModelFeatureId') is not None:
            self.model_feature_id = m.get('ModelFeatureId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

