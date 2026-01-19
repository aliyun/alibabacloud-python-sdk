# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class CreateBackendRequest(DaraModel):
    def __init__(
        self,
        backend_name: str = None,
        backend_type: str = None,
        create_event_bridge_service_linked_role: bool = None,
        create_slr: bool = None,
        description: str = None,
        security_token: str = None,
        tag: List[main_models.CreateBackendRequestTag] = None,
    ):
        # The name of the backend service.
        # 
        # This parameter is required.
        self.backend_name = backend_name
        # The type of the backend service.
        # 
        # This parameter is required.
        self.backend_type = backend_type
        # Specifies to create a EventBridge service-linked role.
        self.create_event_bridge_service_linked_role = create_event_bridge_service_linked_role
        # Specifies to create a service-linked role.
        self.create_slr = create_slr
        # The description.
        self.description = description
        self.security_token = security_token
        # The tag of objects that match the rule. You can specify multiple tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_name is not None:
            result['BackendName'] = self.backend_name

        if self.backend_type is not None:
            result['BackendType'] = self.backend_type

        if self.create_event_bridge_service_linked_role is not None:
            result['CreateEventBridgeServiceLinkedRole'] = self.create_event_bridge_service_linked_role

        if self.create_slr is not None:
            result['CreateSlr'] = self.create_slr

        if self.description is not None:
            result['Description'] = self.description

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendName') is not None:
            self.backend_name = m.get('BackendName')

        if m.get('BackendType') is not None:
            self.backend_type = m.get('BackendType')

        if m.get('CreateEventBridgeServiceLinkedRole') is not None:
            self.create_event_bridge_service_linked_role = m.get('CreateEventBridgeServiceLinkedRole')

        if m.get('CreateSlr') is not None:
            self.create_slr = m.get('CreateSlr')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateBackendRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateBackendRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

