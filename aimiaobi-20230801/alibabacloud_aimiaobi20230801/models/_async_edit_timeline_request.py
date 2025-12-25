# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class AsyncEditTimelineRequest(DaraModel):
    def __init__(
        self,
        auto_clips: bool = None,
        task_id: str = None,
        timelines: List[main_models.AsyncEditTimelineRequestTimelines] = None,
        workspace_id: str = None,
    ):
        self.auto_clips = auto_clips
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.timelines = timelines
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.timelines:
            for v1 in self.timelines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_clips is not None:
            result['AutoClips'] = self.auto_clips

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        result['Timelines'] = []
        if self.timelines is not None:
            for k1 in self.timelines:
                result['Timelines'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoClips') is not None:
            self.auto_clips = m.get('AutoClips')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        self.timelines = []
        if m.get('Timelines') is not None:
            for k1 in m.get('Timelines'):
                temp_model = main_models.AsyncEditTimelineRequestTimelines()
                self.timelines.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class AsyncEditTimelineRequestTimelines(DaraModel):
    def __init__(
        self,
        clips: List[main_models.AsyncEditTimelineRequestTimelinesClips] = None,
        timeline_id: str = None,
    ):
        # This parameter is required.
        self.clips = clips
        self.timeline_id = timeline_id

    def validate(self):
        if self.clips:
            for v1 in self.clips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Clips'] = []
        if self.clips is not None:
            for k1 in self.clips:
                result['Clips'].append(k1.to_map() if k1 else None)

        if self.timeline_id is not None:
            result['TimelineId'] = self.timeline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clips = []
        if m.get('Clips') is not None:
            for k1 in m.get('Clips'):
                temp_model = main_models.AsyncEditTimelineRequestTimelinesClips()
                self.clips.append(temp_model.from_map(k1))

        if m.get('TimelineId') is not None:
            self.timeline_id = m.get('TimelineId')

        return self

class AsyncEditTimelineRequestTimelinesClips(DaraModel):
    def __init__(
        self,
        clip_id: str = None,
        content_inner: str = None,
        in_: int = None,
        in_ex: float = None,
        out: int = None,
        out_ex: float = None,
        video_id: str = None,
        video_name: str = None,
    ):
        self.clip_id = clip_id
        self.content_inner = content_inner
        self.in_ = in_
        self.in_ex = in_ex
        self.out = out
        self.out_ex = out_ex
        self.video_id = video_id
        self.video_name = video_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clip_id is not None:
            result['ClipId'] = self.clip_id

        if self.content_inner is not None:
            result['ContentInner'] = self.content_inner

        if self.in_ is not None:
            result['In'] = self.in_

        if self.in_ex is not None:
            result['InEx'] = self.in_ex

        if self.out is not None:
            result['Out'] = self.out

        if self.out_ex is not None:
            result['OutEx'] = self.out_ex

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        if self.video_name is not None:
            result['VideoName'] = self.video_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipId') is not None:
            self.clip_id = m.get('ClipId')

        if m.get('ContentInner') is not None:
            self.content_inner = m.get('ContentInner')

        if m.get('In') is not None:
            self.in_ = m.get('In')

        if m.get('InEx') is not None:
            self.in_ex = m.get('InEx')

        if m.get('Out') is not None:
            self.out = m.get('Out')

        if m.get('OutEx') is not None:
            self.out_ex = m.get('OutEx')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')

        return self

