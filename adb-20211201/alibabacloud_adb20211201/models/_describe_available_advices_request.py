# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAvailableAdvicesRequest(DaraModel):
    def __init__(
        self,
        advice_date: int = None,
        advice_type: str = None,
        dbcluster_id: str = None,
        keyword: str = None,
        lang: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        schema_table_name: str = None,
    ):
        # The date when the advice was generated, in the `yyyyMMdd` format.
        # 
        # > Advice is generated daily. To query for advice, specify a date at least one day before the current date. For example, if you query on June 27, 2024, set this parameter to `20240626` or an earlier date.
        self.advice_date = advice_date
        # The type of advice. Valid values:
        # 
        # - **INDEX**: index optimization.
        # 
        # - **TIERING**: hot and cold data tiering.
        self.advice_type = advice_type
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The keyword for a fuzzy search on table names.
        self.keyword = keyword
        # The display language for the advice. Valid values:
        # 
        # - **zh**: Simplified Chinese (default).
        # 
        # - **en**: English.
        # 
        # - **ja**: Japanese.
        # 
        # - **zh-tw**: Traditional Chinese.
        self.lang = lang
        # Specifies the sort order for the results. The value is a JSON string. Example: `[{"Field":"SchemaName","Type":"Asc"}]`. The JSON string contains the following key-value pairs:
        # 
        # - `Field`: the field to sort by. Valid values:
        # 
        #   - `SchemaName`: the database name.
        # 
        #   - `TableName`: the table name.
        # 
        #   - `Benefit`: the expected benefit.
        # 
        # - `Type`: the sort order. Valid values:
        # 
        #   - `Asc`: ascending order.
        # 
        #   - `Desc`: descending order.
        # 
        # > By default, results are sorted by expected benefit in descending order.
        self.order = order
        # The page number. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # - **30** (default)
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # A concatenation of the database name and the table name.
        self.schema_table_name = schema_table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice_date is not None:
            result['AdviceDate'] = self.advice_date

        if self.advice_type is not None:
            result['AdviceType'] = self.advice_type

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.schema_table_name is not None:
            result['SchemaTableName'] = self.schema_table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceDate') is not None:
            self.advice_date = m.get('AdviceDate')

        if m.get('AdviceType') is not None:
            self.advice_type = m.get('AdviceType')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SchemaTableName') is not None:
            self.schema_table_name = m.get('SchemaTableName')

        return self

