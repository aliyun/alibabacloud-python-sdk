# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExcuteNumRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        degree: str = None,
        end_date: str = None,
        lang: str = None,
        source_ip: str = None,
        start_date: str = None,
    ):
        # Service code.
        # 
        # This parameter is required.
        self.code = code
        # This field is currently unused and has no query significance.
        self.degree = degree
        # End date, format yyyy-MM-dd, e.g., 2025-03-13.
        self.end_date = end_date
        # Set the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Request source IP address.
        self.source_ip = source_ip
        # Start date, format yyyy-MM-dd, e.g., 2025-03-10.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.degree is not None:
            result['Degree'] = self.degree

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Degree') is not None:
            self.degree = m.get('Degree')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

