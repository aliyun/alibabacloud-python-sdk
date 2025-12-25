# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PolicyClassInfo(DaraModel):
    def __init__(
        self,
        alias: str = None,
        attachable_resource_types: List[str] = None,
        class_id: str = None,
        config_example: str = None,
        deprecated: bool = None,
        description: str = None,
        direction: str = None,
        enable_log: bool = None,
        execute_priority: str = None,
        execute_stage: str = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.alias = alias
        self.attachable_resource_types = attachable_resource_types
        self.class_id = class_id
        self.config_example = config_example
        self.deprecated = deprecated
        self.description = description
        self.direction = direction
        self.enable_log = enable_log
        self.execute_priority = execute_priority
        self.execute_stage = execute_stage
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.attachable_resource_types is not None:
            result['attachableResourceTypes'] = self.attachable_resource_types

        if self.class_id is not None:
            result['classId'] = self.class_id

        if self.config_example is not None:
            result['configExample'] = self.config_example

        if self.deprecated is not None:
            result['deprecated'] = self.deprecated

        if self.description is not None:
            result['description'] = self.description

        if self.direction is not None:
            result['direction'] = self.direction

        if self.enable_log is not None:
            result['enableLog'] = self.enable_log

        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority

        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('attachableResourceTypes') is not None:
            self.attachable_resource_types = m.get('attachableResourceTypes')

        if m.get('classId') is not None:
            self.class_id = m.get('classId')

        if m.get('configExample') is not None:
            self.config_example = m.get('configExample')

        if m.get('deprecated') is not None:
            self.deprecated = m.get('deprecated')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('enableLog') is not None:
            self.enable_log = m.get('enableLog')

        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')

        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

