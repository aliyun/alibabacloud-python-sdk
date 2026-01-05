# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class IdentifyCredential(DaraModel):
    def __init__(
        self,
        data_source: main_models.IdentifyCredentialDataSource = None,
        project_id: str = None,
        user_id: str = None,
        user_type: str = None,
    ):
        self.data_source = data_source
        self.project_id = project_id
        self.user_id = user_id
        self.user_type = user_type

    def validate(self):
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSource') is not None:
            temp_model = main_models.IdentifyCredentialDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

class IdentifyCredentialDataSource(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        password: str = None,
        role: str = None,
        type: str = None,
        user_name: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.password = password
        self.role = role
        self.type = type
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.password is not None:
            result['Password'] = self.password

        if self.role is not None:
            result['Role'] = self.role

        if self.type is not None:
            result['Type'] = self.type

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

