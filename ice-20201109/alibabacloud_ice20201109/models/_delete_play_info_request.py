# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePlayInfoRequest(DaraModel):
    def __init__(
        self,
        delete_physical_files: bool = None,
        file_urls: str = None,
        media_id: str = None,
    ):
        # Specifies whether to delete the physical file of the media stream.
        # 
        # If the media asset is stored in your own Object Storage Service (OSS) bucket, you must authorize the service role AliyunICEDefaultRole in advance. <props="china">For more information, see [Authorize IMS to delete recording files in OSS](https://help.aliyun.com/document_detail/449331.html#p-ko2-wc7-iad).
        # 
        # You can delete only the physical files of transcoded streams, but not the physical files of source files.
        self.delete_physical_files = delete_physical_files
        # The URL of the media stream file that you want to delete. Separate multiple URLs with commas (,).
        self.file_urls = file_urls
        # The ID of the media asset.
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_physical_files is not None:
            result['DeletePhysicalFiles'] = self.delete_physical_files

        if self.file_urls is not None:
            result['FileURLs'] = self.file_urls

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletePhysicalFiles') is not None:
            self.delete_physical_files = m.get('DeletePhysicalFiles')

        if m.get('FileURLs') is not None:
            self.file_urls = m.get('FileURLs')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

