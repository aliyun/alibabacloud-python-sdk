# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class ListConnQuestionResponseBody(DaraModel):
    def __init__(
        self,
        outlines: List[main_models.ListConnQuestionResponseBodyOutlines] = None,
        request_id: str = None,
    ):
        # A list of connected questions.
        self.outlines = outlines
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.outlines:
            for v1 in self.outlines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.ListConnQuestionResponseBodyOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListConnQuestionResponseBodyOutlines(DaraModel):
    def __init__(
        self,
        conn_question_id: int = None,
        create_time: str = None,
        modify_time: str = None,
        outline_id: int = None,
        title: str = None,
    ):
        # The ID of the connected question.
        self.conn_question_id = conn_question_id
        # The creation time, in UTC.
        self.create_time = create_time
        # The last modification time, in UTC.
        self.modify_time = modify_time
        # The relation ID.
        self.outline_id = outline_id
        # The title of the connected question.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conn_question_id is not None:
            result['ConnQuestionId'] = self.conn_question_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnQuestionId') is not None:
            self.conn_question_id = m.get('ConnQuestionId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

