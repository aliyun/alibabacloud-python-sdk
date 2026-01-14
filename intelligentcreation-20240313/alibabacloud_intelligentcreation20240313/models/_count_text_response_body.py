# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class CountTextResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        count_text_cmd_list: List[main_models.CountTextResponseBodyCountTextCmdList] = None,
    ):
        self.request_id = request_id
        self.count_text_cmd_list = count_text_cmd_list

    def validate(self):
        if self.count_text_cmd_list:
            for v1 in self.count_text_cmd_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['countTextCmdList'] = []
        if self.count_text_cmd_list is not None:
            for k1 in self.count_text_cmd_list:
                result['countTextCmdList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.count_text_cmd_list = []
        if m.get('countTextCmdList') is not None:
            for k1 in m.get('countTextCmdList'):
                temp_model = main_models.CountTextResponseBodyCountTextCmdList()
                self.count_text_cmd_list.append(temp_model.from_map(k1))

        return self

class CountTextResponseBodyCountTextCmdList(DaraModel):
    def __init__(
        self,
        count: int = None,
        theme: str = None,
    ):
        self.count = count
        self.theme = theme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.theme is not None:
            result['theme'] = self.theme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('theme') is not None:
            self.theme = m.get('theme')

        return self

