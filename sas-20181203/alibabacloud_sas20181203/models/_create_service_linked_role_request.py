# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceLinkedRoleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        service_linked_role: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Different requests must use different tokens. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # - true: performs only a dry run without executing the actual operation.
        # - false: performs the actual operation.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # The service-linked role. Default value: **AliyunServiceRoleForSas**. Valid values:
        # 
        # - **AliyunServiceRoleForSas**: The service-linked role for Security Center (SAS). Security Center uses this role to access your resources in other Alibaba Cloud services.
        # - **AliyunServiceRoleForSasCspm**: The service-linked role for Security Center - Cloud Security Posture Management (CSPM) (sas-cspm). sas-cspm uses this role to access your resources in other Alibaba Cloud services.
        self.service_linked_role = service_linked_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.service_linked_role is not None:
            result['ServiceLinkedRole'] = self.service_linked_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ServiceLinkedRole') is not None:
            self.service_linked_role = m.get('ServiceLinkedRole')

        return self

