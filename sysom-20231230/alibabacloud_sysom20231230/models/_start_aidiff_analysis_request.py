# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class StartAIDiffAnalysisRequest(DaraModel):
    def __init__(
        self,
        task_1: main_models.StartAIDiffAnalysisRequestTask1 = None,
        task_2: main_models.StartAIDiffAnalysisRequestTask2 = None,
    ):
        # This parameter is required.
        self.task_1 = task_1
        # This parameter is required.
        self.task_2 = task_2

    def validate(self):
        if self.task_1:
            self.task_1.validate()
        if self.task_2:
            self.task_2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_1 is not None:
            result['task1'] = self.task_1.to_map()

        if self.task_2 is not None:
            result['task2'] = self.task_2.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task1') is not None:
            temp_model = main_models.StartAIDiffAnalysisRequestTask1()
            self.task_1 = temp_model.from_map(m.get('task1'))

        if m.get('task2') is not None:
            temp_model = main_models.StartAIDiffAnalysisRequestTask2()
            self.task_2 = temp_model.from_map(m.get('task2'))

        return self

class StartAIDiffAnalysisRequestTask2(DaraModel):
    def __init__(
        self,
        analysis_id: str = None,
        pids: List[str] = None,
        step_end: float = None,
        step_start: float = None,
    ):
        # This parameter is required.
        self.analysis_id = analysis_id
        # This parameter is required.
        self.pids = pids
        # This parameter is required.
        self.step_end = step_end
        # This parameter is required.
        self.step_start = step_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id

        if self.pids is not None:
            result['pids'] = self.pids

        if self.step_end is not None:
            result['step_end'] = self.step_end

        if self.step_start is not None:
            result['step_start'] = self.step_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')

        if m.get('pids') is not None:
            self.pids = m.get('pids')

        if m.get('step_end') is not None:
            self.step_end = m.get('step_end')

        if m.get('step_start') is not None:
            self.step_start = m.get('step_start')

        return self

class StartAIDiffAnalysisRequestTask1(DaraModel):
    def __init__(
        self,
        analysis_id: str = None,
        pids: List[str] = None,
        step_end: float = None,
        step_start: float = None,
    ):
        self.analysis_id = analysis_id
        self.pids = pids
        self.step_end = step_end
        self.step_start = step_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id

        if self.pids is not None:
            result['pids'] = self.pids

        if self.step_end is not None:
            result['step_end'] = self.step_end

        if self.step_start is not None:
            result['step_start'] = self.step_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')

        if m.get('pids') is not None:
            self.pids = m.get('pids')

        if m.get('step_end') is not None:
            self.step_end = m.get('step_end')

        if m.get('step_start') is not None:
            self.step_start = m.get('step_start')

        return self

