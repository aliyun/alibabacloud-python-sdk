# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmInstanceConfigEnableStatusRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        config_id: str = None,
        enable_status: str = None,
        instance_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - **zh-CN**: Chinese.
        # 
        # - **en-US** (default): English.
        self.accept_language = accept_language
        # A client-generated token that is used to ensure the idempotence of the request. The token must be unique among different requests and can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The ID of the domain name instance configuration. For the same access domain name and GTM instance, you can configure both A and AAAA records. This results in two domain name instance configurations for the GTM instance. The ConfigId uniquely identifies a specific configuration.
        # 
        # Call the [ListCloudGtmInstanceConfigs](https://help.aliyun.com/document_detail/2797349.html) operation to query the ConfigId of a domain name instance.
        self.config_id = config_id
        # The enablement status of the domain name instance. Valid values:
        # 
        # - enable: Enables the domain name instance.
        # 
        # - disable: Disables the domain name instance.
        self.enable_status = enable_status
        # The ID of the GTM 3.0 instance that you want to modify.
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

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

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

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

