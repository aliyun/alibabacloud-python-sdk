# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebLockStartRequest(DaraModel):
    def __init__(
        self,
        defence_mode: str = None,
        dir: str = None,
        exclusive_dir: str = None,
        exclusive_file: str = None,
        exclusive_file_type: str = None,
        inclusive_file_type: str = None,
        local_backup_dir: str = None,
        mode: str = None,
        uuid: str = None,
    ):
        # The defense mode. Valid values:
        # 
        # - **block**: block
        # - **audit**: alert.
        # 
        # This parameter is required.
        self.defence_mode = defence_mode
        # The protection directories. Separate multiple directories with commas (,).
        # 
        # This parameter is required.
        self.dir = dir
        # The folder that does not require web tamper proofing protection (excluded folder).
        # > This parameter is required when the Defense mode **Mode** is set to the **blacklist** pattern.
        self.exclusive_dir = exclusive_dir
        # The files that do not require web tamper proofing protection (excluded files).
        # > This parameter is required when the Defense mode **Mode** is set to the **blacklist** pattern.
        self.exclusive_file = exclusive_file
        # The file types that do not require web tamper proofing protection (excluded file types). Separate multiple file types with commas (,). Valid values:
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
        # > This parameter is required when the Defense mode **Mode** is set to the **blacklist** pattern.
        self.exclusive_file_type = exclusive_file_type
        # The file types that require web tamper proofing protection. Separate multiple file types with commas (,). Valid values:
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
        # > This parameter is required when the Defense mode **Mode** is set to the **whitelist** pattern.
        self.inclusive_file_type = inclusive_file_type
        # The local backup path used to back up the protection directories. The format of the protection directory path may differ between Linux servers and Windows servers. Make sure that you enter the path in the correct format. The following examples show the directory formats:
        #  - Linux server: /usr/local/aegis/bak
        #  - Windows server: C:\\Program Files (x86)\\Alibaba\\Aegis\\bak.
        # 
        # This parameter is required.
        self.local_backup_dir = local_backup_dir
        # The protection type. Valid values:
        # - **whitelist**: whitelist mode. Protects the specified protection directories and file types.
        # - **blacklist**: blacklist mode. Protects all subdirectories, file types, and specified files in the protection directories that are not excluded.
        # 
        # This parameter is required.
        self.mode = mode
        # The UUID of the server that you want to protect.
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

        if m.get('InclusiveFileType') is not None:
            self.inclusive_file_type = m.get('InclusiveFileType')

        if m.get('LocalBackupDir') is not None:
            self.local_backup_dir = m.get('LocalBackupDir')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

