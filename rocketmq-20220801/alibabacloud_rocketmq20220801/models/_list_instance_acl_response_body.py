# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListInstanceAclResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.ListInstanceAclResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied due to the reason that the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListInstanceAclResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListInstanceAclResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListInstanceAclResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The pagination information.
        self.list = list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListInstanceAclResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListInstanceAclResponseBodyDataList(DaraModel):
    def __init__(
        self,
        acl_type: str = None,
        actions: List[str] = None,
        decision: str = None,
        instance_id: str = None,
        ip_whitelists: List[str] = None,
        region_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        username: str = None,
    ):
        # The ACL type.
        # 
        # Valid value:
        # 
        # *   APACHE: open source ACL.
        self.acl_type = acl_type
        # The types of the operations that are allowed by the ACL.
        self.actions = actions
        # The decision result.
        # 
        # Valid values:
        # 
        # *   Deny: Access is denied.
        # *   Allow: Access is allowed.
        self.decision = decision
        # The instance ID.
        self.instance_id = instance_id
        # The IP address whitelists.
        self.ip_whitelists = ip_whitelists
        # The region ID.
        self.region_id = region_id
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        # 
        # Valid values:
        # 
        # *   Group
        # *   Topic
        self.resource_type = resource_type
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_type is not None:
            result['aclType'] = self.acl_type

        if self.actions is not None:
            result['actions'] = self.actions

        if self.decision is not None:
            result['decision'] = self.decision

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.ip_whitelists is not None:
            result['ipWhitelists'] = self.ip_whitelists

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aclType') is not None:
            self.acl_type = m.get('aclType')

        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('decision') is not None:
            self.decision = m.get('decision')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('ipWhitelists') is not None:
            self.ip_whitelists = m.get('ipWhitelists')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

