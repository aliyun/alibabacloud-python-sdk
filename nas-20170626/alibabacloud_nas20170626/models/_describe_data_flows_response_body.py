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
        self.auto_refresh = auto_refresh
        self.auto_refresh_interval = auto_refresh_interval
        self.auto_refresh_policy = auto_refresh_policy
        self.create_time = create_time
        self.data_flow_id = data_flow_id
        self.description = description
        self.error_message = error_message
        self.file_system_id = file_system_id
        self.file_system_path = file_system_path
        self.fset_description = fset_description
        self.fset_id = fset_id
        self.source_security_type = source_security_type
        self.source_storage = source_storage
        # 源端存储内的访问路径。
        self.source_storage_path = source_storage_path
        self.status = status
        self.throughput = throughput
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

