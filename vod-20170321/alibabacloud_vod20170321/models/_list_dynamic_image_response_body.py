# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class ListDynamicImageResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_image_list: List[main_models.ListDynamicImageResponseBodyDynamicImageList] = None,
        request_id: str = None,
    ):
        # The list of animated stickers.
        self.dynamic_image_list = dynamic_image_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dynamic_image_list:
            for v1 in self.dynamic_image_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DynamicImageList'] = []
        if self.dynamic_image_list is not None:
            for k1 in self.dynamic_image_list:
                result['DynamicImageList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dynamic_image_list = []
        if m.get('DynamicImageList') is not None:
            for k1 in m.get('DynamicImageList'):
                temp_model = main_models.ListDynamicImageResponseBodyDynamicImageList()
                self.dynamic_image_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDynamicImageResponseBodyDynamicImageList(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        duration: str = None,
        dynamic_image_id: str = None,
        file_size: str = None,
        file_url: str = None,
        format: str = None,
        fps: str = None,
        height: str = None,
        job_id: str = None,
        video_id: str = None,
        width: str = None,
    ):
        # The time when the animated sticker was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The duration of the animated sticker. Unit: seconds.
        self.duration = duration
        # The ID of the animated sticker.
        self.dynamic_image_id = dynamic_image_id
        # The size of the animated sticker file. Unit: byte.
        self.file_size = file_size
        # The URL of the animated sticker file.
        self.file_url = file_url
        # The format of the animated sticker. Valid values: gif and webp.
        self.format = format
        # The frame rate of the animated sticker. Unit: frames per second.
        self.fps = fps
        # The height of the animated sticker. Unit: pixel.
        self.height = height
        # The job ID for creating the animated sticker.
        self.job_id = job_id
        # The ID of the video.
        self.video_id = video_id
        # The width of the animated sticker. Unit: pixel.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.dynamic_image_id is not None:
            result['DynamicImageId'] = self.dynamic_image_id

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.format is not None:
            result['Format'] = self.format

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('DynamicImageId') is not None:
            self.dynamic_image_id = m.get('DynamicImageId')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

