# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetVideoListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        video_list: main_models.GetVideoListResponseBodyVideoList = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of media files returned.
        self.total = total
        self.video_list = video_list

    def validate(self):
        if self.video_list:
            self.video_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        if self.video_list is not None:
            result['VideoList'] = self.video_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('VideoList') is not None:
            temp_model = main_models.GetVideoListResponseBodyVideoList()
            self.video_list = temp_model.from_map(m.get('VideoList'))

        return self

class GetVideoListResponseBodyVideoList(DaraModel):
    def __init__(
        self,
        video: List[main_models.GetVideoListResponseBodyVideoListVideo] = None,
    ):
        self.video = video

    def validate(self):
        if self.video:
            for v1 in self.video:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Video'] = []
        if self.video is not None:
            for k1 in self.video:
                result['Video'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video = []
        if m.get('Video') is not None:
            for k1 in m.get('Video'):
                temp_model = main_models.GetVideoListResponseBodyVideoListVideo()
                self.video.append(temp_model.from_map(k1))

        return self

class GetVideoListResponseBodyVideoListVideo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cate_id: int = None,
        cate_name: str = None,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        duration: float = None,
        modification_time: str = None,
        reference_id: str = None,
        restore_expiration: str = None,
        restore_status: str = None,
        size: int = None,
        snapshots: main_models.GetVideoListResponseBodyVideoListVideoSnapshots = None,
        status: str = None,
        storage_class: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
        user_data: str = None,
        video_id: str = None,
    ):
        self.app_id = app_id
        self.cate_id = cate_id
        self.cate_name = cate_name
        self.cover_url = cover_url
        self.creation_time = creation_time
        self.description = description
        self.duration = duration
        self.modification_time = modification_time
        self.reference_id = reference_id
        self.restore_expiration = restore_expiration
        self.restore_status = restore_status
        self.size = size
        self.snapshots = snapshots
        self.status = status
        self.storage_class = storage_class
        self.storage_location = storage_location
        self.tags = tags
        self.title = title
        self.user_data = user_data
        self.video_id = video_id

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

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

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.restore_expiration is not None:
            result['RestoreExpiration'] = self.restore_expiration

        if self.restore_status is not None:
            result['RestoreStatus'] = self.restore_status

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

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

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('RestoreExpiration') is not None:
            self.restore_expiration = m.get('RestoreExpiration')

        if m.get('RestoreStatus') is not None:
            self.restore_status = m.get('RestoreStatus')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Snapshots') is not None:
            temp_model = main_models.GetVideoListResponseBodyVideoListVideoSnapshots()
            self.snapshots = temp_model.from_map(m.get('Snapshots'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

class GetVideoListResponseBodyVideoListVideoSnapshots(DaraModel):
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

