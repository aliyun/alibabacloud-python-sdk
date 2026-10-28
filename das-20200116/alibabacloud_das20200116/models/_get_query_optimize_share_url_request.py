# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQueryOptimizeShareUrlRequest(DaraModel):
    def __init__(
        self,
        asc: bool = None,
        db_names: str = None,
        engine: str = None,
        instance_ids: str = None,
        keywords: str = None,
        logical_operator: str = None,
        only_optimized_sql: bool = None,
        order_by: str = None,
        page_no: int = None,
        page_size: int = None,
        region: str = None,
        rules: str = None,
        sql_ids: str = None,
        tag_names: str = None,
        time: int = None,
        user: str = None,
    ):
        # Specifies whether to sort the results in ascending order. Default value: **true**. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.asc = asc
        # The names of the databases to be queried.
        self.db_names = db_names
        # The database engine. Valid values:
        # 
        # - **MySQL**: RDS MySQL
        # - **PolarDBMySQL**: PolarDB for MySQL
        # - **PostgreSQL**: RDS PostgreSQL
        # 
        # This parameter is required.
        self.engine = engine
        # The instance IDs. Separate multiple instance IDs with commas.
        self.instance_ids = instance_ids
        # The keywords in the SQL text. Separate multiple keywords with spaces.
        self.keywords = keywords
        # The logical relationship between multiple keywords in the SQL text. Valid values:
        # 
        # - **or**: The OR logical relationship.
        # - **and**: The AND logical relationship.
        self.logical_operator = logical_operator
        # Specifies whether to query only the SQL statements that need to be optimized. Default value: **false**. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.only_optimized_sql = only_optimized_sql
        # The field by which to sort the results. Default value: **count**. Valid values:
        # 
        # - **count**: The number of executions.
        # - **maxQueryTime**: The maximum execution time.
        # - **avgQueryTime**: The average execution time.
        # - **maxLockTime**: The maximum lock wait time.
        # - **avgLockTime**: The average lock wait time.
        # - **maxRowsExamined**: The maximum number of scanned rows.
        # - **avgRowsExamined**: The average number of scanned rows.
        # - **maxRowsSent**: The maximum number of returned rows.
        # - **avgRowsSent**: The average number of returned rows.
        self.order_by = order_by
        # The page number of the paging query. Pages start from 1. Default value: 1.
        self.page_no = page_no
        # The maximum number of records per page in a paging query. Default value: 10.
        self.page_size = page_size
        # The region where the instance resides. Valid values:
        # 
        # - **cn-china**: The Chinese mainland.
        # - **cn-hongkong**: Hong Kong (China).
        # - **ap-southeast-1**: Singapore.
        # 
        # This parameter is valid only when the **InstanceIds** request parameter is empty. If the **InstanceIds** request parameter is empty, data is retrieved based on the region specified by the **Region** parameter, and the default region is **cn-china**. If the **InstanceIds** request parameter is not empty, data is retrieved based on the region of the first instance specified in **InstanceIds**, regardless of the value of the **Region** parameter.
        # 
        # > For instances created in regions in the Chinese mainland, set this parameter to **cn-china**.
        self.region = region
        # The rules to be filtered. Separate multiple rules with commas. For more information, see [Query Governance](https://help.aliyun.com/document_detail/290038.html).
        self.rules = rules
        # The SQL template IDs. You can call the [GetQueryOptimizeDataStats](https://help.aliyun.com/document_detail/405261.html) operation to query the SQL template IDs.
        self.sql_ids = sql_ids
        # The reserved parameter.
        self.tag_names = tag_names
        # The date when the data is queried. The value is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.time = time
        # The database account to be queried.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc is not None:
            result['Asc'] = self.asc

        if self.db_names is not None:
            result['DbNames'] = self.db_names

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.logical_operator is not None:
            result['LogicalOperator'] = self.logical_operator

        if self.only_optimized_sql is not None:
            result['OnlyOptimizedSql'] = self.only_optimized_sql

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region is not None:
            result['Region'] = self.region

        if self.rules is not None:
            result['Rules'] = self.rules

        if self.sql_ids is not None:
            result['SqlIds'] = self.sql_ids

        if self.tag_names is not None:
            result['TagNames'] = self.tag_names

        if self.time is not None:
            result['Time'] = self.time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')

        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('LogicalOperator') is not None:
            self.logical_operator = m.get('LogicalOperator')

        if m.get('OnlyOptimizedSql') is not None:
            self.only_optimized_sql = m.get('OnlyOptimizedSql')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        if m.get('SqlIds') is not None:
            self.sql_ids = m.get('SqlIds')

        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

