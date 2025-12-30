# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListBizUnitsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListBizUnitsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListBizUnitsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListBizUnitsResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_unit_list: List[main_models.ListBizUnitsResponseBodyDataBizUnitList] = None,
    ):
        self.biz_unit_list = biz_unit_list

    def validate(self):
        if self.biz_unit_list:
            for v1 in self.biz_unit_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BizUnitList'] = []
        if self.biz_unit_list is not None:
            for k1 in self.biz_unit_list:
                result['BizUnitList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_unit_list = []
        if m.get('BizUnitList') is not None:
            for k1 in m.get('BizUnitList'):
                temp_model = main_models.ListBizUnitsResponseBodyDataBizUnitList()
                self.biz_unit_list.append(temp_model.from_map(k1))

        return self

class ListBizUnitsResponseBodyDataBizUnitList(DaraModel):
    def __init__(
        self,
        account_list: List[main_models.ListBizUnitsResponseBodyDataBizUnitListAccountList] = None,
        description: str = None,
        display_name: str = None,
        env: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icon: str = None,
        id: int = None,
        last_modifier: str = None,
        last_modifier_name: str = None,
        mode: str = None,
        name: str = None,
        owner_name: str = None,
        owner_user_id: str = None,
    ):
        self.account_list = account_list
        self.description = description
        self.display_name = display_name
        self.env = env
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.icon = icon
        self.id = id
        self.last_modifier = last_modifier
        self.last_modifier_name = last_modifier_name
        self.mode = mode
        self.name = name
        self.owner_name = owner_name
        self.owner_user_id = owner_user_id

    def validate(self):
        if self.account_list:
            for v1 in self.account_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountList'] = []
        if self.account_list is not None:
            for k1 in self.account_list:
                result['AccountList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env is not None:
            result['Env'] = self.env

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.last_modifier_name is not None:
            result['LastModifierName'] = self.last_modifier_name

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_list = []
        if m.get('AccountList') is not None:
            for k1 in m.get('AccountList'):
                temp_model = main_models.ListBizUnitsResponseBodyDataBizUnitListAccountList()
                self.account_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('LastModifierName') is not None:
            self.last_modifier_name = m.get('LastModifierName')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        return self

class ListBizUnitsResponseBodyDataBizUnitListAccountList(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
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

