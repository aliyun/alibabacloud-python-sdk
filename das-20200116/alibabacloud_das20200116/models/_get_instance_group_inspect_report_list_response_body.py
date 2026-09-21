# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetInstanceGroupInspectReportListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetInstanceGroupInspectReportListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response status code.
        self.code = code
        # List<ReportStatus>
        self.data = data
        # The response message.
        # >If the request is successful, **Successful** is returned. If the request fails, exception information such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # * **true**: The request is successful.
        # * **false**: The request fails.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetInstanceGroupInspectReportListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInstanceGroupInspectReportListResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        report_date: str = None,
        report_id: str = None,
        status: str = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The date of the diagnosis.
        self.report_date = report_date
        # The report ID.
        self.report_id = report_id
        # The task status. Valid values: WAITING_UNREADY = 0, WAITING_READY = 1, PROCESSING = 2, FINISHED = 3, ERROR = 4, STOPPED = -1.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.report_date is not None:
            result['ReportDate'] = self.report_date

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ReportDate') is not None:
            self.report_date = m.get('ReportDate')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

