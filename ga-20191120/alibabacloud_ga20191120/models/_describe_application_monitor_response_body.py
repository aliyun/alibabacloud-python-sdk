# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationMonitorResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        address: str = None,
        detect_enable: bool = None,
        detect_threshold: int = None,
        detect_times: int = None,
        isp_city_list: List[main_models.DescribeApplicationMonitorResponseBodyIspCityList] = None,
        listener_id: str = None,
        options_json: str = None,
        region_id: str = None,
        request_id: str = None,
        silence_time: int = None,
        state: str = None,
        task_id: str = None,
        task_name: str = None,
    ):
        # The ID of the GA instance on which the origin probing task ran.
        self.accelerator_id = accelerator_id
        # The URL or IP address that was probed.
        self.address = address
        # Indicates whether the automatic diagnostics feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.detect_enable = detect_enable
        # The threshold that is used to trigger automatic diagnostics.
        # 
        # If the availability of the origin server drops below the specified threshold, the automatic diagnostics feature is triggered.
        self.detect_threshold = detect_threshold
        # The number of times that are required to reach the threshold before the automatic diagnostics feature is triggered.
        self.detect_times = detect_times
        # The probe points of the Internet service provider (ISP).
        self.isp_city_list = isp_city_list
        # The ID of the listener on which the origin probing task ran.
        self.listener_id = listener_id
        # The extended options of the listener protocol that is used by the origin probing task. The options vary based on the listener protocol.
        self.options_json = options_json
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The silence period of the automatic diagnostics feature. This parameter indicates the interval at which the automatic diagnostics feature is triggered. If the availability rate does not return to normal after GA triggers automatic diagnostics, GA must wait until the silence period ends before GA can trigger another automatic diagnostic.
        # 
        # If the number of consecutive times that the availability rate drops below the automatic diagnostics threshold reaches the value of **DetectTimes**, the automatic diagnostics feature is triggered. The automatic diagnostics feature is not triggered again within the silence period regardless of whether the availability rate remains below the threshold. If the availability rate does not return to normal after the silence period ends, the automatic diagnostics feature is triggered again.
        # 
        # Unit: seconds.
        self.silence_time = silence_time
        # The status of the origin probing task. Valid values:
        # 
        # *   **init**
        # *   **active**
        # *   **updating**
        # *   **inactive**
        # *   **deleting**
        self.state = state
        # The ID of the origin probing task.
        self.task_id = task_id
        # The name of the origin probing task.
        self.task_name = task_name

    def validate(self):
        if self.isp_city_list:
            for v1 in self.isp_city_list:
                 if v1:
                    v1.validate()

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

        result['IspCityList'] = []
        if self.isp_city_list is not None:
            for k1 in self.isp_city_list:
                result['IspCityList'].append(k1.to_map() if k1 else None)

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.options_json is not None:
            result['OptionsJson'] = self.options_json

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        self.isp_city_list = []
        if m.get('IspCityList') is not None:
            for k1 in m.get('IspCityList'):
                temp_model = main_models.DescribeApplicationMonitorResponseBodyIspCityList()
                self.isp_city_list.append(temp_model.from_map(k1))

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

class DescribeApplicationMonitorResponseBodyIspCityList(DaraModel):
    def __init__(
        self,
        city: str = None,
        city_name: str = None,
        isp: str = None,
        isp_name: str = None,
    ):
        # The ID of the city in which the probe point of the ISP is deployed.
        self.city = city
        # The name of the city in which the probe point of the ISP is deployed.
        self.city_name = city_name
        # The probe point ID of the ISP.
        self.isp = isp
        # The probe point name of the ISP.
        self.isp_name = isp_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        return self

