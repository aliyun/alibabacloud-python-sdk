# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSceneBatchEditingJobRequest(DaraModel):
    def __init__(
        self,
        output_config: str = None,
        project_ids: str = None,
        user_data: str = None,
    ):
        # The output configuration. The structure is the same as the [OutputConfig](https://help.aliyun.com/zh/ims/use-cases/create-highlight-videos?spm=a2c4g.11186623.help-menu-193643.d_3_2_0_3.3af86997GreVu9\\&scm=20140722.H_2863940._.OR_help-T_cn~zh-V_1#4111a373d0xbz) for batch video generation, except that Count and GeneratePreviewOnly are not supported.
        # 
        # This parameter is required.
        self.output_config = output_config
        # A comma-separated list of editing project IDs. The video is rendered based on the timeline from each project.
        # 
        # This parameter is required.
        self.project_ids = project_ids
        # Custom user data, including callback configurations. For more information, see [UserData](~~357745#section-urj-v3f-0s1~~).
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

