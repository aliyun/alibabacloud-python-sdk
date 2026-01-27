# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class PAL7Config(DaraModel):
    def __init__(
        self,
        bypass_config: main_models.PAL7ConfigBypassConfig = None,
        cert_id: str = None,
        dns_config: main_models.PAL7ConfigDnsConfig = None,
        js_hook_config: main_models.PAL7ConfigJsHookConfig = None,
        proxy_domain_types: bytes = None,
        request_header_rewrite_config: main_models.PAL7ConfigRequestHeaderRewriteConfig = None,
        request_query_rewrite_config: main_models.PAL7ConfigRequestQueryRewriteConfig = None,
        response_header_rewrite_config: main_models.PAL7ConfigResponseHeaderRewriteConfig = None,
        response_rewrite_config: main_models.PAL7ConfigResponseRewriteConfig = None,
    ):
        self.bypass_config = bypass_config
        self.cert_id = cert_id
        self.dns_config = dns_config
        self.js_hook_config = js_hook_config
        self.proxy_domain_types = proxy_domain_types
        self.request_header_rewrite_config = request_header_rewrite_config
        self.request_query_rewrite_config = request_query_rewrite_config
        self.response_header_rewrite_config = response_header_rewrite_config
        self.response_rewrite_config = response_rewrite_config

    def validate(self):
        if self.bypass_config:
            self.bypass_config.validate()
        if self.dns_config:
            self.dns_config.validate()
        if self.js_hook_config:
            self.js_hook_config.validate()
        if self.request_header_rewrite_config:
            self.request_header_rewrite_config.validate()
        if self.request_query_rewrite_config:
            self.request_query_rewrite_config.validate()
        if self.response_header_rewrite_config:
            self.response_header_rewrite_config.validate()
        if self.response_rewrite_config:
            self.response_rewrite_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bypass_config is not None:
            result['BypassConfig'] = self.bypass_config.to_map()

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.dns_config is not None:
            result['DnsConfig'] = self.dns_config.to_map()

        if self.js_hook_config is not None:
            result['JsHookConfig'] = self.js_hook_config.to_map()

        if self.proxy_domain_types is not None:
            result['ProxyDomainTypes'] = self.proxy_domain_types

        if self.request_header_rewrite_config is not None:
            result['RequestHeaderRewriteConfig'] = self.request_header_rewrite_config.to_map()

        if self.request_query_rewrite_config is not None:
            result['RequestQueryRewriteConfig'] = self.request_query_rewrite_config.to_map()

        if self.response_header_rewrite_config is not None:
            result['ResponseHeaderRewriteConfig'] = self.response_header_rewrite_config.to_map()

        if self.response_rewrite_config is not None:
            result['ResponseRewriteConfig'] = self.response_rewrite_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BypassConfig') is not None:
            temp_model = main_models.PAL7ConfigBypassConfig()
            self.bypass_config = temp_model.from_map(m.get('BypassConfig'))

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('DnsConfig') is not None:
            temp_model = main_models.PAL7ConfigDnsConfig()
            self.dns_config = temp_model.from_map(m.get('DnsConfig'))

        if m.get('JsHookConfig') is not None:
            temp_model = main_models.PAL7ConfigJsHookConfig()
            self.js_hook_config = temp_model.from_map(m.get('JsHookConfig'))

        if m.get('ProxyDomainTypes') is not None:
            self.proxy_domain_types = m.get('ProxyDomainTypes')

        if m.get('RequestHeaderRewriteConfig') is not None:
            temp_model = main_models.PAL7ConfigRequestHeaderRewriteConfig()
            self.request_header_rewrite_config = temp_model.from_map(m.get('RequestHeaderRewriteConfig'))

        if m.get('RequestQueryRewriteConfig') is not None:
            temp_model = main_models.PAL7ConfigRequestQueryRewriteConfig()
            self.request_query_rewrite_config = temp_model.from_map(m.get('RequestQueryRewriteConfig'))

        if m.get('ResponseHeaderRewriteConfig') is not None:
            temp_model = main_models.PAL7ConfigResponseHeaderRewriteConfig()
            self.response_header_rewrite_config = temp_model.from_map(m.get('ResponseHeaderRewriteConfig'))

        if m.get('ResponseRewriteConfig') is not None:
            temp_model = main_models.PAL7ConfigResponseRewriteConfig()
            self.response_rewrite_config = temp_model.from_map(m.get('ResponseRewriteConfig'))

        return self

