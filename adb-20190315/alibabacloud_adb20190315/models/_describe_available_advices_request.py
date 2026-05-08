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
        # The date when the suggestion is generated. Specify the date in the yyyyMMdd format. The date must be in UTC.
        # 
        # >  Suggestions are generated after analysis after midnight every day. You must specify a date that is at least one day earlier than the current date. For example, if the current date is 20240627, you must specify 20240626 or an earlier date.
        # 
        # This parameter is required.
        self.advice_date = advice_date
        # The type of the suggestion. Valid values:
        # 
        # *   **INDEX**: index optimization.
        # *   **TIERING**: hot and cold data optimization.
        self.advice_type = advice_type
        # The ID of the cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of Data Warehouse Edition (V3.0) clusters.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The keyword that is used to query information by table name.
        self.keyword = keyword
        # The display language of the suggestion. Default value: zh. Valid values:
        # 
        # *   **zh**: simplified Chinese
        # *   **en**: English
        # *   **ja**: Japanese
        # *   **zh-tw**: traditional Chinese
        # 
        # This parameter is required.
        self.lang = lang
        # The order by which to sort query results. Specify the parameter value in the JSON format. Example: `[{"Field":"SchemaName","Type":"Asc"}]`.
        # 
        # *   `Field` specifies the field by which to sort the query results. Valid values:
        # 
        #     *   `SchemaName`: the name of the database.
        #     *   `TableName`: the name of the table.
        #     *   `Benefit`: the expected benefits of the applied optimization suggestion.
        # 
        # *   `Type` specifies the sorting order. Valid values:
        # 
        #     *   `Asc`: ascending order.
        #     *   `Desc`: descending order.
        # 
        # >  If you do not specify this parameter, the query results are sorted in descending order based on the Benefit field.
        self.order = order
        # The number of the page to return. The value must be an integer that is greater than 0. Default value: 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 30. Valid values:
        # 
        # *   **30**
        # *   **50**
        # *   **100**
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region ID of the cluster.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the table in the **DatabaseName.TableName** format.
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

