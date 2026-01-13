# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCalculationJobsRequest(DaraModel):
    def __init__(
        self,
        abmetric_ids: str = None,
        end_date: str = None,
        instance_id: str = None,
        start_date: str = None,
    ):
        # This parameter is required.
        self.abmetric_ids = abmetric_ids
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abmetric_ids is not None:
            result['ABMetricIds'] = self.abmetric_ids

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricIds') is not None:
            self.abmetric_ids = m.get('ABMetricIds')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

