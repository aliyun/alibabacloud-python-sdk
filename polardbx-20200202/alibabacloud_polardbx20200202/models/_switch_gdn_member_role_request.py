# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchGdnMemberRoleRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dst_main_connect_string: str = None,
        dst_main_port: str = None,
        is_modify_endpoint: str = None,
        region_id: str = None,
        src_main_connect_string: str = None,
        src_main_port: str = None,
        switch_mode: str = None,
        task_timeout: int = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.dst_main_connect_string = dst_main_connect_string
        self.dst_main_port = dst_main_port
        self.is_modify_endpoint = is_modify_endpoint
        # This parameter is required.
        self.region_id = region_id
        self.src_main_connect_string = src_main_connect_string
        self.src_main_port = src_main_port
        # This parameter is required.
        self.switch_mode = switch_mode
        self.task_timeout = task_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dst_main_connect_string is not None:
            result['DstMainConnectString'] = self.dst_main_connect_string

        if self.dst_main_port is not None:
            result['DstMainPort'] = self.dst_main_port

        if self.is_modify_endpoint is not None:
            result['IsModifyEndpoint'] = self.is_modify_endpoint

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.src_main_connect_string is not None:
            result['SrcMainConnectString'] = self.src_main_connect_string

        if self.src_main_port is not None:
            result['SrcMainPort'] = self.src_main_port

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        if self.task_timeout is not None:
            result['TaskTimeout'] = self.task_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DstMainConnectString') is not None:
            self.dst_main_connect_string = m.get('DstMainConnectString')

        if m.get('DstMainPort') is not None:
            self.dst_main_port = m.get('DstMainPort')

        if m.get('IsModifyEndpoint') is not None:
            self.is_modify_endpoint = m.get('IsModifyEndpoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SrcMainConnectString') is not None:
            self.src_main_connect_string = m.get('SrcMainConnectString')

        if m.get('SrcMainPort') is not None:
            self.src_main_port = m.get('SrcMainPort')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        if m.get('TaskTimeout') is not None:
            self.task_timeout = m.get('TaskTimeout')

        return self

