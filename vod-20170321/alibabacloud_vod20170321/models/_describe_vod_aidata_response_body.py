# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodAIDataResponseBody(DaraModel):
    def __init__(
        self,
        aidata: main_models.DescribeVodAIDataResponseBodyAIData = None,
        data_interval: str = None,
        request_id: str = None,
    ):
        self.aidata = aidata
        # The time granularity at which the data was queried. Valid values:
        # 
        # *   **hour**
        # *   **day**
        self.data_interval = data_interval
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.aidata:
            self.aidata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aidata is not None:
            result['AIData'] = self.aidata.to_map()

        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIData') is not None:
            temp_model = main_models.DescribeVodAIDataResponseBodyAIData()
            self.aidata = temp_model.from_map(m.get('AIData'))

        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVodAIDataResponseBodyAIData(DaraModel):
    def __init__(
        self,
        aidata_item: List[main_models.DescribeVodAIDataResponseBodyAIDataAIDataItem] = None,
    ):
        self.aidata_item = aidata_item

    def validate(self):
        if self.aidata_item:
            for v1 in self.aidata_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AIDataItem'] = []
        if self.aidata_item is not None:
            for k1 in self.aidata_item:
                result['AIDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aidata_item = []
        if m.get('AIDataItem') is not None:
            for k1 in m.get('AIDataItem'):
                temp_model = main_models.DescribeVodAIDataResponseBodyAIDataAIDataItem()
                self.aidata_item.append(temp_model.from_map(k1))

        return self

class DescribeVodAIDataResponseBodyAIDataAIDataItem(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeVodAIDataResponseBodyAIDataAIDataItemData = None,
        time_stamp: str = None,
    ):
        self.data = data
        self.time_stamp = time_stamp

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

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeVodAIDataResponseBodyAIDataAIDataItemData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

class DescribeVodAIDataResponseBodyAIDataAIDataItemData(DaraModel):
    def __init__(
        self,
        data_item: List[main_models.DescribeVodAIDataResponseBodyAIDataAIDataItemDataDataItem] = None,
    ):
        self.data_item = data_item

    def validate(self):
        if self.data_item:
            for v1 in self.data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataItem'] = []
        if self.data_item is not None:
            for k1 in self.data_item:
                result['DataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_item = []
        if m.get('DataItem') is not None:
            for k1 in m.get('DataItem'):
                temp_model = main_models.DescribeVodAIDataResponseBodyAIDataAIDataItemDataDataItem()
                self.data_item.append(temp_model.from_map(k1))

        return self

class DescribeVodAIDataResponseBodyAIDataAIDataItemDataDataItem(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

