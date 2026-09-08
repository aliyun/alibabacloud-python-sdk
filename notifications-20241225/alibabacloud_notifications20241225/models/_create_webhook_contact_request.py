# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWebhookContactRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        bot_security_token: str = None,
        caller_protocol: str = None,
        client_source: str = None,
        contact_name: str = None,
        cookies: str = None,
        security_token: str = None,
        server_url: str = None,
        src_url: str = None,
        template_code: str = None,
        tenant_code: str = None,
        uid_type: str = None,
        verification_code: str = None,
        webhook_type: str = None,
    ):
        # The language.
        self.accept_language = accept_language
        # The application name of the caller.
        self.app_name = app_name
        # The business line of the caller.
        self.biz_name = biz_name
        # The webhook security signature token.
        self.bot_security_token = bot_security_token
        # The request protocol type.
        self.caller_protocol = caller_protocol
        # The source of the operation terminal.
        self.client_source = client_source
        # The name of the webhook contact.
        self.contact_name = contact_name
        # The user cookies.
        self.cookies = cookies
        self.security_token = security_token
        # The DingTalk group chatbot URL.
        self.server_url = server_url
        # The URL of the source page.
        self.src_url = src_url
        # The template code.
        self.template_code = template_code
        # The tenant information.
        self.tenant_code = tenant_code
        # The user type.
        self.uid_type = uid_type
        # The verification code.
        self.verification_code = verification_code
        # The webhook type.
        self.webhook_type = webhook_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.bot_security_token is not None:
            result['BotSecurityToken'] = self.bot_security_token

        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol

        if self.client_source is not None:
            result['ClientSource'] = self.client_source

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.cookies is not None:
            result['Cookies'] = self.cookies

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.server_url is not None:
            result['ServerUrl'] = self.server_url

        if self.src_url is not None:
            result['SrcUrl'] = self.src_url

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code

        if self.uid_type is not None:
            result['UidType'] = self.uid_type

        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code

        if self.webhook_type is not None:
            result['WebhookType'] = self.webhook_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('BotSecurityToken') is not None:
            self.bot_security_token = m.get('BotSecurityToken')

        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')

        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')

        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')

        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')

        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')

        if m.get('WebhookType') is not None:
            self.webhook_type = m.get('WebhookType')

        return self

