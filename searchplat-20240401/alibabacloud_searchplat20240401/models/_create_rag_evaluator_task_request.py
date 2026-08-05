# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class CreateRagEvaluatorTaskRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        data: List[main_models.CreateRagEvaluatorTaskRequestData] = None,
        data_source_config: Any = None,
        emails: List[str] = None,
        evaluate_config: main_models.CreateRagEvaluatorTaskRequestEvaluateConfig = None,
        has_data_source: bool = None,
        metrics: List[Any] = None,
        task_name: str = None,
    ):
        # app_name
        self.app_name = app_name
        # The list of evaluation data.
        self.data = data
        # The datasource config.
        self.data_source_config = data_source_config
        # emails
        self.emails = emails
        # The evaluation configuration.
        self.evaluate_config = evaluate_config
        # has_data_source
        self.has_data_source = has_data_source
        # The metric values. Valid values:
        # - context_recall
        # - context_precision
        # - faithfulness
        # - satisfaction
        # - comprehensive_score.
        self.metrics = metrics
        # The evaluation task name.
        self.task_name = task_name

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.evaluate_config:
            self.evaluate_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['app_name'] = self.app_name

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.data_source_config is not None:
            result['data_source_config'] = self.data_source_config

        if self.emails is not None:
            result['emails'] = self.emails

        if self.evaluate_config is not None:
            result['evaluate_config'] = self.evaluate_config.to_map()

        if self.has_data_source is not None:
            result['has_data_source'] = self.has_data_source

        if self.metrics is not None:
            result['metrics'] = self.metrics

        if self.task_name is not None:
            result['task_name'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_name') is not None:
            self.app_name = m.get('app_name')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.CreateRagEvaluatorTaskRequestData()
                self.data.append(temp_model.from_map(k1))

        if m.get('data_source_config') is not None:
            self.data_source_config = m.get('data_source_config')

        if m.get('emails') is not None:
            self.emails = m.get('emails')

        if m.get('evaluate_config') is not None:
            temp_model = main_models.CreateRagEvaluatorTaskRequestEvaluateConfig()
            self.evaluate_config = temp_model.from_map(m.get('evaluate_config'))

        if m.get('has_data_source') is not None:
            self.has_data_source = m.get('has_data_source')

        if m.get('metrics') is not None:
            self.metrics = m.get('metrics')

        if m.get('task_name') is not None:
            self.task_name = m.get('task_name')

        return self

class CreateRagEvaluatorTaskRequestEvaluateConfig(DaraModel):
    def __init__(
        self,
        model: str = None,
        prompt: str = None,
        run_all_step: bool = None,
    ):
        # The model to use.
        self.model = model
        # prompt
        self.prompt = prompt
        # run_all_step
        self.run_all_step = run_all_step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['model'] = self.model

        if self.prompt is not None:
            result['prompt'] = self.prompt

        if self.run_all_step is not None:
            result['run_all_step'] = self.run_all_step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        if m.get('run_all_step') is not None:
            self.run_all_step = m.get('run_all_step')

        return self

class CreateRagEvaluatorTaskRequestData(DaraModel):
    def __init__(
        self,
        model_answer: str = None,
        question: str = None,
        recall_docs: List[str] = None,
        standard_answer: str = None,
    ):
        # model_answer
        self.model_answer = model_answer
        # question
        self.question = question
        # recall_docs
        self.recall_docs = recall_docs
        # standard_answer
        self.standard_answer = standard_answer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_answer is not None:
            result['model_answer'] = self.model_answer

        if self.question is not None:
            result['question'] = self.question

        if self.recall_docs is not None:
            result['recall_docs'] = self.recall_docs

        if self.standard_answer is not None:
            result['standard_answer'] = self.standard_answer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model_answer') is not None:
            self.model_answer = m.get('model_answer')

        if m.get('question') is not None:
            self.question = m.get('question')

        if m.get('recall_docs') is not None:
            self.recall_docs = m.get('recall_docs')

        if m.get('standard_answer') is not None:
            self.standard_answer = m.get('standard_answer')

        return self

