# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListAgentInstanceMemoryResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAgentInstanceMemoryResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The memory configurations and statistics information of agent instances on the current page.
        self.data = data
        # The current page number. Pages start from 1.
        self.page_number = page_number
        # The number of entries per page used for this query.
        self.page_size = page_size
        # The unique identifier of the request, which can be used for troubleshooting.
        self.request_id = request_id
        # The total number of instances that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAgentInstanceMemoryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAgentInstanceMemoryResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_instance_id: str = None,
        agent_instance_status: str = None,
        agent_platform: str = None,
        agent_provider: str = None,
        backup_count: int = None,
        end_user_id: str = None,
        last_memory_updated_at: str = None,
        latest_backup_at: str = None,
        memory_count: int = None,
        memory_enabled: str = None,
        region_id: str = None,
        resource_id: str = None,
        runtime_id: str = None,
        runtime_name: str = None,
        user_groups: List[main_models.ListAgentInstanceMemoryResponseBodyDataUserGroups] = None,
        user_name: str = None,
        user_orgs: List[main_models.ListAgentInstanceMemoryResponseBodyDataUserOrgs] = None,
        wy_id: str = None,
    ):
        # The Agent instance ID, which can be used to set the instance memory switch or clear the instance memory.
        self.agent_instance_id = agent_instance_id
        # The lifecycle status of the agent instance.
        # - `UNDEPLOYED`: Undeployed.
        # - `DEPLOYING`: Deploying.
        # - `DEPLOYED`: Deployed.
        # - `STARTING`: Starting.
        # - `RUNNING`: Running.
        # - `STOPPING`: Stopping.
        # - `STOPPED`: Stopped.
        # - `UNAVAILABLE`: Unavailable.
        # - `FAILED`: Failed.
        # - `UPGRADING`: Upgrading.
        # - `REBUILDING`: Resetting.
        # - `DELETING`: Deleting.
        # - `DELETED`: Deleted.
        self.agent_instance_status = agent_instance_status
        # The business platform to which the Agent belongs.
        self.agent_platform = agent_platform
        # The Agent provider.
        self.agent_provider = agent_provider
        # The number of undeleted memory backups for the instance.
        self.backup_count = backup_count
        # The ID of the end user to which the instance belongs.
        self.end_user_id = end_user_id
        # The time of the last memory update. The time is returned in the YYYY-MM-DDThh:mm:ss format, which may include fractional seconds. The time value uses the default time zone of the server, and the string does not contain a time zone offset. This field is omitted if the last update time is unavailable.
        self.last_memory_updated_at = last_memory_updated_at
        # The time of the latest backup. The time is returned in the YYYY-MM-DDThh:mm:ss format, which may include fractional seconds. The time value uses the default time zone of the server, and the string does not contain a time zone offset. This field is omitted if the backup time is unavailable.
        self.latest_backup_at = latest_backup_at
        # The number of memory entries for the instance. This field may be omitted if statistics are unavailable.
        self.memory_count = memory_count
        # The memory switch configured for the instance, returned as a string. A value of `true` indicates that the switch is turned on. A value of `false` indicates that the switch is turned off.
        self.memory_enabled = memory_enabled
        # The ID of the region where the runtime is located.
        self.region_id = region_id
        # The ID of the resource associated with the instance.
        self.resource_id = resource_id
        # The runtime ID of the instance.
        self.runtime_id = runtime_id
        # The runtime name. The associated resource name is returned in preference. If the resource name is unavailable, the instance name is returned.
        self.runtime_name = runtime_name
        # The list of user groups to which the end user belongs.
        self.user_groups = user_groups
        # The username of the end user to which the instance belongs.
        self.user_name = user_name
        # The list of organizations to which the end user belongs.
        self.user_orgs = user_orgs
        # The Wuying user ID of the end user.
        self.wy_id = wy_id

    def validate(self):
        if self.user_groups:
            for v1 in self.user_groups:
                 if v1:
                    v1.validate()
        if self.user_orgs:
            for v1 in self.user_orgs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_instance_id is not None:
            result['AgentInstanceId'] = self.agent_instance_id

        if self.agent_instance_status is not None:
            result['AgentInstanceStatus'] = self.agent_instance_status

        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.backup_count is not None:
            result['BackupCount'] = self.backup_count

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.last_memory_updated_at is not None:
            result['LastMemoryUpdatedAt'] = self.last_memory_updated_at

        if self.latest_backup_at is not None:
            result['LatestBackupAt'] = self.latest_backup_at

        if self.memory_count is not None:
            result['MemoryCount'] = self.memory_count

        if self.memory_enabled is not None:
            result['MemoryEnabled'] = self.memory_enabled

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.runtime_name is not None:
            result['RuntimeName'] = self.runtime_name

        result['UserGroups'] = []
        if self.user_groups is not None:
            for k1 in self.user_groups:
                result['UserGroups'].append(k1.to_map() if k1 else None)

        if self.user_name is not None:
            result['UserName'] = self.user_name

        result['UserOrgs'] = []
        if self.user_orgs is not None:
            for k1 in self.user_orgs:
                result['UserOrgs'].append(k1.to_map() if k1 else None)

        if self.wy_id is not None:
            result['WyId'] = self.wy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentInstanceId') is not None:
            self.agent_instance_id = m.get('AgentInstanceId')

        if m.get('AgentInstanceStatus') is not None:
            self.agent_instance_status = m.get('AgentInstanceStatus')

        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('BackupCount') is not None:
            self.backup_count = m.get('BackupCount')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('LastMemoryUpdatedAt') is not None:
            self.last_memory_updated_at = m.get('LastMemoryUpdatedAt')

        if m.get('LatestBackupAt') is not None:
            self.latest_backup_at = m.get('LatestBackupAt')

        if m.get('MemoryCount') is not None:
            self.memory_count = m.get('MemoryCount')

        if m.get('MemoryEnabled') is not None:
            self.memory_enabled = m.get('MemoryEnabled')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('RuntimeName') is not None:
            self.runtime_name = m.get('RuntimeName')

        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k1 in m.get('UserGroups'):
                temp_model = main_models.ListAgentInstanceMemoryResponseBodyDataUserGroups()
                self.user_groups.append(temp_model.from_map(k1))

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        self.user_orgs = []
        if m.get('UserOrgs') is not None:
            for k1 in m.get('UserOrgs'):
                temp_model = main_models.ListAgentInstanceMemoryResponseBodyDataUserOrgs()
                self.user_orgs.append(temp_model.from_map(k1))

        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')

        return self

class ListAgentInstanceMemoryResponseBodyDataUserOrgs(DaraModel):
    def __init__(
        self,
        org_id: str = None,
        org_name: str = None,
    ):
        # The organization ID.
        self.org_id = org_id
        # The organization name.
        self.org_name = org_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.org_name is not None:
            result['OrgName'] = self.org_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')

        return self

class ListAgentInstanceMemoryResponseBodyDataUserGroups(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
    ):
        # The user group ID.
        self.group_id = group_id
        # The user group name.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

