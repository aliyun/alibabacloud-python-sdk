# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRepoTagRequest(DaraModel):
    def __init__(
        self,
        from_tag: str = None,
        instance_id: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        to_tag: str = None,
    ):
        # The source image tag.
        # 
        # This parameter is required.
        self.from_tag = from_tag
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        # 
        # This parameter is required.
        self.namespace_name = namespace_name
        # The name of the image repository.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The image tag that you want to create.
        # 
        # This parameter is required.
        self.to_tag = to_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_tag is not None:
            result['FromTag'] = self.from_tag

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.to_tag is not None:
            result['ToTag'] = self.to_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromTag') is not None:
            self.from_tag = m.get('FromTag')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('ToTag') is not None:
            self.to_tag = m.get('ToTag')

        return self

