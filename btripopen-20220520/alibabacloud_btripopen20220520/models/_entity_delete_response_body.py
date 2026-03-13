# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class EntityDeleteResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.EntityDeleteResponseBodyModule = None,
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

        if m.get('module') is not None:
            temp_model = main_models.EntityDeleteResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('more_page') is not None:
            self.more_page = m.get('more_page')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class EntityDeleteResponseBodyModule(DaraModel):
    def __init__(
        self,
        remove_num: int = None,
        selected_user_num: int = None,
    ):
        self.remove_num = remove_num
        self.selected_user_num = selected_user_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remove_num is not None:
            result['remove_num'] = self.remove_num

        if self.selected_user_num is not None:
            result['selected_user_num'] = self.selected_user_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('remove_num') is not None:
            self.remove_num = m.get('remove_num')

        if m.get('selected_user_num') is not None:
            self.selected_user_num = m.get('selected_user_num')

        return self

