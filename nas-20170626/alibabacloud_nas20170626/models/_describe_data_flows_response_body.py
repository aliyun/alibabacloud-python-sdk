# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeDataFlowsResponseBody(DaraModel):
    def __init__(
        self,
        data_flow_info: main_models.DescribeDataFlowsResponseBodyDataFlowInfo = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The dataflow details.
        self.data_flow_info = data_flow_info
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_flow_info:
            self.data_flow_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_flow_info is not None:
            result['DataFlowInfo'] = self.data_flow_info.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFlowInfo') is not None:
            temp_model = main_models.DescribeDataFlowsResponseBodyDataFlowInfo()
            self.data_flow_info = temp_model.from_map(m.get('DataFlowInfo'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDataFlowsResponseBodyDataFlowInfo(DaraModel):
    def __init__(
        self,
        data_flow: List[main_models.DescribeDataFlowsResponseBodyDataFlowInfoDataFlow] = None,
    ):
        self.data_flow = data_flow

    def validate(self):
        if self.data_flow:
            for v1 in self.data_flow:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataFlow'] = []
        if self.data_flow is not None:
            for k1 in self.data_flow:
                result['DataFlow'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_flow = []
        if m.get('DataFlow') is not None:
            for k1 in m.get('DataFlow'):
                temp_model = main_models.DescribeDataFlowsResponseBodyDataFlowInfoDataFlow()
                self.data_flow.append(temp_model.from_map(k1))

        return self

class DescribeDataFlowsResponseBodyDataFlowInfoDataFlow(DaraModel):
    def __init__(
        self,
        auto_refresh: main_models.DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefresh = None,
        auto_refresh_interval: int = None,
        auto_refresh_policy: str = None,
        create_time: str = None,
        data_flow_id: str = None,
        description: str = None,
        error_message: str = None,
        file_system_id: str = None,
        file_system_path: str = None,
        fset_description: str = None,
        fset_id: str = None,
        source_security_type: str = None,
        source_storage: str = None,
        source_storage_path: str = None,
        status: str = None,
        throughput: int = None,
        update_time: str = None,
    ):
        # The details about automatic update policies.
        # 
        # >  Only CPFS supports this parameter.
        self.auto_refresh = auto_refresh
        # The automatic update interval. CPFS checks whether data is updated in the directory at the interval specified by this parameter. If data is updated, CPFS starts an automatic update task. Unit: minutes.
        # 
        # Valid values: 5 to 526600. Default value: 10.
        # 
        # >  Only CPFS supports this parameter.
        self.auto_refresh_interval = auto_refresh_interval
        # The automatic update policy. The updated data in the source storage is imported into the CPFS file system based on the policy. The following information is displayed:
        # 
        # *   None: Updated data in the source storage is not automatically imported into the CPFS file system. You can run a dataflow task to import the updated data from the source storage.
        # *   ImportChanged: Updated data in the source storage is automatically imported into the CPFS file system.
        # 
        # >  Only CPFS is supported.
        self.auto_refresh_policy = auto_refresh_policy
        # The time when the fileset was created.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # >  Only CPFS supports this parameter.
        self.create_time = create_time
        # The ID of the dataflow.
        self.data_flow_id = data_flow_id
        # The description of the dataflow.
        # 
        # Limits:
        # 
        # *   The name must be 2 to 128 characters in length and
        # *   start with a letter but cannot start with `http://` or `https://`.
        # *   The name can contain digits, letters, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The error message. Valid values:
        # 
        # *   None (default): The dataflow status is normal.
        # *   SourceStorageUnreachable: The access path of the source storage is not found.
        # *   ThroughputTooLow: The dataflow throughput is low.
        self.error_message = error_message
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The directory of the fileset in the CPFS file system.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # *   The directory must be a fileset directory in the CPFS file system.
        # 
        # >  Only CPFS is supported.
        self.file_system_path = file_system_path
        # The description of the automatic update.
        # 
        # >  Only CPFS supports this parameter.
        self.fset_description = fset_description
        # The fileset ID.
        # 
        # >  Only CPFS supports this parameter.
        self.fset_id = fset_id
        # The type of security mechanism for the source storage. This parameter must be specified if the source storage is accessed with a security mechanism. Valid value:
        # 
        # *   Null (default): The OSS bucket can be accessed without a security mechanism.
        # *   SSL: The source storage must be accessed with an SSL certificate.
        self.source_security_type = source_security_type
        # The access path of the source storage. Format: `<storage type>://[<account id>:]<path>`.
        # 
        # Among them:
        # 
        # *   storage type: Only OSS is supported.
        # 
        # *   account id: The UID of the account of the source storage.
        # 
        # *   path: The name of the OSS bucket.
        # 
        #     *   The name can contain only lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit.
        #     *   The name must be 8 to 128 characters in length.
        #     *   Must be encoded in UTF-8.
        #     *   The name cannot start with http:// or https://.
        # 
        # > 
        # 
        # *   The OSS bucket must be an existing bucket in the region.
        # 
        # *   Only CPFS for Lingjun V2.6.0 and later support the account id parameter.
        self.source_storage = source_storage
        # The access path in the bucket of the source storage.
        # 
        # >  Only CPFS for Lingjun supports this parameter.
        self.source_storage_path = source_storage_path
        # The dataflow status. The following information is displayed:
        # 
        # *   Starting: The dataflow is being created or enabled.
        # *   Running: The dataflow has been created and is running properly.
        # *   Updating: The dataflow is being modified. For example, the dataflow throughput is increased and the automatic update interval is modified.
        # *   Deleting: The dataflow is being deleted.
        # *   Stopping: The dataflow is being disabled.
        # *   Stopped: The dataflow has been disabled.
        # *   Misconfigured: The dataflow configuration is abnormal. For example, the source storage is inaccessible, and the automatic update cannot be completed due to low dataflow throughput.
        self.status = status
        # The maximum dataflow throughput. Unit: MB/s. Valid value:
        # 
        # *   600
        # *   1200
        # *   1500
        # 
        # > 
        # 
        # *   The dataflow throughput must be less than the I/O throughput of the file system.
        # 
        # *   Only CPFS supports this parameter.
        self.throughput = throughput
        # The time when the fileset was last updated.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # >  Only CPFS supports this parameter.
        self.update_time = update_time

    def validate(self):
        if self.auto_refresh:
            self.auto_refresh.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_refresh is not None:
            result['AutoRefresh'] = self.auto_refresh.to_map()

        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval

        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id

        if self.description is not None:
            result['Description'] = self.description

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path

        if self.fset_description is not None:
            result['FsetDescription'] = self.fset_description

        if self.fset_id is not None:
            result['FsetId'] = self.fset_id

        if self.source_security_type is not None:
            result['SourceSecurityType'] = self.source_security_type

        if self.source_storage is not None:
            result['SourceStorage'] = self.source_storage

        if self.source_storage_path is not None:
            result['SourceStoragePath'] = self.source_storage_path

        if self.status is not None:
            result['Status'] = self.status

        if self.throughput is not None:
            result['Throughput'] = self.throughput

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRefresh') is not None:
            temp_model = main_models.DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefresh()
            self.auto_refresh = temp_model.from_map(m.get('AutoRefresh'))

        if m.get('AutoRefreshInterval') is not None:
            self.auto_refresh_interval = m.get('AutoRefreshInterval')

        if m.get('AutoRefreshPolicy') is not None:
            self.auto_refresh_policy = m.get('AutoRefreshPolicy')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')

        if m.get('FsetDescription') is not None:
            self.fset_description = m.get('FsetDescription')

        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')

        if m.get('SourceSecurityType') is not None:
            self.source_security_type = m.get('SourceSecurityType')

        if m.get('SourceStorage') is not None:
            self.source_storage = m.get('SourceStorage')

        if m.get('SourceStoragePath') is not None:
            self.source_storage_path = m.get('SourceStoragePath')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefresh(DaraModel):
    def __init__(
        self,
        auto_refresh: List[main_models.DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefreshAutoRefresh] = None,
    ):
        self.auto_refresh = auto_refresh

    def validate(self):
        if self.auto_refresh:
            for v1 in self.auto_refresh:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoRefresh'] = []
        if self.auto_refresh is not None:
            for k1 in self.auto_refresh:
                result['AutoRefresh'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_refresh = []
        if m.get('AutoRefresh') is not None:
            for k1 in m.get('AutoRefresh'):
                temp_model = main_models.DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefreshAutoRefresh()
                self.auto_refresh.append(temp_model.from_map(k1))

        return self

class DescribeDataFlowsResponseBodyDataFlowInfoDataFlowAutoRefreshAutoRefresh(DaraModel):
    def __init__(
        self,
        refresh_path: str = None,
    ):
        # The automatic update directory. CPFS automatically checks whether the source data only in the directory is updated and imports the updated data.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1,024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # 
        # >  The directory must be an existing directory in the CPFS file system and must be in a fileset where the dataflow is enabled.
        self.refresh_path = refresh_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')

        return self