class PAL7ConfigResponseRewriteConfig(DaraModel):
    def __init__(
        self,
        mode: str = None,
        replace_rules: List[main_models.PAL7ConfigReplaceRule] = None,
    ):
        self.mode = mode
        self.replace_rules = replace_rules

    def validate(self):
        if self.replace_rules:
            for v1 in self.replace_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        result['ReplaceRules'] = []
        if self.replace_rules is not None:
            for k1 in self.replace_rules:
                result['ReplaceRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        self.replace_rules = []
        if m.get('ReplaceRules') is not None:
            for k1 in m.get('ReplaceRules'):
                temp_model = main_models.PAL7ConfigReplaceRule()
                self.replace_rules.append(temp_model.from_map(k1))

        return self

class PAL7ConfigResponseHeaderRewriteConfig(DaraModel):
    def __init__(
        self,
        ops: List[main_models.PAL7ConfigRewriteOp] = None,
    ):
        self.ops = ops

    def validate(self):
        if self.ops:
            for v1 in self.ops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ops'] = []
        if self.ops is not None:
            for k1 in self.ops:
                result['Ops'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ops = []
        if m.get('Ops') is not None:
            for k1 in m.get('Ops'):
                temp_model = main_models.PAL7ConfigRewriteOp()
                self.ops.append(temp_model.from_map(k1))

        return self

class PAL7ConfigRequestQueryRewriteConfig(DaraModel):
    def __init__(
        self,
        ops: List[main_models.PAL7ConfigRewriteOp] = None,
    ):
        self.ops = ops

    def validate(self):
        if self.ops:
            for v1 in self.ops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ops'] = []
        if self.ops is not None:
            for k1 in self.ops:
                result['Ops'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ops = []
        if m.get('Ops') is not None:
            for k1 in m.get('Ops'):
                temp_model = main_models.PAL7ConfigRewriteOp()
                self.ops.append(temp_model.from_map(k1))

        return self

class PAL7ConfigRequestHeaderRewriteConfig(DaraModel):
    def __init__(
        self,
        ops: List[main_models.PAL7ConfigRewriteOp] = None,
    ):
        self.ops = ops

    def validate(self):
        if self.ops:
            for v1 in self.ops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ops'] = []
        if self.ops is not None:
            for k1 in self.ops:
                result['Ops'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ops = []
        if m.get('Ops') is not None:
            for k1 in m.get('Ops'):
                temp_model = main_models.PAL7ConfigRewriteOp()
                self.ops.append(temp_model.from_map(k1))

        return self

class PAL7ConfigJsHookConfig(DaraModel):
    def __init__(
        self,
        mode: str = None,
        replace_rules: List[main_models.PAL7ConfigReplaceRule] = None,
    ):
        self.mode = mode
        self.replace_rules = replace_rules

    def validate(self):
        if self.replace_rules:
            for v1 in self.replace_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        result['ReplaceRules'] = []
        if self.replace_rules is not None:
            for k1 in self.replace_rules:
                result['ReplaceRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        self.replace_rules = []
        if m.get('ReplaceRules') is not None:
            for k1 in m.get('ReplaceRules'):
                temp_model = main_models.PAL7ConfigReplaceRule()
                self.replace_rules.append(temp_model.from_map(k1))

        return self

class PAL7ConfigDnsConfig(DaraModel):
    def __init__(
        self,
        dns_servers: List[str] = None,
    ):
        self.dns_servers = dns_servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServers') is not None:
            self.dns_servers = m.get('DnsServers')

        return self

class PAL7ConfigBypassConfig(DaraModel):
    def __init__(
        self,
        app_bypass_froms: List[str] = None,
        mode: str = None,
        url_bypass_rules: List[main_models.PAL7ConfigBypassConfigUrlBypassRules] = None,
    ):
        self.app_bypass_froms = app_bypass_froms
        self.mode = mode
        self.url_bypass_rules = url_bypass_rules

    def validate(self):
        if self.url_bypass_rules:
            for v1 in self.url_bypass_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_bypass_froms is not None:
            result['AppBypassFroms'] = self.app_bypass_froms

        if self.mode is not None:
            result['Mode'] = self.mode

        result['UrlBypassRules'] = []
        if self.url_bypass_rules is not None:
            for k1 in self.url_bypass_rules:
                result['UrlBypassRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppBypassFroms') is not None:
            self.app_bypass_froms = m.get('AppBypassFroms')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        self.url_bypass_rules = []
        if m.get('UrlBypassRules') is not None:
            for k1 in m.get('UrlBypassRules'):
                temp_model = main_models.PAL7ConfigBypassConfigUrlBypassRules()
                self.url_bypass_rules.append(temp_model.from_map(k1))

        return self

class PAL7ConfigBypassConfigUrlBypassRules(DaraModel):
    def __init__(
        self,
        froms: List[str] = None,
        paths: List[str] = None,
    ):
        self.froms = froms
        self.paths = paths

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.froms is not None:
            result['Froms'] = self.froms

        if self.paths is not None:
            result['Paths'] = self.paths

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Froms') is not None:
            self.froms = m.get('Froms')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        return self

