# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class RegisterMediaResponseBody(DaraModel):
    def __init__(
        self,
        failed_file_urls: List[str] = None,
        registered_media_list: List[main_models.RegisterMediaResponseBodyRegisteredMediaList] = None,
        request_id: str = None,
    ):
        # The URLs of the media files that failed to be registered.
        self.failed_file_urls = failed_file_urls
        # The media files that are registered, including newly registered and repeatedly registered media files.
        self.registered_media_list = registered_media_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.registered_media_list:
            for v1 in self.registered_media_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_file_urls is not None:
            result['FailedFileURLs'] = self.failed_file_urls

        result['RegisteredMediaList'] = []
        if self.registered_media_list is not None:
            for k1 in self.registered_media_list:
                result['RegisteredMediaList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedFileURLs') is not None:
            self.failed_file_urls = m.get('FailedFileURLs')

        self.registered_media_list = []
        if m.get('RegisteredMediaList') is not None:
            for k1 in m.get('RegisteredMediaList'):
                temp_model = main_models.RegisterMediaResponseBodyRegisteredMediaList()
                self.registered_media_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RegisterMediaResponseBodyRegisteredMediaList(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_id: str = None,
        new_register: bool = None,
    ):
        # The URL of the media file.
        self.file_url = file_url
        # The ID of the media file that is registered with ApsaraVideo VOD. If the registered media file is an audio or video file, the value of this parameter is the same as that of the VideoId parameter.
        self.media_id = media_id
        # Indicates whether the media file is newly registered or repeatedly registered. Valid values:
        # 
        # *   **true**: The media file is newly registered.
        # *   **false**: The media file is repeatedly registered.
        self.new_register = new_register

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.new_register is not None:
            result['NewRegister'] = self.new_register

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('NewRegister') is not None:
            self.new_register = m.get('NewRegister')

        return self

