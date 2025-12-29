# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNamespaceRequest(DaraModel):
    def __init__(
        self,
        enable_micro_registration: bool = None,
        name_space_short_id: str = None,
        namespace_description: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
    ):
        # Indicates whether to enable SAE built-in registry:
        # 
        # *   **true**
        # *   **false**
        # 
        # Default value: true. If you do not use the built-in registry, you can set this parameter to false to accelerate the creation of a namespace.
        self.enable_micro_registration = enable_micro_registration
        # The trace ID that is used to query the details of the request.
        self.name_space_short_id = name_space_short_id
        # The message returned for the operation.
        self.namespace_description = namespace_description
        # The data returned.
        self.namespace_id = namespace_id
        # The ID of the request.
        # 
        # This parameter is required.
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_micro_registration is not None:
            result['EnableMicroRegistration'] = self.enable_micro_registration

        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id

        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableMicroRegistration') is not None:
            self.enable_micro_registration = m.get('EnableMicroRegistration')

        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')

        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        return self

