# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableInternalAuthenticationSourceRequest(DaraModel):
    def __init__(
        self,
        authentication_source_id: str = None,
        instance_id: str = None,
    ):
        # 内部认证源ID，比如 ia_password, ia_otp_sms 等
        self.authentication_source_id = authentication_source_id
        # IDaaS EIAM的实例id
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
        if self.authentication_source_id is not None:
            result['AuthenticationSourceId'] = self.authentication_source_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationSourceId') is not None:
            self.authentication_source_id = m.get('AuthenticationSourceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

