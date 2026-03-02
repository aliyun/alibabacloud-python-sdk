# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorContactGroup(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        contacts: List[main_models.MonitorContact] = None,
        enterprise_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
    ):
        self.account_id = account_id
        self.contacts = contacts
        # This parameter is required.
        self.enterprise_id = enterprise_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.contacts:
            for v1 in self.contacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        result['contacts'] = []
        if self.contacts is not None:
            for k1 in self.contacts:
                result['contacts'].append(k1.to_map() if k1 else None)

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        self.contacts = []
        if m.get('contacts') is not None:
            for k1 in m.get('contacts'):
                temp_model = main_models.MonitorContact()
                self.contacts.append(temp_model.from_map(k1))

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

