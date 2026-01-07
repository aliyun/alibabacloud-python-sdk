# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_accountcenter20241209 import models as main_models
from darabonba.model import DaraModel

class EnterpriseRegisterAccountResponseBody(DaraModel):
    def __init__(
        self,
        account_info: main_models.EnterpriseRegisterAccountResponseBodyAccountInfo = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.account_info = account_info
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.account_info:
            self.account_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_info is not None:
            result['AccountInfo'] = self.account_info.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountInfo') is not None:
            temp_model = main_models.EnterpriseRegisterAccountResponseBodyAccountInfo()
            self.account_info = temp_model.from_map(m.get('AccountInfo'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EnterpriseRegisterAccountResponseBodyAccountInfo(DaraModel):
    def __init__(
        self,
        enterprise_license_no: str = None,
        enterprise_name: str = None,
        login_id: str = None,
        pk: str = None,
    ):
        self.enterprise_license_no = enterprise_license_no
        self.enterprise_name = enterprise_name
        self.login_id = login_id
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enterprise_license_no is not None:
            result['EnterpriseLicenseNo'] = self.enterprise_license_no

        if self.enterprise_name is not None:
            result['EnterpriseName'] = self.enterprise_name

        if self.login_id is not None:
            result['LoginId'] = self.login_id

        if self.pk is not None:
            result['Pk'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnterpriseLicenseNo') is not None:
            self.enterprise_license_no = m.get('EnterpriseLicenseNo')

        if m.get('EnterpriseName') is not None:
            self.enterprise_name = m.get('EnterpriseName')

        if m.get('LoginId') is not None:
            self.login_id = m.get('LoginId')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        return self

