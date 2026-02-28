# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeBgpGroupsResponseBody(DaraModel):
    def __init__(
        self,
        bgp_groups: main_models.DescribeBgpGroupsResponseBodyBgpGroups = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.bgp_groups = bgp_groups
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.bgp_groups:
            self.bgp_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bgp_groups is not None:
            result['BgpGroups'] = self.bgp_groups.to_map()

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
        if m.get('BgpGroups') is not None:
            temp_model = main_models.DescribeBgpGroupsResponseBodyBgpGroups()
            self.bgp_groups = temp_model.from_map(m.get('BgpGroups'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBgpGroupsResponseBodyBgpGroups(DaraModel):
    def __init__(
        self,
        bgp_group: List[main_models.DescribeBgpGroupsResponseBodyBgpGroupsBgpGroup] = None,
    ):
        self.bgp_group = bgp_group

    def validate(self):
        if self.bgp_group:
            for v1 in self.bgp_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BgpGroup'] = []
        if self.bgp_group is not None:
            for k1 in self.bgp_group:
                result['BgpGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bgp_group = []
        if m.get('BgpGroup') is not None:
            for k1 in m.get('BgpGroup'):
                temp_model = main_models.DescribeBgpGroupsResponseBodyBgpGroupsBgpGroup()
                self.bgp_group.append(temp_model.from_map(k1))

        return self

class DescribeBgpGroupsResponseBodyBgpGroupsBgpGroup(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        bgp_group_id: str = None,
        description: str = None,
        hold: str = None,
        ip_version: str = None,
        is_fake: str = None,
        keepalive: str = None,
        local_asn: str = None,
        name: str = None,
        peer_asn: str = None,
        region_id: str = None,
        route_limit: str = None,
        router_id: str = None,
        status: str = None,
    ):
        self.auth_key = auth_key
        self.bgp_group_id = bgp_group_id
        self.description = description
        self.hold = hold
        self.ip_version = ip_version
        self.is_fake = is_fake
        self.keepalive = keepalive
        self.local_asn = local_asn
        self.name = name
        self.peer_asn = peer_asn
        self.region_id = region_id
        self.route_limit = route_limit
        self.router_id = router_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.bgp_group_id is not None:
            result['BgpGroupId'] = self.bgp_group_id

        if self.description is not None:
            result['Description'] = self.description

        if self.hold is not None:
            result['Hold'] = self.hold

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.is_fake is not None:
            result['IsFake'] = self.is_fake

        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive

        if self.local_asn is not None:
            result['LocalAsn'] = self.local_asn

        if self.name is not None:
            result['Name'] = self.name

        if self.peer_asn is not None:
            result['PeerAsn'] = self.peer_asn

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.route_limit is not None:
            result['RouteLimit'] = self.route_limit

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('BgpGroupId') is not None:
            self.bgp_group_id = m.get('BgpGroupId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Hold') is not None:
            self.hold = m.get('Hold')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IsFake') is not None:
            self.is_fake = m.get('IsFake')

        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')

        if m.get('LocalAsn') is not None:
            self.local_asn = m.get('LocalAsn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PeerAsn') is not None:
            self.peer_asn = m.get('PeerAsn')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteLimit') is not None:
            self.route_limit = m.get('RouteLimit')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

