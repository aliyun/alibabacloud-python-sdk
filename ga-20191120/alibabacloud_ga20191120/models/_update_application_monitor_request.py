# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationMonitorRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        client_token: str = None,
        detect_enable: bool = None,
        detect_threshold: int = None,
        detect_times: int = None,
        listener_id: str = None,
        options_json: str = None,
        region_id: str = None,
        silence_time: int = None,
        task_id: str = None,
        task_name: str = None,
    ):
        # The URL or IP address that is probed.
        self.address = address
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to enable the automatic diagnostics feature. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.detect_enable = detect_enable
        # Set the threshold that is used to trigger the automatic diagnostics feature. If the liveness of the origin in percentile drops below the specified threshold, the automatic diagnostics feature is triggered.
        # 
        # Valid values: **0** to **100**.
        self.detect_threshold = detect_threshold
        # The number of times that the threshold must be reached before the automatic diagnostics feature is triggered.
        # 
        # Valid values: **1** to **20**.
        self.detect_times = detect_times
        # The ID of the listener that you want to modify. The listener runs the origin probing task.
        self.listener_id = listener_id
        # The extended options of the listener protocol that is used by the origin probing task. The options vary based on the listener protocol.
        self.options_json = options_json
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
        self.region_id = region_id
        # The silence period of the automatic diagnostics feature. This parameter specifies the interval at which the automatic diagnostics feature is triggered. If the availability rate does not return to normal after GA triggers an automatic diagnostic task, GA must wait until the silence period ends before GA can trigger another automatic diagnostic task.
        # 
        # If the number of consecutive times that the availability rate drops below the threshold of automatic diagnostics reaches the value of the **DetectTimes** parameter, the automatic diagnostics feature is triggered. The automatic diagnostics feature is not triggered again within the silence period even if the availability rate stays below the threshold. If the availability rate does not return to normal after the silence period ends, the automatic diagnostics feature is triggered again.
        # 
        # Unit: seconds. Valid values: **300** to **86400**.
        self.silence_time = silence_time
        # The ID of the origin probing task that you want to modify.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The name of the origin probing task.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

