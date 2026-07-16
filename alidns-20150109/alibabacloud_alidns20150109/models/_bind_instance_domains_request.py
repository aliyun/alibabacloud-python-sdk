# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindInstanceDomainsRequest(DaraModel):
    def __init__(
        self,
        domain_names: str = None,
        instance_id: str = None,
        lang: str = None,
    ):
        # A list of domain names.
        # 
        # > Separate multiple domain names with a comma (,). You can specify up to 100 domain names.
        # 
        # This parameter is required.
        self.domain_names = domain_names
        # The ID of the Alibaba Cloud DNS instance. You can call the [ListCloudGtmInstances](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-listcloudgtminstances) operation to obtain the ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of the response. Valid values:
        # 
        # - zh: Chinese
        # 
        # - en: English
        # 
        # Default value: zh
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

