# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListRoutesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListRoutesResponseBodyPagingInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The ID of the request. It is used to locate logs and troubleshoot problems.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListRoutesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRoutesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        route_list: List[main_models.ListRoutesResponseBodyPagingInfoRouteList] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of network resource routing information obtained.
        self.route_list = route_list
        # All data entries
        self.total_count = total_count

    def validate(self):
        if self.route_list:
            for v1 in self.route_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['RouteList'] = []
        if self.route_list is not None:
            for k1 in self.route_list:
                result['RouteList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.route_list = []
        if m.get('RouteList') is not None:
            for k1 in m.get('RouteList'):
                temp_model = main_models.ListRoutesResponseBodyPagingInfoRouteList()
                self.route_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRoutesResponseBodyPagingInfoRouteList(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        destination_cidr: str = None,
        id: int = None,
        network_id: int = None,
        resource_group_id: str = None,
        resource_id: str = None,
    ):
        # The creation time, which is a 64-bit timestamp.
        self.create_time = create_time
        # Route destination CIDR
        self.destination_cidr = destination_cidr
        # Route ID
        self.id = id
        # Network Resource ID
        self.network_id = network_id
        # Unique identifier of the resource group to which it belongs
        self.resource_group_id = resource_group_id
        # Unique identifier of network resource
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.id is not None:
            result['Id'] = self.id

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

