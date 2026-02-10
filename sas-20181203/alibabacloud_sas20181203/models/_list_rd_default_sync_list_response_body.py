# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListRdDefaultSyncListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListRdDefaultSyncListResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned if the call is successful.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListRdDefaultSyncListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRdDefaultSyncListResponseBodyData(DaraModel):
    def __init__(
        self,
        folder_ids: str = None,
    ):
        # The IDs of the folders in the resource directory.
        self.folder_ids = folder_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_ids is not None:
            result['FolderIds'] = self.folder_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderIds') is not None:
            self.folder_ids = m.get('FolderIds')

        return self

