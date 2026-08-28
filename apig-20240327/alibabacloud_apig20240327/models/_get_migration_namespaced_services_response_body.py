# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetMigrationNamespacedServicesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetMigrationNamespacedServicesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetMigrationNamespacedServicesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetMigrationNamespacedServicesResponseBodyData(DaraModel):
    def __init__(
        self,
        namespaced_services: List[main_models.GetMigrationNamespacedServicesResponseBodyDataNamespacedServices] = None,
    ):
        self.namespaced_services = namespaced_services

    def validate(self):
        if self.namespaced_services:
            for v1 in self.namespaced_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['namespacedServices'] = []
        if self.namespaced_services is not None:
            for k1 in self.namespaced_services:
                result['namespacedServices'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.namespaced_services = []
        if m.get('namespacedServices') is not None:
            for k1 in m.get('namespacedServices'):
                temp_model = main_models.GetMigrationNamespacedServicesResponseBodyDataNamespacedServices()
                self.namespaced_services.append(temp_model.from_map(k1))

        return self

class GetMigrationNamespacedServicesResponseBodyDataNamespacedServices(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        services: List[main_models.GetMigrationNamespacedServicesResponseBodyDataNamespacedServicesServices] = None,
    ):
        self.namespace = namespace
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
        if self.namespace is not None:
            result['namespace'] = self.namespace

        result['services'] = []
        if self.services is not None:
            for k1 in self.services:
                result['services'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        self.services = []
        if m.get('services') is not None:
            for k1 in m.get('services'):
                temp_model = main_models.GetMigrationNamespacedServicesResponseBodyDataNamespacedServicesServices()
                self.services.append(temp_model.from_map(k1))

        return self

class GetMigrationNamespacedServicesResponseBodyDataNamespacedServicesServices(DaraModel):
    def __init__(
        self,
        name: str = None,
        slb_id: str = None,
    ):
        self.name = name
        self.slb_id = slb_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.slb_id is not None:
            result['slbId'] = self.slb_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('slbId') is not None:
            self.slb_id = m.get('slbId')

        return self

