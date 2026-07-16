# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bailianmodelonchip20240816 import models as main_models
from darabonba.model import DaraModel

class ModelTypeDetermineResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ModelTypeDetermineResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ModelTypeDetermineResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ModelTypeDetermineResponseBodyData(DaraModel):
    def __init__(
        self,
        follow_up: bool = None,
        rewrite_text: str = None,
        vl: bool = None,
    ):
        self.follow_up = follow_up
        self.rewrite_text = rewrite_text
        self.vl = vl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.follow_up is not None:
            result['followUp'] = self.follow_up

        if self.rewrite_text is not None:
            result['rewriteText'] = self.rewrite_text

        if self.vl is not None:
            result['vl'] = self.vl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('followUp') is not None:
            self.follow_up = m.get('followUp')

        if m.get('rewriteText') is not None:
            self.rewrite_text = m.get('rewriteText')

        if m.get('vl') is not None:
            self.vl = m.get('vl')

        return self

