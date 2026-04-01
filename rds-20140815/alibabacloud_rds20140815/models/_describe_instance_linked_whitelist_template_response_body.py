# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceLinkedWhitelistTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeInstanceLinkedWhitelistTemplateResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code returned. Valid values:
        # 
        # *   **200**: success
        # *   **400**: client error
        # *   **401**: identity authentication failed
        # *   **404**: request page not found
        # *   **500**: server error
        self.code = code
        # The data returned.
        self.data = data
        # The HTTP status code returned. Valid values:
        # 
        # *   **200**: success
        # *   **400**: client error
        # *   **500**: server error
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.DescribeInstanceLinkedWhitelistTemplateResponseBodyData()
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

class DescribeInstanceLinkedWhitelistTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        ins_name: str = None,
        templates: List[main_models.DescribeInstanceLinkedWhitelistTemplateResponseBodyDataTemplates] = None,
    ):
        # The instance name.
        self.ins_name = ins_name
        # The information about whitelists that are returned by page.
        self.templates = templates

    def validate(self):
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ins_name is not None:
            result['InsName'] = self.ins_name

        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')

        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.DescribeInstanceLinkedWhitelistTemplateResponseBodyDataTemplates()
                self.templates.append(temp_model.from_map(k1))

        return self

class DescribeInstanceLinkedWhitelistTemplateResponseBodyDataTemplates(DaraModel):
    def __init__(
        self,
        id: int = None,
        ips: str = None,
        template_id: int = None,
        template_name: str = None,
        user_id: int = None,
    ):
        # The primary key of the data table.
        self.id = id
        # The IP addresses.
        self.ips = ips
        # The whitelist template ID.
        self.template_id = template_id
        # The whitelist template name.
        self.template_name = template_name
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.ips is not None:
            result['Ips'] = self.ips

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ips') is not None:
            self.ips = m.get('Ips')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

