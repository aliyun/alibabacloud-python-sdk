# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_ecd20210602 import models as main_models
from darabonba.model import DaraModel

class ListSkillsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        skills: List[main_models.ListSkillsResponseBodySkills] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of skill details.
        self.skills = skills
        # The total number of query results.
        self.total_count = total_count

    def validate(self):
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['Skills'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.skills = []
        if m.get('Skills') is not None:
            for k1 in m.get('Skills'):
                temp_model = main_models.ListSkillsResponseBodySkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSkillsResponseBodySkills(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        author: str = None,
        default_version: str = None,
        description: str = None,
        display_name: str = None,
        enable: bool = None,
        env_vars: Dict[str, str] = None,
        gmt_created: str = None,
        skill_icon_url: str = None,
        skill_id: str = None,
        skill_name: str = None,
        skill_versions: List[main_models.ListSkillsResponseBodySkillsSkillVersions] = None,
        slug: str = None,
        source_market: str = None,
        source_market_name: str = None,
        supplier_type: str = None,
        support_agent_list: List[main_models.ListSkillsResponseBodySkillsSupportAgentList] = None,
    ):
        # The API key of the skill.
        self.api_key = api_key
        # The author.
        self.author = author
        # The currently effective version number. If no version is effective, an empty value is returned.
        self.default_version = default_version
        # The skill description.
        self.description = description
        # The display name.
        self.display_name = display_name
        # Indicates whether the skill is enabled.
        self.enable = enable
        # The environment variables.
        self.env_vars = env_vars
        # The creation time.
        self.gmt_created = gmt_created
        # The URL of the skill icon.
        self.skill_icon_url = skill_icon_url
        # The unique identifier of the skill.
        self.skill_id = skill_id
        # The name in the SKILL.md file.
        self.skill_name = skill_name
        self.skill_versions = skill_versions
        # The skill slug identifier, which is user-defined and unique within the tenant.
        self.slug = slug
        # The source marketplace code.
        self.source_market = source_market
        # The source marketplace name.
        self.source_market_name = source_market_name
        # The supply type.
        self.supplier_type = supplier_type
        self.support_agent_list = support_agent_list

    def validate(self):
        if self.skill_versions:
            for v1 in self.skill_versions:
                 if v1:
                    v1.validate()
        if self.support_agent_list:
            for v1 in self.support_agent_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.author is not None:
            result['Author'] = self.author

        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.env_vars is not None:
            result['EnvVars'] = self.env_vars

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.skill_icon_url is not None:
            result['SkillIconUrl'] = self.skill_icon_url

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        result['SkillVersions'] = []
        if self.skill_versions is not None:
            for k1 in self.skill_versions:
                result['SkillVersions'].append(k1.to_map() if k1 else None)

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.source_market is not None:
            result['SourceMarket'] = self.source_market

        if self.source_market_name is not None:
            result['SourceMarketName'] = self.source_market_name

        if self.supplier_type is not None:
            result['SupplierType'] = self.supplier_type

        result['SupportAgentList'] = []
        if self.support_agent_list is not None:
            for k1 in self.support_agent_list:
                result['SupportAgentList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('Author') is not None:
            self.author = m.get('Author')

        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EnvVars') is not None:
            self.env_vars = m.get('EnvVars')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('SkillIconUrl') is not None:
            self.skill_icon_url = m.get('SkillIconUrl')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        self.skill_versions = []
        if m.get('SkillVersions') is not None:
            for k1 in m.get('SkillVersions'):
                temp_model = main_models.ListSkillsResponseBodySkillsSkillVersions()
                self.skill_versions.append(temp_model.from_map(k1))

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('SourceMarket') is not None:
            self.source_market = m.get('SourceMarket')

        if m.get('SourceMarketName') is not None:
            self.source_market_name = m.get('SourceMarketName')

        if m.get('SupplierType') is not None:
            self.supplier_type = m.get('SupplierType')

        self.support_agent_list = []
        if m.get('SupportAgentList') is not None:
            for k1 in m.get('SupportAgentList'):
                temp_model = main_models.ListSkillsResponseBodySkillsSupportAgentList()
                self.support_agent_list.append(temp_model.from_map(k1))

        return self

class ListSkillsResponseBodySkillsSupportAgentList(DaraModel):
    def __init__(
        self,
        tag_id: str = None,
        tag_value: str = None,
    ):
        self.tag_id = tag_id
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class ListSkillsResponseBodySkillsSkillVersions(DaraModel):
    def __init__(
        self,
        change_log: str = None,
        created_at: int = None,
        publish_status: str = None,
        security_scan_fail_reason: str = None,
        security_scan_score: int = None,
        security_scan_status: str = None,
        version: str = None,
    ):
        self.change_log = change_log
        self.created_at = created_at
        self.publish_status = publish_status
        self.security_scan_fail_reason = security_scan_fail_reason
        self.security_scan_score = security_scan_score
        self.security_scan_status = security_scan_status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_log is not None:
            result['ChangeLog'] = self.change_log

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        if self.security_scan_fail_reason is not None:
            result['SecurityScanFailReason'] = self.security_scan_fail_reason

        if self.security_scan_score is not None:
            result['SecurityScanScore'] = self.security_scan_score

        if self.security_scan_status is not None:
            result['SecurityScanStatus'] = self.security_scan_status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeLog') is not None:
            self.change_log = m.get('ChangeLog')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        if m.get('SecurityScanFailReason') is not None:
            self.security_scan_fail_reason = m.get('SecurityScanFailReason')

        if m.get('SecurityScanScore') is not None:
            self.security_scan_score = m.get('SecurityScanScore')

        if m.get('SecurityScanStatus') is not None:
            self.security_scan_status = m.get('SecurityScanStatus')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

