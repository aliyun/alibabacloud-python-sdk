# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindUserAuthnSourceMappingRequest(DaraModel):
    def __init__(
        self,
        identity_provider_id: str = None,
        instance_id: str = None,
        user_external_id: str = None,
        user_id: str = None,
    ):
        # 来源Idp Id
        # 
        # This parameter is required.
        self.identity_provider_id = identity_provider_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 外部关联ID
        # 
        # This parameter is required.
        self.user_external_id = user_external_id
        # 用户ID
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.user_external_id is not None:
            result['UserExternalId'] = self.user_external_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UserExternalId') is not None:
            self.user_external_id = m.get('UserExternalId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

