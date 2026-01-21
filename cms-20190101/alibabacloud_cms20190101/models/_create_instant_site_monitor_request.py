# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstantSiteMonitorRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        agent_group: str = None,
        isp_cities: str = None,
        options_json: str = None,
        random_isp_city: int = None,
        region_id: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The URL or IP address that you want to test.
        # 
        # This parameter is required.
        self.address = address
        self.agent_group = agent_group
        # The detection points. If you leave this parameter empty, the system randomly selects three detection points.
        # 
        # The value is a `JSON array`. Example: {"city":"546","isp":"465"},{"city":"572","isp":"465"},{"city":"738","isp":"465"}. The values of the city field indicate Beijing, Hangzhou, and Qingdao.
        # 
        # For information about how to obtain detection points, see [DescribeSiteMonitorISPCityList](https://help.aliyun.com/document_detail/115045.html).
        # 
        # > You must specify one of the `IspCities` and `RandomIspCity` parameters.
        self.isp_cities = isp_cities
        # The extended options of the protocol that is used by the instant test task. The options vary based on the protocol.
        self.options_json = options_json
        # The number of detection points.
        # 
        # > 
        # 
        # *   You must specify one of the `IspCities` and `RandomIspCity` parameters. If you specify the `RandomIspCity` parameter, the `IspCities` parameter automatically becomes invalid.
        self.random_isp_city = random_isp_city
        self.region_id = region_id
        # The name of the instant test task.
        # 
        # The name must be 4 to 100 characters in length, and can contain letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.task_name = task_name
        # The type of the instant test task. Valid values: HTTP, PING, TCP, UDP, and DNS.
        # 
        # This parameter is required.
        self.task_type = task_type

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

        if self.isp_cities is not None:
            result['IspCities'] = self.isp_cities

        if self.options_json is not None:
            result['OptionsJson'] = self.options_json

        if self.random_isp_city is not None:
            result['RandomIspCity'] = self.random_isp_city

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AgentGroup') is not None:
            self.agent_group = m.get('AgentGroup')

        if m.get('IspCities') is not None:
            self.isp_cities = m.get('IspCities')

        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')

        if m.get('RandomIspCity') is not None:
            self.random_isp_city = m.get('RandomIspCity')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

