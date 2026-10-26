# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHostAccountsForHostShareKeyRequest(DaraModel):
    def __init__(
        self,
        host_share_key_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # The ID of the host shared key.
        # > You can call the [ListHostShareKeys](https://help.aliyun.com/document_detail/462973.html) operation to retrieve this parameter.
        self.host_share_key_id = host_share_key_id
        # The instance ID of the Bastionhost.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to retrieve this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies the page number of the returned results. Default value: **1**.
        self.page_number = page_number
        # The Settings for the paged query determine the number of host accounts associated with the host shared key to return on each page during paging. Default value: **10**, which indicates that 10 host accounts associated with the host shared key are displayed on each page.
        self.page_size = page_size
        # The project ID.
        self.project_id = project_id
        # The region ID of the Bastionhost instance.
        # > For the mappings between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

