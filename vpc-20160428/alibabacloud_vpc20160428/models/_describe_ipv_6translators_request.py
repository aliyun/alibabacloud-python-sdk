# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIPv6TranslatorsRequest(DaraModel):
    def __init__(
        self,
        allocate_ipv_4addr: str = None,
        allocate_ipv_6addr: str = None,
        business_status: str = None,
        ipv_6translator_id: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        pay_type: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spec: str = None,
        status: str = None,
    ):
        # The IPv4 address allocated to the IPv6 Translation Service instance.
        self.allocate_ipv_4addr = allocate_ipv_4addr
        # The IPv6 address allocated to the IPv6 Translation Service instance.
        self.allocate_ipv_6addr = allocate_ipv_6addr
        # The business status of the IPv6 Translation Service instance. Valid values:
        # 
        # *   **Normal**
        # *   **FinancialLocked**
        self.business_status = business_status
        # The ID of the IPv6 Translation Service instance.
        self.ipv_6translator_id = ipv_6translator_id
        # The name of the IPv6 Translation Service instance.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The billing method of the IPv6 Translation Service instance. Valid values:
        # 
        # *   **Prepay**: subscription
        # *   **Postpay**: pay-as-you-go
        self.pay_type = pay_type
        # The region of the IPv6 Translation Service instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The specification of the IPv6 Translation Service instance. Set the value to **small**.
        self.spec = spec
        # The status of the IPv6 Translation Service instance. Valid values:
        # 
        # *   **init**
        # *   **provisioning**
        # *   **active**
        # *   **updating**
        # *   **upgrading**
        # *   **deleting**
        # *   **deleted**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocate_ipv_4addr is not None:
            result['AllocateIpv4Addr'] = self.allocate_ipv_4addr

        if self.allocate_ipv_6addr is not None:
            result['AllocateIpv6Addr'] = self.allocate_ipv_6addr

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.ipv_6translator_id is not None:
            result['Ipv6TranslatorId'] = self.ipv_6translator_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocateIpv4Addr') is not None:
            self.allocate_ipv_4addr = m.get('AllocateIpv4Addr')

        if m.get('AllocateIpv6Addr') is not None:
            self.allocate_ipv_6addr = m.get('AllocateIpv6Addr')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('Ipv6TranslatorId') is not None:
            self.ipv_6translator_id = m.get('Ipv6TranslatorId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

