# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgGetVisitStatRequest(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        engine_name: str = None,
        node_id: str = None,
        page_no: int = None,
        page_size: int = None,
        project_id: str = None,
        rule_name: str = None,
        sens_level: str = None,
    ):
        # The start time in the format of "2026-06-30 03:59:59".
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The end time in the format of "2026-06-30 23:59:59".
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
        # The node ID. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to query the node ID.
        self.node_id = node_id
        # The page number. Minimum value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The name of the project space. Example value: dsg_demo_gw.
        self.project_id = project_id
        # The name of the sensitive field.
        self.rule_name = rule_name
        # The classification level. Example value: 3.
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

        if self.node_id is not None:
            result['NodeId'] = self.node_id

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

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

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

