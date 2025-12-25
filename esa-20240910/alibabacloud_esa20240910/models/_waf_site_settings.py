# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class WafSiteSettings(DaraModel):
    def __init__(
        self,
        add_bot_protection_headers: main_models.WafSiteSettingsAddBotProtectionHeaders = None,
        add_security_headers: main_models.WafSiteSettingsAddSecurityHeaders = None,
        bandwidth_abuse_protection: main_models.WafSiteSettingsBandwidthAbuseProtection = None,
        bot_management: main_models.WafSiteSettingsBotManagement = None,
        client_ip_identifier: main_models.WafSiteSettingsClientIpIdentifier = None,
        disable_security_module: main_models.WafSiteSettingsDisableSecurityModule = None,
        security_level: main_models.WafSiteSettingsSecurityLevel = None,
    ):
        self.add_bot_protection_headers = add_bot_protection_headers
        self.add_security_headers = add_security_headers
        self.bandwidth_abuse_protection = bandwidth_abuse_protection
        self.bot_management = bot_management
        self.client_ip_identifier = client_ip_identifier
        self.disable_security_module = disable_security_module
        self.security_level = security_level

    def validate(self):
        if self.add_bot_protection_headers:
            self.add_bot_protection_headers.validate()
        if self.add_security_headers:
            self.add_security_headers.validate()
        if self.bandwidth_abuse_protection:
            self.bandwidth_abuse_protection.validate()
        if self.bot_management:
            self.bot_management.validate()
        if self.client_ip_identifier:
            self.client_ip_identifier.validate()
        if self.disable_security_module:
            self.disable_security_module.validate()
        if self.security_level:
            self.security_level.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_bot_protection_headers is not None:
            result['AddBotProtectionHeaders'] = self.add_bot_protection_headers.to_map()

        if self.add_security_headers is not None:
            result['AddSecurityHeaders'] = self.add_security_headers.to_map()

        if self.bandwidth_abuse_protection is not None:
            result['BandwidthAbuseProtection'] = self.bandwidth_abuse_protection.to_map()

        if self.bot_management is not None:
            result['BotManagement'] = self.bot_management.to_map()

        if self.client_ip_identifier is not None:
            result['ClientIpIdentifier'] = self.client_ip_identifier.to_map()

        if self.disable_security_module is not None:
            result['DisableSecurityModule'] = self.disable_security_module.to_map()

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddBotProtectionHeaders') is not None:
            temp_model = main_models.WafSiteSettingsAddBotProtectionHeaders()
            self.add_bot_protection_headers = temp_model.from_map(m.get('AddBotProtectionHeaders'))

        if m.get('AddSecurityHeaders') is not None:
            temp_model = main_models.WafSiteSettingsAddSecurityHeaders()
            self.add_security_headers = temp_model.from_map(m.get('AddSecurityHeaders'))

        if m.get('BandwidthAbuseProtection') is not None:
            temp_model = main_models.WafSiteSettingsBandwidthAbuseProtection()
            self.bandwidth_abuse_protection = temp_model.from_map(m.get('BandwidthAbuseProtection'))

        if m.get('BotManagement') is not None:
            temp_model = main_models.WafSiteSettingsBotManagement()
            self.bot_management = temp_model.from_map(m.get('BotManagement'))

        if m.get('ClientIpIdentifier') is not None:
            temp_model = main_models.WafSiteSettingsClientIpIdentifier()
            self.client_ip_identifier = temp_model.from_map(m.get('ClientIpIdentifier'))

        if m.get('DisableSecurityModule') is not None:
            temp_model = main_models.WafSiteSettingsDisableSecurityModule()
            self.disable_security_module = temp_model.from_map(m.get('DisableSecurityModule'))

        if m.get('SecurityLevel') is not None:
            temp_model = main_models.WafSiteSettingsSecurityLevel()
            self.security_level = temp_model.from_map(m.get('SecurityLevel'))

        return self

