# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeIpStatusResponseBody(DaraModel):
    def __init__(
        self,
        ip_status: List[main_models.DescribeIpStatusResponseBodyIpStatus] = None,
        request_id: str = None,
    ):
        # The status of the IP addresses of the POPs.
        self.ip_status = ip_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ip_status:
            for v1 in self.ip_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpStatus'] = []
        if self.ip_status is not None:
            for k1 in self.ip_status:
                result['IpStatus'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_status = []
        if m.get('IpStatus') is not None:
            for k1 in m.get('IpStatus'):
                temp_model = main_models.DescribeIpStatusResponseBodyIpStatus()
                self.ip_status.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeIpStatusResponseBodyIpStatus(DaraModel):
    def __init__(
        self,
        ip: str = None,
        status: str = None,
    ):
        # The IP address of the POP.
        self.ip = ip
        # The status.
        # 
        # *   **nonali**: not an Alibaba Cloud CDN POP
        # *   **normal**: an available Alibaba Cloud CDN POP
        # *   **abnormal**: an unavailable Alibaba Cloud CDN POP
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['ip'] = self.ip

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

