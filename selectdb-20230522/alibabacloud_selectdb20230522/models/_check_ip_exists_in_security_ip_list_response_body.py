# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class CheckIpExistsInSecurityIpListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CheckIpExistsInSecurityIpListResponseBodyData = None,
        request_id: str = None,
    ):
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
            temp_model = main_models.CheckIpExistsInSecurityIpListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class CheckIpExistsInSecurityIpListResponseBodyData(DaraModel):
    def __init__(
        self,
        ip_exists: bool = None,
    ):
        self.ip_exists = ip_exists

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_exists is not None:
            result['IpExists'] = self.ip_exists

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpExists') is not None:
            self.ip_exists = m.get('IpExists')

        return self

