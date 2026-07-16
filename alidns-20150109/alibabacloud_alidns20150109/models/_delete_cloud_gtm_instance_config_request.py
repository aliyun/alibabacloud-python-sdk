# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCloudGtmInstanceConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        config_id: str = None,
        instance_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese.
        # 
        # - en-US: English. This is the default value.
        self.accept_language = accept_language
        # The client token that is used to ensure the idempotence of the request. Generate a unique token for each request. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The ID of the instance configuration. A GTM instance can have two configurations, an A record and an AAAA record, for the same access domain name. The ConfigId uniquely identifies one of the configurations. To obtain the ConfigId, call the [ListCloudGtmInstanceConfigs](https://help.aliyun.com/document_detail/2797349.html) operation.
        self.config_id = config_id
        # The ID of the Global Traffic Manager (GTM) 3.0 instance.
        self.instance_id = instance_id

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

        return self

