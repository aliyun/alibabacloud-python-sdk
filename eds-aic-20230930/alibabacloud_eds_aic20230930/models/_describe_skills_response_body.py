# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeSkillsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        skill_info: List[main_models.DescribeSkillsResponseBodySkillInfo] = None,
        total_count: str = None,
    ):
        # The status code. A value of 200 indicates success.
        self.code = code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The skill information.
        self.skill_info = skill_info
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.skill_info:
            for v1 in self.skill_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SkillInfo'] = []
        if self.skill_info is not None:
            for k1 in self.skill_info:
                result['SkillInfo'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.skill_info = []
        if m.get('SkillInfo') is not None:
            for k1 in m.get('SkillInfo'):
                temp_model = main_models.DescribeSkillsResponseBodySkillInfo()
                self.skill_info.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSkillsResponseBodySkillInfo(DaraModel):
    def __init__(
        self,
        category: str = None,
        create_time: str = None,
        description: str = None,
        icon_oss_url: str = None,
        installed_count: int = None,
        installed_instances: List[main_models.DescribeSkillsResponseBodySkillInfoInstalledInstances] = None,
        instruction: str = None,
        skill_id: str = None,
        skill_name: str = None,
        skill_source: str = None,
        skill_status: str = None,
        source_instance_id: str = None,
        status: str = None,
        type: str = None,
        version: str = None,
    ):
        # The skill category.
        self.category = category
        # The creation time.
        self.create_time = create_time
        # The skill description.
        self.description = description
        # The OSS download URL of the skill icon.
        self.icon_oss_url = icon_oss_url
        # The number of instances that have the skill installed.
        self.installed_count = installed_count
        # The information about the installed instances.
        self.installed_instances = installed_instances
        # The skill summary.
        self.instruction = instruction
        # The skill ID.
        self.skill_id = skill_id
        # The skill name.
        self.skill_name = skill_name
        # The skill source.
        self.skill_source = skill_source
        # The skill lifecycle status.
        self.skill_status = skill_status
        # The source node ID of the skill created from a conversation. This value is empty for user-uploaded skills.
        self.source_instance_id = source_instance_id
        # The skill status.
        self.status = status
        # The skill type.
        self.type = type
        # The skill version.
        self.version = version

    def validate(self):
        if self.installed_instances:
            for v1 in self.installed_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.icon_oss_url is not None:
            result['IconOssUrl'] = self.icon_oss_url

        if self.installed_count is not None:
            result['InstalledCount'] = self.installed_count

        result['InstalledInstances'] = []
        if self.installed_instances is not None:
            for k1 in self.installed_instances:
                result['InstalledInstances'].append(k1.to_map() if k1 else None)

        if self.instruction is not None:
            result['Instruction'] = self.instruction

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.skill_source is not None:
            result['SkillSource'] = self.skill_source

        if self.skill_status is not None:
            result['SkillStatus'] = self.skill_status

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IconOssUrl') is not None:
            self.icon_oss_url = m.get('IconOssUrl')

        if m.get('InstalledCount') is not None:
            self.installed_count = m.get('InstalledCount')

        self.installed_instances = []
        if m.get('InstalledInstances') is not None:
            for k1 in m.get('InstalledInstances'):
                temp_model = main_models.DescribeSkillsResponseBodySkillInfoInstalledInstances()
                self.installed_instances.append(temp_model.from_map(k1))

        if m.get('Instruction') is not None:
            self.instruction = m.get('Instruction')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SkillSource') is not None:
            self.skill_source = m.get('SkillSource')

        if m.get('SkillStatus') is not None:
            self.skill_status = m.get('SkillStatus')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeSkillsResponseBodySkillInfoInstalledInstances(DaraModel):
    def __init__(
        self,
        install_status: str = None,
        instance_id: str = None,
    ):
        # The installation status.
        self.install_status = install_status
        # The cloud phone instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.install_status is not None:
            result['InstallStatus'] = self.install_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstallStatus') is not None:
            self.install_status = m.get('InstallStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

