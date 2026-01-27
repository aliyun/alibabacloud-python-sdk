# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OssUploadCredential(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        endpoint: str = None,
        file_path: str = None,
        oss_policy: str = None,
        oss_signature: str = None,
        sts_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.endpoint = endpoint
        self.file_path = file_path
        self.oss_policy = oss_policy
        self.oss_signature = oss_signature
        self.sts_token = sts_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.oss_policy is not None:
            result['OssPolicy'] = self.oss_policy

        if self.oss_signature is not None:
            result['OssSignature'] = self.oss_signature

        if self.sts_token is not None:
            result['StsToken'] = self.sts_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('OssPolicy') is not None:
            self.oss_policy = m.get('OssPolicy')

        if m.get('OssSignature') is not None:
            self.oss_signature = m.get('OssSignature')

        if m.get('StsToken') is not None:
            self.sts_token = m.get('StsToken')

        return self

