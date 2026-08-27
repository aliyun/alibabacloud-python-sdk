# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListAgentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.ListAgentsResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The list of skill cards.
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
                temp_model = main_models.ListAgentsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListAgentsResponseBodyItems(DaraModel):
    def __init__(
        self,
        auth_mode: str = None,
        display_name: str = None,
        is_active: bool = None,
        operating_object_name: str = None,
    ):
        # The authentication mode.
        self.auth_mode = auth_mode
        # The display name of the tool.
        self.display_name = display_name
        # Indicates whether the account is activated.
        self.is_active = is_active
        # The name of the digital employee.
        self.operating_object_name = operating_object_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_mode is not None:
            result['authMode'] = self.auth_mode

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.is_active is not None:
            result['isActive'] = self.is_active

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authMode') is not None:
            self.auth_mode = m.get('authMode')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        return self

