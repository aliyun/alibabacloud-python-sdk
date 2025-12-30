# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartBackToBackCallRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        call_center_number: str = None,
        caller: str = None,
        mobile_key: str = None,
        skill_type: int = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.biz_type = biz_type
        self.call_center_number = call_center_number
        # This parameter is required.
        self.caller = caller
        self.mobile_key = mobile_key
        # This parameter is required.
        self.skill_type = skill_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.call_center_number is not None:
            result['CallCenterNumber'] = self.call_center_number

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.mobile_key is not None:
            result['MobileKey'] = self.mobile_key

        if self.skill_type is not None:
            result['SkillType'] = self.skill_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CallCenterNumber') is not None:
            self.call_center_number = m.get('CallCenterNumber')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('MobileKey') is not None:
            self.mobile_key = m.get('MobileKey')

        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')

        return self

