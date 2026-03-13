# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class QueryGroupCorpListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        message: str = None,
        module: List[main_models.QueryGroupCorpListResponseBodyModule] = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.module = module
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['module'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['trace_id'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.module = []
        if m.get('module') is not None:
            for k1 in m.get('module'):
                temp_model = main_models.QueryGroupCorpListResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('trace_id') is not None:
            self.trace_id = m.get('trace_id')

        return self

class QueryGroupCorpListResponseBodyModule(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        corp_name: str = None,
    ):
        self.corp_id = corp_id
        self.corp_name = corp_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        return self

