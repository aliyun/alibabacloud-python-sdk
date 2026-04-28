# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDownloadUrlResponseBody(DaraModel):
    def __init__(
        self,
        cdn_url: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        crc_64hash: str = None,
        expiration: str = None,
        internal_url: str = None,
        size: int = None,
        url: str = None,
    ):
        # The download URL of a file that is downloaded by using Alibaba Cloud CDN.
        self.cdn_url = cdn_url
        # The hash value of the file content.
        self.content_hash = content_hash
        # The name of the algorithm that is used to calculate the hash value of the file content.
        self.content_hash_name = content_hash_name
        # The hash value calculated by using 64-bit cyclic redundancy check (CRC-64).
        self.crc_64hash = crc_64hash
        # The time when the download URL expires.
        self.expiration = expiration
        # The download URL of a file that is downloaded over a virtual private cloud (VPC).
        self.internal_url = internal_url
        # The size of the file. Unit: bytes.
        self.size = size
        # The download URL of a file that is downloaded over the Internet.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdn_url is not None:
            result['cdn_url'] = self.cdn_url

        if self.content_hash is not None:
            result['content_hash'] = self.content_hash

        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name

        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash

        if self.expiration is not None:
            result['expiration'] = self.expiration

        if self.internal_url is not None:
            result['internal_url'] = self.internal_url

        if self.size is not None:
            result['size'] = self.size

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cdn_url') is not None:
            self.cdn_url = m.get('cdn_url')

        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')

        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')

        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')

        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')

        if m.get('internal_url') is not None:
            self.internal_url = m.get('internal_url')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

