# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class CreateLogtailPipelineConfigRequest(DaraModel):
    def __init__(
        self,
        aggregators: List[Dict[str, Any]] = None,
        config_name: str = None,
        flushers: List[Dict[str, Any]] = None,
        global_: Dict[str, Any] = None,
        inputs: List[Dict[str, Any]] = None,
        log_sample: str = None,
        processors: List[Dict[str, Any]] = None,
        task: Dict[str, Any] = None,
    ):
        # The list of aggregation plugins. >Notice: This parameter is valid only when you use extension processing plugins. You can use a maximum of one aggregation plugin.
        self.aggregators = aggregators
        # The name of the configuration.
        # 
        # > The configuration name must be unique within the project and cannot be modified after the configuration is created. The name must follow these rules:
        # >
        # > - It can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # >
        # > - It must start and end with a lowercase letter or a digit.
        # >
        # > - It must be 2 to 128 characters in length.
        # 
        # This parameter is required.
        self.config_name = config_name
        # The list of output plugins. >Notice: Currently, you can add only one flusher_sls plugin.
        # 
        # This parameter is required.
        self.flushers = flushers
        # The global configuration.
        self.global_ = global_
        # The list of input plugins. >Notice: Currently, you can configure only one input plugin.
        # 
        # This parameter is required.
        self.inputs = inputs
        # A sample log. Multiple log entries are supported.
        self.log_sample = log_sample
        # The list of processing plugins.
        # 
        # > Processing plugins are classified into native processing plugins and extension processing plugins. For more information, see [Processing plugins](https://help.aliyun.com/document_detail/64957.html).
        # 
        # >Notice: 
        # 
        # > - Native plugins can be used only to collect text logs.
        # >
        # > - You cannot add native plugins and extension plugins at the same time.
        # >
        # > - When you use native plugins, the following requirements must be met:
        # >
        # >   - The first processing plugin must be a regular expression-based parsing plugin, a separator-based parsing plugin, a JSON-based parsing plugin, an NGINX-based parsing plugin, an Apache-based parsing plugin, or an IIS-based parsing plugin.
        # >
        # >   - After the first processing plugin, you can add only one time parsing processing plugin, one filter plugin, and multiple data masking plugins.
        self.processors = processors
        # The task configuration.
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

        if self.flushers is not None:
            result['flushers'] = self.flushers

        if self.global_ is not None:
            result['global'] = self.global_

        if self.inputs is not None:
            result['inputs'] = self.inputs

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

        if m.get('flushers') is not None:
            self.flushers = m.get('flushers')

        if m.get('global') is not None:
            self.global_ = m.get('global')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('logSample') is not None:
            self.log_sample = m.get('logSample')

        if m.get('processors') is not None:
            self.processors = m.get('processors')

        if m.get('task') is not None:
            self.task = m.get('task')

        return self

