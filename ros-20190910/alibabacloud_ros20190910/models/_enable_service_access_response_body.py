# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class EnableServiceAccessResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_access_info: main_models.EnableServiceAccessResponseBodyServiceAccessInfo = None,
    ):
        self.request_id = request_id
        self.service_access_info = service_access_info

    def validate(self):
        if self.service_access_info:
            self.service_access_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_access_info is not None:
            result['ServiceAccessInfo'] = self.service_access_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceAccessInfo') is not None:
            temp_model = main_models.EnableServiceAccessResponseBodyServiceAccessInfo()
            self.service_access_info = temp_model.from_map(m.get('ServiceAccessInfo'))

        return self

class EnableServiceAccessResponseBodyServiceAccessInfo(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

