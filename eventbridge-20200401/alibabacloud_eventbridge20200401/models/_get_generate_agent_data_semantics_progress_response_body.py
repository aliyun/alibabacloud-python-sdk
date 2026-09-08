# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class GetGenerateAgentDataSemanticsProgressResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetGenerateAgentDataSemanticsProgressResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code of the operation.
        self.code = code
        # The generation progress details. When the initial generation is complete, a full snapshot of the current generation round is returned. When regeneration is complete, the current Metrics, Joins, Examples, and new Text are returned. To discard a regeneration, first call Get to retrieve the current official version, and then call Save with the four types of content unchanged to idempotently clean up temporary results.
        self.data = data
        # The response message. If the request fails, an error message is returned.
        self.message = message
        # The unique identifier that Alibaba Cloud generates for the request.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetGenerateAgentDataSemanticsProgressResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetGenerateAgentDataSemanticsProgressResponseBodyData(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        examples: List[main_models.AgentDataSemanticsExample] = None,
        joins: List[main_models.AgentDataSemanticsJoin] = None,
        metrics: List[main_models.AgentDataSemanticsMetric] = None,
        progress: List[main_models.AgentDataSemanticsStageProgress] = None,
        stage: str = None,
        text: main_models.AgentDataSemanticsText = None,
    ):
        # The error code returned when the generation task fails.
        self.error_code = error_code
        # The error message returned when the generation task fails.
        self.error_message = error_message
        # The SQL example knowledge returned when the generation is complete. A maximum of 50 items can be returned.
        self.examples = examples
        # The data association knowledge returned when the generation is complete. A maximum of 100 items can be returned.
        self.joins = joins
        # The SQL expression knowledge returned when the generation is complete. A maximum of 100 items can be returned.
        self.metrics = metrics
        # The four-phase stage progress. This parameter may not be returned when the overall generation is complete.
        self.progress = progress
        # The current overall stage.
        self.stage = stage
        # The Markdown text knowledge returned when the generation is complete.
        self.text = text

    def validate(self):
        if self.examples:
            for v1 in self.examples:
                 if v1:
                    v1.validate()
        if self.joins:
            for v1 in self.joins:
                 if v1:
                    v1.validate()
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()
        if self.progress:
            for v1 in self.progress:
                 if v1:
                    v1.validate()
        if self.text:
            self.text.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        result['Examples'] = []
        if self.examples is not None:
            for k1 in self.examples:
                result['Examples'].append(k1.to_map() if k1 else None)

        result['Joins'] = []
        if self.joins is not None:
            for k1 in self.joins:
                result['Joins'].append(k1.to_map() if k1 else None)

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        result['Progress'] = []
        if self.progress is not None:
            for k1 in self.progress:
                result['Progress'].append(k1.to_map() if k1 else None)

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.text is not None:
            result['Text'] = self.text.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.examples = []
        if m.get('Examples') is not None:
            for k1 in m.get('Examples'):
                temp_model = main_models.AgentDataSemanticsExample()
                self.examples.append(temp_model.from_map(k1))

        self.joins = []
        if m.get('Joins') is not None:
            for k1 in m.get('Joins'):
                temp_model = main_models.AgentDataSemanticsJoin()
                self.joins.append(temp_model.from_map(k1))

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.AgentDataSemanticsMetric()
                self.metrics.append(temp_model.from_map(k1))

        self.progress = []
        if m.get('Progress') is not None:
            for k1 in m.get('Progress'):
                temp_model = main_models.AgentDataSemanticsStageProgress()
                self.progress.append(temp_model.from_map(k1))

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('Text') is not None:
            temp_model = main_models.AgentDataSemanticsText()
            self.text = temp_model.from_map(m.get('Text'))

        return self

