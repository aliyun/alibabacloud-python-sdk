# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribePhysicalConnectionsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        filter: List[main_models.DescribePhysicalConnectionsRequestFilter] = None,
        include_reservation_data: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: List[main_models.DescribePhysicalConnectionsRequestTags] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # The filter keys.
        self.filter = filter
        # Specifies whether to return the data about pending orders. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.include_reservation_data = include_reservation_data
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**. Valid values: **1** to **50**.
        self.page_size = page_size
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the Express Connect circuit belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag list.
        self.tags = tags

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.include_reservation_data is not None:
            result['IncludeReservationData'] = self.include_reservation_data

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribePhysicalConnectionsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('IncludeReservationData') is not None:
            self.include_reservation_data = m.get('IncludeReservationData')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribePhysicalConnectionsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribePhysicalConnectionsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the resource. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # It can be up to 64 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N to add to the resource. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # It can be up to 128 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribePhysicalConnectionsRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The key of the filter. Valid values:
        # 
        # *   **PhysicalConnectionId**: the ID of the Express Connect circuit.
        # 
        # *   **AccessPointId**: the ID of the access point.
        # 
        # *   **Type**: the type of resource to which the Express Connect circuit is connected. You can set Type only to **VPC**.
        # 
        # *   **LineOperator**: the connectivity provider of the Express Connect circuit. Valid values:
        # 
        #     *   **CT**: China Telecom.
        #     *   **CU**: China Unicom.
        #     *   **CM**: China Mobile.
        #     *   **CO**: other connectivity providers in the Chinese mainland.
        #     *   **Equinix**: Equinix.
        #     *   **Other**: other connectivity providers outside the Chinese mainland.
        # 
        # *   **Spec**: the specification of the Express Connect circuit. Valid values:
        # 
        #     *   **1G and below**
        #     *   **10G**
        #     *   **40G**
        #     *   **100G**
        # 
        # >  By default, you cannot set the value to **40G** or **100G**. To use these values, you must first contact your account manager.
        # 
        # *   **Status**: the status of the Express Connect circuit. Valid values:
        # 
        #     *   **Initial**: The application is under review.
        #     *   **Approved**: The application is approved.
        #     *   **Allocating**: The system is allocating resources.
        #     *   **Allocated**: The Express Connect circuit is under construction.
        #     *   **Confirmed**: The Express Connect circuit is pending for user confirmation.
        #     *   **Enabled**: The Express Connect circuit is enabled.
        #     *   **Rejected**: The application is rejected.
        #     *   **Canceled**: The application is canceled.
        #     *   **Allocation Failed**: The system failed to allocate resources.
        #     *   **Terminating**: The Express Connect circuit is being disabled.
        #     *   **Terminated**: The Express Connect circuit is disabled.
        # 
        # *   **Name**: the name of the Express Connect circuit.
        # 
        # *   **ProductType**: the type of the Express Connect circuit. Valid values:
        # 
        #     *   **VirtualPhysicalConnection**: shared Express Connect circuit
        #     *   **PhysicalConnection**: dedicated Express Connect circuit.
        # 
        # You can specify at most five filter conditions in each request. The logical relation among the filter conditions is **AND**. Therefore, an Express Connect circuit is returned only when all specified filter conditions are matched.
        self.key = key
        # The filter values.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

