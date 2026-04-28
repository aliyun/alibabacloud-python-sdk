# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SimpleStreamInfo(DaraModel):
    def __init__(
        self,
        content_hash: str = None,
        content_hash_name: str = None,
        crc_64hash: str = None,
        download_url: str = None,
        size: int = None,
        thumbnail: str = None,
        url: str = None,
    ):
        self.content_hash = content_hash
        self.content_hash_name = content_hash_name
        self.crc_64hash = crc_64hash
        self.download_url = download_url
        self.size = size
        self.thumbnail = thumbnail
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash

        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name

        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash

        if self.download_url is not None:
            result['download_url'] = self.download_url

        if self.size is not None:
            result['size'] = self.size

        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')

        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')

        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')

        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

