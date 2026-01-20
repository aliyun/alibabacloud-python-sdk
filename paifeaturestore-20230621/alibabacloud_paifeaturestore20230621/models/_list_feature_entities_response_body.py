# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListFeatureEntitiesResponseBody(DaraModel):
    def __init__(
        self,
        feature_entities: List[main_models.ListFeatureEntitiesResponseBodyFeatureEntities] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.feature_entities = feature_entities
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.feature_entities:
            for v1 in self.feature_entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FeatureEntities'] = []
        if self.feature_entities is not None:
            for k1 in self.feature_entities:
                result['FeatureEntities'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_entities = []
        if m.get('FeatureEntities') is not None:
            for k1 in m.get('FeatureEntities'):
                temp_model = main_models.ListFeatureEntitiesResponseBodyFeatureEntities()
                self.feature_entities.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFeatureEntitiesResponseBodyFeatureEntities(DaraModel):
    def __init__(
        self,
        feature_entity_id: str = None,
        gmt_create_time: str = None,
        join_id: str = None,
        name: str = None,
        owner: str = None,
        parent_feature_entity_id: str = None,
        parent_feature_entity_name: str = None,
        parent_join_id: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.feature_entity_id = feature_entity_id
        self.gmt_create_time = gmt_create_time
        self.join_id = join_id
        self.name = name
        self.owner = owner
        self.parent_feature_entity_id = parent_feature_entity_id
        self.parent_feature_entity_name = parent_feature_entity_name
        self.parent_join_id = parent_join_id
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_entity_id is not None:
            result['FeatureEntityId'] = self.feature_entity_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.join_id is not None:
            result['JoinId'] = self.join_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parent_feature_entity_id is not None:
            result['ParentFeatureEntityId'] = self.parent_feature_entity_id

        if self.parent_feature_entity_name is not None:
            result['ParentFeatureEntityName'] = self.parent_feature_entity_name

        if self.parent_join_id is not None:
            result['ParentJoinId'] = self.parent_join_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureEntityId') is not None:
            self.feature_entity_id = m.get('FeatureEntityId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('JoinId') is not None:
            self.join_id = m.get('JoinId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParentFeatureEntityId') is not None:
            self.parent_feature_entity_id = m.get('ParentFeatureEntityId')

        if m.get('ParentFeatureEntityName') is not None:
            self.parent_feature_entity_name = m.get('ParentFeatureEntityName')

        if m.get('ParentJoinId') is not None:
            self.parent_join_id = m.get('ParentJoinId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

