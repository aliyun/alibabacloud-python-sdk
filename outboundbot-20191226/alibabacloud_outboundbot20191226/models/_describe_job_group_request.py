# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeJobGroupRequest(DaraModel):
    def __init__(
        self,
        brief_types: List[str] = None,
        instance_id: str = None,
        job_group_id: str = None,
    ):
        self.brief_types = brief_types
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.job_group_id = job_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brief_types is not None:
            result['BriefTypes'] = self.brief_types

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BriefTypes') is not None:
            self.brief_types = m.get('BriefTypes')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        return self

