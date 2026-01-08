# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccessInstanceTaskRequest(DaraModel):
    def __init__(
        self,
        access_instance_id: str = None,
        access_instance_type: str = None,
        lang: str = None,
        region_no: str = None,
        task_id: str = None,
    ):
        self.access_instance_id = access_instance_id
        self.access_instance_type = access_instance_type
        self.lang = lang
        self.region_no = region_no
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_instance_id is not None:
            result['AccessInstanceId'] = self.access_instance_id

        if self.access_instance_type is not None:
            result['AccessInstanceType'] = self.access_instance_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessInstanceId') is not None:
            self.access_instance_id = m.get('AccessInstanceId')

        if m.get('AccessInstanceType') is not None:
            self.access_instance_type = m.get('AccessInstanceType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

