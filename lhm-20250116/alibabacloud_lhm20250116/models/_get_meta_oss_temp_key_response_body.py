# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetMetaOssTempKeyResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetaOssTempKeyResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        success: bool = None,
    ):
        # The response body. For more information about the fields, see the child field descriptions.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # Indicates whether the call is successful. Valid values:
        # - true: The call is successful.
        # - false: The call failed. Check errCode and errMessage for troubleshooting.
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
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetMetaOssTempKeyResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetMetaOssTempKeyResponseBodyData(DaraModel):
    def __init__(
        self,
        ak: str = None,
        bucket: str = None,
        dir: str = None,
        endpoint: str = None,
        expire: int = None,
        policy: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        # The temporary AccessKey ID (STS token). This value is used together with securityToken to authenticate direct uploads to OSS. This is a sensitive credential. Do not hard-code it in your code or print it to logs.
        self.ak = ak
        # The name of the OSS bucket.
        self.bucket = bucket
        # The allowed OSS upload directory prefix. The value must end with a forward slash (/). The key of the uploaded object must start with this prefix. Otherwise, the request is rejected by OSS.
        self.dir = dir
        # The endpoint of the region where the OSS bucket resides.
        self.endpoint = endpoint
        # The credential expiration timestamp in Unix seconds. Before use, verify whether the current time has exceeded this value. If the credential has expired, obtain new credentials.
        self.expire = expire
        # The Base64-encoded upload policy that defines constraints such as file size and path prefix. The decoded value is a JSON string.
        self.policy = policy
        # The STS temporary security token. This value is used together with ak for authentication and is returned only in STS authentication mode. This is a sensitive credential. Do not hard-code it in your code or print it to logs.
        self.security_token = security_token
        # The signature calculated based on the policy. The OSS server uses this signature to verify the validity of upload requests.
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ak is not None:
            result['ak'] = self.ak

        if self.bucket is not None:
            result['bucket'] = self.bucket

        if self.dir is not None:
            result['dir'] = self.dir

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.expire is not None:
            result['expire'] = self.expire

        if self.policy is not None:
            result['policy'] = self.policy

        if self.security_token is not None:
            result['securityToken'] = self.security_token

        if self.signature is not None:
            result['signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ak') is not None:
            self.ak = m.get('ak')

        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')

        if m.get('dir') is not None:
            self.dir = m.get('dir')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('expire') is not None:
            self.expire = m.get('expire')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        return self

