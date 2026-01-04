# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeL7UsKeepaliveResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rs_keepalive: main_models.DescribeL7UsKeepaliveResponseBodyRsKeepalive = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The value of the Back-to-origin Persistent Connections parameter.
        self.rs_keepalive = rs_keepalive

    def validate(self):
        if self.rs_keepalive:
            self.rs_keepalive.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rs_keepalive is not None:
            result['RsKeepalive'] = self.rs_keepalive.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RsKeepalive') is not None:
            temp_model = main_models.DescribeL7UsKeepaliveResponseBodyRsKeepalive()
            self.rs_keepalive = temp_model.from_map(m.get('RsKeepalive'))

        return self

class DescribeL7UsKeepaliveResponseBodyRsKeepalive(DaraModel):
    def __init__(
        self,
        ds_keepalive_timeout: int = None,
        enabled: bool = None,
        keepalive_requests: int = None,
        keepalive_timeout: int = None,
    ):
        self.ds_keepalive_timeout = ds_keepalive_timeout
        # Indicates whether Back-to-origin Persistent Connections is turned on. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enabled = enabled
        # The number of requests that reuse persistent connections.
        self.keepalive_requests = keepalive_requests
        # The timeout period of idle persistent connections.
        self.keepalive_timeout = keepalive_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds_keepalive_timeout is not None:
            result['DsKeepaliveTimeout'] = self.ds_keepalive_timeout

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.keepalive_requests is not None:
            result['KeepaliveRequests'] = self.keepalive_requests

        if self.keepalive_timeout is not None:
            result['KeepaliveTimeout'] = self.keepalive_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DsKeepaliveTimeout') is not None:
            self.ds_keepalive_timeout = m.get('DsKeepaliveTimeout')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('KeepaliveRequests') is not None:
            self.keepalive_requests = m.get('KeepaliveRequests')

        if m.get('KeepaliveTimeout') is not None:
            self.keepalive_timeout = m.get('KeepaliveTimeout')

        return self

