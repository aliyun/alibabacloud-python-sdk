# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppliedAdvicesRequest(DaraModel):
    def __init__(
        self,
        advice_type: str = None,
        dbcluster_id: str = None,
        end_time: int = None,
        keyword: str = None,
        lang: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        schema_table_name: str = None,
        start_time: int = None,
    ):
        # The type of the advice. Valid values:
        # 
        # - **INDEX**: index optimization
        # 
        # - **TIERING**: hot/cold data optimization
        self.advice_type = advice_type
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end date of the query. The date is in the `yyyyMMdd` format.
        self.end_time = end_time
        # The keyword for the query. Fuzzy match by table name is supported.
        self.keyword = keyword
        # The language of the query results. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        # 
        # - **ja**: Japanese
        # 
        # - **zh-tw**: Traditional Chinese
        self.lang = lang
        # The order by which to sort the query results. The value is a JSON string. Example: `[{"Field":"SchemaName","Type":"Asc"}]`. Fields:
        # 
        # - `Field`: The field by which to sort the results. Valid values:
        # 
        #   - `SchemaName`: the database name
        # 
        #   - `TableName`: the table name
        # 
        #   - `JobStatus`: the status of the build job for the table
        # 
        #   - `SubmitTime`: the time when the advice was submitted
        # 
        #   - `Benefit`: the estimated benefit
        # 
        # - `Type`: The sort order. Valid values:
        # 
        #   - `Asc`: ascending
        # 
        #   - `Desc`: descending
        # 
        # > If you do not set this parameter, the query results are sorted by advice submission time in descending order.
        self.order = order
        # The page number. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
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
        # The name of the database and table. Format: **database.table**.
        self.schema_table_name = schema_table_name
        # The start date of the query. The date is in the `yyyyMMdd` format.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice_type is not None:
            result['AdviceType'] = self.advice_type

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceType') is not None:
            self.advice_type = m.get('AdviceType')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

