# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ListAnswerLibResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAnswerLibResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAnswerLibResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAnswerLibResponseBodyData(DaraModel):
    def __init__(
        self,
        answer_count: int = None,
        gmt_modified: str = None,
        lib_id: str = None,
        lib_name: str = None,
        uid: str = None,
    ):
        self.answer_count = answer_count
        self.gmt_modified = gmt_modified
        self.lib_id = lib_id
        self.lib_name = lib_name
        # UID。
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer_count is not None:
            result['AnswerCount'] = self.answer_count

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.lib_name is not None:
            result['LibName'] = self.lib_name

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerCount') is not None:
            self.answer_count = m.get('AnswerCount')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

