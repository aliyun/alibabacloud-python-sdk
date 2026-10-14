# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StartAIAnalysisRequest(DaraModel):
    def __init__(
        self,
        analysis_tool: str = None,
        analysis_params: List[str] = None,
        channel: str = None,
        comms: str = None,
        created_by: str = None,
        instance: str = None,
        instance_type: str = None,
        iteration_func: str = None,
        iteration_mod: str = None,
        iteration_range: List[int] = None,
        pids: str = None,
        region: str = None,
        timeout: int = None,
        uid: str = None,
    ):
        # The analysis tool. This parameter does not need to be specified when you call this operation by using OpenAPI.
        self.analysis_tool = analysis_tool
        # The data richness.
        self.analysis_params = analysis_params
        # The channel name.
        self.channel = channel
        # The process name. This parameter is optional.
        self.comms = comms
        # The creator. This parameter does not need to be specified when you call this operation by using OpenAPI.
        self.created_by = created_by
        # The instance ID.
        self.instance = instance
        # The instance type. This parameter does not need to be specified when you call this operation by using OpenAPI.
        self.instance_type = instance_type
        # The iteration entry function. This parameter is required only in iteration mode and can be left empty.
        self.iteration_func = iteration_func
        # The iteration entry module. This parameter is required only in iteration mode and can be left empty.
        self.iteration_mod = iteration_mod
        # The iteration range. The iteration count refers to the number of iterations when the data collection module is activated, which is independent of the AI job iteration count.
        self.iteration_range = iteration_range
        # The process IDs (PIDs) of the AI job. Multiple PIDs are supported and separated by commas (,).
        self.pids = pids
        # The region ID.
        self.region = region
        # The AI Infra analysis duration.
        # Unit: milliseconds.
        # Default value: 2000.
        self.timeout = timeout
        # The Alibaba Cloud account ID. This parameter does not need to be specified when you call this operation by using OpenAPI.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_tool is not None:
            result['analysisTool'] = self.analysis_tool

        if self.analysis_params is not None:
            result['analysis_params'] = self.analysis_params

        if self.channel is not None:
            result['channel'] = self.channel

        if self.comms is not None:
            result['comms'] = self.comms

        if self.created_by is not None:
            result['created_by'] = self.created_by

        if self.instance is not None:
            result['instance'] = self.instance

        if self.instance_type is not None:
            result['instance_type'] = self.instance_type

        if self.iteration_func is not None:
            result['iteration_func'] = self.iteration_func

        if self.iteration_mod is not None:
            result['iteration_mod'] = self.iteration_mod

        if self.iteration_range is not None:
            result['iteration_range'] = self.iteration_range

        if self.pids is not None:
            result['pids'] = self.pids

        if self.region is not None:
            result['region'] = self.region

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisTool') is not None:
            self.analysis_tool = m.get('analysisTool')

        if m.get('analysis_params') is not None:
            self.analysis_params = m.get('analysis_params')

        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('comms') is not None:
            self.comms = m.get('comms')

        if m.get('created_by') is not None:
            self.created_by = m.get('created_by')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('instance_type') is not None:
            self.instance_type = m.get('instance_type')

        if m.get('iteration_func') is not None:
            self.iteration_func = m.get('iteration_func')

        if m.get('iteration_mod') is not None:
            self.iteration_mod = m.get('iteration_mod')

        if m.get('iteration_range') is not None:
            self.iteration_range = m.get('iteration_range')

        if m.get('pids') is not None:
            self.pids = m.get('pids')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

