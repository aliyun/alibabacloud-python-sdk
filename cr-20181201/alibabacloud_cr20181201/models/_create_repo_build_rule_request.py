# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateRepoBuildRuleRequest(DaraModel):
    def __init__(
        self,
        build_args: List[str] = None,
        dockerfile_location: str = None,
        dockerfile_name: str = None,
        image_tag: str = None,
        instance_id: str = None,
        platforms: List[str] = None,
        push_name: str = None,
        push_type: str = None,
        repo_id: str = None,
    ):
        # Building arguments.
        self.build_args = build_args
        # The path of the Dockerfile.
        self.dockerfile_location = dockerfile_location
        # The name of the Dockerfile.
        self.dockerfile_name = dockerfile_name
        # The tag of the image.
        # 
        # This parameter is required.
        self.image_tag = image_tag
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Architecture for image building. Valid values:
        # 
        # *   `linux/amd64`
        # *   `linux/arm64`
        # *   `linux/386`
        # *   `linux/arm/v7`
        # *   `inux/arm/v6`
        # 
        # Default value: `linux/amd64`
        self.platforms = platforms
        # The name of the push that triggers the building rule.
        # 
        # This parameter is required.
        self.push_name = push_name
        # The type of the push that triggers the building rule. Valid values:
        # 
        # *   `GIT_TAG`: tag push
        # *   `GIT_BRANCH`: branch push
        # 
        # This parameter is required.
        self.push_type = push_type
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_args is not None:
            result['BuildArgs'] = self.build_args

        if self.dockerfile_location is not None:
            result['DockerfileLocation'] = self.dockerfile_location

        if self.dockerfile_name is not None:
            result['DockerfileName'] = self.dockerfile_name

        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.platforms is not None:
            result['Platforms'] = self.platforms

        if self.push_name is not None:
            result['PushName'] = self.push_name

        if self.push_type is not None:
            result['PushType'] = self.push_type

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildArgs') is not None:
            self.build_args = m.get('BuildArgs')

        if m.get('DockerfileLocation') is not None:
            self.dockerfile_location = m.get('DockerfileLocation')

        if m.get('DockerfileName') is not None:
            self.dockerfile_name = m.get('DockerfileName')

        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')

        if m.get('PushName') is not None:
            self.push_name = m.get('PushName')

        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        return self

