# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyAdviceByIdRequest(DaraModel):
    def __init__(
        self,
        advice_date: int = None,
        advice_id: str = None,
        apply_type: str = None,
        build_immediately: bool = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # The date on which you want to apply the suggestion. Format: yyyyMMdd.
        self.advice_date = advice_date
        # The suggestion ID.
        self.advice_id = advice_id
        self.apply_type = apply_type
        self.build_immediately = build_immediately
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice_date is not None:
            result['AdviceDate'] = self.advice_date

        if self.advice_id is not None:
            result['AdviceId'] = self.advice_id

        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type

        if self.build_immediately is not None:
            result['BuildImmediately'] = self.build_immediately

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceDate') is not None:
            self.advice_date = m.get('AdviceDate')

        if m.get('AdviceId') is not None:
            self.advice_id = m.get('AdviceId')

        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')

        if m.get('BuildImmediately') is not None:
            self.build_immediately = m.get('BuildImmediately')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

