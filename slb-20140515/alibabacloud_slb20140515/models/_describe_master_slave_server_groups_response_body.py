# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeMasterSlaveServerGroupsResponseBody(DaraModel):
    def __init__(
        self,
        master_slave_server_groups: main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroups = None,
        request_id: str = None,
    ):
        # The primary/secondary server groups.
        self.master_slave_server_groups = master_slave_server_groups
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.master_slave_server_groups:
            self.master_slave_server_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.master_slave_server_groups is not None:
            result['MasterSlaveServerGroups'] = self.master_slave_server_groups.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterSlaveServerGroups') is not None:
            temp_model = main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroups()
            self.master_slave_server_groups = temp_model.from_map(m.get('MasterSlaveServerGroups'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroups(DaraModel):
    def __init__(
        self,
        master_slave_server_group: List[main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroup] = None,
    ):
        self.master_slave_server_group = master_slave_server_group

    def validate(self):
        if self.master_slave_server_group:
            for v1 in self.master_slave_server_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MasterSlaveServerGroup'] = []
        if self.master_slave_server_group is not None:
            for k1 in self.master_slave_server_group:
                result['MasterSlaveServerGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.master_slave_server_group = []
        if m.get('MasterSlaveServerGroup') is not None:
            for k1 in m.get('MasterSlaveServerGroup'):
                temp_model = main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroup()
                self.master_slave_server_group.append(temp_model.from_map(k1))

        return self

class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroup(DaraModel):
    def __init__(
        self,
        associated_objects: main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjects = None,
        create_time: str = None,
        master_slave_server_group_id: str = None,
        master_slave_server_group_name: str = None,
        tags: main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupTags = None,
    ):
        # The associated resources.
        self.associated_objects = associated_objects
        # The time when the CLB instance was created. Specify the time in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.create_time = create_time
        # The ID of the primary/secondary server group.
        self.master_slave_server_group_id = master_slave_server_group_id
        # The name of the primary/secondary server group.
        self.master_slave_server_group_name = master_slave_server_group_name
        # The tags to add to the resource.
        self.tags = tags

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

        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id

        if self.master_slave_server_group_name is not None:
            result['MasterSlaveServerGroupName'] = self.master_slave_server_group_name

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedObjects') is not None:
            temp_model = main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjects()
            self.associated_objects = temp_model.from_map(m.get('AssociatedObjects'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')

        if m.get('MasterSlaveServerGroupName') is not None:
            self.master_slave_server_group_name = m.get('MasterSlaveServerGroupName')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupTagsTag] = None,
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
                temp_model = main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupTagsTag(DaraModel):
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

class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjects(DaraModel):
    def __init__(
        self,
        listeners: main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListeners = None,
    ):
        # The listeners.
        self.listeners = listeners

    def validate(self):
        if self.listeners:
            self.listeners.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listeners is not None:
            result['Listeners'] = self.listeners.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            temp_model = main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListeners()
            self.listeners = temp_model.from_map(m.get('Listeners'))

        return self

class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListeners(DaraModel):
    def __init__(
        self,
        listener: List[main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListenersListener] = None,
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
                temp_model = main_models.DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListenersListener()
                self.listener.append(temp_model.from_map(k1))

        return self

class DescribeMasterSlaveServerGroupsResponseBodyMasterSlaveServerGroupsMasterSlaveServerGroupAssociatedObjectsListenersListener(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The listener port.
        self.port = port
        # The listener protocol.
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

