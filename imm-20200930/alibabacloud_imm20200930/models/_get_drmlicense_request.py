# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDRMLicenseRequest(DaraModel):
    def __init__(
        self,
        key_id: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        project_name: str = None,
        protection_system: str = None,
    ):
        self.key_id = key_id
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.project_name = project_name
        self.protection_system = protection_system

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint

        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.protection_system is not None:
            result['ProtectionSystem'] = self.protection_system

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')

        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ProtectionSystem') is not None:
            self.protection_system = m.get('ProtectionSystem')

        return self

