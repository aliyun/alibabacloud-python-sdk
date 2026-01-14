# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class QuerySlbSpecResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.QuerySlbSpecResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return value.
        self.code = code
        # The data entries returned.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned. If the request is successful, a success message is returned. If the request fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QuerySlbSpecResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySlbSpecResponseBodyData(DaraModel):
    def __init__(
        self,
        id: int = None,
        max_connection: str = None,
        name: str = None,
        new_connection_per_second: str = None,
        qps: str = None,
        spec: str = None,
    ):
        # The ID of the returned data.
        self.id = id
        # The maximum number of connections.
        self.max_connection = max_connection
        # The name of the instance.
        self.name = name
        # The number of connections per second.
        self.new_connection_per_second = new_connection_per_second
        # The number of queries per second (QPS).
        self.qps = qps
        # The specification of the instance.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.max_connection is not None:
            result['MaxConnection'] = self.max_connection

        if self.name is not None:
            result['Name'] = self.name

        if self.new_connection_per_second is not None:
            result['NewConnectionPerSecond'] = self.new_connection_per_second

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MaxConnection') is not None:
            self.max_connection = m.get('MaxConnection')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewConnectionPerSecond') is not None:
            self.new_connection_per_second = m.get('NewConnectionPerSecond')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

