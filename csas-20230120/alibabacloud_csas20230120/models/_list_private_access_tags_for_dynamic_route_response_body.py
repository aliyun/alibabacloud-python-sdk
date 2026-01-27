# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListPrivateAccessTagsForDynamicRouteResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_routes: List[main_models.ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutes] = None,
        request_id: str = None,
    ):
        self.dynamic_routes = dynamic_routes
        self.request_id = request_id

    def validate(self):
        if self.dynamic_routes:
            for v1 in self.dynamic_routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DynamicRoutes'] = []
        if self.dynamic_routes is not None:
            for k1 in self.dynamic_routes:
                result['DynamicRoutes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dynamic_routes = []
        if m.get('DynamicRoutes') is not None:
            for k1 in m.get('DynamicRoutes'):
                temp_model = main_models.ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutes()
                self.dynamic_routes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutes(DaraModel):
    def __init__(
        self,
        dynamic_route_id: str = None,
        tags: List[main_models.ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutesTags] = None,
    ):
        self.dynamic_route_id = dynamic_route_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_route_id is not None:
            result['DynamicRouteId'] = self.dynamic_route_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicRouteId') is not None:
            self.dynamic_route_id = m.get('DynamicRouteId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListPrivateAccessTagsForDynamicRouteResponseBodyDynamicRoutesTags(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        tag_id: str = None,
        tag_type: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.tag_id = tag_id
        self.tag_type = tag_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_type is not None:
            result['TagType'] = self.tag_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')

        return self

