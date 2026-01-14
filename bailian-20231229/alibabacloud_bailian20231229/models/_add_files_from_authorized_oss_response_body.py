# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class AddFilesFromAuthorizedOssResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AddFilesFromAuthorizedOssResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AddFilesFromAuthorizedOssResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AddFilesFromAuthorizedOssResponseBodyData(DaraModel):
    def __init__(
        self,
        add_file_result_list: List[main_models.AddFilesFromAuthorizedOssResponseBodyDataAddFileResultList] = None,
    ):
        self.add_file_result_list = add_file_result_list

    def validate(self):
        if self.add_file_result_list:
            for v1 in self.add_file_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddFileResultList'] = []
        if self.add_file_result_list is not None:
            for k1 in self.add_file_result_list:
                result['AddFileResultList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_file_result_list = []
        if m.get('AddFileResultList') is not None:
            for k1 in m.get('AddFileResultList'):
                temp_model = main_models.AddFilesFromAuthorizedOssResponseBodyDataAddFileResultList()
                self.add_file_result_list.append(temp_model.from_map(k1))

        return self

class AddFilesFromAuthorizedOssResponseBodyDataAddFileResultList(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        msg: str = None,
        oss_key: str = None,
        status: str = None,
    ):
        self.file_id = file_id
        self.msg = msg
        self.oss_key = oss_key
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

