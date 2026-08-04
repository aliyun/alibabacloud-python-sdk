# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class MapFromHavanaBindIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.MapFromHavanaBindIdResponseBodyData] = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.MapFromHavanaBindIdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class MapFromHavanaBindIdResponseBodyData(DaraModel):
    def __init__(
        self,
        bind_hid: str = None,
        havana_bind_id: str = None,
        havana_bind_station: str = None,
        pk: str = None,
    ):
        self.bind_hid = bind_hid
        self.havana_bind_id = havana_bind_id
        self.havana_bind_station = havana_bind_station
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_hid is not None:
            result['BindHid'] = self.bind_hid

        if self.havana_bind_id is not None:
            result['HavanaBindId'] = self.havana_bind_id

        if self.havana_bind_station is not None:
            result['HavanaBindStation'] = self.havana_bind_station

        if self.pk is not None:
            result['Pk'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindHid') is not None:
            self.bind_hid = m.get('BindHid')

        if m.get('HavanaBindId') is not None:
            self.havana_bind_id = m.get('HavanaBindId')

        if m.get('HavanaBindStation') is not None:
            self.havana_bind_station = m.get('HavanaBindStation')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        return self

