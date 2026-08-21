# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTranscodeTaskRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        page_no: int = None,
        page_size: int = None,
        start_time: str = None,
        video_id: str = None,
    ):
        # The end time, which must be later than the start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.end_time = end_time
        # The page number. Specify this parameter to return data starting from the specified page. Default value: **1**.
        self.page_no = page_no
        # The number of entries per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.start_time = start_time
        # The audio or video ID. You can obtain the ID by using one of the following methods:
        # - For audio or video files uploaded in the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the ID.
        # - Obtain the video ID from the VideoId response parameter when you call the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation to obtain the upload URL and credential.
        # - After the audio or video file is uploaded, call the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation to query the audio or video ID, which is the VideoId value in the response.
        # 
        # This parameter is required.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

