# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class UpdateLogtailPipelineConfigRequest(DaraModel):
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
        # The list of aggregator plug-ins.
        # 
        # >Notice: 
        # 
        # This parameter is valid only when you use an extension processing plug-in. You can use a maximum of one aggregator plug-in.
        self.aggregators = aggregators
        # The name of the configuration.
        # 
        # >Notice: 
        # 
        # The name must be the same as the value of the configName parameter in the request path.
        # 
        # This parameter is required.
        self.config_name = config_name
        # The list of output plug-ins.
        # 
        # >Notice: 
        # 
        # Currently, you can add only one SLS output plug-in.
        # 
        # This parameter is required.
        self.flushers = flushers
        # The global configuration.
        self.global_ = global_
        # The list of input plug-ins.
        # 
        # >Notice: 
        # 
        # Currently, you can configure only one input plug-in.
        # 
        # This parameter is required.
        self.inputs = inputs
        # A sample log. Multiple logs are supported.
        self.log_sample = log_sample
        # The list of processing plug-ins.
        # 
        # > Processing plug-ins are classified into native processing plug-ins and extension processing plug-ins. For more information, see [Processing plug-ins](https://help.aliyun.com/document_detail/64957.html).
        # 
        # >Notice: 
        # 
        # > - Native plug-ins can be used only to collect text logs.
        # >
        # > - You cannot add native plug-ins and extension plug-ins at the same time.
        # >
        # > - When you use native plug-ins, the following requirements must be met:
        # >
        # >   - The first processing plug-in must be a regular expression-based parsing plug-in, a separator-based parsing plug-in, a JSON-based parsing plug-in, an NGINX-based parsing plug-in, an Apache-based parsing plug-in, or an IIS-based parsing plug-in.
        # >
        # >   - After the first processing plug-in, you can add only one time parsing plug-in, one filter plug-in, and multiple data masking plug-ins.
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

