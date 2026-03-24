# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListKspmInstancesRequest(DaraModel):
    def __init__(
        self,
        cloud_asset_types: List[main_models.ListKspmInstancesRequestCloudAssetTypes] = None,
        criteria: str = None,
        current_page: int = None,
        logical_exp: str = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # List of Kubernetes asset type information.
        self.cloud_asset_types = cloud_asset_types
        # Set the conditions for searching assets. This parameter is in JSON format, and case sensitivity should be noted when entering parameters. It includes the following fields:
        # 
        # - **name**: Search item
        # - **value**: Value of the search item
        # - **logicalExp**: The relationship between search items when multiple conditions are used. Values:
        #     - **OR**: Indicates an **or** relationship between multiple conditions.
        #     - **AND**: Indicates an **and** relationship between multiple conditions.
        # > Supports using region, instance name, instance ID, alarm status, risk status, and tag search conditions.
        self.criteria = criteria
        # Set which page to start displaying the query results from. The default value is 1, indicating that the display starts from the first page.
        self.current_page = current_page
        # Set the logical relationship that takes effect between multiple search conditions. Values:
        # 
        # - **OR**: Indicates an **or** relationship between multiple search conditions.
        # - **AND**: Indicates an **and** relationship between multiple search conditions.
        self.logical_exp = logical_exp
        # The maximum number of data entries displayed per page during pagination. The default value is 20.
        self.page_size = page_size
        # The ID of the region where the instance is located.
        self.region_id = region_id

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

        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_asset_types = []
        if m.get('CloudAssetTypes') is not None:
            for k1 in m.get('CloudAssetTypes'):
                temp_model = main_models.ListKspmInstancesRequestCloudAssetTypes()
                self.cloud_asset_types.append(temp_model.from_map(k1))

        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ListKspmInstancesRequestCloudAssetTypes(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        vendor: int = None,
    ):
        # Subtype of the product.
        # Asset type-subtype. Values:
        # 
        # - **0**: Workload
        #     *  **0**: Pod
        #     *  **1**: DaemonSet
        #     *  **2**: StatefulSet
        # - **1**: Service
        #     *  **0**: Service
        # - **2**: Namespace
        #     *  **0**: Namespace
        # - **3**: Authorization
        #     *  **0**: Role
        #     *  **1**: ClusterRole
        #     *  **2**: ClusterRoleBinding
        #     *  **3**: RoleBinding
        #     *  **4**: ServiceAccount
        # - **4**: Storage
        #     *  **0**: PersistentVolume
        #     *  **1**: PersistentVolumeClaim
        #     *  **2**: StorageClass
        # - **5**: Container
        #     *  **0**: Image
        # - **6**: Network
        #     *  **0**: Route
        #     *  **0**: Ingress
        # - **7**: Configuration
        #     *  **0**: ConfigMap
        # - **8**: Policies
        #     *  **0**: LimitRanges
        #     *  **1**: ResourceQuota
        self.asset_sub_type = asset_sub_type
        # Type of the asset. Values:
        # 
        # - **0**: Workload
        # - **1**: Service
        # - **2**: Namespace
        # - **3**: Authorization
        # - **4**: Storage
        # - **5**: Container
        # - **6**: Network
        # - **7**: Configuration
        # - **8**: Policies
        self.asset_type = asset_type
        # Vendor of the asset. The fixed value is **200**.
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

