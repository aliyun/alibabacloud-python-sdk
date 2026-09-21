# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateAgentSkillRequest(DaraModel):
    def __init__(
        self,
        file_list: List[str] = None,
        icon_key: str = None,
        package_oss_key: str = None,
        skill_description: str = None,
        skill_name: str = None,
        skill_package_url: str = None,
    ):
        # The list of files in the skill package.
        self.file_list = file_list
        # The icon of the custom skill.
        self.icon_key = icon_key
        # The OSS path of the skill package. This parameter is reserved by the system and does not need to be specified.
        self.package_oss_key = package_oss_key
        # The skill description.
        self.skill_description = skill_description
        # The skill name.
        self.skill_name = skill_name
        # The OSS download URL of the skill package. This parameter is required for API calls.
        self.skill_package_url = skill_package_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_list is not None:
            result['FileList'] = self.file_list

        if self.icon_key is not None:
            result['IconKey'] = self.icon_key

        if self.package_oss_key is not None:
            result['PackageOssKey'] = self.package_oss_key

        if self.skill_description is not None:
            result['SkillDescription'] = self.skill_description

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.skill_package_url is not None:
            result['SkillPackageUrl'] = self.skill_package_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileList') is not None:
            self.file_list = m.get('FileList')

        if m.get('IconKey') is not None:
            self.icon_key = m.get('IconKey')

        if m.get('PackageOssKey') is not None:
            self.package_oss_key = m.get('PackageOssKey')

        if m.get('SkillDescription') is not None:
            self.skill_description = m.get('SkillDescription')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SkillPackageUrl') is not None:
            self.skill_package_url = m.get('SkillPackageUrl')

        return self

