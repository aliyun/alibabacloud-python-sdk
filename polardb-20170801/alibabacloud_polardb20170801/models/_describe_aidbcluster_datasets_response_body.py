# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAIDBClusterDatasetsResponseBody(DaraModel):
    def __init__(
        self,
        continuation_token: str = None,
        data_service_id: str = None,
        dataset_id: str = None,
        dataset_mode: str = None,
        dataset_type: str = None,
        datasets: List[main_models.DescribeAIDBClusterDatasetsResponseBodyDatasets] = None,
        file_count: str = None,
        is_truncated: bool = None,
        next_continuation_token: str = None,
        page_number: str = None,
        page_size: str = None,
        relative_dbcluster_id: str = None,
        request_id: str = None,
        total_count: str = None,
        total_records: str = None,
    ):
        # The continuation token from the request.
        self.continuation_token = continuation_token
        # The data service ID.
        self.data_service_id = data_service_id
        # The dataset ID.
        self.dataset_id = dataset_id
        # The training mode. Valid values:
        # 
        # - **sft**: Supervised Fine-Tuning (SFT).
        # 
        # - **grpo**: Reinforcement Learning (RL).
        # 
        # - **text**: Text generation.
        self.dataset_mode = dataset_mode
        # The dataset type. Valid values:
        # 
        # - **train**: The training set.
        # 
        # - **eval**: The evaluation set.
        self.dataset_type = dataset_type
        # An array of dataset objects.
        self.datasets = datasets
        # The total number of files in the dataset.
        self.file_count = file_count
        # Indicates if more datasets are available. Valid values:
        # 
        # - **true**: More datasets are available.
        # 
        # - **false**: All datasets have been listed.
        self.is_truncated = is_truncated
        # The token for retrieving the next page of results. This parameter is returned only if `IsTruncated` is `true`.
        self.next_continuation_token = next_continuation_token
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The relative DB cluster ID.
        self.relative_dbcluster_id = relative_dbcluster_id
        # The request ID.
        self.request_id = request_id
        # The total count of datasets.
        self.total_count = total_count
        # The total number of records.
        self.total_records = total_records

    def validate(self):
        if self.datasets:
            for v1 in self.datasets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.continuation_token is not None:
            result['ContinuationToken'] = self.continuation_token

        if self.data_service_id is not None:
            result['DataServiceId'] = self.data_service_id

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_mode is not None:
            result['DatasetMode'] = self.dataset_mode

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        result['Datasets'] = []
        if self.datasets is not None:
            for k1 in self.datasets:
                result['Datasets'].append(k1.to_map() if k1 else None)

        if self.file_count is not None:
            result['FileCount'] = self.file_count

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.next_continuation_token is not None:
            result['NextContinuationToken'] = self.next_continuation_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.relative_dbcluster_id is not None:
            result['RelativeDBClusterId'] = self.relative_dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_records is not None:
            result['TotalRecords'] = self.total_records

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContinuationToken') is not None:
            self.continuation_token = m.get('ContinuationToken')

        if m.get('DataServiceId') is not None:
            self.data_service_id = m.get('DataServiceId')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetMode') is not None:
            self.dataset_mode = m.get('DatasetMode')

        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        self.datasets = []
        if m.get('Datasets') is not None:
            for k1 in m.get('Datasets'):
                temp_model = main_models.DescribeAIDBClusterDatasetsResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k1))

        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('NextContinuationToken') is not None:
            self.next_continuation_token = m.get('NextContinuationToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RelativeDBClusterId') is not None:
            self.relative_dbcluster_id = m.get('RelativeDBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')

        return self

class DescribeAIDBClusterDatasetsResponseBodyDatasets(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        capacity: str = None,
        creation_time: str = None,
        dataset_id: str = None,
        dataset_type: str = None,
        file_name: str = None,
        last_modified: str = None,
        path: str = None,
        storage_type: str = None,
        train_mode: str = None,
    ):
        # The bucket name.
        self.bucket_name = bucket_name
        # The file size in bytes.
        self.capacity = capacity
        # The time the file was created, in UTC and formatted as ISO 8601.
        self.creation_time = creation_time
        # The dataset ID.
        self.dataset_id = dataset_id
        # The dataset type. Valid values:
        # 
        # - **train**: The training set.
        # 
        # - **eval**: The evaluation set.
        self.dataset_type = dataset_type
        # The file name.
        self.file_name = file_name
        # The time the file was last modified, in UTC and formatted as ISO 8601.
        self.last_modified = last_modified
        # The file path.
        self.path = path
        # The storage type. The only valid value is:
        # 
        # - **Standard**.
        self.storage_type = storage_type
        # The training mode. Valid values:
        # 
        # - **sft**: Supervised Fine-Tuning (SFT).
        # 
        # - **grpo**: Reinforcement Learning (RL).
        # 
        # - **text**: Text generation.
        self.train_mode = train_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.path is not None:
            result['Path'] = self.path

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.train_mode is not None:
            result['TrainMode'] = self.train_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('TrainMode') is not None:
            self.train_mode = m.get('TrainMode')

        return self

