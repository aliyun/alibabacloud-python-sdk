# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class CostCenterQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.CostCenterQueryResponseBodyModule] = None,
        more_page: bool = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.more_page = more_page
        self.request_id = request_id
        self.success = success
        # traceId
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
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['module'].append(k1.to_map() if k1 else None)

        if self.more_page is not None:
            result['more_page'] = self.more_page

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.module = []
        if m.get('module') is not None:
            for k1 in m.get('module'):
                temp_model = main_models.CostCenterQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('more_page') is not None:
            self.more_page = m.get('more_page')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class CostCenterQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        alipay_no: str = None,
        corp_id: str = None,
        disable: int = None,
        entity_dos: List[main_models.CostCenterQueryResponseBodyModuleEntityDOS] = None,
        id: int = None,
        number: str = None,
        rule_code: int = None,
        scope: int = None,
        thirdpart_id: str = None,
        title: str = None,
    ):
        self.alipay_no = alipay_no
        self.corp_id = corp_id
        self.disable = disable
        self.entity_dos = entity_dos
        self.id = id
        self.number = number
        # rule code
        self.rule_code = rule_code
        self.scope = scope
        self.thirdpart_id = thirdpart_id
        self.title = title

    def validate(self):
        if self.entity_dos:
            for v1 in self.entity_dos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alipay_no is not None:
            result['alipay_no'] = self.alipay_no

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.disable is not None:
            result['disable'] = self.disable

        result['entity_d_o_s'] = []
        if self.entity_dos is not None:
            for k1 in self.entity_dos:
                result['entity_d_o_s'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['id'] = self.id

        if self.number is not None:
            result['number'] = self.number

        if self.rule_code is not None:
            result['rule_code'] = self.rule_code

        if self.scope is not None:
            result['scope'] = self.scope

        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipay_no') is not None:
            self.alipay_no = m.get('alipay_no')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('disable') is not None:
            self.disable = m.get('disable')

        self.entity_dos = []
        if m.get('entity_d_o_s') is not None:
            for k1 in m.get('entity_d_o_s'):
                temp_model = main_models.CostCenterQueryResponseBodyModuleEntityDOS()
                self.entity_dos.append(temp_model.from_map(k1))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('number') is not None:
            self.number = m.get('number')

        if m.get('rule_code') is not None:
            self.rule_code = m.get('rule_code')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class CostCenterQueryResponseBodyModuleEntityDOS(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        entity_id: str = None,
        entity_type: str = None,
        name: str = None,
        user_num: int = None,
    ):
        self.corp_id = corp_id
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.name = name
        self.user_num = user_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.entity_id is not None:
            result['entity_id'] = self.entity_id

        if self.entity_type is not None:
            result['entity_type'] = self.entity_type

        if self.name is not None:
            result['name'] = self.name

        if self.user_num is not None:
            result['user_num'] = self.user_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('entity_id') is not None:
            self.entity_id = m.get('entity_id')

        if m.get('entity_type') is not None:
            self.entity_type = m.get('entity_type')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('user_num') is not None:
            self.user_num = m.get('user_num')

        return self

