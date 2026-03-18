# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceDiagnosisResultRequest(DaraModel):
    def __init__(
        self,
        dimension: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        report_date: str = None,
        statuses: str = None,
    ):
        self.dimension = dimension
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.report_date = report_date
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.report_date is not None:
            result['ReportDate'] = self.report_date

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ReportDate') is not None:
            self.report_date = m.get('ReportDate')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

