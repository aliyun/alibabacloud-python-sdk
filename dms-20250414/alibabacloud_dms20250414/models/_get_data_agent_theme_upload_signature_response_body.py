# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class GetDataAgentThemeUploadSignatureResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataAgentThemeUploadSignatureResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response struct.
        self.data = data
        # The error code returned when the request fails.
        self.error_code = error_code
        # The error message returned when the call fails.
        self.error_message = error_message
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDataAgentThemeUploadSignatureResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataAgentThemeUploadSignatureResponseBodyData(DaraModel):
    def __init__(
        self,
        expire_time: str = None,
        object_key: str = None,
        oss_credential: str = None,
        oss_date: str = None,
        oss_security_token: str = None,
        oss_signature: str = None,
        oss_signature_version: str = None,
        policy: str = None,
        theme_id: str = None,
        upload_dir: str = None,
        upload_host: str = None,
    ):
        # The policy expiration time in ISO 8601 UTC format.
        self.expire_time = expire_time
        # The target object key, which is exactly locked by the policy.
        self.object_key = object_key
        # The parameter set that specifies the derived key.
        self.oss_credential = oss_credential
        # The signature time in the format of yyyyMMdd\\"T\\"HHmmss\\"Z\\".
        self.oss_date = oss_date
        # The STS token used to upload files to OSS. The token is valid for 1 hour.
        self.oss_security_token = oss_security_token
        # The V4 signature value.
        self.oss_signature = oss_signature
        # The signature version. The value is fixed as OSS4-HMAC-SHA256.
        self.oss_signature_version = oss_signature_version
        # The Base64-encoded value of the policy JSON.
        self.policy = policy
        # The theme business identifier generated or reused for this request. Pass this identifier to the CreateDataAgentTheme operation after the upload is complete to register the metadata.
        self.theme_id = theme_id
        # The upload directory prefix.
        self.upload_dir = upload_dir
        # The PostObject destination address over the public network.
        self.upload_host = upload_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.oss_credential is not None:
            result['OssCredential'] = self.oss_credential

        if self.oss_date is not None:
            result['OssDate'] = self.oss_date

        if self.oss_security_token is not None:
            result['OssSecurityToken'] = self.oss_security_token

        if self.oss_signature is not None:
            result['OssSignature'] = self.oss_signature

        if self.oss_signature_version is not None:
            result['OssSignatureVersion'] = self.oss_signature_version

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id

        if self.upload_dir is not None:
            result['UploadDir'] = self.upload_dir

        if self.upload_host is not None:
            result['UploadHost'] = self.upload_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('OssCredential') is not None:
            self.oss_credential = m.get('OssCredential')

        if m.get('OssDate') is not None:
            self.oss_date = m.get('OssDate')

        if m.get('OssSecurityToken') is not None:
            self.oss_security_token = m.get('OssSecurityToken')

        if m.get('OssSignature') is not None:
            self.oss_signature = m.get('OssSignature')

        if m.get('OssSignatureVersion') is not None:
            self.oss_signature_version = m.get('OssSignatureVersion')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')

        if m.get('UploadDir') is not None:
            self.upload_dir = m.get('UploadDir')

        if m.get('UploadHost') is not None:
            self.upload_host = m.get('UploadHost')

        return self

