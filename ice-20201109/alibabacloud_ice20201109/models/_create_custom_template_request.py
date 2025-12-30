# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomTemplateRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        subtype: int = None,
        template_config: str = None,
        type: int = None,
    ):
        # The template name.
        # 
        # This parameter is required.
        self.name = name
        # The template subtype.
        # 
        # Valid values for transcoding templates:
        # 
        # *   1 (Normal): regular template.
        # *   2 (AudioTranscode): audio transcoding template.
        # *   3 (Remux): container format conversion template.
        # *   4 (NarrowBandV1): Narrowband HD 1.0 template.
        # *   5 (NarrowBandV2): Narrowband HD 2.0 template.
        # 
        # Valid values for snapshot templates:
        # 
        # *   1 (Normal): regular template.
        # *   2 (Sprite): sprite template.
        # *   3 (WebVtt): WebVTT template.
        # 
        # Valid values for AI-assisted content moderation templates:
        # 
        # *   1 (Video): video moderation template.
        # *   2 (Audio): audio moderation template.
        # *   3 (Image): image moderation template.
        # 
        # Valid values for AI-assisted intelligent erasure templates.
        # 
        # *   1 (VideoDelogo): logo erasure template.
        # *   2 (VideoDetext): subtitle erasure template.
        self.subtype = subtype
        # The template configurations. For more information, see [Template parameters](https://help.aliyun.com/document_detail/448291.html).
        # 
        # This parameter is required.
        self.template_config = template_config
        # The template type. Valid values:
        # 
        # *   1: transcoding template.
        # *   2: snapshot template.
        # *   3: animated image template.
        # *   4\\. image watermark template.
        # *   5: text watermark template.
        # *   6: subtitle template.
        # *   7: AI-assisted content moderation template.
        # *   8: AI-assisted intelligent thumbnail template.
        # *   9: AI-assisted intelligent erasure template.
        # *   10: AI-assisted media fingerprint analysis template.
        # *   11: AI-assisted smart tagging template.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.subtype is not None:
            result['Subtype'] = self.subtype

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Subtype') is not None:
            self.subtype = m.get('Subtype')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

