# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetRouteResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        route: main_models.GetRouteResponseBodyRoute = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the route.
        self.route = route
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.route:
            self.route.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.route is not None:
            result['Route'] = self.route.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Route') is not None:
            temp_model = main_models.GetRouteResponseBodyRoute()
            self.route = temp_model.from_map(m.get('Route'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRouteResponseBodyRoute(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        destination_cidr: str = None,
        id: int = None,
        network_id: int = None,
        resource_group_id: str = None,
        resource_id: str = None,
    ):
        # The time when the route was created. The value is a 64-bit timestamp.
        self.create_time = create_time
        # The CIDR block of the destination-based route.
        self.destination_cidr = destination_cidr
        # The route ID.
        self.id = id
        # The network ID.
        self.network_id = network_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The network resource ID.
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

