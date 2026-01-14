# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class DetailsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        model: main_models.DetailsResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
        timestamp: int = None,
    ):
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success
        self.timestamp = timestamp

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.DetailsResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class DetailsResponseBodyModel(DaraModel):
    def __init__(
        self,
        list: List[main_models.DetailsResponseBodyModelList] = None,
        page_no: int = None,
        page_size: int = None,
        total_count: int = None,
        total_page: float = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.DetailsResponseBodyModelList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DetailsResponseBodyModelList(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        call_desc: str = None,
        call_id: str = None,
        call_status: int = None,
        call_type: int = None,
        import_time: str = None,
        intercept_reason: str = None,
        number: str = None,
        number_desc: str = None,
        number_md5: str = None,
        number_status: int = None,
        tag: str = None,
        task_id: int = None,
    ):
        # 批次号
        self.batch_id = batch_id
        # 呼叫状态描述
        self.call_desc = call_desc
        # 外呼ID
        self.call_id = call_id
        # 呼叫状态
        self.call_status = call_status
        # 外呼类型
        self.call_type = call_type
        # 导入时间
        self.import_time = import_time
        # 拦截原因
        self.intercept_reason = intercept_reason
        # 外呼号码
        self.number = number
        # 号码状态描述
        self.number_desc = number_desc
        # 外呼号码MD5
        self.number_md5 = number_md5
        # 号码状态
        self.number_status = number_status
        # 用户自定义标签
        self.tag = tag
        # 任务ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.call_desc is not None:
            result['CallDesc'] = self.call_desc

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_status is not None:
            result['CallStatus'] = self.call_status

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.import_time is not None:
            result['ImportTime'] = self.import_time

        if self.intercept_reason is not None:
            result['InterceptReason'] = self.intercept_reason

        if self.number is not None:
            result['Number'] = self.number

        if self.number_desc is not None:
            result['NumberDesc'] = self.number_desc

        if self.number_md5 is not None:
            result['NumberMD5'] = self.number_md5

        if self.number_status is not None:
            result['NumberStatus'] = self.number_status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('CallDesc') is not None:
            self.call_desc = m.get('CallDesc')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('ImportTime') is not None:
            self.import_time = m.get('ImportTime')

        if m.get('InterceptReason') is not None:
            self.intercept_reason = m.get('InterceptReason')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('NumberDesc') is not None:
            self.number_desc = m.get('NumberDesc')

        if m.get('NumberMD5') is not None:
            self.number_md5 = m.get('NumberMD5')

        if m.get('NumberStatus') is not None:
            self.number_status = m.get('NumberStatus')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

