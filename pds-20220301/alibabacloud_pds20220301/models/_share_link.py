# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ShareLink(DaraModel):
    def __init__(
        self,
        access_count: int = None,
        created_at: str = None,
        creator: str = None,
        description: str = None,
        disable_download: bool = None,
        disable_preview: bool = None,
        disable_save: bool = None,
        download_count: int = None,
        download_limit: int = None,
        drive_id: str = None,
        expiration: str = None,
        expired: bool = None,
        file_id_list: List[str] = None,
        office_editable: bool = None,
        preview_count: int = None,
        preview_limit: int = None,
        report_count: int = None,
        save_count: int = None,
        save_download_limit: int = None,
        save_limit: int = None,
        share_all_files: bool = None,
        share_id: str = None,
        share_name: str = None,
        share_pwd: str = None,
        status: str = None,
        updated_at: str = None,
        video_preview_count: int = None,
    ):
        # The number of times that the shared files are visited.
        self.access_count = access_count
        # The time when the share was created.
        self.created_at = created_at
        # The user who created the share.
        self.creator = creator
        # The description of the share.
        self.description = description
        # Specifies whether to disable the download feature.
        self.disable_download = disable_download
        # Specifies whether to disable the preview feature.
        self.disable_preview = disable_preview
        # Specifies whether to disable the save feature.
        self.disable_save = disable_save
        # The number of times that the shared files are downloaded.
        self.download_count = download_count
        # The limit on the number of times that the shared files can be downloaded.
        self.download_limit = download_limit
        # The drive ID.
        self.drive_id = drive_id
        # The time when the share URL expires. The value of this parameter follows the RFC 3339 standard. Example: "2020-06-28T11:33:00.000+08:00". If you set the value to "", the share URL never expires.
        self.expiration = expiration
        # Specifies whether the share is expired.
        self.expired = expired
        # The IDs of the files to share in the parent path.
        self.file_id_list = file_id_list
        self.office_editable = office_editable
        # The number of times that the shared files are previewed.
        self.preview_count = preview_count
        # The limit on the number of times that the shared files can be previewed.
        self.preview_limit = preview_limit
        # The number of times that the shared files are reported.
        self.report_count = report_count
        # The number of times that the shared files are saved.
        self.save_count = save_count
        self.save_download_limit = save_download_limit
        # The limit on the number of times that the shared files can be saved.
        self.save_limit = save_limit
        # Specifies whether to share all files in the drive.
        self.share_all_files = share_all_files
        # The share ID.
        self.share_id = share_id
        # The name of the share. By default, the file name that corresponds to the first ID in the file ID list is used.
        self.share_name = share_name
        # The access code. An access code can be up to 64 characters in length. If you do not specify a value, files can be accessed without an access code.
        self.share_pwd = share_pwd
        # The status of the share. Valid values:
        # 
        # *   disabled: The share is canceled.
        # *   enabled: The share is effective.
        self.status = status
        # The time when the share was last modified.
        self.updated_at = updated_at
        # The number of times that the shared audio and video files are played.
        self.video_preview_count = video_preview_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_count is not None:
            result['access_count'] = self.access_count

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.description is not None:
            result['description'] = self.description

        if self.disable_download is not None:
            result['disable_download'] = self.disable_download

        if self.disable_preview is not None:
            result['disable_preview'] = self.disable_preview

        if self.disable_save is not None:
            result['disable_save'] = self.disable_save

        if self.download_count is not None:
            result['download_count'] = self.download_count

        if self.download_limit is not None:
            result['download_limit'] = self.download_limit

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.expiration is not None:
            result['expiration'] = self.expiration

        if self.expired is not None:
            result['expired'] = self.expired

        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list

        if self.office_editable is not None:
            result['office_editable'] = self.office_editable

        if self.preview_count is not None:
            result['preview_count'] = self.preview_count

        if self.preview_limit is not None:
            result['preview_limit'] = self.preview_limit

        if self.report_count is not None:
            result['report_count'] = self.report_count

        if self.save_count is not None:
            result['save_count'] = self.save_count

        if self.save_download_limit is not None:
            result['save_download_limit'] = self.save_download_limit

        if self.save_limit is not None:
            result['save_limit'] = self.save_limit

        if self.share_all_files is not None:
            result['share_all_files'] = self.share_all_files

        if self.share_id is not None:
            result['share_id'] = self.share_id

        if self.share_name is not None:
            result['share_name'] = self.share_name

        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.video_preview_count is not None:
            result['video_preview_count'] = self.video_preview_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_count') is not None:
            self.access_count = m.get('access_count')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('disable_download') is not None:
            self.disable_download = m.get('disable_download')

        if m.get('disable_preview') is not None:
            self.disable_preview = m.get('disable_preview')

        if m.get('disable_save') is not None:
            self.disable_save = m.get('disable_save')

        if m.get('download_count') is not None:
            self.download_count = m.get('download_count')

        if m.get('download_limit') is not None:
            self.download_limit = m.get('download_limit')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')

        if m.get('expired') is not None:
            self.expired = m.get('expired')

        if m.get('file_id_list') is not None:
            self.file_id_list = m.get('file_id_list')

        if m.get('office_editable') is not None:
            self.office_editable = m.get('office_editable')

        if m.get('preview_count') is not None:
            self.preview_count = m.get('preview_count')

        if m.get('preview_limit') is not None:
            self.preview_limit = m.get('preview_limit')

        if m.get('report_count') is not None:
            self.report_count = m.get('report_count')

        if m.get('save_count') is not None:
            self.save_count = m.get('save_count')

        if m.get('save_download_limit') is not None:
            self.save_download_limit = m.get('save_download_limit')

        if m.get('save_limit') is not None:
            self.save_limit = m.get('save_limit')

        if m.get('share_all_files') is not None:
            self.share_all_files = m.get('share_all_files')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')

        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('video_preview_count') is not None:
            self.video_preview_count = m.get('video_preview_count')

        return self

