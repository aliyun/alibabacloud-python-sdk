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
        # 云产品的子类型。
        # 资产的类型-子类型。取值：
        # 
        # - **0**：云服务器 ECS 
        #     *  **1**：磁盘（存储）
        #     *  **2**：安全组
        #     *  **100**：实例
        # - **1**：负载均衡
        #     *  **0**：负载均衡
        #     *  **1**：应用型负载均衡
        # - **3**：云数据库 RDS
        #     *  **0**：实例
        # - **4**：云数据库 MongoDB 版
        #     *  **0**：实例
        # - **5**：云数据库 Tair（兼容 Redis）
        #     *  **0**：实例
        # - **6**：容器镜像服务
        #     *  **1**：企业版
        #     *  **2**：个人版
        # - **8**：容器服务Kubernetes版
        #     *  **0**：集群
        # - **9**：专有网络VPC
        #     *  **0**：NAT网关
        #     *  **1**：EIP
        #     *  **2**：VPN
        #     *  **3**：FLOW_LOG
        # - **11**：操作审计
        #     *  **0**：跟踪
        # - **12**：CDN
        #     *  **0**：实例
        # - **13**：数字证书管理服务（原SSL证书）
        #     *  **0**：证书
        # - **14**：云效
        #     *  **0**：组织
        # - **16**：DDoS防护
        #     *  **0**：实例
        # - **17**：Web应用防火墙
        #     *  **0**：域名
        # - **18**：对象存储
        #     *  **0**：Bucket
        # - **19**：云原生关系型数据库 PolarDB
        #     *  **0**：集群
        # - **20**：云数据库 PostgreSQL 版
        #     *  **0**：实例
        # - **21**：微服务引擎
        #     *  **0**：集群
        # - **22**：文件存储NAS
        #     *  **0**：文件系统
        # - **23**：数据安全中心
        #     *  **0**：实例
        # - **24**：弹性公网IP
        #     *  **0**：任播弹性公网IP
        # - **25**：云身份服务-EIAM
        #     *  **0**：实例
        # - **26**：PolarDB-X
        #     *  **0**：实例
        # - **27**：Elasticsearch
        #     *  **0**：实例
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

