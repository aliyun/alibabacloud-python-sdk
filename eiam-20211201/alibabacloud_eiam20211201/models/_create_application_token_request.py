# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationTokenRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_token_type: str = None,
        expiration_time: int = None,
        instance_id: str = None,
    ):
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        # 应用token类型
        # 
        # This parameter is required.
        self.application_token_type = application_token_type
        # 不填，默认1年后到期
        self.expiration_time = expiration_time
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_token_type is not None:
            result['ApplicationTokenType'] = self.application_token_type

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationTokenType') is not None:
            self.application_token_type = m.get('ApplicationTokenType')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

