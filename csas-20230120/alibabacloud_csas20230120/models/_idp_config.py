# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class IdpConfig(DaraModel):
    def __init__(
        self,
        attr_map_config: main_models.IdpAttrMapConfig = None,
        connect_config: main_models.IdpConnectConfig = None,
        description: str = None,
        dingtalk_config: main_models.IdpDingtalkSubConfig = None,
        enabled: bool = None,
        feishu_config: main_models.IdpFeishuSubConfig = None,
        idaas_config: main_models.IdpIdaas2SubConfig = None,
        idp_config_id: str = None,
        last_sync_time_unix: int = None,
        ldap_config: main_models.IdpLdapSubConfig = None,
        login_config: main_models.IdpLoginConfig = None,
        logo_directory: str = None,
        name: str = None,
        sync_config: main_models.IdpSyncConfig = None,
        sync_status: str = None,
        type: str = None,
        weixin_config: main_models.IdpWeixin2SubConfig = None,
        wuying_config: main_models.OpenStructIdpWuyingSubConfig = None,
    ):
        self.attr_map_config = attr_map_config
        self.connect_config = connect_config
        self.description = description
        self.dingtalk_config = dingtalk_config
        self.enabled = enabled
        self.feishu_config = feishu_config
        self.idaas_config = idaas_config
        self.idp_config_id = idp_config_id
        self.last_sync_time_unix = last_sync_time_unix
        self.ldap_config = ldap_config
        self.login_config = login_config
        self.logo_directory = logo_directory
        self.name = name
        self.sync_config = sync_config
        self.sync_status = sync_status
        self.type = type
        self.weixin_config = weixin_config
        self.wuying_config = wuying_config

    def validate(self):
        if self.attr_map_config:
            self.attr_map_config.validate()
        if self.connect_config:
            self.connect_config.validate()
        if self.dingtalk_config:
            self.dingtalk_config.validate()
        if self.feishu_config:
            self.feishu_config.validate()
        if self.idaas_config:
            self.idaas_config.validate()
        if self.ldap_config:
            self.ldap_config.validate()
        if self.login_config:
            self.login_config.validate()
        if self.sync_config:
            self.sync_config.validate()
        if self.weixin_config:
            self.weixin_config.validate()
        if self.wuying_config:
            self.wuying_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attr_map_config is not None:
            result['AttrMapConfig'] = self.attr_map_config.to_map()

        if self.connect_config is not None:
            result['ConnectConfig'] = self.connect_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.dingtalk_config is not None:
            result['DingtalkConfig'] = self.dingtalk_config.to_map()

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.feishu_config is not None:
            result['FeishuConfig'] = self.feishu_config.to_map()

        if self.idaas_config is not None:
            result['IdaasConfig'] = self.idaas_config.to_map()

        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id

        if self.last_sync_time_unix is not None:
            result['LastSyncTimeUnix'] = self.last_sync_time_unix

        if self.ldap_config is not None:
            result['LdapConfig'] = self.ldap_config.to_map()

        if self.login_config is not None:
            result['LoginConfig'] = self.login_config.to_map()

        if self.logo_directory is not None:
            result['LogoDirectory'] = self.logo_directory

        if self.name is not None:
            result['Name'] = self.name

        if self.sync_config is not None:
            result['SyncConfig'] = self.sync_config.to_map()

        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status

        if self.type is not None:
            result['Type'] = self.type

        if self.weixin_config is not None:
            result['WeixinConfig'] = self.weixin_config.to_map()

        if self.wuying_config is not None:
            result['WuyingConfig'] = self.wuying_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttrMapConfig') is not None:
            temp_model = main_models.IdpAttrMapConfig()
            self.attr_map_config = temp_model.from_map(m.get('AttrMapConfig'))

        if m.get('ConnectConfig') is not None:
            temp_model = main_models.IdpConnectConfig()
            self.connect_config = temp_model.from_map(m.get('ConnectConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DingtalkConfig') is not None:
            temp_model = main_models.IdpDingtalkSubConfig()
            self.dingtalk_config = temp_model.from_map(m.get('DingtalkConfig'))

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('FeishuConfig') is not None:
            temp_model = main_models.IdpFeishuSubConfig()
            self.feishu_config = temp_model.from_map(m.get('FeishuConfig'))

        if m.get('IdaasConfig') is not None:
            temp_model = main_models.IdpIdaas2SubConfig()
            self.idaas_config = temp_model.from_map(m.get('IdaasConfig'))

        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')

        if m.get('LastSyncTimeUnix') is not None:
            self.last_sync_time_unix = m.get('LastSyncTimeUnix')

        if m.get('LdapConfig') is not None:
            temp_model = main_models.IdpLdapSubConfig()
            self.ldap_config = temp_model.from_map(m.get('LdapConfig'))

        if m.get('LoginConfig') is not None:
            temp_model = main_models.IdpLoginConfig()
            self.login_config = temp_model.from_map(m.get('LoginConfig'))

        if m.get('LogoDirectory') is not None:
            self.logo_directory = m.get('LogoDirectory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SyncConfig') is not None:
            temp_model = main_models.IdpSyncConfig()
            self.sync_config = temp_model.from_map(m.get('SyncConfig'))

        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WeixinConfig') is not None:
            temp_model = main_models.IdpWeixin2SubConfig()
            self.weixin_config = temp_model.from_map(m.get('WeixinConfig'))

        if m.get('WuyingConfig') is not None:
            temp_model = main_models.OpenStructIdpWuyingSubConfig()
            self.wuying_config = temp_model.from_map(m.get('WuyingConfig'))

        return self

