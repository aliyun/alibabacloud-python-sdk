# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnServiceResponseBody(DaraModel):
    def __init__(
        self,
        changing_affect_time: str = None,
        changing_charge_type: str = None,
        instance_id: str = None,
        internet_charge_type: str = None,
        opening_time: str = None,
        operation_locks: main_models.DescribeDcdnServiceResponseBodyOperationLocks = None,
        request_id: str = None,
        websocket_changing_time: str = None,
        websocket_changing_type: str = None,
        websocket_type: str = None,
    ):
        # The time when the renewed secure DCDN takes effect. The time is displayed in UTC.
        self.changing_affect_time = changing_affect_time
        # The new metering method for the renewed secure DCDN. Valid values:
        # 
        # *   **PayByTraffic**: pay by data transfer
        # *   **PayByBandwidth**: pay by bandwidth
        # *   **PayByBandwidth95**: pay by 95th percentile bandwidth
        # *   **PayByBandwidth_monthavg**: pay by monthly average bandwidth
        # *   **PayByBandwidth_month4th**: pay by fourth peak bandwidth per month
        # *   **PayByBandwidth_monthday95avg**: pay by monthly average 95th percentile bandwidth
        # *   **PayByBandwidth_nighthalf95**: pay by 95th percentile bandwidth (50% off during nighttime)
        self.changing_charge_type = changing_charge_type
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
        # The time when the DCDN service was activated. The time follows the ISO 8601 standard.
        self.opening_time = opening_time
        # The lock status of DCDN.
        self.operation_locks = operation_locks
        # The request ID.
        self.request_id = request_id
        # The time when the changes of the WebSocket configuration take effect. The value is the same as that of the ChangingAffectTime parameter. This parameter can be displayed in the console only if the specified time is later than the current time.
        self.websocket_changing_time = websocket_changing_time
        # The next effective billing method of WebSocket. Valid values: **websockettraffic** and **websocketbps**. A value of websockettraffic indicates that you are billed based on the traffic volume. A value of websocketbps indicates that you are billed based on the bandwidth.
        self.websocket_changing_type = websocket_changing_type
        # The current billing method of WebSocket. Valid values: **websockettraffic** and **websocketbps**. A value of websockettraffic indicates that you are billed based on the traffic volume. A value of websocketbps indicates that you are billed based on the bandwidth.
        self.websocket_type = websocket_type

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

        if self.websocket_changing_time is not None:
            result['WebsocketChangingTime'] = self.websocket_changing_time

        if self.websocket_changing_type is not None:
            result['WebsocketChangingType'] = self.websocket_changing_type

        if self.websocket_type is not None:
            result['WebsocketType'] = self.websocket_type

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
            temp_model = main_models.DescribeDcdnServiceResponseBodyOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WebsocketChangingTime') is not None:
            self.websocket_changing_time = m.get('WebsocketChangingTime')

        if m.get('WebsocketChangingType') is not None:
            self.websocket_changing_type = m.get('WebsocketChangingType')

        if m.get('WebsocketType') is not None:
            self.websocket_type = m.get('WebsocketType')

        return self

class DescribeDcdnServiceResponseBodyOperationLocks(DaraModel):
    def __init__(
        self,
        lock_reason: List[main_models.DescribeDcdnServiceResponseBodyOperationLocksLockReason] = None,
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
                temp_model = main_models.DescribeDcdnServiceResponseBodyOperationLocksLockReason()
                self.lock_reason.append(temp_model.from_map(k1))

        return self

class DescribeDcdnServiceResponseBodyOperationLocksLockReason(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        # The reason why secure DCDN was locked. For example, a value of financial indicates that an overdue payment exists.
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

