# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CdsFileShareLinkModel(DaraModel):
    def __init__(
        self,
        access_count: int = None,
        create_time: str = None,
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
        file_ids: str = None,
        modifiy_time: str = None,
        preview_count: int = None,
        preview_limit: int = None,
        report_count: int = None,
        save_count: int = None,
        save_limit: int = None,
        share_id: str = None,
        share_link: str = None,
        share_name: str = None,
        share_pwd: str = None,
        status: str = None,
        video_preview_count: int = None,
    ):
        self.access_count = access_count
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.disable_download = disable_download
        self.disable_preview = disable_preview
        self.disable_save = disable_save
        self.download_count = download_count
        self.download_limit = download_limit
        self.drive_id = drive_id
        self.expiration = expiration
        self.expired = expired
        self.file_ids = file_ids
        self.modifiy_time = modifiy_time
        self.preview_count = preview_count
        self.preview_limit = preview_limit
        self.report_count = report_count
        self.save_count = save_count
        self.save_limit = save_limit
        self.share_id = share_id
        self.share_link = share_link
        self.share_name = share_name
        self.share_pwd = share_pwd
        self.status = status
        self.video_preview_count = video_preview_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_count is not None:
            result['AccessCount'] = self.access_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.disable_download is not None:
            result['DisableDownload'] = self.disable_download

        if self.disable_preview is not None:
            result['DisablePreview'] = self.disable_preview

        if self.disable_save is not None:
            result['DisableSave'] = self.disable_save

        if self.download_count is not None:
            result['DownloadCount'] = self.download_count

        if self.download_limit is not None:
            result['DownloadLimit'] = self.download_limit

        if self.drive_id is not None:
            result['DriveId'] = self.drive_id

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.file_ids is not None:
            result['FileIds'] = self.file_ids

        if self.modifiy_time is not None:
            result['ModifiyTime'] = self.modifiy_time

        if self.preview_count is not None:
            result['PreviewCount'] = self.preview_count

        if self.preview_limit is not None:
            result['PreviewLimit'] = self.preview_limit

        if self.report_count is not None:
            result['ReportCount'] = self.report_count

        if self.save_count is not None:
            result['SaveCount'] = self.save_count

        if self.save_limit is not None:
            result['SaveLimit'] = self.save_limit

        if self.share_id is not None:
            result['ShareId'] = self.share_id

        if self.share_link is not None:
            result['ShareLink'] = self.share_link

        if self.share_name is not None:
            result['ShareName'] = self.share_name

        if self.share_pwd is not None:
            result['SharePwd'] = self.share_pwd

        if self.status is not None:
            result['Status'] = self.status

        if self.video_preview_count is not None:
            result['VideoPreviewCount'] = self.video_preview_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessCount') is not None:
            self.access_count = m.get('AccessCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisableDownload') is not None:
            self.disable_download = m.get('DisableDownload')

        if m.get('DisablePreview') is not None:
            self.disable_preview = m.get('DisablePreview')

        if m.get('DisableSave') is not None:
            self.disable_save = m.get('DisableSave')

        if m.get('DownloadCount') is not None:
            self.download_count = m.get('DownloadCount')

        if m.get('DownloadLimit') is not None:
            self.download_limit = m.get('DownloadLimit')

        if m.get('DriveId') is not None:
            self.drive_id = m.get('DriveId')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('FileIds') is not None:
            self.file_ids = m.get('FileIds')

        if m.get('ModifiyTime') is not None:
            self.modifiy_time = m.get('ModifiyTime')

        if m.get('PreviewCount') is not None:
            self.preview_count = m.get('PreviewCount')

        if m.get('PreviewLimit') is not None:
            self.preview_limit = m.get('PreviewLimit')

        if m.get('ReportCount') is not None:
            self.report_count = m.get('ReportCount')

        if m.get('SaveCount') is not None:
            self.save_count = m.get('SaveCount')

        if m.get('SaveLimit') is not None:
            self.save_limit = m.get('SaveLimit')

        if m.get('ShareId') is not None:
            self.share_id = m.get('ShareId')

        if m.get('ShareLink') is not None:
            self.share_link = m.get('ShareLink')

        if m.get('ShareName') is not None:
            self.share_name = m.get('ShareName')

        if m.get('SharePwd') is not None:
            self.share_pwd = m.get('SharePwd')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VideoPreviewCount') is not None:
            self.video_preview_count = m.get('VideoPreviewCount')

        return self

