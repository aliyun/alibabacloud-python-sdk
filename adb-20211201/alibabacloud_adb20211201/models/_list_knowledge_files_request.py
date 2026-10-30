# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKnowledgeFilesRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        file_ids: str = None,
        file_location: str = None,
        page: str = None,
        page_size: str = None,
        status: str = None,
        user: str = None,
    ):
        # The ID of the ADB instance.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The JSON string of the file ID array, which contains up to 200 positive integers.
        self.file_ids = file_ids
        # The URL of the knowledge base file.
        self.file_location = file_location
        # The page number. Pages start from 1. If you do not specify this parameter, the default value is 1.
        self.page = page
        # The number of entries per page. Valid values: 1 to 100. If you do not specify this parameter, the default value is 20.
        self.page_size = page_size
        # The processing status. Valid values: PENDING, PROCESSING, COMPLETED, FAILED, DUPLICATED, and SKIPPED.
        self.status = status
        # The stable ID of the authorized user. If you do not specify this parameter, all files in the knowledge base can be queried.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.file_ids is not None:
            result['FileIds'] = self.file_ids

        if self.file_location is not None:
            result['FileLocation'] = self.file_location

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FileIds') is not None:
            self.file_ids = m.get('FileIds')

        if m.get('FileLocation') is not None:
            self.file_location = m.get('FileLocation')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

