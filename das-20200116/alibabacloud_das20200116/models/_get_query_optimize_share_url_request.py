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
        # Specifies whether to sort the returned entries in ascending order. Default value: **true**. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.asc = asc
        # The name of the database to be queried.
        self.db_names = db_names
        # The database engine. Valid values:
        # 
        # *   **MySQL**: ApsaraDB RDS for MySQL
        # *   **PolarDBMySQL**: PolarDB for MySQL
        # *   **PostgreSQL**: ApsaraDB RDS for PostgreSQL
        # 
        # This parameter is required.
        self.engine = engine
        # The instance IDs. Separate multiple IDs with commas (,).
        self.instance_ids = instance_ids
        # The keywords of the SQL template. Separate multiple keywords with spaces.
        self.keywords = keywords
        # The logical relationship between multiple keywords. Valid values:
        # 
        # *   **or**
        # *   **and**
        self.logical_operator = logical_operator
        # Specifies whether to query only SQL templates that need to be optimized. Default value: **false**. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.only_optimized_sql = only_optimized_sql
        # The field by which to sort the returned entries. Default value: **count**. Valid values:
        # 
        # *   **count**: the number of executions.
        # *   **maxQueryTime**: the longest execution duration.
        # *   **avgQueryTime**: the average execution duration.
        # *   **maxLockTime**: the longest lock wait duration.
        # *   **avgLockTime**: the average lock wait duration.
        # *   **maxRowsExamined**: the largest number of scanned rows.
        # *   **avgRowsExamined**: the average number of scanned rows.
        # *   **maxRowsSent**: the largest number of returned rows.
        # *   **avgRowsSent**: the average number of returned rows.
        self.order_by = order_by
        # The page number. Pages start from page 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region in which the instance resides. Valid values:
        # 
        # *   **cn-china**: Chinese mainland
        # *   **cn-hongkong**: China (Hong Kong)
        # *   **ap-southeast-1**: Singapore
        # 
        # This parameter takes effect only if **InstanceIds** is left empty. If you leave **InstanceIds** empty, the system obtains data from the region set by **Region**. By default, Region is set to **cn-china**. If you specify **InstanceIds**, **Region** does not take effect and the system obtains data from the region in which the first specified instance resides.****
        # 
        # >  If your instances reside in the regions in the Chinese mainland, set this parameter to **cn-china**.
        self.region = region
        # The tags that are used to filter SQL templates. Separate multiple tags with commas (,). For more information, see [Query governance](https://help.aliyun.com/document_detail/290038.html).
        self.rules = rules
        # The SQL template IDs. You can call the [GetQueryOptimizeExecErrorStats](https://help.aliyun.com/document_detail/405261.html) operation to obtain the SQL template IDs.
        self.sql_ids = sql_ids
        # A reserved parameter.
        self.tag_names = tag_names
        # The date to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.time = time
        # The account of the database to be queried.
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

