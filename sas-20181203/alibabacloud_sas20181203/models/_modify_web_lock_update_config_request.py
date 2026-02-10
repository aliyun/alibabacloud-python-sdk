# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebLockUpdateConfigRequest(DaraModel):
    def __init__(
        self,
        defence_mode: str = None,
        dir: str = None,
        exclusive_dir: str = None,
        exclusive_file: str = None,
        exclusive_file_type: str = None,
        id: int = None,
        inclusive_file: str = None,
        inclusive_file_type: str = None,
        lang: str = None,
        local_backup_dir: str = None,
        mode: str = None,
        source_ip: str = None,
        uuid: str = None,
    ):
        # The prevention mode. Valid values:
        # 
        # *   **block**: Interception Mode
        # *   **audit**: Alert Mode
        # 
        # This parameter is required.
        self.defence_mode = defence_mode
        # The directory for which you want to enable web tamper proofing.
        # 
        # This parameter is required.
        self.dir = dir
        # The directory for which you want to disable web tamper proofing.
        # 
        # > If you set **Mode** to **blacklist**, you must specify this parameter.
        self.exclusive_dir = exclusive_dir
        # The file for which you want to disable web tamper proofing.
        # 
        # > If you set **Mode** to **blacklist**, you must specify this parameter.
        self.exclusive_file = exclusive_file
        # The type of the file for which you want to disable web tamper proofing. Separate multiple types with semicolons (;). Valid values:
        # 
        # *   php
        # *   jsp
        # *   asp
        # *   aspx
        # *   js
        # *   cgi
        # *   html
        # *   htm
        # *   xml
        # *   shtml
        # *   shtm
        # *   jpg
        # *   gif
        # *   png
        # 
        # > If you set **Mode** to **blacklist**, you must specify this parameter.
        self.exclusive_file_type = exclusive_file_type
        # The ID of the protected directory for which you want to change the status of web tamper proofing.
        # 
        # > You can call the [DescribeWebLockConfigList](~~DescribeWebLockConfigList~~) operation to query the IDs of protected directories.
        # 
        # This parameter is required.
        self.id = id
        # The file for which you want to enable web tamper proofing.
        # 
        # > If you set **Mode** to **whitelist**, you must specify this parameter.
        self.inclusive_file = inclusive_file
        # The type of the file for which you want to enable web tamper proofing. Separate multiple types with semicolons (;). Valid values:
        # 
        # *   php
        # *   jsp
        # *   asp
        # *   aspx
        # *   js
        # *   cgi
        # *   html
        # *   htm
        # *   xml
        # *   shtml
        # *   shtm
        # *   jpg
        # *   gif
        # *   png
        # 
        # > If you set **Mode** to **whitelist**, you must specify this parameter.
        self.inclusive_file_type = inclusive_file_type
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The local path to the backup files of the protected directory.\\
        # The directory format of a Linux server is different from that of a Windows server. You must enter the directory in the required format based on your operating system. Examples:
        # 
        # *   Linux server: /usr/local/aegis/bak
        # *   Windows server: C:\\Program Files (x86)\\Alibaba\\Aegis\\bak
        # 
        # This parameter is required.
        self.local_backup_dir = local_backup_dir
        # The protection mode of web tamper proofing. Valid values:
        # 
        # *   **whitelist**: In this mode, web tamper proofing is enabled for the specified directories and file types.
        # *   **blacklist**: In this mode, web tamper proofing is enabled for the unspecified subdirectories, file types, and files in the protected directory.
        self.mode = mode
        # The source IP address of the request.
        self.source_ip = source_ip
        # The UUID of the server on which the protected directory is located.
        # 
        # > You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
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

        if self.id is not None:
            result['Id'] = self.id

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

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

