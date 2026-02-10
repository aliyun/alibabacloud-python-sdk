# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListInstanceCatalogResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vendors: List[main_models.ListInstanceCatalogResponseBodyVendors] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The asset types by service provider.
        self.vendors = vendors

    def validate(self):
        if self.vendors:
            for v1 in self.vendors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Vendors'] = []
        if self.vendors is not None:
            for k1 in self.vendors:
                result['Vendors'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.vendors = []
        if m.get('Vendors') is not None:
            for k1 in m.get('Vendors'):
                temp_model = main_models.ListInstanceCatalogResponseBodyVendors()
                self.vendors.append(temp_model.from_map(k1))

        return self

class ListInstanceCatalogResponseBodyVendors(DaraModel):
    def __init__(
        self,
        instance_types: List[main_models.ListInstanceCatalogResponseBodyVendorsInstanceTypes] = None,
        name: str = None,
        value: int = None,
    ):
        # The asset types.
        self.instance_types = instance_types
        # The name of the service provider.
        self.name = name
        # The ID of the service provider type. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud
        # *   **1**: an asset outside Alibaba Cloud
        # *   **2**: an asset in a data center
        # *   **3**, **4**, **5**, and **7**: an asset from a third-party cloud service provider
        # *   **8**: a lightweight cloud asset
        self.value = value

    def validate(self):
        if self.instance_types:
            for v1 in self.instance_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceTypes'] = []
        if self.instance_types is not None:
            for k1 in self.instance_types:
                result['InstanceTypes'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_types = []
        if m.get('InstanceTypes') is not None:
            for k1 in m.get('InstanceTypes'):
                temp_model = main_models.ListInstanceCatalogResponseBodyVendorsInstanceTypes()
                self.instance_types.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListInstanceCatalogResponseBodyVendorsInstanceTypes(DaraModel):
    def __init__(
        self,
        instance_sub_types: List[main_models.ListInstanceCatalogResponseBodyVendorsInstanceTypesInstanceSubTypes] = None,
        name: str = None,
        value: int = None,
    ):
        # The asset subtypes.
        self.instance_sub_types = instance_sub_types
        # The name of the asset type.
        self.name = name
        # The ID of the asset type. Valid values:
        # 
        # *   **0**: Elastic Compute Service (ECS)
        # *   **1**: Server Load Balancer (SLB)
        # *   **3**: ApsaraDB RDS
        # *   **4**: ApsaraDB for MongoDB (MongoDB)
        # *   **5**: Tair (Redis OSS-compatible)
        # *   **6**: Container Registry
        # *   **8**: Container Service for Kubernetes (ACK)
        # *   **9**: Virtual Private Cloud (VPC)
        # *   **11**: ActionTrail
        # *   **12**: Alibaba Cloud CDN (CDN)
        # *   **13**: Certificate Management Service (formerly SSL Certificates Service)
        # *   **14**: Alibaba Cloud DevOps
        # *   **15**: Resource Access Management (RAM)
        # *   **16**: Anti-DDoS
        # *   **17**: Web Application Firewall (WAF)
        # *   **18**: Object Storage Service (OSS)
        # *   **19**: PolarDB
        # *   **20**: ApsaraDB RDS for PostgreSQL
        # *   **21**: Microservices Engine (MSE)
        # *   **22**: Apsara File Storage NAS (NAS)
        # *   **23**: Data Security Center (DSC)
        # *   **24**: Elastic IP Address (EIP)
        # *   **25**: Identity as a Service (IDaaS) - Enterprise Identity Access Management (EIAM)
        # *   **26**: PolarDB for Xscale (PolarDB-X)
        # *   **27**: Elasticsearch
        self.value = value

    def validate(self):
        if self.instance_sub_types:
            for v1 in self.instance_sub_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceSubTypes'] = []
        if self.instance_sub_types is not None:
            for k1 in self.instance_sub_types:
                result['InstanceSubTypes'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_sub_types = []
        if m.get('InstanceSubTypes') is not None:
            for k1 in m.get('InstanceSubTypes'):
                temp_model = main_models.ListInstanceCatalogResponseBodyVendorsInstanceTypesInstanceSubTypes()
                self.instance_sub_types.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListInstanceCatalogResponseBodyVendorsInstanceTypesInstanceSubTypes(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        # The name of the asset subtype.
        self.name = name
        # The ID of the asset subtype.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

