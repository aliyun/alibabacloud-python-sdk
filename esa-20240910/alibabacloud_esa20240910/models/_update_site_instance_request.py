# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSiteInstanceRequest(DaraModel):
    def __init__(
        self,
        new_instance_id: str = None,
        resource_owner: int = None,
        site_id: int = None,
    ):
        # The target instance ID.
        # 
        # This parameter is required.
        self.new_instance_id = new_instance_id
        self.resource_owner = resource_owner
        # The site ID. You can call [ListSites](https://help.aliyun.com/document_detail/2850189.html) to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_instance_id is not None:
            result['NewInstanceId'] = self.new_instance_id

        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewInstanceId') is not None:
            self.new_instance_id = m.get('NewInstanceId')

        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

