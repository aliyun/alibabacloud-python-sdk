# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPluginsRequest(DaraModel):
    def __init__(
        self,
        attach_resource_id: str = None,
        attach_resource_type: str = None,
        gateway_id: str = None,
        gateway_type: str = None,
        include_builtin_ai_gateway: bool = None,
        page_number: int = None,
        page_size: int = None,
        plugin_class_id: str = None,
        plugin_class_name: str = None,
        with_attachment_info: bool = None,
    ):
        # The resource attachment ID.
        self.attach_resource_id = attach_resource_id
        # The resource attachment type.
        # 
        # - HttpApi: HttpApi.
        # - Operation: Operation of HttpApi.
        # - GatewayRoute: Gateway route.
        # - GatewayService: Gateway service.
        # - GatewayServicePort: Gateway service port.
        # - Domain: Gateway domain.
        # - Gateway: Gateway.
        self.attach_resource_type = attach_resource_type
        # The gateway instance ID for filtering.
        self.gateway_id = gateway_id
        # The instance type. Valid values: **AI** and **API**.
        self.gateway_type = gateway_type
        # Specifies whether to include built-in AI plug-ins in the returned results. Default: false.
        self.include_builtin_ai_gateway = include_builtin_ai_gateway
        # The page number to return. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The plug-in type ID for filtering.
        self.plugin_class_id = plugin_class_id
        # The plug-in type name for filtering.
        self.plugin_class_name = plugin_class_name
        # Specifies whether the returned results should include plug-in attachment information corresponding to the attachResourceId.
        self.with_attachment_info = with_attachment_info

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

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.include_builtin_ai_gateway is not None:
            result['includeBuiltinAiGateway'] = self.include_builtin_ai_gateway

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.plugin_class_id is not None:
            result['pluginClassId'] = self.plugin_class_id

        if self.plugin_class_name is not None:
            result['pluginClassName'] = self.plugin_class_name

        if self.with_attachment_info is not None:
            result['withAttachmentInfo'] = self.with_attachment_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attachResourceId') is not None:
            self.attach_resource_id = m.get('attachResourceId')

        if m.get('attachResourceType') is not None:
            self.attach_resource_type = m.get('attachResourceType')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('includeBuiltinAiGateway') is not None:
            self.include_builtin_ai_gateway = m.get('includeBuiltinAiGateway')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('pluginClassId') is not None:
            self.plugin_class_id = m.get('pluginClassId')

        if m.get('pluginClassName') is not None:
            self.plugin_class_name = m.get('pluginClassName')

        if m.get('withAttachmentInfo') is not None:
            self.with_attachment_info = m.get('withAttachmentInfo')

        return self

