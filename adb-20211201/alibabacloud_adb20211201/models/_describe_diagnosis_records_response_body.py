# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnosisRecordsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        querys: List[main_models.DescribeDiagnosisRecordsResponseBodyQuerys] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number. The value is an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # - **30** (default)
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The list of SQL statement details.
        self.querys = querys
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.querys:
            for v1 in self.querys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Querys'] = []
        if self.querys is not None:
            for k1 in self.querys:
                result['Querys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.querys = []
        if m.get('Querys') is not None:
            for k1 in m.get('Querys'):
                temp_model = main_models.DescribeDiagnosisRecordsResponseBodyQuerys()
                self.querys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDiagnosisRecordsResponseBodyQuerys(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        cost: int = None,
        database: str = None,
        etl_write_rows: int = None,
        execution_time: int = None,
        output_data_size: int = None,
        output_rows: int = None,
        pattern_id: str = None,
        peak_memory: int = None,
        process_id: str = None,
        query_properties: List[main_models.DescribeDiagnosisRecordsResponseBodyQuerysQueryProperties] = None,
        queue_time: int = None,
        rc_host: str = None,
        resource_cost_rank: int = None,
        resource_group: str = None,
        sql: str = None,
        sqltruncated: bool = None,
        sqltruncated_threshold: int = None,
        scan_rows: int = None,
        scan_size: int = None,
        start_time: int = None,
        status: str = None,
        total_planning_time: int = None,
        total_stages: int = None,
        user_name: str = None,
    ):
        # The source IP address.
        self.client_ip = client_ip
        # The total execution duration of the query. Unit: milliseconds.
        # 
        # > This duration is the sum of `QueuedTime`, `TotalPlanningTime`, and `ExecutionTime`.
        self.cost = cost
        # The name of the database where the SQL statement is executed.
        self.database = database
        # The number of rows written to a table in an ETL task.
        self.etl_write_rows = etl_write_rows
        # The execution duration of the query. Unit: milliseconds (ms).
        self.execution_time = execution_time
        # The amount of returned data. Unit: bytes.
        self.output_data_size = output_data_size
        # The number of returned rows.
        self.output_rows = output_rows
        # The ID of the SQL pattern.
        # 
        # > Call the [DescribePatternPerformance](https://help.aliyun.com/document_detail/612503.html) operation to view the detailed execution metrics of the SQL pattern within a specified time range.
        self.pattern_id = pattern_id
        # The peak memory. Unit: bytes.
        self.peak_memory = peak_memory
        # The query ID.
        self.process_id = process_id
        # The list of properties that are in effect for the current query.
        # 
        # > For a list of common properties, see [Config and Hint configuration parameters](https://help.aliyun.com/document_detail/408955.html).
        self.query_properties = query_properties
        # The amount of time that the query waited in a queue before execution. Unit: milliseconds (ms).
        self.queue_time = queue_time
        # The IP address and port number of the AnalyticDB for MySQL frontend node that is used to execute the SQL statement.
        self.rc_host = rc_host
        # The ranking of the execution duration of an operator in the SQL statement.
        # 
        # > This parameter is returned only for SQL statements that are in the `running` state.
        self.resource_cost_rank = resource_cost_rank
        # The resource pool to which the SQL statement belongs.
        self.resource_group = resource_group
        # The details of the SQL statement.
        # 
        # > For performance, an SQL statement can be up to 5,120 characters long. Longer statements are truncated. Call the [DownloadDiagnosisRecords](https://help.aliyun.com/document_detail/308212.html) operation to download the summary information of SQL statements that meet the specified conditions, including the complete SQL statements.
        self.sql = sql
        # Indicates whether the length of the query result exceeds the threshold. If the length exceeds the threshold, the query result is truncated. Valid values:
        # 
        # - **true**: The length of the query result exceeds the threshold.
        # 
        # - **false**: The length of the query result does not exceed the threshold.
        self.sqltruncated = sqltruncated
        # The truncation threshold for the SQL statement. The value is fixed at 5,120 characters. SQL statements that exceed this limit are truncated.
        self.sqltruncated_threshold = sqltruncated_threshold
        # The number of scanned rows.
        self.scan_rows = scan_rows
        # The amount of scanned data. Unit: bytes.
        self.scan_size = scan_size
        # The start time of the SQL execution. This value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time
        # The state of the SQL statement. Valid values:
        # 
        # - **running**: The statement is running.
        # 
        # - **finished**: The statement is complete.
        # 
        # - **failed**: The statement failed to be executed.
        self.status = status
        # The amount of time that was required to generate the execution plan. Unit: milliseconds (ms).
        self.total_planning_time = total_planning_time
        # The total number of stages generated for the query.
        self.total_stages = total_stages
        # The username used to execute the SQL statement.
        self.user_name = user_name

    def validate(self):
        if self.query_properties:
            for v1 in self.query_properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.cost is not None:
            result['Cost'] = self.cost

        if self.database is not None:
            result['Database'] = self.database

        if self.etl_write_rows is not None:
            result['EtlWriteRows'] = self.etl_write_rows

        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time

        if self.output_data_size is not None:
            result['OutputDataSize'] = self.output_data_size

        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows

        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        result['QueryProperties'] = []
        if self.query_properties is not None:
            for k1 in self.query_properties:
                result['QueryProperties'].append(k1.to_map() if k1 else None)

        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time

        if self.rc_host is not None:
            result['RcHost'] = self.rc_host

        if self.resource_cost_rank is not None:
            result['ResourceCostRank'] = self.resource_cost_rank

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.sql is not None:
            result['SQL'] = self.sql

        if self.sqltruncated is not None:
            result['SQLTruncated'] = self.sqltruncated

        if self.sqltruncated_threshold is not None:
            result['SQLTruncatedThreshold'] = self.sqltruncated_threshold

        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows

        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.total_planning_time is not None:
            result['TotalPlanningTime'] = self.total_planning_time

        if self.total_stages is not None:
            result['TotalStages'] = self.total_stages

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('EtlWriteRows') is not None:
            self.etl_write_rows = m.get('EtlWriteRows')

        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')

        if m.get('OutputDataSize') is not None:
            self.output_data_size = m.get('OutputDataSize')

        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')

        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        self.query_properties = []
        if m.get('QueryProperties') is not None:
            for k1 in m.get('QueryProperties'):
                temp_model = main_models.DescribeDiagnosisRecordsResponseBodyQuerysQueryProperties()
                self.query_properties.append(temp_model.from_map(k1))

        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')

        if m.get('RcHost') is not None:
            self.rc_host = m.get('RcHost')

        if m.get('ResourceCostRank') is not None:
            self.resource_cost_rank = m.get('ResourceCostRank')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('SQL') is not None:
            self.sql = m.get('SQL')

        if m.get('SQLTruncated') is not None:
            self.sqltruncated = m.get('SQLTruncated')

        if m.get('SQLTruncatedThreshold') is not None:
            self.sqltruncated_threshold = m.get('SQLTruncatedThreshold')

        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')

        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalPlanningTime') is not None:
            self.total_planning_time = m.get('TotalPlanningTime')

        if m.get('TotalStages') is not None:
            self.total_stages = m.get('TotalStages')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeDiagnosisRecordsResponseBodyQuerysQueryProperties(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The property name.
        self.name = name
        # The property value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

