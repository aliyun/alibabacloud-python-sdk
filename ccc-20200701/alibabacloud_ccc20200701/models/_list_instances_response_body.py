# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListInstancesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListInstancesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListInstancesResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyDataList(DaraModel):
    def __init__(
        self,
        admin_list: List[main_models.ListInstancesResponseBodyDataListAdminList] = None,
        aliyun_uid: str = None,
        console_url: str = None,
        create_time: int = None,
        description: str = None,
        domain_name: str = None,
        id: str = None,
        name: str = None,
        number_list: List[main_models.ListInstancesResponseBodyDataListNumberList] = None,
        status: str = None,
    ):
        self.admin_list = admin_list
        self.aliyun_uid = aliyun_uid
        self.console_url = console_url
        self.create_time = create_time
        self.description = description
        self.domain_name = domain_name
        self.id = id
        self.name = name
        self.number_list = number_list
        self.status = status

    def validate(self):
        if self.admin_list:
            for v1 in self.admin_list:
                 if v1:
                    v1.validate()
        if self.number_list:
            for v1 in self.number_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdminList'] = []
        if self.admin_list is not None:
            for k1 in self.admin_list:
                result['AdminList'].append(k1.to_map() if k1 else None)

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.console_url is not None:
            result['ConsoleUrl'] = self.console_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        result['NumberList'] = []
        if self.number_list is not None:
            for k1 in self.number_list:
                result['NumberList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.admin_list = []
        if m.get('AdminList') is not None:
            for k1 in m.get('AdminList'):
                temp_model = main_models.ListInstancesResponseBodyDataListAdminList()
                self.admin_list.append(temp_model.from_map(k1))

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('ConsoleUrl') is not None:
            self.console_url = m.get('ConsoleUrl')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.number_list = []
        if m.get('NumberList') is not None:
            for k1 in m.get('NumberList'):
                temp_model = main_models.ListInstancesResponseBodyDataListNumberList()
                self.number_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListInstancesResponseBodyDataListNumberList(DaraModel):
    def __init__(
        self,
        number: str = None,
    ):
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.number is not None:
            result['Number'] = self.number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')

        return self

class ListInstancesResponseBodyDataListAdminList(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        extension: str = None,
        instance_id: str = None,
        login_name: str = None,
        mobile: str = None,
        role_id: str = None,
        role_name: str = None,
        user_id: str = None,
        work_mode: str = None,
    ):
        self.display_name = display_name
        self.email = email
        self.extension = extension
        self.instance_id = instance_id
        self.login_name = login_name
        self.mobile = mobile
        self.role_id = role_id
        self.role_name = role_name
        self.user_id = user_id
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

