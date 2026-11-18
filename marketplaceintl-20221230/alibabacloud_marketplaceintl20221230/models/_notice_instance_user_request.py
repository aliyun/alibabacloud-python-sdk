# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NoticeInstanceUserRequest(DaraModel):
    def __init__(
        self,
        instance_id: int = None,
        notice_param: str = None,
        notice_type: int = None,
    ):
        self.instance_id = instance_id
        self.notice_param = notice_param
        self.notice_type = notice_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.notice_param is not None:
            result['NoticeParam'] = self.notice_param

        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NoticeParam') is not None:
            self.notice_param = m.get('NoticeParam')

        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')

        return self

