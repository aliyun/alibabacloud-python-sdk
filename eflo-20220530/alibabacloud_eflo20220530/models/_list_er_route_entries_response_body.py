# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListErRouteEntriesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.ListErRouteEntriesResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The error message. (If the instance is in the Exception state, the exception cause is prompted.)
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Content') is not None:
            temp_model = main_models.ListErRouteEntriesResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListErRouteEntriesResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListErRouteEntriesResponseBodyContentData] = None,
        total: int = None,
    ):
        # Lingjun HUB Route Entry Information List
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListErRouteEntriesResponseBodyContentData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListErRouteEntriesResponseBodyContentData(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        er_id: str = None,
        er_route_entry_id: str = None,
        gmt_modified: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_tenant_id: str = None,
        route_type: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB Instance ID
        self.er_id = er_id
        # The ID of the route entry.
        self.er_route_entry_id = er_route_entry_id
        # The time when the cluster was updated.
        self.gmt_modified = gmt_modified
        # Next Hop Instance
        self.next_hop_id = next_hop_id
        # Next Hop Instance Type
        self.next_hop_type = next_hop_type
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant to which the resource belongs.
        self.resource_tenant_id = resource_tenant_id
        # Route type
        self.route_type = route_type
        # The task status. Valid values:
        # 
        # *   Synchronizing
        # *   Available
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.er_route_entry_id is not None:
            result['ErRouteEntryId'] = self.er_route_entry_id

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_tenant_id is not None:
            result['ResourceTenantId'] = self.resource_tenant_id

        if self.route_type is not None:
            result['RouteType'] = self.route_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ErRouteEntryId') is not None:
            self.er_route_entry_id = m.get('ErRouteEntryId')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceTenantId') is not None:
            self.resource_tenant_id = m.get('ResourceTenantId')

        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

