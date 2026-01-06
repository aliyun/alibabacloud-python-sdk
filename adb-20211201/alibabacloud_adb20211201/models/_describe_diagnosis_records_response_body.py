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
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The queried SQL statements.
        self.querys = querys
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
        # The total execution duration. Unit: milliseconds.
        # 
        # >  This value is the cumulative value of the `QueuedTime`, `TotalPlanningTime`, and `ExecutionTime` parameters.
        self.cost = cost
        # The name of the database on which the SQL statement is executed.
        self.database = database
        # The number of rows written to the table by an extract-transform-load (ETL) job.
        self.etl_write_rows = etl_write_rows
        # The execution duration. Unit: milliseconds.
        self.execution_time = execution_time
        # The amount of returned data. Unit: bytes.
        self.output_data_size = output_data_size
        # The number of rows returned.
        self.output_rows = output_rows
        self.pattern_id = pattern_id
        # The peak memory. Unit: bytes.
        self.peak_memory = peak_memory
        # The query ID.
        self.process_id = process_id
        # The query properties.
        # 
        # >  For information about common properties, see [Config and hint configuration parameters](https://help.aliyun.com/document_detail/408955.html).
        self.query_properties = query_properties
        # The amount of time that is consumed for queuing. Unit: milliseconds.
        self.queue_time = queue_time
        # The IP address and port number of the AnalyticDB for MySQL frontend node on which the SQL statement is executed.
        self.rc_host = rc_host
        # The execution duration rank of operators that are used in the SQL statement.
        # 
        # >  This parameter is returned only for SQL statements whose `Status` parameter is `running`.
        self.resource_cost_rank = resource_cost_rank
        # The resource group to which the SQL statement belongs.
        self.resource_group = resource_group
        # The queried SQL statement.
        # 
        # >  For performance considerations, an SQL statement cannot exceed 5,120 characters in length. Otherwise, the SQL statement is truncated. You can call the [DownloadDiagnosisRecords](https://help.aliyun.com/document_detail/308212.html) operation to download the information about SQL statements that meet a query condition for an AnalyticDB for MySQL cluster, including the complete SQL statements.
        self.sql = sql
        # Indicates whether the SQL statement is truncated. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.sqltruncated = sqltruncated
        # The maximum length of the SQL statement. 5120 is returned. Unit: characters. SQL statements that exceed this limit are truncated.
        self.sqltruncated_threshold = sqltruncated_threshold
        # The number of rows scanned.
        self.scan_rows = scan_rows
        # The amount of scanned data. Unit: bytes.
        self.scan_size = scan_size
        # The execution start time of the SQL statement. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The state of the SQL statement. Valid values:
        # 
        # *   **running**
        # *   **finished**
        # *   **failed**
        self.status = status
        # The amount of time that is consumed to generate an execution plan. Unit: milliseconds.
        self.total_planning_time = total_planning_time
        # The total number of stages generated.
        self.total_stages = total_stages
        # The username that is used to execute the SQL statements.
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
        self.name = name
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

