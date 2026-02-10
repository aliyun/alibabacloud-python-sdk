# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSnapshotsRequest(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        current_page: int = None,
        is_ali_yun_ecs: str = None,
        machine_region: str = None,
        machine_remark: str = None,
        next_token: str = None,
        page_size: int = None,
        status_list: str = None,
        uuid: str = None,
    ):
        # The version of the anti-ransomware policy. Valid values:
        # 
        # *   **1.0.0**
        # *   **2.0.0**
        # 
        # This parameter is required.
        self.api_version = api_version
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # Specifies whether the server is an Elastic Compute Service (ECS) instance. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.is_ali_yun_ecs = is_ali_yun_ecs
        # The region in which the server resides.
        # 
        # >  If the Uuid parameter is not specified, this parameter is required.
        self.machine_region = machine_region
        # The name or IP address of the server.
        self.machine_remark = machine_remark
        # The starting position of the query. If this parameter is left empty, the query starts from the beginning.
        # 
        # >  If you call the operation for the first time, you do not need to specify the parameter. The response to the first call contains the token that can be used for the second call. Each subsequent response contains the token that can be used for the next call.
        self.next_token = next_token
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The status of backup snapshots from which data can be restored. Valid values:
        # 
        # *   **COMPLETE**: complete
        # *   **PARTIAL_COMPLETE**: partial complete
        self.status_list = status_list
        # The UUID of the server.
        # 
        # >  You can call the [DescribeBackupPolicy](~~DescribeBackupPolicy~~) operation to query the UUIDs of servers.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.is_ali_yun_ecs is not None:
            result['IsAliYunEcs'] = self.is_ali_yun_ecs

        if self.machine_region is not None:
            result['MachineRegion'] = self.machine_region

        if self.machine_remark is not None:
            result['MachineRemark'] = self.machine_remark

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IsAliYunEcs') is not None:
            self.is_ali_yun_ecs = m.get('IsAliYunEcs')

        if m.get('MachineRegion') is not None:
            self.machine_region = m.get('MachineRegion')

        if m.get('MachineRemark') is not None:
            self.machine_remark = m.get('MachineRemark')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

