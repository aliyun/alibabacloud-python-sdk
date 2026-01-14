# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryUserByMobileAccountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryUserByMobileAccountResponseBodyResult = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryUserByMobileAccountResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryUserByMobileAccountResponseBodyResult(DaraModel):
    def __init__(
        self,
        bound_user_id: str = None,
        third_account_name: str = None,
    ):
        self.bound_user_id = bound_user_id
        self.third_account_name = third_account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bound_user_id is not None:
            result['BoundUserId'] = self.bound_user_id

        if self.third_account_name is not None:
            result['ThirdAccountName'] = self.third_account_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundUserId') is not None:
            self.bound_user_id = m.get('BoundUserId')

        if m.get('ThirdAccountName') is not None:
            self.third_account_name = m.get('ThirdAccountName')

        return self

