# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListInstancesTrafficPackagesResponseBody(DaraModel):
    def __init__(
        self,
        instance_traffic_package_usages: List[main_models.ListInstancesTrafficPackagesResponseBodyInstanceTrafficPackageUsages] = None,
        request_id: str = None,
    ):
        # The data transfers that exceed the quota of the data transfer plan in the current month. Unit: bytes.
        self.instance_traffic_package_usages = instance_traffic_package_usages
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_traffic_package_usages:
            for v1 in self.instance_traffic_package_usages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceTrafficPackageUsages'] = []
        if self.instance_traffic_package_usages is not None:
            for k1 in self.instance_traffic_package_usages:
                result['InstanceTrafficPackageUsages'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_traffic_package_usages = []
        if m.get('InstanceTrafficPackageUsages') is not None:
            for k1 in m.get('InstanceTrafficPackageUsages'):
                temp_model = main_models.ListInstancesTrafficPackagesResponseBodyInstanceTrafficPackageUsages()
                self.instance_traffic_package_usages.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstancesTrafficPackagesResponseBodyInstanceTrafficPackageUsages(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        traffic_overflow: int = None,
        traffic_package_remaining: int = None,
        traffic_package_total: int = None,
        traffic_used: int = None,
    ):
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The data transfers that exceeds the quota of the data transfer plan in the current month. Unit: Byte.
        self.traffic_overflow = traffic_overflow
        # The unused quota of the data transfer plan in the current month. Unit: Byte.
        self.traffic_package_remaining = traffic_package_remaining
        # The quota of the data transfer plan in the current month. Unit: Byte.
        # 
        # > TrafficPackageTotal = TrafficUsed + TrafficPackageRemaining
        self.traffic_package_total = traffic_package_total
        # The used quota of the data transfer plan in the current month. Unit: Byte.
        self.traffic_used = traffic_used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.traffic_overflow is not None:
            result['TrafficOverflow'] = self.traffic_overflow

        if self.traffic_package_remaining is not None:
            result['TrafficPackageRemaining'] = self.traffic_package_remaining

        if self.traffic_package_total is not None:
            result['TrafficPackageTotal'] = self.traffic_package_total

        if self.traffic_used is not None:
            result['TrafficUsed'] = self.traffic_used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TrafficOverflow') is not None:
            self.traffic_overflow = m.get('TrafficOverflow')

        if m.get('TrafficPackageRemaining') is not None:
            self.traffic_package_remaining = m.get('TrafficPackageRemaining')

        if m.get('TrafficPackageTotal') is not None:
            self.traffic_package_total = m.get('TrafficPackageTotal')

        if m.get('TrafficUsed') is not None:
            self.traffic_used = m.get('TrafficUsed')

        return self

