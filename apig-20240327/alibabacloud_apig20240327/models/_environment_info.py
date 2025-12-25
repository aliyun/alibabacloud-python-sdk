# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class EnvironmentInfo(DaraModel):
    def __init__(
        self,
        alias: str = None,
        create_timestamp: int = None,
        default: bool = None,
        description: str = None,
        environment_id: str = None,
        gateway_info: main_models.GatewayInfo = None,
        name: str = None,
        resource_group_id: str = None,
        sub_domain_infos: List[main_models.SubDomainInfo] = None,
        update_timestamp: int = None,
    ):
        self.alias = alias
        self.create_timestamp = create_timestamp
        self.default = default
        self.description = description
        self.environment_id = environment_id
        self.gateway_info = gateway_info
        self.name = name
        self.resource_group_id = resource_group_id
        self.sub_domain_infos = sub_domain_infos
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.gateway_info:
            self.gateway_info.validate()
        if self.sub_domain_infos:
            for v1 in self.sub_domain_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.default is not None:
            result['default'] = self.default

        if self.description is not None:
            result['description'] = self.description

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.gateway_info is not None:
            result['gatewayInfo'] = self.gateway_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        result['subDomainInfos'] = []
        if self.sub_domain_infos is not None:
            for k1 in self.sub_domain_infos:
                result['subDomainInfos'].append(k1.to_map() if k1 else None)

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('default') is not None:
            self.default = m.get('default')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('gatewayInfo') is not None:
            temp_model = main_models.GatewayInfo()
            self.gateway_info = temp_model.from_map(m.get('gatewayInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.sub_domain_infos = []
        if m.get('subDomainInfos') is not None:
            for k1 in m.get('subDomainInfos'):
                temp_model = main_models.SubDomainInfo()
                self.sub_domain_infos.append(temp_model.from_map(k1))

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

