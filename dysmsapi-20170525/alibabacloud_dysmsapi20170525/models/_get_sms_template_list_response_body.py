# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetSmsTemplateListResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetSmsTemplateListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetSmsTemplateListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSmsTemplateListResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.GetSmsTemplateListResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetSmsTemplateListResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetSmsTemplateListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        gmt_create: str = None,
        sign_name: str = None,
        template_code: str = None,
        template_name: str = None,
        template_tag: List[main_models.GetSmsTemplateListResponseBodyDataListTemplateTag] = None,
        template_type: int = None,
        usable_state_list: List[str] = None,
        work_order_id: str = None,
    ):
        # 模板审核状态
        self.audit_status = audit_status
        # 创建时间
        self.gmt_create = gmt_create
        # 签名
        self.sign_name = sign_name
        # 模板code
        self.template_code = template_code
        # 模板名称
        self.template_name = template_name
        # 模板标签
        self.template_tag = template_tag
        # 模板类型
        self.template_type = template_type
        # 模板可用状态
        self.usable_state_list = usable_state_list
        # 工单号
        self.work_order_id = work_order_id

    def validate(self):
        if self.template_tag:
            for v1 in self.template_tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        result['TemplateTag'] = []
        if self.template_tag is not None:
            for k1 in self.template_tag:
                result['TemplateTag'].append(k1.to_map() if k1 else None)

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.usable_state_list is not None:
            result['UsableStateList'] = self.usable_state_list

        if self.work_order_id is not None:
            result['WorkOrderId'] = self.work_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        self.template_tag = []
        if m.get('TemplateTag') is not None:
            for k1 in m.get('TemplateTag'):
                temp_model = main_models.GetSmsTemplateListResponseBodyDataListTemplateTag()
                self.template_tag.append(temp_model.from_map(k1))

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('UsableStateList') is not None:
            self.usable_state_list = m.get('UsableStateList')

        if m.get('WorkOrderId') is not None:
            self.work_order_id = m.get('WorkOrderId')

        return self

class GetSmsTemplateListResponseBodyDataListTemplateTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

