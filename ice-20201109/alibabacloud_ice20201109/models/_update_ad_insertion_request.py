# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAdInsertionRequest(DaraModel):
    def __init__(
        self,
        ad_marker_passthrough: str = None,
        ads_url: str = None,
        cdn_ad_segment_url_prefix: str = None,
        cdn_content_segment_url_prefix: str = None,
        config_aliases: str = None,
        content_url_prefix: str = None,
        name: str = None,
        personalization_threshold: int = None,
        slate_ad_url: str = None,
    ):
        # Specifies whether to enable ad marker passthrough. Default value: OFF.
        # 
        # Valid values:
        # 
        # *   OFF: Disable.
        # *   ON: Enable.
        self.ad_marker_passthrough = ad_marker_passthrough
        # The request URL of the ad decision server (ADS). HTTP and HTTPS are supported. The maximum length is 2,048 characters.
        # 
        # This parameter is required.
        self.ads_url = ads_url
        # The CDN prefix for ad segments. HTTP and HTTPS are supported. The maximum length is 512 characters.
        self.cdn_ad_segment_url_prefix = cdn_ad_segment_url_prefix
        # The CDN prefix for content segments. HTTP and HTTPS are supported. The maximum length is 512 characters.
        self.cdn_content_segment_url_prefix = cdn_content_segment_url_prefix
        # A JSON string that specifies the player parameter variables and aliases. Format: { "player_params.{name}": { "{key}": "{value}" } }. You can add up to 20 player_params.{name} entries. The name field can be up to 150 characters in length. Each player parameter can include up to 50 key-value pairs. A key can be up to 150 characters long, and a value can be up to 500 characters.
        self.config_aliases = config_aliases
        # The URL prefix for the source content. HTTP and HTTPS are supported. The maximum length is 512 characters.
        # 
        # This parameter is required.
        self.content_url_prefix = content_url_prefix
        # The configuration name, which cannot be modified.
        # 
        # This parameter is required.
        self.name = name
        # Specifies the maximum duration of underfilled time allowed in an ad break. Unit: seconds. Default value: 8 seconds.
        self.personalization_threshold = personalization_threshold
        # The HTTP or HTTPS URL of the slate ad. Only MP4 format is supported. The maximum length is 2,048 characters.
        self.slate_ad_url = slate_ad_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_marker_passthrough is not None:
            result['AdMarkerPassthrough'] = self.ad_marker_passthrough

        if self.ads_url is not None:
            result['AdsUrl'] = self.ads_url

        if self.cdn_ad_segment_url_prefix is not None:
            result['CdnAdSegmentUrlPrefix'] = self.cdn_ad_segment_url_prefix

        if self.cdn_content_segment_url_prefix is not None:
            result['CdnContentSegmentUrlPrefix'] = self.cdn_content_segment_url_prefix

        if self.config_aliases is not None:
            result['ConfigAliases'] = self.config_aliases

        if self.content_url_prefix is not None:
            result['ContentUrlPrefix'] = self.content_url_prefix

        if self.name is not None:
            result['Name'] = self.name

        if self.personalization_threshold is not None:
            result['PersonalizationThreshold'] = self.personalization_threshold

        if self.slate_ad_url is not None:
            result['SlateAdUrl'] = self.slate_ad_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdMarkerPassthrough') is not None:
            self.ad_marker_passthrough = m.get('AdMarkerPassthrough')

        if m.get('AdsUrl') is not None:
            self.ads_url = m.get('AdsUrl')

        if m.get('CdnAdSegmentUrlPrefix') is not None:
            self.cdn_ad_segment_url_prefix = m.get('CdnAdSegmentUrlPrefix')

        if m.get('CdnContentSegmentUrlPrefix') is not None:
            self.cdn_content_segment_url_prefix = m.get('CdnContentSegmentUrlPrefix')

        if m.get('ConfigAliases') is not None:
            self.config_aliases = m.get('ConfigAliases')

        if m.get('ContentUrlPrefix') is not None:
            self.content_url_prefix = m.get('ContentUrlPrefix')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PersonalizationThreshold') is not None:
            self.personalization_threshold = m.get('PersonalizationThreshold')

        if m.get('SlateAdUrl') is not None:
            self.slate_ad_url = m.get('SlateAdUrl')

        return self

