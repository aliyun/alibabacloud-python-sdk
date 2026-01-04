# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetLoginRedirectApplicationForBrandResponseBody(DaraModel):
    def __init__(
        self,
        brand_login_redirect_application: main_models.GetLoginRedirectApplicationForBrandResponseBodyBrandLoginRedirectApplication = None,
        request_id: str = None,
    ):
        self.brand_login_redirect_application = brand_login_redirect_application
        self.request_id = request_id

    def validate(self):
        if self.brand_login_redirect_application:
            self.brand_login_redirect_application.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand_login_redirect_application is not None:
            result['BrandLoginRedirectApplication'] = self.brand_login_redirect_application.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrandLoginRedirectApplication') is not None:
            temp_model = main_models.GetLoginRedirectApplicationForBrandResponseBodyBrandLoginRedirectApplication()
            self.brand_login_redirect_application = temp_model.from_map(m.get('BrandLoginRedirectApplication'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLoginRedirectApplicationForBrandResponseBodyBrandLoginRedirectApplication(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        brand_id: str = None,
        instance_id: str = None,
    ):
        # 应用ID
        self.application_id = application_id
        # 品牌ID
        self.brand_id = brand_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.brand_id is not None:
            result['BrandId'] = self.brand_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('BrandId') is not None:
            self.brand_id = m.get('BrandId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

