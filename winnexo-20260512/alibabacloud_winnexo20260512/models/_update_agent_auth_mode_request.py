# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAgentAuthModeRequest(DaraModel):
    def __init__(
        self,
        auth_mode: str = None,
        operating_object_name: str = None,
        tenant_id: str = None,
    ):
        # The authentication mode.
        # 
        # This parameter is required.
        self.auth_mode = auth_mode
        # The name of the digital employee (operating object name, optional).
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # The ID of the effective tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_mode is not None:
            result['authMode'] = self.auth_mode

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authMode') is not None:
            self.auth_mode = m.get('authMode')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

