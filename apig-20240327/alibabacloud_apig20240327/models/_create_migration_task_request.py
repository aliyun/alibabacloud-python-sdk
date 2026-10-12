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
        # The ID of the source ACK cluster. The value must be the same as the cluster specified in the IngressInfo of the API. Note: This parameter is actually required. If this parameter is not specified, the API returns 400 InvalidParameter.IsEmpty.
        self.cluster_id = cluster_id
        # The description of the task. The description is stored only when the task is created.
        self.description = description
        # The ID of the destination environment. The value must be the same as the Ingress import environment of the API. Note: This parameter is actually required. If this parameter is not specified, the API returns 400 InvalidParameter.IsEmpty. You can call ListEnvironments to query existing environment IDs. CreateEnvironment has been deprecated.
        self.environment_id = environment_id
        # The ID of the destination gateway to which traffic is migrated.
        self.gateway_id = gateway_id
        # The HTTP API ID. The API must have been imported as an Ingress type (HttpIngress) API. Note: This parameter is actually required. If this parameter is not specified, the API returns 400 InvalidParameter.IsEmpty.
        self.http_api_id = http_api_id
        # The Ingress class. If specified, the value must be the same as the API import configuration. Otherwise, an ingress class conflict error is returned.
        self.ingress_class = ingress_class
        # The migration type.
        # [_single.params.body.props.migrationType.enum.Nginx Ingress]Nginx Ingress migration.
        self.migration_type = migration_type
        # The watched namespace. If specified, the value must be the same as the API import configuration. Otherwise, a watchNamespace conflict error is returned.
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

