# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetMiniAppAuthUrlResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMiniAppAuthUrlResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            temp_model = main_models.GetMiniAppAuthUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMiniAppAuthUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_url: str = None,
    ):
        self.auth_url = auth_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_url is not None:
            result['AuthUrl'] = self.auth_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthUrl') is not None:
            self.auth_url = m.get('AuthUrl')

        return self

