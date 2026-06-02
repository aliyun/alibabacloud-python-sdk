# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListWorkspaceCodeResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListWorkspaceCodeResponseBodyData = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

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
        if m.get('Data') is not None:
            temp_model = main_models.ListWorkspaceCodeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListWorkspaceCodeResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListWorkspaceCodeResponseBodyDataList] = None,
    ):
        self.list = list

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListWorkspaceCodeResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        return self

class ListWorkspaceCodeResponseBodyDataList(DaraModel):
    def __init__(
        self,
        is_dir: bool = None,
        mtime: str = None,
        name: str = None,
        size: int = None,
        symlink: str = None,
    ):
        self.is_dir = is_dir
        self.mtime = mtime
        self.name = name
        self.size = size
        self.symlink = symlink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_dir is not None:
            result['IsDir'] = self.is_dir

        if self.mtime is not None:
            result['Mtime'] = self.mtime

        if self.name is not None:
            result['Name'] = self.name

        if self.size is not None:
            result['Size'] = self.size

        if self.symlink is not None:
            result['Symlink'] = self.symlink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDir') is not None:
            self.is_dir = m.get('IsDir')

        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Symlink') is not None:
            self.symlink = m.get('Symlink')

        return self

