# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetSqlInstanceResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.GetSqlInstanceResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.GetSqlInstanceResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class GetSqlInstanceResponseBody(DaraModel):
    def __init__(
        self,
        name: str = None,
        cu: int = None,
        create_time: int = None,
        update_time: int = None,
        use_as_default: bool = None,
    ):
        self.name = name
        self.cu = cu
        self.create_time = create_time
        self.update_time = update_time
        self.use_as_default = use_as_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.cu is not None:
            result['cu'] = self.cu

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.use_as_default is not None:
            result['useAsDefault'] = self.use_as_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('useAsDefault') is not None:
            self.use_as_default = m.get('useAsDefault')

        return self

