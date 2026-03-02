# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorNotifyAlert(DaraModel):
    def __init__(
        self,
        contact_groups: List[main_models.MonitorContactGroup] = None,
        contacts: List[main_models.MonitorContact] = None,
        end_time: str = None,
        id: int = None,
        name: str = None,
        notify_channels: List[str] = None,
        rule_names: List[str] = None,
        start_time: str = None,
        type: str = None,
        webhooks: List[main_models.MonitorWebhook] = None,
    ):
        self.contact_groups = contact_groups
        self.contacts = contacts
        self.end_time = end_time
        self.id = id
        self.name = name
        self.notify_channels = notify_channels
        self.rule_names = rule_names
        self.start_time = start_time
        # This parameter is required.
        self.type = type
        self.webhooks = webhooks

    def validate(self):
        if self.contact_groups:
            for v1 in self.contact_groups:
                 if v1:
                    v1.validate()
        if self.contacts:
            for v1 in self.contacts:
                 if v1:
                    v1.validate()
        if self.webhooks:
            for v1 in self.webhooks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['contactGroups'] = []
        if self.contact_groups is not None:
            for k1 in self.contact_groups:
                result['contactGroups'].append(k1.to_map() if k1 else None)

        result['contacts'] = []
        if self.contacts is not None:
            for k1 in self.contacts:
                result['contacts'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.notify_channels is not None:
            result['notifyChannels'] = self.notify_channels

        if self.rule_names is not None:
            result['ruleNames'] = self.rule_names

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.type is not None:
            result['type'] = self.type

        result['webhooks'] = []
        if self.webhooks is not None:
            for k1 in self.webhooks:
                result['webhooks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_groups = []
        if m.get('contactGroups') is not None:
            for k1 in m.get('contactGroups'):
                temp_model = main_models.MonitorContactGroup()
                self.contact_groups.append(temp_model.from_map(k1))

        self.contacts = []
        if m.get('contacts') is not None:
            for k1 in m.get('contacts'):
                temp_model = main_models.MonitorContact()
                self.contacts.append(temp_model.from_map(k1))

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('notifyChannels') is not None:
            self.notify_channels = m.get('notifyChannels')

        if m.get('ruleNames') is not None:
            self.rule_names = m.get('ruleNames')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('type') is not None:
            self.type = m.get('type')

        self.webhooks = []
        if m.get('webhooks') is not None:
            for k1 in m.get('webhooks'):
                temp_model = main_models.MonitorWebhook()
                self.webhooks.append(temp_model.from_map(k1))

        return self

