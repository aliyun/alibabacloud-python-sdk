# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveApplicationAccountFromUserRequest(DaraModel):
    def __init__(
        self,
        application_account_id: str = None,
        application_id: str = None,
        instance_id: str = None,
        user_id: str = None,
    ):
        # 应用账号Id
        # 
        # This parameter is required.
        self.application_account_id = application_account_id
        # IDaaS的应用主键id
        # 
        # This parameter is required.
        self.application_id = application_id
        # IDaaS EIAM的实例id
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 用户Id
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
        if self.application_account_id is not None:
            result['ApplicationAccountId'] = self.application_account_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationAccountId') is not None:
            self.application_account_id = m.get('ApplicationAccountId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

