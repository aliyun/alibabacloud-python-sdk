# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class QueryUserUsageReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        user_usage_report_data_model: List[main_models.QueryUserUsageReportResponseBodyUserUsageReportDataModel] = None,
    ):
        # The business status code. A value of 200 indicates that the request is successful. Other values indicate that the request failed.
        self.code = code
        # The total number of records that meet the query conditions.
        self.count = count
        # The description of the request processing result. Typically, success is returned when the request is successful.
        self.message = message
        # The page number corresponding to the current response.
        self.page_number = page_number
        # The number of entries per page used in the current response.
        self.page_size = page_size
        # The unique identifier of the request. You can use this ID to troubleshoot request issues.
        self.request_id = request_id
        # The list of user usage data, sorted in descending order of cumulative usage duration.
        self.user_usage_report_data_model = user_usage_report_data_model

    def validate(self):
        if self.user_usage_report_data_model:
            for v1 in self.user_usage_report_data_model:
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UserUsageReportDataModel'] = []
        if self.user_usage_report_data_model is not None:
            for k1 in self.user_usage_report_data_model:
                result['UserUsageReportDataModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

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

        self.user_usage_report_data_model = []
        if m.get('UserUsageReportDataModel') is not None:
            for k1 in m.get('UserUsageReportDataModel'):
                temp_model = main_models.QueryUserUsageReportResponseBodyUserUsageReportDataModel()
                self.user_usage_report_data_model.append(temp_model.from_map(k1))

        return self

class QueryUserUsageReportResponseBodyUserUsageReportDataModel(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        connection_status: str = None,
        last_connected_time: str = None,
        region_id: str = None,
        sessions_hold_duration: float = None,
        usage_duration: float = None,
        user_id: str = None,
    ):
        # The ID of the app instance group to which the user usage record belongs.
        self.app_instance_group_id = app_instance_group_id
        # The name of the app instance group to which the user usage record belongs.
        self.app_instance_group_name = app_instance_group_name
        # The current connection status of the user.
        # 
        # Valid values:
        # 
        # - `Connected`: At least one currently connected session exists.
        # - `Disconnected`: The session binding is retained, but no currently connected session exists.
        # - `Unbound`: No session binding exists.
        self.connection_status = connection_status
        # The last connection time. Format: `yyyy-MM-dd HH:mm:ss`. If no current or historical connection record exists, - is returned. The string itself does not carry a time zone and is interpreted as Asia/Shanghai (UTC+8).
        self.last_connected_time = last_connected_time
        # The current version does not return a valid region ID. Callers should not rely on this field. To filter by business region, use the BizRegionId request parameter.
        self.region_id = region_id
        # The cumulative session persistence duration within the query range. This is the duration during which the user occupies the session from session attach to session release. Multiple sessions under the same app instance group are accumulated. Unit: hours.
        self.sessions_hold_duration = sessions_hold_duration
        # The cumulative user usage duration within the query range. The usage duration of the same user under the same app instance group is aggregated by day. Unit: hours.
        self.usage_duration = usage_duration
        # The ID of the end user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.last_connected_time is not None:
            result['LastConnectedTime'] = self.last_connected_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sessions_hold_duration is not None:
            result['SessionsHoldDuration'] = self.sessions_hold_duration

        if self.usage_duration is not None:
            result['UsageDuration'] = self.usage_duration

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('LastConnectedTime') is not None:
            self.last_connected_time = m.get('LastConnectedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionsHoldDuration') is not None:
            self.sessions_hold_duration = m.get('SessionsHoldDuration')

        if m.get('UsageDuration') is not None:
            self.usage_duration = m.get('UsageDuration')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

