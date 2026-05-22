# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSiteRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        coverage: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        site_name: str = None,
    ):
        # The DNS setup. Valid values:
        # 
        # *   **NS**
        # *   **CNAME**
        # 
        # This parameter is required.
        self.access_type = access_type
        # The service location. Valid values:
        # 
        # *   **domestic**: the Chinese mainland
        # *   **global**: global
        # *   **overseas**: outside the Chinese mainland
        # 
        # This parameter is required.
        self.coverage = coverage
        # The instance ID, which can be obtained by calling the [ListUserRatePlanInstances](https://help.aliyun.com/document_detail/2852398.html) operation. Specify at least one of the instance ID and website ID. If you specify both of them, the instance ID is used.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the resource group. If you leave this parameter empty, the system uses the default resource group ID.
        self.resource_group_id = resource_group_id
        # The website name.
        # 
        # This parameter is required.
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.coverage is not None:
            result['Coverage'] = self.coverage

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        return self

