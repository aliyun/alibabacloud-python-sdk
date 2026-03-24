# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCloudAssetSummaryRequest(DaraModel):
    def __init__(
        self,
        cloud_asset_types: List[main_models.GetCloudAssetSummaryRequestCloudAssetTypes] = None,
        vendors: List[int] = None,
    ):
        # List of asset type information for cloud assets
        self.cloud_asset_types = cloud_asset_types
        # List of cloud vendors to be queried.
        self.vendors = vendors

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
        result['CloudAssetTypes'] = []
        if self.cloud_asset_types is not None:
            for k1 in self.cloud_asset_types:
                result['CloudAssetTypes'].append(k1.to_map() if k1 else None)

        if self.vendors is not None:
            result['Vendors'] = self.vendors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_asset_types = []
        if m.get('CloudAssetTypes') is not None:
            for k1 in m.get('CloudAssetTypes'):
                temp_model = main_models.GetCloudAssetSummaryRequestCloudAssetTypes()
                self.cloud_asset_types.append(temp_model.from_map(k1))

        if m.get('Vendors') is not None:
            self.vendors = m.get('Vendors')

        return self

class GetCloudAssetSummaryRequestCloudAssetTypes(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        vendor: int = None,
    ):
        # Subtypes of cloud products. Asset type-subtype. Values:
        # - **0**: ECS (Elastic Compute Service)
        #   *  **1**: Disk (Storage)
        #   *  **2**: Security Group
        #   *  **100**: Instance
        # - **1**: Load Balancer 
        #   *  **0**: Load Balancer 
        #   *  **1**: Application Load Balancer 
        # - **3**: ApsaraDB RDS 
        #   *  **0**: Instance 
        # - **4**: ApsaraDB for MongoDB 
        #   *  **0**: Instance 
        # - **5**: ApsaraDB Tair (Redis Compatible) 
        #   *  **0**: Instance 
        # - **6**: Container Registry 
        #   *  **1**: Enterprise Edition 
        #   *  **2**: Personal Edition 
        # - **8**: Container Service for Kubernetes 
        #   *  **0**: Cluster 
        # - **9**: Virtual Private Cloud (VPC) 
        #   *  **0**: NAT Gateway 
        #   *  **1**: EIP (Elastic IP) 
        #   *  **2**: VPN 
        #   *  **3**: FLOW_LOG 
        # - **11**: ActionTrail 
        #   *  **0**: Trail 
        # - **12**: CDN 
        #   *  **0**: Instance 
        # - **13**: Digital Certificate Management Service (formerly SSL Certificates) 
        #   *  **0**: Certificate 
        # - **14**: DevOps 
        #   *  **0**: Organization 
        # - **16**: DDoS Protection 
        #   *  **0**: Instance 
        # - **17**: Web Application Firewall 
        #   *  **0**: Domain 
        # - **18**: Object Storage 
        #   *  **0**: Bucket 
        # - **19**: PolarDB (Cloud-Native Relational Database) 
        #   *  **0**: Cluster 
        # - **20**: ApsaraDB for PostgreSQL 
        #   *  **0**: Instance 
        # - **21**: Microservices Engine 
        #   *  **0**: Cluster 
        # - **22**: File Storage NAS 
        #   *  **0**: File System 
        # - **23**: Data Security Center 
        #   *  **0**: Instance 
        # - **24**: Elastic Public IP 
        #   *  **0**: Anycast Elastic Public IP 
        # - **25**: Cloud Identity Service - EIAM 
        #   *  **0**: Instance 
        # - **26**: PolarDB-X 
        #   *  **0**: Instance 
        # - **27**: Elasticsearch 
        #   *  **0**: Instance
        self.asset_sub_type = asset_sub_type
        # The type of asset. Values:
        # - **0**: Elastic Compute Service (ECS) 
        # - **1**: Load Balancer 
        # - **3**: ApsaraDB for RDS 
        # - **4**: ApsaraDB for MongoDB 
        # - **5**: ApsaraDB for Tair (Redis compatible) 
        # - **6**: Container Registry 
        # - **8**: Container Service for Kubernetes 
        # - **9**: Virtual Private Cloud (VPC) 
        # - **11**: ActionTrail 
        # - **12**: Content Delivery Network (CDN) 
        # - **13**: SSL Certificates (now known as Certificate Management Service) 
        # - **14**: DevOps 
        # - **16**: DDoS Protection 
        # - **17**: Web Application Firewall 
        # - **18**: Object Storage Service (OSS) 
        # - **19**: PolarDB 
        # - **20**: ApsaraDB for PostgreSQL 
        # - **21**: Microservices Engine 
        # - **22**: File Storage NAS 
        # - **23**: Data Security Center 
        # - **24**: Elastic IP Address 
        # - **25**: Cloud Identity Service - EIAM 
        # - **26**: PolarDB-X 
        # - **27**: Elasticsearch
        self.asset_type = asset_type
        # Server vendor. Values:
        # - **0**: Alibaba Cloud Asset 
        # - **1**: Non-cloud Asset 
        # - **2**: IDC Asset 
        # - **3**, **4**, **5**, **7**: Other Cloud Assets 
        # - **8**: Lightweight Asset
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

