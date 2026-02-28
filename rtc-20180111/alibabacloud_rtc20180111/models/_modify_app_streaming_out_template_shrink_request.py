# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAppStreamingOutTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        streaming_out_template_shrink: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.streaming_out_template_shrink = streaming_out_template_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.streaming_out_template_shrink is not None:
            result['StreamingOutTemplate'] = self.streaming_out_template_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('StreamingOutTemplate') is not None:
            self.streaming_out_template_shrink = m.get('StreamingOutTemplate')

        return self

