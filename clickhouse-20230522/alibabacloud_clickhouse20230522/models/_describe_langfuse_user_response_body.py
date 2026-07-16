# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeLangfuseUserResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeLangfuseUserResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # Id of the request
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
            temp_model = main_models.DescribeLangfuseUserResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLangfuseUserResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        email: str = None,
        memberships: List[main_models.DescribeLangfuseUserResponseBodyDataMemberships] = None,
        name: str = None,
        updated_at: str = None,
    ):
        # The time when the user was created.
        self.created_at = created_at
        # The email address of the user.
        self.email = email
        # The role information of the user.
        self.memberships = memberships
        # The username.
        self.name = name
        # The time when the user was last updated.
        self.updated_at = updated_at

    def validate(self):
        if self.memberships:
            for v1 in self.memberships:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.email is not None:
            result['Email'] = self.email

        result['Memberships'] = []
        if self.memberships is not None:
            for k1 in self.memberships:
                result['Memberships'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        self.memberships = []
        if m.get('Memberships') is not None:
            for k1 in m.get('Memberships'):
                temp_model = main_models.DescribeLangfuseUserResponseBodyDataMemberships()
                self.memberships.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

class DescribeLangfuseUserResponseBodyDataMemberships(DaraModel):
    def __init__(
        self,
        org_role: str = None,
        organization_id: str = None,
        organization_name: str = None,
        projects: List[main_models.DescribeLangfuseUserResponseBodyDataMembershipsProjects] = None,
    ):
        # The role of the user within the organization.
        self.org_role = org_role
        # The Langfuse organization ID.
        self.organization_id = organization_id
        # The Langfuse organization name.
        self.organization_name = organization_name
        # The list of Langfuse projects.
        self.projects = projects

    def validate(self):
        if self.projects:
            for v1 in self.projects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.org_role is not None:
            result['OrgRole'] = self.org_role

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.organization_name is not None:
            result['OrganizationName'] = self.organization_name

        result['Projects'] = []
        if self.projects is not None:
            for k1 in self.projects:
                result['Projects'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgRole') is not None:
            self.org_role = m.get('OrgRole')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('OrganizationName') is not None:
            self.organization_name = m.get('OrganizationName')

        self.projects = []
        if m.get('Projects') is not None:
            for k1 in m.get('Projects'):
                temp_model = main_models.DescribeLangfuseUserResponseBodyDataMembershipsProjects()
                self.projects.append(temp_model.from_map(k1))

        return self

class DescribeLangfuseUserResponseBodyDataMembershipsProjects(DaraModel):
    def __init__(
        self,
        project_id: str = None,
        project_name: str = None,
        project_role: str = None,
    ):
        # The Langfuse project ID.
        self.project_id = project_id
        # The Langfuse project name.
        self.project_name = project_name
        # The role of the user within the project.
        self.project_role = project_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.project_role is not None:
            result['ProjectRole'] = self.project_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ProjectRole') is not None:
            self.project_role = m.get('ProjectRole')

        return self

