# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyCloudDrivePermissionRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        download_end_user_ids: List[str] = None,
        download_upload_end_user_ids: List[str] = None,
        no_download_no_upload_end_user_ids: List[str] = None,
        region_id: str = None,
    ):
        # The ID of the cloud disk in Cloud Drive Service.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The IDs of the users who have the download permissions.
        self.download_end_user_ids = download_end_user_ids
        # The IDs of the users who have the upload and download permissions.
        self.download_upload_end_user_ids = download_upload_end_user_ids
        self.no_download_no_upload_end_user_ids = no_download_no_upload_end_user_ids
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.download_end_user_ids is not None:
            result['DownloadEndUserIds'] = self.download_end_user_ids

        if self.download_upload_end_user_ids is not None:
            result['DownloadUploadEndUserIds'] = self.download_upload_end_user_ids

        if self.no_download_no_upload_end_user_ids is not None:
            result['NoDownloadNoUploadEndUserIds'] = self.no_download_no_upload_end_user_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('DownloadEndUserIds') is not None:
            self.download_end_user_ids = m.get('DownloadEndUserIds')

        if m.get('DownloadUploadEndUserIds') is not None:
            self.download_upload_end_user_ids = m.get('DownloadUploadEndUserIds')

        if m.get('NoDownloadNoUploadEndUserIds') is not None:
            self.no_download_no_upload_end_user_ids = m.get('NoDownloadNoUploadEndUserIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

