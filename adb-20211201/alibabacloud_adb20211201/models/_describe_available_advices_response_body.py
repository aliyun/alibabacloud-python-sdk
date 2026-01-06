# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableAdvicesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeAvailableAdvicesResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        schema_table_names: List[str] = None,
        total_count: int = None,
    ):
        # The queried suggestions.
        self.items = items
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The name of the table in the DatabaseName.TableName format.
        self.schema_table_names = schema_table_names
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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema_table_names is not None:
            result['SchemaTableNames'] = self.schema_table_names

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAvailableAdvicesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SchemaTableNames') is not None:
            self.schema_table_names = m.get('SchemaTableNames')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAvailableAdvicesResponseBodyItems(DaraModel):
    def __init__(
        self,
        advice_date: str = None,
        advice_id: str = None,
        advice_type: str = None,
        benefit: str = None,
        index_fields: str = None,
        page_number: int = None,
        page_size: int = None,
        reason: str = None,
        sql: str = None,
        schema_name: str = None,
        table_name: str = None,
        total_count: int = None,
    ):
        # The date when the suggestion is generated. The date is in the yyyyMMdd format.
        self.advice_date = advice_date
        # The suggestion ID.
        self.advice_id = advice_id
        # The type of the suggestion. Valid values:
        # 
        # *   **INDEX**: index optimization.
        # *   **TIERING**: hot and cold data optimization.
        self.advice_type = advice_type
        # The benefit of the suggestion.
        self.benefit = benefit
        self.index_fields = index_fields
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The reason why the suggestion was generated.
        self.reason = reason
        # The SQL statement that is used to apply the suggestion.
        self.sql = sql
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice_date is not None:
            result['AdviceDate'] = self.advice_date

        if self.advice_id is not None:
            result['AdviceId'] = self.advice_id

        if self.advice_type is not None:
            result['AdviceType'] = self.advice_type

        if self.benefit is not None:
            result['Benefit'] = self.benefit

        if self.index_fields is not None:
            result['IndexFields'] = self.index_fields

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.sql is not None:
            result['SQL'] = self.sql

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceDate') is not None:
            self.advice_date = m.get('AdviceDate')

        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')

        if m.get('AdviceType') is not None:
            self.advice_type = m.get('AdviceType')

        if m.get('Benefit') is not None:
            self.benefit = m.get('Benefit')

        if m.get('IndexFields') is not None:
            self.index_fields = m.get('IndexFields')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('SQL') is not None:
            self.sql = m.get('SQL')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

