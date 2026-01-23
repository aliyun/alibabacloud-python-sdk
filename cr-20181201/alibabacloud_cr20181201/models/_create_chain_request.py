# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateChainRequest(DaraModel):
    def __init__(
        self,
        chain_config: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        scope_exclude: List[str] = None,
    ):
        # The configuration of the delivery chain in the JSON format.
        self.chain_config = chain_config
        # The description of the delivery chain.
        self.description = description
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the delivery chain.
        # 
        # This parameter is required.
        self.name = name
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name
        # Repositories in which the delivery chain does not take effect.
        self.scope_exclude = scope_exclude

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chain_config is not None:
            result['ChainConfig'] = self.chain_config

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name

        if self.scope_exclude is not None:
            result['ScopeExclude'] = self.scope_exclude

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainConfig') is not None:
            self.chain_config = m.get('ChainConfig')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')

        if m.get('ScopeExclude') is not None:
            self.scope_exclude = m.get('ScopeExclude')

        return self

