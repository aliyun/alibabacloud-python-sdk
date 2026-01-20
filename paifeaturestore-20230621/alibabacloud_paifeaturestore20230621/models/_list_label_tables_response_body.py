# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListLabelTablesResponseBody(DaraModel):
    def __init__(
        self,
        label_tables: List[main_models.ListLabelTablesResponseBodyLabelTables] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.label_tables = label_tables
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.label_tables:
            for v1 in self.label_tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LabelTables'] = []
        if self.label_tables is not None:
            for k1 in self.label_tables:
                result['LabelTables'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_tables = []
        if m.get('LabelTables') is not None:
            for k1 in m.get('LabelTables'):
                temp_model = main_models.ListLabelTablesResponseBodyLabelTables()
                self.label_tables.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLabelTablesResponseBodyLabelTables(DaraModel):
    def __init__(
        self,
        datasource_id: str = None,
        datasource_name: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        label_table_id: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.datasource_id = datasource_id
        self.datasource_name = datasource_name
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.label_table_id = label_table_id
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
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id

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
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

