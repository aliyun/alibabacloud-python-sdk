# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListApplicationMonitorResponseBody(DaraModel):
    def __init__(
        self,
        application_monitors: List[main_models.ListApplicationMonitorResponseBodyApplicationMonitors] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of origin probing tasks.
        self.application_monitors = application_monitors
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.application_monitors:
            for v1 in self.application_monitors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationMonitors'] = []
        if self.application_monitors is not None:
            for k1 in self.application_monitors:
                result['ApplicationMonitors'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_monitors = []
        if m.get('ApplicationMonitors') is not None:
            for k1 in m.get('ApplicationMonitors'):
                temp_model = main_models.ListApplicationMonitorResponseBodyApplicationMonitors()
                self.application_monitors.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationMonitorResponseBodyApplicationMonitors(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        address: str = None,
        detect_enable: bool = None,
        detect_threshold: int = None,
        detect_times: int = None,
        listener_id: str = None,
        options_json: str = None,
        silence_time: int = None,
        state: str = None,
        task_id: str = None,
        task_name: str = None,
    ):
        # The ID of the GA instance on which the origin probing task runs.
        self.accelerator_id = accelerator_id
        # The URL or IP address that was probed.
        self.address = address
        # Indicates whether the automatic diagnostics feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.detect_enable = detect_enable
        # The threshold that is used to trigger the automatic diagnostics feature.
        self.detect_threshold = detect_threshold
        # The number of times that are required to reach the threshold before the automatic diagnostics feature can be triggered.
        self.detect_times = detect_times
        # The ID of the listener on which the origin probing task runs.
        self.listener_id = listener_id
        # The extended options of the listener protocol that is used by the origin probing task. The options vary based on the listener protocol.
        self.options_json = options_json
        # The silence period of the automatic diagnostics feature. This parameter indicates the interval at which the automatic diagnostics feature is triggered. If the availability rate does not return to normal after GA triggers an automatic diagnostic task, GA must wait until the silence period ends before GA can trigger another automatic diagnostic task.
        # 
        # If the number of consecutive times that the availability rate drops below the threshold of automatic diagnostics reaches the value of **DetectTimes** , the automatic diagnostics feature is triggered. The automatic diagnostics feature is not triggered again within the silence period even if the availability rate stays below the threshold. If the availability rate does not return to normal after the silence period ends, the automatic diagnostics feature is triggered again.
        # 
        # Unit: seconds.
        self.silence_time = silence_time
        # The status of the origin probing task. Valid values:
        # 
        # *   **active:** The origin probing task is running.
        # *   **inactive:** The origin probing task is stopped.
        # *   **init:** The origin probing task is being initialized.
        # *   **deleting:** The origin probing task is being deleted.
        self.state = state
        # The origin probing task ID.
        self.task_id = task_id
        # The origin probing task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.address is not None:
            result['Address'] = self.address

        if self.detect_enable is not None:
            result['DetectEnable'] = self.detect_enable

        if self.detect_threshold is not None:
            result['DetectThreshold'] = self.detect_threshold

        if self.detect_times is not None:
            result['DetectTimes'] = self.detect_times

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.options_json is not None:
            result['OptionsJson'] = self.options_json

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.state is not None:
            result['State'] = self.state

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('DetectEnable') is not None:
            self.detect_enable = m.get('DetectEnable')

        if m.get('DetectThreshold') is not None:
            self.detect_threshold = m.get('DetectThreshold')

        if m.get('DetectTimes') is not None:
            self.detect_times = m.get('DetectTimes')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

