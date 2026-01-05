# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataQualityRuleTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        checking_config_shrink: str = None,
        code: str = None,
        directory_path: str = None,
        name: str = None,
        project_id: int = None,
        sampling_config_shrink: str = None,
    ):
        # The check settings for sample data.
        self.checking_config_shrink = checking_config_shrink
        # The code for the template.
        # 
        # This parameter is required.
        self.code = code
        # The directory in which the template is stored. Slashes (/) are used to separate directory levels. The name of each directory level can be up to 1,024 characters in length. It cannot contain whitespace characters or slashes (/).
        self.directory_path = directory_path
        # The name of the template. The name can be up to 512 characters in length and can contain digits, letters, and punctuation marks.
        self.name = name
        # This parameter is required.
        self.project_id = project_id
        # The sampling settings.
        self.sampling_config_shrink = sampling_config_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_config_shrink is not None:
            result['CheckingConfig'] = self.checking_config_shrink

        if self.code is not None:
            result['Code'] = self.code

        if self.directory_path is not None:
            result['DirectoryPath'] = self.directory_path

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sampling_config_shrink is not None:
            result['SamplingConfig'] = self.sampling_config_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingConfig') is not None:
            self.checking_config_shrink = m.get('CheckingConfig')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DirectoryPath') is not None:
            self.directory_path = m.get('DirectoryPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SamplingConfig') is not None:
            self.sampling_config_shrink = m.get('SamplingConfig')

        return self

