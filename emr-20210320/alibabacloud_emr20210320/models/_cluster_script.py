# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ClusterScript(DaraModel):
    def __init__(
        self,
        execution_fail_strategy: str = None,
        execution_moment: str = None,
        node_select: main_models.NodeSelector = None,
        priority: int = None,
        script_args: str = None,
        script_name: str = None,
        script_path: str = None,
    ):
        self.execution_fail_strategy = execution_fail_strategy
        self.execution_moment = execution_moment
        self.node_select = node_select
        self.priority = priority
        self.script_args = script_args
        self.script_name = script_name
        self.script_path = script_path

    def validate(self):
        if self.node_select:
            self.node_select.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_fail_strategy is not None:
            result['ExecutionFailStrategy'] = self.execution_fail_strategy

        if self.execution_moment is not None:
            result['ExecutionMoment'] = self.execution_moment

        if self.node_select is not None:
            result['NodeSelect'] = self.node_select.to_map()

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.script_args is not None:
            result['ScriptArgs'] = self.script_args

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.script_path is not None:
            result['ScriptPath'] = self.script_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionFailStrategy') is not None:
            self.execution_fail_strategy = m.get('ExecutionFailStrategy')

        if m.get('ExecutionMoment') is not None:
            self.execution_moment = m.get('ExecutionMoment')

        if m.get('NodeSelect') is not None:
            temp_model = main_models.NodeSelector()
            self.node_select = temp_model.from_map(m.get('NodeSelect'))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ScriptArgs') is not None:
            self.script_args = m.get('ScriptArgs')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('ScriptPath') is not None:
            self.script_path = m.get('ScriptPath')

        return self

