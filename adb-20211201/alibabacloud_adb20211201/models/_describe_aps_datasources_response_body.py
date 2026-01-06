# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeApsDatasourcesResponseBody(DaraModel):
    def __init__(
        self,
        aps_datasources: List[main_models.DescribeApsDatasourcesResponseBodyApsDatasources] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The queried APS data sources.
        self.aps_datasources = aps_datasources
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.aps_datasources:
            for v1 in self.aps_datasources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApsDatasources'] = []
        if self.aps_datasources is not None:
            for k1 in self.aps_datasources:
                result['ApsDatasources'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aps_datasources = []
        if m.get('ApsDatasources') is not None:
            for k1 in m.get('ApsDatasources'):
                temp_model = main_models.DescribeApsDatasourcesResponseBodyApsDatasources()
                self.aps_datasources.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApsDatasourcesResponseBodyApsDatasources(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        datasource_description: str = None,
        datasource_id: int = None,
        datasource_name: str = None,
        datasource_type: str = None,
        has_job: bool = None,
    ):
        # The time when the data source was created.
        self.create_time = create_time
        # The description of the data source.
        self.datasource_description = datasource_description
        # The data source ID.
        self.datasource_id = datasource_id
        # The name of the data source.
        self.datasource_name = datasource_name
        # The type of the data source.
        self.datasource_type = datasource_type
        # Indicates whether a job is using the data source.
        self.has_job = has_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.datasource_description is not None:
            result['DatasourceDescription'] = self.datasource_description

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.datasource_type is not None:
            result['DatasourceType'] = self.datasource_type

        if self.has_job is not None:
            result['HasJob'] = self.has_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DatasourceDescription') is not None:
            self.datasource_description = m.get('DatasourceDescription')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('DatasourceType') is not None:
            self.datasource_type = m.get('DatasourceType')

        if m.get('HasJob') is not None:
            self.has_job = m.get('HasJob')

        return self

