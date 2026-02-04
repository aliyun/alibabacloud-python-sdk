# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnIpaServiceResponseBody(DaraModel):
    def __init__(
        self,
        changing_affect_time: str = None,
        changing_charge_type: str = None,
        instance_id: str = None,
        internet_charge_type: str = None,
        opening_time: str = None,
        operation_locks: main_models.DescribeDcdnIpaServiceResponseBodyOperationLocks = None,
        request_id: str = None,
    ):
        # The time when the change of the billing method starts to take effect. The time is in GMT. This time appears on the frontend only when it is later than the current time.
        self.changing_affect_time = changing_affect_time
        # The new billing method to take effect. Valid values:
        # 
        # *   **PayByTraffic**: pay-by-data-transfer
        # *   **PayByBandwidth**: pay-by-bandwidth
        # *   **PayByBandwidth95**: pay-by-95th percentile bandwidth
        # *   **PayByBandwidth_monthavg**: pay-by-monthly average bandwidth
        # *   **PayByBandwidth_month4th**: pay-by-fourth peak bandwidth per month
        # *   **PayByBandwidth_monthday95avg**: pay-by-monthly average 95th percentile bandwidth
        # *   **PayByBandwidth_nighthalf95**: pay-by-95th percentile bandwidth (50% off during nighttime)
        self.changing_charge_type = changing_charge_type
        # The ID of the instance.
        self.instance_id = instance_id
        # The billing method of the instance. Valid values:
        # 
        # *   **PayByTraffic**: pay-by-data-transfer
        # *   **PayByBandwidth**: pay-by-bandwidth
        # *   **PayByBandwidth95**: pay-by-95th percentile bandwidth
        # *   **PayByBandwidth_monthavg**: pay-by-monthly average bandwidth
        # *   **PayByBandwidth_month4th**: pay-by-fourth peak bandwidth per month
        # *   **PayByBandwidth_monthday95avg**: pay-by-monthly average 95th percentile bandwidth
        # *   **PayByBandwidth_nighthalf95**: pay-by-95th percentile bandwidth (50% off during nighttime)
        self.internet_charge_type = internet_charge_type
        # The time when the DCDN service was activated. The time follows the ISO 8601 standard.
        self.opening_time = opening_time
        # The lock status of secure DCDN.
        self.operation_locks = operation_locks
        # The ID of the request.
        self.request_id = request_id

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.opening_time is not None:
            result['OpeningTime'] = self.opening_time

        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangingAffectTime') is not None:
            self.changing_affect_time = m.get('ChangingAffectTime')

        if m.get('ChangingChargeType') is not None:
            self.changing_charge_type = m.get('ChangingChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('OpeningTime') is not None:
            self.opening_time = m.get('OpeningTime')

        if m.get('OperationLocks') is not None:
            temp_model = main_models.DescribeDcdnIpaServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnIpaServiceResponseBodyOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: List[main_models.DescribeDcdnIpaServiceResponseBodyOperationLocksLockReason] = None,
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
                temp_model = main_models.DescribeDcdnIpaServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k1))

        return self

class DescribeDcdnIpaServiceResponseBodyOperationLocksLockReason(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        # The reason why the instance is locked. For example, a value of **financial** indicates that an overdue payment exists.
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

