# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCdsFileShareLinkRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        description: str = None,
        disable_download: bool = None,
        disable_preview: bool = None,
        disable_save: bool = None,
        download_count: int = None,
        download_limit: int = None,
        expiration: str = None,
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
        # The ID of the cloud disk.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The description of the file sharing task. The description must be 0 to 1,024 characters in length.
        self.description = description
        # Specifies whether to prohibit the download of the files that are being shared.
        # 
        # Valid values:
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.disable_download = disable_download
        # Specifies whether to prohibit the preview of the files that are being shared.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.disable_preview = disable_preview
        # Specifies whether to prohibit the dump of the files that are being shared.
        # 
        # Valid values:
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.disable_save = disable_save
        # The number of times that the shared files are downloaded. The value of this parameter must be equal to or greater than 0.
        self.download_count = download_count
        # The limit on the number of times that the shared files can be downloaded. The value of this parameter must be equal to or greater than 0. The value 0 specifies that no limit is imposed on the number of times that the shared files can be downloaded.
        self.download_limit = download_limit
        # The time when the file sharing link expires. The value of this parameter follows the RFC 3339 standard. Example: "2020-06-28T11:33:00.000+08:00". If this parameter is set to "", the file sharing link never expires.
        self.expiration = expiration
        # The number of times that the shared files are previewed. The value of this parameter must be equal to or greater than 0.
        self.preview_count = preview_count
        # The limit on the number of times that the shared files can be previewed. The value of this parameter must be equal to or greater than 0. The value 0 specifies that no limit is imposed on the number of times that the shared files can be downloaded.
        self.preview_limit = preview_limit
        # The number of times that the shared files are reported. The value of this parameter must be equal to or greater than 0.
        self.report_count = report_count
        # The number of times that the shared files are dumped. The value of this parameter must be equal to or greater than 0.
        self.save_count = save_count
        # The limit on the number of times that the shared files can be dumped. The value of this parameter must be equal to or greater than 0. The value 0 specifies that no limit is imposed on the number of times that the shared files can be downloaded.
        self.save_limit = save_limit
        # The ID of the file sharing task.
        # 
        # This parameter is required.
        self.share_id = share_id
        # The name of the file sharing task. If you do not configure this parameter, the sharing task name is the first ID that is returned in the file_id_list value.
        # 
        # >  The sharing task name must be 0 to 128 characters in length.
        self.share_name = share_name
        # The length of the access code. Valid values: 6 to 8. Unit: bytes. If you leave this parameter empty or set it to null, no access code is required. If you use a token to share files, you do not need to configure this parameter. The access code can contain only visible ASCII characters.
        self.share_pwd = share_pwd
        # The sharing status.
        # 
        # Valid values:
        # 
        # *   disabled: The sharing task is canceled.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   enabled: The sharing task is valid.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # The number of times that the videos are previewed in the shared files. The value of this parameter must be equal to or greater than 0.
        self.video_preview_count = video_preview_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

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

        if self.expiration is not None:
            result['Expiration'] = self.expiration

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
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

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

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

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

        if m.get('ShareName') is not None:
            self.share_name = m.get('ShareName')

        if m.get('SharePwd') is not None:
            self.share_pwd = m.get('SharePwd')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VideoPreviewCount') is not None:
            self.video_preview_count = m.get('VideoPreviewCount')

        return self

