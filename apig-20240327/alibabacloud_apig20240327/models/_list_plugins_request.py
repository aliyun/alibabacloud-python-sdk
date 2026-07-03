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
        # The ID of the attached resource.
        self.attach_resource_id = attach_resource_id
        # The type of the attachment point supported by the policy.
        # 
        # - HttpApi: HttpApi.
        # - Operation: Operation of HttpApi.
        # - GatewayRoute: gateway route.
        # - GatewayService: gateway service.
        # - GatewayServicePort: gateway service port.
        # - Domain: gateway domain name.
        # - Gateway: gateway.
        self.attach_resource_type = attach_resource_type
        # The ID of the gateway instance used to filter results.
        self.gateway_id = gateway_id
        # The gateway type used to filter results. Valid values: **AI** and **API**.
        self.gateway_type = gateway_type
        # Specifies whether the response includes built-in AI plugins installed by the system. Default value: false.
        self.include_builtin_ai_gateway = include_builtin_ai_gateway
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The ID of the plugin type used to filter results.
        self.plugin_class_id = plugin_class_id
        # The name of the plugin type used to filter results.
        self.plugin_class_name = plugin_class_name
        # Specifies whether the response includes the plugin attachment information corresponding to attachResourceId.
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

