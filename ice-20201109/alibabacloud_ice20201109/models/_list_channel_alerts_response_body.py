# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListChannelAlertsResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        program_alerts: List[main_models.ListChannelAlertsResponseBodyProgramAlerts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The alerts.
        self.program_alerts = program_alerts
        # **Request ID**
        self.request_id = request_id
        # The total number of alerts returned.
        self.total_count = total_count

    def validate(self):
        if self.program_alerts:
            for v1 in self.program_alerts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ProgramAlerts'] = []
        if self.program_alerts is not None:
            for k1 in self.program_alerts:
                result['ProgramAlerts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.program_alerts = []
        if m.get('ProgramAlerts') is not None:
            for k1 in m.get('ProgramAlerts'):
                temp_model = main_models.ListChannelAlertsResponseBodyProgramAlerts()
                self.program_alerts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListChannelAlertsResponseBodyProgramAlerts(DaraModel):
    def __init__(
        self,
        arn: str = None,
        category: str = None,
        count: int = None,
        gmt_modified: str = None,
        program_name: str = None,
    ):
        # The ARN of the program.
        self.arn = arn
        # The alert type.
        self.category = category
        # The number of alerts.
        self.count = count
        # The time when the alert was last modified in UTC.
        self.gmt_modified = gmt_modified
        # The name of the program.
        self.program_name = program_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.category is not None:
            result['Category'] = self.category

        if self.count is not None:
            result['Count'] = self.count

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.program_name is not None:
            result['ProgramName'] = self.program_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ProgramName') is not None:
            self.program_name = m.get('ProgramName')

        return self

