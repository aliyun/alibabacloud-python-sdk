# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartBack2BackCallRequest(DaraModel):
    def __init__(
        self,
        additional_broker: str = None,
        broker: str = None,
        callee: str = None,
        caller: str = None,
        instance_id: str = None,
        tags: str = None,
        timeout_seconds: int = None,
    ):
        # Additional intermediate number. If this parameter is provided, the intermediate number specified by the Broker parameter is used to call the caller, and the number specified by this parameter is used to call the callee. This parameter is optional and defaults to empty.
        self.additional_broker = additional_broker
        # The intermediate number, which must be an active outbound number under the instance. This number is used to sequentially call the caller and the callee in a double-call scenario.
        # 
        # This parameter is required.
        self.broker = broker
        # The callee number.
        # 
        # This parameter is required.
        self.callee = callee
        # Caller number.
        # 
        # This parameter is required.
        self.caller = caller
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Ingest endpoint data. It must not exceed 128 bytes and is primarily used for extension purposes. Ordinary customers do not need to concern themselves with it.
        self.tags = tags
        # The timeout for the dual-call, in seconds. If the call is not answered within the specified time, it will be automatically disconnected. This parameter is optional and defaults to 30 seconds.
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_broker is not None:
            result['AdditionalBroker'] = self.additional_broker

        if self.broker is not None:
            result['Broker'] = self.broker

        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalBroker') is not None:
            self.additional_broker = m.get('AdditionalBroker')

        if m.get('Broker') is not None:
            self.broker = m.get('Broker')

        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

