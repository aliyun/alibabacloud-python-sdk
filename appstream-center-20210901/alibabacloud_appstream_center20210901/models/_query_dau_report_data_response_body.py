# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class QueryDauReportDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        dau_report_data_model: List[main_models.QueryDauReportDataResponseBodyDauReportDataModel] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The business status code. A value of 200 indicates that the request is processed successfully. Other values indicate that the processing failed.
        self.code = code
        # The total number of records that meet the query conditions.
        self.count = count
        # The list of daily active user report data.
        self.dau_report_data_model = dau_report_data_model
        # The description of the request processing result. Typically, success is returned if the request is successful.
        self.message = message
        # The page number corresponding to the current response.
        self.page_number = page_number
        # The number of records per page used in the current response.
        self.page_size = page_size
        # The unique identifier of the request, which can be used to troubleshoot request issues.
        self.request_id = request_id

    def validate(self):
        if self.dau_report_data_model:
            for v1 in self.dau_report_data_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['DauReportDataModel'] = []
        if self.dau_report_data_model is not None:
            for k1 in self.dau_report_data_model:
                result['DauReportDataModel'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.dau_report_data_model = []
        if m.get('DauReportDataModel') is not None:
            for k1 in m.get('DauReportDataModel'):
                temp_model = main_models.QueryDauReportDataResponseBodyDauReportDataModel()
                self.dau_report_data_model.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDauReportDataResponseBodyDauReportDataModel(DaraModel):
    def __init__(
        self,
        dau: int = None,
        stat_date: str = None,
        streaming_dau: int = None,
    ):
        # The number of active users within the statistical epoch. Unit: users.
        self.dau = dau
        # The statistics date. Format: yyyy-MM-dd. The string does not contain a time zone and is interpreted as a natural date in the Asia/Shanghai (UTC+8) time zone.
        self.stat_date = stat_date
        # The number of active users who generated sessions through streaming access within the statistical epoch. Unit: users.
        self.streaming_dau = streaming_dau

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dau is not None:
            result['Dau'] = self.dau

        if self.stat_date is not None:
            result['StatDate'] = self.stat_date

        if self.streaming_dau is not None:
            result['StreamingDau'] = self.streaming_dau

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dau') is not None:
            self.dau = m.get('Dau')

        if m.get('StatDate') is not None:
            self.stat_date = m.get('StatDate')

        if m.get('StreamingDau') is not None:
            self.streaming_dau = m.get('StreamingDau')

        return self

