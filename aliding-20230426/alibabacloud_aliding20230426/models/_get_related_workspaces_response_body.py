# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetRelatedWorkspacesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
        workspaces: List[main_models.GetRelatedWorkspacesResponseBodyWorkspaces] = None,
    ):
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type
        self.workspaces = workspaces

    def validate(self):
        if self.workspaces:
            for v1 in self.workspaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        result['workspaces'] = []
        if self.workspaces is not None:
            for k1 in self.workspaces:
                result['workspaces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        self.workspaces = []
        if m.get('workspaces') is not None:
            for k1 in m.get('workspaces'):
                temp_model = main_models.GetRelatedWorkspacesResponseBodyWorkspaces()
                self.workspaces.append(temp_model.from_map(k1))

        return self

class GetRelatedWorkspacesResponseBodyWorkspaces(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        deleted: bool = None,
        name: str = None,
        owner: str = None,
        recent_list: List[main_models.GetRelatedWorkspacesResponseBodyWorkspacesRecentList] = None,
        role: str = None,
        url: str = None,
        workspace_id: str = None,
    ):
        self.create_time = create_time
        self.deleted = deleted
        self.name = name
        self.owner = owner
        self.recent_list = recent_list
        self.role = role
        self.url = url
        self.workspace_id = workspace_id

    def validate(self):
        if self.recent_list:
            for v1 in self.recent_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        result['RecentList'] = []
        if self.recent_list is not None:
            for k1 in self.recent_list:
                result['RecentList'].append(k1.to_map() if k1 else None)

        if self.role is not None:
            result['Role'] = self.role

        if self.url is not None:
            result['Url'] = self.url

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        self.recent_list = []
        if m.get('RecentList') is not None:
            for k1 in m.get('RecentList'):
                temp_model = main_models.GetRelatedWorkspacesResponseBodyWorkspacesRecentList()
                self.recent_list.append(temp_model.from_map(k1))

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetRelatedWorkspacesResponseBodyWorkspacesRecentList(DaraModel):
    def __init__(
        self,
        last_edit_time: int = None,
        name: str = None,
        node_id: str = None,
        url: str = None,
    ):
        self.last_edit_time = last_edit_time
        self.name = name
        self.node_id = node_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_edit_time is not None:
            result['LastEditTime'] = self.last_edit_time

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastEditTime') is not None:
            self.last_edit_time = m.get('LastEditTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

