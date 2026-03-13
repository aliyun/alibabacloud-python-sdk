# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class ListEvaluationScoreHistoryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        score_history: main_models.ListEvaluationScoreHistoryResponseBodyScoreHistory = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The historical scores.
        self.score_history = score_history

    def validate(self):
        if self.score_history:
            self.score_history.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.score_history is not None:
            result['ScoreHistory'] = self.score_history.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScoreHistory') is not None:
            temp_model = main_models.ListEvaluationScoreHistoryResponseBodyScoreHistory()
            self.score_history = temp_model.from_map(m.get('ScoreHistory'))

        return self

class ListEvaluationScoreHistoryResponseBodyScoreHistory(DaraModel):
    def __init__(
        self,
        total_score_history: List[main_models.ListEvaluationScoreHistoryResponseBodyScoreHistoryTotalScoreHistory] = None,
    ):
        # The historical scores.
        self.total_score_history = total_score_history

    def validate(self):
        if self.total_score_history:
            for v1 in self.total_score_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TotalScoreHistory'] = []
        if self.total_score_history is not None:
            for k1 in self.total_score_history:
                result['TotalScoreHistory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.total_score_history = []
        if m.get('TotalScoreHistory') is not None:
            for k1 in m.get('TotalScoreHistory'):
                temp_model = main_models.ListEvaluationScoreHistoryResponseBodyScoreHistoryTotalScoreHistory()
                self.total_score_history.append(temp_model.from_map(k1))

        return self

class ListEvaluationScoreHistoryResponseBodyScoreHistoryTotalScoreHistory(DaraModel):
    def __init__(
        self,
        evaluation_time: str = None,
        score: float = None,
    ):
        # The time when the score was generated. The time is in UTC.
        self.evaluation_time = evaluation_time
        # The score.
        # 
        # Valid values: 0 to 1.
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.evaluation_time is not None:
            result['EvaluationTime'] = self.evaluation_time

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationTime') is not None:
            self.evaluation_time = m.get('EvaluationTime')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

