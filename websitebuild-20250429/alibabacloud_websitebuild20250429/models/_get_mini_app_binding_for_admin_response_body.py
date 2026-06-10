# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetMiniAppBindingForAdminResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMiniAppBindingForAdminResponseBodyData = None,
        request_id: str = None,
    ):
        # Request result.
        self.data = data
        # Id of the request
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetMiniAppBindingForAdminResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMiniAppBindingForAdminResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_status: str = None,
        biz_id: str = None,
        platform_appid: str = None,
    ):
        # Authorization status
        self.auth_status = auth_status
        # Business ID
        self.biz_id = biz_id
        # Miniapp ID
        self.platform_appid = platform_appid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.platform_appid is not None:
            result['PlatformAppid'] = self.platform_appid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('PlatformAppid') is not None:
            self.platform_appid = m.get('PlatformAppid')

        return self

