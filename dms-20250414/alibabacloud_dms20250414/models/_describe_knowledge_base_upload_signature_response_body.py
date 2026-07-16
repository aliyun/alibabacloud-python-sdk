# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class DescribeKnowledgeBaseUploadSignatureResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeKnowledgeBaseUploadSignatureResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The upload signature details.
        self.data = data
        # The error code if the request fails.
        self.error_code = error_code
        # The error message if the request fails.
        self.error_message = error_message
        # The unique ID of the request. If an error occurs, use this ID to troubleshoot the issue.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
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
            temp_model = main_models.DescribeKnowledgeBaseUploadSignatureResponseBodyData()
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

class DescribeKnowledgeBaseUploadSignatureResponseBodyData(DaraModel):
    def __init__(
        self,
        oss_credential: str = None,
        oss_date: str = None,
        oss_security_token: str = None,
        oss_signature: str = None,
        oss_signature_version: str = None,
        policy: str = None,
        upload_dir: str = None,
        upload_host: str = None,
    ):
        # The credential scope string for the signature.
        self.oss_credential = oss_credential
        # The request time in ISO 8601 format.
        self.oss_date = oss_date
        # The STS token used for uploading to OSS. It is valid for one hour.
        self.oss_security_token = oss_security_token
        # The authentication signature.
        self.oss_signature = oss_signature
        # The signature version and algorithm.
        self.oss_signature_version = oss_signature_version
        # The Base64-encoded POST policy that specifies the conditions for the file upload.
        self.policy = policy
        # The path prefix for the file upload.
        self.upload_dir = upload_dir
        # The destination URL for the file upload.
        self.upload_host = upload_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.upload_dir is not None:
            result['UploadDir'] = self.upload_dir

        if self.upload_host is not None:
            result['UploadHost'] = self.upload_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('UploadDir') is not None:
            self.upload_dir = m.get('UploadDir')

        if m.get('UploadHost') is not None:
            self.upload_host = m.get('UploadHost')

        return self

