# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListPublishedServicesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListPublishedServicesResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # - **2xx**: The request is successful.
        # 
        # - **3xx**: The request is redirected.
        # 
        # - **4xx**: A client error occurs.
        # 
        # - **5xx**: A server error occurs.
        self.code = code
        # The list of published microservices.
        self.data = data
        # The error code.
        # 
        # - This parameter is not returned if the request is successful.
        # 
        # - For more information about error codes, see the **Error codes** section.
        self.error_code = error_code
        # The returned message.
        # 
        # - Returns **success** if the request is successful.
        # 
        # - Returns an error code if the request fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success
        # The trace ID for querying call details.
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
                temp_model = main_models.ListPublishedServicesResponseBodyData()
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

class ListPublishedServicesResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        group_2ip: str = None,
        groups: List[str] = None,
        ips: List[str] = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # A reserved field.
        self.group_2ip = group_2ip
        # The groups to which the service belongs.
        self.groups = groups
        # The service subscription addresses.
        self.ips = ips
        # The published service name.
        self.name = name
        # The published service type.
        self.type = type
        # The published service version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.group_2ip is not None:
            result['Group2Ip'] = self.group_2ip

        if self.groups is not None:
            result['Groups'] = self.groups

        if self.ips is not None:
            result['Ips'] = self.ips

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Group2Ip') is not None:
            self.group_2ip = m.get('Group2Ip')

        if m.get('Groups') is not None:
            self.groups = m.get('Groups')

        if m.get('Ips') is not None:
            self.ips = m.get('Ips')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

