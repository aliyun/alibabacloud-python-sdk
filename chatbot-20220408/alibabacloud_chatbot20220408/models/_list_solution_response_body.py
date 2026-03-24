# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class ListSolutionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        solutions: List[main_models.ListSolutionResponseBodySolutions] = None,
    ):
        self.request_id = request_id
        self.solutions = solutions

    def validate(self):
        if self.solutions:
            for v1 in self.solutions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Solutions'] = []
        if self.solutions is not None:
            for k1 in self.solutions:
                result['Solutions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.solutions = []
        if m.get('Solutions') is not None:
            for k1 in m.get('Solutions'):
                temp_model = main_models.ListSolutionResponseBodySolutions()
                self.solutions.append(temp_model.from_map(k1))

        return self

class ListSolutionResponseBodySolutions(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: int = None,
        create_time: str = None,
        modify_time: str = None,
        perspective_codes: List[str] = None,
        plain_text: str = None,
        solution_id: int = None,
        tag_id_list: List[int] = None,
    ):
        self.content = content
        self.content_type = content_type
        self.create_time = create_time
        self.modify_time = modify_time
        self.perspective_codes = perspective_codes
        self.plain_text = plain_text
        self.solution_id = solution_id
        self.tag_id_list = tag_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes

        if self.plain_text is not None:
            result['PlainText'] = self.plain_text

        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id

        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')

        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')

        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')

        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')

        return self

