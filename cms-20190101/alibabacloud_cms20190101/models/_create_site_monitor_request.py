# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSiteMonitorRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        agent_group: str = None,
        alert_ids: str = None,
        custom_schedule: str = None,
        interval: str = None,
        isp_cities: str = None,
        options_json: str = None,
        region_id: str = None,
        task_name: str = None,
        task_type: str = None,
        vpc_config: str = None,
    ):
        # The URL or IP address that is monitored by the task.
        # 
        # This parameter is required.
        self.address = address
        self.agent_group = agent_group
        # The ID of the alert rule.
        # 
        # For more information about how to obtain the ID of an alert rule, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        self.alert_ids = alert_ids
        # The custom detection period. You can only select a time period from Monday to Sunday for detection.
        self.custom_schedule = custom_schedule
        # The interval at which detection requests are sent.
        # 
        # Valid values: 1, 5, 15, 30, and 60. Unit: minutes.
        # 
        # Default value: 1.
        self.interval = interval
        # The information of the detection points. If you leave this parameter empty, the system randomly selects three detection points.
        # 
        # The value is a JSON array. Example: `[{"city":"546","isp":"465"},{"city":"572","isp":"465"},{"city":"738","isp":"465"}]`. The values of the city field indicate Beijing, Hangzhou, and Qingdao.
        # 
        # For information about how to obtain detection points, see [DescribeSiteMonitorISPCityList](https://help.aliyun.com/document_detail/115045.html).
        self.isp_cities = isp_cities
        # The extended options of the protocol that is used by the site monitoring task. The options vary based on the protocol.
        self.options_json = options_json
        self.region_id = region_id
        # The name of the site monitoring task.
        # 
        # The name must be 4 to 100 characters in length, and can contain letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.task_name = task_name
        # The protocol that is used by the site monitoring task.
        # 
        # Valid values: HTTP, HTTPS, PING, TCP, UDP, DNS, SMTP, POP3, FTP, and WEBSOCKET.
        # 
        # This parameter is required.
        self.task_type = task_type
        self.vpc_config = vpc_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.agent_group is not None:
            result['AgentGroup'] = self.agent_group

        if self.alert_ids is not None:
            result['AlertIds'] = self.alert_ids

        if self.custom_schedule is not None:
            result['CustomSchedule'] = self.custom_schedule

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.isp_cities is not None:
            result['IspCities'] = self.isp_cities

        if self.options_json is not None:
            result['OptionsJson'] = self.options_json

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.vpc_config is not None:
            result['VpcConfig'] = self.vpc_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AgentGroup') is not None:
            self.agent_group = m.get('AgentGroup')

        if m.get('AlertIds') is not None:
            self.alert_ids = m.get('AlertIds')

        if m.get('CustomSchedule') is not None:
            self.custom_schedule = m.get('CustomSchedule')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IspCities') is not None:
            self.isp_cities = m.get('IspCities')

        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('VpcConfig') is not None:
            self.vpc_config = m.get('VpcConfig')

        return self

