# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ABTestExperiment(DaraModel):
    def __init__(
        self,
        name: str = None,
        online: bool = None,
        params: Dict[str, str] = None,
        serial_number: int = None,
        traffic: int = None,
    ):
        self.name = name
        self.online = online
        self.params = params
        self.serial_number = serial_number
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.online is not None:
            result['online'] = self.online

        if self.params is not None:
            result['params'] = self.params

        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number

        if self.traffic is not None:
            result['traffic'] = self.traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('online') is not None:
            self.online = m.get('online')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')

        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')

        return self

