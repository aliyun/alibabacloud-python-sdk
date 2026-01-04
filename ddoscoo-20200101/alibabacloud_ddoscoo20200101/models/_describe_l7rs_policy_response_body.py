# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeL7RsPolicyResponseBody(DaraModel):
    def __init__(
        self,
        attributes: List[main_models.DescribeL7RsPolicyResponseBodyAttributes] = None,
        proxy_mode: str = None,
        request_id: str = None,
        rs_attr_rw_timeout_max: int = None,
        upstream_retry: int = None,
    ):
        # The details about the parameters for back-to-origin settings.
        self.attributes = attributes
        # The scheduling algorithm for back-to-origin traffic. Valid values:
        # 
        # *   **ip_hash**: the IP hash algorithm. This algorithm is used to redirect the requests from the same IP address to the same origin server.
        # *   **rr**: the round-robin algorithm. This algorithm is used to redirect requests to origin servers in turn.
        # *   **least_time**: the least response time algorithm. This algorithm is used to minimize the latency when requests are forwarded from Anti-DDoS Pro or Anti-DDoS Premium instances to origin servers based on the intelligent DNS resolution feature.
        self.proxy_mode = proxy_mode
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The timeout period for a read or write connection.
        self.rs_attr_rw_timeout_max = rs_attr_rw_timeout_max
        # The back-to-origin retry switch. Valid values:
        # 
        # *   **1**: on
        # *   **0**: off
        self.upstream_retry = upstream_retry

    def validate(self):
        if self.attributes:
            for v1 in self.attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attributes'] = []
        if self.attributes is not None:
            for k1 in self.attributes:
                result['Attributes'].append(k1.to_map() if k1 else None)

        if self.proxy_mode is not None:
            result['ProxyMode'] = self.proxy_mode

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rs_attr_rw_timeout_max is not None:
            result['RsAttrRwTimeoutMax'] = self.rs_attr_rw_timeout_max

        if self.upstream_retry is not None:
            result['UpstreamRetry'] = self.upstream_retry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k1 in m.get('Attributes'):
                temp_model = main_models.DescribeL7RsPolicyResponseBodyAttributes()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('ProxyMode') is not None:
            self.proxy_mode = m.get('ProxyMode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RsAttrRwTimeoutMax') is not None:
            self.rs_attr_rw_timeout_max = m.get('RsAttrRwTimeoutMax')

        if m.get('UpstreamRetry') is not None:
            self.upstream_retry = m.get('UpstreamRetry')

        return self

class DescribeL7RsPolicyResponseBodyAttributes(DaraModel):
    def __init__(
        self,
        attribute: main_models.DescribeL7RsPolicyResponseBodyAttributesAttribute = None,
        real_server: str = None,
        rs_type: int = None,
    ):
        # The parameters for back-to-origin settings.
        self.attribute = attribute
        # The address of the origin server.
        self.real_server = real_server
        # The address type of the origin server. Valid values:
        # 
        # *   **0**: IP address
        # *   **1**: domain name
        self.rs_type = rs_type

    def validate(self):
        if self.attribute:
            self.attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute.to_map()

        if self.real_server is not None:
            result['RealServer'] = self.real_server

        if self.rs_type is not None:
            result['RsType'] = self.rs_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            temp_model = main_models.DescribeL7RsPolicyResponseBodyAttributesAttribute()
            self.attribute = temp_model.from_map(m.get('Attribute'))

        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')

        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')

        return self

class DescribeL7RsPolicyResponseBodyAttributesAttribute(DaraModel):
    def __init__(
        self,
        connect_timeout: int = None,
        fail_timeout: int = None,
        max_fails: int = None,
        mode: str = None,
        read_timeout: int = None,
        send_timeout: int = None,
        weight: int = None,
    ):
        # The timeout period for a new connection. Valid values: **1** to **10**. Unit: seconds. Default value: **5**.
        self.connect_timeout = connect_timeout
        # The expiration time of a connection, in seconds. If the number of failures at the origin server exceeds the **MaxFails** value, the address of the origin server is set to down and the expiration time is **FailTimeout**. The final value is the maximum value of **ConnectTimeout** and **FailTimeout**. Valid values: **1** to **3600**. Unit: seconds. Default value: **10**.
        self.fail_timeout = fail_timeout
        # The maximum number of failures. This parameter is related to health check. Valid values: **1** to **10**. Unit: seconds. Default value: **3**.
        self.max_fails = max_fails
        # The primary/secondary flag. Valid values:
        # 
        # *   **active**: primary
        # *   **backup**: secondary
        self.mode = mode
        # The timeout period for a read connection. Valid values: **10** to **300**. Unit: seconds. Default value: **120**.
        self.read_timeout = read_timeout
        # The timeout period for a write connection. Valid values: **10** to **300**. Unit: seconds. Default value: **120**.
        self.send_timeout = send_timeout
        # The weight of the origin server. This parameter takes effect only if the value of **ProxyMode** is **rr** or **ip_hash**.****
        # 
        # Valid values: **1** to **100**. Default value: **100**. A server with a higher weight receives more requests.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout

        if self.fail_timeout is not None:
            result['FailTimeout'] = self.fail_timeout

        if self.max_fails is not None:
            result['MaxFails'] = self.max_fails

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.read_timeout is not None:
            result['ReadTimeout'] = self.read_timeout

        if self.send_timeout is not None:
            result['SendTimeout'] = self.send_timeout

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')

        if m.get('FailTimeout') is not None:
            self.fail_timeout = m.get('FailTimeout')

        if m.get('MaxFails') is not None:
            self.max_fails = m.get('MaxFails')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ReadTimeout') is not None:
            self.read_timeout = m.get('ReadTimeout')

        if m.get('SendTimeout') is not None:
            self.send_timeout = m.get('SendTimeout')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

