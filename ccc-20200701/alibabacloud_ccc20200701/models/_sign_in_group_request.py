# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SignInGroupRequest(DaraModel):
    def __init__(
        self,
        additivity: bool = None,
        chat_device_id: str = None,
        device_id: str = None,
        instance_id: str = None,
        signed_skill_group_id_list: str = None,
        user_id: str = None,
    ):
        self.additivity = additivity
        self.chat_device_id = chat_device_id
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.signed_skill_group_id_list = signed_skill_group_id_list
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additivity is not None:
            result['Additivity'] = self.additivity

        if self.chat_device_id is not None:
            result['ChatDeviceId'] = self.chat_device_id

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.signed_skill_group_id_list is not None:
            result['SignedSkillGroupIdList'] = self.signed_skill_group_id_list

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Additivity') is not None:
            self.additivity = m.get('Additivity')

        if m.get('ChatDeviceId') is not None:
            self.chat_device_id = m.get('ChatDeviceId')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SignedSkillGroupIdList') is not None:
            self.signed_skill_group_id_list = m.get('SignedSkillGroupIdList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

