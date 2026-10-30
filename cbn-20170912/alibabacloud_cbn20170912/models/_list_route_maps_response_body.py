# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListRouteMapsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        route_maps: List[main_models.ListRouteMapsResponseBodyRouteMaps] = None,
        total_count: int = None,
    ):
        # The number of entries returned on each page. Default value: **20**.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - If **NextToken** is empty, no next query is available.
        # - If **NextToken** returns a value, the value is the token for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information about the route maps.
        self.route_maps = route_maps
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.route_maps:
            for v1 in self.route_maps:
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

        result['RouteMaps'] = []
        if self.route_maps is not None:
            for k1 in self.route_maps:
                result['RouteMaps'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.route_maps = []
        if m.get('RouteMaps') is not None:
            for k1 in m.get('RouteMaps'):
                temp_model = main_models.ListRouteMapsResponseBodyRouteMaps()
                self.route_maps.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRouteMapsResponseBodyRouteMaps(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        direction: str = None,
        name: str = None,
        priority: int = None,
        resource_group_id: str = None,
        route_map_id: str = None,
        status: str = None,
        tag: List[main_models.ListRouteMapsResponseBodyRouteMapsTag] = None,
        version: int = None,
    ):
        # The time when the route map was created.
        # 
        # The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mmZ` format. The time is displayed in UTC.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.creation_time = creation_time
        # The description of the route map.
        self.description = description
        # The direction of the route map. Valid values: 
        # - Inbound: inbound.
        # - Outbound: outbound.
        self.direction = direction
        # The name of the route map.
        self.name = name
        # The priority of the route map. A smaller value indicates a higher priority.
        self.priority = priority
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the route map.
        self.route_map_id = route_map_id
        # The status of the route map. Valid values:
        # 
        # - **Creating**: The route map is being created.
        # - **Updating**: The route map is being updated.
        # - **Active**: The route map is available.
        # - **Deleting**: The route map is being deleted.
        self.status = status
        # The list of tags.
        self.tag = tag
        # The version number of the route map configuration.
        # The version number increases each time the route map and its associated route map rules are modified.
        self.version = version

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListRouteMapsResponseBodyRouteMapsTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListRouteMapsResponseBodyRouteMapsTag(DaraModel):
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

