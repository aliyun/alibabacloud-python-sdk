# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateAndAttachPolicyRequest(DaraModel):
    def __init__(
        self,
        attach_resource_ids: List[str] = None,
        attach_resource_type: str = None,
        config: str = None,
        description: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        name: str = None,
    ):
        # The association IDs.
        # 
        # This parameter is required.
        self.attach_resource_ids = attach_resource_ids
        # The supported associated resource type. Valid values:
        # 
        # *   HttpApi: an HTTP API
        # *   Operation: an operation in an HTTP API
        # *   GatewayRoute: a route
        # *   GatewayService: a service
        # *   GatewayServicePort: a service port
        # *   Domain: a domain name
        # *   Gateway: an instance
        # 
        # This parameter is required.
        self.attach_resource_type = attach_resource_type
        # The policy configurations. The value is a JSON string.
        # 
        # This parameter is required.
        self.config = config
        # The policy description.
        self.description = description
        # The environment ID.
        self.environment_id = environment_id
        # The instance ID.
        self.gateway_id = gateway_id
        # The policy name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_resource_ids is not None:
            result['attachResourceIds'] = self.attach_resource_ids

        if self.attach_resource_type is not None:
            result['attachResourceType'] = self.attach_resource_type

        if self.config is not None:
            result['config'] = self.config

        if self.description is not None:
            result['description'] = self.description

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceIds') is not None:
            self.attach_resource_ids = m.get('attachResourceIds')

        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

