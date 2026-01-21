# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNetworkDomainsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        network_domain_name: str = None,
        network_domain_type: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        # The bastion host ID.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the network domain.
        self.network_domain_name = network_domain_name
        # The connection mode of the network domain. Valid values:
        # 
        # *   **Direct**
        # *   **Proxy**
        self.network_domain_type = network_domain_type
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page.\\
        # Valid values: 1 to 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The region ID of the bastion host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_domain_name is not None:
            result['NetworkDomainName'] = self.network_domain_name

        if self.network_domain_type is not None:
            result['NetworkDomainType'] = self.network_domain_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkDomainName') is not None:
            self.network_domain_name = m.get('NetworkDomainName')

        if m.get('NetworkDomainType') is not None:
            self.network_domain_type = m.get('NetworkDomainType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

