# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class SearchSampleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: List[main_models.SearchSampleResponseBodyResultObject] = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.SearchSampleResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class SearchSampleResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_size: int = None,
        remark: str = None,
        row_count: int = None,
        sample_id: int = None,
        sample_name: str = None,
        tab: str = None,
        upload_time: str = None,
        upload_user_name: str = None,
    ):
        self.file_name = file_name
        self.file_size = file_size
        self.remark = remark
        self.row_count = row_count
        self.sample_id = sample_id
        self.sample_name = sample_name
        self.tab = tab
        self.upload_time = upload_time
        self.upload_user_name = upload_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        if self.sample_id is not None:
            result['SampleId'] = self.sample_id

        if self.sample_name is not None:
            result['SampleName'] = self.sample_name

        if self.tab is not None:
            result['Tab'] = self.tab

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        if self.upload_user_name is not None:
            result['UploadUserName'] = self.upload_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        if m.get('SampleId') is not None:
            self.sample_id = m.get('SampleId')

        if m.get('SampleName') is not None:
            self.sample_name = m.get('SampleName')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        if m.get('UploadUserName') is not None:
            self.upload_user_name = m.get('UploadUserName')

        return self

