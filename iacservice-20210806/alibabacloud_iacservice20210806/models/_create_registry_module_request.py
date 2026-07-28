# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRegistryModuleRequest(DaraModel):
    def __init__(
        self,
        acl: str = None,
        client_token: str = None,
        description: str = None,
        module_name: str = None,
        namespace_name: str = None,
        provider: str = None,
        type: str = None,
    ):
        # The access permission. Valid values:
        # 
        # - private: private.
        self.acl = acl
        # The idempotence token. Format: [0-9a-zA-Z-]{1,64}. Use a UUID.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The description of the Registry template.
        self.description = description
        # The name of the Registry template. The name must meet the following requirements:
        # 
        # - The name must be 3 to 63 characters in length.
        # - The name can contain uppercase and lowercase letters, digits, hyphens (-), and underscores (_), and cannot start or end with a hyphen.
        # - The name must be unique within the workspace.
        # 
        # This parameter is required.
        self.module_name = module_name
        # The workspace name.
        # 
        # This parameter is required.
        self.namespace_name = namespace_name
        # The provider type. Valid values:
        # 
        # - alicloud: Alibaba Cloud.
        self.provider = provider
        # The template type. Valid values:
        # 
        # - self: custom template.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['acl'] = self.acl

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.description is not None:
            result['description'] = self.description

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.provider is not None:
            result['provider'] = self.provider

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

