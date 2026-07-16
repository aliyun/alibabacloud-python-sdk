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
        # Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters.
        self.client_token = client_token
        # The list of filter conditions.
        self.filter = filter
        # Specifies whether to return data of orders that have not taken effect. Valid values:
        # 
        # * **true**: Returns data of orders that have not taken effect.
        # 
        # * **false** (default): Does not return data of orders that have not taken effect.
        self.include_reservation_data = include_reservation_data
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the list. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page in a paged query. Default value: **10**. Valid values: **1** to **50**.
        self.page_size = page_size
        # The region ID of the Express Connect circuit. 
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the Express Connect circuit belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags.
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
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
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
        # The filter condition. Valid values:
        # 
        # - **PhysicalConnectionId**: the Express Connect circuit ID.
        # 
        # - **AccessPointId**: the access point ID.
        # 
        # - **Type**: the Express Connect circuit type. This filter condition supports only the value **VPC**.
        # 
        # - **LineOperator**: the carrier of the Express Connect circuit. This filter condition supports the following values:
        #     - **CT**: China Telecom.
        #     - **CU**: China Unicom.
        #     - **CM**: China Mobile.
        #     - **CO**: other carriers in China.
        #     - **Equinix**: Equinix.
        #     - **Other**: other carriers outside China.
        # 
        # - **Spec**: the specification of the Express Connect circuit. This filter condition supports the following values:
        #     - **1G and below**.
        #     - **10G**.
        #     - **40G**.
        #     - **100G**.
        # >  The **40G** and **100G** specifications are not available by default. Only users who have committed an application to their account manager and received approval can use these values.
        # 
        # - **Status**: the status of the Express Connect circuit. This filter condition supports the following values:
        #     - **Initial**: pending application.
        #     - **Approved**: approved.
        #     - **Allocating**: allocating resources.
        #     - **Allocated**: under construction.
        #     - **Confirmed**: pending user confirmation.
        #     - **Enabled**: enabled.
        #     - **Rejected**: application denied.
        #     - **Canceled**: canceled.
        #     - **Allocation Failed**: resource allocation failed.
        #     - **Terminating**: stopping.
        #     - **Terminated**: stopped.
        # 
        # - **Name**: the name of the Express Connect circuit.
        # - **ProductType**: the circuit type. Valid values:
        #     - **VirtualPhysicalConnection**: shared Express Connect circuit.
        #     - **PhysicalConnection**: dedicated Express Connect circuit.
        # 
        # You can specify up to 5 filter conditions at a time. The filter conditions have an **AND** relationship. Results are returned only when all filter conditions are met.
        self.key = key
        # The list of filter values.
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

