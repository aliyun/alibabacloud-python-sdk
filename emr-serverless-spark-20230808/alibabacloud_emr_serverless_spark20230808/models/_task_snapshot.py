# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class TaskSnapshot(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        commiter: int = None,
        gmt_created: str = None,
        item: main_models.Task = None,
        message: str = None,
        task_biz_id: str = None,
        version: str = None,
    ):
        self.biz_id = biz_id
        self.commiter = commiter
        self.gmt_created = gmt_created
        self.item = item
        self.message = message
        self.task_biz_id = task_biz_id
        self.version = version

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.commiter is not None:
            result['commiter'] = self.commiter

        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created

        if self.item is not None:
            result['item'] = self.item.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('commiter') is not None:
            self.commiter = m.get('commiter')

        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')

        if m.get('item') is not None:
            temp_model = main_models.Task()
            self.item = temp_model.from_map(m.get('item'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

