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
        # The URL or IP address of the detection task.
        # 
        # This parameter is required.
        self.address = address
        # The type of the detection point. Valid values: PC and MOBILE. PC indicates a fixed broadband detection point. MOBILE indicates a mobile detection point. Default value: PC.
        self.agent_group = agent_group
        # The information about the detection points. If this parameter is left empty, the system randomly selects three detection points.
        # 
        # The value is a JSON array. Example: [{"city":"546","isp":"465", "type":"IDC"},{"city":"572","isp":"465", "type":"LASTMILE"},{"city":"738","isp":"465"}], which correspond to Beijing, Hangzhou, and Qingdao.
        # 
        # type indicates the type of the detection point. When AgentGroup is set to PC, valid values are IDC and LASTMILE. IDC indicates a detection point deployed in a data center. LASTMILE indicates a detection point deployed in a residential area that uses a fixed broadband network. type is optional and defaults to IDC. When AgentGroup is set to MOBILE, you do not need to specify type.
        # 
        # For more information about how to obtain detection point information, see [DescribeSiteMonitorISPCityList](https://help.aliyun.com/document_detail/115045.html).
        # 
        # > You must specify either IspCities or RandomIspCity.
        self.isp_cities = isp_cities
        # The advanced extension options for the protocol type of the detection task. Different protocol types correspond to different extension options.
        self.options_json = options_json
        # The number of detection points.
        # 
        # > - You must specify either IspCities or RandomIspCity. - If you specify RandomIspCity, IspCities automatically becomes invalid.
        self.random_isp_city = random_isp_city
        self.region_id = region_id
        # The name of the detection task.
        # 
        # <props="china">The name must be 4 to 100 characters in length and can contain letters, digits, underscores (_), and Chinese characters.
        # 
        # 
        # <props="intl">The name must be 4 to 100 characters in length and can contain letters, digits, and underscores (_).
        # 
        # <props="partner">The name must be 4 to 100 characters in length and can contain letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.task_name = task_name
        # The type of the detection task. Valid values: HTTP, PING, TCP, UDP, and DNS.
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

