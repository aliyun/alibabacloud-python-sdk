# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListIdpConfigsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListIdpConfigsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            temp_model = main_models.ListIdpConfigsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListIdpConfigsResponseBodyData(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.ListIdpConfigsResponseBodyDataDataList] = None,
        total_num: int = None,
    ):
        self.data_list = data_list
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.ListIdpConfigsResponseBodyDataDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListIdpConfigsResponseBodyDataDataList(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        mfa: str = None,
        mobile_login_type: str = None,
        mobile_mfa_config_type: str = None,
        multi_idp_info: str = None,
        name: str = None,
        pc_login_type: str = None,
        status: str = None,
        type: str = None,
        update_time: str = None,
    ):
        self.description = description
        self.id = id
        self.mfa = mfa
        self.mobile_login_type = mobile_login_type
        self.mobile_mfa_config_type = mobile_mfa_config_type
        self.multi_idp_info = multi_idp_info
        self.name = name
        self.pc_login_type = pc_login_type
        self.status = status
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.mfa is not None:
            result['Mfa'] = self.mfa

        if self.mobile_login_type is not None:
            result['MobileLoginType'] = self.mobile_login_type

        if self.mobile_mfa_config_type is not None:
            result['MobileMfaConfigType'] = self.mobile_mfa_config_type

        if self.multi_idp_info is not None:
            result['MultiIdpInfo'] = self.multi_idp_info

        if self.name is not None:
            result['Name'] = self.name

        if self.pc_login_type is not None:
            result['PcLoginType'] = self.pc_login_type

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mfa') is not None:
            self.mfa = m.get('Mfa')

        if m.get('MobileLoginType') is not None:
            self.mobile_login_type = m.get('MobileLoginType')

        if m.get('MobileMfaConfigType') is not None:
            self.mobile_mfa_config_type = m.get('MobileMfaConfigType')

        if m.get('MultiIdpInfo') is not None:
            self.multi_idp_info = m.get('MultiIdpInfo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PcLoginType') is not None:
            self.pc_login_type = m.get('PcLoginType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

