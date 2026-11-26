# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class QueryScriptHotWordListResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        script_hot_word_list: List[main_models.AICoachScriptHotWordItem] = None,
        success: bool = None,
        total: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.script_hot_word_list = script_hot_word_list
        self.success = success
        self.total = total

    def validate(self):
        if self.script_hot_word_list:
            for v1 in self.script_hot_word_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['scriptHotWordList'] = []
        if self.script_hot_word_list is not None:
            for k1 in self.script_hot_word_list:
                result['scriptHotWordList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['success'] = self.success

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.script_hot_word_list = []
        if m.get('scriptHotWordList') is not None:
            for k1 in m.get('scriptHotWordList'):
                temp_model = main_models.AICoachScriptHotWordItem()
                self.script_hot_word_list.append(temp_model.from_map(k1))

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

