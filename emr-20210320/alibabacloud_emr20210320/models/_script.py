# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class Script(DaraModel):
    def __init__(
        self,
        execution_fail_strategy: str = None,
        execution_moment: str = None,
        node_selector: main_models.NodeSelector = None,
        priority: int = None,
        script_args: str = None,
        script_name: str = None,
        script_path: str = None,
    ):
        # The execution failure strategy. Valid values:
        # 
        # - `FAILED_CONTINUE`: If the script fails, cluster creation or scaling continues.
        # 
        # - `FAILED_BLOCK`: If the script fails, cluster creation or scaling is blocked.
        self.execution_fail_strategy = execution_fail_strategy
        # The execution timing for the script. Valid values:
        # 
        # - `BEFORE_INSTALL`: The script runs before applications are installed.
        # 
        # - `AFTER_STARTED`: The script runs after applications start.
        self.execution_moment = execution_moment
        # Specifies the nodes on which the script runs.
        # 
        # This parameter is required.
        self.node_selector = node_selector
        # > This parameter is deprecated. Scripts run in the order they are defined.
        self.priority = priority
        # The optional script execution arguments.
        self.script_args = script_args
        # The required script name. The name must be 1 to 64 characters long and start with a letter or a Chinese character. It cannot start with `http://` or `https://`. It can contain Chinese characters, letters, numbers, underscores (`_`), or hyphens (`-`).
        # 
        # This parameter is required.
        self.script_name = script_name
        # The required path to the script in Object Storage Service (OSS). The path must start with `oss://`.
        # 
        # This parameter is required.
        self.script_path = script_path

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_fail_strategy is not None:
            result['ExecutionFailStrategy'] = self.execution_fail_strategy

        if self.execution_moment is not None:
            result['ExecutionMoment'] = self.execution_moment

        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()

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

        if m.get('NodeSelector') is not None:
            temp_model = main_models.NodeSelector()
            self.node_selector = temp_model.from_map(m.get('NodeSelector'))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ScriptArgs') is not None:
            self.script_args = m.get('ScriptArgs')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('ScriptPath') is not None:
            self.script_path = m.get('ScriptPath')

        return self

