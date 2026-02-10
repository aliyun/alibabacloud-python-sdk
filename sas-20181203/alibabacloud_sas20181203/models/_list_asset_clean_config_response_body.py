# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListAssetCleanConfigResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        data: List[main_models.ListAssetCleanConfigResponseBodyData] = None,
        request_id: str = None,
    ):
        # The number of cleanup configurations.
        self.count = count
        # The asset cleanup configurations.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAssetCleanConfigResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAssetCleanConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        clean_days: int = None,
        status: int = None,
        type: int = None,
    ):
        # The number of days before hosts whose provider cannot be identified are automatically cleaned after they enter the offline state. Valid value: an integer that ranges from 1 to 30.
        self.clean_days = clean_days
        # Indicates whether the configuration takes effect. Valid values:
        # 
        # *   **0**: The configuration does not take effect.
        # *   **1**: The configuration takes effect.
        self.status = status
        # The type of hosts that are cleaned.
        # 
        # *   The value is set to **1**, which indicates hosts whose provider cannot be identified.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clean_days is not None:
            result['CleanDays'] = self.clean_days

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleanDays') is not None:
            self.clean_days = m.get('CleanDays')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

