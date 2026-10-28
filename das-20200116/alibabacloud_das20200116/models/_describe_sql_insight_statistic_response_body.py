# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlInsightStatisticResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSqlInsightStatisticResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response status code.
        self.code = code
        # The envelope for the asynchronous query result. The first call returns **ResultId** and **State**. You must poll the API with the exact same request parameters until **State** is **SUCCESS**, and then retrieve the statistical details from **List**.
        self.data = data
        # The response message. An error description is returned when the request fails.
        self.message = message
        # The unique identifier of the request, which can be used for troubleshooting.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed. Check the cause based on **Code** and **Message**.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeSqlInsightStatisticResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSqlInsightStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSqlInsightStatisticResponseBodyDataData = None,
        error_code: int = None,
        is_finish: bool = None,
        message: str = None,
        request_key: str = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        # The SQL Explorer statistical query result.
        # 
        # > Returned only when **State** is **SUCCESS**.
        self.data = data
        # The error code for the failed asynchronous query.
        # 
        # > This field is returned only when the query fails.
        self.error_code = error_code
        # Indicates whether the asynchronous query has finished. Valid values:
        # 
        # - **true**: **State** is **SUCCESS** or **FAIL**.
        # - **false**: **State** is **RUNNING**.
        self.is_finish = is_finish
        # The error description for the failed asynchronous query.
        # 
        # > This field is returned only when the query fails.
        self.message = message
        # The hash identifier of the request parameters.
        # 
        # > This operation does not return this field. Use **ResultId** to identify the asynchronous query.
        self.request_key = request_key
        # The asynchronous query result ID, which is in the format of an async_ prefix followed by a hash value. It is calculated based on all business parameters of the current request.
        # 
        # > Repeated calls with the same parameters hit the same query result. Therefore, you must carry the exact same request parameters as the first call when polling. Any parameter change generates a different **ResultId** and triggers a new query.
        self.result_id = result_id
        # The current state of the asynchronous query. Valid values:
        # 
        # - **RUNNING**: The query is running. Continue polling.
        # - **SUCCESS**: The query is successful. The **Data** field has a value.
        # - **FAIL**: The query failed.
        # 
        # > When the query fails, the operation directly returns an error code and an error message, instead of a normal response body with **State** set to **FAIL**.
        self.state = state
        # The time when the asynchronous query was submitted, which is a UNIX timestamp in milliseconds.
        # 
        # > When the query fails, this value is the time when the failure occurred.
        self.timestamp = timestamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.is_finish is not None:
            result['IsFinish'] = self.is_finish

        if self.message is not None:
            result['Message'] = self.message

        if self.request_key is not None:
            result['RequestKey'] = self.request_key

        if self.result_id is not None:
            result['ResultId'] = self.result_id

        if self.state is not None:
            result['State'] = self.state

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeSqlInsightStatisticResponseBodyDataData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('IsFinish') is not None:
            self.is_finish = m.get('IsFinish')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestKey') is not None:
            self.request_key = m.get('RequestKey')

        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class DescribeSqlInsightStatisticResponseBodyDataData(DaraModel):
    def __init__(
        self,
        extra: Any = None,
        list: List[main_models.DescribeSqlInsightStatisticResponseBodyDataDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The extended information.
        # 
        # > This operation does not return this field.
        self.extra = extra
        # The list of SQL Explorer statistical results. Each element is a statistical entry under an aggregation dimension.
        self.list = list
        # The current page number, which corresponds to the request parameter **PageNo**.
        self.page_no = page_no
        # The number of entries returned per page, which corresponds to the request parameter **PageSize**.
        self.page_size = page_size
        # The total number of statistical entries that meet the query conditions, which can be used for pagination.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.DescribeSqlInsightStatisticResponseBodyDataDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeSqlInsightStatisticResponseBodyDataDataList(DaraModel):
    def __init__(
        self,
        affect_rows: int = None,
        agg_key: str = None,
        avg_affect_rows: float = None,
        avg_cpu_time: float = None,
        avg_frows: float = None,
        avg_lock_wait_time: float = None,
        avg_logical_read: float = None,
        avg_physical_async_read: float = None,
        avg_physical_read: float = None,
        avg_physical_sync_read: float = None,
        avg_rows: float = None,
        avg_rows_examined: float = None,
        avg_rows_returned: float = None,
        avg_rows_updated: float = None,
        avg_rt: float = None,
        avg_scan_rows: float = None,
        avg_scnt: float = None,
        avg_writes: float = None,
        count: int = None,
        count_rate: float = None,
        cpu_time: int = None,
        database: str = None,
        error_code: str = None,
        error_count: int = None,
        first_time: int = None,
        frows: int = None,
        hash: str = None,
        ip: str = None,
        lock_wait_time: float = None,
        logical_read: float = None,
        max_cpu_time: int = None,
        max_logical_read: int = None,
        max_physical_read: int = None,
        max_rows_examined: int = None,
        max_rows_returned: int = None,
        max_rt: float = None,
        max_writes: int = None,
        min_cpu_time: int = None,
        min_logical_read: int = None,
        min_physical_read: int = None,
        min_rows_returned: int = None,
        min_rt: float = None,
        min_writes: int = None,
        origin_alias: str = None,
        origin_host: str = None,
        params: str = None,
        physical_async_read: float = None,
        physical_read: int = None,
        physical_sync_read: float = None,
        port: int = None,
        psql: str = None,
        rows: int = None,
        rows_examined: int = None,
        rows_returned: int = None,
        rt: float = None,
        rt_greater_than_one_second_count: int = None,
        rt_rate: float = None,
        sample_type: str = None,
        scan_rows: int = None,
        scnt: int = None,
        sql: str = None,
        sql_id: str = None,
        sql_new: str = None,
        sql_text_feature: str = None,
        sql_type: str = None,
        sum_rows_updated: float = None,
        tables: List[str] = None,
        thread_id: str = None,
        time_rate: float = None,
        timestamp: int = None,
        total_affect_rows: int = None,
        total_rt: int = None,
        total_scan_rows: int = None,
        trend: List[main_models.DescribeSqlInsightStatisticResponseBodyDataDataListTrend] = None,
        update_rows: int = None,
        user: str = None,
        version: int = None,
        vpc_id: str = None,
        writes: int = None,
    ):
        # The number of affected rows for a single SQL statement. For **SELECT** statements, this indicates the number of scanned rows. For **DML** statements, this indicates the number of affected rows.
        # 
        # > Returned only for Lindorm instances.
        self.affect_rows = affect_rows
        # The value of the aggregation dimension for the current statistics. This value varies based on the **Type** request parameter. Valid values:
        # 
        # - When aggregated by SQL template: the SQL template ID, which is the same as **SqlId**.
        # - When **Type** is **FullRequestOrigin**: the source access address.
        # - When **Type** is **FullRequestUser**: the database username.
        self.agg_key = agg_key
        # The average number of affected rows.
        # 
        # > Returned only for Lindorm instances. For other engines, the value is null.
        self.avg_affect_rows = avg_affect_rows
        # The average CPU time consumed by SQL execution, in microseconds.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.avg_cpu_time = avg_cpu_time
        # The average number of rows fetched by PolarDB-X compute nodes from data nodes.
        # 
        # > This is an exclusive metric for PolarDB-X compute nodes. For other engines, the value is null or 0.
        self.avg_frows = avg_frows
        # The average lock wait time per execution, in milliseconds.
        # 
        # > Data is available only when **Version** is **1**.
        self.avg_lock_wait_time = avg_lock_wait_time
        # The average number of logical reads per execution.
        # 
        # > Data is available only when **Version** is **1**.
        self.avg_logical_read = avg_logical_read
        # The average number of physical asynchronous reads per execution.
        # 
        # > Data is available only when **Version** is **1**.
        self.avg_physical_async_read = avg_physical_async_read
        # The average number of physical reads.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.avg_physical_read = avg_physical_read
        # The average number of physical synchronous reads per execution.
        # 
        # > Data is available only when **Version** is **1**.
        self.avg_physical_sync_read = avg_physical_sync_read
        # The average number of updated and returned rows for PolarDB-X compute nodes.
        # 
        # > This is an exclusive metric for PolarDB-X compute nodes. For other engines, the value is null or 0.
        self.avg_rows = avg_rows
        # The average number of scanned rows per execution.
        self.avg_rows_examined = avg_rows_examined
        # The average number of returned rows per execution.
        self.avg_rows_returned = avg_rows_returned
        # The average number of updated rows per execution.
        self.avg_rows_updated = avg_rows_updated
        # The average execution time per execution, in milliseconds.
        self.avg_rt = avg_rt
        # The average number of scanned rows.
        # 
        # > This operation does not return this field. To obtain the average number of scanned rows, use **AvgRowsExamined**.
        self.avg_scan_rows = avg_scan_rows
        # The average number of requests sent from PolarDB-X compute nodes to data nodes.
        # 
        # > This is an exclusive metric for PolarDB-X compute nodes. For other engines, the value is null or 0.
        self.avg_scnt = avg_scnt
        # The average number of logical writes.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.avg_writes = avg_writes
        # The total number of executions for the SQL template within the statistical period.
        self.count = count
        # The ratio of the number of times the SQL template in this entry is executed to the total number of times SQL statements execute on the instance. Valid values: 0 to 1.
        self.count_rate = count_rate
        # The total CPU time consumed by SQL execution, in microseconds.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.cpu_time = cpu_time
        # The name of the database where the SQL statement is executed.
        self.database = database
        # The error code returned by the SQL execution.
        # 
        # > Error codes belong to the details of a single SQL statement. This operation returns aggregated statistics at the template level and does not return this field. To check error occurrences, use **ErrorCount**.
        self.error_code = error_code
        # The number of execution errors for the SQL template within the statistical period.
        self.error_count = error_count
        # The time when the SQL template first appeared. The time is a UNIX timestamp in milliseconds.
        # 
        # > This operation does not return this field.
        self.first_time = first_time
        # The total number of rows fetched by PolarDB-X compute nodes from data nodes.
        # 
        # > This is an exclusive metric for PolarDB-X compute nodes. For other engines, the value is null or 0.
        self.frows = frows
        # The hash value of the SQL template, returned together with the SQL template.
        # 
        # > This value is generated by the kernel of PolarDB-X compute nodes. For instances that are not PolarDB-X compute nodes, the value is empty.
        self.hash = hash
        # The endpoint of the instance to which the statistical data belongs.
        # 
        # > Whether this field is returned depends on the converged storage link of the instance. For some links, the value is null.
        self.ip = ip
        # The total lock wait time, in milliseconds.
        # 
        # > Data is available only when **Version** is **1**.
        self.lock_wait_time = lock_wait_time
        # The total number of logical reads.
        # 
        # > Data is available only when **Version** is **1**.
        self.logical_read = logical_read
        # The maximum CPU time consumed in a single execution, in microseconds.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.max_cpu_time = max_cpu_time
        # The maximum number of logical reads in a single execution.
        # 
        # > Data is available only when **Version** is **1**.
        self.max_logical_read = max_logical_read
        # The maximum number of physical reads in a single execution.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.max_physical_read = max_physical_read
        # The maximum number of scanned rows in a single execution.
        # 
        # > This operation does not return this field. To obtain the number of scanned rows, use **RowsExamined** and **AvgRowsExamined**.
        self.max_rows_examined = max_rows_examined
        # The maximum number of returned rows in a single execution.
        self.max_rows_returned = max_rows_returned
        # The maximum execution time in a single execution, in milliseconds.
        self.max_rt = max_rt
        # The maximum number of logical writes in a single execution.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.max_writes = max_writes
        # The minimum CPU time consumed in a single execution, in microseconds.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.min_cpu_time = min_cpu_time
        # The minimum number of logical reads in a single execution.
        # 
        # > Data is available only when **Version** is **1**.
        self.min_logical_read = min_logical_read
        # The minimum number of physical reads in a single execution.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.min_physical_read = min_physical_read
        # The minimum number of returned rows in a single execution.
        self.min_rows_returned = min_rows_returned
        # The minimum execution time in a single execution, in milliseconds.
        self.min_rt = min_rt
        # The minimum number of logical writes in a single execution.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.min_writes = min_writes
        # The display alias configured for the source access address.
        # 
        # > Returned only when aggregated by access source (when **Type** is **FullRequestOrigin**). In other scenarios, the value is null.
        self.origin_alias = origin_alias
        # The source address of the client that initiated the SQL statement.
        # 
        # > When **Type** is **FullRequestOrigin**, this field is the aggregation dimension for the statistics.
        self.origin_host = origin_host
        # The parameter content of the SQL sample.
        # 
        # > This operation returns aggregated statistics at the template level and does not return this field.
        self.params = params
        # The total number of physical asynchronous reads.
        # 
        # > Data is available only when **Version** is **1**.
        self.physical_async_read = physical_async_read
        # The total number of physical reads.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.physical_read = physical_read
        # The total number of physical synchronous reads.
        # 
        # > Data is available only when **Version** is **1**.
        self.physical_sync_read = physical_sync_read
        # The connection port of the instance to which the statistical data belongs.
        # 
        # > Whether this field is returned depends on the converged storage link of the instance. For some links, the value is null.
        self.port = port
        # The parameterized SQL template text, which is the statement with constants in the SQL replaced by placeholders.
        self.psql = psql
        # The total number of updated and returned rows for PolarDB-X compute nodes.
        # 
        # > This is an exclusive metric for PolarDB-X compute nodes. For other engines, the value is null or 0.
        self.rows = rows
        # The total number of scanned rows for the SQL template within the statistical period.
        self.rows_examined = rows_examined
        # The total number of returned rows for the SQL template within the statistical period.
        self.rows_returned = rows_returned
        # The total execution time of the SQL template within the statistical period, in milliseconds.
        # 
        # > For PolarDB-X compute nodes (where **Role** is **polarx_cn**) with a kernel version earlier than 5.4.13, this value is converted from microseconds to milliseconds.
        self.rt = rt
        # The number of times the execution duration exceeded 1 second.
        # 
        # > Whether this field is returned depends on the aggregated storage link of the instance. For some links, the value is null.
        self.rt_greater_than_one_second_count = rt_greater_than_one_second_count
        # The ratio of the total execution time of this statistic to the total execution time of all SQL statements for the instance. Valid values: 0 to 1.
        self.rt_rate = rt_rate
        # The type identifier of the sample data.
        # 
        # > This operation returns aggregated statistics and does not return this field.
        self.sample_type = sample_type
        # The number of scanned rows for a single SQL statement.
        # 
        # > This operation returns aggregated statistics at the template dimension and does not return this field. Use the aggregated metrics **RowsExamined** and **AvgRowsExamined** instead.
        self.scan_rows = scan_rows
        # The total number of requests sent from PolarDB-X compute nodes to data nodes.
        # 
        # > This is an exclusive metric for PolarDB-X compute nodes. For other engines, the value is null or 0.
        self.scnt = scnt
        # The original SQL text.
        # 
        # > The statistical results return the SQL template (**Psql**) and do not return this field.
        self.sql = sql
        # The SQL template ID, which uniquely identifies a category of parameterized SQL statements. Multiple executions under the same template are aggregated into a single statistic. You can use this ID to associate the same category of SQL statements across multi-dimensional queries.
        self.sql_id = sql_id
        # The SQL text after unified processing of parameter values, used in sample data scenarios.
        # 
        # > This operation does not return this field.
        self.sql_new = sql_new
        # The SQL text feature value, used in SQL analysis scenarios.
        # 
        # > This operation does not return this field.
        self.sql_text_feature = sql_text_feature
        # The SQL type. Valid values:
        # 
        # - **select**
        # - **insert**
        # - **update**
        # - **delete**
        # - **other**
        self.sql_type = sql_type
        # The total number of updated rows for the SQL template within the statistical period.
        self.sum_rows_updated = sum_rows_updated
        # The list of table names involved in the SQL statement.
        self.tables = tables
        # The database thread ID that executed the SQL statement.
        # 
        # > The thread ID belongs to the details of a single SQL statement. This operation returns aggregated statistics at the template dimension and does not return this field.
        self.thread_id = thread_id
        # The execution time proportion.
        # 
        # > This operation returns the execution time proportion through **RtRate** and does not return this field.
        self.time_rate = time_rate
        # The data timestamp, which is a UNIX timestamp in milliseconds.
        # 
        # > The statistical results are aggregated at the SQL template dimension and do not return this field.
        self.timestamp = timestamp
        # The total number of affected rows.
        # 
        # > This field is returned only for Lindorm instances. For other engines, the value is null.
        self.total_affect_rows = total_affect_rows
        # The total execution time of the SQL statement.
        # 
        # > This operation does not return this field. Use **Rt** for the total execution time.
        self.total_rt = total_rt
        # The total number of scanned rows.
        # 
        # > This operation does not return this field. Use **RowsExamined** for the total number of scanned rows.
        self.total_scan_rows = total_scan_rows
        # The trend sequence of execution counts for the SQL template, divided by time slices within the query time window.
        # 
        # > This field is returned only when the request parameter **DoFillTrend** is set to **true** and the trend padding feature is enabled for the instance. The time slice interval is automatically determined by the query span. Time slices with no data may be padded with zeros.
        self.trend = trend
        # The number of updated rows for a single SQL statement.
        # 
        # > This operation returns aggregated statistics at the template dimension and does not return this field. Use the aggregated metrics **SumRowsUpdated** and **AvgRowsUpdated** instead.
        self.update_rows = update_rows
        # The database username that executed the SQL statement.
        # 
        # > When **Type** is **FullRequestUser**, this field is the aggregation dimension for this statistic.
        self.user = user
        # The version of the SQL Explorer data collection link. If the instance collects logical read or lock wait data, the value is **1**. Otherwise, the value is **0**. Valid values:
        # 
        # - **0**: V0 basic collection link.
        # - **1**: V1 collection link, which collects four additional metrics based on V0: **LockWaitTime**, **LogicalRead**, **PhysicalSyncRead**, and **PhysicalAsyncRead**.
        # 
        # > When **0** is returned, the preceding extended metrics have no data.
        self.version = version
        # The VPC ID of the instance to which the statistical data belongs.
        # 
        # > Whether this field is returned depends on the aggregated storage link of the instance. For some links, the value is null.
        self.vpc_id = vpc_id
        # The total number of logical writes.
        # 
        # > This is an exclusive metric for SQL Server instances. For other engines, the value is null.
        self.writes = writes

    def validate(self):
        if self.trend:
            for v1 in self.trend:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows

        if self.agg_key is not None:
            result['AggKey'] = self.agg_key

        if self.avg_affect_rows is not None:
            result['AvgAffectRows'] = self.avg_affect_rows

        if self.avg_cpu_time is not None:
            result['AvgCpuTime'] = self.avg_cpu_time

        if self.avg_frows is not None:
            result['AvgFrows'] = self.avg_frows

        if self.avg_lock_wait_time is not None:
            result['AvgLockWaitTime'] = self.avg_lock_wait_time

        if self.avg_logical_read is not None:
            result['AvgLogicalRead'] = self.avg_logical_read

        if self.avg_physical_async_read is not None:
            result['AvgPhysicalAsyncRead'] = self.avg_physical_async_read

        if self.avg_physical_read is not None:
            result['AvgPhysicalRead'] = self.avg_physical_read

        if self.avg_physical_sync_read is not None:
            result['AvgPhysicalSyncRead'] = self.avg_physical_sync_read

        if self.avg_rows is not None:
            result['AvgRows'] = self.avg_rows

        if self.avg_rows_examined is not None:
            result['AvgRowsExamined'] = self.avg_rows_examined

        if self.avg_rows_returned is not None:
            result['AvgRowsReturned'] = self.avg_rows_returned

        if self.avg_rows_updated is not None:
            result['AvgRowsUpdated'] = self.avg_rows_updated

        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt

        if self.avg_scan_rows is not None:
            result['AvgScanRows'] = self.avg_scan_rows

        if self.avg_scnt is not None:
            result['AvgScnt'] = self.avg_scnt

        if self.avg_writes is not None:
            result['AvgWrites'] = self.avg_writes

        if self.count is not None:
            result['Count'] = self.count

        if self.count_rate is not None:
            result['CountRate'] = self.count_rate

        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time

        if self.database is not None:
            result['Database'] = self.database

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.frows is not None:
            result['Frows'] = self.frows

        if self.hash is not None:
            result['Hash'] = self.hash

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.lock_wait_time is not None:
            result['LockWaitTime'] = self.lock_wait_time

        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read

        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time

        if self.max_logical_read is not None:
            result['MaxLogicalRead'] = self.max_logical_read

        if self.max_physical_read is not None:
            result['MaxPhysicalRead'] = self.max_physical_read

        if self.max_rows_examined is not None:
            result['MaxRowsExamined'] = self.max_rows_examined

        if self.max_rows_returned is not None:
            result['MaxRowsReturned'] = self.max_rows_returned

        if self.max_rt is not None:
            result['MaxRt'] = self.max_rt

        if self.max_writes is not None:
            result['MaxWrites'] = self.max_writes

        if self.min_cpu_time is not None:
            result['MinCpuTime'] = self.min_cpu_time

        if self.min_logical_read is not None:
            result['MinLogicalRead'] = self.min_logical_read

        if self.min_physical_read is not None:
            result['MinPhysicalRead'] = self.min_physical_read

        if self.min_rows_returned is not None:
            result['MinRowsReturned'] = self.min_rows_returned

        if self.min_rt is not None:
            result['MinRt'] = self.min_rt

        if self.min_writes is not None:
            result['MinWrites'] = self.min_writes

        if self.origin_alias is not None:
            result['OriginAlias'] = self.origin_alias

        if self.origin_host is not None:
            result['OriginHost'] = self.origin_host

        if self.params is not None:
            result['Params'] = self.params

        if self.physical_async_read is not None:
            result['PhysicalAsyncRead'] = self.physical_async_read

        if self.physical_read is not None:
            result['PhysicalRead'] = self.physical_read

        if self.physical_sync_read is not None:
            result['PhysicalSyncRead'] = self.physical_sync_read

        if self.port is not None:
            result['Port'] = self.port

        if self.psql is not None:
            result['Psql'] = self.psql

        if self.rows is not None:
            result['Rows'] = self.rows

        if self.rows_examined is not None:
            result['RowsExamined'] = self.rows_examined

        if self.rows_returned is not None:
            result['RowsReturned'] = self.rows_returned

        if self.rt is not None:
            result['Rt'] = self.rt

        if self.rt_greater_than_one_second_count is not None:
            result['RtGreaterThanOneSecondCount'] = self.rt_greater_than_one_second_count

        if self.rt_rate is not None:
            result['RtRate'] = self.rt_rate

        if self.sample_type is not None:
            result['SampleType'] = self.sample_type

        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows

        if self.scnt is not None:
            result['Scnt'] = self.scnt

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_new is not None:
            result['SqlNew'] = self.sql_new

        if self.sql_text_feature is not None:
            result['SqlTextFeature'] = self.sql_text_feature

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.sum_rows_updated is not None:
            result['SumRowsUpdated'] = self.sum_rows_updated

        if self.tables is not None:
            result['Tables'] = self.tables

        if self.thread_id is not None:
            result['ThreadId'] = self.thread_id

        if self.time_rate is not None:
            result['TimeRate'] = self.time_rate

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.total_affect_rows is not None:
            result['TotalAffectRows'] = self.total_affect_rows

        if self.total_rt is not None:
            result['TotalRt'] = self.total_rt

        if self.total_scan_rows is not None:
            result['TotalScanRows'] = self.total_scan_rows

        result['Trend'] = []
        if self.trend is not None:
            for k1 in self.trend:
                result['Trend'].append(k1.to_map() if k1 else None)

        if self.update_rows is not None:
            result['UpdateRows'] = self.update_rows

        if self.user is not None:
            result['User'] = self.user

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.writes is not None:
            result['Writes'] = self.writes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')

        if m.get('AggKey') is not None:
            self.agg_key = m.get('AggKey')

        if m.get('AvgAffectRows') is not None:
            self.avg_affect_rows = m.get('AvgAffectRows')

        if m.get('AvgCpuTime') is not None:
            self.avg_cpu_time = m.get('AvgCpuTime')

        if m.get('AvgFrows') is not None:
            self.avg_frows = m.get('AvgFrows')

        if m.get('AvgLockWaitTime') is not None:
            self.avg_lock_wait_time = m.get('AvgLockWaitTime')

        if m.get('AvgLogicalRead') is not None:
            self.avg_logical_read = m.get('AvgLogicalRead')

        if m.get('AvgPhysicalAsyncRead') is not None:
            self.avg_physical_async_read = m.get('AvgPhysicalAsyncRead')

        if m.get('AvgPhysicalRead') is not None:
            self.avg_physical_read = m.get('AvgPhysicalRead')

        if m.get('AvgPhysicalSyncRead') is not None:
            self.avg_physical_sync_read = m.get('AvgPhysicalSyncRead')

        if m.get('AvgRows') is not None:
            self.avg_rows = m.get('AvgRows')

        if m.get('AvgRowsExamined') is not None:
            self.avg_rows_examined = m.get('AvgRowsExamined')

        if m.get('AvgRowsReturned') is not None:
            self.avg_rows_returned = m.get('AvgRowsReturned')

        if m.get('AvgRowsUpdated') is not None:
            self.avg_rows_updated = m.get('AvgRowsUpdated')

        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')

        if m.get('AvgScanRows') is not None:
            self.avg_scan_rows = m.get('AvgScanRows')

        if m.get('AvgScnt') is not None:
            self.avg_scnt = m.get('AvgScnt')

        if m.get('AvgWrites') is not None:
            self.avg_writes = m.get('AvgWrites')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CountRate') is not None:
            self.count_rate = m.get('CountRate')

        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('Frows') is not None:
            self.frows = m.get('Frows')

        if m.get('Hash') is not None:
            self.hash = m.get('Hash')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('LockWaitTime') is not None:
            self.lock_wait_time = m.get('LockWaitTime')

        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')

        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')

        if m.get('MaxLogicalRead') is not None:
            self.max_logical_read = m.get('MaxLogicalRead')

        if m.get('MaxPhysicalRead') is not None:
            self.max_physical_read = m.get('MaxPhysicalRead')

        if m.get('MaxRowsExamined') is not None:
            self.max_rows_examined = m.get('MaxRowsExamined')

        if m.get('MaxRowsReturned') is not None:
            self.max_rows_returned = m.get('MaxRowsReturned')

        if m.get('MaxRt') is not None:
            self.max_rt = m.get('MaxRt')

        if m.get('MaxWrites') is not None:
            self.max_writes = m.get('MaxWrites')

        if m.get('MinCpuTime') is not None:
            self.min_cpu_time = m.get('MinCpuTime')

        if m.get('MinLogicalRead') is not None:
            self.min_logical_read = m.get('MinLogicalRead')

        if m.get('MinPhysicalRead') is not None:
            self.min_physical_read = m.get('MinPhysicalRead')

        if m.get('MinRowsReturned') is not None:
            self.min_rows_returned = m.get('MinRowsReturned')

        if m.get('MinRt') is not None:
            self.min_rt = m.get('MinRt')

        if m.get('MinWrites') is not None:
            self.min_writes = m.get('MinWrites')

        if m.get('OriginAlias') is not None:
            self.origin_alias = m.get('OriginAlias')

        if m.get('OriginHost') is not None:
            self.origin_host = m.get('OriginHost')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('PhysicalAsyncRead') is not None:
            self.physical_async_read = m.get('PhysicalAsyncRead')

        if m.get('PhysicalRead') is not None:
            self.physical_read = m.get('PhysicalRead')

        if m.get('PhysicalSyncRead') is not None:
            self.physical_sync_read = m.get('PhysicalSyncRead')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Psql') is not None:
            self.psql = m.get('Psql')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('RowsExamined') is not None:
            self.rows_examined = m.get('RowsExamined')

        if m.get('RowsReturned') is not None:
            self.rows_returned = m.get('RowsReturned')

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        if m.get('RtGreaterThanOneSecondCount') is not None:
            self.rt_greater_than_one_second_count = m.get('RtGreaterThanOneSecondCount')

        if m.get('RtRate') is not None:
            self.rt_rate = m.get('RtRate')

        if m.get('SampleType') is not None:
            self.sample_type = m.get('SampleType')

        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')

        if m.get('Scnt') is not None:
            self.scnt = m.get('Scnt')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlNew') is not None:
            self.sql_new = m.get('SqlNew')

        if m.get('SqlTextFeature') is not None:
            self.sql_text_feature = m.get('SqlTextFeature')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('SumRowsUpdated') is not None:
            self.sum_rows_updated = m.get('SumRowsUpdated')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        if m.get('ThreadId') is not None:
            self.thread_id = m.get('ThreadId')

        if m.get('TimeRate') is not None:
            self.time_rate = m.get('TimeRate')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TotalAffectRows') is not None:
            self.total_affect_rows = m.get('TotalAffectRows')

        if m.get('TotalRt') is not None:
            self.total_rt = m.get('TotalRt')

        if m.get('TotalScanRows') is not None:
            self.total_scan_rows = m.get('TotalScanRows')

        self.trend = []
        if m.get('Trend') is not None:
            for k1 in m.get('Trend'):
                temp_model = main_models.DescribeSqlInsightStatisticResponseBodyDataDataListTrend()
                self.trend.append(temp_model.from_map(k1))

        if m.get('UpdateRows') is not None:
            self.update_rows = m.get('UpdateRows')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('Writes') is not None:
            self.writes = m.get('Writes')

        return self

class DescribeSqlInsightStatisticResponseBodyDataDataListTrend(DaraModel):
    def __init__(
        self,
        timestamp: int = None,
        value: Any = None,
    ):
        # The timestamp of the trend point, which is a UNIX timestamp in milliseconds.
        self.timestamp = timestamp
        # The number of SQL executions within the time slice.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

