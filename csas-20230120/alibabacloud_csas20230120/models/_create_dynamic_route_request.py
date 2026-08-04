# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateDynamicRouteRequest(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        description: str = None,
        dynamic_route_type: str = None,
        name: str = None,
        next_hop: str = None,
        priority: int = None,
        region_ids: List[str] = None,
        status: str = None,
        tag_ids: List[str] = None,
    ):
        # A collection of internal network access application IDs for the dynamic route. You can enter a maximum of 200 internal network access application IDs. Required when ApplicationType is **Application**. Choose one of **ApplicationIds** or **TagIds**. Do not enter when **ApplicationType** is **All**.
        self.application_ids = application_ids
        # The application type of the dynamic route. Valid values:
        # 
        # - **All**: All applications.
        # 
        # - **Application**: Application.
        # 
        # - **Tag**: Tag.
        # 
        # This parameter is required.
        self.application_type = application_type
        # The dynamic route description. It is 1 to 128 characters long. It supports Chinese characters, uppercase and lowercase letters, numbers, periods (.), underscores (_), hyphens (-), and spaces.
        self.description = description
        # The dynamic route type. Valid values: **connector**: Leased line.
        # 
        # This parameter is required.
        self.dynamic_route_type = dynamic_route_type
        # The dynamic route name. It is 1 to 128 characters long. It supports Chinese characters, uppercase and lowercase letters, numbers, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.name = name
        # The next hop instance ID of the dynamic route. Source:
        # 
        # - For more information, see [ListConnectors](): Query Connectors in batches.
        # 
        # This parameter is required.
        self.next_hop = next_hop
        # The dynamic route priority. 1 indicates the highest priority. Valid values: 1-99.
        # 
        # This parameter is required.
        self.priority = priority
        # A list of regions supported by SASE POP cluster access points.
        # 
        # This parameter is required.
        self.region_ids = region_ids
        # The dynamic route status. Valid values:
        # 
        # - **Enabled**: Enabled.
        # 
        # - **Disabled**: Disabled.
        # 
        # This parameter is required.
        self.status = status
        # A collection of internal network access tag IDs for the dynamic route. You can enter a maximum of 40 internal network access tag IDs. Required when ApplicationType is **Tag**. Choose one of **ApplicationIds** or **TagIds**. Do not enter when **ApplicationType** is **All**.
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.description is not None:
            result['Description'] = self.description

        if self.dynamic_route_type is not None:
            result['DynamicRouteType'] = self.dynamic_route_type

        if self.name is not None:
            result['Name'] = self.name

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DynamicRouteType') is not None:
            self.dynamic_route_type = m.get('DynamicRouteType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')

        return self

