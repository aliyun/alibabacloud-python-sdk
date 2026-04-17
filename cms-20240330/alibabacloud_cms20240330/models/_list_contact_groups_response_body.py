# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListContactGroupsResponseBody(DaraModel):
    def __init__(
        self,
        contact_groups: List[main_models.ListContactGroupsResponseBodyContactGroups] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.contact_groups = contact_groups
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.contact_groups:
            for v1 in self.contact_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['contactGroups'] = []
        if self.contact_groups is not None:
            for k1 in self.contact_groups:
                result['contactGroups'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_groups = []
        if m.get('contactGroups') is not None:
            for k1 in m.get('contactGroups'):
                temp_model = main_models.ListContactGroupsResponseBodyContactGroups()
                self.contact_groups.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListContactGroupsResponseBodyContactGroups(DaraModel):
    def __init__(
        self,
        contact_group_id: str = None,
        contact_ids: List[str] = None,
        name: str = None,
        workspace: str = None,
    ):
        self.contact_group_id = contact_group_id
        self.contact_ids = contact_ids
        self.name = name
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_id is not None:
            result['contactGroupId'] = self.contact_group_id

        if self.contact_ids is not None:
            result['contactIds'] = self.contact_ids

        if self.name is not None:
            result['name'] = self.name

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactGroupId') is not None:
            self.contact_group_id = m.get('contactGroupId')

        if m.get('contactIds') is not None:
            self.contact_ids = m.get('contactIds')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

