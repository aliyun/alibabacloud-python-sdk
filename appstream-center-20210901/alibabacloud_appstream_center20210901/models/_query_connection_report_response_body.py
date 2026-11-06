# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class QueryConnectionReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        connection_report_data_model: List[main_models.QueryConnectionReportResponseBodyConnectionReportDataModel] = None,
        count: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The business status code. `200` indicates that the request is successful. Other values indicate that the request failed.
        self.code = code
        # The list of connection report data.
        self.connection_report_data_model = connection_report_data_model
        # The total number of records that meet the query conditions.
        self.count = count
        # The description of the request processing result. `success` is usually returned when the request is successful.
        self.message = message
        # The page number corresponding to the current response.
        self.page_number = page_number
        # The number of entries per page used in the current response.
        self.page_size = page_size
        # The unique identifier of the current request, which can be used to troubleshoot the request.
        self.request_id = request_id

    def validate(self):
        if self.connection_report_data_model:
            for v1 in self.connection_report_data_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['ConnectionReportDataModel'] = []
        if self.connection_report_data_model is not None:
            for k1 in self.connection_report_data_model:
                result['ConnectionReportDataModel'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

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

        self.connection_report_data_model = []
        if m.get('ConnectionReportDataModel') is not None:
            for k1 in m.get('ConnectionReportDataModel'):
                temp_model = main_models.QueryConnectionReportResponseBodyConnectionReportDataModel()
                self.connection_report_data_model.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryConnectionReportResponseBodyConnectionReportDataModel(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        connection_avg_duration_seconds: float = None,
        connection_failure_count: int = None,
        connection_success_count: int = None,
        connection_success_rate: float = None,
        region_id: str = None,
        stat_end_date: str = None,
        stat_start_date: str = None,
    ):
        # The ID of the app instance group.
        self.app_instance_group_id = app_instance_group_id
        # The average duration of successful connections. In the current version, the return value is in milliseconds, so parse it as milliseconds. The `Seconds` in the field name is retained for compatibility and does not indicate the unit. This value may not be returned if there are no successful connections.
        self.connection_avg_duration_seconds = connection_avg_duration_seconds
        # The number of connection failures within the statistical window.
        self.connection_failure_count = connection_failure_count
        # The number of successful connections within the statistical window.
        self.connection_success_count = connection_success_count
        # The connection success rate, which is calculated by dividing the number of successful connections by the sum of successful and failed connections. The value ranges from 0 to 1. Multiply the value by 100 to get the percentage. This value may not be returned if there are no connection records.
        self.connection_success_rate = connection_success_rate
        # The ID of the business region to which the report data belongs.
        self.region_id = region_id
        # The end time of the statistical window. Format: `yyyy-MM-dd HH:mm:ss`. The string itself does not carry a time zone and is interpreted in the Asia/Shanghai (UTC+8) time zone.
        self.stat_end_date = stat_end_date
        # The start time of the statistical window. Format: `yyyy-MM-dd HH:mm:ss`. The string itself does not carry a time zone and is interpreted in the Asia/Shanghai (UTC+8) time zone.
        self.stat_start_date = stat_start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.connection_avg_duration_seconds is not None:
            result['ConnectionAvgDurationSeconds'] = self.connection_avg_duration_seconds

        if self.connection_failure_count is not None:
            result['ConnectionFailureCount'] = self.connection_failure_count

        if self.connection_success_count is not None:
            result['ConnectionSuccessCount'] = self.connection_success_count

        if self.connection_success_rate is not None:
            result['ConnectionSuccessRate'] = self.connection_success_rate

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stat_end_date is not None:
            result['StatEndDate'] = self.stat_end_date

        if self.stat_start_date is not None:
            result['StatStartDate'] = self.stat_start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('ConnectionAvgDurationSeconds') is not None:
            self.connection_avg_duration_seconds = m.get('ConnectionAvgDurationSeconds')

        if m.get('ConnectionFailureCount') is not None:
            self.connection_failure_count = m.get('ConnectionFailureCount')

        if m.get('ConnectionSuccessCount') is not None:
            self.connection_success_count = m.get('ConnectionSuccessCount')

        if m.get('ConnectionSuccessRate') is not None:
            self.connection_success_rate = m.get('ConnectionSuccessRate')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StatEndDate') is not None:
            self.stat_end_date = m.get('StatEndDate')

        if m.get('StatStartDate') is not None:
            self.stat_start_date = m.get('StatStartDate')

        return self

