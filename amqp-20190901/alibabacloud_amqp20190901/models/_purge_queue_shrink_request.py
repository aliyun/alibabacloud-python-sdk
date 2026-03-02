# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PurgeQueueShrinkRequest(DaraModel):
    def __init__(
        self,
        collina: str = None,
        console_session_id: str = None,
        instance_id: str = None,
        queue_name: str = None,
        queue_names_shrink: str = None,
        umid_token: str = None,
        vhost_name: str = None,
    ):
        self.collina = collina
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.queue_names_shrink = queue_names_shrink
        self.umid_token = umid_token
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collina is not None:
            result['Collina'] = self.collina

        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.queue_names_shrink is not None:
            result['QueueNames'] = self.queue_names_shrink

        if self.umid_token is not None:
            result['UmidToken'] = self.umid_token

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collina') is not None:
            self.collina = m.get('Collina')

        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('QueueNames') is not None:
            self.queue_names_shrink = m.get('QueueNames')

        if m.get('UmidToken') is not None:
            self.umid_token = m.get('UmidToken')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self

