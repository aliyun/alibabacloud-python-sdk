# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVideoPreviewPlayInfoRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        drive_id: str = None,
        file_id: str = None,
        get_master_url: bool = None,
        get_without_url: bool = None,
        re_transcode: bool = None,
        share_id: str = None,
        template_id: str = None,
        url_expire_sec: int = None,
    ):
        # The category. It is the transcoding mode that you want to use. Valid values:
        # 
        # *   live_transcoding: plays a live stream while transcoding is in progress.
        # *   quick_video: plays a video while transcoding is in progress.
        # *   offline_audio: plays a piece of audio after the audio is transcoded offline.
        # *   offline_video: plays a video after the video is transcoded offline.
        # 
        # This parameter is required.
        self.category = category
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # Specifies whether to obtain the URL of the master M3U8 playlist. This parameter is valid only if the category parameter is set to quick_video.
        self.get_master_url = get_master_url
        # Specifies whether not to query the playback URL. If you set this parameter to true, only transcoding metadata is returned. The video is not transcoded in the TS format, and the playback URL is not returned. If you set this parameter to false, the playback URL is returned. If the video has not been transcoded by using the template specified by template_id, the transcoding process is triggered. You are charged value-added service fees generated for transcoding.
        self.get_without_url = get_without_url
        # Specifies whether to initiate re-transcoding. If you set this parameter to true, the file is re-transcoded, with a fixed 202 response for retries. Before you use this parameter, contact us to enable it for you.
        self.re_transcode = re_transcode
        # The share ID. If you want to share a file, carry the `x-share-token` header for authentication in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify one of `share_id` and `drive_id`.
        self.share_id = share_id
        # The ID of the definition template. If you leave this parameter empty, all definition templates are available.
        self.template_id = template_id
        # The validity period of the URL. Unit: seconds. Default value: 900, which is 15 minutes. Maximum value: 14400, which is 4 hours.
        self.url_expire_sec = url_expire_sec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.get_master_url is not None:
            result['get_master_url'] = self.get_master_url

        if self.get_without_url is not None:
            result['get_without_url'] = self.get_without_url

        if self.re_transcode is not None:
            result['re_transcode'] = self.re_transcode

        if self.share_id is not None:
            result['share_id'] = self.share_id

        if self.template_id is not None:
            result['template_id'] = self.template_id

        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('get_master_url') is not None:
            self.get_master_url = m.get('get_master_url')

        if m.get('get_without_url') is not None:
            self.get_without_url = m.get('get_without_url')

        if m.get('re_transcode') is not None:
            self.re_transcode = m.get('re_transcode')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')

        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')

        return self

