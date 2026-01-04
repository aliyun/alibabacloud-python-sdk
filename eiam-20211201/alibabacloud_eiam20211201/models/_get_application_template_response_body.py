# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetApplicationTemplateResponseBody(DaraModel):
    def __init__(
        self,
        application_template: main_models.GetApplicationTemplateResponseBodyApplicationTemplate = None,
        request_id: str = None,
    ):
        self.application_template = application_template
        self.request_id = request_id

    def validate(self):
        if self.application_template:
            self.application_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_template is not None:
            result['ApplicationTemplate'] = self.application_template.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTemplate') is not None:
            temp_model = main_models.GetApplicationTemplateResponseBodyApplicationTemplate()
            self.application_template = temp_model.from_map(m.get('ApplicationTemplate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationTemplateResponseBodyApplicationTemplate(DaraModel):
    def __init__(
        self,
        application_template_id: str = None,
        application_template_name: str = None,
        create_time: int = None,
        description: str = None,
        help_document_url: str = None,
        logo_url: str = None,
        managed_service_code: str = None,
        sale_info: main_models.GetApplicationTemplateResponseBodyApplicationTemplateSaleInfo = None,
        service_console_url: str = None,
        service_managed: bool = None,
        sso_types: List[str] = None,
        update_time: int = None,
    ):
        # 应用模板Id
        self.application_template_id = application_template_id
        # 应用模板名称
        self.application_template_name = application_template_name
        # 应用模板创建时间
        self.create_time = create_time
        # 应用模板描述信息
        self.description = description
        # 应用模板对应帮助文档地址
        self.help_document_url = help_document_url
        # 应用模板Logo地址
        self.logo_url = logo_url
        # 托管应用模板的云产品ServiceCode。当且仅当ServiceManaged为true是返回。
        self.managed_service_code = managed_service_code
        # 应用模板售卖信息
        self.sale_info = sale_info
        # 托管应用模板的云产品控制台地址。当且仅当ServiceManaged为true是返回。
        self.service_console_url = service_console_url
        # 应用模板是否被云产品托管。
        self.service_managed = service_managed
        # 支持SSO协议
        self.sso_types = sso_types
        # 应用模板更新时间
        self.update_time = update_time

    def validate(self):
        if self.sale_info:
            self.sale_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        if self.application_template_name is not None:
            result['ApplicationTemplateName'] = self.application_template_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.help_document_url is not None:
            result['HelpDocumentUrl'] = self.help_document_url

        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url

        if self.managed_service_code is not None:
            result['ManagedServiceCode'] = self.managed_service_code

        if self.sale_info is not None:
            result['SaleInfo'] = self.sale_info.to_map()

        if self.service_console_url is not None:
            result['ServiceConsoleUrl'] = self.service_console_url

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.sso_types is not None:
            result['SsoTypes'] = self.sso_types

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        if m.get('ApplicationTemplateName') is not None:
            self.application_template_name = m.get('ApplicationTemplateName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HelpDocumentUrl') is not None:
            self.help_document_url = m.get('HelpDocumentUrl')

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

        if m.get('ManagedServiceCode') is not None:
            self.managed_service_code = m.get('ManagedServiceCode')

        if m.get('SaleInfo') is not None:
            temp_model = main_models.GetApplicationTemplateResponseBodyApplicationTemplateSaleInfo()
            self.sale_info = temp_model.from_map(m.get('SaleInfo'))

        if m.get('ServiceConsoleUrl') is not None:
            self.service_console_url = m.get('ServiceConsoleUrl')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('SsoTypes') is not None:
            self.sso_types = m.get('SsoTypes')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetApplicationTemplateResponseBodyApplicationTemplateSaleInfo(DaraModel):
    def __init__(
        self,
        always_free: bool = None,
    ):
        # 是否永久免费
        self.always_free = always_free

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.always_free is not None:
            result['AlwaysFree'] = self.always_free

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlwaysFree') is not None:
            self.always_free = m.get('AlwaysFree')

        return self

