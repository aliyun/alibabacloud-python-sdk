# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class Hook(DaraModel):
    def __init__(
        self,
        debug: bool = None,
        description: str = None,
        enable: bool = None,
        event: str = None,
        execution: main_models.HookExecution = None,
        invisible: bool = None,
        match: List[str] = None,
        name: str = None,
        schema_version: str = None,
        scope: str = None,
    ):
        # Specifies whether to enable debug mode.
        self.debug = debug
        # The description.
        self.description = description
        # Specifies whether the Hook is enabled. It is executed only when this parameter is set to true. If not configured, the Hook is disabled.
        self.enable = enable
        # The event. Each Hook processes only one event.
        self.event = event
        # The execution configuration. Configures the synchronous execution, total timeout, number of retries, and invalid return value handling policy for the Hook.
        self.execution = execution
        # Specifies whether to hide Hook invocation events. When set to true, Hook invocation events are not sent to the frontend, regardless of whether debug mode is enabled.
        self.invisible = invisible
        # The list of tool names. Only ToolStart and ToolEnd perform an exact match based on the actual tool name. Tool names such as Read, Write, Bash, and Edit are supported. Wildcards are not supported. An empty array does not restrict tools. This field is ignored for other events.
        self.match = match
        # The Hook name. Only digits, letters, underscores, and hyphens are allowed, and it cannot be empty. Hooks with the same name are executed independently in the order of the list.
        self.name = name
        # The configuration protocol version.
        self.schema_version = schema_version
        # The effective scope. A value of all indicates Chat and Mission. A value of chat or mission indicates that the Hook takes effect only in the corresponding scenario.
        self.scope = scope

    def validate(self):
        if self.execution:
            self.execution.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debug is not None:
            result['debug'] = self.debug

        if self.description is not None:
            result['description'] = self.description

        if self.enable is not None:
            result['enable'] = self.enable

        if self.event is not None:
            result['event'] = self.event

        if self.execution is not None:
            result['execution'] = self.execution.to_map()

        if self.invisible is not None:
            result['invisible'] = self.invisible

        if self.match is not None:
            result['match'] = self.match

        if self.name is not None:
            result['name'] = self.name

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        if self.scope is not None:
            result['scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('debug') is not None:
            self.debug = m.get('debug')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('execution') is not None:
            temp_model = main_models.HookExecution()
            self.execution = temp_model.from_map(m.get('execution'))

        if m.get('invisible') is not None:
            self.invisible = m.get('invisible')

        if m.get('match') is not None:
            self.match = m.get('match')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        return self

class HookExecution(DaraModel):
    def __init__(
        self,
        fail_result: str = None,
        instruction: str = None,
        max_retry: int = None,
        timeout_seconds: int = None,
        type: str = None,
    ):
        # The invalid return value handling policy. If the handler return value is still invalid after retries, it is processed as allow or reject.
        self.fail_result = fail_result
        # The execution instruction. For the prompt type, it is a prompt. For the bash type, it is a Bash script. For the python3 type, it is a Python 3 script. For the hint type, it is contextual text directly appended. Non-empty UTF-8 text must be provided for all four types.
        self.instruction = instruction
        # The maximum number of retries. Specifies the number of additional attempts after a failure. Valid values: 0 to 3.
        self.max_retry = max_retry
        # The timeout period in seconds. Valid values: 1 to 30. All attempts and waits for this Hook share this timeout period.
        self.timeout_seconds = timeout_seconds
        # The handler type. Only prompt, bash, python3, and hint are supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_result is not None:
            result['failResult'] = self.fail_result

        if self.instruction is not None:
            result['instruction'] = self.instruction

        if self.max_retry is not None:
            result['maxRetry'] = self.max_retry

        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failResult') is not None:
            self.fail_result = m.get('failResult')

        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('maxRetry') is not None:
            self.max_retry = m.get('maxRetry')

        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

