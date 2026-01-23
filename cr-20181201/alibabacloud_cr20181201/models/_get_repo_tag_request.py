# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRepoTagRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        tag: str = None,
    ):
        # The return value of status code.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The operation that you want to perform. Set the value to **GetRepoTag**.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The number of milliseconds that have elapsed since the image was created.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

