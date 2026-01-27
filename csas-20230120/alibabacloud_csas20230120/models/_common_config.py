# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CommonConfig(DaraModel):
    def __init__(
        self,
        idp: main_models.CommonConfigIdp = None,
    ):
        self.idp = idp

    def validate(self):
        if self.idp:
            self.idp.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idp is not None:
            result['Idp'] = self.idp.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Idp') is not None:
            temp_model = main_models.CommonConfigIdp()
            self.idp = temp_model.from_map(m.get('Idp'))

        return self

class CommonConfigIdp(DaraModel):
    def __init__(
        self,
        ap_oidc_callback_url: str = None,
        dingtalk: main_models.CommonConfigIdpDingtalk = None,
        feishu: main_models.CommonConfigIdpFeishu = None,
        idaas_2: main_models.CommonConfigIdpIdaas2 = None,
        saml: main_models.CommonConfigIdpSaml = None,
    ):
        self.ap_oidc_callback_url = ap_oidc_callback_url
        self.dingtalk = dingtalk
        self.feishu = feishu
        self.idaas_2 = idaas_2
        self.saml = saml

    def validate(self):
        if self.dingtalk:
            self.dingtalk.validate()
        if self.feishu:
            self.feishu.validate()
        if self.idaas_2:
            self.idaas_2.validate()
        if self.saml:
            self.saml.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ap_oidc_callback_url is not None:
            result['ApOidcCallbackUrl'] = self.ap_oidc_callback_url

        if self.dingtalk is not None:
            result['Dingtalk'] = self.dingtalk.to_map()

        if self.feishu is not None:
            result['Feishu'] = self.feishu.to_map()

        if self.idaas_2 is not None:
            result['Idaas2'] = self.idaas_2.to_map()

        if self.saml is not None:
            result['Saml'] = self.saml.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApOidcCallbackUrl') is not None:
            self.ap_oidc_callback_url = m.get('ApOidcCallbackUrl')

        if m.get('Dingtalk') is not None:
            temp_model = main_models.CommonConfigIdpDingtalk()
            self.dingtalk = temp_model.from_map(m.get('Dingtalk'))

        if m.get('Feishu') is not None:
            temp_model = main_models.CommonConfigIdpFeishu()
            self.feishu = temp_model.from_map(m.get('Feishu'))

        if m.get('Idaas2') is not None:
            temp_model = main_models.CommonConfigIdpIdaas2()
            self.idaas_2 = temp_model.from_map(m.get('Idaas2'))

        if m.get('Saml') is not None:
            temp_model = main_models.CommonConfigIdpSaml()
            self.saml = temp_model.from_map(m.get('Saml'))

        return self

class CommonConfigIdpSaml(DaraModel):
    def __init__(
        self,
        acs: str = None,
        metadata: str = None,
    ):
        self.acs = acs
        self.metadata = metadata

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acs is not None:
            result['Acs'] = self.acs

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acs') is not None:
            self.acs = m.get('Acs')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        return self

class CommonConfigIdpIdaas2(DaraModel):
    def __init__(
        self,
        event_callback_base: str = None,
        event_label: str = None,
    ):
        self.event_callback_base = event_callback_base
        self.event_label = event_label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_callback_base is not None:
            result['EventCallbackBase'] = self.event_callback_base

        if self.event_label is not None:
            result['EventLabel'] = self.event_label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCallbackBase') is not None:
            self.event_callback_base = m.get('EventCallbackBase')

        if m.get('EventLabel') is not None:
            self.event_label = m.get('EventLabel')

        return self

class CommonConfigIdpFeishu(DaraModel):
    def __init__(
        self,
        event_callback_base: str = None,
        event_label: str = None,
        home_page: str = None,
        login_redirect: str = None,
    ):
        self.event_callback_base = event_callback_base
        self.event_label = event_label
        self.home_page = home_page
        self.login_redirect = login_redirect

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_callback_base is not None:
            result['EventCallbackBase'] = self.event_callback_base

        if self.event_label is not None:
            result['EventLabel'] = self.event_label

        if self.home_page is not None:
            result['HomePage'] = self.home_page

        if self.login_redirect is not None:
            result['LoginRedirect'] = self.login_redirect

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCallbackBase') is not None:
            self.event_callback_base = m.get('EventCallbackBase')

        if m.get('EventLabel') is not None:
            self.event_label = m.get('EventLabel')

        if m.get('HomePage') is not None:
            self.home_page = m.get('HomePage')

        if m.get('LoginRedirect') is not None:
            self.login_redirect = m.get('LoginRedirect')

        return self

class CommonConfigIdpDingtalk(DaraModel):
    def __init__(
        self,
        event_callback_base: str = None,
        event_label: str = None,
        home_page: str = None,
        login_redirect: str = None,
    ):
        self.event_callback_base = event_callback_base
        self.event_label = event_label
        self.home_page = home_page
        self.login_redirect = login_redirect

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_callback_base is not None:
            result['EventCallbackBase'] = self.event_callback_base

        if self.event_label is not None:
            result['EventLabel'] = self.event_label

        if self.home_page is not None:
            result['HomePage'] = self.home_page

        if self.login_redirect is not None:
            result['LoginRedirect'] = self.login_redirect

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCallbackBase') is not None:
            self.event_callback_base = m.get('EventCallbackBase')

        if m.get('EventLabel') is not None:
            self.event_label = m.get('EventLabel')

        if m.get('HomePage') is not None:
            self.home_page = m.get('HomePage')

        if m.get('LoginRedirect') is not None:
            self.login_redirect = m.get('LoginRedirect')

        return self

