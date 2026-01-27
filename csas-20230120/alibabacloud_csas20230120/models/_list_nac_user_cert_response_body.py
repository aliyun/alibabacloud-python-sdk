# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListNacUserCertResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data_list: List[main_models.ListNacUserCertResponseBodyDataList] = None,
        message: str = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.code = code
        self.data_list = data_list
        self.message = message
        self.request_id = request_id
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
        if self.code is not None:
            result['Code'] = self.code

        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.ListNacUserCertResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListNacUserCertResponseBodyDataList(DaraModel):
    def __init__(
        self,
        aliuid: str = None,
        department: str = None,
        dev_tag: str = None,
        device_type: str = None,
        expired_time: str = None,
        hostname: str = None,
        mac: str = None,
        status: str = None,
        user_id: str = None,
        username: str = None,
    ):
        self.aliuid = aliuid
        self.department = department
        self.dev_tag = dev_tag
        self.device_type = device_type
        self.expired_time = expired_time
        self.hostname = hostname
        self.mac = mac
        self.status = status
        self.user_id = user_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.department is not None:
            result['Department'] = self.department

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

