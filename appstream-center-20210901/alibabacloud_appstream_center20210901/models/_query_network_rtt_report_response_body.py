# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class QueryNetworkRttReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        message: str = None,
        network_rtt_report_data_model: List[main_models.QueryNetworkRttReportResponseBodyNetworkRttReportDataModel] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The business status code. `200` indicates that the request is processed successfully. Other values indicate that the processing failed.
        self.code = code
        # The total number of records that meet the query conditions.
        self.count = count
        # The description of the request processing result. If the request is successful, `success` is usually returned.
        self.message = message
        # The list of network RTT report data.
        self.network_rtt_report_data_model = network_rtt_report_data_model
        # The page number corresponding to the current response.
        self.page_number = page_number
        # The number of entries per page used in the current response.
        self.page_size = page_size
        # The unique identifier of the request, which can be used to troubleshoot request issues.
        self.request_id = request_id

    def validate(self):
        if self.network_rtt_report_data_model:
            for v1 in self.network_rtt_report_data_model:
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

        if self.message is not None:
            result['Message'] = self.message

        result['NetworkRttReportDataModel'] = []
        if self.network_rtt_report_data_model is not None:
            for k1 in self.network_rtt_report_data_model:
                result['NetworkRttReportDataModel'].append(k1.to_map() if k1 else None)

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

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.network_rtt_report_data_model = []
        if m.get('NetworkRttReportDataModel') is not None:
            for k1 in m.get('NetworkRttReportDataModel'):
                temp_model = main_models.QueryNetworkRttReportResponseBodyNetworkRttReportDataModel()
                self.network_rtt_report_data_model.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryNetworkRttReportResponseBodyNetworkRttReportDataModel(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        low_rtt_user_count: int = None,
        low_rtt_user_rate: float = None,
        region_id: str = None,
        rtt_avg: float = None,
        rtt_max: float = None,
        rtt_min: float = None,
        stat_end_date: str = None,
        stat_start_date: str = None,
        total_user_count: int = None,
    ):
        # The ID of the app instance group.
        self.app_instance_group_id = app_instance_group_id
        # The number of users that meet the low-RTT criteria of the report. Unit: users. The current API operation does not return the specific threshold.
        self.low_rtt_user_count = low_rtt_user_count
        # The ratio of low-RTT users to the total number of users involved in the statistics. Valid values: 0 to 1. To obtain the percentage, multiply the value by 100.
        self.low_rtt_user_rate = low_rtt_user_rate
        # The ID of the business region to which the report data belongs.
        self.region_id = region_id
        # The average RTT of all users involved in the statistics. Unit: milliseconds.
        self.rtt_avg = rtt_avg
        # The maximum value among the average RTTs of all users. Unit: milliseconds.
        self.rtt_max = rtt_max
        # The minimum value among the average RTTs of all users. Unit: milliseconds.
        self.rtt_min = rtt_min
        # The end time of the statistical window. Format: `yyyy-MM-dd HH:mm:ss`. The string itself does not carry a time zone and is interpreted as Asia/Shanghai (UTC+8).
        self.stat_end_date = stat_end_date
        # The start time of the statistical window. Format: `yyyy-MM-dd HH:mm:ss`. The string itself does not carry a time zone and is interpreted as Asia/Shanghai (UTC+8).
        self.stat_start_date = stat_start_date
        # The total number of users involved in the RTT calculation for the current statistical window. Unit: users.
        self.total_user_count = total_user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.low_rtt_user_count is not None:
            result['LowRttUserCount'] = self.low_rtt_user_count

        if self.low_rtt_user_rate is not None:
            result['LowRttUserRate'] = self.low_rtt_user_rate

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rtt_avg is not None:
            result['RttAvg'] = self.rtt_avg

        if self.rtt_max is not None:
            result['RttMax'] = self.rtt_max

        if self.rtt_min is not None:
            result['RttMin'] = self.rtt_min

        if self.stat_end_date is not None:
            result['StatEndDate'] = self.stat_end_date

        if self.stat_start_date is not None:
            result['StatStartDate'] = self.stat_start_date

        if self.total_user_count is not None:
            result['TotalUserCount'] = self.total_user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('LowRttUserCount') is not None:
            self.low_rtt_user_count = m.get('LowRttUserCount')

        if m.get('LowRttUserRate') is not None:
            self.low_rtt_user_rate = m.get('LowRttUserRate')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RttAvg') is not None:
            self.rtt_avg = m.get('RttAvg')

        if m.get('RttMax') is not None:
            self.rtt_max = m.get('RttMax')

        if m.get('RttMin') is not None:
            self.rtt_min = m.get('RttMin')

        if m.get('StatEndDate') is not None:
            self.stat_end_date = m.get('StatEndDate')

        if m.get('StatStartDate') is not None:
            self.stat_start_date = m.get('StatStartDate')

        if m.get('TotalUserCount') is not None:
            self.total_user_count = m.get('TotalUserCount')

        return self

