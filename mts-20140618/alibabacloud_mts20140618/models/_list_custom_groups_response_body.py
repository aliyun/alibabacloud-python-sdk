# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class ListCustomGroupsResponseBody(DaraModel):
    def __init__(
        self,
        custom_groups: main_models.ListCustomGroupsResponseBodyCustomGroups = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.custom_groups = custom_groups
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.custom_groups:
            self.custom_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_groups is not None:
            result['CustomGroups'] = self.custom_groups.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomGroups') is not None:
            temp_model = main_models.ListCustomGroupsResponseBodyCustomGroups()
            self.custom_groups = temp_model.from_map(m.get('CustomGroups'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomGroupsResponseBodyCustomGroups(DaraModel):
    def __init__(
        self,
        custom_group: List[main_models.ListCustomGroupsResponseBodyCustomGroupsCustomGroup] = None,
    ):
        self.custom_group = custom_group

    def validate(self):
        if self.custom_group:
            for v1 in self.custom_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomGroup'] = []
        if self.custom_group is not None:
            for k1 in self.custom_group:
                result['CustomGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_group = []
        if m.get('CustomGroup') is not None:
            for k1 in m.get('CustomGroup'):
                temp_model = main_models.ListCustomGroupsResponseBodyCustomGroupsCustomGroup()
                self.custom_group.append(temp_model.from_map(k1))

        return self

class ListCustomGroupsResponseBodyCustomGroupsCustomGroup(DaraModel):
    def __init__(
        self,
        custom_group_description: str = None,
        custom_group_id: str = None,
        custom_group_name: str = None,
    ):
        self.custom_group_description = custom_group_description
        self.custom_group_id = custom_group_id
        self.custom_group_name = custom_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_group_description is not None:
            result['CustomGroupDescription'] = self.custom_group_description

        if self.custom_group_id is not None:
            result['CustomGroupId'] = self.custom_group_id

        if self.custom_group_name is not None:
            result['CustomGroupName'] = self.custom_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomGroupDescription') is not None:
            self.custom_group_description = m.get('CustomGroupDescription')

        if m.get('CustomGroupId') is not None:
            self.custom_group_id = m.get('CustomGroupId')

        if m.get('CustomGroupName') is not None:
            self.custom_group_name = m.get('CustomGroupName')

        return self

