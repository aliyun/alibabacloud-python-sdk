# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDedicatedClusterMonitorRuleResponseBody(DaraModel):
    def __init__(
        self,
        cpu_alarm_threshold: str = None,
        dedicated_cluster_id: str = None,
        disk_alarm_threshold: str = None,
        du_alarm_threshold: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        mem_alarm_threshold: str = None,
        notice_switch: str = None,
        phones: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The alert threshold for CPU utilization. Unit: percentage.
        self.cpu_alarm_threshold = cpu_alarm_threshold
        # The ID of the cluster.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The alert threshold for disk usage. Unit: percentage.
        self.disk_alarm_threshold = disk_alarm_threshold
        # The alert threshold for DTS Unit (DU) usage. Unit: percentage.
        self.du_alarm_threshold = du_alarm_threshold
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The alert threshold for memory usage. Unit: percentage.
        self.mem_alarm_threshold = mem_alarm_threshold
        # Indicates whether the alert feature is enabled. Valid values:
        # 
        # *   **1**: The alert feature is enabled.
        # *   **0**: The alert feature is disabled.
        self.notice_switch = notice_switch
        # The mobile phone number to which alerts are sent. Separate multiple mobile phone numbers with commas (,).
        self.phones = phones
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_alarm_threshold is not None:
            result['CpuAlarmThreshold'] = self.cpu_alarm_threshold

        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.disk_alarm_threshold is not None:
            result['DiskAlarmThreshold'] = self.disk_alarm_threshold

        if self.du_alarm_threshold is not None:
            result['DuAlarmThreshold'] = self.du_alarm_threshold

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.mem_alarm_threshold is not None:
            result['MemAlarmThreshold'] = self.mem_alarm_threshold

        if self.notice_switch is not None:
            result['NoticeSwitch'] = self.notice_switch

        if self.phones is not None:
            result['Phones'] = self.phones

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuAlarmThreshold') is not None:
            self.cpu_alarm_threshold = m.get('CpuAlarmThreshold')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('DiskAlarmThreshold') is not None:
            self.disk_alarm_threshold = m.get('DiskAlarmThreshold')

        if m.get('DuAlarmThreshold') is not None:
            self.du_alarm_threshold = m.get('DuAlarmThreshold')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MemAlarmThreshold') is not None:
            self.mem_alarm_threshold = m.get('MemAlarmThreshold')

        if m.get('NoticeSwitch') is not None:
            self.notice_switch = m.get('NoticeSwitch')

        if m.get('Phones') is not None:
            self.phones = m.get('Phones')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

