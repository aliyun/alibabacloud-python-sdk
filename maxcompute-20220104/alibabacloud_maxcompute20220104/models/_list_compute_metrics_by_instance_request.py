# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListComputeMetricsByInstanceRequest(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        instance_id: str = None,
        job_owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_names: List[str] = None,
        region: str = None,
        signature: str = None,
        spec_codes: List[str] = None,
        start_date: int = None,
        types: List[str] = None,
    ):
        self.end_date = end_date
        self.instance_id = instance_id
        self.job_owner = job_owner
        self.page_number = page_number
        self.page_size = page_size
        self.project_names = project_names
        self.region = region
        self.signature = signature
        self.spec_codes = spec_codes
        self.start_date = start_date
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.project_names is not None:
            result['projectNames'] = self.project_names

        if self.region is not None:
            result['region'] = self.region

        if self.signature is not None:
            result['signature'] = self.signature

        if self.spec_codes is not None:
            result['specCodes'] = self.spec_codes

        if self.start_date is not None:
            result['startDate'] = self.start_date

        if self.types is not None:
            result['types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('projectNames') is not None:
            self.project_names = m.get('projectNames')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        if m.get('specCodes') is not None:
            self.spec_codes = m.get('specCodes')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        if m.get('types') is not None:
            self.types = m.get('types')

        return self

