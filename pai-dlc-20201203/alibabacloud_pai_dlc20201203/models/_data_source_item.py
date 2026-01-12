# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataSourceItem(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_type: str = None,
        description: str = None,
        display_name: str = None,
        endpoint: str = None,
        file_system_id: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        mount_path: str = None,
        options: str = None,
        path: str = None,
        user_id: str = None,
    ):
        self.data_source_id = data_source_id
        self.data_source_type = data_source_type
        self.description = description
        self.display_name = display_name
        self.endpoint = endpoint
        self.file_system_id = file_system_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time
        self.mount_path = mount_path
        self.options = options
        self.path = path
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.options is not None:
            result['Options'] = self.options

        if self.path is not None:
            result['Path'] = self.path

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

