# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeIPv6TranslatorsResponseBody(DaraModel):
    def __init__(
        self,
        ipv_6translators: main_models.DescribeIPv6TranslatorsResponseBodyIpv6Translators = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of IPv6 Translation Service instances.
        self.ipv_6translators = ipv_6translators
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.ipv_6translators:
            self.ipv_6translators.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6translators is not None:
            result['Ipv6Translators'] = self.ipv_6translators.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Translators') is not None:
            temp_model = main_models.DescribeIPv6TranslatorsResponseBodyIpv6Translators()
            self.ipv_6translators = temp_model.from_map(m.get('Ipv6Translators'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeIPv6TranslatorsResponseBodyIpv6Translators(DaraModel):
    def __init__(
        self,
        ipv_6translator: List[main_models.DescribeIPv6TranslatorsResponseBodyIpv6TranslatorsIpv6Translator] = None,
    ):
        self.ipv_6translator = ipv_6translator

    def validate(self):
        if self.ipv_6translator:
            for v1 in self.ipv_6translator:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6Translator'] = []
        if self.ipv_6translator is not None:
            for k1 in self.ipv_6translator:
                result['Ipv6Translator'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6translator = []
        if m.get('Ipv6Translator') is not None:
            for k1 in m.get('Ipv6Translator'):
                temp_model = main_models.DescribeIPv6TranslatorsResponseBodyIpv6TranslatorsIpv6Translator()
                self.ipv_6translator.append(temp_model.from_map(k1))

        return self

class DescribeIPv6TranslatorsResponseBodyIpv6TranslatorsIpv6Translator(DaraModel):
    def __init__(
        self,
        allocate_ipv_4addr: str = None,
        allocate_ipv_6addr: str = None,
        available_bandwidth: str = None,
        bandwidth: int = None,
        business_status: str = None,
        create_time: int = None,
        description: str = None,
        end_time: int = None,
        ipv_6translator_entry_ids: main_models.DescribeIPv6TranslatorsResponseBodyIpv6TranslatorsIpv6TranslatorIpv6TranslatorEntryIds = None,
        ipv_6translator_id: str = None,
        name: str = None,
        pay_type: str = None,
        region_id: str = None,
        spec: str = None,
        status: str = None,
    ):
        # The IPv4 address allocated to the IPv6 Translation Service instance.
        self.allocate_ipv_4addr = allocate_ipv_4addr
        # The IPv6 address allocated to the IPv6 Translation Service instance.
        self.allocate_ipv_6addr = allocate_ipv_6addr
        # The bandwidth of the IPv6 Translation Service instance.
        self.available_bandwidth = available_bandwidth
        # The bandwidth of the IPv6 Translation Service instance. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The business status of the IPv6 Translation Service instance. Valid values:
        # 
        # *   **Normal**
        # *   **FinancialLocked**
        self.business_status = business_status
        # The timestamp when the IPv6 Translation Service instance was created.
        self.create_time = create_time
        # The description of the IPv6 Translation Service instance.
        self.description = description
        # The timestamp when IPv6 Translation Service instance expires.
        self.end_time = end_time
        # The IDs of IPv6 mapping entries of the IPv6 Translation Service instance.
        self.ipv_6translator_entry_ids = ipv_6translator_entry_ids
        # The ID of the IPv6 Translation Service instance.
        self.ipv_6translator_id = ipv_6translator_id
        # The name of the IPv6 Translation Service instance.
        self.name = name
        # The billing method of the IPv6 Translation Service instance.
        # 
        # *   **Prepay**: subscription
        # *   **Postpay**: pay-as-you-go
        self.pay_type = pay_type
        # The region of the IPv6 Translation Service instance.
        self.region_id = region_id
        # The specification of the IPv6 Translation Service instance.
        self.spec = spec
        # The status of the IPv6 Translation Service instance.
        self.status = status

    def validate(self):
        if self.ipv_6translator_entry_ids:
            self.ipv_6translator_entry_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocate_ipv_4addr is not None:
            result['AllocateIpv4Addr'] = self.allocate_ipv_4addr

        if self.allocate_ipv_6addr is not None:
            result['AllocateIpv6Addr'] = self.allocate_ipv_6addr

        if self.available_bandwidth is not None:
            result['AvailableBandwidth'] = self.available_bandwidth

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ipv_6translator_entry_ids is not None:
            result['Ipv6TranslatorEntryIds'] = self.ipv_6translator_entry_ids.to_map()

        if self.ipv_6translator_id is not None:
            result['Ipv6TranslatorId'] = self.ipv_6translator_id

        if self.name is not None:
            result['Name'] = self.name

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('AvailableBandwidth') is not None:
            self.available_bandwidth = m.get('AvailableBandwidth')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Ipv6TranslatorEntryIds') is not None:
            temp_model = main_models.DescribeIPv6TranslatorsResponseBodyIpv6TranslatorsIpv6TranslatorIpv6TranslatorEntryIds()
            self.ipv_6translator_entry_ids = temp_model.from_map(m.get('Ipv6TranslatorEntryIds'))

        if m.get('Ipv6TranslatorId') is not None:
            self.ipv_6translator_id = m.get('Ipv6TranslatorId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeIPv6TranslatorsResponseBodyIpv6TranslatorsIpv6TranslatorIpv6TranslatorEntryIds(DaraModel):
    def __init__(
        self,
        ipv_6translator_entry_id: List[str] = None,
    ):
        self.ipv_6translator_entry_id = ipv_6translator_entry_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6translator_entry_id is not None:
            result['Ipv6TranslatorEntryId'] = self.ipv_6translator_entry_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6TranslatorEntryId') is not None:
            self.ipv_6translator_entry_id = m.get('Ipv6TranslatorEntryId')

        return self

