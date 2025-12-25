# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSourceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
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
            temp_model = main_models.GetSourceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetSourceResponseBodyData(DaraModel):
    def __init__(
        self,
        create_timestamp: int = None,
        gateway_id: str = None,
        k_8ssource_info: main_models.GetSourceResponseBodyDataK8SSourceInfo = None,
        nacos_source_info: main_models.GetSourceResponseBodyDataNacosSourceInfo = None,
        name: str = None,
        resource_group_id: str = None,
        source_id: str = None,
        type: str = None,
        update_timestamp: int = None,
    ):
        # The creation timestamp.
        self.create_timestamp = create_timestamp
        # The gateway ID.
        self.gateway_id = gateway_id
        # Kubernetes source information.
        self.k_8ssource_info = k_8ssource_info
        # The source information when the source type is MSE_NACOS.
        self.nacos_source_info = nacos_source_info
        # The name.
        self.name = name
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The source ID.
        self.source_id = source_id
        # The type.
        self.type = type
        # The update timestamp.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.k_8ssource_info:
            self.k_8ssource_info.validate()
        if self.nacos_source_info:
            self.nacos_source_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.k_8ssource_info is not None:
            result['k8SSourceInfo'] = self.k_8ssource_info.to_map()

        if self.nacos_source_info is not None:
            result['nacosSourceInfo'] = self.nacos_source_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.type is not None:
            result['type'] = self.type

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('k8SSourceInfo') is not None:
            temp_model = main_models.GetSourceResponseBodyDataK8SSourceInfo()
            self.k_8ssource_info = temp_model.from_map(m.get('k8SSourceInfo'))

        if m.get('nacosSourceInfo') is not None:
            temp_model = main_models.GetSourceResponseBodyDataNacosSourceInfo()
            self.nacos_source_info = temp_model.from_map(m.get('nacosSourceInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

class GetSourceResponseBodyDataNacosSourceInfo(DaraModel):
    def __init__(
        self,
        address: str = None,
        cluster_id: str = None,
        instance_id: str = None,
    ):
        # The endpoint of the Nacos instance.
        self.address = address
        # The cluster ID.
        self.cluster_id = cluster_id
        # The Nacos instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        return self

class GetSourceResponseBodyDataK8SSourceInfo(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The ID of the Container Service for Kubernetes (ACK) cluster.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        return self

