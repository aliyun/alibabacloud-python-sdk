# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class PreviewNotifyTemplateResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.PreviewNotifyTemplateResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.msg = msg
        # 请求ID
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
            result['data'] = self.data.to_map()

        if self.msg is not None:
            result['msg'] = self.msg

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.PreviewNotifyTemplateResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('msg') is not None:
            self.msg = m.get('msg')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class PreviewNotifyTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        failed: Dict[str, Any] = None,
        success: Dict[str, Any] = None,
    ):
        self.failed = failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['failed'] = self.failed

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failed') is not None:
            self.failed = m.get('failed')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

