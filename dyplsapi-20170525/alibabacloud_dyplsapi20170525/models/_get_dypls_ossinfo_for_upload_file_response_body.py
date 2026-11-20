# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetDyplsOSSInfoForUploadFileResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetDyplsOSSInfoForUploadFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details of denied access.
        self.access_denied_detail = access_denied_detail
        # Request status code. Valid values:  
        # * OK: indicates that the request succeeded.  
        # * For other error codes, see [Error Code List](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # Returned data.
        self.data = data
        # Description of the status code.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request succeeded. Valid values:  
        # 
        # - true: indicates success.  
        # 
        # - false: indicates failure.
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
            temp_model = main_models.GetDyplsOSSInfoForUploadFileResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDyplsOSSInfoForUploadFileResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        expire_time: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
        start_path: str = None,
    ):
        # AccessKey ID used for signing.
        self.access_key_id = access_key_id
        # Expiration Time.
        self.expire_time = expire_time
        # Host address.
        self.host = host
        # Signing policy.
        self.policy = policy
        # Signature computed from the **AccessKey secret** and **policy**. When invoking the OSS API, OSS authenticates this signature to confirm the validity of the POST request.
        self.signature = signature
        # Policy path.
        self.start_path = start_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.host is not None:
            result['Host'] = self.host

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.start_path is not None:
            result['StartPath'] = self.start_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('StartPath') is not None:
            self.start_path = m.get('StartPath')

        return self

