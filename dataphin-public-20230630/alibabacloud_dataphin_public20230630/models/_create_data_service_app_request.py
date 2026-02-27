# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateDataServiceAppRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateDataServiceAppRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateDataServiceAppRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateDataServiceAppRequestCreateCommand(DaraModel):
    def __init__(
        self,
        app_group_id: int = None,
        app_key: str = None,
        app_name: str = None,
        app_secret: str = None,
        owner_ids: List[str] = None,
        scenarios: str = None,
    ):
        # This parameter is required.
        self.app_group_id = app_group_id
        self.app_key = app_key
        # This parameter is required.
        self.app_name = app_name
        self.app_secret = app_secret
        # This parameter is required.
        self.owner_ids = owner_ids
        # This parameter is required.
        self.scenarios = scenarios

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids

        if self.scenarios is not None:
            result['Scenarios'] = self.scenarios

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')

        if m.get('Scenarios') is not None:
            self.scenarios = m.get('Scenarios')

        return self

