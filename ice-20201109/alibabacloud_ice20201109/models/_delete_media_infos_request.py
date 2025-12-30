# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMediaInfosRequest(DaraModel):
    def __init__(
        self,
        delete_physical_files: bool = None,
        input_urls: str = None,
        media_ids: str = None,
    ):
        # Specifies whether to delete the physical file of the media asset.
        # 
        # If the media asset is stored in your own OSS bucket, you must authorize the service role AliyunICEDefaultRole in advance. For more information<props="china">, see [Authorize IMS to delete recording files in OSS](https://help.aliyun.com/zh/ims/user-guide/record?spm=a2c4g.11186623.0.i8#0737d9c437bmn).
        self.delete_physical_files = delete_physical_files
        # The URL of the media asset that you want to delete. The file corresponding to the URL must be registered with IMS. Separate multiple URLs with commas (,). The following two formats are supported:
        # 
        # 1.  http(s)://example-bucket.oss-cn-shanghai.aliyuncs.com/example.mp4?
        # 2.  OSS://example-bucket/example.mp4?\\
        #     In this format, it is considered by default that the region of the OSS bucket in which the media asset resides is the same as the region in which IMS is activated.
        self.input_urls = input_urls
        # The ID of the media asset that you want to delete from Intelligent Media Services (IMS).
        # 
        # *   Separate multiple IDs with commas (,).
        # 
        # If you leave MediaIds empty, you must specify InputURLs.
        self.media_ids = media_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_physical_files is not None:
            result['DeletePhysicalFiles'] = self.delete_physical_files

        if self.input_urls is not None:
            result['InputURLs'] = self.input_urls

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletePhysicalFiles') is not None:
            self.delete_physical_files = m.get('DeletePhysicalFiles')

        if m.get('InputURLs') is not None:
            self.input_urls = m.get('InputURLs')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        return self

