# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeWorkModeRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        instance_id: str = None,
        mobile: str = None,
        signed_skill_group_id_list: str = None,
        user_id: str = None,
        work_mode: str = None,
    ):
        self.device_id = device_id
        # This parameter is required.
        self.instance_id = instance_id
        self.mobile = mobile
        self.signed_skill_group_id_list = signed_skill_group_id_list
        self.user_id = user_id
        # This parameter is required.
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.signed_skill_group_id_list is not None:
            result['SignedSkillGroupIdList'] = self.signed_skill_group_id_list

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('SignedSkillGroupIdList') is not None:
            self.signed_skill_group_id_list = m.get('SignedSkillGroupIdList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

