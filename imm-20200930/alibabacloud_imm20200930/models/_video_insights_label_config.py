# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class VideoInsightsLabelConfig(DaraModel):
    def __init__(
        self,
        highlight: main_models.VideoInsightsHighlightLabelConfig = None,
        system: main_models.VideoInsightsSystemLabelConfig = None,
        user_defined: main_models.VideoInsightsUserDefinedLabelConfig = None,
    ):
        self.highlight = highlight
        self.system = system
        self.user_defined = user_defined

    def validate(self):
        if self.highlight:
            self.highlight.validate()
        if self.system:
            self.system.validate()
        if self.user_defined:
            self.user_defined.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.highlight is not None:
            result['Highlight'] = self.highlight.to_map()

        if self.system is not None:
            result['System'] = self.system.to_map()

        if self.user_defined is not None:
            result['UserDefined'] = self.user_defined.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Highlight') is not None:
            temp_model = main_models.VideoInsightsHighlightLabelConfig()
            self.highlight = temp_model.from_map(m.get('Highlight'))

        if m.get('System') is not None:
            temp_model = main_models.VideoInsightsSystemLabelConfig()
            self.system = temp_model.from_map(m.get('System'))

        if m.get('UserDefined') is not None:
            temp_model = main_models.VideoInsightsUserDefinedLabelConfig()
            self.user_defined = temp_model.from_map(m.get('UserDefined'))

        return self

