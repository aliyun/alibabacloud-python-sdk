# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlInsightStatisticRequest(DaraModel):
    def __init__(
        self,
        asc: bool = None,
        console_context: str = None,
        db_name: str = None,
        do_fill_trend: bool = None,
        end_time: int = None,
        filters: List[main_models.DescribeSqlInsightStatisticRequestFilters] = None,
        instance_id: str = None,
        job_id: str = None,
        keyword: str = None,
        node_id: str = None,
        order_by: str = None,
        page_no: int = None,
        page_size: int = None,
        role: str = None,
        sql_type: str = None,
        start_time: int = None,
        template_id: str = None,
        type: str = None,
    ):
        # The sort order. Default value: **false** (descending order). Valid values:
        # 
        # - **true**: ascending order.
        # - **false**: descending order.
        self.asc = asc
        # The reserved parameter.
        self.console_context = console_context
        # The name of the database used to filter the results.
        # 
        # > In the aggregation storage links of some instances, you can specify multiple database names separated by commas. In other links, you can specify only a single database name.
        self.db_name = db_name
        # Specifies whether to populate time series trend data for each statistical result, which corresponds to the **Trend** field in the response. Default value: **true**. Valid values:
        # 
        # - **true**: populates trend data.
        # - **false**: does not populate trend data.
        # 
        # > If this parameter is set to true, the system additionally queries data for each time slice for each result, which significantly increases the query overhead. If the trend filling capability is not enabled for the instance, this parameter does not take effect.
        self.do_fill_trend = do_fill_trend
        # The end time of the query. The value is a UNIX timestamp in milliseconds. The system rounds up the value to the nearest minute.
        # 
        # > The time span between **EndTime** and **StartTime** cannot exceed 7 days. If **EndTime** is earlier than the time when the SQL Explorer feature was enabled for the instance, an error indicating that the query time is earlier than the available time is returned.
        # 
        # > Due to delays in data aggregation, the actual effective value is truncated to a few minutes before the current time. Therefore, data from the most recent few minutes may not be queried.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The list of structured filter conditions. The conditions are passed as key-value pairs. The POP format is **Filters.N.Key** and **Filters.N.Value**. A maximum of 100 pairs can be specified. **Key** is not case-sensitive. Entries with an empty **Value** are ignored. Valid values of **Key** that take effect in this operation:
        # 
        # - **keyWord**: the keywords. The keywords are split into multiple words by whitespace characters and take effect together with the **Keyword** parameter.
        # - **hostAddress**: the access source addresses. Separate multiple addresses with commas. This key takes effect together with **TemplateId** when **Type** is set to **OriginHost**.
        # - **accountName**: the database usernames. Separate multiple usernames with commas.
        # - **dbName**: the database names. Separate multiple names with commas. This key takes effect together with the **DbName** parameter.
        # - **sqlType**: the SQL statement types. Separate multiple types with commas. This key takes effect together with the **SqlType** parameter.
        # - **sqlId**: the SQL template IDs. Separate multiple IDs with commas. This key takes effect together with **TemplateId** when **Type** is set to **SQL**.
        # - **insRole**: the primary/secondary role. Valid values are **master** and **slave**. This value is case-sensitive.
        # 
        # > If you specify a **Key** other than the preceding values, the key is ignored.
        # 
        # > This parameter takes effect only in the aggregation storage links of some instances. In other links, this parameter is completely ignored.
        self.filters = filters
        # The database instance ID.
        # 
        # > This operation supports ApsaraDB RDS for MySQL, PolarDB for MySQL, PolarDB-X, ApsaraDB RDS for PostgreSQL, PolarDB for PostgreSQL, ApsaraDB RDS for SQL Server, and Lindorm instances that have the SQL Explorer feature enabled. MongoDB and Redis instances are not supported. If you invoke this operation for unsupported instances, a fault indicating that the operation is not supported is returned.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The idempotent ID for querying SQL Explorer data. You do not need to specify this parameter for common queries.
        self.job_id = job_id
        # The keywords used to retrieve SQL templates by fuzzy match based on the SQL template content. Separate multiple keywords with spaces. The system first performs keyword match to retrieve up to 1,000 corresponding SQL templates, and then performs aggregation statistics based on these templates. If no matching templates are found, an empty list is returned.
        # 
        # > This parameter does not take effect when **Type** is set to **SQL** and **TemplateId** is specified.
        self.keyword = keyword
        # The ID of the node in the instance. This parameter is used to narrow the statistics scope to the specified node. Only a single node ID is supported. Multiple node IDs separated by commas are not supported.
        # 
        # > This parameter is required only for instances that consist of multiple nodes, such as PolarDB-X and Lindorm instances. You can ignore this parameter for single-node instances.
        self.node_id = node_id
        # The field by which to sort the results. If this parameter is not specified or an unsupported value is specified, the results are sorted by **rt** (total response time). Valid values:
        # 
        # - Response time: **rt**, **avgRt**, **maxRt**, **minRt**, and **rtRate**.
        # - Executions: **count**, **countRate**, and **timestamp**.
        # - Scanned rows: **rowsExamined** and **avgRowsExamined**.
        # - Returned rows: **rowsReturned**, **totalRowsReturned**, **avgRowsReturned**, **maxRowsReturned**, **minRowsReturned**, **maxRowReturned**, and **minRowReturned**.
        # - Logical reads: **logicalRead**, **totalLogicalRead**, **avgLogicalRead**, **maxLogicalRead**, and **minLogicalRead**.
        # - Physical reads: **physicalRead**, **totalPhysicalRead**, **avgPhysicalRead**, **maxPhysicalRead**, and **minPhysicalRead**.
        # - Logical writes (valid only for SQL Server instances): **writes**, **totalWrites**, **avgWrites**, **maxWrites**, and **minWrites**.
        # - CPU time (valid only for SQL Server instances): **totalCpuTime**, **avgCpuTime**, **maxCpuTime**, and **minCpuTime**.
        # - PolarDB-X compute nodes (valid only when **Role** is set to **polarx_cn**): **scnt**, **avgScnt**, **rows**, **avgRows**, **frows**, and **avgFrows**.
        # - Affected rows (valid only for Lindorm instances): **totalAffectRows** and **avgAffectRows**.
        # 
        # > **timestamp** indicates that the results are sorted by data timestamp. The timestamp is a UNIX timestamp in milliseconds.
        # 
        # > Only the first letter is case-insensitive. The remaining characters must exactly match the preceding values. For example, **AvgRt** is valid, but **avgrt** is invalid.
        self.order_by = order_by
        # The page number. Pages start from page 1. If this parameter is not specified, the default value 1 is used.
        self.page_no = page_no
        # The number of statistical entries to return on each page. If this parameter is not specified, the default value 10 is used. The maximum value is 2000.
        # 
        # > If the value exceeds 2000, an InvalidParams error is returned instead of being truncated.
        # 
        # > When statistics are aggregated by access source or database user (when **Type** is set to **FullRequestOrigin** or **FullRequestUser**), a value greater than 100 is reset to 10 in some aggregation storage links.
        self.page_size = page_size
        # The role of the instance node. The value is not case-sensitive. If this parameter is not specified, the role is automatically parsed based on **InstanceId**. Valid values:
        # 
        # - **polarx_cn**: PolarDB-X compute node.
        # - **polarx_dn**: PolarDB-X storage node.
        # 
        # > This value affects the scope of returned fields. For example, **Scnt**, **Rows**, and **Frows** are returned only when the value is **polarx_cn**.
        self.role = role
        # The SQL statement type used to filter the results. Valid values:
        # 
        # - **select**
        # - **insert**
        # - **update**
        # - **delete**
        # 
        # > The values must be in lowercase. In the aggregation storage links of some instances, you can specify multiple values separated by commas. In other links, you can specify only a single value.
        self.sql_type = sql_type
        # The start time of the query. The value is a UNIX timestamp in milliseconds. The system rounds down the value to the nearest minute.
        # 
        # > The start time cannot be more than 30 days before the current time. If the specified start time is earlier than the time when the SQL Explorer feature was enabled for the instance, the start time is automatically adjusted to the enabling time.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The identifier of the statistics object. The meaning varies based on the value of **Type**. Valid values:
        # 
        # - When **Type** is set to **SQL**: specify the SQL template ID, which is the **SqlId** in the response.
        # - When **Type** is set to **OriginHost**: specify the access source address.
        # - When **Type** is set to **User**: specify the database username.
        # 
        # > This parameter does not take effect when **Type** is empty, **FullRequestOrigin**, or **FullRequestUser**.
        # 
        # > When **Type** is set to **SQL**, you can specify multiple template IDs separated by commas. In this case, **Keyword** does not take effect.
        self.template_id = template_id
        # The aggregation or filter dimension for statistics. The value is not case-sensitive. If this parameter is not specified, the statistics are aggregated by SQL template by default. Valid values:
        # 
        # - **FullRequestOrigin**: aggregates statistics by access source address.
        # - **FullRequestUser**: aggregates statistics by database user.
        # - **SQL**: filters statistics by SQL template. You must also specify **TemplateId** as the SQL template ID.
        # - **OriginHost**: filters statistics by access source. You must also specify **TemplateId** as the source address.
        # - **User**: filters statistics by database user. You must also specify **TemplateId** as the username.
        # 
        # > If you specify a value other than the preceding values, an InvalidParams error is returned.
        self.type = type

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc is not None:
            result['Asc'] = self.asc

        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.do_fill_trend is not None:
            result['DoFillTrend'] = self.do_fill_trend

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.role is not None:
            result['Role'] = self.role

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')

        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DoFillTrend') is not None:
            self.do_fill_trend = m.get('DoFillTrend')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribeSqlInsightStatisticRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeSqlInsightStatisticRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the conditional filter. The key is not case-sensitive. For active values, see the metric description of the **Filters** parameter.
        self.key = key
        # The value of the filter condition. If the value is null or an empty string, the filter condition is ignored. Separate multiple values with commas. The specific upper limit depends on the corresponding key.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

