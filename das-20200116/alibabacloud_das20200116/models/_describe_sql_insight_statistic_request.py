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
        # The sort direction. Default value: **false** (descending). Valid values:
        # 
        # - **true**: ascending.
        # - **false**: descending.
        self.asc = asc
        # A reserved parameter.
        self.console_context = console_context
        # The database name used for filtering.
        # 
        # > In certain aggregation storage pipelines, you can specify multiple database names separated by commas. In other pipelines, only a single database name is supported.
        self.db_name = db_name
        # Specifies whether to populate time series trend data for each statistical entry, which corresponds to the **Trend** field in the response. Default value: **true**. Valid values:
        # 
        # - **true**: Populates trend data.
        # - **false**: Does not populate trend data.
        # 
        # > Enabling this option triggers additional queries for each time slice per entry, which significantly increases query overhead. If the trend filling capability is not enabled for the instance, this parameter does not take effect.
        self.do_fill_trend = do_fill_trend
        # The end time of the query. Specify a UNIX timestamp in milliseconds. The system rounds up to the nearest minute.
        # 
        # > The span between this value and **StartTime** must not exceed 7 days. If **EndTime** is earlier than the time when SQL Explorer was enabled for the instance, an error indicating that the query time is earlier than the available time is returned.
        # 
        # > Because data aggregation involves latency, the actual effective value is trimmed to a few minutes before the current time. Data from the most recent minutes may not be available.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The list of structured filter conditions, specified as Key/Value pairs. The POP format is **Filters.N.Key** and **Filters.N.Value**, with a maximum of 100 pairs. **Key** is case-insensitive. Entries with an empty **Value** are ignored. Valid values of **Key** for this operation:
        # 
        # - **keyWord**: the keyword. The value is split by whitespace into multiple words and takes effect together with the **Keyword** parameter.
        # - **hostAddress**: the access source address. Separate multiple values with commas. This takes effect together with **TemplateId** when **Type** is set to **OriginHost**.
        # - **accountName**: the database username. Separate multiple values with commas.
        # - **dbName**: the database name. Separate multiple values with commas. This takes effect together with the **DbName** parameter.
        # - **sqlType**: the SQL type. Separate multiple values with commas. This takes effect together with the **SqlType** parameter.
        # - **sqlId**: the SQL template ID. Separate multiple values with commas. This takes effect together with **TemplateId** when **Type** is set to **SQL**.
        # - **insRole**: the primary/secondary role. Valid values: **master** and **slave**. These values are case-sensitive.
        # 
        # > Any **Key** value other than the preceding values is ignored.
        # 
        # > This parameter takes effect only in certain aggregation storage pipelines. In other pipelines, this parameter is entirely ignored.
        self.filters = filters
        # The database instance ID.
        # 
        # > This operation supports RDS for MySQL, PolarDB for MySQL, PolarDB-X, RDS for PostgreSQL, PolarDB for PostgreSQL, RDS for SQL Server, and Lindorm instances that have SQL Explorer enabled. MongoDB and Redis instances are not supported. Calling this operation for unsupported instances returns an error indicating that the operation is not supported.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The idempotency ID for the SQL Explorer data query. This parameter is not required for regular queries.
        self.job_id = job_id
        # The keyword for fuzzy retrieve on SQL template content. Separate multiple keywords with spaces. The system first performs keyword match to find the corresponding SQL templates (up to 1,000 templates), and then performs aggregation statistics based on these templates. If no templates match, an empty list is returned.
        # 
        # > This parameter does not take effect when **Type** is set to **SQL** and **TemplateId** is specified.
        self.keyword = keyword
        # The node ID of the instance. This parameter narrows the statistical scope to the specified node. Only a single node ID is supported. You cannot specify multiple node IDs separated by commas.
        # 
        # > This parameter is required only for instances that consist of multiple nodes, such as PolarDB-X and Lindorm instances. You can ignore this parameter for single-node instances.
        self.node_id = node_id
        # The field used for sorting. If this parameter is not specified or an unsupported value is specified, the results are sorted by **rt** (total response time). Valid values:
        # 
        # - Response time: **rt**, **avgRt**, **maxRt**, **minRt**, **rtRate**.
        # - Executions: **count**, **countRate**, **timestamp**.
        # - Scan rows: **rowsExamined**, **avgRowsExamined**.
        # - Returned rows: **rowsReturned**, **totalRowsReturned**, **avgRowsReturned**, **maxRowsReturned**, **minRowsReturned**, **maxRowReturned**, **minRowReturned**.
        # - Logical reads: **logicalRead**, **totalLogicalRead**, **avgLogicalRead**, **maxLogicalRead**, **minLogicalRead**.
        # - Physical reads: **physicalRead**, **totalPhysicalRead**, **avgPhysicalRead**, **maxPhysicalRead**, **minPhysicalRead**.
        # - Logical writes (valid only for SQL Server instances): **writes**, **totalWrites**, **avgWrites**, **maxWrites**, **minWrites**.
        # - CPU time (valid only for SQL Server instances): **totalCpuTime**, **avgCpuTime**, **maxCpuTime**, **minCpuTime**.
        # - PolarDB-X compute node metrics (valid only when **Role** is set to **polarx_cn**): **scnt**, **avgScnt**, **rows**, **avgRows**, **frows**, **avgFrows**.
        # - Affected rows (valid only for Lindorm instances): **totalAffectRows**, **avgAffectRows**.
        # 
        # > **timestamp** sorts by the data timestamp, which is a millisecond-level UNIX timestamp.
        # 
        # > Only the first letter is case-insensitive. The remaining characters must exactly match the preceding values. For example, **AvgRt** is valid but **avgrt** is not.
        self.order_by = order_by
        # The page number. Pages start from page 1. Default value: 1.
        self.page_no = page_no
        # The number of statistical entries per page. Default value: 10. Maximum value: 2000.
        # 
        # > A value greater than 2000 returns an InvalidParams error instead of being trimmed.
        # 
        # > When aggregating by access source or database user (**Type** is set to **FullRequestOrigin** or **FullRequestUser**), a value greater than 100 may be reset to 10 in certain aggregation storage pipelines.
        self.page_size = page_size
        # The role of the instance node. The value is case-insensitive. If this parameter is not specified, the role is automatically resolved from **InstanceId**. Valid values:
        # 
        # - **polarx_cn**: PolarDB-X compute node.
        # - **polarx_dn**: PolarDB-X storage node.
        # 
        # > This value affects the scope of returned fields. For example, **Scnt**, **Rows**, and **Frows** are returned only when the value is **polarx_cn**.
        self.role = role
        # The SQL type used for filtering. Valid values:
        # 
        # - **select**
        # - **insert**
        # - **update**
        # - **delete**
        # 
        # > Values are lowercase. In certain aggregation storage pipelines, you can specify multiple values separated by commas. In other pipelines, only a single value is supported.
        self.sql_type = sql_type
        # The start time of the query. Specify a UNIX timestamp in milliseconds. The system rounds down to the nearest minute.
        # 
        # > The value must be within the last 30 days. If the value is earlier than the time when SQL Explorer was enabled for the instance, it is automatically adjusted to the time when SQL Explorer was enabled.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The identifier of the statistical object. The meaning varies depending on the value of **Type**. Valid values:
        # 
        # - When **Type** is set to **SQL**: the SQL template ID, which corresponds to **SqlId** in the response.
        # - When **Type** is set to **OriginHost**: the access source address.
        # - When **Type** is set to **User**: the database username.
        # 
        # > This parameter does not take effect when **Type** is not specified, or is set to **FullRequestOrigin** or **FullRequestUser**.
        # 
        # > When **Type** is set to **SQL**, you can specify multiple template IDs separated by commas. In this case, the **Keyword** parameter does not take effect.
        self.template_id = template_id
        # The aggregation or filter dimension for statistics. The value is case-insensitive. If this parameter is not specified, statistics are aggregated by SQL template by default. Valid values:
        # 
        # - **FullRequestOrigin**: Aggregates by access source address.
        # - **FullRequestUser**: Aggregates by database user.
        # - **SQL**: Filters by SQL template. You must also specify **TemplateId** as the SQL template ID.
        # - **OriginHost**: Filters by access source. You must also specify **TemplateId** as the source address.
        # - **User**: Filters by database user. You must also specify **TemplateId** as the username.
        # 
        # > Specifying a value other than the preceding values returns an InvalidParams error.
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
        # The key of the filter condition. The value is case-insensitive. For valid values, see the description of the **Filters** parameter.
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

