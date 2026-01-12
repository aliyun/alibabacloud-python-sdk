# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SmartCache(DaraModel):
    def __init__(
        self,
        cache_worker_num: int = None,
        cache_worker_size: int = None,
        description: str = None,
        display_name: str = None,
        duration: str = None,
        endpoint: str = None,
        file_system_id: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
        mount_path: str = None,
        options: str = None,
        path: str = None,
        smart_cache_id: str = None,
        status: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.cache_worker_num = cache_worker_num
        self.cache_worker_size = cache_worker_size
        self.description = description
        self.display_name = display_name
        self.duration = duration
        self.endpoint = endpoint
        self.file_system_id = file_system_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time
        self.mount_path = mount_path
        self.options = options
        self.path = path
        self.smart_cache_id = smart_cache_id
        self.status = status
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_worker_num is not None:
            result['CacheWorkerNum'] = self.cache_worker_num

        if self.cache_worker_size is not None:
            result['CacheWorkerSize'] = self.cache_worker_size

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.duration is not None:
            result['Duration'] = self.duration

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

        if self.smart_cache_id is not None:
            result['SmartCacheId'] = self.smart_cache_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheWorkerNum') is not None:
            self.cache_worker_num = m.get('CacheWorkerNum')

        if m.get('CacheWorkerSize') is not None:
            self.cache_worker_size = m.get('CacheWorkerSize')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

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

        if m.get('SmartCacheId') is not None:
            self.smart_cache_id = m.get('SmartCacheId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

