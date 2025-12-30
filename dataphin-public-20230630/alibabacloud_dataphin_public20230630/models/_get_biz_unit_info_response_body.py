# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetBizUnitInfoResponseBody(DaraModel):
    def __init__(
        self,
        biz_unit_info: main_models.GetBizUnitInfoResponseBodyBizUnitInfo = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.biz_unit_info = biz_unit_info
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.biz_unit_info:
            self.biz_unit_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_info is not None:
            result['BizUnitInfo'] = self.biz_unit_info.to_map()

        if self.code is not None:
            result['Code'] = self.code

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
        if m.get('BizUnitInfo') is not None:
            temp_model = main_models.GetBizUnitInfoResponseBodyBizUnitInfo()
            self.biz_unit_info = temp_model.from_map(m.get('BizUnitInfo'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBizUnitInfoResponseBodyBizUnitInfo(DaraModel):
    def __init__(
        self,
        account_list: List[main_models.GetBizUnitInfoResponseBodyBizUnitInfoAccountList] = None,
        biz_object_count: int = None,
        biz_process_count: int = None,
        business_leader_list: List[main_models.GetBizUnitInfoResponseBodyBizUnitInfoBusinessLeaderList] = None,
        data_domain_count: int = None,
        data_leader_list: List[main_models.GetBizUnitInfoResponseBodyBizUnitInfoDataLeaderList] = None,
        description: str = None,
        display_name: str = None,
        env_list: List[main_models.GetBizUnitInfoResponseBodyBizUnitInfoEnvList] = None,
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
        self.biz_object_count = biz_object_count
        self.biz_process_count = biz_process_count
        self.business_leader_list = business_leader_list
        self.data_domain_count = data_domain_count
        self.data_leader_list = data_leader_list
        self.description = description
        self.display_name = display_name
        self.env_list = env_list
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
        if self.business_leader_list:
            for v1 in self.business_leader_list:
                 if v1:
                    v1.validate()
        if self.data_leader_list:
            for v1 in self.data_leader_list:
                 if v1:
                    v1.validate()
        if self.env_list:
            for v1 in self.env_list:
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

        if self.biz_object_count is not None:
            result['BizObjectCount'] = self.biz_object_count

        if self.biz_process_count is not None:
            result['BizProcessCount'] = self.biz_process_count

        result['BusinessLeaderList'] = []
        if self.business_leader_list is not None:
            for k1 in self.business_leader_list:
                result['BusinessLeaderList'].append(k1.to_map() if k1 else None)

        if self.data_domain_count is not None:
            result['DataDomainCount'] = self.data_domain_count

        result['DataLeaderList'] = []
        if self.data_leader_list is not None:
            for k1 in self.data_leader_list:
                result['DataLeaderList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        result['EnvList'] = []
        if self.env_list is not None:
            for k1 in self.env_list:
                result['EnvList'].append(k1.to_map() if k1 else None)

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
                temp_model = main_models.GetBizUnitInfoResponseBodyBizUnitInfoAccountList()
                self.account_list.append(temp_model.from_map(k1))

        if m.get('BizObjectCount') is not None:
            self.biz_object_count = m.get('BizObjectCount')

        if m.get('BizProcessCount') is not None:
            self.biz_process_count = m.get('BizProcessCount')

        self.business_leader_list = []
        if m.get('BusinessLeaderList') is not None:
            for k1 in m.get('BusinessLeaderList'):
                temp_model = main_models.GetBizUnitInfoResponseBodyBizUnitInfoBusinessLeaderList()
                self.business_leader_list.append(temp_model.from_map(k1))

        if m.get('DataDomainCount') is not None:
            self.data_domain_count = m.get('DataDomainCount')

        self.data_leader_list = []
        if m.get('DataLeaderList') is not None:
            for k1 in m.get('DataLeaderList'):
                temp_model = main_models.GetBizUnitInfoResponseBodyBizUnitInfoDataLeaderList()
                self.data_leader_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        self.env_list = []
        if m.get('EnvList') is not None:
            for k1 in m.get('EnvList'):
                temp_model = main_models.GetBizUnitInfoResponseBodyBizUnitInfoEnvList()
                self.env_list.append(temp_model.from_map(k1))

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

class GetBizUnitInfoResponseBodyBizUnitInfoEnvList(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        env_name: str = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.env_name = env_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env_name is not None:
            result['EnvName'] = self.env_name

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetBizUnitInfoResponseBodyBizUnitInfoDataLeaderList(DaraModel):
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

class GetBizUnitInfoResponseBodyBizUnitInfoBusinessLeaderList(DaraModel):
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

class GetBizUnitInfoResponseBodyBizUnitInfoAccountList(DaraModel):
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

