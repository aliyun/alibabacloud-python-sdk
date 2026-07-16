# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class BatchCreateInstantSiteMonitorRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        task_list: List[main_models.BatchCreateInstantSiteMonitorRequestTaskList] = None,
    ):
        self.region_id = region_id
        # The list of site monitoring tasks.
        # 
        # > You must create at least one site monitoring task. The `Address`, `TaskName`, and `TaskType` parameters are required.
        # 
        # This parameter is required.
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for v1 in self.task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['TaskList'] = []
        if self.task_list is not None:
            for k1 in self.task_list:
                result['TaskList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.task_list = []
        if m.get('TaskList') is not None:
            for k1 in m.get('TaskList'):
                temp_model = main_models.BatchCreateInstantSiteMonitorRequestTaskList()
                self.task_list.append(temp_model.from_map(k1))

        return self

class BatchCreateInstantSiteMonitorRequestTaskList(DaraModel):
    def __init__(
        self,
        address: str = None,
        isp_cities: str = None,
        options_json: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The URL or IP address of the site monitoring task.
        # 
        # > You must create at least one site monitoring task. The `Address`, `TaskName`, and `TaskType` parameters are required.
        self.address = address
        # The information about the detection points. If you leave this parameter empty, the system randomly selects three detection points.
        # 
        # The value must be a `JSONArray`. For example, `[{"city":"546","isp":"465"},{"city":"572","isp":"465"},{"city":"738","isp":"465"}]` corresponds to Beijing, Hangzhou, and Qingdao.
        # 
        # For more information about how to obtain detection point information, see [DescribeSiteMonitorISPCityList](https://help.aliyun.com/document_detail/115045.html).
        self.isp_cities = isp_cities
        # The advanced extension options for the protocol type of the site monitoring task. Different protocol types correspond to different extension options.
        self.options_json = options_json
        # The name of the site monitoring task.
        # 
        # <props="china">
        # 
        # The value must be 4 to 100 characters in length and can contain English letters, numbers, underscores (_), and Chinese characters.
        # 
        # 
        # 
        # <props="intl">
        # 
        # The name of the site monitoring task.
        # 
        # 
        # 
        # <props="partner">
        # 
        # The name must be 4 to 100 characters in length and can contain letters, digits, and underscores (_).
        # 
        # 
        # 
        # > You must create at least one site monitoring task. The `Address`, `TaskName`, and `TaskType` parameters are required.
        self.task_name = task_name
        # The protocol type of the monitoring task.
        # 
        # Valid values: HTTP, PING, TCP, UDP, DNS, SMTP, POP3, and FTP.
        # 
        # > You must create at least one site monitoring task. The `Address`, `TaskName`, and `TaskType` parameters are required.
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

        if self.isp_cities is not None:
            result['IspCities'] = self.isp_cities

        if self.options_json is not None:
            result['OptionsJson'] = self.options_json

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('IspCities') is not None:
            self.isp_cities = m.get('IspCities')

        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

