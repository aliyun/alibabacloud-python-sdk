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
        # The aggregation plug-ins.
        # 
        # >  This parameter takes effect only when extended plug-ins are used. You can use only one aggregation plug-in.
        self.aggregators = aggregators
        # The name of the configuration.
        # 
        # >  The value of this parameter must be the same as the value of configName in the outer layer.
        # 
        # This parameter is required.
        self.config_name = config_name
        # The output plug-ins.
        # 
        # >  You can configure only one output plug-in.
        # 
        # This parameter is required.
        self.flushers = flushers
        # The global settings.
        self.global_ = global_
        # The input plug-ins.
        # 
        # >  You can configure only one input plug-in.
        # 
        # This parameter is required.
        self.inputs = inputs
        # The sample log. You can specify multiple sample logs.
        self.log_sample = log_sample
        # The processing plug-ins.
        # 
        # >  Logtail plug-ins for data processing are classified into native plug-ins and extended plug-ins. For more information, see [Overview of Logtail plug-ins for data processing](https://help.aliyun.com/document_detail/64957.html).
        # 
        # > 
        # 
        # *   You can use native plug-ins only to collect text logs.
        # 
        # *   You cannot add native plug-ins and extended plug-ins at a time.
        # 
        # *   When you add native plug-ins, take note of the following items:
        # 
        #     *   You must add one of the following Logtail plug-ins for data processing as the first plug-in: Data Parsing (Regex Mode), Data Parsing (Delimiter Mode), Data Parsing (JSON Mode), Data Parsing (NGINX Mode), Data Parsing (Apache Mode), and Data Parsing (IIS Mode).
        #     *   After you add the first plug-in, you can add one Time Parsing plug-in, one Data Filtering plug-in, and multiple Data Masking plug-ins.
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

