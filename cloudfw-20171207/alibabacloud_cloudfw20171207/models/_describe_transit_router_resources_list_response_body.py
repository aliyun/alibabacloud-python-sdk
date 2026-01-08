# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeTransitRouterResourcesListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        transit_router_attached_resources: List[main_models.DescribeTransitRouterResourcesListResponseBodyTransitRouterAttachedResources] = None,
    ):
        self.request_id = request_id
        self.transit_router_attached_resources = transit_router_attached_resources

    def validate(self):
        if self.transit_router_attached_resources:
            for v1 in self.transit_router_attached_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TransitRouterAttachedResources'] = []
        if self.transit_router_attached_resources is not None:
            for k1 in self.transit_router_attached_resources:
                result['TransitRouterAttachedResources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.transit_router_attached_resources = []
        if m.get('TransitRouterAttachedResources') is not None:
            for k1 in m.get('TransitRouterAttachedResources'):
                temp_model = main_models.DescribeTransitRouterResourcesListResponseBodyTransitRouterAttachedResources()
                self.transit_router_attached_resources.append(temp_model.from_map(k1))

        return self

class DescribeTransitRouterResourcesListResponseBodyTransitRouterAttachedResources(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

