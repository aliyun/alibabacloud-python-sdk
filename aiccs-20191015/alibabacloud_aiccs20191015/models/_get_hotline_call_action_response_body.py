# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetHotlineCallActionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHotlineCallActionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetHotlineCallActionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetHotlineCallActionResponseBodyData(DaraModel):
    def __init__(
        self,
        action_id: int = None,
        bu_id: int = None,
        callout_id: int = None,
        callout_name: str = None,
        case_id: int = None,
        channel_id: str = None,
        channel_type: int = None,
        dep_id: int = None,
        is_transfer: str = None,
        member_id: int = None,
        member_list: str = None,
        member_name: str = None,
        servicer_id: int = None,
        servicer_name: str = None,
        sub_touch_id: int = None,
        task_id: int = None,
        touch_id: int = None,
    ):
        self.action_id = action_id
        self.bu_id = bu_id
        self.callout_id = callout_id
        self.callout_name = callout_name
        self.case_id = case_id
        self.channel_id = channel_id
        self.channel_type = channel_type
        self.dep_id = dep_id
        self.is_transfer = is_transfer
        self.member_id = member_id
        self.member_list = member_list
        self.member_name = member_name
        self.servicer_id = servicer_id
        self.servicer_name = servicer_name
        self.sub_touch_id = sub_touch_id
        self.task_id = task_id
        self.touch_id = touch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_id is not None:
            result['ActionId'] = self.action_id

        if self.bu_id is not None:
            result['BuId'] = self.bu_id

        if self.callout_id is not None:
            result['CalloutId'] = self.callout_id

        if self.callout_name is not None:
            result['CalloutName'] = self.callout_name

        if self.case_id is not None:
            result['CaseId'] = self.case_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.dep_id is not None:
            result['DepId'] = self.dep_id

        if self.is_transfer is not None:
            result['IsTransfer'] = self.is_transfer

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_list is not None:
            result['MemberList'] = self.member_list

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id

        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name

        if self.sub_touch_id is not None:
            result['SubTouchId'] = self.sub_touch_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.touch_id is not None:
            result['TouchId'] = self.touch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionId') is not None:
            self.action_id = m.get('ActionId')

        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')

        if m.get('CalloutId') is not None:
            self.callout_id = m.get('CalloutId')

        if m.get('CalloutName') is not None:
            self.callout_name = m.get('CalloutName')

        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('DepId') is not None:
            self.dep_id = m.get('DepId')

        if m.get('IsTransfer') is not None:
            self.is_transfer = m.get('IsTransfer')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberList') is not None:
            self.member_list = m.get('MemberList')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')

        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')

        if m.get('SubTouchId') is not None:
            self.sub_touch_id = m.get('SubTouchId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')

        return self

