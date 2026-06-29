# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPolicyClassesRequest(DaraModel):
    def __init__(
        self,
        attach_resource_id: str = None,
        attach_resource_type: str = None,
        direction: str = None,
        gateway_id: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # The ID of the attached resource.
        self.attach_resource_id = attach_resource_id
        # The type of resource that the policy can be attached to. Valid values:
        # - HttpApi: HttpApi.
        # - Operation: an operation of an HttpApi.
        # - GatewayRoute: a gateway route.
        # - GatewayService: a gateway service.
        # - GatewayServicePort: a gateway service port.
        # - Domain: a gateway domain name.
        # - Gateway: a gateway.
        self.attach_resource_type = attach_resource_type
        # The direction of the policy. Valid values:
        # - OutBound: outbound.
        # - InBound: inbound.
        # - Both: both directions.
        self.direction = direction
        # The gateway ID.
        self.gateway_id = gateway_id
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The policy templatetype.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_resource_id is not None:
            result['attachResourceId'] = self.attach_resource_id

        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type

        if self.direction is not None:
            result['direction'] = self.direction

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceId') is not None:
            self.attach_resource_id = m.get('attachResourceId')

        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

