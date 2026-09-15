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
        is_sale_data: bool = None,
        resource_directory_account_id: int = None,
        vendors: List[int] = None,
    ):
        # The list of asset type information for cloud assets.
        self.cloud_asset_types = cloud_asset_types
        # Specifies whether to return sale-related data. Valid values:
        # - **true**: Returns sale-related data.
        # - **false**: Does not return sale-related data.
        self.is_sale_data = is_sale_data
        # The ID of the member accounts in the resource folder.
        # > Invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The list of cloud vendors to query.
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

        if self.is_sale_data is not None:
            result['IsSaleData'] = self.is_sale_data

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

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

        if m.get('IsSaleData') is not None:
            self.is_sale_data = m.get('IsSaleData')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

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
        # The subtype of the cloud service. The asset type-subtype. Valid values:
        # 
        # - **0**: Elastic Compute Service (ECS) server
        #     *  **1**: Cloud disk (storage)
        #     *  **2**: Security group
        #     *  **100**: Instance
        # - **1**: Load balancing
        #     *  **0**: Classic Load Balancer (CLB)
        #     *  **1**: Application Load Balancer (ALB)
        # - **3**: ApsaraDB RDS database
        #     *  **0**: Instance
        # - **4**: ApsaraDB for MongoDB database
        #     *  **0**: Instance
        # - **5**: Tair (Redis® OSS-Compatible) database
        #     *  **0**: Instance
        # - **6**: Container Registry
        #     *  **1**: Enterprise Edition
        #     *  **2**: Personal Edition
        # - **8**: Container Service for Kubernetes (ACK)
        #     *  **0**: Cluster
        # - **9**: Virtual Private Cloud (VPC)
        #     *  **0**: NAT gateway
        #     *  **1**: EIP
        #     *  **2**: VPN
        #     *  **3**: FLOW_LOG
        # - **11**: ActionTrail
        #     *  **0**: Trail
        # - **12**: CDN
        #     *  **0**: Instance
        # - **13**: Certificate Management Service (formerly SSL Certificates Service)
        #     *  **0**: Certificate
        # - **14**: Apsara Devops
        #     *  **0**: Organization
        # - **16**: Anti-DDoS
        #     *  **0**: Instance
        # - **17**: Web Application Firewall (WAF)
        #     *  **0**: Domain name
        # - **18**: Object Storage Service (OSS)
        #     *  **0**: Bucket
        # - **19**: Cloud-native relational database PolarDB
        #     *  **0**: Cluster
        # - **20**: ApsaraDB RDS for PostgreSQL database
        #     *  **0**: Instance
        # - **21**: Microservices Engine (MSE)
        #     *  **0**: Cluster
        # - **22**: Apsara File Storage NAS
        #     *  **0**: File system
        # - **23**: Data Security Center (DSC)
        #     *  **0**: Instance
        # - **24**: Elastic IP Address (EIP)
        #     *  **0**: Anycast EIP
        # - **25**: Alibaba Cloud IDaaS EIAM
        #     *  **0**: Instance
        # - **26**: PolarDB-X
        #     *  **0**: Instance
        # - **27**: Elasticsearch
        #     *  **0**: Instance
        self.asset_sub_type = asset_sub_type
        # The type of the asset. Valid values:
        # 
        # - **0**: Elastic Compute Service (ECS) server
        # - **1**: Load balancing
        # - **3**: ApsaraDB RDS database
        # - **4**: ApsaraDB for MongoDB database
        # - **5**: Tair (Redis® OSS-Compatible) database
        # - **6**: Container Registry
        # - **8**: Container Service for Kubernetes (ACK)
        # - **9**: Virtual Private Cloud (VPC)
        # - **11**: ActionTrail
        # - **12**: CDN
        # - **13**: Certificate Management Service (formerly SSL Certificates Service)
        # - **14**: Apsara Devops
        # - **16**: Anti-DDoS
        # - **17**: Web Application Firewall (WAF)
        # - **18**: Object Storage Service (OSS)
        # - **19**: Cloud-native relational database PolarDB
        # - **20**: ApsaraDB RDS for PostgreSQL database
        # - **21**: Microservices Engine (MSE)
        # - **22**: Apsara File Storage NAS
        # - **23**: Data Security Center (DSC)
        # - **24**: Elastic IP Address (EIP)
        # - **25**: Alibaba Cloud IDaaS EIAM
        # - **26**: PolarDB-X
        # - **27**: Elasticsearch
        self.asset_type = asset_type
        # The server vendor. Valid values:
        # 
        # - **0**: Alibaba Cloud asset
        # - **1**: Non-cloud asset
        # - **2**: IDC asset
        # - **3**, **4**, **5**, **7**: Other cloud asset
        # - **8**: Lightweight asset
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

