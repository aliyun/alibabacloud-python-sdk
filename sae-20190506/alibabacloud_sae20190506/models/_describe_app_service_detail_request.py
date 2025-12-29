# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppServiceDetailRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        nacos_instance_id: str = None,
        nacos_namespace_id: str = None,
        service_group: str = None,
        service_name: str = None,
        service_type: str = None,
        service_version: str = None,
    ):
        # 6dcc8c9e-d3da-478a-a066-86dcf820\\*\\*\\*\\*
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the MSE Nacos instance.
        self.nacos_instance_id = nacos_instance_id
        # The ID of the namespace for the MSE Nacos instance.
        self.nacos_namespace_id = nacos_namespace_id
        # springCloud
        self.service_group = service_group
        # edas.service.provider
        self.service_name = service_name
        # springCloud
        self.service_type = service_type
        # 1.0.0
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.nacos_instance_id is not None:
            result['NacosInstanceId'] = self.nacos_instance_id

        if self.nacos_namespace_id is not None:
            result['NacosNamespaceId'] = self.nacos_namespace_id

        if self.service_group is not None:
            result['ServiceGroup'] = self.service_group

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('NacosInstanceId') is not None:
            self.nacos_instance_id = m.get('NacosInstanceId')

        if m.get('NacosNamespaceId') is not None:
            self.nacos_namespace_id = m.get('NacosNamespaceId')

        if m.get('ServiceGroup') is not None:
            self.service_group = m.get('ServiceGroup')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        return self

