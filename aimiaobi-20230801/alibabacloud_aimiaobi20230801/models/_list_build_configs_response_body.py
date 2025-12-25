# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListBuildConfigsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListBuildConfigsResponseBodyData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListBuildConfigsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListBuildConfigsResponseBodyData(DaraModel):
    def __init__(
        self,
        build_in: bool = None,
        create_time: str = None,
        create_user: str = None,
        id: int = None,
        keywords: List[main_models.ListBuildConfigsResponseBodyDataKeywords] = None,
        tag: str = None,
        tag_description: str = None,
        type: str = None,
        update_time: str = None,
        update_user: str = None,
    ):
        self.build_in = build_in
        self.create_time = create_time
        self.create_user = create_user
        self.id = id
        self.keywords = keywords
        self.tag = tag
        self.tag_description = tag_description
        self.type = type
        self.update_time = update_time
        self.update_user = update_user

    def validate(self):
        if self.keywords:
            for v1 in self.keywords:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_in is not None:
            result['BuildIn'] = self.build_in

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.id is not None:
            result['Id'] = self.id

        result['Keywords'] = []
        if self.keywords is not None:
            for k1 in self.keywords:
                result['Keywords'].append(k1.to_map() if k1 else None)

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_user is not None:
            result['UpdateUser'] = self.update_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildIn') is not None:
            self.build_in = m.get('BuildIn')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.keywords = []
        if m.get('Keywords') is not None:
            for k1 in m.get('Keywords'):
                temp_model = main_models.ListBuildConfigsResponseBodyDataKeywords()
                self.keywords.append(temp_model.from_map(k1))

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')

        return self

class ListBuildConfigsResponseBodyDataKeywords(DaraModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
    ):
        self.description = description
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

