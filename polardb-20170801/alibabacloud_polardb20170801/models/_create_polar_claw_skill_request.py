# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolarClawSkillRequest(DaraModel):
    def __init__(
        self,
        bucket_region_id: str = None,
        bucket_type: str = None,
        ossbucket: str = None,
        ossprefix: str = None,
        region_id: str = None,
        skill_name: str = None,
        skill_version: str = None,
        summary: str = None,
        tags: str = None,
        title: str = None,
    ):
        self.bucket_region_id = bucket_region_id
        self.bucket_type = bucket_type
        # This parameter is required.
        self.ossbucket = ossbucket
        # This parameter is required.
        self.ossprefix = ossprefix
        self.region_id = region_id
        # This parameter is required.
        self.skill_name = skill_name
        # This parameter is required.
        self.skill_version = skill_version
        self.summary = summary
        self.tags = tags
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_region_id is not None:
            result['BucketRegionId'] = self.bucket_region_id

        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type

        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.ossprefix is not None:
            result['OSSPrefix'] = self.ossprefix

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.skill_version is not None:
            result['SkillVersion'] = self.skill_version

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketRegionId') is not None:
            self.bucket_region_id = m.get('BucketRegionId')

        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')

        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('OSSPrefix') is not None:
            self.ossprefix = m.get('OSSPrefix')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SkillVersion') is not None:
            self.skill_version = m.get('SkillVersion')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

