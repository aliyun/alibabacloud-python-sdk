# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class SmsTemplatePageListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        model: main_models.SmsTemplatePageListResponseBodyModel = None,
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
            temp_model = main_models.SmsTemplatePageListResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class SmsTemplatePageListResponseBodyModel(DaraModel):
    def __init__(
        self,
        list: List[main_models.SmsTemplatePageListResponseBodyModelList] = None,
        page_no: int = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
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
                temp_model = main_models.SmsTemplatePageListResponseBodyModelList()
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

class SmsTemplatePageListResponseBodyModelList(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        properties: str = None,
        short_url_task_id: int = None,
        sign: str = None,
        sms_type: str = None,
        status: int = None,
        template_id: int = None,
        template_name: str = None,
        template_type: int = None,
    ):
        # 短信内容
        self.content = content
        # 创建时间
        self.create_time = create_time
        # 模板所需参数
        self.properties = properties
        # 智能短链ID
        self.short_url_task_id = short_url_task_id
        # 短信签名
        self.sign = sign
        # 短信类型
        self.sms_type = sms_type
        # 模板状态
        self.status = status
        # 模板ID
        self.template_id = template_id
        # 模板名称
        self.template_name = template_name
        # 模板类型
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.short_url_task_id is not None:
            result['ShortUrlTaskId'] = self.short_url_task_id

        if self.sign is not None:
            result['Sign'] = self.sign

        if self.sms_type is not None:
            result['SmsType'] = self.sms_type

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('ShortUrlTaskId') is not None:
            self.short_url_task_id = m.get('ShortUrlTaskId')

        if m.get('Sign') is not None:
            self.sign = m.get('Sign')

        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

