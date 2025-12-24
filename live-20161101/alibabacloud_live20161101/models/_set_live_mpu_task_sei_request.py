# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveMpuTaskSeiRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        custom_sei: str = None,
        task_id: str = None,
    ):
        # The application ID.
        # 
        # >  The ID can be up to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The custom SEI.
        # 
        # >  The value is a JSON string that can be up to 4,096 characters in length.
        # 
        # This parameter is required.
        self.custom_sei = custom_sei
        # The task ID.
        # 
        # >  The ID can be up to 55 characters in length and can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.custom_sei is not None:
            result['CustomSei'] = self.custom_sei

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CustomSei') is not None:
            self.custom_sei = m.get('CustomSei')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

