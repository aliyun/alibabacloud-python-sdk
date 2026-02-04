# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class AddDcdnDomainRequest(DaraModel):
    def __init__(
        self,
        check_url: str = None,
        domain_name: str = None,
        function_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        scene: str = None,
        scope: str = None,
        security_token: str = None,
        sources: str = None,
        tag: List[main_models.AddDcdnDomainRequestTag] = None,
        top_level_domain: str = None,
    ):
        # The URL that is used for health checks.
        self.check_url = check_url
        # The domain name that you want to add. You can specify only one domain name in each request.
        # 
        # Wildcard domain names are supported. A wildcard domain name must start with a period (.), such as .example.com.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Computing service type. Valid values:
        # 
        # *   **routine**
        # *   **image**
        # *   **cloudFunction**
        self.function_type = function_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the resource group. If you do not specify a value for this parameter, the system automatically assigns the ID of the default resource group.
        self.resource_group_id = resource_group_id
        # The Acceleration scen. Supported:
        # 
        # * apiscene:API acceleration.
        # * webservicescene: accelerate website business.
        # * staticscene: video and graphic acceleration.
        # * (Empty): no scene.
        self.scene = scene
        # The acceleration region. Valid values:
        # 
        # *   **domestic**: Chinese mainland
        # *   **overseas**: outside the Chinese mainland
        # *   **global**: global
        # 
        # Default value: **domestic**.
        self.scope = scope
        self.security_token = security_token
        # The information about the addresses of origin servers.
        self.sources = sources
        # The information about the tags.
        self.tag = tag
        # The top-level domain.
        self.top_level_domain = top_level_domain

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.function_type is not None:
            result['FunctionType'] = self.function_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.sources is not None:
            result['Sources'] = self.sources

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Sources') is not None:
            self.sources = m.get('Sources')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.AddDcdnDomainRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')

        return self



class AddDcdnDomainRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of a tag. Valid values of N: **1 to 20**.
        self.key = key
        # The value of a tag. Valid values of N: **1 to 20**.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

