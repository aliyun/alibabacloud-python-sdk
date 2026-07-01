# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteLiveSnapshotFilesRequest(DaraModel):
    def __init__(
        self,
        create_timestamp_list: List[int] = None,
        delete_original_file: bool = None,
        job_id: str = None,
    ):
        # A list of creation timestamps for the files to delete. You can specify up to 200 timestamps per request.
        # 
        # This parameter is required.
        self.create_timestamp_list = create_timestamp_list
        # Specifies whether to delete the original OSS files. The default value is false.
        self.delete_original_file = delete_original_file
        # The ID of the snapshot job.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_timestamp_list is not None:
            result['CreateTimestampList'] = self.create_timestamp_list

        if self.delete_original_file is not None:
            result['DeleteOriginalFile'] = self.delete_original_file

        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestampList') is not None:
            self.create_timestamp_list = m.get('CreateTimestampList')

        if m.get('DeleteOriginalFile') is not None:
            self.delete_original_file = m.get('DeleteOriginalFile')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

