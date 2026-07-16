# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublicCreateImageScanTaskRequest(DaraModel):
    def __init__(
        self,
        digests: str = None,
        instance_ids: str = None,
        region_ids: str = None,
        registry_types: str = None,
        repo_ids: str = None,
        repo_names: str = None,
        repo_namespaces: str = None,
        source_ip: str = None,
        tags: str = None,
    ):
        # The SHA256 digest values of the images. Separate multiple SHA256 values with commas (,).
        self.digests = digests
        # The IDs of the Container Registry (ACR) instances. Separate multiple IDs with commas (,).
        self.instance_ids = instance_ids
        # The region IDs of the images. Separate multiple region IDs with commas (,).
        self.region_ids = region_ids
        # The types of image registries. Separate multiple types with commas (,). Valid values:
        # 
        # - **acr**
        # - **harbor**
        # - **quay**.
        self.registry_types = registry_types
        # The IDs of the image registries. Separate multiple IDs with commas (,).
        self.repo_ids = repo_ids
        # The names of the image registries. Separate multiple names with commas (,).
        self.repo_names = repo_names
        # The namespaces of the image registries. Separate multiple namespaces with commas (,).
        self.repo_namespaces = repo_namespaces
        # The IP address of the access source.
        self.source_ip = source_ip
        # The tags of the images. Separate multiple tags with commas (,).
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digests is not None:
            result['Digests'] = self.digests

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        if self.registry_types is not None:
            result['RegistryTypes'] = self.registry_types

        if self.repo_ids is not None:
            result['RepoIds'] = self.repo_ids

        if self.repo_names is not None:
            result['RepoNames'] = self.repo_names

        if self.repo_namespaces is not None:
            result['RepoNamespaces'] = self.repo_namespaces

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digests') is not None:
            self.digests = m.get('Digests')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')

        if m.get('RegistryTypes') is not None:
            self.registry_types = m.get('RegistryTypes')

        if m.get('RepoIds') is not None:
            self.repo_ids = m.get('RepoIds')

        if m.get('RepoNames') is not None:
            self.repo_names = m.get('RepoNames')

        if m.get('RepoNamespaces') is not None:
            self.repo_namespaces = m.get('RepoNamespaces')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

