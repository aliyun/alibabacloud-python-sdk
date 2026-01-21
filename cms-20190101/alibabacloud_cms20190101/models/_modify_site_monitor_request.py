# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySiteMonitorRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        alert_ids: str = None,
        custom_schedule: str = None,
        interval: str = None,
        interval_unit: str = None,
        isp_cities: str = None,
        options_json: str = None,
        region_id: str = None,
        task_id: str = None,
        task_name: str = None,
    ):
        # The URL or IP address that is monitored by the task.
        self.address = address
        # The ID of the alert rule. You can call the DescribeMetricRuleList operation to query the IDs of existing alert rules in CloudMonitor. For more information, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        self.alert_ids = alert_ids
        # The custom detection period. You can only select a time period from Monday to Sunday for detection.
        self.custom_schedule = custom_schedule
        # The interval at which detection requests are sent. Valid values: 1, 5, and 15. Unit: minutes. Default value: 1.
        self.interval = interval
        # The unit of the metric.
        # 
        # Unit: milliseconds.
        self.interval_unit = interval_unit
        # The information of the detection points. The value is a JSON array. Example: `[{"city":"546","isp":"465"},{"city":"572","isp":"465"},{"city":"738","isp":"465"}]`. The values of the `city` field indicate Beijing, Hangzhou, and Qingdao.
        # 
        # > You can call the DescribeSiteMonitorISPCityList operation to query the detection points. For more information, see [DescribeSiteMonitorISPCityList](https://help.aliyun.com/document_detail/115045.html). If you leave this parameter empty, the system randomly selects three detection points.
        self.isp_cities = isp_cities
        # The extended options of the protocol that is used by the site monitoring task. The options vary based on the protocol.
        self.options_json = options_json
        self.region_id = region_id
        # The ID of the site monitoring task.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The name of the site monitoring task. The name must be 4 to 100 characters in length, and can contain letters, digits, and underscores (_).
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

        if self.alert_ids is not None:
            result['AlertIds'] = self.alert_ids

        if self.custom_schedule is not None:
            result['CustomSchedule'] = self.custom_schedule

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.interval_unit is not None:
            result['IntervalUnit'] = self.interval_unit

        if self.isp_cities is not None:
            result['IspCities'] = self.isp_cities

        if self.options_json is not None:
            result['OptionsJson'] = self.options_json

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AlertIds') is not None:
            self.alert_ids = m.get('AlertIds')

        if m.get('CustomSchedule') is not None:
            self.custom_schedule = m.get('CustomSchedule')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IntervalUnit') is not None:
            self.interval_unit = m.get('IntervalUnit')

        if m.get('IspCities') is not None:
            self.isp_cities = m.get('IspCities')

        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

