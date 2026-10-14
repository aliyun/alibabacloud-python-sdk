# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ListOptimizeTasksResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        optimize_tasks: List[main_models.ListOptimizeTasksResponseBodyOptimizeTasks] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of results per page.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The list of optimization tasks.
        self.optimize_tasks = optimize_tasks
        # The request ID.
        self.request_id = request_id
        # The total count.
        self.total_count = total_count

    def validate(self):
        if self.optimize_tasks:
            for v1 in self.optimize_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['optimizeTasks'] = []
        if self.optimize_tasks is not None:
            for k1 in self.optimize_tasks:
                result['optimizeTasks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.optimize_tasks = []
        if m.get('optimizeTasks') is not None:
            for k1 in m.get('optimizeTasks'):
                temp_model = main_models.ListOptimizeTasksResponseBodyOptimizeTasks()
                self.optimize_tasks.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListOptimizeTasksResponseBodyOptimizeTasks(DaraModel):
    def __init__(
        self,
        checkpoint: Dict[str, Any] = None,
        config: Dict[str, Any] = None,
        create_time: str = None,
        next_trigger_time: str = None,
        optimize_task_name: str = None,
        region_id: str = None,
        status: str = None,
        type: str = None,
        update_time: str = None,
    ):
        # The scheduling checkpoint that stores states such as the general scheduling watermark.
        self.checkpoint = checkpoint
        # The type-specific configuration. For ExperienceMining and SkillOptimize, optional prompts support only inline Markdown, and the body is stored in inputs.prompt.content (non-empty UTF-8, up to 16 KiB).
        self.config = config
        # The creation time.
        self.create_time = create_time
        # The next scheduling trigger time.
        self.next_trigger_time = next_trigger_time
        # The name of the optimization task.
        self.optimize_task_name = optimize_task_name
        # The region ID.
        self.region_id = region_id
        # The task status.
        self.status = status
        # The type of the optimization task. Valid values: ExperienceMining, SkillOptimize, EfficiencyAnalysis, SOPGeneration, EvalMining, PolicyMining, and AssetMining.
        self.type = type
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint

        if self.config is not None:
            result['config'] = self.config

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.next_trigger_time is not None:
            result['nextTriggerTime'] = self.next_trigger_time

        if self.optimize_task_name is not None:
            result['optimizeTaskName'] = self.optimize_task_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('nextTriggerTime') is not None:
            self.next_trigger_time = m.get('nextTriggerTime')

        if m.get('optimizeTaskName') is not None:
            self.optimize_task_name = m.get('optimizeTaskName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

