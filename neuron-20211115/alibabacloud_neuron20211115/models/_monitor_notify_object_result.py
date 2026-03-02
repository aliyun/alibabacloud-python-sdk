# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorNotifyObjectResult(DaraModel):
    def __init__(
        self,
        contact_groups: List[main_models.MonitorContactGroup] = None,
        contacts: List[main_models.MonitorContact] = None,
        request_id: str = None,
        webhooks: List[main_models.MonitorWebhook] = None,
    ):
        self.contact_groups = contact_groups
        self.contacts = contacts
        self.request_id = request_id
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

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.webhooks = []
        if m.get('webhooks') is not None:
            for k1 in m.get('webhooks'):
                temp_model = main_models.MonitorWebhook()
                self.webhooks.append(temp_model.from_map(k1))

        return self

