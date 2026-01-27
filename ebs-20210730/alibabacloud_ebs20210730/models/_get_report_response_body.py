# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class GetReportResponseBody(DaraModel):
    def __init__(
        self,
        datas: List[main_models.GetReportResponseBodyDatas] = None,
        request_id: str = None,
    ):
        # Data Details.
        self.datas = datas
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.datas:
            for v1 in self.datas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Datas'] = []
        if self.datas is not None:
            for k1 in self.datas:
                result['Datas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datas = []
        if m.get('Datas') is not None:
            for k1 in m.get('Datas'):
                temp_model = main_models.GetReportResponseBodyDatas()
                self.datas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetReportResponseBodyDatas(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetReportResponseBodyDatasData] = None,
        title: str = None,
    ):
        # Data.
        self.data = data
        # Data Title.
        self.title = title

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetReportResponseBodyDatasData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetReportResponseBodyDatasData(DaraModel):
    def __init__(
        self,
        data_points: Dict[str, Any] = None,
        labels: Dict[str, Any] = None,
    ):
        # Data Points.
        self.data_points = data_points
        # Data Labels.
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_points is not None:
            result['DataPoints'] = self.data_points

        if self.labels is not None:
            result['Labels'] = self.labels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPoints') is not None:
            self.data_points = m.get('DataPoints')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        return self

