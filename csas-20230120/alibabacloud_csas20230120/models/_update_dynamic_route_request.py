# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateDynamicRouteRequest(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        description: str = None,
        dynamic_route_id: str = None,
        dynamic_route_type: str = None,
        modify_type: str = None,
        name: str = None,
        next_hop: str = None,
        priority: int = None,
        region_ids: List[str] = None,
        status: str = None,
        tag_ids: List[str] = None,
    ):
        # A collection of private network access application IDs for the dynamic route. You can specify up to 200 IDs. This parameter is required when **ApplicationType** is set to **Application**. Specify either this parameter or **TagIds**, but not both. Do not specify this parameter when **ApplicationType** is set to **All**.
        self.application_ids = application_ids
        # The application type of the dynamic route. Valid values:
        # 
        # - **All**: All applications.
        # 
        # - **Application**: Application.
        # 
        # - **Tag**: Tag.
        self.application_type = application_type
        # The description of the dynamic route. The description must be 1 to 128 characters long and can contain letters, digits, periods (.), underscores (_), hyphens (-), and spaces.
        self.description = description
        # The ID of the dynamic route.
        # 
        # This parameter is required.
        self.dynamic_route_id = dynamic_route_id
        # The type of the dynamic route. Valid value: **connector**: leased line.
        self.dynamic_route_type = dynamic_route_type
        # The modification type of the dynamic route. Valid values:
        # 
        # - **Cover** (default): Use the values of **RegionIds**, **ApplicationIds**, and **TagIds** to overwrite the existing regions, private network access application IDs, and private network access tag IDs supported by the SASE POP cluster access points.
        # 
        # - **Append**: Add the values specified in **RegionIds**, **ApplicationIds**, and **TagIds** to the existing regions, private network access application IDs, and private network access tag IDs supported by the SASE POP cluster access points.
        self.modify_type = modify_type
        # The name of the dynamic route. The name must be 1 to 128 characters long and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The next hop instance ID of the dynamic route. To get valid values, see:
        # 
        # - [ListConnectors](~~ListConnectors~~): Query connectors in bulk.
        self.next_hop = next_hop
        # The route priority. A value of 1 indicates the highest priority. Valid values: 1 to 99.
        self.priority = priority
        # A list of regions supported by the SASE POP cluster access points.
        self.region_ids = region_ids
        # The status of the dynamic route. Valid values:
        # 
        # - **Enabled**: Enable the route.
        # 
        # - **Disabled**: Disable the route.
        self.status = status
        # A collection of private network access tag IDs for the dynamic route. You can specify up to 40 IDs. This parameter is required when **ApplicationType** is set to **Tag**. Specify either this parameter or **ApplicationIds**, but not both. Do not specify this parameter when **ApplicationType** is set to **All**.
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

        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id

        if self.dynamic_route_type is not None:
            result['DynamicRouteType'] = self.dynamic_route_type

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

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

        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')

        if m.get('DynamicRouteType') is not None:
            self.dynamic_route_type = m.get('DynamicRouteType')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

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

