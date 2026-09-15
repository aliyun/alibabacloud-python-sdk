# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCloudAssetInstancesRequest(DaraModel):
    def __init__(
        self,
        cloud_asset_query_data: List[main_models.ListCloudAssetInstancesRequestCloudAssetQueryData] = None,
        cloud_asset_types: List[main_models.ListCloudAssetInstancesRequestCloudAssetTypes] = None,
        criteria: str = None,
        current_page: int = None,
        is_sale_data: bool = None,
        logical_exp: str = None,
        page_size: int = None,
        region_id: str = None,
        resource_directory_account_id: int = None,
    ):
        # The data list queried by keyword.
        self.cloud_asset_query_data = cloud_asset_query_data
        # The list of cloud asset instance types.
        self.cloud_asset_types = cloud_asset_types
        # The search conditions for assets. This parameter is in JSON format and contains the following fields:
        # - **name**: The search item.
        # - **value**: The value of the search item.
        # - **logicalExp**: The logical relationship between multiple search item values. Valid values:
        #     - **OR**: The search item values are evaluated using the OR operator.
        #     - **AND**: The search item values are evaluated using the AND operator.
        # > You can call the [GetCloudAssetCriteria](~~GetCloudAssetCriteria~~) operation to query the supported search conditions.
        self.criteria = criteria
        # The page number of the current page in a paging query.
        self.current_page = current_page
        # Specifies whether to return sale-related data. Valid values:
        # - **true**: Returns sale-related data.
        # - **false**: Does not return sale-related data.
        self.is_sale_data = is_sale_data
        # The logical relationship between multiple search conditions. Valid values:
        # 
        # - **OR**: The search conditions are evaluated using the OR operator.
        # - **AND**: The search conditions are evaluated using the AND operator.
        self.logical_exp = logical_exp
        # The maximum number of entries per page. Maximum value: 100. Default value: 20.
        self.page_size = page_size
        # The region ID of the instance.
        self.region_id = region_id
        # The ID of the Alibaba Cloud account of the resource folder member accounts.
        # > You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        if self.cloud_asset_query_data:
            for v1 in self.cloud_asset_query_data:
                 if v1:
                    v1.validate()
        if self.cloud_asset_types:
            for v1 in self.cloud_asset_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudAssetQueryData'] = []
        if self.cloud_asset_query_data is not None:
            for k1 in self.cloud_asset_query_data:
                result['CloudAssetQueryData'].append(k1.to_map() if k1 else None)

        result['CloudAssetTypes'] = []
        if self.cloud_asset_types is not None:
            for k1 in self.cloud_asset_types:
                result['CloudAssetTypes'].append(k1.to_map() if k1 else None)

        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.is_sale_data is not None:
            result['IsSaleData'] = self.is_sale_data

        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_asset_query_data = []
        if m.get('CloudAssetQueryData') is not None:
            for k1 in m.get('CloudAssetQueryData'):
                temp_model = main_models.ListCloudAssetInstancesRequestCloudAssetQueryData()
                self.cloud_asset_query_data.append(temp_model.from_map(k1))

        self.cloud_asset_types = []
        if m.get('CloudAssetTypes') is not None:
            for k1 in m.get('CloudAssetTypes'):
                temp_model = main_models.ListCloudAssetInstancesRequestCloudAssetTypes()
                self.cloud_asset_types.append(temp_model.from_map(k1))

        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IsSaleData') is not None:
            self.is_sale_data = m.get('IsSaleData')

        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        return self

class ListCloudAssetInstancesRequestCloudAssetTypes(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        vendor: int = None,
    ):
        # The subtype of the cloud service.
        # 
        # > For specific meanings, refer to the AssetSubType parameter in the [GetCloudAssetCriteria](~~GetCloudAssetCriteria~~) operation.
        self.asset_sub_type = asset_sub_type
        # The type of the cloud asset.
        # 
        # > For specific meanings, refer to the AssetType parameter in the [GetCloudAssetCriteria](~~GetCloudAssetCriteria~~) operation.
        self.asset_type = asset_type
        # The server vendor. Valid values:
        # 
        # - **0**: Alibaba Cloud asset
        # - **1**: Non-cloud asset
        # - **2**: IDC asset
        # - **3**, **4**, **5**, **7**: Third-party cloud asset
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

class ListCloudAssetInstancesRequestCloudAssetQueryData(DaraModel):
    def __init__(
        self,
        data: str = None,
        operator: str = None,
    ):
        # The query content.
        self.data = data
        # The query operator. Currently, only INCLUDE is supported.
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.operator is not None:
            result['Operator'] = self.operator

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        return self

