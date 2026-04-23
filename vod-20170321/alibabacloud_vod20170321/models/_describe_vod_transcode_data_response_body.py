# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodTranscodeDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        request_id: str = None,
        transcode_data: main_models.DescribeVodTranscodeDataResponseBodyTranscodeData = None,
    ):
        # The interval at which the data was queried. Valid values:
        # 
        # *   **hour**
        # *   **day**
        self.data_interval = data_interval
        # The ID of the request.
        self.request_id = request_id
        self.transcode_data = transcode_data

    def validate(self):
        if self.transcode_data:
            self.transcode_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.transcode_data is not None:
            result['TranscodeData'] = self.transcode_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TranscodeData') is not None:
            temp_model = main_models.DescribeVodTranscodeDataResponseBodyTranscodeData()
            self.transcode_data = temp_model.from_map(m.get('TranscodeData'))

        return self

class DescribeVodTranscodeDataResponseBodyTranscodeData(DaraModel):
    def __init__(
        self,
        transcode_data_item: List[main_models.DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItem] = None,
    ):
        self.transcode_data_item = transcode_data_item

    def validate(self):
        if self.transcode_data_item:
            for v1 in self.transcode_data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TranscodeDataItem'] = []
        if self.transcode_data_item is not None:
            for k1 in self.transcode_data_item:
                result['TranscodeDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.transcode_data_item = []
        if m.get('TranscodeDataItem') is not None:
            for k1 in m.get('TranscodeDataItem'):
                temp_model = main_models.DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItem()
                self.transcode_data_item.append(temp_model.from_map(k1))

        return self

class DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItem(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemData = None,
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
            temp_model = main_models.DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

class DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemData(DaraModel):
    def __init__(
        self,
        data_item: List[main_models.DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemDataDataItem] = None,
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
                temp_model = main_models.DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemDataDataItem()
                self.data_item.append(temp_model.from_map(k1))

        return self

class DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemDataDataItem(DaraModel):
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

