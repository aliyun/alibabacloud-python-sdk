# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetDataTrendResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataTrendResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
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
            temp_model = main_models.GetDataTrendResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDataTrendResponseBodyData(DaraModel):
    def __init__(
        self,
        date_list: List[int] = None,
        date_str_list: List[str] = None,
        item_list: List[main_models.GetDataTrendResponseBodyDataItemList] = None,
    ):
        # The statistical timestamps of the trend data.
        self.date_list = date_list
        # The statistical dates and time for the trend data.
        self.date_str_list = date_str_list
        # The returned data.
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for v1 in self.item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_list is not None:
            result['DateList'] = self.date_list

        if self.date_str_list is not None:
            result['DateStrList'] = self.date_str_list

        result['ItemList'] = []
        if self.item_list is not None:
            for k1 in self.item_list:
                result['ItemList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateList') is not None:
            self.date_list = m.get('DateList')

        if m.get('DateStrList') is not None:
            self.date_str_list = m.get('DateStrList')

        self.item_list = []
        if m.get('ItemList') is not None:
            for k1 in m.get('ItemList'):
                temp_model = main_models.GetDataTrendResponseBodyDataItemList()
                self.item_list.append(temp_model.from_map(k1))

        return self

class GetDataTrendResponseBodyDataItemList(DaraModel):
    def __init__(
        self,
        count_list: List[int] = None,
        key_name: str = None,
    ):
        # The statistical values of the trend data.
        self.count_list = count_list
        # The type of the security data. Valid values:
        # 
        # *   **HC_NEW**: the number of new baseline risks.
        # *   **HC_OPERATE**: the number of handled baseline risks.
        # *   **VUL_NEW**: the number of new vulnerabilities.
        # *   **VUL_OPERATE**: the number of handled vulnerabilities.
        # *   **SUSP_NEW**: the number of new alerts.
        # *   **SUSP_OPERATE**: the number of handled alerts.
        self.key_name = key_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count_list is not None:
            result['CountList'] = self.count_list

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountList') is not None:
            self.count_list = m.get('CountList')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        return self

