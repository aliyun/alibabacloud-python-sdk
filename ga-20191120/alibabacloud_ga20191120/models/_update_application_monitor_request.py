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
        # The URL or IP address to be probed.
        self.address = address
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** value as the **ClientToken** value. The **RequestId** value of each API request is different.
        self.client_token = client_token
        # Specifies whether to enable the automatic diagnostics feature. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false** (default): Disabled.
        self.detect_enable = detect_enable
        # The threshold that triggers automatic diagnostics. When the origin availability rate falls below this threshold, automatic diagnostics is triggered.
        # 
        # Valid values: **0** to **100**.
        self.detect_threshold = detect_threshold
        # The number of consecutive times that the availability rate must fall below the threshold before automatic diagnostics is triggered.
        # 
        # Valid values: **1** to **20**.
        self.detect_times = detect_times
        # The instance ID of the listener associated with the origin probing task that you want to modify.
        self.listener_id = listener_id
        # The advanced extension options for the listener protocol type of the origin probing task. Different listener protocol types correspond to different extension options.
        self.options_json = options_json
        # The region ID of the Alibaba Cloud Global Accelerator (GA) instance. Set the value to **cn-hangzhou**.
        self.region_id = region_id
        # The silence period for automatic diagnostics. This specifies the interval between automatic diagnostics triggers when the availability rate does not recover to normal after diagnostics is triggered.
        # 
        # When the availability rate falls below the automatic diagnostics threshold for consecutive times (as specified by **DetectTimes**), automatic diagnostics is triggered. If the availability rate remains below the threshold during the silence period, automatic diagnostics is not triggered again within the silence period. If the availability rate has not recovered after the silence period expires, automatic diagnostics is triggered again.
        # 
        # Unit: seconds. Valid values: **300** to **86400**.
        self.silence_time = silence_time
        # The ID of the origin probing task that you want to modify.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The name of the origin probing task.
        # 
        # The name must be 1 to 128 characters in length and must start with a letter or a Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
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

