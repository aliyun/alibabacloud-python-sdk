# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopRtcCloudTranscodeRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        task_id: str = None,
    ):
        # The application ID. The ID can be up to 64 characters long and can contain uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the cloud transcoding job. The ID can be up to 64 characters long and can contain uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).
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

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

