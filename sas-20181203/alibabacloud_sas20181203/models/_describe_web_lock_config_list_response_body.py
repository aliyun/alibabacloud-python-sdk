# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeWebLockConfigListResponseBody(DaraModel):
    def __init__(
        self,
        config_list: List[main_models.DescribeWebLockConfigListResponseBodyConfigList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The configurations of web tamper proofing.
        self.config_list = config_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of directories that have web tamper proofing enabled on the server.
        self.total_count = total_count

    def validate(self):
        if self.config_list:
            for v1 in self.config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigList'] = []
        if self.config_list is not None:
            for k1 in self.config_list:
                result['ConfigList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k1 in m.get('ConfigList'):
                temp_model = main_models.DescribeWebLockConfigListResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWebLockConfigListResponseBodyConfigList(DaraModel):
    def __init__(
        self,
        defence_mode: str = None,
        dir: str = None,
        exclusive_dir: str = None,
        exclusive_file: str = None,
        exclusive_file_type: str = None,
        id: str = None,
        inclusive_file: str = None,
        inclusive_file_type: str = None,
        local_backup_dir: str = None,
        mode: str = None,
        uuid: str = None,
    ):
        # The prevention mode. Valid values:
        # 
        # *   **block**: Interception Mode
        # *   **audit**: Alert Mode
        self.defence_mode = defence_mode
        # The directory that has web tamper proofing enabled.
        self.dir = dir
        # The directory that has web tamper proofing disabled.
        # 
        # > If the value of **Mode** is **blacklist**, this parameter is returned.
        self.exclusive_dir = exclusive_dir
        # The file that has web tamper proofing disabled.
        # 
        # > If the value of **Mode** is **blacklist**, this parameter is returned.
        self.exclusive_file = exclusive_file
        # The type of the file that has web tamper proofing disabled.
        # 
        # > If the value of **Mode** is **blacklist**, this parameter is returned.
        self.exclusive_file_type = exclusive_file_type
        # The configuration ID of the protected directory.
        self.id = id
        # The file that has web tamper proofing enabled.
        # 
        # > If the value of **Mode** is **whitelist**, this parameter is returned.
        self.inclusive_file = inclusive_file
        # The type of the file that has web tamper proofing enabled.
        # 
        # > If the value of **Mode** is **whitelist**, this parameter is returned.
        self.inclusive_file_type = inclusive_file_type
        # The local path to the backup files of the protected directory.
        self.local_backup_dir = local_backup_dir
        # The protection mode of web tamper proofing. Valid values:
        # 
        # *   **whitelist**: In this mode, web tamper proofing is enabled for the specified directories and file types.
        # *   **blacklist**: In this mode, web tamper proofing is enabled for the unspecified subdirectories, file types, and files in the protected directory.
        self.mode = mode
        # The UUID of the server that has web tamper proofing enabled.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defence_mode is not None:
            result['DefenceMode'] = self.defence_mode

        if self.dir is not None:
            result['Dir'] = self.dir

        if self.exclusive_dir is not None:
            result['ExclusiveDir'] = self.exclusive_dir

        if self.exclusive_file is not None:
            result['ExclusiveFile'] = self.exclusive_file

        if self.exclusive_file_type is not None:
            result['ExclusiveFileType'] = self.exclusive_file_type

        if self.id is not None:
            result['Id'] = self.id

        if self.inclusive_file is not None:
            result['InclusiveFile'] = self.inclusive_file

        if self.inclusive_file_type is not None:
            result['InclusiveFileType'] = self.inclusive_file_type

        if self.local_backup_dir is not None:
            result['LocalBackupDir'] = self.local_backup_dir

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenceMode') is not None:
            self.defence_mode = m.get('DefenceMode')

        if m.get('Dir') is not None:
            self.dir = m.get('Dir')

        if m.get('ExclusiveDir') is not None:
            self.exclusive_dir = m.get('ExclusiveDir')

        if m.get('ExclusiveFile') is not None:
            self.exclusive_file = m.get('ExclusiveFile')

        if m.get('ExclusiveFileType') is not None:
            self.exclusive_file_type = m.get('ExclusiveFileType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InclusiveFile') is not None:
            self.inclusive_file = m.get('InclusiveFile')

        if m.get('InclusiveFileType') is not None:
            self.inclusive_file_type = m.get('InclusiveFileType')

        if m.get('LocalBackupDir') is not None:
            self.local_backup_dir = m.get('LocalBackupDir')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

