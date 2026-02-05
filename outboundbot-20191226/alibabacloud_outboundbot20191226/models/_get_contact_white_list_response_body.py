# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class GetContactWhiteListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        contact_whitelist_list: main_models.GetContactWhiteListResponseBodyContactWhitelistList = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.contact_whitelist_list = contact_whitelist_list
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.contact_whitelist_list:
            self.contact_whitelist_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.contact_whitelist_list is not None:
            result['ContactWhitelistList'] = self.contact_whitelist_list.to_map()

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

        if m.get('ContactWhitelistList') is not None:
            temp_model = main_models.GetContactWhiteListResponseBodyContactWhitelistList()
            self.contact_whitelist_list = temp_model.from_map(m.get('ContactWhitelistList'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetContactWhiteListResponseBodyContactWhitelistList(DaraModel):
    def __init__(
        self,
        list: List[main_models.GetContactWhiteListResponseBodyContactWhitelistListList] = None,
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
                temp_model = main_models.GetContactWhiteListResponseBodyContactWhitelistListList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetContactWhiteListResponseBodyContactWhitelistListList(DaraModel):
    def __init__(
        self,
        contact_white_list_id: str = None,
        creation_time: int = None,
        creator: str = None,
        instance_id: str = None,
        name: str = None,
        operator: str = None,
        phone_number: str = None,
        remark: str = None,
    ):
        self.contact_white_list_id = contact_white_list_id
        self.creation_time = creation_time
        self.creator = creator
        self.instance_id = instance_id
        self.name = name
        self.operator = operator
        self.phone_number = phone_number
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_white_list_id is not None:
            result['ContactWhiteListId'] = self.contact_white_list_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactWhiteListId') is not None:
            self.contact_white_list_id = m.get('ContactWhiteListId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

