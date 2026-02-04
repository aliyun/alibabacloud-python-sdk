# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210218 import models as main_models
from darabonba.model import DaraModel

class GetAuthCodeResponseBody(DaraModel):
    def __init__(
        self,
        auth_model: main_models.GetAuthCodeResponseBodyAuthModel = None,
        request_id: str = None,
    ):
        self.auth_model = auth_model
        self.request_id = request_id

    def validate(self):
        if self.auth_model:
            self.auth_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_model is not None:
            result['AuthModel'] = self.auth_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthModel') is not None:
            temp_model = main_models.GetAuthCodeResponseBodyAuthModel()
            self.auth_model = temp_model.from_map(m.get('AuthModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class GetAuthCodeResponseBodyAuthModel(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        end_user_id: str = None,
        expire_time: str = None,
    ):
        self.auth_code = auth_code
        self.end_user_id = end_user_id
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        return self

