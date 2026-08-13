# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListAvailableConfigsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        configs: List[main_models.ListAvailableConfigsResponseBodyConfigs] = None,
        message: str = None,
        request_id: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 可用的组织同步配置列表
        self.configs = configs
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['configs'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.configs = []
        if m.get('configs') is not None:
            for k1 in m.get('configs'):
                temp_model = main_models.ListAvailableConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListAvailableConfigsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        corp_name: str = None,
        platform_type: str = None,
        sso_settings_id: str = None,
        sso_settings_name: str = None,
    ):
        # 企业标识（wecom=corpId, saml=idpEntityId, oauth2=clientId, custom=客户自定义）。注意：OAuth2 多 IdP 配置使用相同 clientId 时，需在 syncOrgStructure 中显式传 ssoSettingsId
        self.corp_id = corp_id
        # 企业展示名称
        self.corp_name = corp_name
        # 平台类型: wecom / saml / oauth2 / custom
        self.platform_type = platform_type
        # SSO 配置 ID（仅 SAML/OAuth2/WeCom 有值，custom 为 null）
        self.sso_settings_id = sso_settings_id
        # SSO 配置名称（仅 SAML/OAuth2/WeCom 有值，custom 为 null）
        self.sso_settings_name = sso_settings_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        if self.corp_name is not None:
            result['corpName'] = self.corp_name

        if self.platform_type is not None:
            result['platformType'] = self.platform_type

        if self.sso_settings_id is not None:
            result['ssoSettingsId'] = self.sso_settings_id

        if self.sso_settings_name is not None:
            result['ssoSettingsName'] = self.sso_settings_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        if m.get('corpName') is not None:
            self.corp_name = m.get('corpName')

        if m.get('platformType') is not None:
            self.platform_type = m.get('platformType')

        if m.get('ssoSettingsId') is not None:
            self.sso_settings_id = m.get('ssoSettingsId')

        if m.get('ssoSettingsName') is not None:
            self.sso_settings_name = m.get('ssoSettingsName')

        return self

