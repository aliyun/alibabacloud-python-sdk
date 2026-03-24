# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnDeliverListResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.DescribeCdnDeliverListResponseBodyContent = None,
        request_id: str = None,
    ):
        # The information about the tracking task.
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
            temp_model = main_models.DescribeCdnDeliverListResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCdnDeliverListResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeCdnDeliverListResponseBodyContentData] = None,
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
                temp_model = main_models.DescribeCdnDeliverListResponseBodyContentData()
                self.data.append(temp_model.from_map(k1))

        return self

class DescribeCdnDeliverListResponseBodyContentData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        crontab: str = None,
        deliver: main_models.DescribeCdnDeliverListResponseBodyContentDataDeliver = None,
        deliver_id: int = None,
        dm_list: List[str] = None,
        frequency: str = None,
        name: str = None,
        reports: List[main_models.DescribeCdnDeliverListResponseBodyContentDataReports] = None,
        status: str = None,
        time_end_format: str = None,
        time_from_format: str = None,
    ):
        self.create_time = create_time
        self.crontab = crontab
        self.deliver = deliver
        self.deliver_id = deliver_id
        self.dm_list = dm_list
        self.frequency = frequency
        self.name = name
        self.reports = reports
        self.status = status
        self.time_end_format = time_end_format
        self.time_from_format = time_from_format

    def validate(self):
        if self.deliver:
            self.deliver.validate()
        if self.reports:
            for v1 in self.reports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.crontab is not None:
            result['crontab'] = self.crontab

        if self.deliver is not None:
            result['deliver'] = self.deliver.to_map()

        if self.deliver_id is not None:
            result['deliverId'] = self.deliver_id

        if self.dm_list is not None:
            result['dmList'] = self.dm_list

        if self.frequency is not None:
            result['frequency'] = self.frequency

        if self.name is not None:
            result['name'] = self.name

        result['reports'] = []
        if self.reports is not None:
            for k1 in self.reports:
                result['reports'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.time_end_format is not None:
            result['timeEndFormat'] = self.time_end_format

        if self.time_from_format is not None:
            result['timeFromFormat'] = self.time_from_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('crontab') is not None:
            self.crontab = m.get('crontab')

        if m.get('deliver') is not None:
            temp_model = main_models.DescribeCdnDeliverListResponseBodyContentDataDeliver()
            self.deliver = temp_model.from_map(m.get('deliver'))

        if m.get('deliverId') is not None:
            self.deliver_id = m.get('deliverId')

        if m.get('dmList') is not None:
            self.dm_list = m.get('dmList')

        if m.get('frequency') is not None:
            self.frequency = m.get('frequency')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.reports = []
        if m.get('reports') is not None:
            for k1 in m.get('reports'):
                temp_model = main_models.DescribeCdnDeliverListResponseBodyContentDataReports()
                self.reports.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('timeEndFormat') is not None:
            self.time_end_format = m.get('timeEndFormat')

        if m.get('timeFromFormat') is not None:
            self.time_from_format = m.get('timeFromFormat')

        return self

class DescribeCdnDeliverListResponseBodyContentDataReports(DaraModel):
    def __init__(
        self,
        report_id: int = None,
    ):
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.report_id is not None:
            result['reportId'] = self.report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        return self

class DescribeCdnDeliverListResponseBodyContentDataDeliver(DaraModel):
    def __init__(
        self,
        email: main_models.DescribeCdnDeliverListResponseBodyContentDataDeliverEmail = None,
    ):
        self.email = email

    def validate(self):
        if self.email:
            self.email.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['email'] = self.email.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            temp_model = main_models.DescribeCdnDeliverListResponseBodyContentDataDeliverEmail()
            self.email = temp_model.from_map(m.get('email'))

        return self

class DescribeCdnDeliverListResponseBodyContentDataDeliverEmail(DaraModel):
    def __init__(
        self,
        to: List[str] = None,
    ):
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.to is not None:
            result['to'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('to') is not None:
            self.to = m.get('to')

        return self

