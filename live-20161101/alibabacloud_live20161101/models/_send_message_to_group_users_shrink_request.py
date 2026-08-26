# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendMessageToGroupUsersShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        data: str = None,
        group_id: str = None,
        operator_user_id: str = None,
        receiver_id_list_shrink: str = None,
        skip_audit: bool = None,
        type: int = None,
    ):
        # Interactive Messages application
        # 
        # This parameter is required.
        self.app_id = app_id
        # Message body in JSONString format.
        # 
        # This parameter is required.
        self.data = data
        # Message group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # Operator user ID.
        # 
        # This parameter is required.
        self.operator_user_id = operator_user_id
        # User list.
        self.receiver_id_list_shrink = receiver_id_list_shrink
        # Specifies whether the current message content requires Content Moderation by Alibaba Cloud. Valid values:
        # 
        # - **true**: Content Moderation is not required.
        # - **false** (default): Content Moderation is required.
        self.skip_audit = skip_audit
        # Message type. When the type field value is less than or equal to 10000, it indicates a system message. When the value is greater than 10000, it indicates a custom message.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.data is not None:
            result['Data'] = self.data

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.operator_user_id is not None:
            result['OperatorUserId'] = self.operator_user_id

        if self.receiver_id_list_shrink is not None:
            result['ReceiverIdList'] = self.receiver_id_list_shrink

        if self.skip_audit is not None:
            result['SkipAudit'] = self.skip_audit

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('OperatorUserId') is not None:
            self.operator_user_id = m.get('OperatorUserId')

        if m.get('ReceiverIdList') is not None:
            self.receiver_id_list_shrink = m.get('ReceiverIdList')

        if m.get('SkipAudit') is not None:
            self.skip_audit = m.get('SkipAudit')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

