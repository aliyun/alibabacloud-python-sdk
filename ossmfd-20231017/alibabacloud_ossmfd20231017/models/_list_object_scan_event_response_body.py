# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ossmfd20231017 import models as main_models
from darabonba.model import DaraModel

class ListObjectScanEventResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListObjectScanEventResponseBodyData] = None,
        page_info: main_models.ListObjectScanEventResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data = data
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListObjectScanEventResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListObjectScanEventResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListObjectScanEventResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListObjectScanEventResponseBodyData(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        details: List[main_models.ListObjectScanEventResponseBodyDataDetails] = None,
        display_sandbox_result: str = None,
        error_msg: str = None,
        event_id: int = None,
        event_name: str = None,
        file_path: str = None,
        first_time: int = None,
        has_sub_event: bool = None,
        last_time: int = None,
        md_5: str = None,
        operate_result: str = None,
        oss_key: str = None,
        remark: str = None,
        risk_level: str = None,
        sha_1: str = None,
        sha_256: str = None,
        source: str = None,
        status: int = None,
    ):
        self.bucket_name = bucket_name
        self.details = details
        self.display_sandbox_result = display_sandbox_result
        self.error_msg = error_msg
        self.event_id = event_id
        self.event_name = event_name
        self.file_path = file_path
        self.first_time = first_time
        self.has_sub_event = has_sub_event
        self.last_time = last_time
        self.md_5 = md_5
        self.operate_result = operate_result
        self.oss_key = oss_key
        self.remark = remark
        self.risk_level = risk_level
        self.sha_1 = sha_1
        self.sha_256 = sha_256
        self.source = source
        self.status = status

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.display_sandbox_result is not None:
            result['DisplaySandboxResult'] = self.display_sandbox_result

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.has_sub_event is not None:
            result['HasSubEvent'] = self.has_sub_event

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.operate_result is not None:
            result['OperateResult'] = self.operate_result

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.sha_1 is not None:
            result['Sha1'] = self.sha_1

        if self.sha_256 is not None:
            result['Sha256'] = self.sha_256

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.ListObjectScanEventResponseBodyDataDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('DisplaySandboxResult') is not None:
            self.display_sandbox_result = m.get('DisplaySandboxResult')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('HasSubEvent') is not None:
            self.has_sub_event = m.get('HasSubEvent')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('OperateResult') is not None:
            self.operate_result = m.get('OperateResult')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Sha1') is not None:
            self.sha_1 = m.get('Sha1')

        if m.get('Sha256') is not None:
            self.sha_256 = m.get('Sha256')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListObjectScanEventResponseBodyDataDetails(DaraModel):
    def __init__(
        self,
        name: str = None,
        name_display: str = None,
        type: str = None,
        value: str = None,
        value_display: str = None,
    ):
        self.name = name
        self.name_display = name_display
        self.type = type
        self.value = value
        self.value_display = value_display

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.name_display is not None:
            result['NameDisplay'] = self.name_display

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.value_display is not None:
            result['ValueDisplay'] = self.value_display

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameDisplay') is not None:
            self.name_display = m.get('NameDisplay')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueDisplay') is not None:
            self.value_display = m.get('ValueDisplay')

        return self

