# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ListPipelinesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        pipelines: List[main_models.ListPipelinesResponseBodyPipelines] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.pipelines = pipelines
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.pipelines:
            for v1 in self.pipelines:
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

        result['pipelines'] = []
        if self.pipelines is not None:
            for k1 in self.pipelines:
                result['pipelines'].append(k1.to_map() if k1 else None)

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

        self.pipelines = []
        if m.get('pipelines') is not None:
            for k1 in m.get('pipelines'):
                temp_model = main_models.ListPipelinesResponseBodyPipelines()
                self.pipelines.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListPipelinesResponseBodyPipelines(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        execute_policy: main_models.ListPipelinesResponseBodyPipelinesExecutePolicy = None,
        pipeline_name: str = None,
        region_id: str = None,
        schedule_status: str = None,
        schedule_type: str = None,
        update_time: str = None,
        workspace: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.description = description
        self.execute_policy = execute_policy
        self.pipeline_name = pipeline_name
        self.region_id = region_id
        self.schedule_status = schedule_status
        self.schedule_type = schedule_type
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time
        self.workspace = workspace

    def validate(self):
        if self.execute_policy:
            self.execute_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.execute_policy is not None:
            result['executePolicy'] = self.execute_policy.to_map()

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.schedule_status is not None:
            result['scheduleStatus'] = self.schedule_status

        if self.schedule_type is not None:
            result['scheduleType'] = self.schedule_type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executePolicy') is not None:
            temp_model = main_models.ListPipelinesResponseBodyPipelinesExecutePolicy()
            self.execute_policy = temp_model.from_map(m.get('executePolicy'))

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('scheduleStatus') is not None:
            self.schedule_status = m.get('scheduleStatus')

        if m.get('scheduleType') is not None:
            self.schedule_type = m.get('scheduleType')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class ListPipelinesResponseBodyPipelinesExecutePolicy(DaraModel):
    def __init__(
        self,
        mode: str = None,
        run_once: main_models.ListPipelinesResponseBodyPipelinesExecutePolicyRunOnce = None,
        scheduled: main_models.ListPipelinesResponseBodyPipelinesExecutePolicyScheduled = None,
    ):
        self.mode = mode
        self.run_once = run_once
        self.scheduled = scheduled

    def validate(self):
        if self.run_once:
            self.run_once.validate()
        if self.scheduled:
            self.scheduled.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['mode'] = self.mode

        if self.run_once is not None:
            result['runOnce'] = self.run_once.to_map()

        if self.scheduled is not None:
            result['scheduled'] = self.scheduled.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('runOnce') is not None:
            temp_model = main_models.ListPipelinesResponseBodyPipelinesExecutePolicyRunOnce()
            self.run_once = temp_model.from_map(m.get('runOnce'))

        if m.get('scheduled') is not None:
            temp_model = main_models.ListPipelinesResponseBodyPipelinesExecutePolicyScheduled()
            self.scheduled = temp_model.from_map(m.get('scheduled'))

        return self

class ListPipelinesResponseBodyPipelinesExecutePolicyScheduled(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        interval: str = None,
    ):
        self.from_time = from_time
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.interval is not None:
            result['interval'] = self.interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('interval') is not None:
            self.interval = m.get('interval')

        return self

class ListPipelinesResponseBodyPipelinesExecutePolicyRunOnce(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        to_time: int = None,
    ):
        self.from_time = from_time
        self.to_time = to_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.to_time is not None:
            result['toTime'] = self.to_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        return self

