# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteStreamRequest(DaraModel):
    def __init__(
        self,
        job_ids: str = None,
        reference_id: str = None,
        video_id: str = None,
    ):
        # The list of job IDs for media stream transcoding, which consists of one or more job IDs.
        # - Separate multiple IDs with commas (,). A maximum of 20 job IDs under the same video are supported.
        # - You can obtain the JobId from the PlayInfo struct returned by the [GetPlayInfo](https://help.aliyun.com/document_detail/56124.html) operation. Each media stream has a different JobId.
        # 
        # This parameter is required.
        self.job_ids = job_ids
        # The custom ID. Only lowercase letters, uppercase letters, digits, hyphens (-), and underscores (_) are supported. The value must be 6 to 64 characters in length. The value is unique per user.
        self.reference_id = reference_id
        # The video ID. You can obtain the video ID by using one of the following methods:
        # - For videos uploaded by using the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the video ID.
        # - When you upload a video by calling the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation, the video ID is the value of the VideoId parameter in the response.
        # - After a video is uploaded, you can call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the video ID, which is the value of the VideoId parameter in the response.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

