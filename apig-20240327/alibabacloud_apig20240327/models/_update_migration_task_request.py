# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateMigrationTaskRequest(DaraModel):
    def __init__(
        self,
        cluster_namespace: str = None,
        description: str = None,
        service_name: str = None,
        slb_id: str = None,
        switch_type: str = None,
        target: str = None,
        virtual_services: List[main_models.UpdateMigrationTaskRequestVirtualServices] = None,
        weight: int = None,
    ):
        self.cluster_namespace = cluster_namespace
        self.description = description
        self.service_name = service_name
        self.slb_id = slb_id
        self.switch_type = switch_type
        self.target = target
        self.virtual_services = virtual_services
        self.weight = weight

    def validate(self):
        if self.virtual_services:
            for v1 in self.virtual_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_namespace is not None:
            result['clusterNamespace'] = self.cluster_namespace

        if self.description is not None:
            result['description'] = self.description

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.slb_id is not None:
            result['slbId'] = self.slb_id

        if self.switch_type is not None:
            result['switchType'] = self.switch_type

        if self.target is not None:
            result['target'] = self.target

        result['virtualServices'] = []
        if self.virtual_services is not None:
            for k1 in self.virtual_services:
                result['virtualServices'].append(k1.to_map() if k1 else None)

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterNamespace') is not None:
            self.cluster_namespace = m.get('clusterNamespace')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('slbId') is not None:
            self.slb_id = m.get('slbId')

        if m.get('switchType') is not None:
            self.switch_type = m.get('switchType')

        if m.get('target') is not None:
            self.target = m.get('target')

        self.virtual_services = []
        if m.get('virtualServices') is not None:
            for k1 in m.get('virtualServices'):
                temp_model = main_models.UpdateMigrationTaskRequestVirtualServices()
                self.virtual_services.append(temp_model.from_map(k1))

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class UpdateMigrationTaskRequestVirtualServices(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
        virtual_service_group_id: str = None,
        virtual_service_group_name: str = None,
    ):
        self.port = port
        self.protocol = protocol
        self.virtual_service_group_id = virtual_service_group_id
        self.virtual_service_group_name = virtual_service_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.virtual_service_group_id is not None:
            result['virtualServiceGroupId'] = self.virtual_service_group_id

        if self.virtual_service_group_name is not None:
            result['virtualServiceGroupName'] = self.virtual_service_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('virtualServiceGroupId') is not None:
            self.virtual_service_group_id = m.get('virtualServiceGroupId')

        if m.get('virtualServiceGroupName') is not None:
            self.virtual_service_group_name = m.get('virtualServiceGroupName')

        return self

