# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class TaskInstance(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        creator: int = None,
        fenix_run_id: str = None,
        gmt_created: str = None,
        task_biz_id: str = None,
        task_info: main_models.Task = None,
        task_status: str = None,
        workspace_biz_id: str = None,
    ):
        self.biz_id = biz_id
        self.creator = creator
        self.fenix_run_id = fenix_run_id
        self.gmt_created = gmt_created
        self.task_biz_id = task_biz_id
        self.task_info = task_info
        self.task_status = task_status
        self.workspace_biz_id = workspace_biz_id

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.creator is not None:
            result['creator'] = self.creator

        if self.fenix_run_id is not None:
            result['fenixRunId'] = self.fenix_run_id

        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created

        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id

        if self.task_info is not None:
            result['taskInfo'] = self.task_info.to_map()

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        if self.workspace_biz_id is not None:
            result['workspaceBizId'] = self.workspace_biz_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('fenixRunId') is not None:
            self.fenix_run_id = m.get('fenixRunId')

        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')

        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')

        if m.get('taskInfo') is not None:
            temp_model = main_models.Task()
            self.task_info = temp_model.from_map(m.get('taskInfo'))

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        if m.get('workspaceBizId') is not None:
            self.workspace_biz_id = m.get('workspaceBizId')

        return self

