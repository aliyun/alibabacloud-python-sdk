# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetOSSInfoForCardTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetOSSInfoForCardTemplateResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetOSSInfoForCardTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOSSInfoForCardTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        ali_uid: str = None,
        bucket: str = None,
        expire_time: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
        start_path: str = None,
    ):
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The name of the OSS bucket.
        self.bucket = bucket
        # The timeout period.
        self.expire_time = expire_time
        # The hostname.
        self.host = host
        # The signature policy.
        self.policy = policy
        # The signature.
        self.signature = signature
        # The path of the policy.
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

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bucket is not None:
            result['Bucket'] = self.bucket

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

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

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

