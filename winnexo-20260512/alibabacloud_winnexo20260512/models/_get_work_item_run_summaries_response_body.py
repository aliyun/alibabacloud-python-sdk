# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetWorkItemRunSummariesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: List[main_models.GetWorkItemRunSummariesResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The common business status code.
        self.code = code
        # The execution summaries generated for the current plan and current turn. Previous summaries are not returned until new summaries are generated for affected nodes that are re-run.
        self.items = items
        # The common error description.
        self.message = message
        # The request tracking ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetWorkItemRunSummariesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetWorkItemRunSummariesResponseBodyItems(DaraModel):
    def __init__(
        self,
        attempt_id: str = None,
        attempt_seq: int = None,
        executor_id: str = None,
        executor_name: str = None,
        executor_type: str = None,
        finished_at: str = None,
        node_key: str = None,
        node_name: str = None,
        node_status: str = None,
        plan_id: str = None,
        result: Any = None,
        run_summary: Any = None,
        run_summary_error: str = None,
        run_summary_generated_at: str = None,
        run_summary_sources: List[Any] = None,
        run_summary_status: str = None,
        run_summary_tools: List[main_models.GetWorkItemRunSummariesResponseBodyItemsRunSummaryTools] = None,
        started_at: str = None,
        turn_seq: int = None,
    ):
        # The ID of the node attempt.
        self.attempt_id = attempt_id
        # The sequence number of the node attempt, starting from 1.
        self.attempt_seq = attempt_seq
        # The ID of the executor.
        self.executor_id = executor_id
        # The name of the executor.
        self.executor_name = executor_name
        # The executor type, such as AGENT or HUMAN.
        self.executor_type = executor_type
        # The end time of the node, in ISO 8601 format.
        self.finished_at = finished_at
        # The node key.
        self.node_key = node_key
        # The name of the node.
        self.node_name = node_name
        # The node status, such as COMPLETED or FAILED.
        self.node_status = node_status
        # The ID of the associated physical plan.
        self.plan_id = plan_id
        # The execution result of the node, as a JSON object.
        self.result = result
        # The content of the execution summary. This field is empty if the summary is not generated.
        self.run_summary = run_summary
        # The reason for the execution summary failure. This field is empty if the generation is successful.
        self.run_summary_error = run_summary_error
        # The generation time of the execution summary, in ISO 8601 format.
        self.run_summary_generated_at = run_summary_generated_at
        # The list of data sources referenced in the execution summary.
        self.run_summary_sources = run_summary_sources
        # The generation status of the execution summary, such as COMPLETED, FAILED, or PROCESSING.
        self.run_summary_status = run_summary_status
        # The list of tools used in the execution summary.
        self.run_summary_tools = run_summary_tools
        # The start time of the node, in ISO 8601 format.
        self.started_at = started_at
        # The sequence number of the node turn, starting from 1.
        self.turn_seq = turn_seq

    def validate(self):
        if self.run_summary_tools:
            for v1 in self.run_summary_tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempt_id is not None:
            result['attemptId'] = self.attempt_id

        if self.attempt_seq is not None:
            result['attemptSeq'] = self.attempt_seq

        if self.executor_id is not None:
            result['executorId'] = self.executor_id

        if self.executor_name is not None:
            result['executorName'] = self.executor_name

        if self.executor_type is not None:
            result['executorType'] = self.executor_type

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.node_key is not None:
            result['nodeKey'] = self.node_key

        if self.node_name is not None:
            result['nodeName'] = self.node_name

        if self.node_status is not None:
            result['nodeStatus'] = self.node_status

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.result is not None:
            result['result'] = self.result

        if self.run_summary is not None:
            result['runSummary'] = self.run_summary

        if self.run_summary_error is not None:
            result['runSummaryError'] = self.run_summary_error

        if self.run_summary_generated_at is not None:
            result['runSummaryGeneratedAt'] = self.run_summary_generated_at

        if self.run_summary_sources is not None:
            result['runSummarySources'] = self.run_summary_sources

        if self.run_summary_status is not None:
            result['runSummaryStatus'] = self.run_summary_status

        result['runSummaryTools'] = []
        if self.run_summary_tools is not None:
            for k1 in self.run_summary_tools:
                result['runSummaryTools'].append(k1.to_map() if k1 else None)

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.turn_seq is not None:
            result['turnSeq'] = self.turn_seq

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attemptId') is not None:
            self.attempt_id = m.get('attemptId')

        if m.get('attemptSeq') is not None:
            self.attempt_seq = m.get('attemptSeq')

        if m.get('executorId') is not None:
            self.executor_id = m.get('executorId')

        if m.get('executorName') is not None:
            self.executor_name = m.get('executorName')

        if m.get('executorType') is not None:
            self.executor_type = m.get('executorType')

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('nodeKey') is not None:
            self.node_key = m.get('nodeKey')

        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')

        if m.get('nodeStatus') is not None:
            self.node_status = m.get('nodeStatus')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('runSummary') is not None:
            self.run_summary = m.get('runSummary')

        if m.get('runSummaryError') is not None:
            self.run_summary_error = m.get('runSummaryError')

        if m.get('runSummaryGeneratedAt') is not None:
            self.run_summary_generated_at = m.get('runSummaryGeneratedAt')

        if m.get('runSummarySources') is not None:
            self.run_summary_sources = m.get('runSummarySources')

        if m.get('runSummaryStatus') is not None:
            self.run_summary_status = m.get('runSummaryStatus')

        self.run_summary_tools = []
        if m.get('runSummaryTools') is not None:
            for k1 in m.get('runSummaryTools'):
                temp_model = main_models.GetWorkItemRunSummariesResponseBodyItemsRunSummaryTools()
                self.run_summary_tools.append(temp_model.from_map(k1))

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('turnSeq') is not None:
            self.turn_seq = m.get('turnSeq')

        return self

class GetWorkItemRunSummariesResponseBodyItemsRunSummaryTools(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the tool.
        self.name = name
        # The tool type, such as SKILL or MCP.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

