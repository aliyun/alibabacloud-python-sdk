# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListFeatureViewRelationshipsResponseBody(DaraModel):
    def __init__(
        self,
        relationships: List[main_models.ListFeatureViewRelationshipsResponseBodyRelationships] = None,
        request_id: str = None,
    ):
        self.relationships = relationships
        self.request_id = request_id

    def validate(self):
        if self.relationships:
            for v1 in self.relationships:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Relationships'] = []
        if self.relationships is not None:
            for k1 in self.relationships:
                result['Relationships'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.relationships = []
        if m.get('Relationships') is not None:
            for k1 in m.get('Relationships'):
                temp_model = main_models.ListFeatureViewRelationshipsResponseBodyRelationships()
                self.relationships.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFeatureViewRelationshipsResponseBodyRelationships(DaraModel):
    def __init__(
        self,
        feature_view_name: str = None,
        models: List[main_models.ListFeatureViewRelationshipsResponseBodyRelationshipsModels] = None,
        project_name: str = None,
    ):
        self.feature_view_name = feature_view_name
        self.models = models
        self.project_name = project_name

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
        if self.feature_view_name is not None:
            result['FeatureViewName'] = self.feature_view_name

        result['Models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['Models'].append(k1.to_map() if k1 else None)

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureViewName') is not None:
            self.feature_view_name = m.get('FeatureViewName')

        self.models = []
        if m.get('Models') is not None:
            for k1 in m.get('Models'):
                temp_model = main_models.ListFeatureViewRelationshipsResponseBodyRelationshipsModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

class ListFeatureViewRelationshipsResponseBodyRelationshipsModels(DaraModel):
    def __init__(
        self,
        model_id: str = None,
        model_name: str = None,
    ):
        self.model_id = model_id
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        return self

