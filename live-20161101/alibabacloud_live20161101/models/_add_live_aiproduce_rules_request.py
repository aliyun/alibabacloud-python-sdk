# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLiveAIProduceRulesRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        description: str = None,
        domain: str = None,
        is_lazy: bool = None,
        live_template: str = None,
        owner_id: int = None,
        region_id: str = None,
        studio_name: str = None,
        subtitle_name: str = None,
        suffix: str = None,
    ):
        # The name of the application to which the live stream belongs. The name can be up to 256 characters in length and can contain digits, letters, hyphens (-), and underscores (_). The name must be the same as the application name in the ingest URL. Otherwise, the rule does not take effect.
        # 
        # This parameter is required.
        self.app = app
        # The description of the subtitle rule. The description can be up to 128 characters in length and can contain letters, digits, and special characters.
        self.description = description
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        # Specifies whether to trigger the subtitle rule when stream pulling starts. Valid values:
        # 
        # *   true: generates live subtitles when stream pulling starts and stops generating live subtitles when no stream is pulled for 5 minutes. When stream pulling restarts, live subtitles are generated again.
        # *   false: generates live subtitles when stream ingest starts, regardless of whether stream pulling starts.
        self.is_lazy = is_lazy
        # The specification of the output subtitles. Valid values:
        # 
        # *   `lp_ld`: landscape low definition 360p (640×360)
        # *   `lp_ld_v`: portrait low definition 360p (360×640)
        # *   `lp_sd`: landscape standard definition 480p (854×480)
        # *   `lp_sd_v`: portrait standard definition 480p (480×854)
        # *   `lp_hd`: landscape high definition 720p (1280×720)
        # *   `lp_hd_v`: portrait high definition 720p (720×1280)
        # *   `lp_ud`: landscape ultra-high definition 1080p (1920×1080)
        # *   `lp_ud_v`: portrait ultra-high definition 1080p (1080×1920)
        # 
        # This parameter is required.
        self.live_template = live_template
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the virtual background template.
        self.studio_name = studio_name
        # The name of the subtitle template.
        self.subtitle_name = subtitle_name
        # The suffix to match.
        self.suffix = suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.description is not None:
            result['Description'] = self.description

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.is_lazy is not None:
            result['IsLazy'] = self.is_lazy

        if self.live_template is not None:
            result['LiveTemplate'] = self.live_template

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.studio_name is not None:
            result['StudioName'] = self.studio_name

        if self.subtitle_name is not None:
            result['SubtitleName'] = self.subtitle_name

        if self.suffix is not None:
            result['Suffix'] = self.suffix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('IsLazy') is not None:
            self.is_lazy = m.get('IsLazy')

        if m.get('LiveTemplate') is not None:
            self.live_template = m.get('LiveTemplate')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StudioName') is not None:
            self.studio_name = m.get('StudioName')

        if m.get('SubtitleName') is not None:
            self.subtitle_name = m.get('SubtitleName')

        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')

        return self

