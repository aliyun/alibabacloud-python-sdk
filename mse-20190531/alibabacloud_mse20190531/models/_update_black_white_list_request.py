# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBlackWhiteListRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        content: str = None,
        gateway_unique_id: str = None,
        id: int = None,
        is_white: bool = None,
        name: str = None,
        note: str = None,
        resource_id_json_list: str = None,
        resource_type: str = None,
        status: str = None,
        type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The content of the blacklist.
        self.content = content
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the blacklist.
        self.id = id
        # Specifies whether to enable the whitelist.
        self.is_white = is_white
        # The name.
        self.name = name
        # The description.
        self.note = note
        # The resource IDs in the JSON format.
        self.resource_id_json_list = resource_id_json_list
        # The type of the resource.
        self.resource_type = resource_type
        # Specifies whether to enable the blacklist or whitelist.
        self.status = status
        # The type of the blacklist or whitelist.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.content is not None:
            result['Content'] = self.content

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.id is not None:
            result['Id'] = self.id

        if self.is_white is not None:
            result['IsWhite'] = self.is_white

        if self.name is not None:
            result['Name'] = self.name

        if self.note is not None:
            result['Note'] = self.note

        if self.resource_id_json_list is not None:
            result['ResourceIdJsonList'] = self.resource_id_json_list

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsWhite') is not None:
            self.is_white = m.get('IsWhite')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('ResourceIdJsonList') is not None:
            self.resource_id_json_list = m.get('ResourceIdJsonList')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

