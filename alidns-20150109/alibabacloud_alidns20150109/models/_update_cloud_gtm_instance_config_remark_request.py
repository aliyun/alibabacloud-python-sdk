# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmInstanceConfigRemarkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        config_id: str = None,
        instance_id: str = None,
        remark: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - **zh-CN**: Chinese.
        # 
        # - **en-US** (default): English.
        self.accept_language = accept_language
        # The client token that is used to ensure the idempotence of the request. Generate a unique token for each request. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The ID of the instance configuration. A GTM instance can have multiple configurations if you add both an A record and an AAAA record for the same domain name. The ConfigId uniquely identifies the configuration that you want to update.
        # 
        # For more information, see [ListCloudGtmInstanceConfigs](https://help.aliyun.com/document_detail/2797349.html).
        self.config_id = config_id
        # The ID of the Global Traffic Manager (GTM) instance for which you want to update the remarks.
        self.instance_id = instance_id
        # The new remarks for the configuration.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

