# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class GetFileRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        file_id: str = None,
        share_id: str = None,
        thumbnail_processes: Dict[str, main_models.ImageProcess] = None,
        url_expire_sec: int = None,
    ):
        # The drive ID.
        self.drive_id = drive_id
        # The fields to return.
        # 
        # 1.  If this parameter is set to \\*, all fields of the file except the fields that must be specified are returned.
        # 2.  If only specific fields are required, you can specify the following fields: url, thumbnail, exif, cropping_suggestion, characteristic_hash, video_metadata, and video_preview_metadata. If multiple fields are required, separate them with commas (,). Example: url,thumbnail.
        # 3.  The investigation_info field is returned only if it is specified.
        # 
        # By default, all fields except the fields that must be specified are returned.
        self.fields = fields
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The share ID. If you want to share a file, carry the `x-share-token` header for authentication in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify one of `share_id` and `drive_id`.
        self.share_id = share_id
        # The thumbnail configurations. Up to five thumbnails can be returned at a time. The value contains key-value pairs. You can customize the keys. The URL of a thumbnail is returned based on the key.
        self.thumbnail_processes = thumbnail_processes
        # The time when the file expires. Unit: seconds. Valid values: 10 to 14400.
        self.url_expire_sec = url_expire_sec

    def validate(self):
        if self.thumbnail_processes:
            for v1 in self.thumbnail_processes.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.fields is not None:
            result['fields'] = self.fields

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.share_id is not None:
            result['share_id'] = self.share_id

        result['thumbnail_processes'] = {}
        if self.thumbnail_processes is not None:
            for k1, v1 in self.thumbnail_processes.items():
                result['thumbnail_processes'][k1] = v1.to_map() if v1 else None

        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        self.thumbnail_processes = {}
        if m.get('thumbnail_processes') is not None:
            for k1, v1 in m.get('thumbnail_processes').items():
                temp_model = main_models.ImageProcess()
                self.thumbnail_processes[k1] = temp_model.from_map(v1)

        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')

        return self

