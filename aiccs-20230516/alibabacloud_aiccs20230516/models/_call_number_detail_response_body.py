# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class CallNumberDetailResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        message: str = None,
        model: main_models.CallNumberDetailResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
        timestamp: int = None,
    ):
        self.access_denied_detail = access_denied_detail
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.CallNumberDetailResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class CallNumberDetailResponseBodyModel(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        bill: int = None,
        call_id: str = None,
        call_type: int = None,
        id: int = None,
        intent_tag: str = None,
        keywords: str = None,
        number: str = None,
        number_md_5: str = None,
        personality_tag: str = None,
        status_code: int = None,
        tag: str = None,
        task_id: int = None,
        template_id: int = None,
        transfer_status: int = None,
    ):
        # 导入号码时返回的批次号
        self.batch_id = batch_id
        # 通话时长，单位为毫秒，实际计费需向上取整转换为秒
        self.bill = bill
        # 每次呼叫的唯一标识
        self.call_id = call_id
        # 可选项 1-AI外呼，6-语音通知
        self.call_type = call_type
        # 号码编号
        self.id = id
        # 意向标签
        self.intent_tag = intent_tag
        # 回复关键词
        self.keywords = keywords
        # 外呼号码
        self.number = number
        # 外呼号码MD5
        self.number_md_5 = number_md_5
        # 个性标签
        self.personality_tag = personality_tag
        # 外呼状态编码
        self.status_code = status_code
        # 用户自定义标签
        self.tag = tag
        # 任务ID
        self.task_id = task_id
        # 外呼使用的模板ID
        self.template_id = template_id
        # 转人工状态 0-未触发,
        self.transfer_status = transfer_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.bill is not None:
            result['Bill'] = self.bill

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.id is not None:
            result['Id'] = self.id

        if self.intent_tag is not None:
            result['IntentTag'] = self.intent_tag

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.number is not None:
            result['Number'] = self.number

        if self.number_md_5 is not None:
            result['NumberMd5'] = self.number_md_5

        if self.personality_tag is not None:
            result['PersonalityTag'] = self.personality_tag

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.transfer_status is not None:
            result['TransferStatus'] = self.transfer_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('Bill') is not None:
            self.bill = m.get('Bill')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IntentTag') is not None:
            self.intent_tag = m.get('IntentTag')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('NumberMd5') is not None:
            self.number_md_5 = m.get('NumberMd5')

        if m.get('PersonalityTag') is not None:
            self.personality_tag = m.get('PersonalityTag')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TransferStatus') is not None:
            self.transfer_status = m.get('TransferStatus')

        return self

