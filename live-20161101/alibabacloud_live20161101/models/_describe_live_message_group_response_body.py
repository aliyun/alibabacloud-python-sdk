# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from darabonba.model import DaraModel

class DescribeLiveMessageGroupResponseBody(DaraModel):
    def __init__(
        self,
        admin_list: List[str] = None,
        createtime: int = None,
        creator_id: str = None,
        deletatime: int = None,
        delete: bool = None,
        deletor: str = None,
        group_id: str = None,
        group_info: str = None,
        group_name: str = None,
        msg_amount: Dict[str, int] = None,
        online_user_counts: int = None,
        request_id: str = None,
        super_large_group: bool = None,
        total_times: int = None,
    ):
        # The list of the group administrators.
        self.admin_list = admin_list
        # The time when the group was created. The value is a UNIX timestamp. Unit: seconds.
        self.createtime = createtime
        # The ID of the group creator.
        self.creator_id = creator_id
        # The time when the group was deleted. This parameter is returned only if the group was deleted.
        self.deletatime = deletatime
        # Indicates whether the group was deleted.
        self.delete = delete
        # The ID of the user who deleted the group. This parameter is returned only if the group was deleted.
        self.deletor = deletor
        # The group ID.
        self.group_id = group_id
        # Additional information about the group.
        self.group_info = group_info
        # The name of the group.
        self.group_name = group_name
        # The categorized message statistics. This parameter is returned only if the group exists.
        self.msg_amount = msg_amount
        # The number of online users in the group. This parameter is returned only if the group exists.
        self.online_user_counts = online_user_counts
        # The request ID.
        self.request_id = request_id
        # Indicates whether the group is a super group. Valid values:
        # 
        # *   True
        # *   False
        self.super_large_group = super_large_group
        # The total number of sessions. This parameter is returned only if the group exists.
        self.total_times = total_times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_list is not None:
            result['AdminList'] = self.admin_list

        if self.createtime is not None:
            result['Createtime'] = self.createtime

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.deletatime is not None:
            result['Deletatime'] = self.deletatime

        if self.delete is not None:
            result['Delete'] = self.delete

        if self.deletor is not None:
            result['Deletor'] = self.deletor

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_info is not None:
            result['GroupInfo'] = self.group_info

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.msg_amount is not None:
            result['MsgAmount'] = self.msg_amount

        if self.online_user_counts is not None:
            result['OnlineUserCounts'] = self.online_user_counts

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.super_large_group is not None:
            result['SuperLargeGroup'] = self.super_large_group

        if self.total_times is not None:
            result['TotalTimes'] = self.total_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminList') is not None:
            self.admin_list = m.get('AdminList')

        if m.get('Createtime') is not None:
            self.createtime = m.get('Createtime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Deletatime') is not None:
            self.deletatime = m.get('Deletatime')

        if m.get('Delete') is not None:
            self.delete = m.get('Delete')

        if m.get('Deletor') is not None:
            self.deletor = m.get('Deletor')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupInfo') is not None:
            self.group_info = m.get('GroupInfo')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('MsgAmount') is not None:
            self.msg_amount = m.get('MsgAmount')

        if m.get('OnlineUserCounts') is not None:
            self.online_user_counts = m.get('OnlineUserCounts')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuperLargeGroup') is not None:
            self.super_large_group = m.get('SuperLargeGroup')

        if m.get('TotalTimes') is not None:
            self.total_times = m.get('TotalTimes')

        return self

