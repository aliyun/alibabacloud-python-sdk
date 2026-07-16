# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDataSourceAttributeRequest(DaraModel):
    def __init__(
        self,
        db_ids: List[str] = None,
        instance_id: str = None,
        lang: str = None,
        region_id: str = None,
    ):
        self.db_ids = db_ids
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_ids is not None:
            result['DbIds'] = self.db_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbIds') is not None:
            self.db_ids = m.get('DbIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

