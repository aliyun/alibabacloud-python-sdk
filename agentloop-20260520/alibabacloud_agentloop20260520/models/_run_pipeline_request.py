# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class RunPipelineRequest(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        output: main_models.RunPipelineRequestOutput = None,
        to_time: int = None,
    ):
        self.from_time = from_time
        self.output = output
        self.to_time = to_time

    def validate(self):
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.output is not None:
            result['output'] = self.output.to_map()

        if self.to_time is not None:
            result['toTime'] = self.to_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('output') is not None:
            temp_model = main_models.RunPipelineRequestOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        return self

class RunPipelineRequestOutput(DaraModel):
    def __init__(
        self,
        dataset: bool = None,
        inline: bool = None,
    ):
        self.dataset = dataset
        self.inline = inline

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset is not None:
            result['dataset'] = self.dataset

        if self.inline is not None:
            result['inline'] = self.inline

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataset') is not None:
            self.dataset = m.get('dataset')

        if m.get('inline') is not None:
            self.inline = m.get('inline')

        return self

