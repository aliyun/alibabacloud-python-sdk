# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebLockCreateConfigRequest(DaraModel):
    def __init__(
        self,
        defence_mode: str = None,
        dir: str = None,
        exclusive_dir: str = None,
        exclusive_file: str = None,
        exclusive_file_type: str = None,
        inclusive_file: str = None,
        inclusive_file_type: str = None,
        lang: str = None,
        local_backup_dir: str = None,
        mode: str = None,
        source_ip: str = None,
        uuid: str = None,
    ):
        # The defense mode. Valid values:
        # 
        # - **block**: Blocks requests.
        # - **audit**: Generates alerts.
        # 
        # This parameter is required.
        self.defence_mode = defence_mode
        # The protected directory.
        # 
        # This parameter is required.
        self.dir = dir
        # The directory that does not require web tamper-proofing (excluded directory).
        # > If the defense pattern **Mode** is set to **blacklist**, you must configure this parameter.
        self.exclusive_dir = exclusive_dir
        # The files that do not require web tamper-proofing (excluded files).
        # > If the defense pattern **Mode** is set to **blacklist**, you must configure this parameter.
        self.exclusive_file = exclusive_file
        # The file types that do not require web tamper-proofing (excluded file types). Separate multiple file types with a semicolon. Valid values:
        # - php
        # - jsp
        # - asp
        # - aspx
        # - js
        # - cgi
        # - html
        # - htm
        # - xml
        # - shtml
        # - shtm
        # - jpg
        # - gif
        # - png
        # 
        # > If the defense pattern **Mode** is set to **blacklist**, you must configure this parameter.
        self.exclusive_file_type = exclusive_file_type
        # The files that require protection.
        # > If the defense pattern **Mode** is set to **whitelist**, you must configure this parameter.
        self.inclusive_file = inclusive_file
        # The file types that require web tamper-proofing. Separate multiple file types with a semicolon. Valid values:
        # - php
        # - jsp
        # - asp
        # - aspx
        # - js
        # - cgi
        # - html
        # - htm
        # - xml
        # - shtml
        # - shtm
        # - jpg
        # - gif
        # - png
        # 
        # > If the defense pattern **Mode** is set to **whitelist**, you must configure this parameter.
        self.inclusive_file_type = inclusive_file_type
        # The language of the request and response. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The local backup path used for the secure backup of the protected directory.
        # 
        # This parameter is required.
        self.local_backup_dir = local_backup_dir
        # The protection mode of the directory. Valid values:
        # - **whitelist**: Whitelist mode. Protects the added protected directories and file types.
        # - **blacklist**: Blacklist mode. Protects all subdirectories, file types, and specified files under the added protected directory that are not excluded.
        self.mode = mode
        # The source IP address.
        self.source_ip = source_ip
        # The UUID of the server for which you want to add a protected directory.
        # > You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to obtain the UUID of the server.
        # 
        # This parameter is required.
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

        if self.inclusive_file is not None:
            result['InclusiveFile'] = self.inclusive_file

        if self.inclusive_file_type is not None:
            result['InclusiveFileType'] = self.inclusive_file_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.local_backup_dir is not None:
            result['LocalBackupDir'] = self.local_backup_dir

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

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

        if m.get('InclusiveFile') is not None:
            self.inclusive_file = m.get('InclusiveFile')

        if m.get('InclusiveFileType') is not None:
            self.inclusive_file_type = m.get('InclusiveFileType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LocalBackupDir') is not None:
            self.local_backup_dir = m.get('LocalBackupDir')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

