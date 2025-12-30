# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSceneMediaSelectionJobRequest(DaraModel):
    def __init__(
        self,
        editing_config: str = None,
        input_config: str = None,
        job_type: str = None,
        output_config: str = None,
        user_data: str = None,
    ):
        # The editing configuration. Its structure depends on the value of JobType.
        # 
        # *   When JobType is set to Smart_Mix_Media_Select, see [Image-text matching](https://help.aliyun.com/zh/ims/use-cases/intelligent-graphic-matching-into-a-piece/?spm=a2c4g.11186623.help-menu-193643.d_3_2_0_1.7c3d6997qndkZj).
        # *   When JobType is set to Screen_Media_Highlights_Media_Select, see [Highlight mashup](https://help.aliyun.com/zh/ims/use-cases/create-highlight-videos?spm=a2c4g.11186623.help-menu-193643.d_3_2_0_3.84b5661bIcQULE).
        self.editing_config = editing_config
        # The input configuration. Its structure and required fields depend on the value of JobType.
        # 
        # *   When JobType is set to Smart_Mix_Media_Select, see [Image-text matching](https://help.aliyun.com/zh/ims/use-cases/intelligent-graphic-matching-into-a-piece/?spm=a2c4g.11186623.help-menu-193643.d_3_2_0_1.7c3d6997qndkZj).
        # *   When JobType is set to Screen_Media_Highlights_Media_Select, see [Highlight mashup](https://help.aliyun.com/zh/ims/use-cases/create-highlight-videos?spm=a2c4g.11186623.help-menu-193643.d_3_2_0_3.84b5661bIcQULE).
        # 
        # This parameter is required.
        self.input_config = input_config
        # The job type. Valid values:
        # 
        # *   Smart_Mix_Media_Select
        # *   Screen_Media_Highlights_Media_Select
        # 
        # Differences:
        # 
        # *   Smart_Mix_Media_Select: Matches voiceover scripts with provided video/image materials to select the most relevant clips and returns the matching results. Two options are available: Common mode, which is suitable for general-purpose materials like lifestyle vlogs, travel videos, and marketing content; Movie collections, which is optimized for materials with a coherent plot and specific characters, such as TV series and movies.
        # *   Screen_Media_Highlights_Media_Select: Automatically identifies and selects clips that are exciting or represent key story points from longer video materials.
        # 
        # This parameter is required.
        self.job_type = job_type
        # The output configuration. Its structure and required fields depend on the value of JobType.
        # 
        # *   When JobType is set to Smart_Mix_Media_Select, see [Image-text matching](https://help.aliyun.com/zh/ims/use-cases/intelligent-graphic-matching-into-a-piece/?spm=a2c4g.11186623.help-menu-193643.d_3_2_0_1.7c3d6997qndkZj).
        # *   When JobType is set to Screen_Media_Highlights_Media_Select, see [Highlight mashup](https://help.aliyun.com/zh/ims/use-cases/create-highlight-videos?spm=a2c4g.11186623.help-menu-193643.d_3_2_0_3.84b5661bIcQULE).
        # 
        # This parameter is required.
        self.output_config = output_config
        # The user-defined data, including the business and callback configurations. For more information, see [UserData](~~357745#section-urj-v3f-0s1~~).
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config

        if self.input_config is not None:
            result['InputConfig'] = self.input_config

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')

        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

