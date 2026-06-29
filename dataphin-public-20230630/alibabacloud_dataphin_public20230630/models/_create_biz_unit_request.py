# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateBizUnitRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateBizUnitRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # The create request.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
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
            temp_model = main_models.CreateBizUnitRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateBizUnitRequestCreateCommand(DaraModel):
    def __init__(
        self,
        biz_unit_account_list: List[main_models.CreateBizUnitRequestCreateCommandBizUnitAccountList] = None,
        description: str = None,
        display_name: str = None,
        icon: str = None,
        mode: str = None,
        name: str = None,
    ):
        # The list of data domain architects.
        # 
        # This parameter is required.
        self.biz_unit_account_list = biz_unit_account_list
        # The description of the business object. The description can be up to 128 characters in length.
        self.description = description
        # The display name of the business object. The name can be up to 64 characters in length and can contain only Chinese characters, letters, digits, underscores, and hyphens.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The preset icon. Valid values:
        # - icon-e-commerce: E-commerce.
        # - icon-finance: Finance.
        # - con-cloud-computing: Cloud computing.
        # - icon-advertisement: Advertising and marketing.
        # - icon-logistics: Logistics.
        # - icon-entertainment: Entertainment.
        # - icon-traffic: Travel.
        # - icon-health: Health.
        # - icon-social-contact: Social and communication.
        # - con-dining: Dining.
        # - icon-education: Education.
        # - icon-environment: Environment.
        # 
        # This parameter is required.
        self.icon = icon
        # The production mode. Valid values:
        # - BASIC: single-environment mode.
        # - DEV_PROD: development/production dual-environment mode.
        self.mode = mode
        # The code name of the business object. The name can be up to 64 characters in length and can contain only letters, digits, and underscores. For ADB_PG engines, the code name can be up to 40 characters in length.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.biz_unit_account_list:
            for v1 in self.biz_unit_account_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BizUnitAccountList'] = []
        if self.biz_unit_account_list is not None:
            for k1 in self.biz_unit_account_list:
                result['BizUnitAccountList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_unit_account_list = []
        if m.get('BizUnitAccountList') is not None:
            for k1 in m.get('BizUnitAccountList'):
                temp_model = main_models.CreateBizUnitRequestCreateCommandBizUnitAccountList()
                self.biz_unit_account_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreateBizUnitRequestCreateCommandBizUnitAccountList(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

