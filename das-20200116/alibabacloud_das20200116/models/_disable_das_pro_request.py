# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableDasProRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        user_id: str = None,
    ):
        # The database instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the Alibaba Cloud account that is used to create the database instance.
        # 
        # >  This parameter is optional. The system can automatically obtain the account ID based on the value of InstanceId that you set when you call this operation.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

