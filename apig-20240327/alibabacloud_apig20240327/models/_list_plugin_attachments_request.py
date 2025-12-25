# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPluginAttachmentsRequest(DaraModel):
    def __init__(
        self,
        attach_resource_id: str = None,
        attach_resource_type: str = None,
        attach_resource_types: str = None,
        environment_id: str = None,
        gateway_id: str = None,
        page_number: int = None,
        page_size: int = None,
        plugin_id: str = None,
        with_parent_resource: bool = None,
    ):
        # The resource attachment ID.
        self.attach_resource_id = attach_resource_id
        # The resource attachment type (not yet in use).
        self.attach_resource_type = attach_resource_type
        # The resource attachment types, separated by commas.
        self.attach_resource_types = attach_resource_types
        # The environment ID.
        self.environment_id = environment_id
        # The gateway ID.
        self.gateway_id = gateway_id
        # The page number to return. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The plug-in ID.
        self.plugin_id = plugin_id
        # Specifies whether to return parent resource attachments.
        self.with_parent_resource = with_parent_resource

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

        if self.attach_resource_types is not None:
            result['attachResourceTypes'] = self.attach_resource_types

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.plugin_id is not None:
            result['pluginId'] = self.plugin_id

        if self.with_parent_resource is not None:
            result['withParentResource'] = self.with_parent_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceId') is not None:
            self.attach_resource_id = m.get('attachResourceId')

        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('attachResourceTypes') is not None:
            self.attach_resource_types = m.get('attachResourceTypes')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('pluginId') is not None:
            self.plugin_id = m.get('pluginId')

        if m.get('withParentResource') is not None:
            self.with_parent_resource = m.get('withParentResource')

        return self

