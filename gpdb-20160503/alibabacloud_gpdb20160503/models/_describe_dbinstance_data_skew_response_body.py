# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceDataSkewResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDBInstanceDataSkewResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about data skew.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDBInstanceDataSkewResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDBInstanceDataSkewResponseBodyItems(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        distribute_key: str = None,
        owner: str = None,
        schema_name: str = None,
        sequence: int = None,
        table_name: str = None,
        table_size: str = None,
        table_skew: str = None,
        time_last_updated: str = None,
    ):
        # The name of the database.
        self.database_name = database_name
        # The distribution key of the table.
        self.distribute_key = distribute_key
        # The owner of the table.
        self.owner = owner
        # The name of the schema.
        self.schema_name = schema_name
        # The sequence number of the data skew case. All data skew cases are sorted by severity in descending order.
        self.sequence = sequence
        # The name of the table.
        self.table_name = table_name
        # The total number of rows in the table.
        self.table_size = table_size
        # The skew ratio of the table. Valid values: 0 to 100. Unit: %. A greater value indicates that the table is more severely skewed. A smaller value indicates less impact on query performance. A value of 0 indicates no data skew.
        self.table_skew = table_skew
        # The time when the table was last deleted, inserted, or updated.
        self.time_last_updated = time_last_updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.distribute_key is not None:
            result['DistributeKey'] = self.distribute_key

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_size is not None:
            result['TableSize'] = self.table_size

        if self.table_skew is not None:
            result['TableSkew'] = self.table_skew

        if self.time_last_updated is not None:
            result['TimeLastUpdated'] = self.time_last_updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DistributeKey') is not None:
            self.distribute_key = m.get('DistributeKey')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableSize') is not None:
            self.table_size = m.get('TableSize')

        if m.get('TableSkew') is not None:
            self.table_skew = m.get('TableSkew')

        if m.get('TimeLastUpdated') is not None:
            self.time_last_updated = m.get('TimeLastUpdated')

        return self

