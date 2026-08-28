# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dtsai20260401 import models as main_models
from darabonba.model import DaraModel

class AuthorizeFileUploadResponseBody(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        authorizations: List[main_models.AuthorizeFileUploadResponseBodyAuthorizations] = None,
        bucket: str = None,
        encoded_policy: str = None,
        endpoint: str = None,
        error_code: str = None,
        error_message: str = None,
        expire_time: int = None,
        http_status_code: int = None,
        object_key: str = None,
        request_id: str = None,
        security_token: str = None,
        signature: str = None,
        success: bool = None,
    ):
        # The temporary AccessKey ID used for OSS PostObject.
        self.access_key_id = access_key_id
        self.authorizations = authorizations
        # The destination OSS bucket.
        self.bucket = bucket
        # The Base64-encoded PostObject policy, which includes the ObjectKey and file size limits.
        self.encoded_policy = encoded_policy
        # OSS Endpoint
        self.endpoint = endpoint
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        self.expire_time = expire_time
        # The business-level HTTP status code.
        self.http_status_code = http_status_code
        # The object key that must be used as-is for the upload.
        self.object_key = object_key
        # The request ID.
        self.request_id = request_id
        # The Security Token Service (STS) temporary security token.
        self.security_token = security_token
        # The policy signature.
        self.signature = signature
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.authorizations:
            for v1 in self.authorizations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        result['Authorizations'] = []
        if self.authorizations is not None:
            for k1 in self.authorizations:
                result['Authorizations'].append(k1.to_map() if k1 else None)

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.encoded_policy is not None:
            result['EncodedPolicy'] = self.encoded_policy

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

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
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        self.authorizations = []
        if m.get('Authorizations') is not None:
            for k1 in m.get('Authorizations'):
                temp_model = main_models.AuthorizeFileUploadResponseBodyAuthorizations()
                self.authorizations.append(temp_model.from_map(k1))

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('EncodedPolicy') is not None:
            self.encoded_policy = m.get('EncodedPolicy')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class AuthorizeFileUploadResponseBodyAuthorizations(DaraModel):
    def __init__(
        self,
        encoded_policy: str = None,
        object_key: str = None,
        signature: str = None,
    ):
        self.encoded_policy = encoded_policy
        self.object_key = object_key
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encoded_policy is not None:
            result['EncodedPolicy'] = self.encoded_policy

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.signature is not None:
            result['Signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodedPolicy') is not None:
            self.encoded_policy = m.get('EncodedPolicy')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

