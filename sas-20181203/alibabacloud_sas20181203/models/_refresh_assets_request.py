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
        resource_directory_account_id: int = None,
        vendor: int = None,
    ):
        # The type of asset to synchronize. Default value: **ecs**. Valid values:
        # - **cloud_product**: cloud product
        # - **ecs**: server
        # - **container_image**: container image
        self.asset_type = asset_type
        # The subtype of the cloud product.
        # 
        # > Refer to the following list for valid values.
        self.cloud_asset_sub_type = cloud_asset_sub_type
        # The type of cloud product. Valid values:
        # 
        # - **0**: server
        # - **1**: load balancing
        # - **3**: ApsaraDB RDS database
        # - **4**: ApsaraDB for MongoDB database
        # - **5**: Tair (Redis® OSS-Compatible) database
        # - **6**: Container Registry
        # - **8**: container service for Kubernetes
        # - **9**: VPC
        # - **11**: ActionTrail
        # - **12**: CDN
        # - **13**: Certificate Management Service (formerly SSL Certificates Service)
        # - **14**: Apsara Devops
        # - **15**: access control
        # - **16**: Anti-DDoS
        # - **17**: Web Application Firewall
        # - **18**: OSS
        # - **19**: cloud-native relational database PolarDB
        # - **20**: ApsaraDB RDS for PostgreSQL database
        # - **21**: Microservices Engine
        # - **22**: File Storage NAS
        # - **23**: Data Security Center
        # - **24**: EIP
        self.cloud_asset_type = cloud_asset_type
        # The ID of the Alibaba Cloud account of the member accounts in the resource directory.
        # > Call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The server vendor. Valid values:
        # 
        # - **0**: Alibaba Cloud asset
        # - **1**: asset outside the cloud
        # - **2**: IDC asset
        # - **3**, **4**, **5**, **7**: third-party cloud asset
        # - **8**: lightweight asset
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

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

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

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

