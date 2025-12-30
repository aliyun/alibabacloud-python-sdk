# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class OperateInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_status_list: List[main_models.OperateInstanceResponseBodyInstanceStatusList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_status_list = instance_status_list
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instance_status_list:
            for v1 in self.instance_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['InstanceStatusList'] = []
        if self.instance_status_list is not None:
            for k1 in self.instance_status_list:
                result['InstanceStatusList'].append(k1.to_map() if k1 else None)

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.instance_status_list = []
        if m.get('InstanceStatusList') is not None:
            for k1 in m.get('InstanceStatusList'):
                temp_model = main_models.OperateInstanceResponseBodyInstanceStatusList()
                self.instance_status_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class OperateInstanceResponseBodyInstanceStatusList(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        error_message: str = None,
        id: str = None,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        status: str = None,
    ):
        self.display_name = display_name
        self.error_message = error_message
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

