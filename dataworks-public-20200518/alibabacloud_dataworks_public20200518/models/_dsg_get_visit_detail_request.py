# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgGetVisitDetailRequest(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        engine_name: str = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        project_id: str = None,
        rule_name: str = None,
        sens_level: str = None,
    ):
        # The start time of the query range. Example: "2026-06-26 00:00:00".
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The end time of the query range. Example: "2026-06-30 23:59:59".
        # 
        # This parameter is required.
        self.end_time = end_time
        # The engine type. Valid values:
        # - ODPS.ODPS
        # - EMR
        # - HOLO.POSTGRES
        # 
        # This parameter is required.
        self.engine_name = engine_name
        # The keyword of the table or project name. DataWorks supports fuzzy match. You can enter a keyword to query table or project names that contain the keyword.
        self.keyword = keyword
        # The page number. Minimum value: 1.
        self.page_no = page_no
        # The page size.
        self.page_size = page_size
        # The project name (ProjectName is easier to understand). Example: dsg_demo_gw.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The name of the sensitive field.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The sensitivity level. Example: 3.
        self.sens_level = sens_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine_name is not None:
            result['EngineName'] = self.engine_name

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sens_level is not None:
            result['SensLevel'] = self.sens_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SensLevel') is not None:
            self.sens_level = m.get('SensLevel')

        return self

