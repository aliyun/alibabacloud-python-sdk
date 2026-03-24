# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnSubListResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.DescribeCdnSubListResponseBodyContent = None,
        request_id: str = None,
    ):
        # The information about the custom report task.
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
            temp_model = main_models.DescribeCdnSubListResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCdnSubListResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeCdnSubListResponseBodyContentData] = None,
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
                temp_model = main_models.DescribeCdnSubListResponseBodyContentData()
                self.data.append(temp_model.from_map(k1))

        return self

class DescribeCdnSubListResponseBodyContentData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        domains: List[str] = None,
        effective_end: str = None,
        effective_from: str = None,
        report_id: List[int] = None,
        status: str = None,
        sub_id: int = None,
    ):
        self.create_time = create_time
        self.domains = domains
        self.effective_end = effective_end
        self.effective_from = effective_from
        self.report_id = report_id
        self.status = status
        self.sub_id = sub_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.domains is not None:
            result['domains'] = self.domains

        if self.effective_end is not None:
            result['effectiveEnd'] = self.effective_end

        if self.effective_from is not None:
            result['effectiveFrom'] = self.effective_from

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.status is not None:
            result['status'] = self.status

        if self.sub_id is not None:
            result['subId'] = self.sub_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('domains') is not None:
            self.domains = m.get('domains')

        if m.get('effectiveEnd') is not None:
            self.effective_end = m.get('effectiveEnd')

        if m.get('effectiveFrom') is not None:
            self.effective_from = m.get('effectiveFrom')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subId') is not None:
            self.sub_id = m.get('subId')

        return self

