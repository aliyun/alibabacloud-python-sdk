# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetRumExceptionStackResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRumExceptionStackResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The responses code. The status code 200 indicates that the request was successful.
        self.code = code
        # The response message.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message returned if the request failed.
        self.message = message
        # Id of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`
        # *   `false`
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetRumExceptionStackResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRumExceptionStackResponseBodyData(DaraModel):
    def __init__(
        self,
        binary_images: str = None,
        crash_address: str = None,
        crash_reason: str = None,
        lines: List[str] = None,
        module_name: str = None,
        thread_id: str = None,
        thread_info_list: List[main_models.GetRumExceptionStackResponseBodyDataThreadInfoList] = None,
        uuid: str = None,
    ):
        # The name and UUID of the symbol table required for parsing the exception stack. This parameter is exposed during the parsing of PC errors.
        self.binary_images = binary_images
        # The crash address. This parameter is exposed during the parsing of PC errors.
        self.crash_address = crash_address
        # The cause of the exception. This parameter is exposed during the parsing of PC errors.
        self.crash_reason = crash_reason
        # The list of stacks.
        self.lines = lines
        # The name of the crash parsing module. This parameter is exposed during the parsing of PC errors.
        self.module_name = module_name
        # The thread ID.
        self.thread_id = thread_id
        # The thread stack information captured during PC crashes.
        self.thread_info_list = thread_info_list
        # The UUID of the symbol table required for parsing the stack. This parameter is exposed during the parsing of PC errors.
        self.uuid = uuid

    def validate(self):
        if self.thread_info_list:
            for v1 in self.thread_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binary_images is not None:
            result['BinaryImages'] = self.binary_images

        if self.crash_address is not None:
            result['CrashAddress'] = self.crash_address

        if self.crash_reason is not None:
            result['CrashReason'] = self.crash_reason

        if self.lines is not None:
            result['Lines'] = self.lines

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.thread_id is not None:
            result['ThreadId'] = self.thread_id

        result['ThreadInfoList'] = []
        if self.thread_info_list is not None:
            for k1 in self.thread_info_list:
                result['ThreadInfoList'].append(k1.to_map() if k1 else None)

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BinaryImages') is not None:
            self.binary_images = m.get('BinaryImages')

        if m.get('CrashAddress') is not None:
            self.crash_address = m.get('CrashAddress')

        if m.get('CrashReason') is not None:
            self.crash_reason = m.get('CrashReason')

        if m.get('Lines') is not None:
            self.lines = m.get('Lines')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('ThreadId') is not None:
            self.thread_id = m.get('ThreadId')

        self.thread_info_list = []
        if m.get('ThreadInfoList') is not None:
            for k1 in m.get('ThreadInfoList'):
                temp_model = main_models.GetRumExceptionStackResponseBodyDataThreadInfoList()
                self.thread_info_list.append(temp_model.from_map(k1))

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class GetRumExceptionStackResponseBodyDataThreadInfoList(DaraModel):
    def __init__(
        self,
        thread_detail: str = None,
        thread_tag: str = None,
    ):
        # Thread stack details.
        self.thread_detail = thread_detail
        # The thread tag, including the thread number and name.
        self.thread_tag = thread_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.thread_detail is not None:
            result['ThreadDetail'] = self.thread_detail

        if self.thread_tag is not None:
            result['ThreadTag'] = self.thread_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThreadDetail') is not None:
            self.thread_detail = m.get('ThreadDetail')

        if m.get('ThreadTag') is not None:
            self.thread_tag = m.get('ThreadTag')

        return self

