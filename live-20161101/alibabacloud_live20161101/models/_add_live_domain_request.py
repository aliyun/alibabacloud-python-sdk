# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class AddLiveDomainRequest(DaraModel):
    def __init__(
        self,
        check_url: str = None,
        domain_name: str = None,
        live_domain_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region: str = None,
        resource_group_id: str = None,
        scope: str = None,
        security_token: str = None,
        tag: List[main_models.AddLiveDomainRequestTag] = None,
        top_level_domain: str = None,
    ):
        # The URL that is used for health checks.
        self.check_url = check_url
        # The ingest domain or streaming domain that you want to add. Wildcard domain names that start with a period (.) are supported.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The type of the domain name. Valid values:
        # 
        # *   **liveVideo**: streaming domain. This value is required if you set the DomainName parameter to a streaming domain.
        # *   **liveEdge**: ingest domain. This value is required if you set the DomainName parameter to an ingest domain.
        # 
        # This parameter is required.
        self.live_domain_type = live_domain_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region in which the domain name resides. Valid values:
        # 
        # *   **cn-beijing**: China (Beijing)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **cn-qingdao**: China (Qingdao)
        # *   **ap-southeast-1**: Singapore
        # *   **eu-central-1**: Germany (Frankfurt)
        # *   **ap-northeast-1**: Japan (Tokyo)
        # *   **ap-southeast-5**: Indonesia (Jakarta)
        # 
        # >  Make sure that the settings of the Region and Scope parameters do not conflict with each other.
        # 
        # This parameter is required.
        self.region = region
        # The ID of the resource group. For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/2381067.html).
        self.resource_group_id = resource_group_id
        # The edge group. This parameter is applicable to users of level 3 or higher in mainland China and users outside mainland China. Valid values:
        # 
        # *   **domestic**: mainland China. This is the default value.
        # *   **overseas**: outside mainland China.
        # *   **global**: regions in and outside mainland China.
        self.scope = scope
        self.security_token = security_token
        # The tags.
        self.tag = tag
        # The top-level domain name.
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

        if self.live_domain_type is not None:
            result['LiveDomainType'] = self.live_domain_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

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

        if m.get('LiveDomainType') is not None:
            self.live_domain_type = m.get('LiveDomainType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.AddLiveDomainRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')

        return self

class AddLiveDomainRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

