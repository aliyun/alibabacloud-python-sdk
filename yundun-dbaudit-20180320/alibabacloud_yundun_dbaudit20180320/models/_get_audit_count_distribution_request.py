# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAuditCountDistributionRequest(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        db_id: int = None,
        end_date: str = None,
        instance_id: str = None,
        lang: str = None,
        region_id: str = None,
    ):
        self.begin_date = begin_date
        self.db_id = db_id
        self.end_date = end_date
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
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

