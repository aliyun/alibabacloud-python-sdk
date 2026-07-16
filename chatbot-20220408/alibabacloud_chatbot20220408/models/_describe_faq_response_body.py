# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class DescribeFaqResponseBody(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        create_time: str = None,
        create_user_name: str = None,
        effect_status: int = None,
        end_date: str = None,
        knowledge_id: int = None,
        modify_time: str = None,
        modify_user_name: str = None,
        outlines: List[main_models.DescribeFaqResponseBodyOutlines] = None,
        request_id: str = None,
        sim_questions: List[main_models.DescribeFaqResponseBodySimQuestions] = None,
        solutions: List[main_models.DescribeFaqResponseBodySolutions] = None,
        start_date: str = None,
        status: int = None,
        tag_id_list: List[int] = None,
        title: str = None,
    ):
        # The category ID.
        self.category_id = category_id
        # The time the knowledge was created, in UTC.
        self.create_time = create_time
        # The creator of the knowledge.
        self.create_user_name = create_user_name
        # The validity status of the knowledge, calculated based on `StartDate` and `EndDate`. Valid values: `20` (Active), `21` (Expired), and `22` (Pending).
        self.effect_status = effect_status
        # The expiration time of the knowledge, in UTC.
        self.end_date = end_date
        # The knowledge ID.
        self.knowledge_id = knowledge_id
        # The time the knowledge was last modified, in UTC.
        self.modify_time = modify_time
        # The user who last modified the knowledge.
        self.modify_user_name = modify_user_name
        # A list of related questions.
        self.outlines = outlines
        # The request ID.
        self.request_id = request_id
        # A list of similar questions.
        self.sim_questions = sim_questions
        # A list of solutions.
        self.solutions = solutions
        # The effective start time of the knowledge, in UTC.
        self.start_date = start_date
        # The knowledge status. Valid values: `-1` (Deleted and unpublished), `1` (Unpublished), `2` (Published), and `3` (Updated and unpublished).
        self.status = status
        # A list of tag IDs associated with the knowledge.
        self.tag_id_list = tag_id_list
        # The knowledge title.
        self.title = title

    def validate(self):
        if self.outlines:
            for v1 in self.outlines:
                 if v1:
                    v1.validate()
        if self.sim_questions:
            for v1 in self.sim_questions:
                 if v1:
                    v1.validate()
        if self.solutions:
            for v1 in self.solutions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name

        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SimQuestions'] = []
        if self.sim_questions is not None:
            for k1 in self.sim_questions:
                result['SimQuestions'].append(k1.to_map() if k1 else None)

        result['Solutions'] = []
        if self.solutions is not None:
            for k1 in self.solutions:
                result['Solutions'].append(k1.to_map() if k1 else None)

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_id_list is not None:
            result['TagIdList'] = self.tag_id_list

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')

        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.DescribeFaqResponseBodyOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sim_questions = []
        if m.get('SimQuestions') is not None:
            for k1 in m.get('SimQuestions'):
                temp_model = main_models.DescribeFaqResponseBodySimQuestions()
                self.sim_questions.append(temp_model.from_map(k1))

        self.solutions = []
        if m.get('Solutions') is not None:
            for k1 in m.get('Solutions'):
                temp_model = main_models.DescribeFaqResponseBodySolutions()
                self.solutions.append(temp_model.from_map(k1))

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagIdList') is not None:
            self.tag_id_list = m.get('TagIdList')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class DescribeFaqResponseBodySolutions(DaraModel):
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
        # The solution content.
        self.content = content
        # The solution content type. Valid values: `0` (plain text) and `1` (rich text).
        self.content_type = content_type
        # The time the solution was created, in UTC.
        self.create_time = create_time
        # The time the solution was last modified, in UTC.
        self.modify_time = modify_time
        # A list of perspective codes.
        self.perspective_codes = perspective_codes
        # The plain text content of the solution.
        self.plain_text = plain_text
        # The solution ID.
        self.solution_id = solution_id
        # A list of tag IDs.
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

class DescribeFaqResponseBodySimQuestions(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        sim_question_id: int = None,
        title: str = None,
    ):
        # The time the similar question was created, in UTC.
        self.create_time = create_time
        # The time the similar question was last modified, in UTC.
        self.modify_time = modify_time
        # The similar question ID.
        self.sim_question_id = sim_question_id
        # The similar question title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.sim_question_id is not None:
            result['SimQuestionId'] = self.sim_question_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('SimQuestionId') is not None:
            self.sim_question_id = m.get('SimQuestionId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class DescribeFaqResponseBodyOutlines(DaraModel):
    def __init__(
        self,
        conn_question_id: int = None,
        create_time: str = None,
        modify_time: str = None,
        outline_id: int = None,
        title: str = None,
    ):
        # The related knowledge ID.
        self.conn_question_id = conn_question_id
        # The time the related question was created, in UTC.
        self.create_time = create_time
        # The time the related question was last modified, in UTC.
        self.modify_time = modify_time
        # The relationship ID.
        self.outline_id = outline_id
        # The related knowledge title.
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

