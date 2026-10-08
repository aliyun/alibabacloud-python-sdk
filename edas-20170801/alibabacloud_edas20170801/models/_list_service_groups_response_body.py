# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListServiceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        service_groups_list: main_models.ListServiceGroupsResponseBodyServiceGroupsList = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.service_groups_list = service_groups_list

    def validate(self):
        if self.service_groups_list:
            self.service_groups_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_groups_list is not None:
            result['ServiceGroupsList'] = self.service_groups_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceGroupsList') is not None:
            temp_model = main_models.ListServiceGroupsResponseBodyServiceGroupsList()
            self.service_groups_list = temp_model.from_map(m.get('ServiceGroupsList'))

        return self

class ListServiceGroupsResponseBodyServiceGroupsList(DaraModel):
    def __init__(
        self,
        list_service_groups: List[main_models.ListServiceGroupsResponseBodyServiceGroupsListListServiceGroups] = None,
    ):
        self.list_service_groups = list_service_groups

    def validate(self):
        if self.list_service_groups:
            for v1 in self.list_service_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ListServiceGroups'] = []
        if self.list_service_groups is not None:
            for k1 in self.list_service_groups:
                result['ListServiceGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list_service_groups = []
        if m.get('ListServiceGroups') is not None:
            for k1 in m.get('ListServiceGroups'):
                temp_model = main_models.ListServiceGroupsResponseBodyServiceGroupsListListServiceGroups()
                self.list_service_groups.append(temp_model.from_map(k1))

        return self

class ListServiceGroupsResponseBodyServiceGroupsListListServiceGroups(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        self.create_time = create_time
        self.group_id = group_id
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

