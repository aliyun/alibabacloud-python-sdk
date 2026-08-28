# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetMigrationTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetMigrationTaskResponseBodyData = None,
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
            temp_model = main_models.GetMigrationTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetMigrationTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_namespace: str = None,
        create_time: int = None,
        description: str = None,
        env_id: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
        ingress_config: main_models.GetMigrationTaskResponseBodyDataIngressConfig = None,
        migration_type: str = None,
        service_name: str = None,
        slb_id: str = None,
        status: str = None,
        switch_type: str = None,
        task_id: str = None,
        user_id: str = None,
        virtual_services: List[main_models.GetMigrationTaskResponseBodyDataVirtualServices] = None,
        weight: int = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_namespace = cluster_namespace
        self.create_time = create_time
        self.description = description
        self.env_id = env_id
        self.gateway_id = gateway_id
        self.gateway_name = gateway_name
        self.ingress_config = ingress_config
        self.migration_type = migration_type
        self.service_name = service_name
        self.slb_id = slb_id
        self.status = status
        self.switch_type = switch_type
        self.task_id = task_id
        self.user_id = user_id
        self.virtual_services = virtual_services
        self.weight = weight

    def validate(self):
        if self.ingress_config:
            self.ingress_config.validate()
        if self.virtual_services:
            for v1 in self.virtual_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['apiId'] = self.api_id

        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name

        if self.cluster_namespace is not None:
            result['clusterNamespace'] = self.cluster_namespace

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.env_id is not None:
            result['envId'] = self.env_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_name is not None:
            result['gatewayName'] = self.gateway_name

        if self.ingress_config is not None:
            result['ingressConfig'] = self.ingress_config.to_map()

        if self.migration_type is not None:
            result['migrationType'] = self.migration_type

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.slb_id is not None:
            result['slbId'] = self.slb_id

        if self.status is not None:
            result['status'] = self.status

        if self.switch_type is not None:
            result['switchType'] = self.switch_type

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        result['virtualServices'] = []
        if self.virtual_services is not None:
            for k1 in self.virtual_services:
                result['virtualServices'].append(k1.to_map() if k1 else None)

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')

        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')

        if m.get('clusterNamespace') is not None:
            self.cluster_namespace = m.get('clusterNamespace')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('envId') is not None:
            self.env_id = m.get('envId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayName') is not None:
            self.gateway_name = m.get('gatewayName')

        if m.get('ingressConfig') is not None:
            temp_model = main_models.GetMigrationTaskResponseBodyDataIngressConfig()
            self.ingress_config = temp_model.from_map(m.get('ingressConfig'))

        if m.get('migrationType') is not None:
            self.migration_type = m.get('migrationType')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('slbId') is not None:
            self.slb_id = m.get('slbId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('switchType') is not None:
            self.switch_type = m.get('switchType')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        self.virtual_services = []
        if m.get('virtualServices') is not None:
            for k1 in m.get('virtualServices'):
                temp_model = main_models.GetMigrationTaskResponseBodyDataVirtualServices()
                self.virtual_services.append(temp_model.from_map(k1))

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class GetMigrationTaskResponseBodyDataVirtualServices(DaraModel):
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

class GetMigrationTaskResponseBodyDataIngressConfig(DaraModel):
    def __init__(
        self,
        ingress_class: str = None,
        watch_namespace: str = None,
    ):
        self.ingress_class = ingress_class
        self.watch_namespace = watch_namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ingress_class is not None:
            result['ingressClass'] = self.ingress_class

        if self.watch_namespace is not None:
            result['watchNamespace'] = self.watch_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ingressClass') is not None:
            self.ingress_class = m.get('ingressClass')

        if m.get('watchNamespace') is not None:
            self.watch_namespace = m.get('watchNamespace')

        return self

