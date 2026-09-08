# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class ListDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.ListDataSourcesResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.max_results = max_results
        self.next_token = next_token
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListDataSourcesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataSourcesResponseBodyItems(DaraModel):
    def __init__(
        self,
        connect_status: str = None,
        data_asset_id: str = None,
        data_source_id: str = None,
        data_source_size: int = None,
        db_name: str = None,
        description: str = None,
        engine_type: str = None,
        error_code: str = None,
        error_message: str = None,
        id: int = None,
        identify_status: str = None,
        instance_id: str = None,
        member_account: int = None,
        port: int = None,
        product_code: str = None,
        product_id: int = None,
        region_id: str = None,
        region_name: str = None,
        resource_group_id: str = None,
        tenant_id: str = None,
        user_name: str = None,
    ):
        self.connect_status = connect_status
        self.data_asset_id = data_asset_id
        self.data_source_id = data_source_id
        self.data_source_size = data_source_size
        self.db_name = db_name
        self.description = description
        self.engine_type = engine_type
        self.error_code = error_code
        self.error_message = error_message
        self.id = id
        self.identify_status = identify_status
        self.instance_id = instance_id
        self.member_account = member_account
        self.port = port
        self.product_code = product_code
        self.product_id = product_id
        self.region_id = region_id
        self.region_name = region_name
        self.resource_group_id = resource_group_id
        self.tenant_id = tenant_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_status is not None:
            result['ConnectStatus'] = self.connect_status

        if self.data_asset_id is not None:
            result['DataAssetId'] = self.data_asset_id

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_size is not None:
            result['DataSourceSize'] = self.data_source_size

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.description is not None:
            result['Description'] = self.description

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.id is not None:
            result['Id'] = self.id

        if self.identify_status is not None:
            result['IdentifyStatus'] = self.identify_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.member_account is not None:
            result['MemberAccount'] = self.member_account

        if self.port is not None:
            result['Port'] = self.port

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectStatus') is not None:
            self.connect_status = m.get('ConnectStatus')

        if m.get('DataAssetId') is not None:
            self.data_asset_id = m.get('DataAssetId')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceSize') is not None:
            self.data_source_size = m.get('DataSourceSize')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdentifyStatus') is not None:
            self.identify_status = m.get('IdentifyStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

