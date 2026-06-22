# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HandleMaliciousFilesRequest(DaraModel):
    def __init__(
        self,
        file_id_list: List[int] = None,
        operation: str = None,
    ):
        # The list of file IDs to process.
        # > You can call [ListAgentlessMaliciousFiles](~~ListAgentlessMaliciousFiles~~) to obtain the IDs.
        # > -.
        self.file_id_list = file_id_list
        # The type of operation. Valid values:
        # - addWhitelist: adds to the whitelist.
        # - offWhitelist: removes from the whitelist.
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id_list is not None:
            result['FileIdList'] = self.file_id_list

        if self.operation is not None:
            result['Operation'] = self.operation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileIdList') is not None:
            self.file_id_list = m.get('FileIdList')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        return self

