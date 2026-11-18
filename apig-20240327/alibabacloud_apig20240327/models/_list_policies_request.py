# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPoliciesRequest(DaraModel):
    def __init__(
        self,
        attach_resource_id: str = None,
        attach_resource_type: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        page_number: int = None,
        page_size: int = None,
        with_attachments: bool = None,
        with_system_policy: bool = None,
    ):
        # The ID of the mount point.
        self.attach_resource_id = attach_resource_id
        # The type of mount points supported by the policy. Valid values:
        # - HttpApi: HTTP API.
        # - Operation: The operation of the HTTP API.
        # - GatewayRoute: Gateway route.
        # - GatewayService: Gateway service.
        # - GatewayServicePort: Gateway service port.
        # - Domain: Gateway domain name.
        # - Gateway: Gateway.
        self.attach_resource_type = attach_resource_type
        # The ID of the environment.
        self.environment_id = environment_id
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The page number. Pages start from 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # Specifies whether to return mount information.
        self.with_attachments = with_attachments
        # Specifies whether the policy is a system policy.
        self.with_system_policy = with_system_policy

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

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.with_attachments is not None:
            result['withAttachments'] = self.with_attachments

        if self.with_system_policy is not None:
            result['withSystemPolicy'] = self.with_system_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceId') is not None:
            self.attach_resource_id = m.get('attachResourceId')

        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('withAttachments') is not None:
            self.with_attachments = m.get('withAttachments')

        if m.get('withSystemPolicy') is not None:
            self.with_system_policy = m.get('withSystemPolicy')

        return self

