# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodPlayerCollectDataResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeVodPlayerCollectDataResponseBodyDataList] = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeVodPlayerCollectDataResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVodPlayerCollectDataResponseBodyDataList(DaraModel):
    def __init__(
        self,
        metric: str = None,
        value: float = None,
        value_ratio: float = None,
        value_refer: float = None,
    ):
        self.metric = metric
        self.value = value
        self.value_ratio = value_ratio
        self.value_refer = value_refer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric is not None:
            result['Metric'] = self.metric

        if self.value is not None:
            result['Value'] = self.value

        if self.value_ratio is not None:
            result['ValueRatio'] = self.value_ratio

        if self.value_refer is not None:
            result['ValueRefer'] = self.value_refer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueRatio') is not None:
            self.value_ratio = m.get('ValueRatio')

        if m.get('ValueRefer') is not None:
            self.value_refer = m.get('ValueRefer')

        return self

