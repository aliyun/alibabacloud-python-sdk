# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qweneduaisuite20261102 import models as main_models
from darabonba.model import DaraModel

class CreateEduHomeworkCorrectSubmitResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateEduHomeworkCorrectSubmitResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The API status.
        self.code = code
        # The import command.
        self.data = data
        # The request error message.
        self.message = message
        # The request ID of the caller.
        self.request_id = request_id

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

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateEduHomeworkCorrectSubmitResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateEduHomeworkCorrectSubmitResponseBodyData(DaraModel):
    def __init__(
        self,
        angle: int = None,
        dewarp_url: str = None,
        question_results: List[main_models.CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResults] = None,
        status: str = None,
        task_id: str = None,
    ):
        # The rotation angle of the image in the clockwise direction, in degrees.
        self.angle = angle
        # The URL of the corrected image. If `dewarp` is set to `false`, the original image is returned.
        self.dewarp_url = dewarp_url
        # The array of question recognition and grading results.
        self.question_results = question_results
        # The task status.
        self.status = status
        # The unique identifier of the task, which must be included in subsequent queries.
        self.task_id = task_id

    def validate(self):
        if self.question_results:
            for v1 in self.question_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.angle is not None:
            result['angle'] = self.angle

        if self.dewarp_url is not None:
            result['dewarpUrl'] = self.dewarp_url

        result['questionResults'] = []
        if self.question_results is not None:
            for k1 in self.question_results:
                result['questionResults'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('angle') is not None:
            self.angle = m.get('angle')

        if m.get('dewarpUrl') is not None:
            self.dewarp_url = m.get('dewarpUrl')

        self.question_results = []
        if m.get('questionResults') is not None:
            for k1 in m.get('questionResults'):
                temp_model = main_models.CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResults()
                self.question_results.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

class CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResults(DaraModel):
    def __init__(
        self,
        answer_results: List[main_models.CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsAnswerResults] = None,
        finish: bool = None,
        question_content: str = None,
        question_id: str = None,
        question_points: List[List[main_models.CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsQuestionPoints]] = None,
        question_type: str = None,
        solution: str = None,
    ):
        # The array of answering and grading results for the question.
        self.answer_results = answer_results
        # Specifies whether the task is completed. Valid values:
        # 
        # - **true**: The task is completed.
        # - **false**: The task is not completed.
        self.finish = finish
        # The text content of the question.
        self.question_content = question_content
        # The question ID.
        self.question_id = question_id
        # The coordinate group of the question area. It generally contains four vertex coordinates, arranged in the order of top-left, top-right, bottom-right, and bottom-left.
        self.question_points = question_points
        # The question type.
        self.question_type = question_type
        # The question analysis and solution.
        self.solution = solution

    def validate(self):
        if self.answer_results:
            for v1 in self.answer_results:
                 if v1:
                    v1.validate()
        if self.question_points:
            for v1 in self.question_points:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['answerResults'] = []
        if self.answer_results is not None:
            for k1 in self.answer_results:
                result['answerResults'].append(k1.to_map() if k1 else None)

        if self.finish is not None:
            result['finish'] = self.finish

        if self.question_content is not None:
            result['questionContent'] = self.question_content

        if self.question_id is not None:
            result['questionId'] = self.question_id

        result['questionPoints'] = []
        if self.question_points is not None:
            for k1 in self.question_points:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['questionPoints'].append(l1)

        if self.question_type is not None:
            result['questionType'] = self.question_type

        if self.solution is not None:
            result['solution'] = self.solution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_results = []
        if m.get('answerResults') is not None:
            for k1 in m.get('answerResults'):
                temp_model = main_models.CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsAnswerResults()
                self.answer_results.append(temp_model.from_map(k1))

        if m.get('finish') is not None:
            self.finish = m.get('finish')

        if m.get('questionContent') is not None:
            self.question_content = m.get('questionContent')

        if m.get('questionId') is not None:
            self.question_id = m.get('questionId')

        self.question_points = []
        if m.get('questionPoints') is not None:
            for k1 in m.get('questionPoints'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsQuestionPoints()
                    l1.append(temp_model.from_map(k2))
                self.question_points.append(l1)

        if m.get('questionType') is not None:
            self.question_type = m.get('questionType')

        if m.get('solution') is not None:
            self.solution = m.get('solution')

        return self

class CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsQuestionPoints(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        # The X-axis coordinate value.
        self.x = x
        # The Y-axis coordinate value.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

class CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsAnswerResults(DaraModel):
    def __init__(
        self,
        answer_points: List[main_models.CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsAnswerResultsAnswerPoints] = None,
        check_point: main_models.CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsAnswerResultsCheckPoint = None,
        check_result: str = None,
        standard_answer: str = None,
        user_answer: str = None,
    ):
        # The coordinate group of the user\\"s answering area. It generally contains four vertex coordinates, arranged in the order of top-left, top-right, bottom-right, and bottom-left, such as `[{"x": ..., "y": ...}, ...]`.
        self.answer_points = answer_points
        # The coordinates of the grading mark point, such as `{ "x": ..., "y": ... }`.
        self.check_point = check_point
        # The grading conclusion, such as `correct`, `wrong`, or `partial`.
        self.check_result = check_result
        # The ground truth.
        self.standard_answer = standard_answer
        # The student\\"s answer.
        self.user_answer = user_answer

    def validate(self):
        if self.answer_points:
            for v1 in self.answer_points:
                 if v1:
                    v1.validate()
        if self.check_point:
            self.check_point.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['answerPoints'] = []
        if self.answer_points is not None:
            for k1 in self.answer_points:
                result['answerPoints'].append(k1.to_map() if k1 else None)

        if self.check_point is not None:
            result['checkPoint'] = self.check_point.to_map()

        if self.check_result is not None:
            result['checkResult'] = self.check_result

        if self.standard_answer is not None:
            result['standardAnswer'] = self.standard_answer

        if self.user_answer is not None:
            result['userAnswer'] = self.user_answer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_points = []
        if m.get('answerPoints') is not None:
            for k1 in m.get('answerPoints'):
                temp_model = main_models.CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsAnswerResultsAnswerPoints()
                self.answer_points.append(temp_model.from_map(k1))

        if m.get('checkPoint') is not None:
            temp_model = main_models.CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsAnswerResultsCheckPoint()
            self.check_point = temp_model.from_map(m.get('checkPoint'))

        if m.get('checkResult') is not None:
            self.check_result = m.get('checkResult')

        if m.get('standardAnswer') is not None:
            self.standard_answer = m.get('standardAnswer')

        if m.get('userAnswer') is not None:
            self.user_answer = m.get('userAnswer')

        return self

class CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsAnswerResultsCheckPoint(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        # The X-axis coordinate.
        self.x = x
        # The Y-axis coordinate.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

class CreateEduHomeworkCorrectSubmitResponseBodyDataQuestionResultsAnswerResultsAnswerPoints(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        # The X-axis coordinate value.
        self.x = x
        # The Y-axis coordinate value.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

