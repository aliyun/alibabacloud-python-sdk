# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeComfyUserDatasResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
        user_datas: List[main_models.DescribeComfyUserDatasResponseBodyUserDatas] = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total = total
        self.user_datas = user_datas

    def validate(self):
        if self.user_datas:
            for v1 in self.user_datas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        result['UserDatas'] = []
        if self.user_datas is not None:
            for k1 in self.user_datas:
                result['UserDatas'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        self.user_datas = []
        if m.get('UserDatas') is not None:
            for k1 in m.get('UserDatas'):
                temp_model = main_models.DescribeComfyUserDatasResponseBodyUserDatas()
                self.user_datas.append(temp_model.from_map(k1))

        return self

class DescribeComfyUserDatasResponseBodyUserDatas(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_size: int = None,
        type: str = None,
        updated_time: str = None,
    ):
        self.file_name = file_name
        self.file_size = file_size
        self.type = type
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.type is not None:
            result['Type'] = self.type

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

