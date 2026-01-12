# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class Workspace(DaraModel):
    def __init__(
        self,
        creator: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        members: List[main_models.Member] = None,
        quotas: List[main_models.Quota] = None,
        total_resources: main_models.Resources = None,
        workspace_admins: List[main_models.Member] = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.creator = creator
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time
        self.members = members
        self.quotas = quotas
        self.total_resources = total_resources
        self.workspace_admins = workspace_admins
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        if self.members:
            for v1 in self.members:
                 if v1:
                    v1.validate()
        if self.quotas:
            for v1 in self.quotas:
                 if v1:
                    v1.validate()
        if self.total_resources:
            self.total_resources.validate()
        if self.workspace_admins:
            for v1 in self.workspace_admins:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        result['Members'] = []
        if self.members is not None:
            for k1 in self.members:
                result['Members'].append(k1.to_map() if k1 else None)

        result['Quotas'] = []
        if self.quotas is not None:
            for k1 in self.quotas:
                result['Quotas'].append(k1.to_map() if k1 else None)

        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()

        result['WorkspaceAdmins'] = []
        if self.workspace_admins is not None:
            for k1 in self.workspace_admins:
                result['WorkspaceAdmins'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        self.members = []
        if m.get('Members') is not None:
            for k1 in m.get('Members'):
                temp_model = main_models.Member()
                self.members.append(temp_model.from_map(k1))

        self.quotas = []
        if m.get('Quotas') is not None:
            for k1 in m.get('Quotas'):
                temp_model = main_models.Quota()
                self.quotas.append(temp_model.from_map(k1))

        if m.get('TotalResources') is not None:
            temp_model = main_models.Resources()
            self.total_resources = temp_model.from_map(m.get('TotalResources'))

        self.workspace_admins = []
        if m.get('WorkspaceAdmins') is not None:
            for k1 in m.get('WorkspaceAdmins'):
                temp_model = main_models.Member()
                self.workspace_admins.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

