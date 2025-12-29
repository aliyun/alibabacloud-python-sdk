# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNamespaceRequest(DaraModel):
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
        # If you set this parameter to true, a shared registry is created for the namespace. The registry cannot be disabled after it is created.
        self.enable_micro_registration = enable_micro_registration
        # The short ID of the namespace. You do not need to specify a region ID. We recommend that you configure this parameter. The value of this parameter can be up to 20 characters in length and can contain only lowercase letters and digits.
        self.name_space_short_id = name_space_short_id
        # The description of the namespace. The description cannot exceed 100 characters in length.
        self.namespace_description = namespace_description
        # The long ID of the namespace. If you configure this parameter, the long ID take effects and the value of the NameSpaceShortId parameter is ignored. To ensure compatibility, we recommend that you specify a short namespace ID. A long namespace ID follows the `<RegionId>:<NamespaceId>` format. The `NamespaceId` variable can contain only lowercase letters and digits. Example: `cn-beijing:test`. The value of the Namespaceid variable cannot exceed 32 characters in length. For more information about **RegionId**, you can call the [DescribeRegions](https://help.aliyun.com/document_detail/2834842.html) operation to obtain the IDs of regions supported by SAE.
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

