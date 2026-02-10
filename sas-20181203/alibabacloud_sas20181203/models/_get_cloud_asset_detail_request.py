# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCloudAssetDetailRequest(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        cloud_asset_instances: List[main_models.GetCloudAssetDetailRequestCloudAssetInstances] = None,
        vendor: int = None,
    ):
        # The subtype of the cloud service.
        self.asset_sub_type = asset_sub_type
        # The type of the cloud asset. Valid values:
        # 
        # *   **0**: Elastic Compute Service (ECS).
        # *   **1**: Server Load Balancer (SLB).
        # *   **3**: ApsaraDB RDS.
        # *   **4**: ApsaraDB for MongoDB.
        # *   **5**: ApsaraDB for Redis.
        # *   **6**: Container Registry.
        # *   **8**: Container Service for Kubernetes.
        # *   **9**: Virtual Private Cloud (VPC).
        # *   **11**: ActionTrail.
        # *   **12**: Alibaba Cloud CDN (CDN).
        # *   **13**: Certificate Management Service.
        # *   **14**: Apsara Devops.
        # *   **15**: Resource Access Management (RAM).
        # *   **16**: Anti-DDoS.
        # *   **17**: Web Application Firewall (WAF).
        # *   **18**: Object Storage Service (OSS).
        # *   **19**: PolarDB.
        # *   **20**: ApsaraDB RDS for PostgreSQL.
        # *   **21**: Microservices Engine (MSE).
        # *   **22**: File Storage NAS (NAS).
        # *   **23**: Data Security Center (DSC).
        # *   **24**: Elastic IP Address (EIP).
        # *   **25**: Identity as a Service (IDaaS)-Employee Identity and Access Management (EIAM).
        # *   **26**: PolarDB-X.
        # *   **27**: Elasticsearch.
        self.asset_type = asset_type
        # The details of the assets.
        self.cloud_asset_instances = cloud_asset_instances
        # The service provider of the cloud asset. Valid values:
        # 
        # *   **0**: Alibaba Cloud.
        # *   **1**: service provider that is unrecognized.
        # *   **2**: data center.
        # *   **3**, **4**, **5**, and **7**: third-party service provider.
        # *   **8**: simple application server.
        self.vendor = vendor

    def validate(self):
        if self.cloud_asset_instances:
            for v1 in self.cloud_asset_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_sub_type is not None:
            result['AssetSubType'] = self.asset_sub_type

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        result['CloudAssetInstances'] = []
        if self.cloud_asset_instances is not None:
            for k1 in self.cloud_asset_instances:
                result['CloudAssetInstances'].append(k1.to_map() if k1 else None)

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSubType') is not None:
            self.asset_sub_type = m.get('AssetSubType')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        self.cloud_asset_instances = []
        if m.get('CloudAssetInstances') is not None:
            for k1 in m.get('CloudAssetInstances'):
                temp_model = main_models.GetCloudAssetDetailRequestCloudAssetInstances()
                self.cloud_asset_instances.append(temp_model.from_map(k1))

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class GetCloudAssetDetailRequestCloudAssetInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The instance ID of the cloud asset.
        self.instance_id = instance_id
        # The region in which the cloud asset resides.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

