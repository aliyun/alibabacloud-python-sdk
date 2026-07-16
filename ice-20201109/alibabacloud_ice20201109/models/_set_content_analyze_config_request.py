# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetContentAnalyzeConfigRequest(DaraModel):
    def __init__(
        self,
        auto: bool = None,
        save_type: str = None,
        template_id: str = None,
    ):
        # Specifies whether to automatically start Intelligent Content Analysis after a Media Asset is registered.
        # 
        # Valid values:
        # 
        # - true: Enable
        # 
        # - false: Disable (Default)
        self.auto = auto
        # The storage type for analysis results. This parameter applies only when Auto is set to true. Default: Empty.
        # 
        # - TEXT: Label
        # 
        # - FACE: Face
        # 
        # - DNA: Similar Image
        # 
        # You can specify multiple values separated by commas. If this parameter is empty, Intelligent Content Analysis results are not saved to any search library, and you cannot perform content searches.
        self.save_type = save_type
        # The ID of the Intelligent Content Analysis Template. Each Template includes the following AI analysis features:
        # 
        # - S00000101-100040: Text Recognition
        # 
        # - S00000101-100060: Video Categorization and Face Recognition
        # 
        # - S00000101-100070: Text Recognition, Video Categorization, and Face Recognition
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto is not None:
            result['Auto'] = self.auto

        if self.save_type is not None:
            result['SaveType'] = self.save_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')

        if m.get('SaveType') is not None:
            self.save_type = m.get('SaveType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

