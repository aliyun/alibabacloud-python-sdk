# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class SaveOutputFileToResourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        results: List[main_models.SaveOutputFileToResourceResponseBodyResults] = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.SaveOutputFileToResourceResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class SaveOutputFileToResourceResponseBodyResults(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        item_id: str = None,
        source_id: str = None,
        success: bool = None,
    ):
        # 失败时返回业务错误码（i18n key）
        self.error_code = error_code
        # 失败时返回错误描述（已按请求 locale 国际化）
        self.error_message = error_message
        # 产出明细 ID
        self.item_id = item_id
        # 成功时返回新建的资源 sourceId
        self.source_id = source_id
        # 操作是否成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

