# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeJVSInstanceResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeJVSInstanceResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        pending_upgrade_count: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned result object.
        self.data = data
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The token that indicates the current position from which to start reading. An empty value indicates reading from the beginning.
        self.next_token = next_token
        self.pending_upgrade_count = pending_upgrade_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.pending_upgrade_count is not None:
            result['PendingUpgradeCount'] = self.pending_upgrade_count

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
                temp_model = main_models.DescribeJVSInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PendingUpgradeCount') is not None:
            self.pending_upgrade_count = m.get('PendingUpgradeCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeJVSInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_version: main_models.DescribeJVSInstanceResponseBodyDataAgentVersion = None,
        create_time: str = None,
        credit_config: List[main_models.DescribeJVSInstanceResponseBodyDataCreditConfig] = None,
        expire_time: str = None,
        installed_skills: List[main_models.DescribeJVSInstanceResponseBodyDataInstalledSkills] = None,
        instance_id: str = None,
        jvs_package_id: str = None,
        modify_time: str = None,
        status: str = None,
        used_credit: List[main_models.DescribeJVSInstanceResponseBodyDataUsedCredit] = None,
    ):
        self.agent_version = agent_version
        # The creation time.
        self.create_time = create_time
        # The credit quota configuration. Subsequent quota configurations overwrite previous configurations.
        self.credit_config = credit_config
        # The expiration time.
        self.expire_time = expire_time
        self.installed_skills = installed_skills
        # The instance ID.
        self.instance_id = instance_id
        # This parameter is not supported.
        self.jvs_package_id = jvs_package_id
        # The modification time.
        self.modify_time = modify_time
        # The instance status.
        self.status = status
        # The used credits.
        self.used_credit = used_credit

    def validate(self):
        if self.agent_version:
            self.agent_version.validate()
        if self.credit_config:
            for v1 in self.credit_config:
                 if v1:
                    v1.validate()
        if self.installed_skills:
            for v1 in self.installed_skills:
                 if v1:
                    v1.validate()
        if self.used_credit:
            for v1 in self.used_credit:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['CreditConfig'] = []
        if self.credit_config is not None:
            for k1 in self.credit_config:
                result['CreditConfig'].append(k1.to_map() if k1 else None)

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        result['InstalledSkills'] = []
        if self.installed_skills is not None:
            for k1 in self.installed_skills:
                result['InstalledSkills'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.jvs_package_id is not None:
            result['JvsPackageId'] = self.jvs_package_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.status is not None:
            result['Status'] = self.status

        result['UsedCredit'] = []
        if self.used_credit is not None:
            for k1 in self.used_credit:
                result['UsedCredit'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentVersion') is not None:
            temp_model = main_models.DescribeJVSInstanceResponseBodyDataAgentVersion()
            self.agent_version = temp_model.from_map(m.get('AgentVersion'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.credit_config = []
        if m.get('CreditConfig') is not None:
            for k1 in m.get('CreditConfig'):
                temp_model = main_models.DescribeJVSInstanceResponseBodyDataCreditConfig()
                self.credit_config.append(temp_model.from_map(k1))

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        self.installed_skills = []
        if m.get('InstalledSkills') is not None:
            for k1 in m.get('InstalledSkills'):
                temp_model = main_models.DescribeJVSInstanceResponseBodyDataInstalledSkills()
                self.installed_skills.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JvsPackageId') is not None:
            self.jvs_package_id = m.get('JvsPackageId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.used_credit = []
        if m.get('UsedCredit') is not None:
            for k1 in m.get('UsedCredit'):
                temp_model = main_models.DescribeJVSInstanceResponseBodyDataUsedCredit()
                self.used_credit.append(temp_model.from_map(k1))

        return self

class DescribeJVSInstanceResponseBodyDataUsedCredit(DaraModel):
    def __init__(
        self,
        credit: int = None,
        limit_period: str = None,
    ):
        # The number of credits.
        self.credit = credit
        # The dimension of the current credit.
        self.limit_period = limit_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit is not None:
            result['Credit'] = self.credit

        if self.limit_period is not None:
            result['LimitPeriod'] = self.limit_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credit') is not None:
            self.credit = m.get('Credit')

        if m.get('LimitPeriod') is not None:
            self.limit_period = m.get('LimitPeriod')

        return self

class DescribeJVSInstanceResponseBodyDataInstalledSkills(DaraModel):
    def __init__(
        self,
        description: str = None,
        icon_url: str = None,
        installed_at: str = None,
        skill_id: str = None,
        skill_name: str = None,
        skill_type: str = None,
    ):
        self.description = description
        self.icon_url = icon_url
        self.installed_at = installed_at
        self.skill_id = skill_id
        self.skill_name = skill_name
        self.skill_type = skill_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.installed_at is not None:
            result['InstalledAt'] = self.installed_at

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.skill_type is not None:
            result['SkillType'] = self.skill_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('InstalledAt') is not None:
            self.installed_at = m.get('InstalledAt')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')

        return self

class DescribeJVSInstanceResponseBodyDataCreditConfig(DaraModel):
    def __init__(
        self,
        credit_limit: int = None,
        limit_period: str = None,
    ):
        # The quota limit. Valid values:
        # - 0: not available for use.
        # - >0: the quota is configured based on the numeric value.
        # - -1: unlimited.
        self.credit_limit = credit_limit
        # The quota period. Valid values:
        # - total: The total usage limit.
        # - month: Monthly. The quota resets based on the resource activation time as one cycle.
        # - day: Daily. The quota resets at 00:00.
        self.limit_period = limit_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_limit is not None:
            result['CreditLimit'] = self.credit_limit

        if self.limit_period is not None:
            result['LimitPeriod'] = self.limit_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditLimit') is not None:
            self.credit_limit = m.get('CreditLimit')

        if m.get('LimitPeriod') is not None:
            self.limit_period = m.get('LimitPeriod')

        return self

class DescribeJVSInstanceResponseBodyDataAgentVersion(DaraModel):
    def __init__(
        self,
        upgrade_status: str = None,
        version: str = None,
    ):
        self.upgrade_status = upgrade_status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

