# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class ListAIImageInfoResponseBody(DaraModel):
    def __init__(
        self,
        aiimage_info_list: List[main_models.ListAIImageInfoResponseBodyAIImageInfoList] = None,
        request_id: str = None,
    ):
        # The image files that are uploaded for AI processing.
        self.aiimage_info_list = aiimage_info_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.aiimage_info_list:
            for v1 in self.aiimage_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AIImageInfoList'] = []
        if self.aiimage_info_list is not None:
            for k1 in self.aiimage_info_list:
                result['AIImageInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aiimage_info_list = []
        if m.get('AIImageInfoList') is not None:
            for k1 in m.get('AIImageInfoList'):
                temp_model = main_models.ListAIImageInfoResponseBodyAIImageInfoList()
                self.aiimage_info_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAIImageInfoResponseBodyAIImageInfoList(DaraModel):
    def __init__(
        self,
        aiimage_info_id: str = None,
        creation_time: str = None,
        file_url: str = None,
        format: str = None,
        job_id: str = None,
        score: str = None,
        version: str = None,
        video_id: str = None,
    ):
        # The ID of the image information.
        self.aiimage_info_id = aiimage_info_id
        # The time when the file was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The URL of the image file.
        self.file_url = file_url
        # The format of the image. Valid values: **gif** and **png**.
        self.format = format
        # The ID of the image AI processing job.
        self.job_id = job_id
        # The score of the image.
        self.score = score
        # The data version ID.
        self.version = version
        # The ID of the video.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiimage_info_id is not None:
            result['AIImageInfoId'] = self.aiimage_info_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.format is not None:
            result['Format'] = self.format

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.score is not None:
            result['Score'] = self.score

        if self.version is not None:
            result['Version'] = self.version

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIImageInfoId') is not None:
            self.aiimage_info_id = m.get('AIImageInfoId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

