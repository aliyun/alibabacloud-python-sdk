# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCtrlInstanceMemberAccountsResponseBody(DaraModel):
    def __init__(
        self,
        instance_member_count: int = None,
        max_instance_member_num: int = None,
        request_id: str = None,
    ):
        self.instance_member_count = instance_member_count
        self.max_instance_member_num = max_instance_member_num
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_member_count is not None:
            result['InstanceMemberCount'] = self.instance_member_count

        if self.max_instance_member_num is not None:
            result['MaxInstanceMemberNum'] = self.max_instance_member_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceMemberCount') is not None:
            self.instance_member_count = m.get('InstanceMemberCount')

        if m.get('MaxInstanceMemberNum') is not None:
            self.max_instance_member_num = m.get('MaxInstanceMemberNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

