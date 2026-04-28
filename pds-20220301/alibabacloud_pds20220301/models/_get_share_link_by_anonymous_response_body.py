# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetShareLinkByAnonymousResponseBody(DaraModel):
    def __init__(
        self,
        access_count: int = None,
        avatar: str = None,
        creator_id: str = None,
        creator_name: str = None,
        creator_phone: str = None,
        disable_download: bool = None,
        disable_preview: bool = None,
        disable_save: bool = None,
        download_count: int = None,
        download_limit: int = None,
        expiration: str = None,
        has_pwd: bool = None,
        preview_count: int = None,
        preview_limit: int = None,
        report_count: int = None,
        save_count: int = None,
        save_download_limit: int = None,
        save_limit: int = None,
        share_name: str = None,
        updated_at: str = None,
        video_preview_count: int = None,
    ):
        # The number of times that the shared files are visited.
        self.access_count = access_count
        # The profile picture of the user who created the share link.
        self.avatar = avatar
        # The ID of the user who created the share link.
        self.creator_id = creator_id
        # The name of the user who created the share link. The value is masked.
        self.creator_name = creator_name
        # The mobile number of the user who created the share link. The value is masked.
        self.creator_phone = creator_phone
        # Indicates whether the downloads of the shared files are prohibited.
        self.disable_download = disable_download
        # Indicates whether the previews of the shared files are prohibited.
        self.disable_preview = disable_preview
        # Indicates whether the saves of the shared files are prohibited.
        self.disable_save = disable_save
        # The number of times that the shared files are downloaded.
        self.download_count = download_count
        # The maximum number of times that the shared files can be downloaded.
        self.download_limit = download_limit
        # The time when the share link expires.
        self.expiration = expiration
        # Indicates whether a password is specified for the share link.
        self.has_pwd = has_pwd
        # The number of times that the shared files are previewed.
        self.preview_count = preview_count
        # The maximum number of times that the shared files can be previewed.
        self.preview_limit = preview_limit
        # The number of times that the shared files are reported.
        self.report_count = report_count
        # The number of times that the shared files are saved.
        self.save_count = save_count
        # The maximum number of times that the shared files can be saved and downloaded.
        self.save_download_limit = save_download_limit
        # The maximum number of times that the shared files can be saved.
        self.save_limit = save_limit
        # The name of the share link.
        self.share_name = share_name
        # The time when the share link was last modified.
        self.updated_at = updated_at
        # The number of times that the videos are previewed in the shared files.
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

        if self.avatar is not None:
            result['avatar'] = self.avatar

        if self.creator_id is not None:
            result['creator_id'] = self.creator_id

        if self.creator_name is not None:
            result['creator_name'] = self.creator_name

        if self.creator_phone is not None:
            result['creator_phone'] = self.creator_phone

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

        if self.has_pwd is not None:
            result['has_pwd'] = self.has_pwd

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

        if self.share_name is not None:
            result['share_name'] = self.share_name

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.video_preview_count is not None:
            result['video_preview_count'] = self.video_preview_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_count') is not None:
            self.access_count = m.get('access_count')

        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')

        if m.get('creator_id') is not None:
            self.creator_id = m.get('creator_id')

        if m.get('creator_name') is not None:
            self.creator_name = m.get('creator_name')

        if m.get('creator_phone') is not None:
            self.creator_phone = m.get('creator_phone')

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

        if m.get('has_pwd') is not None:
            self.has_pwd = m.get('has_pwd')

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

        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('video_preview_count') is not None:
            self.video_preview_count = m.get('video_preview_count')

        return self

