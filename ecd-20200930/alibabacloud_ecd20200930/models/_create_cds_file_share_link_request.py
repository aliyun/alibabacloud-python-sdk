# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateCdsFileShareLinkRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        description: str = None,
        disable_download: bool = None,
        disable_preview: bool = None,
        disable_save: bool = None,
        download_limit: int = None,
        end_user_id: str = None,
        expiration: str = None,
        file_ids: List[str] = None,
        group_id: str = None,
        preview_limit: int = None,
        save_limit: int = None,
        share_name: str = None,
        share_pwd: str = None,
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
        # *   true
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     prohibits file download
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     allows file download
        # 
        #     <!-- -->
        # 
        #     .
        self.disable_download = disable_download
        # Specifies whether to prohibit the preview of the files that are being shared.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     prohibits file preview
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     allows file preview
        # 
        #     <!-- -->
        # 
        #     .
        self.disable_preview = disable_preview
        # Specifies whether to prohibit the dump of the files that are being shared.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     prohibits file dump
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     allows file dump
        # 
        #     <!-- -->
        # 
        #     .
        self.disable_save = disable_save
        # The limit on the number of times that the shared files can be downloaded. The value of this parameter must be equal to or greater than 0. The value 0 specifies that no limit is imposed on the number of times that the shared files can be downloaded.
        self.download_limit = download_limit
        # The ID of the end user.
        self.end_user_id = end_user_id
        # The time when the file sharing link expires. The value of this parameter follows the RFC 3339 standard. Example: "2020-06-28T11:33:00.000+08:00". If this parameter is set to "", the file sharing link never expires.
        self.expiration = expiration
        # The file IDs.
        self.file_ids = file_ids
        self.group_id = group_id
        # The limit on the number of times that the shared files can be previewed. The value of this parameter must be equal to or greater than 0. The value 0 specifies that no limit is imposed on the number of times that the shared files can be previewed.
        self.preview_limit = preview_limit
        # The limit on the number of times that the shared files can be dumped. The value of this parameter must be equal to or greater than 0. The value 0 specifies that no limit is imposed on the number of times that the shared files can be dumped.
        self.save_limit = save_limit
        # The name of the file sharing task. If you leave this parameter empty, the file name that corresponds to the first ID in the file ID list is used. The name must be 0 to 128 characters in length.
        self.share_name = share_name
        # The length of the access code. Valid values: 6 to 8. Unit: bytes. If you leave this parameter empty or set it to null, no access code is required. If you use a token to share files, you do not need to configure this parameter. The access code can contain only visible ASCII characters.
        self.share_pwd = share_pwd

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

        if self.download_limit is not None:
            result['DownloadLimit'] = self.download_limit

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.file_ids is not None:
            result['FileIds'] = self.file_ids

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.preview_limit is not None:
            result['PreviewLimit'] = self.preview_limit

        if self.save_limit is not None:
            result['SaveLimit'] = self.save_limit

        if self.share_name is not None:
            result['ShareName'] = self.share_name

        if self.share_pwd is not None:
            result['SharePwd'] = self.share_pwd

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

        if m.get('DownloadLimit') is not None:
            self.download_limit = m.get('DownloadLimit')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('FileIds') is not None:
            self.file_ids = m.get('FileIds')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('PreviewLimit') is not None:
            self.preview_limit = m.get('PreviewLimit')

        if m.get('SaveLimit') is not None:
            self.save_limit = m.get('SaveLimit')

        if m.get('ShareName') is not None:
            self.share_name = m.get('ShareName')

        if m.get('SharePwd') is not None:
            self.share_pwd = m.get('SharePwd')

        return self

