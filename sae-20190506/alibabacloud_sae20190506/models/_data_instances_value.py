# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DataInstancesValue(DaraModel):
    def __init__(
        self,
        dns_name: str = None,
        listeners: Dict[str, main_models.DataInstancesValueListenersValue] = None,
        created_by_sae: bool = None,
    ):
        # The domain name.
        self.dns_name = dns_name
        # The listeners.
        self.listeners = listeners
        # Indicates whether the instance is created by SAE.
        # 
        # *   **true**: The instance is created by SAE.
        # *   **false**: The existing instance is reused.
        self.created_by_sae = created_by_sae

    def validate(self):
        if self.listeners:
            for v1 in self.listeners.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name

        result['Listeners'] = {}
        if self.listeners is not None:
            for k1, v1 in self.listeners.items():
                result['Listeners'][k1] = v1.to_map() if v1 else None

        if self.created_by_sae is not None:
            result['CreatedBySae'] = self.created_by_sae

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')

        self.listeners = {}
        if m.get('Listeners') is not None:
            for k1, v1 in m.get('Listeners').items():
                temp_model = main_models.DataInstancesValueListenersValue()
                self.listeners[k1] = temp_model.from_map(v1)

        if m.get('CreatedBySae') is not None:
            self.created_by_sae = m.get('CreatedBySae')

        return self

