# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PausePipelineResponseBody(DaraModel):
    def __init__(
        self,
        agent_space_name: str = None,
        pause_time: str = None,
        paused_reason: str = None,
        pipeline_name: str = None,
        request_id: str = None,
        schedule_status: str = None,
    ):
        # The name of the AgentSpace where the pipeline is located.
        self.agent_space_name = agent_space_name
        # The time when the pipeline was paused, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.pause_time = pause_time
        # The reason for pausing the pipeline.
        self.paused_reason = paused_reason
        # The name of the pipeline.
        self.pipeline_name = pipeline_name
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The scheduling status. The value is fixed as Paused.
        self.schedule_status = schedule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space_name is not None:
            result['agentSpaceName'] = self.agent_space_name

        if self.pause_time is not None:
            result['pauseTime'] = self.pause_time

        if self.paused_reason is not None:
            result['pausedReason'] = self.paused_reason

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.schedule_status is not None:
            result['scheduleStatus'] = self.schedule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpaceName') is not None:
            self.agent_space_name = m.get('agentSpaceName')

        if m.get('pauseTime') is not None:
            self.pause_time = m.get('pauseTime')

        if m.get('pausedReason') is not None:
            self.paused_reason = m.get('pausedReason')

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scheduleStatus') is not None:
            self.schedule_status = m.get('scheduleStatus')

        return self

