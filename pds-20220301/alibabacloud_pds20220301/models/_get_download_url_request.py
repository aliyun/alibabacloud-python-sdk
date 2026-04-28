# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDownloadUrlRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        expire_sec: int = None,
        file_id: str = None,
        file_name: str = None,
        response_content_type: str = None,
        share_id: str = None,
    ):
        # The drive ID.
        self.drive_id = drive_id
        # The validity period of the download URL. Maximum value: 115200. Default value: 900. Unit: seconds.
        self.expire_sec = expire_sec
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The name of the file. The name can be up to 1,024 characters in length.
        self.file_name = file_name
        self.response_content_type = response_content_type
        # The share ID. If you want to manage a file by using a sharing link, carry the `x-share-token` header in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify at least either `share_id` or `drive_id`.
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.file_name is not None:
            result['file_name'] = self.file_name

        if self.response_content_type is not None:
            result['response_content_type'] = self.response_content_type

        if self.share_id is not None:
            result['share_id'] = self.share_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')

        if m.get('response_content_type') is not None:
            self.response_content_type = m.get('response_content_type')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        return self

