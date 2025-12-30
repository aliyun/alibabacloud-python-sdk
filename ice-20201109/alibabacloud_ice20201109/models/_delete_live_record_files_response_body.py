# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class DeleteLiveRecordFilesResponseBody(DaraModel):
    def __init__(
        self,
        delete_file_info_list: List[main_models.DeleteLiveRecordFilesResponseBodyDeleteFileInfoList] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The list of files deleted.
        self.delete_file_info_list = delete_file_info_list
        # The description of the state returned.
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.delete_file_info_list:
            for v1 in self.delete_file_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeleteFileInfoList'] = []
        if self.delete_file_info_list is not None:
            for k1 in self.delete_file_info_list:
                result['DeleteFileInfoList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delete_file_info_list = []
        if m.get('DeleteFileInfoList') is not None:
            for k1 in m.get('DeleteFileInfoList'):
                temp_model = main_models.DeleteLiveRecordFilesResponseBodyDeleteFileInfoList()
                self.delete_file_info_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteLiveRecordFilesResponseBodyDeleteFileInfoList(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        record_id: str = None,
    ):
        # The code that identifies the result of the deletion.
        self.code = code
        # The result of deletion.
        self.message = message
        # The ID of the deleted recording file.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        return self

