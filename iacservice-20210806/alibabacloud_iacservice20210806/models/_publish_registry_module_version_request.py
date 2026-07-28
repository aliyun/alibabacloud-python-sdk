# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishRegistryModuleVersionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        module_name: str = None,
        namespace_name: str = None,
        version: str = None,
    ):
        # The idempotence token. Format: [0-9a-zA-Z-]{1,64}. Use a UUID.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The template name.
        # 
        # This parameter is required.
        self.module_name = module_name
        # The workspace name.
        # 
        # This parameter is required.
        self.namespace_name = namespace_name
        # The version number. The value must conform to the [semantic version](http://semver.org/) specification, such as 1.0.1. The initial version is 1.0.0.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

