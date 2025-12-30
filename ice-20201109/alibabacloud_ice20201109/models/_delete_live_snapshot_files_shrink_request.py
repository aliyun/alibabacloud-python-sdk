# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveSnapshotFilesShrinkRequest(DaraModel):
    def __init__(
        self,
        create_timestamp_list_shrink: str = None,
        delete_original_file: bool = None,
        job_id: str = None,
    ):
        # The list of timestamps when the jobs were created. The values are UNIX timestamps representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. A maximum of 200 jobs can be deleted at a time.
        # 
        # This parameter is required.
        self.create_timestamp_list_shrink = create_timestamp_list_shrink
        # Specifies whether to delete the original files at the same time. Default value: false.
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
        if self.create_timestamp_list_shrink is not None:
            result['CreateTimestampList'] = self.create_timestamp_list_shrink

        if self.delete_original_file is not None:
            result['DeleteOriginalFile'] = self.delete_original_file

        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestampList') is not None:
            self.create_timestamp_list_shrink = m.get('CreateTimestampList')

        if m.get('DeleteOriginalFile') is not None:
            self.delete_original_file = m.get('DeleteOriginalFile')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

