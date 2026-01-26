# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitEnvironmentRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        create_auth_token: bool = None,
        environment_id: str = None,
        managed_type: str = None,
        region_id: str = None,
    ):
        # The language. Valid values: zh and en. Default value: zh.
        self.aliyun_lang = aliyun_lang
        # Specifies whether to create a token to improve data security.
        self.create_auth_token = create_auth_token
        # The ID of the environment instance.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # Whether agents or exporters are managed. Valid values:
        # 
        # *   none: No. By default, no managed agents or exporters are provided for ACK clusters.
        # *   agent: Agents are managed. By default, managed agents are provided for ASK clusters, ACS clusters, and ACK One clusters.
        # *   agent-exproter: Agents and exporters are managed. By default, managed agents and exporters are provided for cloud services.
        self.managed_type = managed_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.create_auth_token is not None:
            result['CreateAuthToken'] = self.create_auth_token

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.managed_type is not None:
            result['ManagedType'] = self.managed_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('CreateAuthToken') is not None:
            self.create_auth_token = m.get('CreateAuthToken')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('ManagedType') is not None:
            self.managed_type = m.get('ManagedType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

