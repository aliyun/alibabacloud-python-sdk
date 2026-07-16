# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetPipelineRunResponseBody(DaraModel):
    def __init__(
        self,
        agent_space_name: str = None,
        attempt: int = None,
        error_code: str = None,
        error_message: str = None,
        finish_time: str = None,
        from_time: int = None,
        max_attempts: int = None,
        next_retry_time: str = None,
        pipeline_name: str = None,
        request_id: str = None,
        results: Dict[str, Any] = None,
        run_id: str = None,
        start_time: str = None,
        stats: Dict[str, Any] = None,
        status: str = None,
        to_time: int = None,
        trigger_time: str = None,
        trigger_type: str = None,
    ):
        # The name of the AgentSpace to which the pipeline belongs.
        self.agent_space_name = agent_space_name
        # The current retry count.
        self.attempt = attempt
        # The semantic error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The finish time, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.finish_time = finish_time
        # The start of the data window, in UNIX seconds.
        self.from_time = from_time
        # The maximum number of retries.
        self.max_attempts = max_attempts
        # The next retry time, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.next_retry_time = next_retry_time
        # The name of the pipeline.
        self.pipeline_name = pipeline_name
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The inline run results. This field is returned only when output.inline is set to true at trigger time.
        self.results = results
        # Run Id
        self.run_id = run_id
        # The execution start time, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.start_time = start_time
        # The run statistics, including processedRows (number of processed rows), processedBytes (number of processed bytes), outputRows (number of output rows), outputBytes (number of output bytes), elapsedMs (elapsed time in milliseconds), cpuSec (CPU seconds), cpuCores (number of CPU cores), and tokenCount (number of tokens consumed).
        self.stats = stats
        # The run status. Valid values:
        # - Pending
        # - Running
        # - Succeeded
        # - Failed
        # - Cancelled
        self.status = status
        # The end of the data window, in UNIX seconds.
        self.to_time = to_time
        # The trigger time, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.trigger_time = trigger_time
        # The trigger type. Valid values:
        # - Scheduled
        # - Manual
        # - RunOnce
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space_name is not None:
            result['agentSpaceName'] = self.agent_space_name

        if self.attempt is not None:
            result['attempt'] = self.attempt

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.finish_time is not None:
            result['finishTime'] = self.finish_time

        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.max_attempts is not None:
            result['maxAttempts'] = self.max_attempts

        if self.next_retry_time is not None:
            result['nextRetryTime'] = self.next_retry_time

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.results is not None:
            result['results'] = self.results

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.stats is not None:
            result['stats'] = self.stats

        if self.status is not None:
            result['status'] = self.status

        if self.to_time is not None:
            result['toTime'] = self.to_time

        if self.trigger_time is not None:
            result['triggerTime'] = self.trigger_time

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpaceName') is not None:
            self.agent_space_name = m.get('agentSpaceName')

        if m.get('attempt') is not None:
            self.attempt = m.get('attempt')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')

        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('maxAttempts') is not None:
            self.max_attempts = m.get('maxAttempts')

        if m.get('nextRetryTime') is not None:
            self.next_retry_time = m.get('nextRetryTime')

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('results') is not None:
            self.results = m.get('results')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('stats') is not None:
            self.stats = m.get('stats')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        if m.get('triggerTime') is not None:
            self.trigger_time = m.get('triggerTime')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

