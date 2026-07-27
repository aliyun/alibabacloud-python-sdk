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
        # The alert method. Valid values: 1 (email), 2 (email and SMS), 4 (DingTalk Group Bot), 5 (DingTalk Group Bot with an @all message), 6 (Lark), 7 (WeCom), 8 (webhook), and 9 (Phone Alert).
        # 
        # This parameter is required.
        self.alarm_mode = alarm_mode
        # The ID of the partition expression.
        # 
        # This parameter is required.
        self.entity_id = entity_id
        # The Alibaba Cloud account ID of the follower.
        # 
        # This parameter is required.
        self.follower = follower
        # The ID of the DataWorks workspace. To find the workspace ID, log in to the DataWorks console.
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

