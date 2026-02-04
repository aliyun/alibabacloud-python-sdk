# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnsecServiceResponseBody(DaraModel):
    def __init__(
        self,
        changing_affect_time: str = None,
        changing_charge_type: str = None,
        domain_num: str = None,
        end_time: str = None,
        flow_type: str = None,
        instance_id: str = None,
        internet_charge_type: str = None,
        operation_locks: main_models.DescribeDcdnsecServiceResponseBodyOperationLocks = None,
        request_id: str = None,
        request_type: str = None,
        start_time: str = None,
        version: str = None,
    ):
        # The time when the renewed service takes effect. The time is displayed in UTC.
        self.changing_affect_time = changing_affect_time
        # The new metering method for the renewed DCDN. Valid values:
        # 
        # *   **PayByTraffic**: pay by data transfer
        # *   **PayByBandwidth**: pay by bandwidth
        # *   **PayByBandwidth95**: pay by 95th percentile bandwidth
        # *   **PayByBandwidth_monthavg**: pay by monthly average bandwidth
        # *   **PayByBandwidth_month4th**: pay by fourth peak bandwidth per month
        # *   **PayByBandwidth_monthday95avg**: pay by monthly average 95th percentile bandwidth
        # *   **PayByBandwidth_nighthalf95**: pay by 95th percentile bandwidth (50% off during nighttime)
        self.changing_charge_type = changing_charge_type
        # The number of accelerated domain names that use DCDN.
        self.domain_num = domain_num
        # The service expiration time.
        self.end_time = end_time
        # The metering method for traffic.
        self.flow_type = flow_type
        # The ID of the instance.
        self.instance_id = instance_id
        # The current metering method. Valid values:
        # 
        # *   **PayByTraffic**: pay by data transfer
        # *   **PayByBandwidth**: pay by bandwidth
        # *   **PayByBandwidth95**: pay by 95th percentile bandwidth
        # *   **PayByBandwidth_monthavg**: pay by monthly average bandwidth
        # *   **PayByBandwidth_month4th**: pay by fourth peak bandwidth per month
        # *   **PayByBandwidth_monthday95avg**: pay by monthly average 95th percentile bandwidth
        # *   **PayByBandwidth_nighthalf95**: pay by 95th percentile bandwidth (50% off during nighttime)
        self.internet_charge_type = internet_charge_type
        # The lock status of DCDN.
        self.operation_locks = operation_locks
        # The ID of the request.
        self.request_id = request_id
        # The metering method for requests.
        self.request_type = request_type
        # The service activation time.
        self.start_time = start_time
        # The version number.
        self.version = version

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changing_affect_time is not None:
            result['ChangingAffectTime'] = self.changing_affect_time

        if self.changing_charge_type is not None:
            result['ChangingChargeType'] = self.changing_charge_type

        if self.domain_num is not None:
            result['DomainNum'] = self.domain_num

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.flow_type is not None:
            result['FlowType'] = self.flow_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_type is not None:
            result['RequestType'] = self.request_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')

        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')

        if m.get('DomainNum') is not None:
            self.domain_num = m.get('DomainNum')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('OperationLocks') is not None:
            temp_model = main_models.DescribeDcdnsecServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestType') is not None:
            self.request_type = m.get('RequestType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeDcdnsecServiceResponseBodyOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: List[main_models.DescribeDcdnsecServiceResponseBodyOperationLocksLockReason] = None,
    ):
        self.lock_reason = lock_reason

    def validate(self):
        if self.lock_reason:
            for v1 in self.lock_reason:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LockReason'] = []
        if self.lock_reason is not None:
            for k1 in self.lock_reason:
                result['LockReason'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lock_reason = []
        if m.get('LockReason') is not None:
            for k1 in m.get('LockReason'):
                temp_model = main_models.DescribeDcdnsecServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k1))

        return self

class DescribeDcdnsecServiceResponseBodyOperationLocksLockReason(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        # The reason why the instance was locked.
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        return self

