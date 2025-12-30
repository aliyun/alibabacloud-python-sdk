# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class ListCloudGtmAvailableAlertGroupsResponseBody(DaraModel):
    def __init__(
        self,
        alert_groups: main_models.ListCloudGtmAvailableAlertGroupsResponseBodyAlertGroups = None,
        request_id: str = None,
    ):
        # The alert contact groups.
        self.alert_groups = alert_groups
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.alert_groups:
            self.alert_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_groups is not None:
            result['AlertGroups'] = self.alert_groups.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertGroups') is not None:
            temp_model = main_models.ListCloudGtmAvailableAlertGroupsResponseBodyAlertGroups()
            self.alert_groups = temp_model.from_map(m.get('AlertGroups'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCloudGtmAvailableAlertGroupsResponseBodyAlertGroups(DaraModel):
    def __init__(
        self,
        alert_group: List[main_models.ListCloudGtmAvailableAlertGroupsResponseBodyAlertGroupsAlertGroup] = None,
    ):
        self.alert_group = alert_group

    def validate(self):
        if self.alert_group:
            for v1 in self.alert_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertGroup'] = []
        if self.alert_group is not None:
            for k1 in self.alert_group:
                result['AlertGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_group = []
        if m.get('AlertGroup') is not None:
            for k1 in m.get('AlertGroup'):
                temp_model = main_models.ListCloudGtmAvailableAlertGroupsResponseBodyAlertGroupsAlertGroup()
                self.alert_group.append(temp_model.from_map(k1))

        return self

class ListCloudGtmAvailableAlertGroupsResponseBodyAlertGroupsAlertGroup(DaraModel):
    def __init__(
        self,
        group_name: str = None,
    ):
        # The name of the alert contact group.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

