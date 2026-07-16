# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListRayJobRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        submission_id: str = None,
        submit_time: main_models.ListRayJobRequestSubmitTime = None,
        task_biz_id: str = None,
    ):
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.submission_id = submission_id
        self.submit_time = submit_time
        self.task_biz_id = task_biz_id

    def validate(self):
        if self.submit_time:
            self.submit_time.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.submission_id is not None:
            result['submissionId'] = self.submission_id

        if self.submit_time is not None:
            result['submitTime'] = self.submit_time.to_map()

        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('submissionId') is not None:
            self.submission_id = m.get('submissionId')

        if m.get('submitTime') is not None:
            temp_model = main_models.ListRayJobRequestSubmitTime()
            self.submit_time = temp_model.from_map(m.get('submitTime'))

        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')

        return self

class ListRayJobRequestSubmitTime(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

