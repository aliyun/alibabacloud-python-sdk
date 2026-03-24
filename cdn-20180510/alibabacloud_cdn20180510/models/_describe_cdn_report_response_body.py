# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnReportResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.DescribeCdnReportResponseBodyContent = None,
        request_id: str = None,
    ):
        # The content of the operations report.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.DescribeCdnReportResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCdnReportResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeCdnReportResponseBodyContentData] = None,
    ):
        self.data = data

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeCdnReportResponseBodyContentData()
                self.data.append(temp_model.from_map(k1))

        return self

class DescribeCdnReportResponseBodyContentData(DaraModel):
    def __init__(
        self,
        data: List[Dict[str, str]] = None,
        deliver: main_models.DescribeCdnReportResponseBodyContentDataDeliver = None,
    ):
        self.data = data
        self.deliver = deliver

    def validate(self):
        if self.deliver:
            self.deliver.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.deliver is not None:
            result['deliver'] = self.deliver.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('deliver') is not None:
            temp_model = main_models.DescribeCdnReportResponseBodyContentDataDeliver()
            self.deliver = temp_model.from_map(m.get('deliver'))

        return self

class DescribeCdnReportResponseBodyContentDataDeliver(DaraModel):
    def __init__(
        self,
        report: main_models.DescribeCdnReportResponseBodyContentDataDeliverReport = None,
    ):
        self.report = report

    def validate(self):
        if self.report:
            self.report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report is not None:
            result['report'] = self.report.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('report') is not None:
            temp_model = main_models.DescribeCdnReportResponseBodyContentDataDeliverReport()
            self.report = temp_model.from_map(m.get('report'))

        return self

class DescribeCdnReportResponseBodyContentDataDeliverReport(DaraModel):
    def __init__(
        self,
        format: str = None,
        header: List[str] = None,
        out_line: int = None,
        out_size: int = None,
        shape: str = None,
        title: str = None,
    ):
        self.format = format
        self.header = header
        self.out_line = out_line
        self.out_size = out_size
        self.shape = shape
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['format'] = self.format

        if self.header is not None:
            result['header'] = self.header

        if self.out_line is not None:
            result['outLine'] = self.out_line

        if self.out_size is not None:
            result['outSize'] = self.out_size

        if self.shape is not None:
            result['shape'] = self.shape

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('header') is not None:
            self.header = m.get('header')

        if m.get('outLine') is not None:
            self.out_line = m.get('outLine')

        if m.get('outSize') is not None:
            self.out_size = m.get('outSize')

        if m.get('shape') is not None:
            self.shape = m.get('shape')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

