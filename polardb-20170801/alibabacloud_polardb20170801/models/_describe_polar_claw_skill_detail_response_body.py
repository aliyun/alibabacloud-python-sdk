# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarClawSkillDetailResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        latest_version: main_models.DescribePolarClawSkillDetailResponseBodyLatestVersion = None,
        message: str = None,
        owner: main_models.DescribePolarClawSkillDetailResponseBodyOwner = None,
        request_id: str = None,
        skill: main_models.DescribePolarClawSkillDetailResponseBodySkill = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The latest version information.
        self.latest_version = latest_version
        # The response message.
        self.message = message
        # The Skill author information.
        self.owner = owner
        # Id of the request
        self.request_id = request_id
        # The core information of the Skill.
        self.skill = skill

    def validate(self):
        if self.latest_version:
            self.latest_version.validate()
        if self.owner:
            self.owner.validate()
        if self.skill:
            self.skill.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.owner is not None:
            result['Owner'] = self.owner.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skill is not None:
            result['Skill'] = self.skill.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('LatestVersion') is not None:
            temp_model = main_models.DescribePolarClawSkillDetailResponseBodyLatestVersion()
            self.latest_version = temp_model.from_map(m.get('LatestVersion'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Owner') is not None:
            temp_model = main_models.DescribePolarClawSkillDetailResponseBodyOwner()
            self.owner = temp_model.from_map(m.get('Owner'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Skill') is not None:
            temp_model = main_models.DescribePolarClawSkillDetailResponseBodySkill()
            self.skill = temp_model.from_map(m.get('Skill'))

        return self

class DescribePolarClawSkillDetailResponseBodySkill(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        display_name: str = None,
        slug: str = None,
        stats: main_models.DescribePolarClawSkillDetailResponseBodySkillStats = None,
        summary: str = None,
        tags: Dict[str, Any] = None,
        updated_at: int = None,
    ):
        # The first publish timestamp in Unix milliseconds.
        self.created_at = created_at
        # The display name.
        self.display_name = display_name
        # The Skill identifier.
        self.slug = slug
        # The statistics information.
        self.stats = stats
        # The brief description.
        self.summary = summary
        # The tag key-value pairs.
        self.tags = tags
        # The last update timestamp in Unix milliseconds.
        self.updated_at = updated_at

    def validate(self):
        if self.stats:
            self.stats.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.stats is not None:
            result['Stats'] = self.stats.to_map()

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('Stats') is not None:
            temp_model = main_models.DescribePolarClawSkillDetailResponseBodySkillStats()
            self.stats = temp_model.from_map(m.get('Stats'))

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

class DescribePolarClawSkillDetailResponseBodySkillStats(DaraModel):
    def __init__(
        self,
        comments: int = None,
        downloads: int = None,
        installs_all_time: int = None,
        installs_current: int = None,
        stars: int = None,
        versions: int = None,
    ):
        # The number of comments.
        self.comments = comments
        # The number of downloads.
        self.downloads = downloads
        # The total number of installations of all time.
        self.installs_all_time = installs_all_time
        # The current number of installations.
        self.installs_current = installs_current
        # The number of stars.
        self.stars = stars
        # The number of versions.
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.downloads is not None:
            result['Downloads'] = self.downloads

        if self.installs_all_time is not None:
            result['InstallsAllTime'] = self.installs_all_time

        if self.installs_current is not None:
            result['InstallsCurrent'] = self.installs_current

        if self.stars is not None:
            result['Stars'] = self.stars

        if self.versions is not None:
            result['Versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('Downloads') is not None:
            self.downloads = m.get('Downloads')

        if m.get('InstallsAllTime') is not None:
            self.installs_all_time = m.get('InstallsAllTime')

        if m.get('InstallsCurrent') is not None:
            self.installs_current = m.get('InstallsCurrent')

        if m.get('Stars') is not None:
            self.stars = m.get('Stars')

        if m.get('Versions') is not None:
            self.versions = m.get('Versions')

        return self

class DescribePolarClawSkillDetailResponseBodyOwner(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        handle: str = None,
        image: str = None,
        user_id: str = None,
    ):
        # The display name of the author.
        self.display_name = display_name
        # The account identifier of the author.
        self.handle = handle
        # The profile picture URL.
        self.image = image
        # The user ID of the author.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.handle is not None:
            result['Handle'] = self.handle

        if self.image is not None:
            result['Image'] = self.image

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Handle') is not None:
            self.handle = m.get('Handle')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribePolarClawSkillDetailResponseBodyLatestVersion(DaraModel):
    def __init__(
        self,
        changelog: str = None,
        created_at: int = None,
        version: str = None,
    ):
        # The version changelog.
        self.changelog = changelog
        # The version publish timestamp in Unix milliseconds.
        self.created_at = created_at
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changelog is not None:
            result['Changelog'] = self.changelog

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Changelog') is not None:
            self.changelog = m.get('Changelog')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

