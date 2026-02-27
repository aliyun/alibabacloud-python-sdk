# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceLinkedRoleRequest(DaraModel):
    def __init__(
        self,
        custom_suffix: str = None,
        description: str = None,
        service_name: str = None,
    ):
        # The suffix of the role name.
        # 
        # The role name (including its suffix) must be 1 to 64 characters in length and can contain letters, digits, periods (.), and hyphens (-).
        # 
        # For example, if the suffix is `Example`, the role name is `ServiceLinkedRoleName_Example`.
        self.custom_suffix = custom_suffix
        # The description of the service-linked role.
        # 
        # You must configure this parameter for service-linked roles that support custom suffixes. Otherwise, the preset value is used and cannot be modified.
        # 
        # The description must be 1 to 1,024 characters in length.
        self.description = description
        # The service name.
        # 
        # For more information about the service name, see [Alibaba Cloud services that support service-linked roles](https://help.aliyun.com/document_detail/461722.html).
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_suffix is not None:
            result['CustomSuffix'] = self.custom_suffix

        if self.description is not None:
            result['Description'] = self.description

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSuffix') is not None:
            self.custom_suffix = m.get('CustomSuffix')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

