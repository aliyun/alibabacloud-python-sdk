# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshAssetsRequest(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        cloud_asset_sub_type: int = None,
        cloud_asset_type: int = None,
        vendor: int = None,
    ):
        # The type of the asset that you want to synchronize. Valid values:
        # 
        # *   **cloud_product**: Alibaba Cloud service
        # *   **ecs**: Elastic Compute Service (ECS) instance
        # *   **container_image**: container image
        self.asset_type = asset_type
        # The subtype of the cloud service.
        # 
        # >  The following list describes the subtypes of cloud services.
        self.cloud_asset_sub_type = cloud_asset_sub_type
        # The type of the cloud service. Valid values:
        # 
        # *   **0**: ECS
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
        # *   **15**: Resource Access Management (RAM)
        # *   **16**: Anti-DDoS
        # *   **17**: Web Application Firewall (WAF)
        # *   **18**: Object Storage Service (OSS)
        # *   **19**: PolarDB
        # *   **20**: ApsaraDB RDS for PostgreSQL
        # *   **21**: Microservices Engine (MSE)
        # *   **22**: File Storage NAS (NAS)
        # *   **23**: Data Security Center (DSC)
        # *   **24**: Elastic IP Address (EIP)
        self.cloud_asset_type = cloud_asset_type
        # The type of the server. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud
        # *   **1**: a third-party cloud asset
        # *   **2**: an asset in a data center
        # *   **3**, **4**, **5**, and **7**: an asset provided by another cloud
        # *   **8**: a lightweight asset
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.cloud_asset_sub_type is not None:
            result['CloudAssetSubType'] = self.cloud_asset_sub_type

        if self.cloud_asset_type is not None:
            result['CloudAssetType'] = self.cloud_asset_type

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('CloudAssetSubType') is not None:
            self.cloud_asset_sub_type = m.get('CloudAssetSubType')

        if m.get('CloudAssetType') is not None:
            self.cloud_asset_type = m.get('CloudAssetType')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

