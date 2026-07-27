# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgQueryDetailsRequest(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        engine_name: str = None,
        ip: str = None,
        ip_aare: str = None,
        node_id: str = None,
        page_no: int = None,
        page_size: int = None,
        project_id: str = None,
        rows: int = None,
        rule_type: str = None,
        sens_level: str = None,
        user: str = None,
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
        # The internal IP address of the ECU.
        self.ip = ip
        # The region to which the IP address belongs. Example: China-Beijing-Beijing, or internal IP address.
        self.ip_aare = ip_aare
        # The node ID.
        self.node_id = node_id
        # The page number. Minimum value: 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The project workspace name (essentially ProjectName). Example: dsg_demo_gw.
        self.project_id = project_id
        # The minimum value of the export volume.
        self.rows = rows
        # The type of triggered sensitive rule. Example: Name.
        self.rule_type = rule_type
        # The classification level. Example: 3.
        self.sens_level = sens_level
        # The operator account. Example: dsg_test.
        self.user = user

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

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ip_aare is not None:
            result['IpAare'] = self.ip_aare

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.rows is not None:
            result['Rows'] = self.rows

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.sens_level is not None:
            result['SensLevel'] = self.sens_level

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IpAare') is not None:
            self.ip_aare = m.get('IpAare')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('SensLevel') is not None:
            self.sens_level = m.get('SensLevel')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

