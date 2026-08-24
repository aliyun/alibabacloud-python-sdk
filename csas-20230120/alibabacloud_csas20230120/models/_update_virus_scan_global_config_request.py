# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateVirusScanGlobalConfigRequest(DaraModel):
    def __init__(
        self,
        upload_file_max_size: int = None,
        upload_file_max_speed: int = None,
        upload_file_suffix_blacklist: List[str] = None,
        virus_file_upload: bool = None,
    ):
        # The maximum size of a single virus file that can be uploaded. Unit: KB. Valid values: 0 to 204800. A value of 0 indicates no size limit. Values from 1 to 204800 specify the actual size limit.
        self.upload_file_max_size = upload_file_max_size
        # The maximum upload rate for virus files. Unit: KB/s. Valid values: 0 to 102400. A value of 0 indicates no rate limit.
        self.upload_file_max_speed = upload_file_max_speed
        # The collection of file types that are prohibited from being uploaded. Duplicate values are not allowed. Files that match the specified types are not uploaded even if upload is enabled.
        self.upload_file_suffix_blacklist = upload_file_suffix_blacklist
        # Specifies whether user terminal devices are allowed to upload detected virus files to the cloud for further analysis. Valid values:
        # - **true**: Allowed.
        # - **false**: Not allowed.
        self.virus_file_upload = virus_file_upload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.upload_file_max_size is not None:
            result['UploadFileMaxSize'] = self.upload_file_max_size

        if self.upload_file_max_speed is not None:
            result['UploadFileMaxSpeed'] = self.upload_file_max_speed

        if self.upload_file_suffix_blacklist is not None:
            result['UploadFileSuffixBlacklist'] = self.upload_file_suffix_blacklist

        if self.virus_file_upload is not None:
            result['VirusFileUpload'] = self.virus_file_upload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UploadFileMaxSize') is not None:
            self.upload_file_max_size = m.get('UploadFileMaxSize')

        if m.get('UploadFileMaxSpeed') is not None:
            self.upload_file_max_speed = m.get('UploadFileMaxSpeed')

        if m.get('UploadFileSuffixBlacklist') is not None:
            self.upload_file_suffix_blacklist = m.get('UploadFileSuffixBlacklist')

        if m.get('VirusFileUpload') is not None:
            self.virus_file_upload = m.get('VirusFileUpload')

        return self

