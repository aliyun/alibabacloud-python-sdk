# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class LogtailPipelineConfig(DaraModel):
    def __init__(
        self,
        aggregators: List[Dict[str, Any]] = None,
        config_name: str = None,
        create_time: int = None,
        flushers: List[Dict[str, Any]] = None,
        global_: Dict[str, Any] = None,
        inputs: List[Dict[str, Any]] = None,
        last_modify_time: int = None,
        log_sample: str = None,
        processors: List[Dict[str, Any]] = None,
        task: Dict[str, Any] = None,
    ):
        self.aggregators = aggregators
        # This parameter is required.
        self.config_name = config_name
        self.create_time = create_time
        # This parameter is required.
        self.flushers = flushers
        self.global_ = global_
        # This parameter is required.
        self.inputs = inputs
        self.last_modify_time = last_modify_time
        self.log_sample = log_sample
        self.processors = processors
        self.task = task

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregators is not None:
            result['aggregators'] = self.aggregators

        if self.config_name is not None:
            result['configName'] = self.config_name

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.flushers is not None:
            result['flushers'] = self.flushers

        if self.global_ is not None:
            result['global'] = self.global_

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time

        if self.log_sample is not None:
            result['logSample'] = self.log_sample

        if self.processors is not None:
            result['processors'] = self.processors

        if self.task is not None:
            result['task'] = self.task

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregators') is not None:
            self.aggregators = m.get('aggregators')

        if m.get('configName') is not None:
            self.config_name = m.get('configName')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('flushers') is not None:
            self.flushers = m.get('flushers')

        if m.get('global') is not None:
            self.global_ = m.get('global')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')

        if m.get('logSample') is not None:
            self.log_sample = m.get('logSample')

        if m.get('processors') is not None:
            self.processors = m.get('processors')

        if m.get('task') is not None:
            self.task = m.get('task')

        return self

