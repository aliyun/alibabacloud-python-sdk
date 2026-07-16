# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DisconnectAndroidInstanceRequest(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        instance_ids: List[str] = None,
    ):
        # <props="china">
        # 
        # If you use the Cloud Phone Matrix Edition and the instance stream pattern is collaborative mode, you can specify `EndUserId` to disconnect a specific user and invalidate the corresponding ticket.
        # 
        # 
        # 
        # <props="intl">
        # 
        # This parameter is not publicly available.
        self.end_user_id = end_user_id
        # A list of instance IDs. You can specify 1 to 100 IDs.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        return self

