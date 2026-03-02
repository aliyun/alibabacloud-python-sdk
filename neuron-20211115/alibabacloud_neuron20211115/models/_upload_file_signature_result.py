# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadFileSignatureResult(DaraModel):
    def __init__(
        self,
        expired_time: int = None,
        file_url: str = None,
        host: str = None,
        key_id: str = None,
        path: str = None,
        policy: str = None,
        signature: str = None,
        thumb_url: str = None,
    ):
        self.expired_time = expired_time
        self.file_url = file_url
        self.host = host
        self.key_id = key_id
        self.path = path
        self.policy = policy
        self.signature = signature
        self.thumb_url = thumb_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time

        if self.file_url is not None:
            result['fileUrl'] = self.file_url

        if self.host is not None:
            result['host'] = self.host

        if self.key_id is not None:
            result['keyId'] = self.key_id

        if self.path is not None:
            result['path'] = self.path

        if self.policy is not None:
            result['policy'] = self.policy

        if self.signature is not None:
            result['signature'] = self.signature

        if self.thumb_url is not None:
            result['thumbUrl'] = self.thumb_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')

        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('keyId') is not None:
            self.key_id = m.get('keyId')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        if m.get('thumbUrl') is not None:
            self.thumb_url = m.get('thumbUrl')

        return self

