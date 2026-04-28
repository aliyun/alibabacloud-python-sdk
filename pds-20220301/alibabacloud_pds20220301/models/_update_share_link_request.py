# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateShareLinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        disable_download: bool = None,
        disable_preview: bool = None,
        disable_save: bool = None,
        download_count: int = None,
        download_limit: int = None,
        expiration: str = None,
        office_editable: bool = None,
        preview_count: int = None,
        preview_limit: int = None,
        report_count: int = None,
        save_count: int = None,
        save_limit: int = None,
        share_id: str = None,
        share_name: str = None,
        share_pwd: str = None,
        status: str = None,
        video_preview_count: int = None,
    ):
        # The description of the share link. The description can be up to 1,024 characters in length.
        self.description = description
        # Specifies whether to prohibit the downloads of the shared files.
        self.disable_download = disable_download
        # Specifies whether to prohibit the previews of the shared files.
        self.disable_preview = disable_preview
        # Specifies whether to prohibit the saves of the shared files.
        self.disable_save = disable_save
        # The number of times that the shared files are downloaded. The value must be greater than or equal to 0.
        self.download_count = download_count
        # The maximum number of times that the shared files can be downloaded. The value must be greater than or equal to 0. A value of 0 specifies that the number is unlimited.
        self.download_limit = download_limit
        # The time when the share link expires. The time follows the RFC 3339 standard. Example: 2020-06-28T11:33:00.000+08:00. If you leave this parameter empty, the share link never expires.
        self.expiration = expiration
        self.office_editable = office_editable
        # The number of times that the shared files are previewed. The value must be greater than or equal to 0.
        self.preview_count = preview_count
        # The maximum number of times that the shared files can be previewed. The value must be greater than or equal to 0. A value of 0 specifies that the number is unlimited.
        self.preview_limit = preview_limit
        # The number of times that the shared files are reported. The value must be greater than or equal to 0.
        self.report_count = report_count
        # The number of times that the shared files are saved. The value must be greater than or equal to 0.
        self.save_count = save_count
        # The maximum number of times that the shared files can be saved. The value must be greater than or equal to 0. A value of 0 specifies that the number is unlimited.
        self.save_limit = save_limit
        # The share ID.
        # 
        # This parameter is required.
        self.share_id = share_id
        # The name of the share link. By default, the name of the first file is used. The name can be up to 128 characters in length.
        self.share_name = share_name
        # The access code. The access code can be up to 64 characters in length. A value of 0 specifies an empty string.
        self.share_pwd = share_pwd
        # The state of the share link. Valid values:
        # 
        # *   disabled: The share link is canceled.
        # *   enabled: The share link is effective.
        self.status = status
        # The number of times that the videos are previewed in the shared files. The value must be greater than or equal to 0.
        self.video_preview_count = video_preview_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.expiration is not None:
            result['expiration'] = self.expiration

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

        if self.save_limit is not None:
            result['save_limit'] = self.save_limit

        if self.share_id is not None:
            result['share_id'] = self.share_id

        if self.share_name is not None:
            result['share_name'] = self.share_name

        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd

        if self.status is not None:
            result['status'] = self.status

        if self.video_preview_count is not None:
            result['video_preview_count'] = self.video_preview_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')

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

        if m.get('save_limit') is not None:
            self.save_limit = m.get('save_limit')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')

        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('video_preview_count') is not None:
            self.video_preview_count = m.get('video_preview_count')

        return self

