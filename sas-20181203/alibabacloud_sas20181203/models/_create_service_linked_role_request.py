# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceLinkedRoleRequest(DaraModel):
    def __init__(
        self,
        service_linked_role: str = None,
    ):
        # The service-linked role. Default value: **AliyunServiceRoleForSas**. Valid values:
        # 
        # - **AliyunServiceRoleForSas**: the service-linked role for Security Center (SAS). Security Center uses this role to access your resources in other Alibaba Cloud services.
        # - **AliyunServiceRoleForSasCspm**: the service-linked role for Security Center - Cloud Security Posture Management (CSPM) (sas-cspm). sas-cspm uses this role to access your resources in other Alibaba Cloud services.
        self.service_linked_role = service_linked_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_linked_role is not None:
            result['ServiceLinkedRole'] = self.service_linked_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceLinkedRole') is not None:
            self.service_linked_role = m.get('ServiceLinkedRole')

        return self

