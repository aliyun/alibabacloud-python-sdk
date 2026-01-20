# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class CreateModelFeatureRequest(DaraModel):
    def __init__(
        self,
        features: List[main_models.CreateModelFeatureRequestFeatures] = None,
        label_priority_level: int = None,
        label_table_id: str = None,
        name: str = None,
        project_id: str = None,
        sequence_feature_view_ids: List[str] = None,
    ):
        # This parameter is required.
        self.features = features
        self.label_priority_level = label_priority_level
        # This parameter is required.
        self.label_table_id = label_table_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id
        self.sequence_feature_view_ids = sequence_feature_view_ids

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

        if self.label_priority_level is not None:
            result['LabelPriorityLevel'] = self.label_priority_level

        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sequence_feature_view_ids is not None:
            result['SequenceFeatureViewIds'] = self.sequence_feature_view_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.features = []
        if m.get('Features') is not None:
            for k1 in m.get('Features'):
                temp_model = main_models.CreateModelFeatureRequestFeatures()
                self.features.append(temp_model.from_map(k1))

        if m.get('LabelPriorityLevel') is not None:
            self.label_priority_level = m.get('LabelPriorityLevel')

        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SequenceFeatureViewIds') is not None:
            self.sequence_feature_view_ids = m.get('SequenceFeatureViewIds')

        return self

class CreateModelFeatureRequestFeatures(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        feature_view_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.alias_name = alias_name
        # This parameter is required.
        self.feature_view_id = feature_view_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

