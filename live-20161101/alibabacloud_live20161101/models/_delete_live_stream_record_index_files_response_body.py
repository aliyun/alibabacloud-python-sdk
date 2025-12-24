# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DeleteLiveStreamRecordIndexFilesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        record_delete_info_list: main_models.DeleteLiveStreamRecordIndexFilesResponseBodyRecordDeleteInfoList = None,
        request_id: str = None,
    ):
        # The status code. A return value of 500 indicates an error. For details, see the Error codes section of this topic.
        self.code = code
        # The status description. A return value of 500 indicates an error. For details, see the Error codes section of this topic.
        self.message = message
        # The deletion information.
        self.record_delete_info_list = record_delete_info_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.record_delete_info_list:
            self.record_delete_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.record_delete_info_list is not None:
            result['RecordDeleteInfoList'] = self.record_delete_info_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RecordDeleteInfoList') is not None:
            temp_model = main_models.DeleteLiveStreamRecordIndexFilesResponseBodyRecordDeleteInfoList()
            self.record_delete_info_list = temp_model.from_map(m.get('RecordDeleteInfoList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteLiveStreamRecordIndexFilesResponseBodyRecordDeleteInfoList(DaraModel):
    def __init__(
        self,
        record_delete_info: List[main_models.DeleteLiveStreamRecordIndexFilesResponseBodyRecordDeleteInfoListRecordDeleteInfo] = None,
    ):
        self.record_delete_info = record_delete_info

    def validate(self):
        if self.record_delete_info:
            for v1 in self.record_delete_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordDeleteInfo'] = []
        if self.record_delete_info is not None:
            for k1 in self.record_delete_info:
                result['RecordDeleteInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_delete_info = []
        if m.get('RecordDeleteInfo') is not None:
            for k1 in m.get('RecordDeleteInfo'):
                temp_model = main_models.DeleteLiveStreamRecordIndexFilesResponseBodyRecordDeleteInfoListRecordDeleteInfo()
                self.record_delete_info.append(temp_model.from_map(k1))

        return self

class DeleteLiveStreamRecordIndexFilesResponseBodyRecordDeleteInfoListRecordDeleteInfo(DaraModel):
    def __init__(
        self,
        message: str = None,
        record_id: str = None,
    ):
        # The processing result of each file indicated by the file ID. Valid values:
        # 
        # *   **OK**: The file has been deleted.
        # *   **AccessDenied**: Access to the file has been denied.
        # *   **FileNotFound**: The file fails to be found.
        self.message = message
        # The ID of the index file that is used to locate the live stream recording files to be deleted.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        return self

