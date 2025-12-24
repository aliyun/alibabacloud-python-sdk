# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveUserDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: main_models.DescribeLiveUserDomainsResponseBodyDomains = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The domain names.
        self.domains = domains
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()

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
        if m.get('Domains') is not None:
            temp_model = main_models.DescribeLiveUserDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m.get('Domains'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLiveUserDomainsResponseBodyDomains(DaraModel):
    def __init__(
        self,
        page_data: List[main_models.DescribeLiveUserDomainsResponseBodyDomainsPageData] = None,
    ):
        self.page_data = page_data

    def validate(self):
        if self.page_data:
            for v1 in self.page_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PageData'] = []
        if self.page_data is not None:
            for k1 in self.page_data:
                result['PageData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k1 in m.get('PageData'):
                temp_model = main_models.DescribeLiveUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k1))

        return self

class DescribeLiveUserDomainsResponseBodyDomainsPageData(DaraModel):
    def __init__(
        self,
        cname: str = None,
        description: str = None,
        domain_name: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        live_domain_status: str = None,
        live_domain_type: str = None,
        region_name: str = None,
        resource_group_id: str = None,
    ):
        # The CNAME generated for the domain name.
        self.cname = cname
        # The description.
        self.description = description
        # The domain name.
        self.domain_name = domain_name
        # The time when the domain name was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.gmt_created = gmt_created
        # The time when the domain name was last modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The status of the domain name. Valid values:
        # 
        # *   **online**
        # *   **offline**
        # *   **configuring**
        self.live_domain_status = live_domain_status
        # The type of the domain name. Valid values:
        # 
        # *   **liveVideo**: streaming domain
        # *   **liveEdge**: ingest domain
        self.live_domain_type = live_domain_type
        # The ID of the region in which the domain name resides.
        self.region_name = region_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.live_domain_status is not None:
            result['LiveDomainStatus'] = self.live_domain_status

        if self.live_domain_type is not None:
            result['LiveDomainType'] = self.live_domain_type

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LiveDomainStatus') is not None:
            self.live_domain_status = m.get('LiveDomainStatus')

        if m.get('LiveDomainType') is not None:
            self.live_domain_type = m.get('LiveDomainType')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

