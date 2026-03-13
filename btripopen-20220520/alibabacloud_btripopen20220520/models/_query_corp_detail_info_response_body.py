# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class QueryCorpDetailInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.QueryCorpDetailInfoResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

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

        if m.get('module') is not None:
            temp_model = main_models.QueryCorpDetailInfoResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class QueryCorpDetailInfoResponseBodyModule(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        corp_name: str = None,
        open_agent_id: str = None,
        super_admin_name: str = None,
        super_admin_phone: str = None,
        user_id: str = None,
    ):
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.open_agent_id = open_agent_id
        self.super_admin_name = super_admin_name
        self.super_admin_phone = super_admin_phone
        self.user_id = user_id

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

        if self.open_agent_id is not None:
            result['open_agent_id'] = self.open_agent_id

        if self.super_admin_name is not None:
            result['super_admin_name'] = self.super_admin_name

        if self.super_admin_phone is not None:
            result['super_admin_phone'] = self.super_admin_phone

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('open_agent_id') is not None:
            self.open_agent_id = m.get('open_agent_id')

        if m.get('super_admin_name') is not None:
            self.super_admin_name = m.get('super_admin_name')

        if m.get('super_admin_phone') is not None:
            self.super_admin_phone = m.get('super_admin_phone')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

