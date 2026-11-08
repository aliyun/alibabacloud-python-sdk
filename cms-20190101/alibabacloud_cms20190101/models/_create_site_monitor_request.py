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
        # The URL or IP address of the monitoring task.
        # 
        # This parameter is required.
        self.address = address
        # The detection point group used by the monitoring task. Different options correspond to different detection point types. PC corresponds to PC clients, MOBIEL corresponds to mobile clients, and FC corresponds to VPC internal network detection. If this parameter is not specified, the default value is PC.
        self.agent_group = agent_group
        # The ID of the alert rule.
        # 
        # For more information about how to obtain the ID of an existing alert rule in CloudMonitor, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        self.alert_ids = alert_ids
        # The custom detection period. You can only select a specific time period from Monday to Sunday for detection.
        self.custom_schedule = custom_schedule
        # The monitoring frequency.
        # 
        # Valid values: 1 minute, 5 minutes, 15 minutes, 30 minutes, and 60 minutes.
        # 
        # Default value: 1 minute.
        self.interval = interval
        # The probe information. If this parameter is left empty, the system randomly selects three detection points.
        # 
        # The value is a JSON array. Example: `[{"city":"546","isp":"465"},{"city":"572","isp":"465"},{"city":"738","isp":"465"}]`, which correspond to Beijing, Hangzhou, and Qingdao.
        # 
        # For more information about how to obtain detection point information, see [DescribeSiteMonitorISPCityList](https://help.aliyun.com/document_detail/115045.html).
        self.isp_cities = isp_cities
        # The advanced extension options for the protocol type of the monitoring task. Different protocol types correspond to different extension options.
        self.options_json = options_json
        self.region_id = region_id
        # The name of the monitoring task.
        # 
        # The name must be 4 to 100 characters in length and can contain letters, digits, underscores (_), and Chinese characters.
        # 
        # This parameter is required.
        self.task_name = task_name
        # Site monitoring type of site monitoring task.
        # 
        # Valid values: HTTP(S), PING, TCP, UDP, DNS, SMTP, POP3, FTP, and WEBSOCKET.
        # 
        # This parameter is required.
        self.task_type = task_type
        # The network information required when creating a VPC internal network monitoring task. You must provide a JSON string that contains the following four fields: vpcId, vswitchId, securityGroupId, and region.
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

