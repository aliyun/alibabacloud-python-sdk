# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class QueryMauReportDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        mau_report_data_model: List[main_models.QueryMauReportDataResponseBodyMauReportDataModel] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The business status code. A value of `200` indicates that the request is processed successfully. Other values indicate that the request fails to be processed.
        self.code = code
        # The total number of entries that meet the query conditions.
        self.count = count
        # The list of monthly active user report data.
        self.mau_report_data_model = mau_report_data_model
        # The description of the request processing result. If the request is successful, `success` is usually returned.
        self.message = message
        # The page number corresponding to the current response.
        self.page_number = page_number
        # The number of entries per page used in the current response.
        self.page_size = page_size
        # The unique identifier of the request, which can be used to troubleshoot request issues.
        self.request_id = request_id

    def validate(self):
        if self.mau_report_data_model:
            for v1 in self.mau_report_data_model:
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

        result['MauReportDataModel'] = []
        if self.mau_report_data_model is not None:
            for k1 in self.mau_report_data_model:
                result['MauReportDataModel'].append(k1.to_map() if k1 else None)

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

        self.mau_report_data_model = []
        if m.get('MauReportDataModel') is not None:
            for k1 in m.get('MauReportDataModel'):
                temp_model = main_models.QueryMauReportDataResponseBodyMauReportDataModel()
                self.mau_report_data_model.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryMauReportDataResponseBodyMauReportDataModel(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        mau: int = None,
        region_id: str = None,
        stat_date: str = None,
        stat_month: str = None,
    ):
        # The app instance group ID.
        self.app_instance_group_id = app_instance_group_id
        # The number of monthly active users in the statistical month. Unit: users.
        self.mau = mau
        # The business region ID to which the report data belongs.
        self.region_id = region_id
        # The statistical cutoff date used for the month. Format: `yyyy-MM-dd`. For the last month, this is usually the day before the requested `EndDate`. The date is interpreted as a calendar date in the Asia/Shanghai (UTC+8) time zone.
        self.stat_date = stat_date
        # The statistical month. Format: `yyyy-MM`. The month is interpreted as a calendar month in the Asia/Shanghai (UTC+8) time zone.
        self.stat_month = stat_month

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.mau is not None:
            result['Mau'] = self.mau

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stat_date is not None:
            result['StatDate'] = self.stat_date

        if self.stat_month is not None:
            result['StatMonth'] = self.stat_month

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('Mau') is not None:
            self.mau = m.get('Mau')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StatDate') is not None:
            self.stat_date = m.get('StatDate')

        if m.get('StatMonth') is not None:
            self.stat_month = m.get('StatMonth')

        return self

