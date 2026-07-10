# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class CreateLangfuseUserResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateLangfuseUserResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data.
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
            temp_model = main_models.CreateLangfuseUserResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateLangfuseUserResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        email: str = None,
        membership: main_models.CreateLangfuseUserResponseBodyDataMembership = None,
        name: str = None,
    ):
        # The time when the user was created.
        self.created_at = created_at
        # The email address of the user.
        self.email = email
        # The role of the user.
        self.membership = membership
        # The username.
        self.name = name

    def validate(self):
        if self.membership:
            self.membership.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.email is not None:
            result['Email'] = self.email

        if self.membership is not None:
            result['Membership'] = self.membership.to_map()

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Membership') is not None:
            temp_model = main_models.CreateLangfuseUserResponseBodyDataMembership()
            self.membership = temp_model.from_map(m.get('Membership'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreateLangfuseUserResponseBodyDataMembership(DaraModel):
    def __init__(
        self,
        organization_id: str = None,
        role: str = None,
    ):
        # The Langfuse organization ID.
        self.organization_id = organization_id
        # The role of the user in the organization.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

