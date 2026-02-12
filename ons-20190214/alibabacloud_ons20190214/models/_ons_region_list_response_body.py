# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsRegionListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsRegionListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.OnsRegionListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsRegionListResponseBodyData(DaraModel):
    def __init__(
        self,
        region_do: List[main_models.OnsRegionListResponseBodyDataRegionDo] = None,
    ):
        self.region_do = region_do

    def validate(self):
        if self.region_do:
            for v1 in self.region_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionDo'] = []
        if self.region_do is not None:
            for k1 in self.region_do:
                result['RegionDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_do = []
        if m.get('RegionDo') is not None:
            for k1 in m.get('RegionDo'):
                temp_model = main_models.OnsRegionListResponseBodyDataRegionDo()
                self.region_do.append(temp_model.from_map(k1))

        return self

class OnsRegionListResponseBodyDataRegionDo(DaraModel):
    def __init__(
        self,
        channel_name: str = None,
        create_time: int = None,
        id: int = None,
        ons_region_id: str = None,
        region_name: str = None,
        update_time: int = None,
    ):
        self.channel_name = channel_name
        self.create_time = create_time
        self.id = id
        self.ons_region_id = ons_region_id
        self.region_name = region_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.ons_region_id is not None:
            result['OnsRegionId'] = self.ons_region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OnsRegionId') is not None:
            self.ons_region_id = m.get('OnsRegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

