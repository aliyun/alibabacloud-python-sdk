# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListAdInsertionsResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListAdInsertionsResponseBodyConfigs] = None,
        max_results: int = None,
        next_token: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        sort_by: str = None,
        total_count: int = None,
    ):
        # Array
        self.configs = configs
        # The maximum number of entries to retrieve in a subsequent request. If this parameter is used, the pagination parameters become invalid.
        self.max_results = max_results
        # The token that is used in the next request to retrieve a new page of results. If this parameter is used, the pagination parameters become invalid.
        self.next_token = next_token
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The sorting order of the configurations by creation time. asc: ascending. desc: descending.
        self.sort_by = sort_by
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.ListAdInsertionsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAdInsertionsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        ad_marker_passthrough: str = None,
        ads_url: str = None,
        cdn_config: main_models.ListAdInsertionsResponseBodyConfigsCdnConfig = None,
        config_aliases: str = None,
        content_url_prefix: str = None,
        create_time: str = None,
        last_modified: str = None,
        manifest_endpoint_config: main_models.ListAdInsertionsResponseBodyConfigsManifestEndpointConfig = None,
        name: str = None,
        personalization_threshold: int = None,
        slate_ad_url: str = None,
    ):
        # Indicates whether ad marker passthrough is enabled.
        self.ad_marker_passthrough = ad_marker_passthrough
        # The request URL of the ad decision server (ADS).
        self.ads_url = ads_url
        # The CDN configurations.
        self.cdn_config = cdn_config
        # The player parameter variables and aliases.
        self.config_aliases = config_aliases
        # The URL prefix for the source content.
        self.content_url_prefix = content_url_prefix
        # The time when the configuration was created.
        self.create_time = create_time
        # The time when the configuration was last modified.
        self.last_modified = last_modified
        # The playback endpoint configuration.
        self.manifest_endpoint_config = manifest_endpoint_config
        # The name of the ad insertion configuration.
        self.name = name
        # The personalization threshold that defines the maximum duration of underfilled time allowed in an ad break.
        self.personalization_threshold = personalization_threshold
        # The URL of the slate ad.
        self.slate_ad_url = slate_ad_url

    def validate(self):
        if self.cdn_config:
            self.cdn_config.validate()
        if self.manifest_endpoint_config:
            self.manifest_endpoint_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_marker_passthrough is not None:
            result['AdMarkerPassthrough'] = self.ad_marker_passthrough

        if self.ads_url is not None:
            result['AdsUrl'] = self.ads_url

        if self.cdn_config is not None:
            result['CdnConfig'] = self.cdn_config.to_map()

        if self.config_aliases is not None:
            result['ConfigAliases'] = self.config_aliases

        if self.content_url_prefix is not None:
            result['ContentUrlPrefix'] = self.content_url_prefix

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.manifest_endpoint_config is not None:
            result['ManifestEndpointConfig'] = self.manifest_endpoint_config.to_map()

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

        if m.get('CdnConfig') is not None:
            temp_model = main_models.ListAdInsertionsResponseBodyConfigsCdnConfig()
            self.cdn_config = temp_model.from_map(m.get('CdnConfig'))

        if m.get('ConfigAliases') is not None:
            self.config_aliases = m.get('ConfigAliases')

        if m.get('ContentUrlPrefix') is not None:
            self.content_url_prefix = m.get('ContentUrlPrefix')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('ManifestEndpointConfig') is not None:
            temp_model = main_models.ListAdInsertionsResponseBodyConfigsManifestEndpointConfig()
            self.manifest_endpoint_config = temp_model.from_map(m.get('ManifestEndpointConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PersonalizationThreshold') is not None:
            self.personalization_threshold = m.get('PersonalizationThreshold')

        if m.get('SlateAdUrl') is not None:
            self.slate_ad_url = m.get('SlateAdUrl')

        return self

class ListAdInsertionsResponseBodyConfigsManifestEndpointConfig(DaraModel):
    def __init__(
        self,
        dash_prefix: str = None,
        hls_prefix: str = None,
    ):
        # DASH清单播放端点前缀
        self.dash_prefix = dash_prefix
        # The prefix of the playback endpoint for HLS manifests.
        self.hls_prefix = hls_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dash_prefix is not None:
            result['DashPrefix'] = self.dash_prefix

        if self.hls_prefix is not None:
            result['HlsPrefix'] = self.hls_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashPrefix') is not None:
            self.dash_prefix = m.get('DashPrefix')

        if m.get('HlsPrefix') is not None:
            self.hls_prefix = m.get('HlsPrefix')

        return self

class ListAdInsertionsResponseBodyConfigsCdnConfig(DaraModel):
    def __init__(
        self,
        ad_segment_url_prefix: str = None,
        content_segment_url_prefix: str = None,
    ):
        # The CDN prefix for ad segments.
        self.ad_segment_url_prefix = ad_segment_url_prefix
        # The CDN prefix for content segments.
        self.content_segment_url_prefix = content_segment_url_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_segment_url_prefix is not None:
            result['AdSegmentUrlPrefix'] = self.ad_segment_url_prefix

        if self.content_segment_url_prefix is not None:
            result['ContentSegmentUrlPrefix'] = self.content_segment_url_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdSegmentUrlPrefix') is not None:
            self.ad_segment_url_prefix = m.get('AdSegmentUrlPrefix')

        if m.get('ContentSegmentUrlPrefix') is not None:
            self.content_segment_url_prefix = m.get('ContentSegmentUrlPrefix')

        return self

