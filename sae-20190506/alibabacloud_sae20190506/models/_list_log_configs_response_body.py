# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListLogConfigsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListLogConfigsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # Indicates whether the logging configurations of an application were obtained. Valid values:
        # 
        # *   **true**: indicates that the configurations were obtained.
        # *   **false**: indicates that the configurations could not be obtained.
        self.code = code
        # The logging configurations.
        self.data = data
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: indicates that the request was successful.
        # *   **3xx**: indicates that the request was redirected.
        # *   **4xx**: indicates that the request was invalid.
        # *   **5xx**: indicates that a server error occurred.
        self.error_code = error_code
        # The ID of the trace. It can be used to query the details of a request.
        self.message = message
        # The returned message.
        # 
        # *   **success** is returned when the request succeeds.
        # *   An error code is returned when the request fails.
        self.request_id = request_id
        self.success = success
        # The logging configurations.
        self.trace_id = trace_id

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListLogConfigsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class ListLogConfigsResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        log_configs: List[main_models.ListLogConfigsResponseBodyDataLogConfigs] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The total number of returned entries.
        self.current_page = current_page
        # The details of the logging configuration.
        self.log_configs = log_configs
        # The error code.
        # 
        # *   The **ErrorCode** parameter is not returned when the request succeeds.
        # *   The **ErrorCode** parameter is returned when the request fails. For more information, see **Error codes** in this topic.
        self.page_size = page_size
        # The number of entries returned on each page.
        self.total_size = total_size

    def validate(self):
        if self.log_configs:
            for v1 in self.log_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['LogConfigs'] = []
        if self.log_configs is not None:
            for k1 in self.log_configs:
                result['LogConfigs'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.log_configs = []
        if m.get('LogConfigs') is not None:
            for k1 in m.get('LogConfigs'):
                temp_model = main_models.ListLogConfigsResponseBodyDataLogConfigs()
                self.log_configs.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListLogConfigsResponseBodyDataLogConfigs(DaraModel):
    def __init__(
        self,
        config_name: str = None,
        create_time: str = None,
        log_dir: str = None,
        log_type: str = None,
        region_id: str = None,
        sls_log_store: str = None,
        sls_project: str = None,
        store_type: str = None,
    ):
        # The path of logs.
        self.config_name = config_name
        # The storage type of logs.
        self.create_time = create_time
        # The path of the log file (log source).
        self.log_dir = log_dir
        # The ID of the region.
        self.log_type = log_type
        # The number of the returned page.
        self.region_id = region_id
        # The time when the configuration was created.
        self.sls_log_store = sls_log_store
        # The type of the log. Set this value to **file_log**.
        self.sls_project = sls_project
        # The ID of the Log Service project.
        self.store_type = store_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_name is not None:
            result['ConfigName'] = self.config_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.log_dir is not None:
            result['LogDir'] = self.log_dir

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store

        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project

        if self.store_type is not None:
            result['StoreType'] = self.store_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LogDir') is not None:
            self.log_dir = m.get('LogDir')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')

        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')

        if m.get('StoreType') is not None:
            self.store_type = m.get('StoreType')

        return self

