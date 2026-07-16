# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHttpsApplicationConfigurationRequest(DaraModel):
    def __init__(
        self,
        alt_svc: str = None,
        alt_svc_clear: str = None,
        alt_svc_ma: str = None,
        alt_svc_persist: str = None,
        hsts: str = None,
        hsts_include_subdomains: str = None,
        hsts_max_age: str = None,
        hsts_preload: str = None,
        https_force: str = None,
        https_force_code: str = None,
        https_no_sni_deny: str = None,
        https_sni_verify: str = None,
        https_sni_whitelist: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # Specifies whether to enable the Alt-Svc header. Disabled by default. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.alt_svc = alt_svc
        # Specifies whether to include the `clear` parameter in the Alt-Svc header. Disabled by default. Valid values:
        # 
        # - `on`: The parameter is included.
        # 
        # - `off`: The parameter is not included.
        self.alt_svc_clear = alt_svc_clear
        # The Max Age for the Alt-Svc header, in seconds. The default is 86400.
        self.alt_svc_ma = alt_svc_ma
        # Specifies whether to include the `persist` parameter in the Alt-Svc header. Disabled by default. Valid values:
        # 
        # - `on`: The parameter is included.
        # 
        # - `off`: The parameter is not included.
        self.alt_svc_persist = alt_svc_persist
        # Specifies whether to enable HTTP Strict Transport Security (HSTS). Disabled by default. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.hsts = hsts
        # Specifies whether to include the `includeSubDomains` directive in the HSTS header. Disabled by default. Valid values:
        # 
        # - `on`: The directive is included.
        # 
        # - `off`: The directive is not included.
        self.hsts_include_subdomains = hsts_include_subdomains
        # The value of the `max-age` directive for the HSTS header, in seconds.
        self.hsts_max_age = hsts_max_age
        # Specifies whether to enable HSTS Preload by including the `preload` directive in the HSTS header. Disabled by default. Valid values:
        # 
        # - `on`: The directive is included.
        # 
        # - `off`: The directive is not included.
        self.hsts_preload = hsts_preload
        # Specifies whether to enable Force HTTPS. Disabled by default. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.https_force = https_force
        # The Redirection Status Code to use when Force HTTPS is enabled. Valid values:
        # 
        # - `301`
        # 
        # - `302`
        # 
        # - `307`
        # 
        # - `308`
        self.https_force_code = https_force_code
        # Specifies whether to reject TLS Handshake Requests that do not include an SNI. Disabled by default. Valid values:
        # 
        # - `on`: Rejects requests without an SNI.
        # 
        # - `off`: Allows requests without an SNI.
        self.https_no_sni_deny = https_no_sni_deny
        # Specifies whether to enable Server Name Indication (SNI) verification. Disabled by default. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.https_sni_verify = https_sni_verify
        # Specifies the allowlist of SNI values. Separate multiple values with a space.
        self.https_sni_whitelist = https_sni_whitelist
        # The content of the Rule, which is a Conditional Expression that matches user Requests. This parameter is optional when adding a Global Configuration. Supported use cases include:
        # 
        # - To match all incoming requests, set the value to `true`.
        # 
        # - To match specific requests, use a custom expression. For example: `(http.host eq "video.example.com")`.
        self.rule = rule
        # Specifies whether to enable the rule. This parameter is optional when adding a Global Configuration. Valid values:
        # 
        # - `on`: The rule is enabled.
        # 
        # - `off`: The rule is disabled.
        self.rule_enable = rule_enable
        # The name of the Rule. This parameter is optional when adding a Global Configuration.
        self.rule_name = rule_name
        # The execution order of the rule. A lower value indicates a higher priority.
        self.sequence = sequence
        # The ID of the Site. You can get this ID by calling the [ListSites](~~ListSites~~) API.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The Site\\"s configuration Version. For Sites with version management enabled, this parameter specifies the Version to which the configuration applies. The default is 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alt_svc is not None:
            result['AltSvc'] = self.alt_svc

        if self.alt_svc_clear is not None:
            result['AltSvcClear'] = self.alt_svc_clear

        if self.alt_svc_ma is not None:
            result['AltSvcMa'] = self.alt_svc_ma

        if self.alt_svc_persist is not None:
            result['AltSvcPersist'] = self.alt_svc_persist

        if self.hsts is not None:
            result['Hsts'] = self.hsts

        if self.hsts_include_subdomains is not None:
            result['HstsIncludeSubdomains'] = self.hsts_include_subdomains

        if self.hsts_max_age is not None:
            result['HstsMaxAge'] = self.hsts_max_age

        if self.hsts_preload is not None:
            result['HstsPreload'] = self.hsts_preload

        if self.https_force is not None:
            result['HttpsForce'] = self.https_force

        if self.https_force_code is not None:
            result['HttpsForceCode'] = self.https_force_code

        if self.https_no_sni_deny is not None:
            result['HttpsNoSniDeny'] = self.https_no_sni_deny

        if self.https_sni_verify is not None:
            result['HttpsSniVerify'] = self.https_sni_verify

        if self.https_sni_whitelist is not None:
            result['HttpsSniWhitelist'] = self.https_sni_whitelist

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AltSvc') is not None:
            self.alt_svc = m.get('AltSvc')

        if m.get('AltSvcClear') is not None:
            self.alt_svc_clear = m.get('AltSvcClear')

        if m.get('AltSvcMa') is not None:
            self.alt_svc_ma = m.get('AltSvcMa')

        if m.get('AltSvcPersist') is not None:
            self.alt_svc_persist = m.get('AltSvcPersist')

        if m.get('Hsts') is not None:
            self.hsts = m.get('Hsts')

        if m.get('HstsIncludeSubdomains') is not None:
            self.hsts_include_subdomains = m.get('HstsIncludeSubdomains')

        if m.get('HstsMaxAge') is not None:
            self.hsts_max_age = m.get('HstsMaxAge')

        if m.get('HstsPreload') is not None:
            self.hsts_preload = m.get('HstsPreload')

        if m.get('HttpsForce') is not None:
            self.https_force = m.get('HttpsForce')

        if m.get('HttpsForceCode') is not None:
            self.https_force_code = m.get('HttpsForceCode')

        if m.get('HttpsNoSniDeny') is not None:
            self.https_no_sni_deny = m.get('HttpsNoSniDeny')

        if m.get('HttpsSniVerify') is not None:
            self.https_sni_verify = m.get('HttpsSniVerify')

        if m.get('HttpsSniWhitelist') is not None:
            self.https_sni_whitelist = m.get('HttpsSniWhitelist')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

