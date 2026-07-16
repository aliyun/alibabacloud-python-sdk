# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListAppServicesPageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAppServicesPageResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The API status code or POP error code. Valid values:
        # 
        # - **2xx**: Success.
        # 
        # - **3xx**: Redirect.
        # 
        # - **4xx**: client error.
        # 
        # - **5xx**: server error.
        self.code = code
        # The service list.
        self.data = data
        # The error code.
        # 
        # - This parameter is not returned if the request is successful.
        # 
        # - This parameter is returned if the request fails. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # A message that describes the outcome of the request.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success
        # The trace ID used to query the details of a request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAppServicesPageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class ListAppServicesPageResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        page_number: str = None,
        page_size: str = None,
        result: List[main_models.ListAppServicesPageResponseBodyDataResult] = None,
        total_size: str = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The page number.
        self.page_number = page_number
        # The number of entries per page. The value must be in the range of 0 to 9999.
        self.page_size = page_size
        # The returned results.
        self.result = result
        # The total number of entries.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListAppServicesPageResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListAppServicesPageResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        edas_app_id: str = None,
        edas_app_name: str = None,
        group: str = None,
        instance_num: int = None,
        service_name: str = None,
        version: str = None,
    ):
        # The application ID.
        self.edas_app_id = edas_app_id
        # The application name.
        self.edas_app_name = edas_app_name
        # The service group. This value is user-defined.
        self.group = group
        # The number of instances.
        self.instance_num = instance_num
        # The service name.
        self.service_name = service_name
        # The service version. This value is user-defined.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edas_app_id is not None:
            result['EdasAppId'] = self.edas_app_id

        if self.edas_app_name is not None:
            result['EdasAppName'] = self.edas_app_name

        if self.group is not None:
            result['Group'] = self.group

        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdasAppId') is not None:
            self.edas_app_id = m.get('EdasAppId')

        if m.get('EdasAppName') is not None:
            self.edas_app_name = m.get('EdasAppName')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

