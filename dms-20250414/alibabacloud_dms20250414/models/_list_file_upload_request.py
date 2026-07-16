# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFileUploadRequest(DaraModel):
    def __init__(
        self,
        call_from: str = None,
        dms_unit: str = None,
        download_link_expire: int = None,
        file_category: str = None,
        file_from: str = None,
        file_id: str = None,
        session_id: str = None,
        sort_column: str = None,
        sort_direction: str = None,
    ):
        # For front-end use only.
        self.call_from = call_from
        # The current DMS unit.
        self.dms_unit = dms_unit
        # The validity period of the download link, in seconds. This parameter applies only to files in user-owned Object Storage Service (OSS) buckets. The default is 3600.
        # 
        # - Minimum value: 3600 (1 hour)
        # 
        # - Maximum value: 129600 (36 hours)
        # 
        # Notes:
        # 
        # - Download links for files in the built-in OSS are valid for 1 hour.
        # 
        # -
        self.download_link_expire = download_link_expire
        # The file category.
        self.file_category = file_category
        # The file source.
        self.file_from = file_from
        # The file ID.
        self.file_id = file_id
        # The session ID.
        self.session_id = session_id
        # The sort column.
        self.sort_column = sort_column
        # The sort direction.
        self.sort_direction = sort_direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_from is not None:
            result['CallFrom'] = self.call_from

        if self.dms_unit is not None:
            result['DmsUnit'] = self.dms_unit

        if self.download_link_expire is not None:
            result['DownloadLinkExpire'] = self.download_link_expire

        if self.file_category is not None:
            result['FileCategory'] = self.file_category

        if self.file_from is not None:
            result['FileFrom'] = self.file_from

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column

        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallFrom') is not None:
            self.call_from = m.get('CallFrom')

        if m.get('DmsUnit') is not None:
            self.dms_unit = m.get('DmsUnit')

        if m.get('DownloadLinkExpire') is not None:
            self.download_link_expire = m.get('DownloadLinkExpire')

        if m.get('FileCategory') is not None:
            self.file_category = m.get('FileCategory')

        if m.get('FileFrom') is not None:
            self.file_from = m.get('FileFrom')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')

        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')

        return self

