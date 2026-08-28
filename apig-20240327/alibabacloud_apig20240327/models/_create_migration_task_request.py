# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMigrationTaskRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        description: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        http_api_id: str = None,
        ingress_class: str = None,
        migration_type: str = None,
        watch_namespace: str = None,
    ):
        self.cluster_id = cluster_id
        self.description = description
        self.environment_id = environment_id
        self.gateway_id = gateway_id
        self.http_api_id = http_api_id
        self.ingress_class = ingress_class
        self.migration_type = migration_type
        self.watch_namespace = watch_namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.description is not None:
            result['description'] = self.description

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id

        if self.ingress_class is not None:
            result['ingressClass'] = self.ingress_class

        if self.migration_type is not None:
            result['migrationType'] = self.migration_type

        if self.watch_namespace is not None:
            result['watchNamespace'] = self.watch_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')

        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')

        if m.get('migrationType') is not None:
            self.migration_type = m.get('migrationType')

        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')

        return self

