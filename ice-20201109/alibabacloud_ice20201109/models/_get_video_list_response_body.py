# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetVideoListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        media_list: List[main_models.GetVideoListResponseBodyMediaList] = None,
        request_id: str = None,
        success: str = None,
        total: int = None,
    ):
        # The status code returned.
        self.code = code
        # The information about the audio and video files.
        self.media_list = media_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of audio and video files that meet the conditions.
        self.total = total

    def validate(self):
        if self.media_list:
            for v1 in self.media_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['MediaList'] = []
        if self.media_list is not None:
            for k1 in self.media_list:
                result['MediaList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.media_list = []
        if m.get('MediaList') is not None:
            for k1 in m.get('MediaList'):
                temp_model = main_models.GetVideoListResponseBodyMediaList()
                self.media_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetVideoListResponseBodyMediaList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cate_id: int = None,
        cate_name: str = None,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        duration: float = None,
        media_id: str = None,
        modification_time: str = None,
        size: int = None,
        snapshots: List[str] = None,
        status: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
    ):
        # The ID of the application. Default value: app-1000000.
        self.app_id = app_id
        # The ID of the category.
        self.cate_id = cate_id
        # The name of the category.
        self.cate_name = cate_name
        # The URL of the thumbnail.
        self.cover_url = cover_url
        # The time when the audio or video file was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the audio or video file.
        self.description = description
        # The duration. Unit: seconds.
        self.duration = duration
        # The ID of the audio or video file.
        self.media_id = media_id
        # The time when the audio or video file was updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The size of the source file. Unit: bytes.
        self.size = size
        # The array of video snapshot URLs.
        self.snapshots = snapshots
        # The status of the video.
        # 
        # Valid values:
        # 
        # *   PrepareFail: The file is abnormal.
        # *   UploadFail: The video failed to be uploaded.
        # *   UploadSucc: The video is uploaded.
        # *   Transcoding: The video is being transcoded.
        # *   TranscodeFail: The video failed to be transcoded.
        # *   ProduceFail: The video failed to be produced.
        # *   Normal: The video is normal.
        # *   Uploading: The video is being uploaded.
        # *   Preparing: The file is being generated.
        # *   Blocked: The video is blocked.
        # *   checking: The video is being reviewed.
        self.status = status
        # The storage address.
        self.storage_location = storage_location
        # The tags of the audio or video file.
        self.tags = tags
        # The title of the audio or video file.
        self.title = title

    def validate(self):
        pass

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
            result['CoverUrl'] = self.cover_url

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

