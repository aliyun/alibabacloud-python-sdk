# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ApplyDataServiceApiRequest(DaraModel):
    def __init__(
        self,
        apply_command: main_models.ApplyDataServiceApiRequestApplyCommand = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.apply_command = apply_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.apply_command:
            self.apply_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_command is not None:
            result['ApplyCommand'] = self.apply_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyCommand') is not None:
            temp_model = main_models.ApplyDataServiceApiRequestApplyCommand()
            self.apply_command = temp_model.from_map(m.get('ApplyCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class ApplyDataServiceApiRequestApplyCommand(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        app_id: int = None,
        dev_field_list: List[main_models.ApplyDataServiceApiRequestApplyCommandDevFieldList] = None,
        expire_date: str = None,
        prod_field_list: List[main_models.ApplyDataServiceApiRequestApplyCommandProdFieldList] = None,
        reason: str = None,
    ):
        # This parameter is required.
        self.api_id = api_id
        # AppId
        # 
        # This parameter is required.
        self.app_id = app_id
        self.dev_field_list = dev_field_list
        # This parameter is required.
        self.expire_date = expire_date
        self.prod_field_list = prod_field_list
        # This parameter is required.
        self.reason = reason

    def validate(self):
        if self.dev_field_list:
            for v1 in self.dev_field_list:
                 if v1:
                    v1.validate()
        if self.prod_field_list:
            for v1 in self.prod_field_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        result['DevFieldList'] = []
        if self.dev_field_list is not None:
            for k1 in self.dev_field_list:
                result['DevFieldList'].append(k1.to_map() if k1 else None)

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        result['ProdFieldList'] = []
        if self.prod_field_list is not None:
            for k1 in self.prod_field_list:
                result['ProdFieldList'].append(k1.to_map() if k1 else None)

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.dev_field_list = []
        if m.get('DevFieldList') is not None:
            for k1 in m.get('DevFieldList'):
                temp_model = main_models.ApplyDataServiceApiRequestApplyCommandDevFieldList()
                self.dev_field_list.append(temp_model.from_map(k1))

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        self.prod_field_list = []
        if m.get('ProdFieldList') is not None:
            for k1 in m.get('ProdFieldList'):
                temp_model = main_models.ApplyDataServiceApiRequestApplyCommandProdFieldList()
                self.prod_field_list.append(temp_model.from_map(k1))

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

class ApplyDataServiceApiRequestApplyCommandProdFieldList(DaraModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class ApplyDataServiceApiRequestApplyCommandDevFieldList(DaraModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

