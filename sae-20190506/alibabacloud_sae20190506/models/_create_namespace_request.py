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
        # Specifies whether to enable the built-in service registry of SAE.
        # 
        # - **true**
        # 
        # - **false**
        # 
        # The default value is true. If you do not use the built-in service registry, set this parameter to false to speed up namespace creation.
        self.enable_micro_registration = enable_micro_registration
        # The short-format namespace ID. You do not need to specify a region ID. This parameter is recommended. The ID cannot exceed 20 characters in length and can contain only lowercase letters and digits.
        self.name_space_short_id = name_space_short_id
        # The description of the namespace. The description cannot exceed 100 characters in length.
        self.namespace_description = namespace_description
        # The long-format namespace ID. If you specify this parameter, NameSpaceShortId is ignored. This parameter is retained for compatibility. Use the short-format namespace ID instead. The format is `<RegionId>:<NamespaceId>`. The `NamespaceId` can contain only lowercase letters and digits and cannot exceed 32 characters in length. Example: `cn-beijing:test`. For information about the regions that SAE supports, see [DescribeRegions](https://help.aliyun.com/document_detail/126213.html).
        self.namespace_id = namespace_id
        # The name of the namespace. The name cannot exceed 64 characters in length.
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

