# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeWorkerDetectionResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        detection_items: List[main_models.DescribeWorkerDetectionResponseBodyDetectionItems] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The queried detection items and detection results.
        self.detection_items = detection_items
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.detection_items:
            for v1 in self.detection_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['DetectionItems'] = []
        if self.detection_items is not None:
            for k1 in self.detection_items:
                result['DetectionItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.detection_items = []
        if m.get('DetectionItems') is not None:
            for k1 in m.get('DetectionItems'):
                temp_model = main_models.DescribeWorkerDetectionResponseBodyDetectionItems()
                self.detection_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWorkerDetectionResponseBodyDetectionItems(DaraModel):
    def __init__(
        self,
        message: str = None,
        name: str = None,
        results: main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResults = None,
        status: str = None,
    ):
        # The information about the detection result.
        self.message = message
        # The name of the detection item.
        self.name = name
        # The detection result items.
        self.results = results
        # The severity level of the detection result. Valid values:
        # 
        # *   NORMAL
        # *   WARNING
        # *   CRITICAL
        self.status = status

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.results is not None:
            result['Results'] = self.results.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Results') is not None:
            temp_model = main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResults()
            self.results = temp_model.from_map(m.get('Results'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeWorkerDetectionResponseBodyDetectionItemsResults(DaraModel):
    def __init__(
        self,
        operator_agg: List[main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorAgg] = None,
        operator_details: List[main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorDetails] = None,
        partitioned_tables: List[main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsPartitionedTables] = None,
        skewed_tables: List[main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsSkewedTables] = None,
        top_access_tables: List[main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsTopAccessTables] = None,
    ):
        # The detection result items of operator metric aggregation.
        self.operator_agg = operator_agg
        # The detection result items of abnormal operators.
        self.operator_details = operator_details
        # The detection result items of improper partitioned tables.
        self.partitioned_tables = partitioned_tables
        # The detection result items of skewed tables.
        self.skewed_tables = skewed_tables
        # The detection result items of table access.
        self.top_access_tables = top_access_tables

    def validate(self):
        if self.operator_agg:
            for v1 in self.operator_agg:
                 if v1:
                    v1.validate()
        if self.operator_details:
            for v1 in self.operator_details:
                 if v1:
                    v1.validate()
        if self.partitioned_tables:
            for v1 in self.partitioned_tables:
                 if v1:
                    v1.validate()
        if self.skewed_tables:
            for v1 in self.skewed_tables:
                 if v1:
                    v1.validate()
        if self.top_access_tables:
            for v1 in self.top_access_tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperatorAgg'] = []
        if self.operator_agg is not None:
            for k1 in self.operator_agg:
                result['OperatorAgg'].append(k1.to_map() if k1 else None)

        result['OperatorDetails'] = []
        if self.operator_details is not None:
            for k1 in self.operator_details:
                result['OperatorDetails'].append(k1.to_map() if k1 else None)

        result['PartitionedTables'] = []
        if self.partitioned_tables is not None:
            for k1 in self.partitioned_tables:
                result['PartitionedTables'].append(k1.to_map() if k1 else None)

        result['SkewedTables'] = []
        if self.skewed_tables is not None:
            for k1 in self.skewed_tables:
                result['SkewedTables'].append(k1.to_map() if k1 else None)

        result['TopAccessTables'] = []
        if self.top_access_tables is not None:
            for k1 in self.top_access_tables:
                result['TopAccessTables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operator_agg = []
        if m.get('OperatorAgg') is not None:
            for k1 in m.get('OperatorAgg'):
                temp_model = main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorAgg()
                self.operator_agg.append(temp_model.from_map(k1))

        self.operator_details = []
        if m.get('OperatorDetails') is not None:
            for k1 in m.get('OperatorDetails'):
                temp_model = main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorDetails()
                self.operator_details.append(temp_model.from_map(k1))

        self.partitioned_tables = []
        if m.get('PartitionedTables') is not None:
            for k1 in m.get('PartitionedTables'):
                temp_model = main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsPartitionedTables()
                self.partitioned_tables.append(temp_model.from_map(k1))

        self.skewed_tables = []
        if m.get('SkewedTables') is not None:
            for k1 in m.get('SkewedTables'):
                temp_model = main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsSkewedTables()
                self.skewed_tables.append(temp_model.from_map(k1))

        self.top_access_tables = []
        if m.get('TopAccessTables') is not None:
            for k1 in m.get('TopAccessTables'):
                temp_model = main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsTopAccessTables()
                self.top_access_tables.append(temp_model.from_map(k1))

        return self

class DescribeWorkerDetectionResponseBodyDetectionItemsResultsTopAccessTables(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        search_results: List[main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsTopAccessTablesSearchResults] = None,
    ):
        # The name of the detection metric.
        self.metric_name = metric_name
        # The detection result items of table access.
        self.search_results = search_results

    def validate(self):
        if self.search_results:
            for v1 in self.search_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        result['SearchResults'] = []
        if self.search_results is not None:
            for k1 in self.search_results:
                result['SearchResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        self.search_results = []
        if m.get('SearchResults') is not None:
            for k1 in m.get('SearchResults'):
                temp_model = main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsTopAccessTablesSearchResults()
                self.search_results.append(temp_model.from_map(k1))

        return self

class DescribeWorkerDetectionResponseBodyDetectionItemsResultsTopAccessTablesSearchResults(DaraModel):
    def __init__(
        self,
        access_count: int = None,
        avg_scan_cost: float = None,
        avg_scan_size: float = None,
        max_scan_cost: int = None,
        max_scan_size: int = None,
        table_name: str = None,
    ):
        # The number of accesses to the table.
        self.access_count = access_count
        # The average amount of time for scanning. Unit: milliseconds.
        self.avg_scan_cost = avg_scan_cost
        # The average data size for scanning. Unit: bytes.
        self.avg_scan_size = avg_scan_size
        # The maximum amount of time for scanning. Unit: milliseconds.
        self.max_scan_cost = max_scan_cost
        # The maximum data size for scanning. Unit: bytes.
        self.max_scan_size = max_scan_size
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_count is not None:
            result['AccessCount'] = self.access_count

        if self.avg_scan_cost is not None:
            result['AvgScanCost'] = self.avg_scan_cost

        if self.avg_scan_size is not None:
            result['AvgScanSize'] = self.avg_scan_size

        if self.max_scan_cost is not None:
            result['MaxScanCost'] = self.max_scan_cost

        if self.max_scan_size is not None:
            result['MaxScanSize'] = self.max_scan_size

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessCount') is not None:
            self.access_count = m.get('AccessCount')

        if m.get('AvgScanCost') is not None:
            self.avg_scan_cost = m.get('AvgScanCost')

        if m.get('AvgScanSize') is not None:
            self.avg_scan_size = m.get('AvgScanSize')

        if m.get('MaxScanCost') is not None:
            self.max_scan_cost = m.get('MaxScanCost')

        if m.get('MaxScanSize') is not None:
            self.max_scan_size = m.get('MaxScanSize')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DescribeWorkerDetectionResponseBodyDetectionItemsResultsSkewedTables(DaraModel):
    def __init__(
        self,
        ddl: str = None,
        partition_count: int = None,
        schema_name: str = None,
        shard_skewed_rows: str = None,
        table_name: str = None,
        total_data_size: int = None,
        total_local_data_size: str = None,
        total_pk_size: int = None,
        total_remote_data_size: int = None,
        total_row_count: int = None,
    ):
        # The SQL statement that is used to create the table.
        self.ddl = ddl
        # The number of partitions.
        self.partition_count = partition_count
        # The name of the database.
        self.schema_name = schema_name
        # The number of skewed rows in the table.
        self.shard_skewed_rows = shard_skewed_rows
        # The name of the table.
        self.table_name = table_name
        # The total data size of the table. Unit: bytes.
        self.total_data_size = total_data_size
        # The size of hot data. Unit: bytes.
        self.total_local_data_size = total_local_data_size
        # The data size of the primary key. Unit: bytes.
        self.total_pk_size = total_pk_size
        # The size of cold data. Unit: bytes.
        self.total_remote_data_size = total_remote_data_size
        # The number of rows in the table.
        self.total_row_count = total_row_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddl is not None:
            result['DDL'] = self.ddl

        if self.partition_count is not None:
            result['PartitionCount'] = self.partition_count

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.shard_skewed_rows is not None:
            result['ShardSkewedRows'] = self.shard_skewed_rows

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.total_data_size is not None:
            result['TotalDataSize'] = self.total_data_size

        if self.total_local_data_size is not None:
            result['TotalLocalDataSize'] = self.total_local_data_size

        if self.total_pk_size is not None:
            result['TotalPkSize'] = self.total_pk_size

        if self.total_remote_data_size is not None:
            result['TotalRemoteDataSize'] = self.total_remote_data_size

        if self.total_row_count is not None:
            result['TotalRowCount'] = self.total_row_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')

        if m.get('PartitionCount') is not None:
            self.partition_count = m.get('PartitionCount')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('ShardSkewedRows') is not None:
            self.shard_skewed_rows = m.get('ShardSkewedRows')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TotalDataSize') is not None:
            self.total_data_size = m.get('TotalDataSize')

        if m.get('TotalLocalDataSize') is not None:
            self.total_local_data_size = m.get('TotalLocalDataSize')

        if m.get('TotalPkSize') is not None:
            self.total_pk_size = m.get('TotalPkSize')

        if m.get('TotalRemoteDataSize') is not None:
            self.total_remote_data_size = m.get('TotalRemoteDataSize')

        if m.get('TotalRowCount') is not None:
            self.total_row_count = m.get('TotalRowCount')

        return self

class DescribeWorkerDetectionResponseBodyDetectionItemsResultsPartitionedTables(DaraModel):
    def __init__(
        self,
        ddl: str = None,
        partition_count: str = None,
        partition_ids: str = None,
        schema_name: str = None,
        table_name: str = None,
        total_data_size: int = None,
    ):
        # The SQL statement that is used to create the table.
        self.ddl = ddl
        # The number of partitions.
        self.partition_count = partition_count
        # The ID of the improper partition.
        self.partition_ids = partition_ids
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name
        # The total data size of the table.
        self.total_data_size = total_data_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddl is not None:
            result['DDL'] = self.ddl

        if self.partition_count is not None:
            result['PartitionCount'] = self.partition_count

        if self.partition_ids is not None:
            result['PartitionIds'] = self.partition_ids

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.total_data_size is not None:
            result['TotalDataSize'] = self.total_data_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')

        if m.get('PartitionCount') is not None:
            self.partition_count = m.get('PartitionCount')

        if m.get('PartitionIds') is not None:
            self.partition_ids = m.get('PartitionIds')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TotalDataSize') is not None:
            self.total_data_size = m.get('TotalDataSize')

        return self

class DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorDetails(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        search_results: List[main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorDetailsSearchResults] = None,
    ):
        # The name of the detection metric.
        self.metric_name = metric_name
        # The detection result items of abnormal operators.
        self.search_results = search_results

    def validate(self):
        if self.search_results:
            for v1 in self.search_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        result['SearchResults'] = []
        if self.search_results is not None:
            for k1 in self.search_results:
                result['SearchResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        self.search_results = []
        if m.get('SearchResults') is not None:
            for k1 in m.get('SearchResults'):
                temp_model = main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorDetailsSearchResults()
                self.search_results.append(temp_model.from_map(k1))

        return self

class DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorDetailsSearchResults(DaraModel):
    def __init__(
        self,
        input_rows: int = None,
        input_size: int = None,
        operator_cost: int = None,
        operator_info: str = None,
        operator_name: str = None,
        output_rows: int = None,
        output_size: int = None,
        peak_memory: int = None,
        process_id: str = None,
        stage_id: str = None,
    ):
        # The number of rows input by the operator.
        self.input_rows = input_rows
        # The amount of data input by the operator. Unit: bytes.
        self.input_size = input_size
        # The total CPU time consumed by all operators in the stage, which is equivalent to the total CPU time of the stage. You can use this parameter to determine which parts of the stage consume a large amount of computing resources. Unit: milliseconds.
        self.operator_cost = operator_cost
        # The property information about the operator.
        self.operator_info = operator_info
        # The name of the operator.
        self.operator_name = operator_name
        # The number of rows output by the operator.
        self.output_rows = output_rows
        # The amount of data output by the operator. Unit: bytes.
        self.output_size = output_size
        # The peak memory. Unit: bytes.
        self.peak_memory = peak_memory
        # The query ID that can be used for diagnostics.
        self.process_id = process_id
        # The stage ID.
        self.stage_id = stage_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_rows is not None:
            result['InputRows'] = self.input_rows

        if self.input_size is not None:
            result['InputSize'] = self.input_size

        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost

        if self.operator_info is not None:
            result['OperatorInfo'] = self.operator_info

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows

        if self.output_size is not None:
            result['OutputSize'] = self.output_size

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputRows') is not None:
            self.input_rows = m.get('InputRows')

        if m.get('InputSize') is not None:
            self.input_size = m.get('InputSize')

        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')

        if m.get('OperatorInfo') is not None:
            self.operator_info = m.get('OperatorInfo')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')

        if m.get('OutputSize') is not None:
            self.output_size = m.get('OutputSize')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        return self

class DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorAgg(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        search_results: List[main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorAggSearchResults] = None,
    ):
        # The detection result items of operator metric aggregation.
        self.metric_name = metric_name
        # The detection result items of operator metric aggregation.
        self.search_results = search_results

    def validate(self):
        if self.search_results:
            for v1 in self.search_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        result['SearchResults'] = []
        if self.search_results is not None:
            for k1 in self.search_results:
                result['SearchResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        self.search_results = []
        if m.get('SearchResults') is not None:
            for k1 in m.get('SearchResults'):
                temp_model = main_models.DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorAggSearchResults()
                self.search_results.append(temp_model.from_map(k1))

        return self

class DescribeWorkerDetectionResponseBodyDetectionItemsResultsOperatorAggSearchResults(DaraModel):
    def __init__(
        self,
        avg_value: float = None,
        max_value: int = None,
        operator_count: int = None,
        operator_name: str = None,
        total_value: int = None,
    ):
        # The average value of the operator metric.
        self.avg_value = avg_value
        # The maximum value of the operator metric.
        self.max_value = max_value
        # The number of occurrences of the operator.
        self.operator_count = operator_count
        # The name of the operator.
        self.operator_name = operator_name
        # The cumulative value of the operator metric.
        self.total_value = total_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_value is not None:
            result['AvgValue'] = self.avg_value

        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.operator_count is not None:
            result['OperatorCount'] = self.operator_count

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.total_value is not None:
            result['TotalValue'] = self.total_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgValue') is not None:
            self.avg_value = m.get('AvgValue')

        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('OperatorCount') is not None:
            self.operator_count = m.get('OperatorCount')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('TotalValue') is not None:
            self.total_value = m.get('TotalValue')

        return self

