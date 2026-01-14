# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class GetInstanceAclResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetInstanceAclResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The response code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID
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
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetInstanceAclResponseBodyData()
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

class GetInstanceAclResponseBodyData(DaraModel):
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
        # The authentication type of the instance.
        # 
        # Valid values:
        # 
        # *   apache_acl: open source access control list (ACL)
        # *   default: the default account of the instance
        self.acl_type = acl_type
        # The type of operations that can be performed on the resource.
        self.actions = actions
        # The decision result of the authorization.
        self.decision = decision
        # The instance ID.
        self.instance_id = instance_id
        # The IP address whitelists.
        self.ip_whitelists = ip_whitelists
        # The region ID.
        self.region_id = region_id
        # The name of the resource on which the permissions are granted.
        self.resource_name = resource_name
        # The type of the resource on which the permissions are granted.
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

