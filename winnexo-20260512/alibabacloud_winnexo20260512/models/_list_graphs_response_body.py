# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListGraphsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListGraphsResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The list of MCP cards.
        # 
        # This parameter is required.
        self.items = items
        # The prompt message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListGraphsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGraphsResponseBodyItems(DaraModel):
    def __init__(
        self,
        business_profile: str = None,
        display_name: str = None,
        graph_name: str = None,
        is_default: bool = None,
    ):
        # The business description of the knowledge graph. An empty string is returned if not configured.
        # 
        # This parameter is required.
        self.business_profile = business_profile
        # The tool display name.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The knowledge graph name.
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # Indicates whether this is the default group.
        # 
        # This parameter is required.
        self.is_default = is_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_profile is not None:
            result['businessProfile'] = self.business_profile

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessProfile') is not None:
            self.business_profile = m.get('businessProfile')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        return self

