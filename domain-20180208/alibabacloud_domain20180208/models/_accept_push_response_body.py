# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class AcceptPushResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        http_status_code: int = None,
        module: main_models.AcceptPushResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        # RAM鉴权失败时的标准化错误详情，JSON字符串，包含NoPermissionType、PolicyType、AuthPrincipalType、EncodedDiagnosticMessage等字段
        self.access_denied_detail = access_denied_detail
        # 是否允许重试
        self.allow_retry = allow_retry
        # HTTP状态码
        self.http_status_code = http_status_code
        # 业务数据模块
        self.module = module
        # 唯一请求识别码
        self.request_id = request_id
        # 是否调用成功
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Module') is not None:
            temp_model = main_models.AcceptPushResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class AcceptPushResponseBodyModule(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        push_no: str = None,
        success: bool = None,
    ):
        # 结果码，失败时返回
        self.code = code
        # 结果描述
        self.message = message
        # Push编号
        self.push_no = push_no
        # 是否接收成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.push_no is not None:
            result['PushNo'] = self.push_no

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PushNo') is not None:
            self.push_no = m.get('PushNo')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

