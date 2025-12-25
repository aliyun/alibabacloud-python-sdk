# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class Backend(DaraModel):
    def __init__(
        self,
        scene: str = None,
        services: List[main_models.BackendServices] = None,
    ):
        self.scene = scene
        self.services = services

    def validate(self):
        if self.services:
            for v1 in self.services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene is not None:
            result['scene'] = self.scene

        result['services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['services'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')

        self.services = []
        if m.get('services') is not None:
            for k1 in m.get('services'):
                temp_model = main_models.BackendServices()
                self.services.append(temp_model.from_map(k1))

        return self

class BackendServices(DaraModel):
    def __init__(
        self,
        name: str = None,
        port: int = None,
        protocol: str = None,
        service_id: str = None,
        version: str = None,
        weight: int = None,
    ):
        self.name = name
        self.port = port
        self.protocol = protocol
        self.service_id = service_id
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.version is not None:
            result['version'] = self.version

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

