# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodMediaPlayDataRequest(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        order_name: str = None,
        order_type: str = None,
        os: str = None,
        page_no: int = None,
        page_size: int = None,
        play_date: str = None,
        region: str = None,
        terminal_type: str = None,
    ):
        # The media ID, which is the audio or video ID (VideoId). Specify this parameter filtered query playback data for a specific media file. Only one media ID can be specified. You can obtain the media ID by using the following methods:
        # - For audio or video files uploaded through the console, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Media Files** > **Audio/Video** to view the audio or video ID.
        # - When you upload an audio or video file by calling the [CreateUploadVideo](~~CreateUploadVideo~~) operation, the audio or video ID is the value of the VideoId response parameter.
        # - After the audio or video file is uploaded, you can call the [SearchMedia](~~SearchMedia~~) operation filtered query the audio or video ID, which is the value of the VideoId response parameter.
        self.media_id = media_id
        # The metric name. This parameter is used together with the `OrderType` parameter. Specify this parameter to sort the returned data in ascending or descending order by a specified metric. Valid values:
        # - **PlaySuccessVv**: total plays.
        # - **PlayPerVv**: average plays per user.
        # - **PlayDuration**: total play duration.
        # - **PlayDurationPerUv**: average play duration per user.
        self.order_name = order_name
        # The sort order. This parameter is used together with the `OrderName` parameter. Specify this parameter to sort the returned data in ascending or descending order by a specified metric. Valid values:
        # - **ASC**: ascending order. The returned data is sorted from smallest to largest.
        # - **DESC**: descending order. The returned data is sorted from largest to smallest.
        self.order_type = order_type
        # The operating system of the playback device. Specify this parameter to perform a filtered query for playback data of all audio and video files by operating system. Valid values:
        # - **Android**
        # - **iOS**
        # - **Windows**
        # - **macOS**
        # - **Linux**
        self.os = os
        # The page number of the data to return. Specify this parameter to set the page from which data starts to be returned.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Specify this parameter to set the number of entries displayed on each page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The playback date. Unit: day. Format: yyyyMMdd.
        # > - Only daily queries are supported.
        # > - Only data within the last 30 days can be queried.
        self.play_date = play_date
        # The service region. Specify this parameter to perform a filtered query for playback data of all audio and video files by service region. Valid values:
        # - **cn-beijing**: China (Beijing)
        # - **cn-shanghai**: China (Shanghai)
        # - **cn-shenzhen**: China (Shenzhen)
        # - **ap-northeast-1**: Japan (Tokyo)
        # - **ap-southeast-1**: Singapore
        # - **ap-southeast-5**: Indonesia (Jakarta)
        # - **eu-central-1**: Germany (Frankfurt)
        self.region = region
        # The terminal type of the Player SDK. Specify this parameter to perform a filtered query for playback data of all audio and video files by terminal type. Valid values:
        # - **Native**: Android Player SDK or iOS Player SDK.
        # - **Web**: Web Player SDK.
        self.terminal_type = terminal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.order_name is not None:
            result['OrderName'] = self.order_name

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.os is not None:
            result['Os'] = self.os

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.play_date is not None:
            result['PlayDate'] = self.play_date

        if self.region is not None:
            result['Region'] = self.region

        if self.terminal_type is not None:
            result['TerminalType'] = self.terminal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('OrderName') is not None:
            self.order_name = m.get('OrderName')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlayDate') is not None:
            self.play_date = m.get('PlayDate')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('TerminalType') is not None:
            self.terminal_type = m.get('TerminalType')

        return self