class WafSiteSettingsSecurityLevel(DaraModel):
    def __init__(
        self,
        value: str = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class WafSiteSettingsDisableSecurityModule(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class WafSiteSettingsClientIpIdentifier(DaraModel):
    def __init__(
        self,
        headers: List[str] = None,
        mode: str = None,
    ):
        self.headers = headers
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

class WafSiteSettingsBotManagement(DaraModel):
    def __init__(
        self,
        definite_bots: main_models.WafSiteSettingsBotManagementDefiniteBots = None,
        effect_on_static: main_models.WafSiteSettingsBotManagementEffectOnStatic = None,
        jsdetection: main_models.WafSiteSettingsBotManagementJSDetection = None,
        likely_bots: main_models.WafSiteSettingsBotManagementLikelyBots = None,
        verified_bots: main_models.WafSiteSettingsBotManagementVerifiedBots = None,
    ):
        self.definite_bots = definite_bots
        self.effect_on_static = effect_on_static
        self.jsdetection = jsdetection
        self.likely_bots = likely_bots
        self.verified_bots = verified_bots

    def validate(self):
        if self.definite_bots:
            self.definite_bots.validate()
        if self.effect_on_static:
            self.effect_on_static.validate()
        if self.jsdetection:
            self.jsdetection.validate()
        if self.likely_bots:
            self.likely_bots.validate()
        if self.verified_bots:
            self.verified_bots.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.definite_bots is not None:
            result['DefiniteBots'] = self.definite_bots.to_map()

        if self.effect_on_static is not None:
            result['EffectOnStatic'] = self.effect_on_static.to_map()

        if self.jsdetection is not None:
            result['JSDetection'] = self.jsdetection.to_map()

        if self.likely_bots is not None:
            result['LikelyBots'] = self.likely_bots.to_map()

        if self.verified_bots is not None:
            result['VerifiedBots'] = self.verified_bots.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefiniteBots') is not None:
            temp_model = main_models.WafSiteSettingsBotManagementDefiniteBots()
            self.definite_bots = temp_model.from_map(m.get('DefiniteBots'))

        if m.get('EffectOnStatic') is not None:
            temp_model = main_models.WafSiteSettingsBotManagementEffectOnStatic()
            self.effect_on_static = temp_model.from_map(m.get('EffectOnStatic'))

        if m.get('JSDetection') is not None:
            temp_model = main_models.WafSiteSettingsBotManagementJSDetection()
            self.jsdetection = temp_model.from_map(m.get('JSDetection'))

        if m.get('LikelyBots') is not None:
            temp_model = main_models.WafSiteSettingsBotManagementLikelyBots()
            self.likely_bots = temp_model.from_map(m.get('LikelyBots'))

        if m.get('VerifiedBots') is not None:
            temp_model = main_models.WafSiteSettingsBotManagementVerifiedBots()
            self.verified_bots = temp_model.from_map(m.get('VerifiedBots'))

        return self

class WafSiteSettingsBotManagementVerifiedBots(DaraModel):
    def __init__(
        self,
        action: str = None,
        id: int = None,
    ):
        self.action = action
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class WafSiteSettingsBotManagementLikelyBots(DaraModel):
    def __init__(
        self,
        action: str = None,
        id: int = None,
    ):
        self.action = action
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class WafSiteSettingsBotManagementJSDetection(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

class WafSiteSettingsBotManagementEffectOnStatic(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

class WafSiteSettingsBotManagementDefiniteBots(DaraModel):
    def __init__(
        self,
        action: str = None,
        id: int = None,
    ):
        self.action = action
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class WafSiteSettingsBandwidthAbuseProtection(DaraModel):
    def __init__(
        self,
        action: str = None,
        id: int = None,
        status: str = None,
    ):
        self.action = action
        self.id = id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class WafSiteSettingsAddSecurityHeaders(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

class WafSiteSettingsAddBotProtectionHeaders(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

