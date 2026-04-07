# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQualityFollowerRequest(DaraModel):
    def __init__(
        self,
        alarm_mode: int = None,
        entity_id: int = None,
        follower: str = None,
        project_id: int = None,
        project_name: str = None,
    ):
        # The notification method. Valid values: 1, 2, 4, 5, 6, 7, 8, and 9. The value 1 indicates that the notification is sent by email. The value 2 indicates that the notification is sent by email and text message. The value 4 indicates that the notification is sent by a DingTalk chatbot. The value 5 indicates that the notification is sent by a DingTalk chatbot to all members in a DingTalk group. The value 6 indicates that the notification is sent by Lark. The value 7 indicates that the notification is sent by WeCom. The value 8 indicates that the notification is sent by webhook. The value 9 indicates that the notification is sent by phone call.
        # 
        # This parameter is required.
        self.alarm_mode = alarm_mode
        # The ID of the partition filter expression.
        # 
        # This parameter is required.
        self.entity_id = entity_id
        # The account ID of the subscriber.
        # 
        # This parameter is required.
        self.follower = follower
        # The DataWorks workspace ID. You can log on to the DataWorks console to query the ID.
        self.project_id = project_id
        # The name of the compute engine or data source.
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_mode is not None:
            result['AlarmMode'] = self.alarm_mode

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.follower is not None:
            result['Follower'] = self.follower

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMode') is not None:
            self.alarm_mode = m.get('AlarmMode')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('Follower') is not None:
            self.follower = m.get('Follower')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

