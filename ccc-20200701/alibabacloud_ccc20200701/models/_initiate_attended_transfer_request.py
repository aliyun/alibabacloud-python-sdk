# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitiateAttendedTransferRequest(DaraModel):
    def __init__(
        self,
        call_priority: int = None,
        device_id: str = None,
        instance_id: str = None,
        job_id: str = None,
        queuing_overflow_threshold: int = None,
        queuing_timeout_seconds: int = None,
        routing_type: str = None,
        strategy_name: str = None,
        strategy_params: str = None,
        tags: str = None,
        timeout_seconds: int = None,
        transferee: str = None,
        transferee_type: str = None,
        transferor: str = None,
        user_id: str = None,
    ):
        self.call_priority = call_priority
        self.device_id = device_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.job_id = job_id
        self.queuing_overflow_threshold = queuing_overflow_threshold
        self.queuing_timeout_seconds = queuing_timeout_seconds
        self.routing_type = routing_type
        self.strategy_name = strategy_name
        self.strategy_params = strategy_params
        self.tags = tags
        self.timeout_seconds = timeout_seconds
        # This parameter is required.
        self.transferee = transferee
        self.transferee_type = transferee_type
        self.transferor = transferor
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_priority is not None:
            result['CallPriority'] = self.call_priority

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.queuing_overflow_threshold is not None:
            result['QueuingOverflowThreshold'] = self.queuing_overflow_threshold

        if self.queuing_timeout_seconds is not None:
            result['QueuingTimeoutSeconds'] = self.queuing_timeout_seconds

        if self.routing_type is not None:
            result['RoutingType'] = self.routing_type

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.strategy_params is not None:
            result['StrategyParams'] = self.strategy_params

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        if self.transferee is not None:
            result['Transferee'] = self.transferee

        if self.transferee_type is not None:
            result['TransfereeType'] = self.transferee_type

        if self.transferor is not None:
            result['Transferor'] = self.transferor

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallPriority') is not None:
            self.call_priority = m.get('CallPriority')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('QueuingOverflowThreshold') is not None:
            self.queuing_overflow_threshold = m.get('QueuingOverflowThreshold')

        if m.get('QueuingTimeoutSeconds') is not None:
            self.queuing_timeout_seconds = m.get('QueuingTimeoutSeconds')

        if m.get('RoutingType') is not None:
            self.routing_type = m.get('RoutingType')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('StrategyParams') is not None:
            self.strategy_params = m.get('StrategyParams')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        if m.get('Transferee') is not None:
            self.transferee = m.get('Transferee')

        if m.get('TransfereeType') is not None:
            self.transferee_type = m.get('TransfereeType')

        if m.get('Transferor') is not None:
            self.transferor = m.get('Transferor')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

