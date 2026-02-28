# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListLegacyQueueEventLogsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListLegacyQueueEventLogsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        if m.get('Data') is not None:
            temp_model = main_models.ListLegacyQueueEventLogsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListLegacyQueueEventLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListLegacyQueueEventLogsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListLegacyQueueEventLogsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLegacyQueueEventLogsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        acid: str = None,
        ani: str = None,
        answer_phone: str = None,
        answer_time: int = None,
        cause: str = None,
        dnis: str = None,
        id: int = None,
        queue_time: int = None,
        statistic_date: str = None,
        tenant_id: str = None,
        vq: str = None,
    ):
        self.acid = acid
        self.ani = ani
        self.answer_phone = answer_phone
        self.answer_time = answer_time
        self.cause = cause
        self.dnis = dnis
        self.id = id
        self.queue_time = queue_time
        self.statistic_date = statistic_date
        self.tenant_id = tenant_id
        self.vq = vq

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acid is not None:
            result['Acid'] = self.acid

        if self.ani is not None:
            result['Ani'] = self.ani

        if self.answer_phone is not None:
            result['AnswerPhone'] = self.answer_phone

        if self.answer_time is not None:
            result['AnswerTime'] = self.answer_time

        if self.cause is not None:
            result['Cause'] = self.cause

        if self.dnis is not None:
            result['Dnis'] = self.dnis

        if self.id is not None:
            result['Id'] = self.id

        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time

        if self.statistic_date is not None:
            result['StatisticDate'] = self.statistic_date

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.vq is not None:
            result['Vq'] = self.vq

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')

        if m.get('Ani') is not None:
            self.ani = m.get('Ani')

        if m.get('AnswerPhone') is not None:
            self.answer_phone = m.get('AnswerPhone')

        if m.get('AnswerTime') is not None:
            self.answer_time = m.get('AnswerTime')

        if m.get('Cause') is not None:
            self.cause = m.get('Cause')

        if m.get('Dnis') is not None:
            self.dnis = m.get('Dnis')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')

        if m.get('StatisticDate') is not None:
            self.statistic_date = m.get('StatisticDate')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Vq') is not None:
            self.vq = m.get('Vq')

        return self

