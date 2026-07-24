# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUploadInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        code: int = None,
        expire: int = None,
        folder: str = None,
        host: str = None,
        http_status_code: int = None,
        key: str = None,
        msg: str = None,
        name: str = None,
        policy: str = None,
        request_id: str = None,
        security_token: str = None,
        signature: str = None,
        success: bool = None,
    ):
        # The upload authorization ID.
        self.access_id = access_id
        # The error code, consistent with the HTTP status code.
        self.code = code
        # Unit: seconds.
        self.expire = expire
        # The file name.
        self.folder = folder
        # The upload host.
        self.host = host
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The key used for file upload.
        self.key = key
        # The further description of the error code.
        self.msg = msg
        # Used for frontend image upload.
        self.name = name
        # The OSS file upload policy.
        self.policy = policy
        # The backend-assigned ID that uniquely identifies a request. This ID can be used for troubleshooting.
        self.request_id = request_id
        self.security_token = security_token
        # The upload signature information.
        self.signature = signature
        # The success flag.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.code is not None:
            result['Code'] = self.code

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.folder is not None:
            result['Folder'] = self.folder

        if self.host is not None:
            result['Host'] = self.host

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.key is not None:
            result['Key'] = self.key

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.name is not None:
            result['Name'] = self.name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Folder') is not None:
            self.folder = m.get('Folder')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

