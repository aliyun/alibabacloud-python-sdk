# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterMulticastDomainsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        transit_router_multicast_domains: List[main_models.ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomains] = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The list of multicast domains.
        self.transit_router_multicast_domains = transit_router_multicast_domains

    def validate(self):
        if self.transit_router_multicast_domains:
            for v1 in self.transit_router_multicast_domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TransitRouterMulticastDomains'] = []
        if self.transit_router_multicast_domains is not None:
            for k1 in self.transit_router_multicast_domains:
                result['TransitRouterMulticastDomains'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.transit_router_multicast_domains = []
        if m.get('TransitRouterMulticastDomains') is not None:
            for k1 in m.get('TransitRouterMulticastDomains'):
                temp_model = main_models.ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomains()
                self.transit_router_multicast_domains.append(temp_model.from_map(k1))

        return self

class ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomains(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        options: main_models.ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomainsOptions = None,
        region_id: str = None,
        status: str = None,
        tags: List[main_models.ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomainsTags] = None,
        transit_router_id: str = None,
        transit_router_multicast_domain_description: str = None,
        transit_router_multicast_domain_id: str = None,
        transit_router_multicast_domain_name: str = None,
    ):
        # The CEN instance ID.
        self.cen_id = cen_id
        # Multicast domain feature.
        self.options = options
        # The region ID of the transit router.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        self.region_id = region_id
        # The status of the multicast domain.
        # 
        # The valid value is **Active**, which indicates that the multicast domain is available.
        self.status = status
        # The tags.
        self.tags = tags
        # The transit router ID.
        self.transit_router_id = transit_router_id
        # The description of the multicast domain.
        self.transit_router_multicast_domain_description = transit_router_multicast_domain_description
        # The ID of the multicast domain.
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id
        # The name of the multicast domain.
        self.transit_router_multicast_domain_name = transit_router_multicast_domain_name

    def validate(self):
        if self.options:
            self.options.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.options is not None:
            result['Options'] = self.options.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_multicast_domain_description is not None:
            result['TransitRouterMulticastDomainDescription'] = self.transit_router_multicast_domain_description

        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id

        if self.transit_router_multicast_domain_name is not None:
            result['TransitRouterMulticastDomainName'] = self.transit_router_multicast_domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('Options') is not None:
            temp_model = main_models.ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomainsOptions()
            self.options = temp_model.from_map(m.get('Options'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomainsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterMulticastDomainDescription') is not None:
            self.transit_router_multicast_domain_description = m.get('TransitRouterMulticastDomainDescription')

        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')

        if m.get('TransitRouterMulticastDomainName') is not None:
            self.transit_router_multicast_domain_name = m.get('TransitRouterMulticastDomainName')

        return self

class ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomainsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class ListTransitRouterMulticastDomainsResponseBodyTransitRouterMulticastDomainsOptions(DaraModel):
    def __init__(
        self,
        igmpv_2support: str = None,
    ):
        # Indicates whether the IGMP feature is enabled for the multicast domain.
        self.igmpv_2support = igmpv_2support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.igmpv_2support is not None:
            result['Igmpv2Support'] = self.igmpv_2support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Igmpv2Support') is not None:
            self.igmpv_2support = m.get('Igmpv2Support')

        return self

