# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRequestMessageEvent(DaraModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
        data_type: str = None,
        sync: bool = None,
        data: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters
        self.data_type = data_type
        self.sync = sync
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service is not None:
            result['Service'] = self.service

        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.sync is not None:
            result['Sync'] = self.sync

        if self.data is not None:
            result['Data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Sync') is not None:
            self.sync = m.get('Sync')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        return self

