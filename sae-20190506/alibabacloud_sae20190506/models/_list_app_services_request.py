# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppServicesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        nacos_instance_id: str = None,
        nacos_namespace_id: str = None,
        namespace_id: str = None,
        page_number: int = None,
        page_size: int = None,
        registry_type: str = None,
        service_type: str = None,
        vpc_id: str = None,
    ):
        # The ID of the application. You must specify only one of the following parameters: vpcId, namespace ID, and application ID.
        self.app_id = app_id
        # The ID of the MSE Nacos instance. This parameter is required when the registry type is set to MSE Nacos.
        self.nacos_instance_id = nacos_instance_id
        # The ID of the MSE Nacos namespace. This parameter is required when the registry type is set to MSE Nacos.
        self.nacos_namespace_id = nacos_namespace_id
        # The ID of the namespace. You must specify only one of the following parameters: VPC ID, namespace ID, and application ID.
        self.namespace_id = namespace_id
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The registry type. Valid values:
        # 
        # *   **0**: SAE Nacos
        # *   **1**: SAE built-in Nacos
        # *   **2** :MSE Nacos
        # *   **9**: SAE Kubernetes service
        self.registry_type = registry_type
        # The service type. Valid values:
        # 
        # *   **dubbo**
        # *   **springCloud**
        # *   **hsf**
        # *   **k8sService**
        self.service_type = service_type
        # The unique identifier of the VPC. You must specify only one of the following parameters: VPC ID, namespace ID, and application ID.
        self.vpc_id = vpc_id

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

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('NacosInstanceId') is not None:
            self.nacos_instance_id = m.get('NacosInstanceId')

        if m.get('NacosNamespaceId') is not None:
            self.nacos_namespace_id = m.get('NacosNamespaceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

