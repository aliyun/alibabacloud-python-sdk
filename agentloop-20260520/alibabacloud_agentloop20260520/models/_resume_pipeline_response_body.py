# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResumePipelineResponseBody(DaraModel):
    def __init__(
        self,
        agent_space_name: str = None,
        committed_watermark: int = None,
        next_trigger_time: int = None,
        pipeline_name: str = None,
        request_id: str = None,
        schedule_status: str = None,
    ):
        # The name of the AgentSpace where the pipeline is located.
        self.agent_space_name = agent_space_name
        # The committed watermark, in UNIX seconds.
        self.committed_watermark = committed_watermark
        # The next scheduling trigger time, in UNIX seconds.
        self.next_trigger_time = next_trigger_time
        # The name of the pipeline.
        self.pipeline_name = pipeline_name
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The scheduling status. The value is fixed to Active.
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

        if self.committed_watermark is not None:
            result['committedWatermark'] = self.committed_watermark

        if self.next_trigger_time is not None:
            result['nextTriggerTime'] = self.next_trigger_time

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

        if m.get('committedWatermark') is not None:
            self.committed_watermark = m.get('committedWatermark')

        if m.get('nextTriggerTime') is not None:
            self.next_trigger_time = m.get('nextTriggerTime')

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('scheduleStatus') is not None:
            self.schedule_status = m.get('scheduleStatus')

        return self

