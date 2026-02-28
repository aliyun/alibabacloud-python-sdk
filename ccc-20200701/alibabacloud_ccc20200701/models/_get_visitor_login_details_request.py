# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVisitorLoginDetailsRequest(DaraModel):
    def __init__(
        self,
        chat_device_id: str = None,
        instance_id: str = None,
        token: str = None,
        visitor_id: str = None,
    ):
        # This parameter is required.
        self.chat_device_id = chat_device_id
        self.instance_id = instance_id
        self.token = token
        # This parameter is required.
        self.visitor_id = visitor_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_device_id is not None:
            result['ChatDeviceId'] = self.chat_device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.token is not None:
            result['Token'] = self.token

        if self.visitor_id is not None:
            result['VisitorId'] = self.visitor_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatDeviceId') is not None:
            self.chat_device_id = m.get('ChatDeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VisitorId') is not None:
            self.visitor_id = m.get('VisitorId')

        return self

