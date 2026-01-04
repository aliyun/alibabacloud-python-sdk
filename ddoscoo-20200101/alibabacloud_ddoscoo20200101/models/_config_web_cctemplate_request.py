# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigWebCCTemplateRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        resource_group_id: str = None,
        template: str = None,
    ):
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The mode of the Frequency Control policy. Valid values:
        # 
        # *   **default**: Normal
        # *   **gf_under_attack**: Emergency
        # *   **gf_sos_verify**: Strict
        # *   **gf_sos_enhance**: Super Strict
        # 
        # This parameter is required.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

