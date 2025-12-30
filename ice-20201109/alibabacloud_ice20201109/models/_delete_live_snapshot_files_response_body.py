# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class DeleteLiveSnapshotFilesResponseBody(DaraModel):
    def __init__(
        self,
        delete_file_result_list: List[main_models.DeleteLiveSnapshotFilesResponseBodyDeleteFileResultList] = None,
        request_id: str = None,
    ):
        # The list of deleted files.
        self.delete_file_result_list = delete_file_result_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.delete_file_result_list:
            for v1 in self.delete_file_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeleteFileResultList'] = []
        if self.delete_file_result_list is not None:
            for k1 in self.delete_file_result_list:
                result['DeleteFileResultList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delete_file_result_list = []
        if m.get('DeleteFileResultList') is not None:
            for k1 in m.get('DeleteFileResultList'):
                temp_model = main_models.DeleteLiveSnapshotFilesResponseBodyDeleteFileResultList()
                self.delete_file_result_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteLiveSnapshotFilesResponseBodyDeleteFileResultList(DaraModel):
    def __init__(
        self,
        create_timestamp: int = None,
        result: str = None,
    ):
        # The time when the file was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The result of deletion. A value of OK indicates that the file is deleted. Other values indicate that the file failed to be deleted.
        # 
        # Valid values:
        # 
        # *   OK: The file was deleted.
        # *   NotFound: The file was not found.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

