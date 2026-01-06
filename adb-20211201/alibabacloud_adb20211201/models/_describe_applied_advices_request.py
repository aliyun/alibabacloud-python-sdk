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
        # The type of the suggestion. Valid values:
        # 
        # *   **INDEX**: index optimization.
        # *   **TIERING**: hot and cold data optimization.
        self.advice_type = advice_type
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end date of the time range to query. Specify the date in the yyyyMMdd format.
        self.end_time = end_time
        # The keyword that is used to query information by table name.
        self.keyword = keyword
        # The display language of the suggestion. Valid values:
        # 
        # *   **zh** (default): simplified Chinese.
        # *   **en**: English.
        # *   **ja**: Japanese.
        # *   **zh-tw**: traditional Chinese.
        self.lang = lang
        # The order by which to sort query results. Specify the parameter value in the JSON format. Example: `[{"Field":"SchemaName","Type":"Asc"}]`.
        # 
        # *   `Field` specifies the field by which to sort the query results. Valid values:
        # 
        #     *   `SchemaName`: the name of the database.
        #     *   `TableName`: the name of the table.
        #     *   `JobStatus`: the status of the BUILD job that is triggered on the table.
        #     *   `SubmitTime`: the time when the suggestion was submitted.
        #     *   `Benefit`: the expected benefits of the applied optimization suggestion.
        # 
        # *   `Type` specifies the sorting order. Valid values:
        # 
        #     *   `Asc`: ascending order.
        #     *   `Desc`: descending order.
        # 
        # >  If you do not specify this parameter, optimization suggestions are sorted in descending order based on the submission time.
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30**(Default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the table in the **DatabaseName.TableName** format.
        self.schema_table_name = schema_table_name
        # The start date of the time range to query. Specify the date in the yyyyMMdd format.
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

