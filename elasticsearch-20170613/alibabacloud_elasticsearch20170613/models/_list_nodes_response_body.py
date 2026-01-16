# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListNodesResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListNodesResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListNodesResponseBodyResult] = None,
    ):
        # The header of the response.
        self.headers = headers
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListNodesResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListNodesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListNodesResponseBodyResult(DaraModel):
    def __init__(
        self,
        agent_status: str = None,
        cloud_assistant_status: str = None,
        ecs_instance_id: str = None,
        ecs_instance_name: str = None,
        ip_address: List[main_models.ListNodesResponseBodyResultIpAddress] = None,
        os_type: str = None,
        status: str = None,
        tags: List[main_models.ListNodesResponseBodyResultTags] = None,
    ):
        # The status of the shipper on the ECS instance. Valid values:
        # 
        # *   heartOk: The heartbeat is normal.
        # *   heartLost: The heartbeat is abnormal.
        # *   uninstalled: The shipper is not installed.
        # *   failed: The shipper fails to be installed.
        self.agent_status = agent_status
        # Indicates whether the Cloud Assistant client is installed. Valid values:
        # 
        # *   true: installed
        # *   false: not installed
        self.cloud_assistant_status = cloud_assistant_status
        # The ID of the ECS instance.
        self.ecs_instance_id = ecs_instance_id
        # The name of the ECS instance.
        self.ecs_instance_name = ecs_instance_name
        # The IP addresses of the ECS instance.
        self.ip_address = ip_address
        # The operating system type of the ECS instance. Valid values:
        # 
        # *   windows: Windows Server
        # *   linux: Linux
        self.os_type = os_type
        # The status of the ECS instance. Valid values:
        # 
        # *   running: The instance is running.
        # *   starting: The instance is being started.
        # *   stopping: The instance is being stopped.
        # *   stopped: The instance is stopped.
        self.status = status
        # The tags of the ECS instance.
        self.tags = tags

    def validate(self):
        if self.ip_address:
            for v1 in self.ip_address:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_status is not None:
            result['agentStatus'] = self.agent_status

        if self.cloud_assistant_status is not None:
            result['cloudAssistantStatus'] = self.cloud_assistant_status

        if self.ecs_instance_id is not None:
            result['ecsInstanceId'] = self.ecs_instance_id

        if self.ecs_instance_name is not None:
            result['ecsInstanceName'] = self.ecs_instance_name

        result['ipAddress'] = []
        if self.ip_address is not None:
            for k1 in self.ip_address:
                result['ipAddress'].append(k1.to_map() if k1 else None)

        if self.os_type is not None:
            result['osType'] = self.os_type

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentStatus') is not None:
            self.agent_status = m.get('agentStatus')

        if m.get('cloudAssistantStatus') is not None:
            self.cloud_assistant_status = m.get('cloudAssistantStatus')

        if m.get('ecsInstanceId') is not None:
            self.ecs_instance_id = m.get('ecsInstanceId')

        if m.get('ecsInstanceName') is not None:
            self.ecs_instance_name = m.get('ecsInstanceName')

        self.ip_address = []
        if m.get('ipAddress') is not None:
            for k1 in m.get('ipAddress'):
                temp_model = main_models.ListNodesResponseBodyResultIpAddress()
                self.ip_address.append(temp_model.from_map(k1))

        if m.get('osType') is not None:
            self.os_type = m.get('osType')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListNodesResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListNodesResponseBodyResultTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

class ListNodesResponseBodyResultIpAddress(DaraModel):
    def __init__(
        self,
        host: str = None,
        ip_type: str = None,
    ):
        # The IP address.
        self.host = host
        # The type of the IP address. Valid values:
        # 
        # *   public: public IP address
        # *   private: private IP address
        self.ip_type = ip_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['host'] = self.host

        if self.ip_type is not None:
            result['ipType'] = self.ip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('ipType') is not None:
            self.ip_type = m.get('ipType')

        return self

class ListNodesResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        # The number of entries returned.
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        return self

