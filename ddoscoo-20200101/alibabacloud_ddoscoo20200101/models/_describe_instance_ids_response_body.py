# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceIdsResponseBody(DaraModel):
    def __init__(
        self,
        instance_ids: List[main_models.DescribeInstanceIdsResponseBodyInstanceIds] = None,
        request_id: str = None,
    ):
        # The ID, type, description, and IP version of the instance.
        self.instance_ids = instance_ids
        self.request_id = request_id

    def validate(self):
        if self.instance_ids:
            for v1 in self.instance_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceIds'] = []
        if self.instance_ids is not None:
            for k1 in self.instance_ids:
                result['InstanceIds'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_ids = []
        if m.get('InstanceIds') is not None:
            for k1 in m.get('InstanceIds'):
                temp_model = main_models.DescribeInstanceIdsResponseBodyInstanceIds()
                self.instance_ids.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceIdsResponseBodyInstanceIds(DaraModel):
    def __init__(
        self,
        edition: int = None,
        instance_id: str = None,
        ip_mode: str = None,
        ip_version: str = None,
        remark: str = None,
    ):
        # The type of the instance. Valid values:
        # 
        # *   **0**: Anti-DDoS Proxy (Outside Chinese Mainland) instance of the Insurance mitigation plan
        # *   **1**: Anti-DDoS Proxy (Outside Chinese Mainland) instance of the Unlimited mitigation plan
        # *   **2**: Anti-DDoS Proxy (Outside Chinese Mainland) instance of the CMA mitigation plan
        # *   **3**: Anti-DDoS Proxy (Outside Chinese Mainland) instance of the Sec-CMA mitigation plan
        # *   **9**: Anti-DDoS Proxy (Chinese Mainland) instance of the Profession mitigation plan
        self.edition = edition
        # The ID of the instance.
        self.instance_id = instance_id
        # The IP address-based forwarding mode of the instance. Valid values:
        # 
        # *   **fnat**: Requests from IPv4 addresses are forwarded to origin servers that use IPv4 addresses and requests from IPv6 addresses are forwarded to origin servers that use IPv6 addresses.
        # *   **v6tov4**: All requests are forwarded to origin servers that use IPv4 addresses.
        self.ip_mode = ip_mode
        # The IP version of the instance. Valid values:
        # 
        # *   **Ipv4**
        # *   **Ipv6**
        self.ip_version = ip_version
        # The description of the instance.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edition is not None:
            result['Edition'] = self.edition

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_mode is not None:
            result['IpMode'] = self.ip_mode

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpMode') is not None:
            self.ip_mode = m.get('IpMode')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

