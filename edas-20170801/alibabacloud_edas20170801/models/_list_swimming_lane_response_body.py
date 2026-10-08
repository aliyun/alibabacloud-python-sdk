# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListSwimmingLaneResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListSwimmingLaneResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data that is returned.
        self.data = data
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSwimmingLaneResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSwimmingLaneResponseBodyData(DaraModel):
    def __init__(
        self,
        enable_rules: bool = None,
        entry_rule: str = None,
        group_id: int = None,
        id: int = None,
        name: str = None,
        namespace_id: str = None,
        scenario_sign: str = None,
        swimming_lane_app_relation_ship_list: List[main_models.ListSwimmingLaneResponseBodyDataSwimmingLaneAppRelationShipList] = None,
        tag: str = None,
    ):
        # Indicates whether the throttling rule is enabled.
        self.enable_rules = enable_rules
        # The conditions.
        self.entry_rule = entry_rule
        # The ID of the lane group.
        self.group_id = group_id
        # The ID of the lane.
        self.id = id
        # The name of the lane.
        self.name = name
        # The ID of the microservices namespace.
        self.namespace_id = namespace_id
        # The expected tag.
        self.scenario_sign = scenario_sign
        # The applications that are related to the lane.
        self.swimming_lane_app_relation_ship_list = swimming_lane_app_relation_ship_list
        # The tag.
        self.tag = tag

    def validate(self):
        if self.swimming_lane_app_relation_ship_list:
            for v1 in self.swimming_lane_app_relation_ship_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_rules is not None:
            result['EnableRules'] = self.enable_rules

        if self.entry_rule is not None:
            result['EntryRule'] = self.entry_rule

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.scenario_sign is not None:
            result['ScenarioSign'] = self.scenario_sign

        result['SwimmingLaneAppRelationShipList'] = []
        if self.swimming_lane_app_relation_ship_list is not None:
            for k1 in self.swimming_lane_app_relation_ship_list:
                result['SwimmingLaneAppRelationShipList'].append(k1.to_map() if k1 else None)

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableRules') is not None:
            self.enable_rules = m.get('EnableRules')

        if m.get('EntryRule') is not None:
            self.entry_rule = m.get('EntryRule')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('ScenarioSign') is not None:
            self.scenario_sign = m.get('ScenarioSign')

        self.swimming_lane_app_relation_ship_list = []
        if m.get('SwimmingLaneAppRelationShipList') is not None:
            for k1 in m.get('SwimmingLaneAppRelationShipList'):
                temp_model = main_models.ListSwimmingLaneResponseBodyDataSwimmingLaneAppRelationShipList()
                self.swimming_lane_app_relation_ship_list.append(temp_model.from_map(k1))

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

class ListSwimmingLaneResponseBodyDataSwimmingLaneAppRelationShipList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        extra: str = None,
        lane_id: int = None,
        rules: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # Additional information.
        self.extra = extra
        # The ID of the lane.
        self.lane_id = lane_id
        # The association rule.
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.lane_id is not None:
            result['LaneId'] = self.lane_id

        if self.rules is not None:
            result['Rules'] = self.rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('LaneId') is not None:
            self.lane_id = m.get('LaneId')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        return self

