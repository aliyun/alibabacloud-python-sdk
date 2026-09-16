# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateArtifactUploadTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        artifact_path: str = None,
        dir: str = None,
        expire: int = None,
        host: str = None,
        max_size: int = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
        success_action_status: str = None,
    ):
        # The AccessKey ID used for OSS uploads.
        self.access_id = access_id
        # The normalized logical upload directory on the server side, relative to the digital human artifact root directory.
        self.artifact_path = artifact_path
        # The allowed OSS object prefix for uploads.
        self.dir = dir
        # The expiration time of the upload credential. The value is a UNIX timestamp in seconds.
        self.expire = expire
        # The OSS form upload URL.
        self.host = host
        # The maximum size of a single file upload, in bytes.
        self.max_size = max_size
        # The Base64-encoded OSS Post Policy.
        self.policy = policy
        # The request ID.
        self.request_id = request_id
        # The OSS Post Policy signature.
        self.signature = signature
        # The status code returned upon a successful OSS upload.
        self.success_action_status = success_action_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['accessId'] = self.access_id

        if self.artifact_path is not None:
            result['artifactPath'] = self.artifact_path

        if self.dir is not None:
            result['dir'] = self.dir

        if self.expire is not None:
            result['expire'] = self.expire

        if self.host is not None:
            result['host'] = self.host

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.policy is not None:
            result['policy'] = self.policy

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.signature is not None:
            result['signature'] = self.signature

        if self.success_action_status is not None:
            result['successActionStatus'] = self.success_action_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessId') is not None:
            self.access_id = m.get('accessId')

        if m.get('artifactPath') is not None:
            self.artifact_path = m.get('artifactPath')

        if m.get('dir') is not None:
            self.dir = m.get('dir')

        if m.get('expire') is not None:
            self.expire = m.get('expire')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        if m.get('successActionStatus') is not None:
            self.success_action_status = m.get('successActionStatus')

        return self

