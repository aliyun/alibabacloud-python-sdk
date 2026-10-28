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
        # The generation date of the suggestion, in the yyyyMMdd format.
        # 
        # > Data is generated after daily analysis in the early morning. Therefore, you must specify a date of T-1 or earlier to query the data. For example, if today is 20240627, you must specify 20240626 or an earlier date.
        self.advice_date = advice_date
        # The type of the suggestion. Valid values:
        # - **INDEX**: Index optimization.
        # - **TIERING**: Hot and cold data optimization.
        self.advice_type = advice_type
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The query keyword. Fuzzy search by table name is supported.
        self.keyword = keyword
        # The display language of the suggestions. Valid values:
        # - **zh**: Simplified Chinese (default).
        # - **en**: English.
        # - **ja**: Japanese.
        # - **zh-tw**: Traditional Chinese.
        self.lang = lang
        # The field by which to sort the query results. The value is a JSON string. Example: `[{"Field":"SchemaName","Type":"Asc"}]`. Parameters:
        # - `Field`: the sort field. Valid values:
        #     - `SchemaName`: the database name.
        #     - `TableName`: the table name.
        #     - `Benefit`: the expected optimization benefit.
        # - `Type`: the sort order. Valid values:
        #     - `Asc`: ascending order.
        #     - `Desc`: descending order.
        # 
        # > If this parameter is not specified, the results are sorted in descending order of the expected optimization benefit by default.
        self.order = order
        # The page number. Valid values: greater than 0 and up to the maximum value of the Integer data type. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # - **30** (default)
        # - **50**
        # - **100**
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The concatenated string of the database name and table name.
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

