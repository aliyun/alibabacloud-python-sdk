# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TerminatePipelineResponseBody(DaraModel):
    def __init__(
        self,
        agent_space_name: str = None,
        pipeline_name: str = None,
        request_id: str = None,
        schedule_status: str = None,
        terminate_time: str = None,
        terminated_reason: str = None,
    ):
        self.agent_space_name = agent_space_name
        self.pipeline_name = pipeline_name
        self.request_id = request_id
        self.schedule_status = schedule_status
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.terminate_time = terminate_time
        self.terminated_reason = terminated_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space_name is not None:
            result['agentSpaceName'] = self.agent_space_name

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.schedule_status is not None:
            result['scheduleStatus'] = self.schedule_status

        if self.terminate_time is not None:
            result['terminateTime'] = self.terminate_time

        if self.terminated_reason is not None:
            result['terminatedReason'] = self.terminated_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpaceName') is not None:
            self.agent_space_name = m.get('agentSpaceName')

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scheduleStatus') is not None:
            self.schedule_status = m.get('scheduleStatus')

        if m.get('terminateTime') is not None:
            self.terminate_time = m.get('terminateTime')

        if m.get('terminatedReason') is not None:
            self.terminated_reason = m.get('terminatedReason')

        return self

