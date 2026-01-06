# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeTablePartitionDiagnoseResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        dbcluster_id: str = None,
        detection_items: List[main_models.DescribeTablePartitionDiagnoseResponseBodyDetectionItems] = None,
        items: List[main_models.DescribeTablePartitionDiagnoseResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        suggest_max_records_per_partition: int = None,
        suggest_min_records_per_partition: int = None,
        total_count: int = None,
    ):
        # The information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The queried detection items and detection results.
        self.detection_items = detection_items
        # The queried partition diagnostic information.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The recommended maximum number of rows in each partition.
        self.suggest_max_records_per_partition = suggest_max_records_per_partition
        # The recommended minimum number of rows in each partition.
        self.suggest_min_records_per_partition = suggest_min_records_per_partition
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.detection_items:
            for v1 in self.detection_items:
                 if v1:
                    v1.validate()
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['DetectionItems'] = []
        if self.detection_items is not None:
            for k1 in self.detection_items:
                result['DetectionItems'].append(k1.to_map() if k1 else None)

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.suggest_max_records_per_partition is not None:
            result['SuggestMaxRecordsPerPartition'] = self.suggest_max_records_per_partition

        if self.suggest_min_records_per_partition is not None:
            result['SuggestMinRecordsPerPartition'] = self.suggest_min_records_per_partition

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.detection_items = []
        if m.get('DetectionItems') is not None:
            for k1 in m.get('DetectionItems'):
                temp_model = main_models.DescribeTablePartitionDiagnoseResponseBodyDetectionItems()
                self.detection_items.append(temp_model.from_map(k1))

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeTablePartitionDiagnoseResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuggestMaxRecordsPerPartition') is not None:
            self.suggest_max_records_per_partition = m.get('SuggestMaxRecordsPerPartition')

        if m.get('SuggestMinRecordsPerPartition') is not None:
            self.suggest_min_records_per_partition = m.get('SuggestMinRecordsPerPartition')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTablePartitionDiagnoseResponseBodyItems(DaraModel):
    def __init__(
        self,
        partition_detail: str = None,
        partition_number: int = None,
        schema_name: str = None,
        space_ratio: float = None,
        table_name: str = None,
        total_size: int = None,
    ):
        # The improper partitions.
        self.partition_detail = partition_detail
        # The number of partitions.
        self.partition_number = partition_number
        # The name of the database.
        self.schema_name = schema_name
        # The storage percentage of the table. Unit: %.
        # 
        # >  Formula: Table storage percentage = Total data size of a table/Total data size of the cluster × 100%.
        self.space_ratio = space_ratio
        # The name of the table.
        self.table_name = table_name
        # The total data size of the table. Unit: bytes.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.partition_detail is not None:
            result['PartitionDetail'] = self.partition_detail

        if self.partition_number is not None:
            result['PartitionNumber'] = self.partition_number

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.space_ratio is not None:
            result['SpaceRatio'] = self.space_ratio

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PartitionDetail') is not None:
            self.partition_detail = m.get('PartitionDetail')

        if m.get('PartitionNumber') is not None:
            self.partition_number = m.get('PartitionNumber')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SpaceRatio') is not None:
            self.space_ratio = m.get('SpaceRatio')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeTablePartitionDiagnoseResponseBodyDetectionItems(DaraModel):
    def __init__(
        self,
        message: str = None,
        name: str = None,
        status: str = None,
    ):
        # The detection result.
        self.message = message
        # The name of the detection item.
        self.name = name
        # The severity level of the detection result. Valid values:
        # 
        # *   NORMAL
        # *   WARNING
        # *   CRITICAL
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

