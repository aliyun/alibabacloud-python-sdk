# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class AttachInstancesResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.AttachInstancesResponseBodyList] = None,
        task_id: str = None,
    ):
        # The details of the added nodes.
        self.list = list
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['task_id'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.AttachInstancesResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        return self

class AttachInstancesResponseBodyList(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
    ):
        # The code that indicates the task result.
        self.code = code
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # Indicates whether the ECS instance is successfully added to the ACK cluster.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

