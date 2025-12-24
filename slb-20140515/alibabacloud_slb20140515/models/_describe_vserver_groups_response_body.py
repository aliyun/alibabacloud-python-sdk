# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeVServerGroupsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vserver_groups: main_models.DescribeVServerGroupsResponseBodyVServerGroups = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The backend servers.
        self.vserver_groups = vserver_groups

    def validate(self):
        if self.vserver_groups:
            self.vserver_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vserver_groups is not None:
            result['VServerGroups'] = self.vserver_groups.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VServerGroups') is not None:
            temp_model = main_models.DescribeVServerGroupsResponseBodyVServerGroups()
            self.vserver_groups = temp_model.from_map(m.get('VServerGroups'))

        return self

class DescribeVServerGroupsResponseBodyVServerGroups(DaraModel):
    def __init__(
        self,
        vserver_group: List[main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroup] = None,
    ):
        self.vserver_group = vserver_group

    def validate(self):
        if self.vserver_group:
            for v1 in self.vserver_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VServerGroup'] = []
        if self.vserver_group is not None:
            for k1 in self.vserver_group:
                result['VServerGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vserver_group = []
        if m.get('VServerGroup') is not None:
            for k1 in m.get('VServerGroup'):
                temp_model = main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroup()
                self.vserver_group.append(temp_model.from_map(k1))

        return self

class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroup(DaraModel):
    def __init__(
        self,
        associated_objects: main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjects = None,
        create_time: str = None,
        server_count: int = None,
        tags: main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupTags = None,
        vserver_group_id: str = None,
        vserver_group_name: str = None,
    ):
        # The associated resources.
        self.associated_objects = associated_objects
        # The time when the CLB instance was created. The time follows the `YYYY-MM-DDThh:mm:ssZ` format.
        self.create_time = create_time
        # The number of servers.
        # 
        # This parameter is unavailable by default. To use this parameter, submit a ticket or contact your account manager.
        self.server_count = server_count
        # The tags.
        self.tags = tags
        # The server group ID.
        self.vserver_group_id = vserver_group_id
        # The server group name.
        self.vserver_group_name = vserver_group_name

    def validate(self):
        if self.associated_objects:
            self.associated_objects.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_objects is not None:
            result['AssociatedObjects'] = self.associated_objects.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.server_count is not None:
            result['ServerCount'] = self.server_count

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        if self.vserver_group_name is not None:
            result['VServerGroupName'] = self.vserver_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedObjects') is not None:
            temp_model = main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjects()
            self.associated_objects = temp_model.from_map(m.get('AssociatedObjects'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ServerCount') is not None:
            self.server_count = m.get('ServerCount')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        if m.get('VServerGroupName') is not None:
            self.vserver_group_name = m.get('VServerGroupName')

        return self

class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupTagsTag] = None,
    ):
        self.tag = tag

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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjects(DaraModel):
    def __init__(
        self,
        listeners: main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListeners = None,
        rules: main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRules = None,
    ):
        # The listeners.
        self.listeners = listeners
        # The forwarding rules.
        self.rules = rules

    def validate(self):
        if self.listeners:
            self.listeners.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listeners is not None:
            result['Listeners'] = self.listeners.to_map()

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            temp_model = main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListeners()
            self.listeners = temp_model.from_map(m.get('Listeners'))

        if m.get('Rules') is not None:
            temp_model = main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        return self

class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for v1 in self.rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rule'] = []
        if self.rule is not None:
            for k1 in self.rule:
                result['Rule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k1 in m.get('Rule'):
                temp_model = main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsRulesRule(DaraModel):
    def __init__(
        self,
        domain: str = None,
        rule_id: str = None,
        rule_name: str = None,
        url: str = None,
    ):
        # The requested domain name.
        self.domain = domain
        # The ID of the forwarding rule.
        self.rule_id = rule_id
        # The name of the forwarding rule.
        self.rule_name = rule_name
        # The request URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListeners(DaraModel):
    def __init__(
        self,
        listener: List[main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListenersListener] = None,
    ):
        self.listener = listener

    def validate(self):
        if self.listener:
            for v1 in self.listener:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Listener'] = []
        if self.listener is not None:
            for k1 in self.listener:
                result['Listener'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener = []
        if m.get('Listener') is not None:
            for k1 in m.get('Listener'):
                temp_model = main_models.DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListenersListener()
                self.listener.append(temp_model.from_map(k1))

        return self

class DescribeVServerGroupsResponseBodyVServerGroupsVServerGroupAssociatedObjectsListenersListener(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The listener port.
        self.port = port
        # The listener protocol. Valid values: **tcp**, **udp**, **http**, and **https**.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

