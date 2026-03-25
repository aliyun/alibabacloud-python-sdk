# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeRouteServicesInCenResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        route_service_entries: main_models.DescribeRouteServicesInCenResponseBodyRouteServiceEntries = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        self.route_service_entries = route_service_entries
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.route_service_entries:
            self.route_service_entries.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.route_service_entries is not None:
            result['RouteServiceEntries'] = self.route_service_entries.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouteServiceEntries') is not None:
            temp_model = main_models.DescribeRouteServicesInCenResponseBodyRouteServiceEntries()
            self.route_service_entries = temp_model.from_map(m.get('RouteServiceEntries'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRouteServicesInCenResponseBodyRouteServiceEntries(DaraModel):
    def __init__(
        self,
        route_service_entry: List[main_models.DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntry] = None,
    ):
        self.route_service_entry = route_service_entry

    def validate(self):
        if self.route_service_entry:
            for v1 in self.route_service_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RouteServiceEntry'] = []
        if self.route_service_entry is not None:
            for k1 in self.route_service_entry:
                result['RouteServiceEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_service_entry = []
        if m.get('RouteServiceEntry') is not None:
            for k1 in m.get('RouteServiceEntry'):
                temp_model = main_models.DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntry()
                self.route_service_entry.append(temp_model.from_map(k1))

        return self

class DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntry(DaraModel):
    def __init__(
        self,
        access_region_id: str = None,
        cen_id: str = None,
        cidrs: main_models.DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntryCidrs = None,
        description: str = None,
        host: str = None,
        host_region_id: str = None,
        host_vpc_id: str = None,
        status: str = None,
    ):
        self.access_region_id = access_region_id
        self.cen_id = cen_id
        self.cidrs = cidrs
        self.description = description
        self.host = host
        self.host_region_id = host_region_id
        self.host_vpc_id = host_vpc_id
        self.status = status

    def validate(self):
        if self.cidrs:
            self.cidrs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.host is not None:
            result['Host'] = self.host

        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id

        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('Cidrs') is not None:
            temp_model = main_models.DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntryCidrs()
            self.cidrs = temp_model.from_map(m.get('Cidrs'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')

        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntryCidrs(DaraModel):
    def __init__(
        self,
        cidr: List[str] = None,
    ):
        self.cidr = cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        return self

