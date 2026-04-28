# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudAgentLogoutRequest(DaraModel):
    def __init__(
        self,
        cno: str = None,
        enterprise_id: int = None,
        ignore_offline: int = None,
        is_kickout: int = None,
        remove_binding: int = None,
    ):
        # 座席工号；取值3-10位正整数
        # 
        # This parameter is required.
        self.cno = cno
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 是否忽略重复下线报错；取值：0:不忽略 1:忽略 默认为0，不忽略
        self.ignore_offline = ignore_offline
        # 是否给座席发生kickout事件；取值： 0:不发送， 1:发送 默认为1，发送
        self.is_kickout = is_kickout
        # 取值： 0:不解除绑定电话， 1:解除绑定电话 默认为0
        self.remove_binding = remove_binding

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cno is not None:
            result['Cno'] = self.cno

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.ignore_offline is not None:
            result['IgnoreOffline'] = self.ignore_offline

        if self.is_kickout is not None:
            result['IsKickout'] = self.is_kickout

        if self.remove_binding is not None:
            result['RemoveBinding'] = self.remove_binding

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('IgnoreOffline') is not None:
            self.ignore_offline = m.get('IgnoreOffline')

        if m.get('IsKickout') is not None:
            self.is_kickout = m.get('IsKickout')

        if m.get('RemoveBinding') is not None:
            self.remove_binding = m.get('RemoveBinding')

        return self

