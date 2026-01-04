# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details about the instances.
        self.instances = instances
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of the instances.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        debt_status: int = None,
        edition: int = None,
        enabled: int = None,
        expire_time: int = None,
        instance_id: str = None,
        ip: str = None,
        ip_mode: str = None,
        ip_version: str = None,
        is_first_open_bw: int = None,
        is_first_open_qps: int = None,
        remark: str = None,
        status: int = None,
    ):
        # The time when the instance was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The overdue status of the instance. The value is fixed as **0**, which indicates that your Alibaba Cloud account does not have overdue payments. The instance supports only the subscription billing method.
        self.debt_status = debt_status
        # The mitigation plan of the instance. Valid values:
        # 
        # *   **0**: Anti-DDoS Proxy (Outside Chinese Mainland) instance of the Insurance mitigation plan
        # *   **1**: Anti-DDoS Proxy (Outside Chinese Mainland) instance of the Unlimited mitigation plan
        # *   **2**: Anti-DDoS Proxy (Outside Chinese Mainland) instance of the Chinese Mainland Acceleration (CMA) mitigation plan
        # *   **9**: Anti-DDoS Proxy (Chinese Mainland) instance of the Profession mitigation plan
        self.edition = edition
        # The traffic forwarding status of the instance. Valid values:
        # 
        # *   **0**: The instance no longer forwards service traffic.
        # *   **1**: The instance forwards service traffic as expected.
        self.enabled = enabled
        # The time when the instance expires. The value is a UNIX timestamp. Unit: milliseconds.
        self.expire_time = expire_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The IP address of the instance.
        self.ip = ip
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
        # Indicates whether the metering method of the 95th percentile burstable clean bandwidth is enabled for the instance. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.is_first_open_bw = is_first_open_bw
        # Indicates whether the metering method of the 95th percentile burstable QPS is enabled for the instance. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.is_first_open_qps = is_first_open_qps
        # The remarks of the instance.
        self.remark = remark
        # The status of the instance. Valid values:
        # 
        # *   **1**: normal
        # *   **2**: expired
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.debt_status is not None:
            result['DebtStatus'] = self.debt_status

        if self.edition is not None:
            result['Edition'] = self.edition

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ip_mode is not None:
            result['IpMode'] = self.ip_mode

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.is_first_open_bw is not None:
            result['IsFirstOpenBw'] = self.is_first_open_bw

        if self.is_first_open_qps is not None:
            result['IsFirstOpenQps'] = self.is_first_open_qps

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DebtStatus') is not None:
            self.debt_status = m.get('DebtStatus')

        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IpMode') is not None:
            self.ip_mode = m.get('IpMode')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IsFirstOpenBw') is not None:
            self.is_first_open_bw = m.get('IsFirstOpenBw')

        if m.get('IsFirstOpenQps') is not None:
            self.is_first_open_qps = m.get('IsFirstOpenQps')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

