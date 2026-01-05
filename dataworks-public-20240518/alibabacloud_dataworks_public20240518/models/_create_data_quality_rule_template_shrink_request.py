# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataQualityRuleTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        checking_config_shrink: str = None,
        directory_path: str = None,
        name: str = None,
        project_id: int = None,
        sampling_config_shrink: str = None,
        visible_scope: str = None,
    ):
        # The check settings for sample data.
        self.checking_config_shrink = checking_config_shrink
        # The directory in which the template is stored. Slashes (/) are used to separate directory levels. The name of each directory level can be up to 1,024 characters in length. It cannot contain whitespace characters or slashes (/).
        self.directory_path = directory_path
        # The name of the template. The name can be up to 512 characters in length and can contain digits, letters, and punctuation marks.
        # 
        # This parameter is required.
        self.name = name
        # The DataWorks workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The sampling settings.
        self.sampling_config_shrink = sampling_config_shrink
        # The applicable scope of the template. Valid values:
        # 
        # *   Tenant: The template is available in all workspaces in the current tenant.
        # *   Project: The template is available only in the current workspace.
        self.visible_scope = visible_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_config_shrink is not None:
            result['CheckingConfig'] = self.checking_config_shrink

        if self.directory_path is not None:
            result['DirectoryPath'] = self.directory_path

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sampling_config_shrink is not None:
            result['SamplingConfig'] = self.sampling_config_shrink

        if self.visible_scope is not None:
            result['VisibleScope'] = self.visible_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingConfig') is not None:
            self.checking_config_shrink = m.get('CheckingConfig')

        if m.get('DirectoryPath') is not None:
            self.directory_path = m.get('DirectoryPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SamplingConfig') is not None:
            self.sampling_config_shrink = m.get('SamplingConfig')

        if m.get('VisibleScope') is not None:
            self.visible_scope = m.get('VisibleScope')

        return self

