# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InstallCloudMonitorRequest(DaraModel):
    def __init__(
        self,
        agent_access_key: str = None,
        agent_secret_key: str = None,
        argus_version: str = None,
        instance_id_list: List[str] = None,
        uuid_list: List[str] = None,
    ):
        # The AccessKey ID that is required to install the CloudMonitor agent. You can call the [DescribeMonitoringAgentAccessKey](https://help.aliyun.com/document_detail/114948.html) operation to query the AccessKey ID.
        # 
        # > This parameter is required only when you install the CloudMonitor agent on servers that are not deployed on Alibaba Cloud.
        self.agent_access_key = agent_access_key
        # The AccessKey secret that is required to install the CloudMonitor agent. You can call the [DescribeMonitoringAgentAccessKey](https://help.aliyun.com/document_detail/114948.html) operation to query the AccessKey secret.
        # 
        # > This parameter is required only when you install the CloudMonitor agent on servers that are not deployed on Alibaba Cloud.
        self.agent_secret_key = agent_secret_key
        # The version of the CloudMonitor agent that you want to install on the servers. For more information about the latest version of the CloudMonitor agent, see [Overview](https://help.aliyun.com/document_detail/183431.html).
        # 
        # This parameter is required.
        self.argus_version = argus_version
        # The IDs of the servers on which you want to install the CloudMonitor agent. Separate multiple IDs with commas (,).
        self.instance_id_list = instance_id_list
        # The UUIDs of the servers on which you want to install the CloudMonitor agent. Separate multiple UUIDs with commas (,).
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_access_key is not None:
            result['AgentAccessKey'] = self.agent_access_key

        if self.agent_secret_key is not None:
            result['AgentSecretKey'] = self.agent_secret_key

        if self.argus_version is not None:
            result['ArgusVersion'] = self.argus_version

        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentAccessKey') is not None:
            self.agent_access_key = m.get('AgentAccessKey')

        if m.get('AgentSecretKey') is not None:
            self.agent_secret_key = m.get('AgentSecretKey')

        if m.get('ArgusVersion') is not None:
            self.argus_version = m.get('ArgusVersion')

        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

