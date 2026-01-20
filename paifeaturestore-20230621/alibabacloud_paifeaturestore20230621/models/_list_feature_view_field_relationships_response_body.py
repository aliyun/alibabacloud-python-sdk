# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListFeatureViewFieldRelationshipsResponseBody(DaraModel):
    def __init__(
        self,
        relationships: List[main_models.ListFeatureViewFieldRelationshipsResponseBodyRelationships] = None,
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
                temp_model = main_models.ListFeatureViewFieldRelationshipsResponseBodyRelationships()
                self.relationships.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFeatureViewFieldRelationshipsResponseBodyRelationships(DaraModel):
    def __init__(
        self,
        feature_name: str = None,
        models: List[main_models.ListFeatureViewFieldRelationshipsResponseBodyRelationshipsModels] = None,
        offline_table_name: str = None,
        online_table_name: str = None,
    ):
        self.feature_name = feature_name
        self.models = models
        self.offline_table_name = offline_table_name
        self.online_table_name = online_table_name

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
        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        result['Models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['Models'].append(k1.to_map() if k1 else None)

        if self.offline_table_name is not None:
            result['OfflineTableName'] = self.offline_table_name

        if self.online_table_name is not None:
            result['OnlineTableName'] = self.online_table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        self.models = []
        if m.get('Models') is not None:
            for k1 in m.get('Models'):
                temp_model = main_models.ListFeatureViewFieldRelationshipsResponseBodyRelationshipsModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('OfflineTableName') is not None:
            self.offline_table_name = m.get('OfflineTableName')

        if m.get('OnlineTableName') is not None:
            self.online_table_name = m.get('OnlineTableName')

        return self

class ListFeatureViewFieldRelationshipsResponseBodyRelationshipsModels(DaraModel):
    def __init__(
        self,
        feature_alias_name: str = None,
        model_id: str = None,
        model_name: str = None,
    ):
        self.feature_alias_name = feature_alias_name
        self.model_id = model_id
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_alias_name is not None:
            result['FeatureAliasName'] = self.feature_alias_name

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureAliasName') is not None:
            self.feature_alias_name = m.get('FeatureAliasName')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        return self

