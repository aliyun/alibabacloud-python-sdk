# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeJobMonitorRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        dts_job_id: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        monitor_rules: List[main_models.DescribeJobMonitorRuleResponseBodyMonitorRules] = None,
        request_id: str = None,
        success: bool = None,
        topics: List[str] = None,
    ):
        # The error code. This parameter will be removed in the future.
        self.code = code
        # The ID of the data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The dynamic part in the error message. This parameter is used to replace the **%s** variable in the **ErrMessage** parameter.
        # 
        # >  If the specified **DtsJobId** parameter is invalid, **The Value of Input Parameter %s is not valid** is returned for **ErrMessage** and **DtsJobId** is returned for **DynamicMessage**.
        self.dynamic_message = dynamic_message
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The monitoring rules of the DTS task.
        self.monitor_rules = monitor_rules
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**: The call was successful.
        # *   **false**:The call failed.
        self.success = success
        # The topics of all subtasks in the distributed change tracking task.
        self.topics = topics

    def validate(self):
        if self.monitor_rules:
            for v1 in self.monitor_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['MonitorRules'] = []
        if self.monitor_rules is not None:
            for k1 in self.monitor_rules:
                result['MonitorRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.topics is not None:
            result['Topics'] = self.topics

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.monitor_rules = []
        if m.get('MonitorRules') is not None:
            for k1 in m.get('MonitorRules'):
                temp_model = main_models.DescribeJobMonitorRuleResponseBodyMonitorRules()
                self.monitor_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Topics') is not None:
            self.topics = m.get('Topics')

        return self

class DescribeJobMonitorRuleResponseBodyMonitorRules(DaraModel):
    def __init__(
        self,
        delay_rule_time: int = None,
        job_id: str = None,
        job_type: str = None,
        notice_value: int = None,
        period: int = None,
        phone: str = None,
        state: str = None,
        times: int = None,
        type: str = None,
    ):
        # The threshold that triggers the alert.
        # 
        # *   If the request parameter **Type** of the [CreateJobMonitorRule](https://help.aliyun.com/document_detail/212332.html) operation is set to **delay**, the unit of DelayRuleTime is seconds.
        # *   If the request parameter **Type** of the [CreateJobMonitorRule](https://help.aliyun.com/document_detail/212332.html) operation is set to **full_timeout**, the unit of DelayRuleTime is hours.
        self.delay_rule_time = delay_rule_time
        # Task ID.
        self.job_id = job_id
        # The task type of the DTS instance, with values: - **normal**: Migration or synchronization task. - **full_check**: Associated full check task. - **etl_check**: Associated incremental check task.
        self.job_type = job_type
        # Alarm threshold.
        self.notice_value = notice_value
        # The statistical period for incremental validation tasks, in minutes.
        # > Currently supported values are 1 minute, 5 minutes, 10 minutes, and 30 minutes.
        self.period = period
        # The mobile phone numbers that receive alert notifications. Multiple mobile numbers are separated by commas (,).
        self.phone = phone
        # Indicates whether the monitoring rule is enabled. Valid values:
        # 
        # *   **Y**: The monitoring rule is enabled.
        # *   **N**: The monitoring rule is disabled.
        self.state = state
        # The number of cycles for the incremental validation task.
        self.times = times
        # The type of the monitoring rule. Valid values:
        # 
        # *   **delay**: If the task latency reaches the threshold, an alert is triggered.
        # *   **error**: If an exception occurs, an alert is triggered.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.notice_value is not None:
            result['NoticeValue'] = self.notice_value

        if self.period is not None:
            result['Period'] = self.period

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.state is not None:
            result['State'] = self.state

        if self.times is not None:
            result['Times'] = self.times

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('NoticeValue') is not None:
            self.notice_value = m.get('NoticeValue')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

