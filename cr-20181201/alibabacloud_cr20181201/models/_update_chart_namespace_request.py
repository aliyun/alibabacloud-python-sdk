# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateChartNamespaceRequest(DaraModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        # Specifies whether to automatically create repositories in the namespace. Valid values:
        # 
        # *   `true`: automatically creates repositories in the namespace.
        # *   `false`: does not automatically create repositories in the namespace.
        self.auto_create_repo = auto_create_repo
        # The default type of the repository. Valid values:
        # 
        # *   `PUBLIC`: a public repository
        # *   `PRIVATE`: a private repository
        self.default_repo_type = default_repo_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace to which the repository belongs.
        # 
        # This parameter is required.
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo

        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')

        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        return self

