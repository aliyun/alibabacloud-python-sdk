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
        # - **block**: Block mode.
        # - **audit**: Alert mode.
        # 
        # This parameter is required.
        self.defence_mode = defence_mode
        # The protected directory.
        # 
        # This parameter is required.
        self.dir = dir
        # The folder to exclude from web tamper proofing protection.
        # > This parameter is required when the Defense mode **Mode** is set to **blacklist** pattern.
        self.exclusive_dir = exclusive_dir
        # The file to exclude from web tamper proofing protection.
        # > This parameter is required when the Defense mode **Mode** is set to **blacklist** pattern.
        self.exclusive_file = exclusive_file
        # The file types to exclude from web tamper proofing protection. Separate multiple file types with semicolons (;). Valid values:
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
        # > This parameter is required when the Defense mode **Mode** is set to **blacklist** pattern.
        self.exclusive_file_type = exclusive_file_type
        # The file to protect.
        # > This parameter is required when the Defense mode **Mode** is set to **whitelist** pattern.
        self.inclusive_file = inclusive_file
        # The file types to protect with web tamper proofing. Separate multiple file types with semicolons (;). Valid values:
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
        # > This parameter is required when the Defense mode **Mode** is set to **whitelist** pattern.
        self.inclusive_file_type = inclusive_file_type
        # The language type of the request and response. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The local backup path used for secure backup of the protected directory.
        # 
        # This parameter is required.
        self.local_backup_dir = local_backup_dir
        # The protection directory mode. Valid values:
        # - **whitelist**: whitelist mode. Protects only the specified directories and file types.
        # - **blacklist**: blacklist mode. Protects all subdirectories, file types, and specified files under the protected directory that are not excluded.
        self.mode = mode
        # The IP address of the access source.
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

