# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_info: main_models.DescribeHybridCloudUserResponseBodyUserInfo = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the ports that can be used by a hybrid cloud cluster.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserInfo') is not None:
            temp_model = main_models.DescribeHybridCloudUserResponseBodyUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class DescribeHybridCloudUserResponseBodyUserInfo(DaraModel):
    def __init__(
        self,
        http_ports: str = None,
        https_ports: str = None,
    ):
        # The HTTP ports. The value is a string. If multiple ports are returned, the value is in the **port1,port2,port3** format.
        self.http_ports = http_ports
        # The HTTPS ports. The value is a string. If multiple ports are returned, the value is in the **port1,port2,port3** format.
        self.https_ports = https_ports

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports

        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')

        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')

        return self

