# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetSmsOcrOssInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: main_models.GetSmsOcrOssInfoResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 访问被拒绝详细信息，只有 RAM 校验失败才会返回此字段。
        self.access_denied_detail = access_denied_detail
        # 请求状态码。
        # 
        # - 返回 OK 代表请求成功。
        # 
        # - 其他错误码，请参见 [API 错误码](https://www.alibabacloud.com/help/en/sms/developer-reference/api-error-codes)。
        self.code = code
        # 状态码的描述。
        self.message = message
        # OSS配置信息。
        self.model = model
        # 本次调用请求的 ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。
        self.request_id = request_id
        # 调用接口是否成功。取值：
        # 
        # - true：调用成功。
        # 
        # - false：调用失败。
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

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

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.GetSmsOcrOssInfoResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSmsOcrOssInfoResponseBodyModel(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        bucket: str = None,
        expire_time: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
        start_path: str = None,
    ):
        # 签名使用的 AccessKey ID。
        self.access_key_id = access_key_id
        # bucket名称。
        self.bucket = bucket
        # 过期时间戳，单位：秒。
        self.expire_time = expire_time
        # Host 地址。
        self.host = host
        # 签名策略。
        self.policy = policy
        # 根据 AccessKey Secret 和 Policy 计算出的签名信息。调用 OSS API 时，OSS 验证该签名信息，从而确认请求的合法性。
        self.signature = signature
        # 策略路径。
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

