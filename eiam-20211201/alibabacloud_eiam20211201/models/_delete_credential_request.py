# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCredentialRequest(DaraModel):
    def __init__(
        self,
        credential_id: str = None,
        instance_id: str = None,
    ):
        # 凭据ID。
        # 
        # This parameter is required.
        self.credential_id = credential_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

