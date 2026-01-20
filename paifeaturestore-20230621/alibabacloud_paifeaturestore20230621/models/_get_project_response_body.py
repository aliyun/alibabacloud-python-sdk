# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProjectResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        feature_entity_count: int = None,
        feature_view_count: int = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        model_count: int = None,
        name: str = None,
        offline_datasource_id: str = None,
        offline_datasource_name: str = None,
        offline_datasource_type: str = None,
        offline_lifecycle: int = None,
        online_datasource_id: str = None,
        online_datasource_name: str = None,
        online_datasource_type: str = None,
        owner: str = None,
        request_id: str = None,
    ):
        self.description = description
        self.feature_entity_count = feature_entity_count
        self.feature_view_count = feature_view_count
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.model_count = model_count
        self.name = name
        self.offline_datasource_id = offline_datasource_id
        self.offline_datasource_name = offline_datasource_name
        self.offline_datasource_type = offline_datasource_type
        self.offline_lifecycle = offline_lifecycle
        self.online_datasource_id = online_datasource_id
        self.online_datasource_name = online_datasource_name
        self.online_datasource_type = online_datasource_type
        self.owner = owner
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.feature_entity_count is not None:
            result['FeatureEntityCount'] = self.feature_entity_count

        if self.feature_view_count is not None:
            result['FeatureViewCount'] = self.feature_view_count

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.model_count is not None:
            result['ModelCount'] = self.model_count

        if self.name is not None:
            result['Name'] = self.name

        if self.offline_datasource_id is not None:
            result['OfflineDatasourceId'] = self.offline_datasource_id

        if self.offline_datasource_name is not None:
            result['OfflineDatasourceName'] = self.offline_datasource_name

        if self.offline_datasource_type is not None:
            result['OfflineDatasourceType'] = self.offline_datasource_type

        if self.offline_lifecycle is not None:
            result['OfflineLifecycle'] = self.offline_lifecycle

        if self.online_datasource_id is not None:
            result['OnlineDatasourceId'] = self.online_datasource_id

        if self.online_datasource_name is not None:
            result['OnlineDatasourceName'] = self.online_datasource_name

        if self.online_datasource_type is not None:
            result['OnlineDatasourceType'] = self.online_datasource_type

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FeatureEntityCount') is not None:
            self.feature_entity_count = m.get('FeatureEntityCount')

        if m.get('FeatureViewCount') is not None:
            self.feature_view_count = m.get('FeatureViewCount')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('ModelCount') is not None:
            self.model_count = m.get('ModelCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OfflineDatasourceId') is not None:
            self.offline_datasource_id = m.get('OfflineDatasourceId')

        if m.get('OfflineDatasourceName') is not None:
            self.offline_datasource_name = m.get('OfflineDatasourceName')

        if m.get('OfflineDatasourceType') is not None:
            self.offline_datasource_type = m.get('OfflineDatasourceType')

        if m.get('OfflineLifecycle') is not None:
            self.offline_lifecycle = m.get('OfflineLifecycle')

        if m.get('OnlineDatasourceId') is not None:
            self.online_datasource_id = m.get('OnlineDatasourceId')

        if m.get('OnlineDatasourceName') is not None:
            self.online_datasource_name = m.get('OnlineDatasourceName')

        if m.get('OnlineDatasourceType') is not None:
            self.online_datasource_type = m.get('OnlineDatasourceType')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

