# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryCardSmsTemplateReportRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        start_date: str = None,
        template_codes: List[str] = None,
    ):
        # The end of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format.
        self.end_date = end_date
        # The beginning of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format.
        self.start_date = start_date
        # The array of message templates.
        # 
        # This parameter is required.
        self.template_codes = template_codes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.template_codes is not None:
            result['TemplateCodes'] = self.template_codes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TemplateCodes') is not None:
            self.template_codes = m.get('TemplateCodes')

        return self

