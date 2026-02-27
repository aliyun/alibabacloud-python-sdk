# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ListDatabasesResponseBody(DaraModel):
    def __init__(
        self,
        database_list: List[main_models.ListDatabasesResponseBodyDatabaseList] = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.database_list = database_list
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.database_list:
            for v1 in self.database_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatabaseList'] = []
        if self.database_list is not None:
            for k1 in self.database_list:
                result['DatabaseList'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_list = []
        if m.get('DatabaseList') is not None:
            for k1 in m.get('DatabaseList'):
                temp_model = main_models.ListDatabasesResponseBodyDatabaseList()
                self.database_list.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDatabasesResponseBodyDatabaseList(DaraModel):
    def __init__(
        self,
        external: bool = None,
        name: str = None,
        permission_model: str = None,
        privilege: str = None,
    ):
        self.external = external
        self.name = name
        self.permission_model = permission_model
        self.privilege = privilege

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external is not None:
            result['External'] = self.external

        if self.name is not None:
            result['Name'] = self.name

        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model

        if self.privilege is not None:
            result['Privilege'] = self.privilege

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('External') is not None:
            self.external = m.get('External')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')

        if m.get('Privilege') is not None:
            self.privilege = m.get('Privilege')

        return self

