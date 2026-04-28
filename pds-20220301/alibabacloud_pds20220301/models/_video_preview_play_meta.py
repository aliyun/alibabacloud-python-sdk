# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class VideoPreviewPlayMeta(DaraModel):
    def __init__(
        self,
        category: str = None,
        live_transcoding_task_list: List[main_models.VideoPreviewPlayMetaLiveTranscodingTaskList] = None,
        meta: main_models.VideoPreviewPlayMetaMeta = None,
        offline_video_transcoding_list: List[main_models.VideoPreviewPlayMetaOfflineVideoTranscodingList] = None,
        quick_video_list: List[main_models.VideoPreviewPlayMetaQuickVideoList] = None,
    ):
        # Category
        self.category = category
        # Status of the live transcoding job.
        self.live_transcoding_task_list = live_transcoding_task_list
        # Video meta information.
        self.meta = meta
        # The status of the offline transcoding job.
        self.offline_video_transcoding_list = offline_video_transcoding_list
        # The state of the transcoding job.
        self.quick_video_list = quick_video_list

    def validate(self):
        if self.live_transcoding_task_list:
            for v1 in self.live_transcoding_task_list:
                 if v1:
                    v1.validate()
        if self.meta:
            self.meta.validate()
        if self.offline_video_transcoding_list:
            for v1 in self.offline_video_transcoding_list:
                 if v1:
                    v1.validate()
        if self.quick_video_list:
            for v1 in self.quick_video_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        result['live_transcoding_task_list'] = []
        if self.live_transcoding_task_list is not None:
            for k1 in self.live_transcoding_task_list:
                result['live_transcoding_task_list'].append(k1.to_map() if k1 else None)

        if self.meta is not None:
            result['meta'] = self.meta.to_map()

        result['offline_video_transcoding_list'] = []
        if self.offline_video_transcoding_list is not None:
            for k1 in self.offline_video_transcoding_list:
                result['offline_video_transcoding_list'].append(k1.to_map() if k1 else None)

        result['quick_video_list'] = []
        if self.quick_video_list is not None:
            for k1 in self.quick_video_list:
                result['quick_video_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        self.live_transcoding_task_list = []
        if m.get('live_transcoding_task_list') is not None:
            for k1 in m.get('live_transcoding_task_list'):
                temp_model = main_models.VideoPreviewPlayMetaLiveTranscodingTaskList()
                self.live_transcoding_task_list.append(temp_model.from_map(k1))

        if m.get('meta') is not None:
            temp_model = main_models.VideoPreviewPlayMetaMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        self.offline_video_transcoding_list = []
        if m.get('offline_video_transcoding_list') is not None:
            for k1 in m.get('offline_video_transcoding_list'):
                temp_model = main_models.VideoPreviewPlayMetaOfflineVideoTranscodingList()
                self.offline_video_transcoding_list.append(temp_model.from_map(k1))

        self.quick_video_list = []
        if m.get('quick_video_list') is not None:
            for k1 in m.get('quick_video_list'):
                temp_model = main_models.VideoPreviewPlayMetaQuickVideoList()
                self.quick_video_list.append(temp_model.from_map(k1))

        return self

class VideoPreviewPlayMetaQuickVideoList(DaraModel):
    def __init__(
        self,
        status: str = None,
        template_id: str = None,
    ):
        # The status. finished: The index is completed, and the url can be obtained. running: Indexing in progress. Wait a moment and try again. failed: Transcoding failed. Check the media file. If you have any questions, contact customer service.
        self.status = status
        # Template ID
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.template_id is not None:
            result['template_id'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')

        return self

class VideoPreviewPlayMetaOfflineVideoTranscodingList(DaraModel):
    def __init__(
        self,
        keep_original_resolution: str = None,
        status: str = None,
        template_id: str = None,
    ):
        # Whether the original resolution is maintained.
        self.keep_original_resolution = keep_original_resolution
        # The status. finished: The index is completed, and the url can be obtained. running: Indexing in progress. Wait a moment and try again. failed: Transcoding failed. Check the media file. If you have any questions, contact customer service.
        self.status = status
        # Template ID
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keep_original_resolution is not None:
            result['keep_original_resolution'] = self.keep_original_resolution

        if self.status is not None:
            result['status'] = self.status

        if self.template_id is not None:
            result['template_id'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keep_original_resolution') is not None:
            self.keep_original_resolution = m.get('keep_original_resolution')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')

        return self

class VideoPreviewPlayMetaMeta(DaraModel):
    def __init__(
        self,
        duration: float = None,
        height: int = None,
        width: int = None,
    ):
        # Length of the video.
        self.duration = duration
        # Height of the video.
        self.height = height
        # Width of the video.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['duration'] = self.duration

        if self.height is not None:
            result['height'] = self.height

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

class VideoPreviewPlayMetaLiveTranscodingTaskList(DaraModel):
    def __init__(
        self,
        keep_original_resolution: bool = None,
        status: str = None,
        template_id: str = None,
    ):
        # Whether the original resolution is maintained.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.keep_original_resolution = keep_original_resolution
        # The status. Valid values:
        # 
        # *   finished: The index is complete, and the url can be obtained.
        # *   running: Indexing in progress. Wait a moment and try again.
        # *   failed: Transcoding failed. Check the media file. If you have any questions, contact customer service.
        self.status = status
        # Template ID
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keep_original_resolution is not None:
            result['keep_original_resolution'] = self.keep_original_resolution

        if self.status is not None:
            result['status'] = self.status

        if self.template_id is not None:
            result['template_id'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keep_original_resolution') is not None:
            self.keep_original_resolution = m.get('keep_original_resolution')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')

        return self

