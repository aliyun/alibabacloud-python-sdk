# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsyncEditTimelineShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_clips: bool = None,
        task_id: str = None,
        timelines_shrink: str = None,
        workspace_id: str = None,
    ):
        self.auto_clips = auto_clips
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.timelines_shrink = timelines_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_clips is not None:
            result['AutoClips'] = self.auto_clips

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.timelines_shrink is not None:
            result['Timelines'] = self.timelines_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoClips') is not None:
            self.auto_clips = m.get('AutoClips')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Timelines') is not None:
            self.timelines_shrink = m.get('Timelines')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

