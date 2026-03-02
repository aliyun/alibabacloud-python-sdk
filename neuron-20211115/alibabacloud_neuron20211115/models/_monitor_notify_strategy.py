# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorNotifyStrategy(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
        contact_group_ids: List[int] = None,
        contact_groups: List[main_models.MonitorContactGroup] = None,
        contact_ids: List[int] = None,
        contacts: List[main_models.MonitorContact] = None,
        end_time: str = None,
        id: int = None,
        name: str = None,
        request_id: str = None,
        start_time: str = None,
        webhook_ids: List[int] = None,
        webhooks: List[main_models.MonitorWebhook] = None,
    ):
        self.channels = channels
        self.contact_group_ids = contact_group_ids
        self.contact_groups = contact_groups
        self.contact_ids = contact_ids
        self.contacts = contacts
        self.end_time = end_time
        self.id = id
        self.name = name
        self.request_id = request_id
        self.start_time = start_time
        self.webhook_ids = webhook_ids
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
        if self.channels is not None:
            result['channels'] = self.channels

        if self.contact_group_ids is not None:
            result['contactGroupIds'] = self.contact_group_ids

        result['contactGroups'] = []
        if self.contact_groups is not None:
            for k1 in self.contact_groups:
                result['contactGroups'].append(k1.to_map() if k1 else None)

        if self.contact_ids is not None:
            result['contactIds'] = self.contact_ids

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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.webhook_ids is not None:
            result['webhookIds'] = self.webhook_ids

        result['webhooks'] = []
        if self.webhooks is not None:
            for k1 in self.webhooks:
                result['webhooks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channels') is not None:
            self.channels = m.get('channels')

        if m.get('contactGroupIds') is not None:
            self.contact_group_ids = m.get('contactGroupIds')

        self.contact_groups = []
        if m.get('contactGroups') is not None:
            for k1 in m.get('contactGroups'):
                temp_model = main_models.MonitorContactGroup()
                self.contact_groups.append(temp_model.from_map(k1))

        if m.get('contactIds') is not None:
            self.contact_ids = m.get('contactIds')

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

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('webhookIds') is not None:
            self.webhook_ids = m.get('webhookIds')

        self.webhooks = []
        if m.get('webhooks') is not None:
            for k1 in m.get('webhooks'):
                temp_model = main_models.MonitorWebhook()
                self.webhooks.append(temp_model.from_map(k1))

        return self

