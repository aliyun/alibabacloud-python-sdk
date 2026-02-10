# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCloudAssetSchemasResponseBody(DaraModel):
    def __init__(
        self,
        cloud_asset_schemas: List[main_models.ListCloudAssetSchemasResponseBodyCloudAssetSchemas] = None,
        page_info: main_models.ListCloudAssetSchemasResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # List of asset structure definitions
        self.cloud_asset_schemas = cloud_asset_schemas
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Values: 
        # - **true**: The call was successful. 
        # - **false**: The call failed.
        self.success = success

    def validate(self):
        if self.cloud_asset_schemas:
            for v1 in self.cloud_asset_schemas:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudAssetSchemas'] = []
        if self.cloud_asset_schemas is not None:
            for k1 in self.cloud_asset_schemas:
                result['CloudAssetSchemas'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_asset_schemas = []
        if m.get('CloudAssetSchemas') is not None:
            for k1 in m.get('CloudAssetSchemas'):
                temp_model = main_models.ListCloudAssetSchemasResponseBodyCloudAssetSchemas()
                self.cloud_asset_schemas.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListCloudAssetSchemasResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCloudAssetSchemasResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # Current page number.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCloudAssetSchemasResponseBodyCloudAssetSchemas(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        data_name: str = None,
        properties: str = None,
        vendor: int = None,
    ):
        # Subtype of the cloud product.
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
        # Asset structure definition name
        self.data_name = data_name
        # Current asset structure definition text.
        self.properties = properties
        # The source of the server. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud.
        # *   **1**: a third-party cloud server
        # *   **2**: a server in a data center
        # *   **3**, **4**, **5**, and **7**: other cloud asset
        # *   **8**: a lightweight asset
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

        if self.data_name is not None:
            result['DataName'] = self.data_name

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSubType') is not None:
            self.asset_sub_type = m.get('AssetSubType')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

