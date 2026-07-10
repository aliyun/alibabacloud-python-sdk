# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class ModifyLangfuseProjectMembershipResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ModifyLangfuseProjectMembershipResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
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
            temp_model = main_models.ModifyLangfuseProjectMembershipResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyLangfuseProjectMembershipResponseBodyData(DaraModel):
    def __init__(
        self,
        email: str = None,
        role: str = None,
    ):
        # The email address of the user.
        self.email = email
        # The role of the user in the project.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

