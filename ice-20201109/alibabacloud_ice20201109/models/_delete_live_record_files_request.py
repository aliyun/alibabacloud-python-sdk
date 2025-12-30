# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteLiveRecordFilesRequest(DaraModel):
    def __init__(
        self,
        record_ids: List[str] = None,
        remove_file: bool = None,
    ):
        # The collection of IDs of recording files.
        # 
        # This parameter is required.
        self.record_ids = record_ids
        # Specifies whether to delete the original files in OSS.
        self.remove_file = remove_file

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_ids is not None:
            result['RecordIds'] = self.record_ids

        if self.remove_file is not None:
            result['RemoveFile'] = self.remove_file

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordIds') is not None:
            self.record_ids = m.get('RecordIds')

        if m.get('RemoveFile') is not None:
            self.remove_file = m.get('RemoveFile')

        return self

