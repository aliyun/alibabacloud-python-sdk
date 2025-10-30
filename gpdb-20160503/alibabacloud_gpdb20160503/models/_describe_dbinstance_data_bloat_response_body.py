# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceDataBloatResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDBInstanceDataBloatResponseBodyItems] = None,
        page_number: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried data bloat.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
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
                temp_model = main_models.DescribeDBInstanceDataBloatResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDBInstanceDataBloatResponseBodyItems(DaraModel):
    def __init__(
        self,
        bloat_ceoff: str = None,
        bloat_size: str = None,
        database_name: str = None,
        expect_table_size: str = None,
        real_table_size: str = None,
        schema_name: str = None,
        sequence: int = None,
        storage_type: str = None,
        suggested_action: str = None,
        table_name: str = None,
        time_last_updated: str = None,
        time_last_vacuumed: str = None,
    ):
        # The coefficient of data bloat. It is calculated by using the following formula:
        # 
        # Bloat coefficient = Number of dead rows/Number of active rows.
        self.bloat_ceoff = bloat_ceoff
        # The bloat size of the table. It indicates the amount of space that can be released.
        self.bloat_size = bloat_size
        # The name of the database.
        self.database_name = database_name
        # The expected size of the table.
        # 
        # It indicates the size of the table that has no data bloat.
        self.expect_table_size = expect_table_size
        # The actual size of the table.
        self.real_table_size = real_table_size
        # The name of the schema.
        self.schema_name = schema_name
        # The sequence number.
        self.sequence = sequence
        # The storage type of the table. Valid values:
        # 
        # *   **Heap Table**
        # *   **Append-Only Heap Table**
        # *   **Append-Only Columnar Table**
        self.storage_type = storage_type
        # This parameter is not returned.
        self.suggested_action = suggested_action
        # The name of the table.
        self.table_name = table_name
        # The time when the table was last deleted, inserted, or updated.
        self.time_last_updated = time_last_updated
        # The time when the table was last vacuumed. The time is displayed in UTC.
        self.time_last_vacuumed = time_last_vacuumed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bloat_ceoff is not None:
            result['BloatCeoff'] = self.bloat_ceoff

        if self.bloat_size is not None:
            result['BloatSize'] = self.bloat_size

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.expect_table_size is not None:
            result['ExpectTableSize'] = self.expect_table_size

        if self.real_table_size is not None:
            result['RealTableSize'] = self.real_table_size

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.suggested_action is not None:
            result['SuggestedAction'] = self.suggested_action

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.time_last_updated is not None:
            result['TimeLastUpdated'] = self.time_last_updated

        if self.time_last_vacuumed is not None:
            result['TimeLastVacuumed'] = self.time_last_vacuumed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BloatCeoff') is not None:
            self.bloat_ceoff = m.get('BloatCeoff')

        if m.get('BloatSize') is not None:
            self.bloat_size = m.get('BloatSize')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('ExpectTableSize') is not None:
            self.expect_table_size = m.get('ExpectTableSize')

        if m.get('RealTableSize') is not None:
            self.real_table_size = m.get('RealTableSize')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('SuggestedAction') is not None:
            self.suggested_action = m.get('SuggestedAction')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TimeLastUpdated') is not None:
            self.time_last_updated = m.get('TimeLastUpdated')

        if m.get('TimeLastVacuumed') is not None:
            self.time_last_vacuumed = m.get('TimeLastVacuumed')

        return self

