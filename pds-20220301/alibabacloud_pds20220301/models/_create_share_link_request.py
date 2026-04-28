# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateShareLinkRequest(DaraModel):
    def __init__(
        self,
        creatable: bool = None,
        creatable_file_id_list: List[str] = None,
        description: str = None,
        disable_download: bool = None,
        disable_preview: bool = None,
        disable_save: bool = None,
        download_limit: int = None,
        drive_id: str = None,
        expiration: str = None,
        file_id_list: List[str] = None,
        office_editable: bool = None,
        preview_limit: int = None,
        require_login: bool = None,
        save_limit: int = None,
        share_all_files: bool = None,
        share_name: str = None,
        share_pwd: str = None,
        user_id: str = None,
    ):
        self.creatable = creatable
        self.creatable_file_id_list = creatable_file_id_list
        # The description of the share. The description must be 0 to 1,024 characters in length.
        self.description = description
        # Specifies whether to disable the download feature.
        self.disable_download = disable_download
        # Specifies whether to disable the preview feature.
        self.disable_preview = disable_preview
        # Specifies whether to disable the dump feature.
        self.disable_save = disable_save
        # The limit on the number of times that the shared files can be downloaded. The value of this parameter must be equal to or greater than 0. A value of 0 indicates no limit.
        self.download_limit = download_limit
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The time when the share URL expires. The value of this parameter follows the RFC 3339 standard. Example: "2020-06-28T11:33:00.000+08:00". If expiration is set to "", the share URL never expires.
        self.expiration = expiration
        # The IDs of the files to share in the parent path. The number of files in the parent path ranges from 1 to 100. If share_all_files is set to true, this parameter does not take effect. Otherwise, you must specify this parameter.``
        self.file_id_list = file_id_list
        self.office_editable = office_editable
        # The limit on the number of times that the shared files can be previewed. The value of this parameter must be equal to or greater than 0. A value of 0 indicates no limit.
        self.preview_limit = preview_limit
        self.require_login = require_login
        # The limit on the number of times that the shared files can be dumped. The value of this parameter must be equal to or greater than 0. A value of 0 indicates no limit.
        self.save_limit = save_limit
        # Specifies whether to share all files in the drive.
        self.share_all_files = share_all_files
        # The name of the share. If you leave this parameter empty, the file name that corresponds to the first ID in the file ID list is used. The name must be 0 to 128 characters in length.
        self.share_name = share_name
        # The access code. An access code must be 0 to 64 bytes in length. If you do not specify this parameter or leave this parameter empty, the files can be accessed without an access code. In this case, you do not need to specify the share_pwd parameter when you call an operation to query the share URL. The access code can contain only visible ASCII characters.
        self.share_pwd = share_pwd
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creatable is not None:
            result['creatable'] = self.creatable

        if self.creatable_file_id_list is not None:
            result['creatable_file_id_list'] = self.creatable_file_id_list

        if self.description is not None:
            result['description'] = self.description

        if self.disable_download is not None:
            result['disable_download'] = self.disable_download

        if self.disable_preview is not None:
            result['disable_preview'] = self.disable_preview

        if self.disable_save is not None:
            result['disable_save'] = self.disable_save

        if self.download_limit is not None:
            result['download_limit'] = self.download_limit

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.expiration is not None:
            result['expiration'] = self.expiration

        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list

        if self.office_editable is not None:
            result['office_editable'] = self.office_editable

        if self.preview_limit is not None:
            result['preview_limit'] = self.preview_limit

        if self.require_login is not None:
            result['require_login'] = self.require_login

        if self.save_limit is not None:
            result['save_limit'] = self.save_limit

        if self.share_all_files is not None:
            result['share_all_files'] = self.share_all_files

        if self.share_name is not None:
            result['share_name'] = self.share_name

        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatable') is not None:
            self.creatable = m.get('creatable')

        if m.get('creatable_file_id_list') is not None:
            self.creatable_file_id_list = m.get('creatable_file_id_list')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('disable_download') is not None:
            self.disable_download = m.get('disable_download')

        if m.get('disable_preview') is not None:
            self.disable_preview = m.get('disable_preview')

        if m.get('disable_save') is not None:
            self.disable_save = m.get('disable_save')

        if m.get('download_limit') is not None:
            self.download_limit = m.get('download_limit')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')

        if m.get('file_id_list') is not None:
            self.file_id_list = m.get('file_id_list')

        if m.get('office_editable') is not None:
            self.office_editable = m.get('office_editable')

        if m.get('preview_limit') is not None:
            self.preview_limit = m.get('preview_limit')

        if m.get('require_login') is not None:
            self.require_login = m.get('require_login')

        if m.get('save_limit') is not None:
            self.save_limit = m.get('save_limit')

        if m.get('share_all_files') is not None:
            self.share_all_files = m.get('share_all_files')

        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')

        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

