# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListEnabledExtensionsForProjectResponseBody(DaraModel):
    def __init__(
        self,
        extensions: List[main_models.ListEnabledExtensionsForProjectResponseBodyExtensions] = None,
        request_id: str = None,
    ):
        # The extensions.
        self.extensions = extensions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.extensions:
            for v1 in self.extensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Extensions'] = []
        if self.extensions is not None:
            for k1 in self.extensions:
                result['Extensions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extensions = []
        if m.get('Extensions') is not None:
            for k1 in m.get('Extensions'):
                temp_model = main_models.ListEnabledExtensionsForProjectResponseBodyExtensions()
                self.extensions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEnabledExtensionsForProjectResponseBodyExtensions(DaraModel):
    def __init__(
        self,
        create_user: str = None,
        extension_code: str = None,
        extension_desc: str = None,
        extension_name: str = None,
        modify_user: str = None,
        owner: str = None,
        parameter_setting: str = None,
        tenant_id: int = None,
    ):
        # The creator of the extension.
        self.create_user = create_user
        # The unique code of the extension.
        self.extension_code = extension_code
        # The description of the extension.
        self.extension_desc = extension_desc
        # The name of the extension.
        self.extension_name = extension_name
        # The modifier of the extension.
        self.modify_user = modify_user
        # The owner ID.
        self.owner = owner
        # The parameter settings of the extension. For more information, see [Configure extension parameters](https://help.aliyun.com/document_detail/405354.html).
        self.parameter_setting = parameter_setting
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.extension_code is not None:
            result['ExtensionCode'] = self.extension_code

        if self.extension_desc is not None:
            result['ExtensionDesc'] = self.extension_desc

        if self.extension_name is not None:
            result['ExtensionName'] = self.extension_name

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parameter_setting is not None:
            result['ParameterSetting'] = self.parameter_setting

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('ExtensionCode') is not None:
            self.extension_code = m.get('ExtensionCode')

        if m.get('ExtensionDesc') is not None:
            self.extension_desc = m.get('ExtensionDesc')

        if m.get('ExtensionName') is not None:
            self.extension_name = m.get('ExtensionName')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParameterSetting') is not None:
            self.parameter_setting = m.get('ParameterSetting')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

