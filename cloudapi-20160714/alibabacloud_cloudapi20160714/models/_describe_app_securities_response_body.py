# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeAppSecuritiesResponseBody(DaraModel):
    def __init__(
        self,
        app_securitys: main_models.DescribeAppSecuritiesResponseBodyAppSecuritys = None,
        request_id: str = None,
    ):
        # The associated security policy information.
        self.app_securitys = app_securitys
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.app_securitys:
            self.app_securitys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_securitys is not None:
            result['AppSecuritys'] = self.app_securitys.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecuritys') is not None:
            temp_model = main_models.DescribeAppSecuritiesResponseBodyAppSecuritys()
            self.app_securitys = temp_model.from_map(m.get('AppSecuritys'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAppSecuritiesResponseBodyAppSecuritys(DaraModel):
    def __init__(
        self,
        app_security: List[main_models.DescribeAppSecuritiesResponseBodyAppSecuritysAppSecurity] = None,
    ):
        self.app_security = app_security

    def validate(self):
        if self.app_security:
            for v1 in self.app_security:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppSecurity'] = []
        if self.app_security is not None:
            for k1 in self.app_security:
                result['AppSecurity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_security = []
        if m.get('AppSecurity') is not None:
            for k1 in m.get('AppSecurity'):
                temp_model = main_models.DescribeAppSecuritiesResponseBodyAppSecuritysAppSecurity()
                self.app_security.append(temp_model.from_map(k1))

        return self

class DescribeAppSecuritiesResponseBodyAppSecuritysAppSecurity(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_key: str = None,
        app_secret: str = None,
        created_time: str = None,
        modified_time: str = None,
    ):
        # The application AppCode.
        self.app_code = app_code
        # The application AppKey.
        self.app_key = app_key
        # The application AppSecret.
        self.app_secret = app_secret
        # The time when the AppKey was created.
        self.created_time = created_time
        # The time when the AppSecret was last modified. The time is displayed in UTC.
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        return self

