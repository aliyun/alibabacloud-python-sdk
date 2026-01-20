# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListFeatureViewsResponseBody(DaraModel):
    def __init__(
        self,
        feature_views: List[main_models.ListFeatureViewsResponseBodyFeatureViews] = None,
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
                temp_model = main_models.ListFeatureViewsResponseBodyFeatureViews()
                self.feature_views.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFeatureViewsResponseBodyFeatureViews(DaraModel):
    def __init__(
        self,
        feature_entity_name: str = None,
        feature_view_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
        register_datasource_id: str = None,
        register_datasource_name: str = None,
        register_table: str = None,
        ttl: int = None,
        type: str = None,
        write_to_feature_db: bool = None,
    ):
        self.feature_entity_name = feature_entity_name
        self.feature_view_id = feature_view_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name
        self.register_datasource_id = register_datasource_id
        self.register_datasource_name = register_datasource_name
        self.register_table = register_table
        self.ttl = ttl
        self.type = type
        self.write_to_feature_db = write_to_feature_db

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_entity_name is not None:
            result['FeatureEntityName'] = self.feature_entity_name

        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.register_datasource_id is not None:
            result['RegisterDatasourceId'] = self.register_datasource_id

        if self.register_datasource_name is not None:
            result['RegisterDatasourceName'] = self.register_datasource_name

        if self.register_table is not None:
            result['RegisterTable'] = self.register_table

        if self.ttl is not None:
            result['TTL'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.write_to_feature_db is not None:
            result['WriteToFeatureDB'] = self.write_to_feature_db

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureEntityName') is not None:
            self.feature_entity_name = m.get('FeatureEntityName')

        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegisterDatasourceId') is not None:
            self.register_datasource_id = m.get('RegisterDatasourceId')

        if m.get('RegisterDatasourceName') is not None:
            self.register_datasource_name = m.get('RegisterDatasourceName')

        if m.get('RegisterTable') is not None:
            self.register_table = m.get('RegisterTable')

        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WriteToFeatureDB') is not None:
            self.write_to_feature_db = m.get('WriteToFeatureDB')

        return self

