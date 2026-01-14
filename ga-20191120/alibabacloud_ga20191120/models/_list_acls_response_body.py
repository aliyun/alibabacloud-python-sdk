# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListAclsResponseBody(DaraModel):
    def __init__(
        self,
        acls: List[main_models.ListAclsResponseBodyAcls] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The network ACLs.
        self.acls = acls
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If **NextToken** is not returned, it indicates that no additional results exist.
        # *   If **NextToken** is returned, the value is the token that is used for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.acls:
            for v1 in self.acls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Acls'] = []
        if self.acls is not None:
            for k1 in self.acls:
                result['Acls'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acls = []
        if m.get('Acls') is not None:
            for k1 in m.get('Acls'):
                temp_model = main_models.ListAclsResponseBodyAcls()
                self.acls.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAclsResponseBodyAcls(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_name: str = None,
        acl_status: str = None,
        address_ipversion: str = None,
        resource_group_id: str = None,
        tags: List[main_models.ListAclsResponseBodyAclsTags] = None,
    ):
        # The ID of the network ACL.
        self.acl_id = acl_id
        # The name of the network ACL.
        self.acl_name = acl_name
        # The status of the network ACL. Valid values:
        # 
        # *   **init**: The network ACL is being initialized.
        # *   **active**: The network ACL is available.
        # *   **configuring**: The network ACL is being configured.
        # *   **updating**: The network ACL is being updated.
        # *   **deleting:** The network ACL is being deleted.
        self.acl_status = acl_status
        # The IP version of the network ACL. Valid values:
        # 
        # *   **IPv4**
        # *   **IPv6**
        self.address_ipversion = address_ipversion
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags of the network ACL.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_name is not None:
            result['AclName'] = self.acl_name

        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListAclsResponseBodyAclsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListAclsResponseBodyAclsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the network ACL.
        self.key = key
        # The tag value of the network ACL.
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

