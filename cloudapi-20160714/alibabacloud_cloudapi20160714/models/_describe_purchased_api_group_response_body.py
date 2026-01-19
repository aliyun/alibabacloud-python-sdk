# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribePurchasedApiGroupResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        domains: main_models.DescribePurchasedApiGroupResponseBodyDomains = None,
        group_id: str = None,
        group_name: str = None,
        purchased_time: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The description of the API group.
        self.description = description
        # The list of domain names.
        self.domains = domains
        # The ID of the API group.
        self.group_id = group_id
        # The name of the API group.
        self.group_name = group_name
        # The time when the API group was purchased.
        self.purchased_time = purchased_time
        # The region where the API group is located.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The status of the API group.
        # 
        # *   **NORMAL**: The API group is normal.
        # *   **DELETE**: The API group is deleted.
        self.status = status

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.domains is not None:
            result['Domains'] = self.domains.to_map()

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.purchased_time is not None:
            result['PurchasedTime'] = self.purchased_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Domains') is not None:
            temp_model = main_models.DescribePurchasedApiGroupResponseBodyDomains()
            self.domains = temp_model.from_map(m.get('Domains'))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('PurchasedTime') is not None:
            self.purchased_time = m.get('PurchasedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribePurchasedApiGroupResponseBodyDomains(DaraModel):
    def __init__(
        self,
        domain_item: List[main_models.DescribePurchasedApiGroupResponseBodyDomainsDomainItem] = None,
    ):
        self.domain_item = domain_item

    def validate(self):
        if self.domain_item:
            for v1 in self.domain_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainItem'] = []
        if self.domain_item is not None:
            for k1 in self.domain_item:
                result['DomainItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_item = []
        if m.get('DomainItem') is not None:
            for k1 in m.get('DomainItem'):
                temp_model = main_models.DescribePurchasedApiGroupResponseBodyDomainsDomainItem()
                self.domain_item.append(temp_model.from_map(k1))

        return self

class DescribePurchasedApiGroupResponseBodyDomainsDomainItem(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # The domain name.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        return self

