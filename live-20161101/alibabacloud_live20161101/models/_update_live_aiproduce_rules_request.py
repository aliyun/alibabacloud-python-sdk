# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveAIProduceRulesRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        description: str = None,
        domain: str = None,
        is_lazy: bool = None,
        live_template: str = None,
        owner_id: int = None,
        region_id: str = None,
        rules_id: str = None,
        studio_name: str = None,
        subtitle_id: str = None,
        subtitle_name: str = None,
        suffix: str = None,
    ):
        # The name of the live stream application.
        # 
        # This parameter is required.
        self.app = app
        # The description of the subtitle rule. The description can contain letters, digits, Chinese characters, and special characters, and can be up to 128 characters in length.
        self.description = description
        # The primary streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        # Specifies whether subtitles are triggered by stream pulling. Valid values:
        # - true: Subtitles start when a stream is pulled. If no stream is pulled within 5 minutes, the subtitles stop. Subtitles restart when a stream is pulled again.
        # - false: Subtitles start as long as stream ingest is active, regardless of whether a stream is being pulled.
        self.is_lazy = is_lazy
        # The output specification of the subtitle. Valid values:
        # - Landscape low definition 360P 640 × 360: `lp_ld`
        # - Portrait low definition 360P 360 × 640: `lp_ld_v`
        # - Landscape standard definition 480P 854 × 480: `lp_sd`
        # - Portrait standard definition 480P 480 × 854: `lp_sd_v`
        # - Landscape high definition 720P 1280 × 720: `lp_hd`
        # - Portrait high definition 720P 720 × 1280: `lp_hd_v`
        # - Landscape ultra-high definition 1080P 1920 × 1080: `lp_ud`
        # - Portrait ultra-high definition 1080P 1080 × 1920: `lp_ud_v`
        self.live_template = live_template
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The ID of the subtitle rule.
        self.rules_id = rules_id
        # The name of the virtual background template. You must specify at least one of SubtitleName and StudioName. Otherwise, a MissingParameter error is returned.
        self.studio_name = studio_name
        # The ID of the subtitle template.
        self.subtitle_id = subtitle_id
        # The name of the subtitle template. You must specify at least one of SubtitleName and StudioName. Otherwise, a MissingParameter error is returned.
        self.subtitle_name = subtitle_name
        # The suffix match.
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

        if self.rules_id is not None:
            result['RulesId'] = self.rules_id

        if self.studio_name is not None:
            result['StudioName'] = self.studio_name

        if self.subtitle_id is not None:
            result['SubtitleId'] = self.subtitle_id

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

        if m.get('RulesId') is not None:
            self.rules_id = m.get('RulesId')

        if m.get('StudioName') is not None:
            self.studio_name = m.get('StudioName')

        if m.get('SubtitleId') is not None:
            self.subtitle_id = m.get('SubtitleId')

        if m.get('SubtitleName') is not None:
            self.subtitle_name = m.get('SubtitleName')

        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')

        return self

