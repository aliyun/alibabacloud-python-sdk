# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class Evaluator(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        evaluator_ref: str = None,
        filters: Dict[str, Any] = None,
        name: str = None,
        result_name: str = None,
        result_type: str = None,
        type: str = None,
        variable_extractor_mapping: Dict[str, main_models.EvaluatorVariableExtractorMappingValue] = None,
        variable_mapping: Dict[str, str] = None,
    ):
        # The runtime configuration of the evaluator. For inline LLM evaluators, this must include configurations such as prompt. When referencing an existing evaluator, this parameter is typically not required and should only be specified when runtime parameters such as version need to be set.
        self.config = config
        # The reference name of a registered evaluator. When specified, the evaluator definition is loaded by this reference with higher priority. Both built-in evaluators and custom evaluators are supported.
        self.evaluator_ref = evaluator_ref
        # The evaluator-level data filter conditions. These take effect together with the task-level dataFilter.query.
        self.filters = filters
        # The evaluator name. Required for inline evaluators when evaluatorRef is not specified. The evaluatorRef or name must be unique within the same task.
        self.name = name
        # The field name for the evaluation result. Required for inline evaluators. When referencing an existing evaluator, the metricName defined in the evaluator definition is used if this parameter is not specified.
        self.result_name = result_name
        # The evaluation result type. Required for inline evaluators. When referencing an existing evaluator, defaults to score if not specified.
        self.result_type = result_type
        # The evaluator type. Defaults to LLM if not specified. Inline CODE evaluators are not currently supported. For the CODE type, reference a previously created evaluator by using evaluatorRef.
        self.type = type
        # The variable extraction rule mapping that maps evaluator variables to a portion of the content within an evaluation data field. This is applicable when the variable value is not the entire field but a subset of the field content. This parameter shares the same variable name key space as variableMapping. Each variable can use only one of the two. Duplicate configurations cause an error. When referencing an existing evaluator, the variable names must exist in the evaluator definition. Call ListTraceFieldExtractionsPreview to perform a trial run for validation before saving.
        self.variable_extractor_mapping = variable_extractor_mapping
        # The variable mapping that maps evaluator variables to evaluation data fields. Required for LLM/AGENT inline evaluators. When referencing an existing evaluator, the variable names must exist in the evaluator definition.
        self.variable_mapping = variable_mapping

    def validate(self):
        if self.variable_extractor_mapping:
            for v1 in self.variable_extractor_mapping.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.evaluator_ref is not None:
            result['evaluatorRef'] = self.evaluator_ref

        if self.filters is not None:
            result['filters'] = self.filters

        if self.name is not None:
            result['name'] = self.name

        if self.result_name is not None:
            result['resultName'] = self.result_name

        if self.result_type is not None:
            result['resultType'] = self.result_type

        if self.type is not None:
            result['type'] = self.type

        result['variableExtractorMapping'] = {}
        if self.variable_extractor_mapping is not None:
            for k1, v1 in self.variable_extractor_mapping.items():
                result['variableExtractorMapping'][k1] = v1.to_map() if v1 else None

        if self.variable_mapping is not None:
            result['variableMapping'] = self.variable_mapping

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('evaluatorRef') is not None:
            self.evaluator_ref = m.get('evaluatorRef')

        if m.get('filters') is not None:
            self.filters = m.get('filters')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resultName') is not None:
            self.result_name = m.get('resultName')

        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')

        if m.get('type') is not None:
            self.type = m.get('type')

        self.variable_extractor_mapping = {}
        if m.get('variableExtractorMapping') is not None:
            for k1, v1 in m.get('variableExtractorMapping').items():
                temp_model = main_models.EvaluatorVariableExtractorMappingValue()
                self.variable_extractor_mapping[k1] = temp_model.from_map(v1)

        if m.get('variableMapping') is not None:
            self.variable_mapping = m.get('variableMapping')

        return self

