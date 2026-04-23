# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class ListLiveRecordVideoResponseBody(DaraModel):
    def __init__(
        self,
        live_record_video_list: main_models.ListLiveRecordVideoResponseBodyLiveRecordVideoList = None,
        request_id: str = None,
        total: int = None,
    ):
        self.live_record_video_list = live_record_video_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of videos.
        self.total = total

    def validate(self):
        if self.live_record_video_list:
            self.live_record_video_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_record_video_list is not None:
            result['LiveRecordVideoList'] = self.live_record_video_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveRecordVideoList') is not None:
            temp_model = main_models.ListLiveRecordVideoResponseBodyLiveRecordVideoList()
            self.live_record_video_list = temp_model.from_map(m.get('LiveRecordVideoList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListLiveRecordVideoResponseBodyLiveRecordVideoList(DaraModel):
    def __init__(
        self,
        live_record_video: List[main_models.ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideo] = None,
    ):
        self.live_record_video = live_record_video

    def validate(self):
        if self.live_record_video:
            for v1 in self.live_record_video:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveRecordVideo'] = []
        if self.live_record_video is not None:
            for k1 in self.live_record_video:
                result['LiveRecordVideo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_record_video = []
        if m.get('LiveRecordVideo') is not None:
            for k1 in m.get('LiveRecordVideo'):
                temp_model = main_models.ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideo()
                self.live_record_video.append(temp_model.from_map(k1))

        return self

class ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideo(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        playlist_id: str = None,
        record_end_time: str = None,
        record_start_time: str = None,
        stream_name: str = None,
        video: main_models.ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideo = None,
    ):
        self.app_name = app_name
        self.domain_name = domain_name
        self.playlist_id = playlist_id
        self.record_end_time = record_end_time
        self.record_start_time = record_start_time
        self.stream_name = stream_name
        self.video = video

    def validate(self):
        if self.video:
            self.video.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.playlist_id is not None:
            result['PlaylistId'] = self.playlist_id

        if self.record_end_time is not None:
            result['RecordEndTime'] = self.record_end_time

        if self.record_start_time is not None:
            result['RecordStartTime'] = self.record_start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.video is not None:
            result['Video'] = self.video.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PlaylistId') is not None:
            self.playlist_id = m.get('PlaylistId')

        if m.get('RecordEndTime') is not None:
            self.record_end_time = m.get('RecordEndTime')

        if m.get('RecordStartTime') is not None:
            self.record_start_time = m.get('RecordStartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('Video') is not None:
            temp_model = main_models.ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideo(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        duration: float = None,
        modify_time: str = None,
        size: int = None,
        snapshots: main_models.ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideoSnapshots = None,
        status: str = None,
        tags: str = None,
        template_group_id: str = None,
        title: str = None,
        video_id: str = None,
    ):
        self.cate_id = cate_id
        self.cate_name = cate_name
        self.cover_url = cover_url
        self.creation_time = creation_time
        self.description = description
        self.duration = duration
        self.modify_time = modify_time
        self.size = size
        self.snapshots = snapshots
        self.status = status
        self.tags = tags
        self.template_group_id = template_group_id
        self.title = title
        self.video_id = video_id

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id

        if self.title is not None:
            result['Title'] = self.title

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Snapshots') is not None:
            temp_model = main_models.ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideoSnapshots()
            self.snapshots = temp_model.from_map(m.get('Snapshots'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

class ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideoSnapshots(DaraModel):
    def __init__(
        self,
        snapshot: List[str] = None,
    ):
        self.snapshot = snapshot

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')

        return self

