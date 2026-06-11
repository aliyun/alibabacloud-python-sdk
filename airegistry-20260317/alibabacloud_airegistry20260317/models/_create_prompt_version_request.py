# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePromptVersionRequest(DaraModel):
    def __init__(
        self,
        based_on_version: str = None,
        commit_msg: str = None,
        namespace_id: str = None,
        prompt_key: str = None,
        target_version: str = None,
        template: str = None,
        variables: str = None,
    ):
        self.based_on_version = based_on_version
        self.commit_msg = commit_msg
        # This parameter is required.
        self.namespace_id = namespace_id
        # This parameter is required.
        self.prompt_key = prompt_key
        self.target_version = target_version
        self.template = template
        self.variables = variables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.based_on_version is not None:
            result['BasedOnVersion'] = self.based_on_version

        if self.commit_msg is not None:
            result['CommitMsg'] = self.commit_msg

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.prompt_key is not None:
            result['PromptKey'] = self.prompt_key

        if self.target_version is not None:
            result['TargetVersion'] = self.target_version

        if self.template is not None:
            result['Template'] = self.template

        if self.variables is not None:
            result['Variables'] = self.variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasedOnVersion') is not None:
            self.based_on_version = m.get('BasedOnVersion')

        if m.get('CommitMsg') is not None:
            self.commit_msg = m.get('CommitMsg')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PromptKey') is not None:
            self.prompt_key = m.get('PromptKey')

        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Variables') is not None:
            self.variables = m.get('Variables')

        return self

