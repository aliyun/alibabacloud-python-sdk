# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCloudAssetSchemasRequest(DaraModel):
    def __init__(
        self,
        associated_data_only: bool = None,
        cloud_asset_types: List[main_models.ListCloudAssetSchemasRequestCloudAssetTypes] = None,
        current_page: int = None,
        data_names: List[str] = None,
        lang: str = None,
        page_size: int = None,
    ):
        # Whether to filter out attributes that can be associated with other assets.
        self.associated_data_only = associated_data_only
        # The types of cloud assets.
        self.cloud_asset_types = cloud_asset_types
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # List of asset data names
        self.data_names = data_names
        # The language type for requesting and receiving messages, with a default value of **zh**. The values can be: - **zh**: Chinese - **en**: English
        self.lang = lang
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        if self.cloud_asset_types:
            for v1 in self.cloud_asset_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_data_only is not None:
            result['AssociatedDataOnly'] = self.associated_data_only

        result['CloudAssetTypes'] = []
        if self.cloud_asset_types is not None:
            for k1 in self.cloud_asset_types:
                result['CloudAssetTypes'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.data_names is not None:
            result['DataNames'] = self.data_names

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedDataOnly') is not None:
            self.associated_data_only = m.get('AssociatedDataOnly')

        self.cloud_asset_types = []
        if m.get('CloudAssetTypes') is not None:
            for k1 in m.get('CloudAssetTypes'):
                temp_model = main_models.ListCloudAssetSchemasRequestCloudAssetTypes()
                self.cloud_asset_types.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DataNames') is not None:
            self.data_names = m.get('DataNames')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListCloudAssetSchemasRequestCloudAssetTypes(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        vendor: int = None,
    ):
        # The subtype of the cloud service or asset. Valid values:
        # 
        # *   **0**: ECS
        # 
        #     *   **0**: instance
        #     *   **1**: disk (storage)
        #     *   **2**: security group
        # 
        # *   **1**: SLB
        # 
        #     *   **0**: SLB
        #     *   **1**: Application Load Balancer (ALB)
        # 
        # *   **3**: ApsaraDB RDS
        # 
        #     *   **0**: instance
        # 
        # *   **4**: MongoDB
        # 
        #     *   **0**: instance
        # 
        # *   **5**: Redis
        # 
        #     *   **0**: instance
        # 
        # *   **6**: Container Registry
        # 
        #     *   **1**: Enterprise Edition
        #     *   **2**: Personal Edition
        # 
        # *   **8**: ACK
        # 
        #     *   **0**: cluster
        # 
        # *   **9**: VPC
        # 
        #     *   **0**: NAT gateway
        #     *   **1**: Elastic IP address (EIP)
        #     *   **2**: VPN
        #     *   **3**: VPC Flow Logs
        # 
        # *   **11**: ActionTrail
        # 
        #     *   **0**: trail
        # 
        # *   **12**: CDN
        # 
        #     *   **0**: instance
        # 
        # *   **13**: Certificate Management Service (formerly SSL Certificates Service)
        # 
        #     *   **0**: certificate
        # 
        # *   **14**: Apsara Devops
        # 
        #     *   **0**: organization
        # 
        # *   **16**: Anti-DDoS
        # 
        #     *   **0**: instance
        # 
        # *   **17**: WAF
        # 
        #     *   **0**: domain name
        # 
        # *   **18**: OSS
        # 
        #     *   **0**: bucket
        # 
        # *   **19**: PolarDB
        # 
        #     *   **0**: cluster
        # 
        # *   **20**: ApsaraDB RDS for PostgreSQL
        # 
        #     *   **0**: instance
        # 
        # *   **21**: MSE
        # 
        #     *   **0**: cluster
        # 
        # *   **22**: NAS
        # 
        #     *   **0**: file system
        # 
        # *   **23**: DSC
        # 
        #     *   **0**: instance
        # 
        # *   **24**: EIP
        # 
        #     *   **0**: Anycast EIP
        # 
        # *   **25**: IDaaS EIAM
        # 
        #     *   **0**: instance
        # 
        # *   **26**: PolarDB-X
        # 
        #     *   **0**: instance
        # 
        # *   **27**: Elasticsearch
        # 
        #     *   **0**: instance
        self.asset_sub_type = asset_sub_type
        # The type of the asset. Valid values:
        # 
        # *   **0**: Elastic Compute Service (ECS)
        # *   **1**: Server Load Balancer (SLB)
        # *   **3**: ApsaraDB RDS
        # *   **4**: ApsaraDB for MongoDB (MongoDB)
        # *   **5**: ApsaraDB for Redis (Redis)
        # *   **6**: Container Registry
        # *   **8**: Container Service for Kubernetes (ACK)
        # *   **9**: Virtual Private Cloud (VPC)
        # *   **11**: ActionTrail
        # *   **12**: Alibaba Cloud CDN (CDN)
        # *   **13**: Certificate Management Service (formerly SSL Certificates Service)
        # *   **14**: Apsara Devops
        # *   **16**: Anti-DDoS
        # *   **17**: Web Application Firewall (WAF)
        # *   **18**: Object Storage Service (OSS)
        # *   **19**: PolarDB
        # *   **20**: ApsaraDB RDS for PostgreSQL
        # *   **21**: Microservices Engine (MSE)
        # *   **22**: File Storage NAS (NAS)
        # *   **23**: Data Security Center (DSC)
        # *   **24**: Elastic IP Address (EIP)
        # *   **25**: IDaaS EIAM
        # *   **26**: PolarDB-X
        # *   **27**: Elasticsearch
        self.asset_type = asset_type
        # The server type. Valid values:
        # 
        # *   **0**: a cloud asset provided by Alibaba Cloud
        # *   **1**: a cloud asset outside Alibaba Cloud
        # *   **2**: a cloud asset in a data center
        # *   **3**, **4**, **5**, and **7**: a cloud asset provided by a third-party service provider
        # *   **8**: a lightweight cloud asset
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_sub_type is not None:
            result['AssetSubType'] = self.asset_sub_type

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSubType') is not None:
            self.asset_sub_type = m.get('AssetSubType')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

