# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListLivyComputeSessionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sessions: List[main_models.ListLivyComputeSessionsResponseBodySessions] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.sessions = sessions
        self.total_count = total_count

    def validate(self):
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['sessions'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.sessions = []
        if m.get('sessions') is not None:
            for k1 in m.get('sessions'):
                temp_model = main_models.ListLivyComputeSessionsResponseBodySessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListLivyComputeSessionsResponseBodySessions(DaraModel):
    def __init__(
        self,
        compute_id: str = None,
        create_time: int = None,
        cu_hours: float = None,
        end_time: int = None,
        info: str = None,
        mb_seconds: int = None,
        name: str = None,
        queue: str = None,
        session_id: str = None,
        spark_conf: str = None,
        state: str = None,
        vcore_seconds: int = None,
        web_ui: str = None,
    ):
        self.compute_id = compute_id
        self.create_time = create_time
        self.cu_hours = cu_hours
        self.end_time = end_time
        self.info = info
        self.mb_seconds = mb_seconds
        self.name = name
        self.queue = queue
        self.session_id = session_id
        self.spark_conf = spark_conf
        self.state = state
        self.vcore_seconds = vcore_seconds
        self.web_ui = web_ui

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_id is not None:
            result['computeId'] = self.compute_id

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.cu_hours is not None:
            result['cuHours'] = self.cu_hours

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.info is not None:
            result['info'] = self.info

        if self.mb_seconds is not None:
            result['mbSeconds'] = self.mb_seconds

        if self.name is not None:
            result['name'] = self.name

        if self.queue is not None:
            result['queue'] = self.queue

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.spark_conf is not None:
            result['sparkConf'] = self.spark_conf

        if self.state is not None:
            result['state'] = self.state

        if self.vcore_seconds is not None:
            result['vcoreSeconds'] = self.vcore_seconds

        if self.web_ui is not None:
            result['webUI'] = self.web_ui

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeId') is not None:
            self.compute_id = m.get('computeId')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('cuHours') is not None:
            self.cu_hours = m.get('cuHours')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('info') is not None:
            self.info = m.get('info')

        if m.get('mbSeconds') is not None:
            self.mb_seconds = m.get('mbSeconds')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('queue') is not None:
            self.queue = m.get('queue')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sparkConf') is not None:
            self.spark_conf = m.get('sparkConf')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('vcoreSeconds') is not None:
            self.vcore_seconds = m.get('vcoreSeconds')

        if m.get('webUI') is not None:
            self.web_ui = m.get('webUI')

        return self

