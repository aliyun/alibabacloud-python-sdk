# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class Artifact(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        name: str = None,
        type: str = None,
        versions: List[main_models.ArtifactVersions] = None,
    ):
        # The creation time.
        self.created_at = created_at
        # The artifact name.
        self.name = name
        # The artifact type.
        self.type = type
        # The version list.
        self.versions = versions

    def validate(self):
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        result['Versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['Versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.versions = []
        if m.get('Versions') is not None:
            for k1 in m.get('Versions'):
                temp_model = main_models.ArtifactVersions()
                self.versions.append(temp_model.from_map(k1))

        return self



class ArtifactVersions(DaraModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
        release_name: str = None,
        version: str = None,
    ):
        # The version alias.
        self.alias = alias
        # The template description associated with the version.
        self.description = description
        # The version name.
        self.release_name = release_name
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.description is not None:
            result['Description'] = self.description

        if self.release_name is not None:
            result['ReleaseName'] = self.release_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ReleaseName') is not None:
            self.release_name = m.get('ReleaseName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

