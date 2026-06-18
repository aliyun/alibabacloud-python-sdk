# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetAudioNoteUploadUrlResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetAudioNoteUploadUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The detailed reason why access is denied.
        self.access_denied_detail = access_denied_detail
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the API call is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAudioNoteUploadUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAudioNoteUploadUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        expire: str = None,
        file_path: str = None,
        host: str = None,
        key: str = None,
        max_file_size: int = None,
        method: str = None,
        policy: str = None,
        security_token: str = None,
        signature: str = None,
        upload_url: str = None,
    ):
        # The AccessKey ID used for signing.
        self.access_key_id = access_key_id
        # The expiration time of the authorization.
        self.expire = expire
        # The storage path of the OSS file.
        self.file_path = file_path
        # The host address.
        self.host = host
        # The key of the OSS file.
        self.key = key
        # The maximum file size.
        self.max_file_size = max_file_size
        # The HTTP method used for upload.
        self.method = method
        # The upload policy.
        self.policy = policy
        # The authorization licensing key.
        self.security_token = security_token
        # The signature of the temporary upload credential, used to verify legitimacy during upload.
        self.signature = signature
        # The upload URL.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.host is not None:
            result['Host'] = self.host

        if self.key is not None:
            result['Key'] = self.key

        if self.max_file_size is not None:
            result['MaxFileSize'] = self.max_file_size

        if self.method is not None:
            result['Method'] = self.method

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MaxFileSize') is not None:
            self.max_file_size = m.get('MaxFileSize')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')

        return self

