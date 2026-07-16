# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListSiteFunctionsResponseBody(DaraModel):
    def __init__(
        self,
        configs: main_models.ListSiteFunctionsResponseBodyConfigs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The configuration information.
        self.configs = configs
        # The current page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.configs:
            self.configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configs is not None:
            result['Configs'] = self.configs.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            temp_model = main_models.ListSiteFunctionsResponseBodyConfigs()
            self.configs = temp_model.from_map(m.get('Configs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListSiteFunctionsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        cache_reserve: List[main_models.ListSiteFunctionsResponseBodyConfigsCacheReserve] = None,
        cache_rules: List[main_models.ListSiteFunctionsResponseBodyConfigsCacheRules] = None,
        cache_tags: List[main_models.ListSiteFunctionsResponseBodyConfigsCacheTags] = None,
        cname_flattening: List[main_models.ListSiteFunctionsResponseBodyConfigsCnameFlattening] = None,
        compression_rules: List[main_models.ListSiteFunctionsResponseBodyConfigsCompressionRules] = None,
        cross_border_optimization: List[main_models.ListSiteFunctionsResponseBodyConfigsCrossBorderOptimization] = None,
        custom_response_code: List[main_models.ListSiteFunctionsResponseBodyConfigsCustomResponseCode] = None,
        development_mode: List[main_models.ListSiteFunctionsResponseBodyConfigsDevelopmentMode] = None,
        error_pages_redirects: List[main_models.ListSiteFunctionsResponseBodyConfigsErrorPagesRedirects] = None,
        http_incoming_request_header_modification_rules: List[main_models.ListSiteFunctionsResponseBodyConfigsHttpIncomingRequestHeaderModificationRules] = None,
        http_incoming_response_header_modification_rules: List[main_models.ListSiteFunctionsResponseBodyConfigsHttpIncomingResponseHeaderModificationRules] = None,
        http_request_header_modification_rules: List[main_models.ListSiteFunctionsResponseBodyConfigsHttpRequestHeaderModificationRules] = None,
        http_response_header_modification_rules: List[main_models.ListSiteFunctionsResponseBodyConfigsHttpResponseHeaderModificationRules] = None,
        https_application_configuration: List[main_models.ListSiteFunctionsResponseBodyConfigsHttpsApplicationConfiguration] = None,
        https_basic_configuration: List[main_models.ListSiteFunctionsResponseBodyConfigsHttpsBasicConfiguration] = None,
        image_transform: List[main_models.ListSiteFunctionsResponseBodyConfigsImageTransform] = None,
        ipv_6: List[main_models.ListSiteFunctionsResponseBodyConfigsIpv6] = None,
        managed_transforms: List[main_models.ListSiteFunctionsResponseBodyConfigsManagedTransforms] = None,
        network_optimization: List[main_models.ListSiteFunctionsResponseBodyConfigsNetworkOptimization] = None,
        origin_rules: List[main_models.ListSiteFunctionsResponseBodyConfigsOriginRules] = None,
        redirect_rules: List[main_models.ListSiteFunctionsResponseBodyConfigsRedirectRules] = None,
        rewrite_url_rules: List[main_models.ListSiteFunctionsResponseBodyConfigsRewriteUrlRules] = None,
        seo_bypass: List[main_models.ListSiteFunctionsResponseBodyConfigsSeoBypass] = None,
        site_name_exclusive: List[main_models.ListSiteFunctionsResponseBodyConfigsSiteNameExclusive] = None,
        site_pause: List[main_models.ListSiteFunctionsResponseBodyConfigsSitePause] = None,
        tiered_cache: List[main_models.ListSiteFunctionsResponseBodyConfigsTieredCache] = None,
        video_processing: List[main_models.ListSiteFunctionsResponseBodyConfigsVideoProcessing] = None,
    ):
        # The cache reserve configuration.
        self.cache_reserve = cache_reserve
        # The cache rules.
        self.cache_rules = cache_rules
        # The cache tags. When using the purge-by-cache-tag feature, specifies the CacheTag name carried in the origin server response.
        self.cache_tags = cache_tags
        # The CNAME flattening configuration.
        self.cname_flattening = cname_flattening
        # The compression rules.
        self.compression_rules = compression_rules
        # The Chinese mainland network optimization configuration.
        self.cross_border_optimization = cross_border_optimization
        # The custom response code rules.
        self.custom_response_code = custom_response_code
        # The development mode configuration.
        self.development_mode = development_mode
        # The error page redirect rules.
        self.error_pages_redirects = error_pages_redirects
        # The inbound request header modification rules.
        self.http_incoming_request_header_modification_rules = http_incoming_request_header_modification_rules
        # The inbound response header modification rules.
        self.http_incoming_response_header_modification_rules = http_incoming_response_header_modification_rules
        # The request header modification rules.
        self.http_request_header_modification_rules = http_request_header_modification_rules
        # The response header modification rules.
        self.http_response_header_modification_rules = http_response_header_modification_rules
        # The HTTPS application configuration.
        self.https_application_configuration = https_application_configuration
        # The HTTPS basic configuration.
        self.https_basic_configuration = https_basic_configuration
        # The image transformation configuration.
        self.image_transform = image_transform
        # The IPv6 configuration.
        self.ipv_6 = ipv_6
        # The managed transforms.
        self.managed_transforms = managed_transforms
        # The network optimization configuration.
        self.network_optimization = network_optimization
        # The back-to-origin rules.
        self.origin_rules = origin_rules
        # The redirect rules.
        self.redirect_rules = redirect_rules
        # The URL rewrite rules.
        self.rewrite_url_rules = rewrite_url_rules
        # The search engine crawler bypass configuration.
        self.seo_bypass = seo_bypass
        # The site name exclusive configuration. When enabled, other accounts cannot create sites or subsites with the same name as the current site.
        self.site_name_exclusive = site_name_exclusive
        # The site acceleration pause configuration. Temporarily pauses the proxy acceleration feature for the entire site. When enabled, all DNS records directly return record values to clients.
        self.site_pause = site_pause
        # The tiered cache configuration.
        self.tiered_cache = tiered_cache
        # The video processing configuration.
        self.video_processing = video_processing

    def validate(self):
        if self.cache_reserve:
            for v1 in self.cache_reserve:
                 if v1:
                    v1.validate()
        if self.cache_rules:
            for v1 in self.cache_rules:
                 if v1:
                    v1.validate()
        if self.cache_tags:
            for v1 in self.cache_tags:
                 if v1:
                    v1.validate()
        if self.cname_flattening:
            for v1 in self.cname_flattening:
                 if v1:
                    v1.validate()
        if self.compression_rules:
            for v1 in self.compression_rules:
                 if v1:
                    v1.validate()
        if self.cross_border_optimization:
            for v1 in self.cross_border_optimization:
                 if v1:
                    v1.validate()
        if self.custom_response_code:
            for v1 in self.custom_response_code:
                 if v1:
                    v1.validate()
        if self.development_mode:
            for v1 in self.development_mode:
                 if v1:
                    v1.validate()
        if self.error_pages_redirects:
            for v1 in self.error_pages_redirects:
                 if v1:
                    v1.validate()
        if self.http_incoming_request_header_modification_rules:
            for v1 in self.http_incoming_request_header_modification_rules:
                 if v1:
                    v1.validate()
        if self.http_incoming_response_header_modification_rules:
            for v1 in self.http_incoming_response_header_modification_rules:
                 if v1:
                    v1.validate()
        if self.http_request_header_modification_rules:
            for v1 in self.http_request_header_modification_rules:
                 if v1:
                    v1.validate()
        if self.http_response_header_modification_rules:
            for v1 in self.http_response_header_modification_rules:
                 if v1:
                    v1.validate()
        if self.https_application_configuration:
            for v1 in self.https_application_configuration:
                 if v1:
                    v1.validate()
        if self.https_basic_configuration:
            for v1 in self.https_basic_configuration:
                 if v1:
                    v1.validate()
        if self.image_transform:
            for v1 in self.image_transform:
                 if v1:
                    v1.validate()
        if self.ipv_6:
            for v1 in self.ipv_6:
                 if v1:
                    v1.validate()
        if self.managed_transforms:
            for v1 in self.managed_transforms:
                 if v1:
                    v1.validate()
        if self.network_optimization:
            for v1 in self.network_optimization:
                 if v1:
                    v1.validate()
        if self.origin_rules:
            for v1 in self.origin_rules:
                 if v1:
                    v1.validate()
        if self.redirect_rules:
            for v1 in self.redirect_rules:
                 if v1:
                    v1.validate()
        if self.rewrite_url_rules:
            for v1 in self.rewrite_url_rules:
                 if v1:
                    v1.validate()
        if self.seo_bypass:
            for v1 in self.seo_bypass:
                 if v1:
                    v1.validate()
        if self.site_name_exclusive:
            for v1 in self.site_name_exclusive:
                 if v1:
                    v1.validate()
        if self.site_pause:
            for v1 in self.site_pause:
                 if v1:
                    v1.validate()
        if self.tiered_cache:
            for v1 in self.tiered_cache:
                 if v1:
                    v1.validate()
        if self.video_processing:
            for v1 in self.video_processing:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CacheReserve'] = []
        if self.cache_reserve is not None:
            for k1 in self.cache_reserve:
                result['CacheReserve'].append(k1.to_map() if k1 else None)

        result['CacheRules'] = []
        if self.cache_rules is not None:
            for k1 in self.cache_rules:
                result['CacheRules'].append(k1.to_map() if k1 else None)

        result['CacheTags'] = []
        if self.cache_tags is not None:
            for k1 in self.cache_tags:
                result['CacheTags'].append(k1.to_map() if k1 else None)

        result['CnameFlattening'] = []
        if self.cname_flattening is not None:
            for k1 in self.cname_flattening:
                result['CnameFlattening'].append(k1.to_map() if k1 else None)

        result['CompressionRules'] = []
        if self.compression_rules is not None:
            for k1 in self.compression_rules:
                result['CompressionRules'].append(k1.to_map() if k1 else None)

        result['CrossBorderOptimization'] = []
        if self.cross_border_optimization is not None:
            for k1 in self.cross_border_optimization:
                result['CrossBorderOptimization'].append(k1.to_map() if k1 else None)

        result['CustomResponseCode'] = []
        if self.custom_response_code is not None:
            for k1 in self.custom_response_code:
                result['CustomResponseCode'].append(k1.to_map() if k1 else None)

        result['DevelopmentMode'] = []
        if self.development_mode is not None:
            for k1 in self.development_mode:
                result['DevelopmentMode'].append(k1.to_map() if k1 else None)

        result['ErrorPagesRedirects'] = []
        if self.error_pages_redirects is not None:
            for k1 in self.error_pages_redirects:
                result['ErrorPagesRedirects'].append(k1.to_map() if k1 else None)

        result['HttpIncomingRequestHeaderModificationRules'] = []
        if self.http_incoming_request_header_modification_rules is not None:
            for k1 in self.http_incoming_request_header_modification_rules:
                result['HttpIncomingRequestHeaderModificationRules'].append(k1.to_map() if k1 else None)

        result['HttpIncomingResponseHeaderModificationRules'] = []
        if self.http_incoming_response_header_modification_rules is not None:
            for k1 in self.http_incoming_response_header_modification_rules:
                result['HttpIncomingResponseHeaderModificationRules'].append(k1.to_map() if k1 else None)

        result['HttpRequestHeaderModificationRules'] = []
        if self.http_request_header_modification_rules is not None:
            for k1 in self.http_request_header_modification_rules:
                result['HttpRequestHeaderModificationRules'].append(k1.to_map() if k1 else None)

        result['HttpResponseHeaderModificationRules'] = []
        if self.http_response_header_modification_rules is not None:
            for k1 in self.http_response_header_modification_rules:
                result['HttpResponseHeaderModificationRules'].append(k1.to_map() if k1 else None)

        result['HttpsApplicationConfiguration'] = []
        if self.https_application_configuration is not None:
            for k1 in self.https_application_configuration:
                result['HttpsApplicationConfiguration'].append(k1.to_map() if k1 else None)

        result['HttpsBasicConfiguration'] = []
        if self.https_basic_configuration is not None:
            for k1 in self.https_basic_configuration:
                result['HttpsBasicConfiguration'].append(k1.to_map() if k1 else None)

        result['ImageTransform'] = []
        if self.image_transform is not None:
            for k1 in self.image_transform:
                result['ImageTransform'].append(k1.to_map() if k1 else None)

        result['Ipv6'] = []
        if self.ipv_6 is not None:
            for k1 in self.ipv_6:
                result['Ipv6'].append(k1.to_map() if k1 else None)

        result['ManagedTransforms'] = []
        if self.managed_transforms is not None:
            for k1 in self.managed_transforms:
                result['ManagedTransforms'].append(k1.to_map() if k1 else None)

        result['NetworkOptimization'] = []
        if self.network_optimization is not None:
            for k1 in self.network_optimization:
                result['NetworkOptimization'].append(k1.to_map() if k1 else None)

        result['OriginRules'] = []
        if self.origin_rules is not None:
            for k1 in self.origin_rules:
                result['OriginRules'].append(k1.to_map() if k1 else None)

        result['RedirectRules'] = []
        if self.redirect_rules is not None:
            for k1 in self.redirect_rules:
                result['RedirectRules'].append(k1.to_map() if k1 else None)

        result['RewriteUrlRules'] = []
        if self.rewrite_url_rules is not None:
            for k1 in self.rewrite_url_rules:
                result['RewriteUrlRules'].append(k1.to_map() if k1 else None)

        result['SeoBypass'] = []
        if self.seo_bypass is not None:
            for k1 in self.seo_bypass:
                result['SeoBypass'].append(k1.to_map() if k1 else None)

        result['SiteNameExclusive'] = []
        if self.site_name_exclusive is not None:
            for k1 in self.site_name_exclusive:
                result['SiteNameExclusive'].append(k1.to_map() if k1 else None)

        result['SitePause'] = []
        if self.site_pause is not None:
            for k1 in self.site_pause:
                result['SitePause'].append(k1.to_map() if k1 else None)

        result['TieredCache'] = []
        if self.tiered_cache is not None:
            for k1 in self.tiered_cache:
                result['TieredCache'].append(k1.to_map() if k1 else None)

        result['VideoProcessing'] = []
        if self.video_processing is not None:
            for k1 in self.video_processing:
                result['VideoProcessing'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cache_reserve = []
        if m.get('CacheReserve') is not None:
            for k1 in m.get('CacheReserve'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsCacheReserve()
                self.cache_reserve.append(temp_model.from_map(k1))

        self.cache_rules = []
        if m.get('CacheRules') is not None:
            for k1 in m.get('CacheRules'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsCacheRules()
                self.cache_rules.append(temp_model.from_map(k1))

        self.cache_tags = []
        if m.get('CacheTags') is not None:
            for k1 in m.get('CacheTags'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsCacheTags()
                self.cache_tags.append(temp_model.from_map(k1))

        self.cname_flattening = []
        if m.get('CnameFlattening') is not None:
            for k1 in m.get('CnameFlattening'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsCnameFlattening()
                self.cname_flattening.append(temp_model.from_map(k1))

        self.compression_rules = []
        if m.get('CompressionRules') is not None:
            for k1 in m.get('CompressionRules'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsCompressionRules()
                self.compression_rules.append(temp_model.from_map(k1))

        self.cross_border_optimization = []
        if m.get('CrossBorderOptimization') is not None:
            for k1 in m.get('CrossBorderOptimization'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsCrossBorderOptimization()
                self.cross_border_optimization.append(temp_model.from_map(k1))

        self.custom_response_code = []
        if m.get('CustomResponseCode') is not None:
            for k1 in m.get('CustomResponseCode'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsCustomResponseCode()
                self.custom_response_code.append(temp_model.from_map(k1))

        self.development_mode = []
        if m.get('DevelopmentMode') is not None:
            for k1 in m.get('DevelopmentMode'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsDevelopmentMode()
                self.development_mode.append(temp_model.from_map(k1))

        self.error_pages_redirects = []
        if m.get('ErrorPagesRedirects') is not None:
            for k1 in m.get('ErrorPagesRedirects'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsErrorPagesRedirects()
                self.error_pages_redirects.append(temp_model.from_map(k1))

        self.http_incoming_request_header_modification_rules = []
        if m.get('HttpIncomingRequestHeaderModificationRules') is not None:
            for k1 in m.get('HttpIncomingRequestHeaderModificationRules'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsHttpIncomingRequestHeaderModificationRules()
                self.http_incoming_request_header_modification_rules.append(temp_model.from_map(k1))

        self.http_incoming_response_header_modification_rules = []
        if m.get('HttpIncomingResponseHeaderModificationRules') is not None:
            for k1 in m.get('HttpIncomingResponseHeaderModificationRules'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsHttpIncomingResponseHeaderModificationRules()
                self.http_incoming_response_header_modification_rules.append(temp_model.from_map(k1))

        self.http_request_header_modification_rules = []
        if m.get('HttpRequestHeaderModificationRules') is not None:
            for k1 in m.get('HttpRequestHeaderModificationRules'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsHttpRequestHeaderModificationRules()
                self.http_request_header_modification_rules.append(temp_model.from_map(k1))

        self.http_response_header_modification_rules = []
        if m.get('HttpResponseHeaderModificationRules') is not None:
            for k1 in m.get('HttpResponseHeaderModificationRules'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsHttpResponseHeaderModificationRules()
                self.http_response_header_modification_rules.append(temp_model.from_map(k1))

        self.https_application_configuration = []
        if m.get('HttpsApplicationConfiguration') is not None:
            for k1 in m.get('HttpsApplicationConfiguration'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsHttpsApplicationConfiguration()
                self.https_application_configuration.append(temp_model.from_map(k1))

        self.https_basic_configuration = []
        if m.get('HttpsBasicConfiguration') is not None:
            for k1 in m.get('HttpsBasicConfiguration'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsHttpsBasicConfiguration()
                self.https_basic_configuration.append(temp_model.from_map(k1))

        self.image_transform = []
        if m.get('ImageTransform') is not None:
            for k1 in m.get('ImageTransform'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsImageTransform()
                self.image_transform.append(temp_model.from_map(k1))

        self.ipv_6 = []
        if m.get('Ipv6') is not None:
            for k1 in m.get('Ipv6'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsIpv6()
                self.ipv_6.append(temp_model.from_map(k1))

        self.managed_transforms = []
        if m.get('ManagedTransforms') is not None:
            for k1 in m.get('ManagedTransforms'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsManagedTransforms()
                self.managed_transforms.append(temp_model.from_map(k1))

        self.network_optimization = []
        if m.get('NetworkOptimization') is not None:
            for k1 in m.get('NetworkOptimization'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsNetworkOptimization()
                self.network_optimization.append(temp_model.from_map(k1))

        self.origin_rules = []
        if m.get('OriginRules') is not None:
            for k1 in m.get('OriginRules'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsOriginRules()
                self.origin_rules.append(temp_model.from_map(k1))

        self.redirect_rules = []
        if m.get('RedirectRules') is not None:
            for k1 in m.get('RedirectRules'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsRedirectRules()
                self.redirect_rules.append(temp_model.from_map(k1))

        self.rewrite_url_rules = []
        if m.get('RewriteUrlRules') is not None:
            for k1 in m.get('RewriteUrlRules'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsRewriteUrlRules()
                self.rewrite_url_rules.append(temp_model.from_map(k1))

        self.seo_bypass = []
        if m.get('SeoBypass') is not None:
            for k1 in m.get('SeoBypass'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsSeoBypass()
                self.seo_bypass.append(temp_model.from_map(k1))

        self.site_name_exclusive = []
        if m.get('SiteNameExclusive') is not None:
            for k1 in m.get('SiteNameExclusive'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsSiteNameExclusive()
                self.site_name_exclusive.append(temp_model.from_map(k1))

        self.site_pause = []
        if m.get('SitePause') is not None:
            for k1 in m.get('SitePause'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsSitePause()
                self.site_pause.append(temp_model.from_map(k1))

        self.tiered_cache = []
        if m.get('TieredCache') is not None:
            for k1 in m.get('TieredCache'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsTieredCache()
                self.tiered_cache.append(temp_model.from_map(k1))

        self.video_processing = []
        if m.get('VideoProcessing') is not None:
            for k1 in m.get('VideoProcessing'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsVideoProcessing()
                self.video_processing.append(temp_model.from_map(k1))

        return self

class ListSiteFunctionsResponseBodyConfigsVideoProcessing(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        flv_seek_end: str = None,
        flv_seek_start: str = None,
        flv_video_seek_mode: str = None,
        mp_4seek_end: str = None,
        mp_4seek_start: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
        video_seek_enable: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The custom FLV end parameter.
        self.flv_seek_end = flv_seek_end
        # The custom FLV start parameter.
        self.flv_seek_start = flv_seek_start
        # The FLV seeking mode. Valid values:
        # - by_byte: seeks by byte.
        # - by_time: seeks by time.
        self.flv_video_seek_mode = flv_video_seek_mode
        # The custom MP4 end parameter.
        self.mp_4seek_end = mp_4seek_end
        # The custom MP4 start parameter.
        self.mp_4seek_start = mp_4seek_start
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence
        # The video seeking switch. Valid values:
        # 
        # - on: enabled.
        # 
        # - off: disabled.
        self.video_seek_enable = video_seek_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.flv_seek_end is not None:
            result['FlvSeekEnd'] = self.flv_seek_end

        if self.flv_seek_start is not None:
            result['FlvSeekStart'] = self.flv_seek_start

        if self.flv_video_seek_mode is not None:
            result['FlvVideoSeekMode'] = self.flv_video_seek_mode

        if self.mp_4seek_end is not None:
            result['Mp4SeekEnd'] = self.mp_4seek_end

        if self.mp_4seek_start is not None:
            result['Mp4SeekStart'] = self.mp_4seek_start

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.video_seek_enable is not None:
            result['VideoSeekEnable'] = self.video_seek_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('FlvSeekEnd') is not None:
            self.flv_seek_end = m.get('FlvSeekEnd')

        if m.get('FlvSeekStart') is not None:
            self.flv_seek_start = m.get('FlvSeekStart')

        if m.get('FlvVideoSeekMode') is not None:
            self.flv_video_seek_mode = m.get('FlvVideoSeekMode')

        if m.get('Mp4SeekEnd') is not None:
            self.mp_4seek_end = m.get('Mp4SeekEnd')

        if m.get('Mp4SeekStart') is not None:
            self.mp_4seek_start = m.get('Mp4SeekStart')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('VideoSeekEnable') is not None:
            self.video_seek_enable = m.get('VideoSeekEnable')

        return self

class ListSiteFunctionsResponseBodyConfigsTieredCache(DaraModel):
    def __init__(
        self,
        cache_architecture_mode: str = None,
        config_id: int = None,
        sequence: str = None,
    ):
        # The tiered cache architecture mode. Valid values:
        # - edge: edge cache layer.
        # - edge_smart: edge cache layer + smart cache layer.
        # - edge_regional: edge cache layer + regional cache layer.
        # - edge_regional_smart: edge cache layer + regional cache layer + smart cache layer.
        self.cache_architecture_mode = cache_architecture_mode
        # The configuration ID.
        self.config_id = config_id
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_architecture_mode is not None:
            result['CacheArchitectureMode'] = self.cache_architecture_mode

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheArchitectureMode') is not None:
            self.cache_architecture_mode = m.get('CacheArchitectureMode')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsSitePause(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        paused: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # Temporarily pauses the proxy acceleration feature for the entire site. When enabled, all DNS records directly return record values to clients. Valid values:
        # - true: site acceleration is paused.
        # - false: site acceleration is active.
        self.paused = paused
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.paused is not None:
            result['Paused'] = self.paused

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Paused') is not None:
            self.paused = m.get('Paused')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsSiteNameExclusive(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        enable: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The feature switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.enable = enable
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsSeoBypass(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        enable: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The feature switch. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.enable = enable
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsRewriteUrlRules(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        query_string: str = None,
        rewrite_query_string_type: str = None,
        rewrite_uri_type: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
        uri: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The query string after rewriting.
        self.query_string = query_string
        # The query string rewrite type. Valid values:
        # - static: static mode.
        self.rewrite_query_string_type = rewrite_query_string_type
        # The path rewrite type. Valid values:
        # - static: static mode.
        self.rewrite_uri_type = rewrite_uri_type
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence
        # The target URI after rewriting.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.query_string is not None:
            result['QueryString'] = self.query_string

        if self.rewrite_query_string_type is not None:
            result['RewriteQueryStringType'] = self.rewrite_query_string_type

        if self.rewrite_uri_type is not None:
            result['RewriteUriType'] = self.rewrite_uri_type

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('QueryString') is not None:
            self.query_string = m.get('QueryString')

        if m.get('RewriteQueryStringType') is not None:
            self.rewrite_query_string_type = m.get('RewriteQueryStringType')

        if m.get('RewriteUriType') is not None:
            self.rewrite_uri_type = m.get('RewriteUriType')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class ListSiteFunctionsResponseBodyConfigsRedirectRules(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        reserve_query_string: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
        status_code: str = None,
        target_url: str = None,
        type: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # Specifies whether to preserve the query string. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.reserve_query_string = reserve_query_string
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence
        # The response status code used by the edge node when responding with the redirect address to the client. Valid values:
        # - 301
        # - 302
        # - 303
        # - 307
        # - 308
        self.status_code = status_code
        # The target URL after redirection.
        self.target_url = target_url
        # The redirect type. Valid values:
        # - static: static mode.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.reserve_query_string is not None:
            result['ReserveQueryString'] = self.reserve_query_string

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ReserveQueryString') is not None:
            self.reserve_query_string = m.get('ReserveQueryString')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListSiteFunctionsResponseBodyConfigsOriginRules(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        dns_record: str = None,
        origin_host: str = None,
        origin_http_port: str = None,
        origin_https_port: str = None,
        origin_mtls: str = None,
        origin_read_timeout: str = None,
        origin_scheme: str = None,
        origin_sni: str = None,
        origin_verify: str = None,
        range: str = None,
        range_chunk_size: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The overridden DNS resolution record for back-to-origin requests.
        self.dns_record = dns_record
        # The HOST header carried in the back-to-origin request.
        self.origin_host = origin_host
        # The origin server port used when fetching content over HTTP.
        self.origin_http_port = origin_http_port
        # The origin server port used when fetching content over HTTPS.
        self.origin_https_port = origin_https_port
        # Specifies whether to enable mTLS for back-to-origin. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.origin_mtls = origin_mtls
        # The origin read timeout, in seconds.
        self.origin_read_timeout = origin_read_timeout
        # The protocol used for back-to-origin requests. Valid values:
        # - http: uses HTTP for back-to-origin.
        # - https: uses HTTPS for back-to-origin.
        # - follow: follows the client protocol for back-to-origin.
        self.origin_scheme = origin_scheme
        # The SNI carried in the back-to-origin request.
        self.origin_sni = origin_sni
        # Specifies whether to enable origin server certificate verification. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.origin_verify = origin_verify
        # Specifies whether to use range-based origin fetch for file downloads. Valid values:
        # - on: enabled.
        # - off: disabled.
        # - force: forced.
        self.range = range
        # The range chunk size. Valid values:
        # - 512KB
        # - 1MB
        # - 2MB
        # - 4MB
        self.range_chunk_size = range_chunk_size
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.dns_record is not None:
            result['DnsRecord'] = self.dns_record

        if self.origin_host is not None:
            result['OriginHost'] = self.origin_host

        if self.origin_http_port is not None:
            result['OriginHttpPort'] = self.origin_http_port

        if self.origin_https_port is not None:
            result['OriginHttpsPort'] = self.origin_https_port

        if self.origin_mtls is not None:
            result['OriginMtls'] = self.origin_mtls

        if self.origin_read_timeout is not None:
            result['OriginReadTimeout'] = self.origin_read_timeout

        if self.origin_scheme is not None:
            result['OriginScheme'] = self.origin_scheme

        if self.origin_sni is not None:
            result['OriginSni'] = self.origin_sni

        if self.origin_verify is not None:
            result['OriginVerify'] = self.origin_verify

        if self.range is not None:
            result['Range'] = self.range

        if self.range_chunk_size is not None:
            result['RangeChunkSize'] = self.range_chunk_size

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('DnsRecord') is not None:
            self.dns_record = m.get('DnsRecord')

        if m.get('OriginHost') is not None:
            self.origin_host = m.get('OriginHost')

        if m.get('OriginHttpPort') is not None:
            self.origin_http_port = m.get('OriginHttpPort')

        if m.get('OriginHttpsPort') is not None:
            self.origin_https_port = m.get('OriginHttpsPort')

        if m.get('OriginMtls') is not None:
            self.origin_mtls = m.get('OriginMtls')

        if m.get('OriginReadTimeout') is not None:
            self.origin_read_timeout = m.get('OriginReadTimeout')

        if m.get('OriginScheme') is not None:
            self.origin_scheme = m.get('OriginScheme')

        if m.get('OriginSni') is not None:
            self.origin_sni = m.get('OriginSni')

        if m.get('OriginVerify') is not None:
            self.origin_verify = m.get('OriginVerify')

        if m.get('Range') is not None:
            self.range = m.get('Range')

        if m.get('RangeChunkSize') is not None:
            self.range_chunk_size = m.get('RangeChunkSize')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsNetworkOptimization(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        grpc: str = None,
        http_2origin: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
        smart_routing: str = None,
        upload_max_filesize: str = None,
        websocket: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # Specifies whether to enable gRPC. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.grpc = grpc
        # Specifies whether to enable HTTP/2 back-to-origin. Disabled by default. Valid values:
        # 
        # - on: enabled.
        # - off: disabled.
        self.http_2origin = http_2origin
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence
        # Specifies whether to enable smart routing. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.smart_routing = smart_routing
        # The maximum upload file size, in MB. Valid values: 100 to 500.
        self.upload_max_filesize = upload_max_filesize
        # Specifies whether to enable WebSocket. Enabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.websocket = websocket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.grpc is not None:
            result['Grpc'] = self.grpc

        if self.http_2origin is not None:
            result['Http2Origin'] = self.http_2origin

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.smart_routing is not None:
            result['SmartRouting'] = self.smart_routing

        if self.upload_max_filesize is not None:
            result['UploadMaxFilesize'] = self.upload_max_filesize

        if self.websocket is not None:
            result['Websocket'] = self.websocket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Grpc') is not None:
            self.grpc = m.get('Grpc')

        if m.get('Http2Origin') is not None:
            self.http_2origin = m.get('Http2Origin')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SmartRouting') is not None:
            self.smart_routing = m.get('SmartRouting')

        if m.get('UploadMaxFilesize') is not None:
            self.upload_max_filesize = m.get('UploadMaxFilesize')

        if m.get('Websocket') is not None:
            self.websocket = m.get('Websocket')

        return self

class ListSiteFunctionsResponseBodyConfigsManagedTransforms(DaraModel):
    def __init__(
        self,
        add_client_geolocation_headers: str = None,
        add_real_client_ip_header: str = None,
        config_id: int = None,
        sequence: str = None,
    ):
        # Specifies whether to add visitor geolocation headers. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.add_client_geolocation_headers = add_client_geolocation_headers
        # Specifies whether to add the "ali-real-client-ip" header that contains the real client IP address. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.add_real_client_ip_header = add_real_client_ip_header
        # The configuration ID.
        self.config_id = config_id
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_client_geolocation_headers is not None:
            result['AddClientGeolocationHeaders'] = self.add_client_geolocation_headers

        if self.add_real_client_ip_header is not None:
            result['AddRealClientIpHeader'] = self.add_real_client_ip_header

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddClientGeolocationHeaders') is not None:
            self.add_client_geolocation_headers = m.get('AddClientGeolocationHeaders')

        if m.get('AddRealClientIpHeader') is not None:
            self.add_real_client_ip_header = m.get('AddRealClientIpHeader')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsIpv6(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        enable: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # Specifies whether to enable IPv6. Enabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.enable = enable
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsImageTransform(DaraModel):
    def __init__(
        self,
        auto_avif: str = None,
        auto_webp: str = None,
        config_id: int = None,
        enable: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
    ):
        # The adaptive AVIF setting.
        self.auto_avif = auto_avif
        # The adaptive WebP setting.
        self.auto_webp = auto_webp
        # The configuration ID.
        self.config_id = config_id
        # Specifies whether to enable image transformation. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.enable = enable
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_avif is not None:
            result['AutoAvif'] = self.auto_avif

        if self.auto_webp is not None:
            result['AutoWebp'] = self.auto_webp

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAvif') is not None:
            self.auto_avif = m.get('AutoAvif')

        if m.get('AutoWebp') is not None:
            self.auto_webp = m.get('AutoWebp')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsHttpsBasicConfiguration(DaraModel):
    def __init__(
        self,
        ciphersuite: str = None,
        ciphersuite_group: str = None,
        config_id: int = None,
        http_2: str = None,
        http_3: str = None,
        https: str = None,
        ocsp_stapling: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
        tls_10: str = None,
        tls_11: str = None,
        tls_12: str = None,
        tls_13: str = None,
    ):
        # The custom cipher suites. Specifies the specific encryption algorithms selected when CiphersuiteGroup is set to custom.
        self.ciphersuite = ciphersuite
        # The cipher suite group. All cipher suites are enabled by default. Valid values:
        # - all: all cipher suites.
        # - strict: strong cipher suites.
        # - custom: custom cipher suites.
        self.ciphersuite_group = ciphersuite_group
        # The configuration ID.
        self.config_id = config_id
        # Specifies whether to enable HTTP/2. Enabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.http_2 = http_2
        # Specifies whether to enable HTTP/3. Enabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.http_3 = http_3
        # Specifies whether to enable HTTPS. Enabled by default. Valid values:
        # 
        # - on: enabled.
        # 
        # - off: disabled.
        self.https = https
        # Specifies whether to enable OCSP stapling. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.ocsp_stapling = ocsp_stapling
        # The matching rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence
        # Specifies whether to enable TLS 1.0. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.tls_10 = tls_10
        # Specifies whether to enable TLS 1.1. Enabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.tls_11 = tls_11
        # Specifies whether to enable TLS 1.2. Enabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.tls_12 = tls_12
        # Specifies whether to enable TLS 1.3. Enabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.tls_13 = tls_13

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ciphersuite is not None:
            result['Ciphersuite'] = self.ciphersuite

        if self.ciphersuite_group is not None:
            result['CiphersuiteGroup'] = self.ciphersuite_group

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.http_2 is not None:
            result['Http2'] = self.http_2

        if self.http_3 is not None:
            result['Http3'] = self.http_3

        if self.https is not None:
            result['Https'] = self.https

        if self.ocsp_stapling is not None:
            result['OcspStapling'] = self.ocsp_stapling

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.tls_10 is not None:
            result['Tls10'] = self.tls_10

        if self.tls_11 is not None:
            result['Tls11'] = self.tls_11

        if self.tls_12 is not None:
            result['Tls12'] = self.tls_12

        if self.tls_13 is not None:
            result['Tls13'] = self.tls_13

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphersuite') is not None:
            self.ciphersuite = m.get('Ciphersuite')

        if m.get('CiphersuiteGroup') is not None:
            self.ciphersuite_group = m.get('CiphersuiteGroup')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Http2') is not None:
            self.http_2 = m.get('Http2')

        if m.get('Http3') is not None:
            self.http_3 = m.get('Http3')

        if m.get('Https') is not None:
            self.https = m.get('Https')

        if m.get('OcspStapling') is not None:
            self.ocsp_stapling = m.get('OcspStapling')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('Tls10') is not None:
            self.tls_10 = m.get('Tls10')

        if m.get('Tls11') is not None:
            self.tls_11 = m.get('Tls11')

        if m.get('Tls12') is not None:
            self.tls_12 = m.get('Tls12')

        if m.get('Tls13') is not None:
            self.tls_13 = m.get('Tls13')

        return self

class ListSiteFunctionsResponseBodyConfigsHttpsApplicationConfiguration(DaraModel):
    def __init__(
        self,
        alt_svc: str = None,
        alt_svc_clear: str = None,
        alt_svc_ma: str = None,
        alt_svc_persist: str = None,
        config_id: int = None,
        hsts: str = None,
        hsts_include_subdomains: str = None,
        hsts_max_age: str = None,
        hsts_preload: str = None,
        https_force: str = None,
        https_force_code: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
    ):
        # The Alt-Svc feature switch. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.alt_svc = alt_svc
        # Specifies whether the Alt-Svc header includes the clear parameter. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.alt_svc_clear = alt_svc_clear
        # The Alt-Svc validity period, in seconds. Default value: 86400.
        self.alt_svc_ma = alt_svc_ma
        # Specifies whether the Alt-Svc header includes the persist parameter. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.alt_svc_persist = alt_svc_persist
        # The configuration ID.
        self.config_id = config_id
        # Specifies whether to enable HSTS. Disabled by default. Valid values:
        # 
        # - on: enabled.
        # - off: disabled.
        self.hsts = hsts
        # Specifies whether to include subdomains in HSTS. Disabled by default. Valid values:
        # 
        # - on: enabled.
        # - off: disabled.
        self.hsts_include_subdomains = hsts_include_subdomains
        # The HSTS expiration time, in seconds.
        self.hsts_max_age = hsts_max_age
        # Specifies whether to enable HSTS preload. Disabled by default. Valid values:
        # 
        # - on: enabled.
        # - off: disabled.
        self.hsts_preload = hsts_preload
        # Specifies whether to enable forced HTTPS. Disabled by default. Valid values:
        # 
        # - on: enabled.
        # 
        # - off: disabled.
        self.https_force = https_force
        # The status code used for forced HTTPS redirect. Valid values:
        # - 301
        # - 302
        # - 307
        # - 308
        self.https_force_code = https_force_code
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alt_svc is not None:
            result['AltSvc'] = self.alt_svc

        if self.alt_svc_clear is not None:
            result['AltSvcClear'] = self.alt_svc_clear

        if self.alt_svc_ma is not None:
            result['AltSvcMa'] = self.alt_svc_ma

        if self.alt_svc_persist is not None:
            result['AltSvcPersist'] = self.alt_svc_persist

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.hsts is not None:
            result['Hsts'] = self.hsts

        if self.hsts_include_subdomains is not None:
            result['HstsIncludeSubdomains'] = self.hsts_include_subdomains

        if self.hsts_max_age is not None:
            result['HstsMaxAge'] = self.hsts_max_age

        if self.hsts_preload is not None:
            result['HstsPreload'] = self.hsts_preload

        if self.https_force is not None:
            result['HttpsForce'] = self.https_force

        if self.https_force_code is not None:
            result['HttpsForceCode'] = self.https_force_code

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AltSvc') is not None:
            self.alt_svc = m.get('AltSvc')

        if m.get('AltSvcClear') is not None:
            self.alt_svc_clear = m.get('AltSvcClear')

        if m.get('AltSvcMa') is not None:
            self.alt_svc_ma = m.get('AltSvcMa')

        if m.get('AltSvcPersist') is not None:
            self.alt_svc_persist = m.get('AltSvcPersist')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Hsts') is not None:
            self.hsts = m.get('Hsts')

        if m.get('HstsIncludeSubdomains') is not None:
            self.hsts_include_subdomains = m.get('HstsIncludeSubdomains')

        if m.get('HstsMaxAge') is not None:
            self.hsts_max_age = m.get('HstsMaxAge')

        if m.get('HstsPreload') is not None:
            self.hsts_preload = m.get('HstsPreload')

        if m.get('HttpsForce') is not None:
            self.https_force = m.get('HttpsForce')

        if m.get('HttpsForceCode') is not None:
            self.https_force_code = m.get('HttpsForceCode')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsHttpResponseHeaderModificationRules(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        response_header_modification: List[main_models.ListSiteFunctionsResponseBodyConfigsHttpResponseHeaderModificationRulesResponseHeaderModification] = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The response header modifications. Supports add, delete, and modify operations.
        self.response_header_modification = response_header_modification
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        if self.response_header_modification:
            for v1 in self.response_header_modification:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        result['ResponseHeaderModification'] = []
        if self.response_header_modification is not None:
            for k1 in self.response_header_modification:
                result['ResponseHeaderModification'].append(k1.to_map() if k1 else None)

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        self.response_header_modification = []
        if m.get('ResponseHeaderModification') is not None:
            for k1 in m.get('ResponseHeaderModification'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsHttpResponseHeaderModificationRulesResponseHeaderModification()
                self.response_header_modification.append(temp_model.from_map(k1))

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsHttpResponseHeaderModificationRulesResponseHeaderModification(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation: str = None,
        value: str = None,
    ):
        # The response header name.
        self.name = name
        # The operation type. Valid values:
        # - add: adds a header.
        # - del: deletes a header.
        # - modify: modifies a header.
        self.operation = operation
        # The response header value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListSiteFunctionsResponseBodyConfigsHttpRequestHeaderModificationRules(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        request_header_modification: List[main_models.ListSiteFunctionsResponseBodyConfigsHttpRequestHeaderModificationRulesRequestHeaderModification] = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The request header modifications. Supports add, delete, and modify operations.
        self.request_header_modification = request_header_modification
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        if self.request_header_modification:
            for v1 in self.request_header_modification:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        result['RequestHeaderModification'] = []
        if self.request_header_modification is not None:
            for k1 in self.request_header_modification:
                result['RequestHeaderModification'].append(k1.to_map() if k1 else None)

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        self.request_header_modification = []
        if m.get('RequestHeaderModification') is not None:
            for k1 in m.get('RequestHeaderModification'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsHttpRequestHeaderModificationRulesRequestHeaderModification()
                self.request_header_modification.append(temp_model.from_map(k1))

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsHttpRequestHeaderModificationRulesRequestHeaderModification(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation: str = None,
        value: str = None,
    ):
        # The request header name.
        self.name = name
        # The operation type. Valid values:
        # - add: adds a header.
        # - del: deletes a header.
        # - modify: modifies a header.
        self.operation = operation
        # The request header value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListSiteFunctionsResponseBodyConfigsHttpIncomingResponseHeaderModificationRules(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        response_header_modification: List[main_models.ListSiteFunctionsResponseBodyConfigsHttpIncomingResponseHeaderModificationRulesResponseHeaderModification] = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The response header modifications. Supports add, delete, and modify operations.
        self.response_header_modification = response_header_modification
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        if self.response_header_modification:
            for v1 in self.response_header_modification:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        result['ResponseHeaderModification'] = []
        if self.response_header_modification is not None:
            for k1 in self.response_header_modification:
                result['ResponseHeaderModification'].append(k1.to_map() if k1 else None)

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        self.response_header_modification = []
        if m.get('ResponseHeaderModification') is not None:
            for k1 in m.get('ResponseHeaderModification'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsHttpIncomingResponseHeaderModificationRulesResponseHeaderModification()
                self.response_header_modification.append(temp_model.from_map(k1))

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsHttpIncomingResponseHeaderModificationRulesResponseHeaderModification(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation: str = None,
        value: str = None,
    ):
        # The response header name.
        self.name = name
        # The operation type. Valid values:
        # - add: adds a header.
        # - del: deletes a header.
        # - modify: modifies a header.
        self.operation = operation
        # The response header value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListSiteFunctionsResponseBodyConfigsHttpIncomingRequestHeaderModificationRules(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        request_header_modification: List[main_models.ListSiteFunctionsResponseBodyConfigsHttpIncomingRequestHeaderModificationRulesRequestHeaderModification] = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The request header modifications. Supports add, delete, and modify operations.
        self.request_header_modification = request_header_modification
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        if self.request_header_modification:
            for v1 in self.request_header_modification:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        result['RequestHeaderModification'] = []
        if self.request_header_modification is not None:
            for k1 in self.request_header_modification:
                result['RequestHeaderModification'].append(k1.to_map() if k1 else None)

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        self.request_header_modification = []
        if m.get('RequestHeaderModification') is not None:
            for k1 in m.get('RequestHeaderModification'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsHttpIncomingRequestHeaderModificationRulesRequestHeaderModification()
                self.request_header_modification.append(temp_model.from_map(k1))

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsHttpIncomingRequestHeaderModificationRulesRequestHeaderModification(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation: str = None,
        value: str = None,
    ):
        # The request header name.
        self.name = name
        # The operation type. Valid values:
        # - add: adds a header.
        # - del: deletes a header.
        # - modify: modifies a header.
        self.operation = operation
        # The request header value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListSiteFunctionsResponseBodyConfigsErrorPagesRedirects(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        error_pages_redirect: List[main_models.ListSiteFunctionsResponseBodyConfigsErrorPagesRedirectsErrorPagesRedirect] = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The error page redirect configuration.
        self.error_pages_redirect = error_pages_redirect
        # The rule content. Uses conditional expressions to match user requests. This parameter is not required when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: set the value to true.
        # - Match specified requests: set the value to a custom expression, such as (http.host eq \\"video.example.com\\").
        self.rule = rule
        # The rule switch. This parameter is not required when adding a global configuration. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name. This parameter is not required when adding a global configuration.
        self.rule_name = rule_name
        # The rule execution order. A smaller value indicates a higher priority.
        self.sequence = sequence

    def validate(self):
        if self.error_pages_redirect:
            for v1 in self.error_pages_redirect:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        result['ErrorPagesRedirect'] = []
        if self.error_pages_redirect is not None:
            for k1 in self.error_pages_redirect:
                result['ErrorPagesRedirect'].append(k1.to_map() if k1 else None)

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        self.error_pages_redirect = []
        if m.get('ErrorPagesRedirect') is not None:
            for k1 in m.get('ErrorPagesRedirect'):
                temp_model = main_models.ListSiteFunctionsResponseBodyConfigsErrorPagesRedirectsErrorPagesRedirect()
                self.error_pages_redirect.append(temp_model.from_map(k1))

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsErrorPagesRedirectsErrorPagesRedirect(DaraModel):
    def __init__(
        self,
        status_code: str = None,
        target_url: str = None,
    ):
        # The response status code used by the edge node when responding with the redirect address to the client. Valid values:
        # - 400
        # - 403
        # - 404
        # - 405
        # - 414
        # - 416
        # - 500
        # - 501
        # - 502
        # - 503
        # - 504
        self.status_code = status_code
        # The target URL after redirection.
        self.target_url = target_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.target_url is not None:
            result['TargetURL'] = self.target_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TargetURL') is not None:
            self.target_url = m.get('TargetURL')

        return self

class ListSiteFunctionsResponseBodyConfigsDevelopmentMode(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        enable: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The feature switch. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.enable = enable
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsCustomResponseCode(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        page_id: str = None,
        return_code: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The response page.
        self.page_id = page_id
        # The response code.
        self.return_code = return_code
        # The rule content. Uses conditional expressions to match user requests. This parameter is not required when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: set the value to true.
        # - Match specified requests: set the value to a custom expression, such as (http.host eq \\"video.example.com\\").
        self.rule = rule
        # The rule switch. This parameter is not required when adding a global configuration. Valid values:
        # 
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name. This parameter is not required when adding a global configuration.
        self.rule_name = rule_name
        # The rule execution order. A smaller value indicates a higher priority.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.return_code is not None:
            result['ReturnCode'] = self.return_code

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsCrossBorderOptimization(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        enable: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # Specifies whether to enable Chinese mainland network access optimization. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.enable = enable
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsCompressionRules(DaraModel):
    def __init__(
        self,
        brotli: str = None,
        config_id: int = None,
        gzip: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
        zstd: str = None,
    ):
        # Specifies whether to enable Brotli compression. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.brotli = brotli
        # The configuration ID.
        self.config_id = config_id
        # Specifies whether to enable Gzip compression. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.gzip = gzip
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence
        # Specifies whether to enable Zstd compression. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.zstd = zstd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brotli is not None:
            result['Brotli'] = self.brotli

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.gzip is not None:
            result['Gzip'] = self.gzip

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.zstd is not None:
            result['Zstd'] = self.zstd

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brotli') is not None:
            self.brotli = m.get('Brotli')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Gzip') is not None:
            self.gzip = m.get('Gzip')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('Zstd') is not None:
            self.zstd = m.get('Zstd')

        return self

class ListSiteFunctionsResponseBodyConfigsCnameFlattening(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        flatten_mode: str = None,
        sequence: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # The flattening mode. Valid values:
        # - flatten_all: flattens all records.
        # - flatten_at_root: flattens only the root domain. This is the default value.
        self.flatten_mode = flatten_mode
        # The rule execution order.
        self.sequence = sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.flatten_mode is not None:
            result['FlattenMode'] = self.flatten_mode

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('FlattenMode') is not None:
            self.flatten_mode = m.get('FlattenMode')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        return self

class ListSiteFunctionsResponseBodyConfigsCacheTags(DaraModel):
    def __init__(
        self,
        case_insensitive: str = None,
        config_id: int = None,
        sequence: str = None,
        tag_name: str = None,
    ):
        # Specifies whether to ignore case. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.case_insensitive = case_insensitive
        # The configuration ID.
        self.config_id = config_id
        # The rule execution order.
        self.sequence = sequence
        # The custom CacheTag name.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_insensitive is not None:
            result['CaseInsensitive'] = self.case_insensitive

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaseInsensitive') is not None:
            self.case_insensitive = m.get('CaseInsensitive')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class ListSiteFunctionsResponseBodyConfigsCacheRules(DaraModel):
    def __init__(
        self,
        additional_cacheable_ports: str = None,
        browser_cache_mode: str = None,
        browser_cache_ttl: str = None,
        bypass_cache: str = None,
        cache_deception_armor: str = None,
        cache_reserve_eligibility: str = None,
        check_presence_cookie: str = None,
        check_presence_header: str = None,
        config_id: int = None,
        edge_cache_mode: str = None,
        edge_cache_ttl: str = None,
        edge_status_code_cache_ttl: str = None,
        include_cookie: str = None,
        include_header: str = None,
        post_body_cache_key: str = None,
        post_body_size_limit: str = None,
        post_cache: str = None,
        query_string: str = None,
        query_string_mode: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: str = None,
        serve_stale: str = None,
        sort_query_string_for_cache: str = None,
        user_device_type: str = None,
        user_geo: str = None,
        user_language: str = None,
    ):
        # The ports on which caching is enabled. Valid values: 8880, 2052, 2082, 2086, 2095, 2053, 2083, 2087, and 2096.
        self.additional_cacheable_ports = additional_cacheable_ports
        # The browser cache mode. Valid values:
        # - no_cache: no caching.
        # - follow_origin: follows the origin server cache policy.
        # - override_origin: overrides the origin server cache policy.
        self.browser_cache_mode = browser_cache_mode
        # The browser cache expiration time, in seconds.
        self.browser_cache_ttl = browser_cache_ttl
        # The bypass cache mode. Valid values:
        # - cache_all: all requests are cached.
        # - bypass_all: all requests bypass the cache.
        self.bypass_cache = bypass_cache
        # Specifies whether to enable cache deception armor. This feature protects against web cache deception attacks by caching only content that passes validation. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.cache_deception_armor = cache_deception_armor
        # The cache reserve eligibility. Controls whether requests bypass the cache reserve node during back-to-origin. Valid values:
        # - bypass_cache_reserve: requests bypass cache reserve.
        # - eligible_for_cache_reserve: requests are eligible for cache reserve.
        self.cache_reserve_eligibility = cache_reserve_eligibility
        # Checks whether a cookie exists when generating cache keys. If the cookie exists, the cookie name (case-insensitive) is added to the cache key. Multiple cookie names are supported and separated by spaces.
        self.check_presence_cookie = check_presence_cookie
        # Checks whether a header exists when generating cache keys. If the header exists, the header name (case-insensitive) is added to the cache key. Multiple header names are supported and separated by spaces.
        self.check_presence_header = check_presence_header
        # The configuration ID.
        self.config_id = config_id
        # The edge cache mode. Valid values:
        # - follow_origin: follows the origin server cache policy (if present). Otherwise, uses the default cache policy.
        # - no_cache: no caching.
        # - override_origin: overrides the origin server cache policy.
        # - follow_origin_bypass: follows the origin server cache policy (if present). Otherwise, does not cache.
        self.edge_cache_mode = edge_cache_mode
        # The edge cache expiration time, in seconds.
        self.edge_cache_ttl = edge_cache_ttl
        # The status code cache expiration time, in seconds.
        self.edge_status_code_cache_ttl = edge_status_code_cache_ttl
        # The cookie names and their values to include when generating cache keys. Multiple values are supported and separated by spaces.
        self.include_cookie = include_cookie
        # The header names and their values to include when generating cache keys. Multiple values are supported and separated by spaces.
        self.include_header = include_header
        # The cache key processing mode.
        self.post_body_cache_key = post_body_cache_key
        # The body size limit, in KB. Supports body sizes from 1 to 8 KB. If left empty, the default value of 8 KB is used.
        self.post_body_size_limit = post_body_size_limit
        # The POST cache switch.
        self.post_cache = post_cache
        # The query strings to retain or remove. Multiple values are supported and separated by spaces.
        self.query_string = query_string
        # The query string processing mode when generating cache keys. Valid values:
        # - ignore_all: ignores all query strings.
        # - exclude_query_string: removes specified query strings.
        # - reserve_all: retains all query strings. This is the default value.
        # - include_query_string: retains specified query strings.
        self.query_string_mode = query_string_mode
        # The rule content.
        self.rule = rule
        # The rule switch. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.rule_enable = rule_enable
        # The rule name.
        self.rule_name = rule_name
        # The rule execution order.
        self.sequence = sequence
        # Specifies whether to serve stale cache. When enabled, the edge node can respond to user requests with cached expired content when the origin server is unavailable. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.serve_stale = serve_stale
        # Specifies whether to sort query strings. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.sort_query_string_for_cache = sort_query_string_for_cache
        # Specifies whether to include the type of the client when generating cache keys. Valid values:
        # - on: enabled.
        # - off: shutdown.
        self.user_device_type = user_device_type
        # Specifies whether to include the client geographic location when generating cache keys. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.user_geo = user_geo
        # Specifies whether to include the client language type when generating cache keys. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.user_language = user_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_cacheable_ports is not None:
            result['AdditionalCacheablePorts'] = self.additional_cacheable_ports

        if self.browser_cache_mode is not None:
            result['BrowserCacheMode'] = self.browser_cache_mode

        if self.browser_cache_ttl is not None:
            result['BrowserCacheTtl'] = self.browser_cache_ttl

        if self.bypass_cache is not None:
            result['BypassCache'] = self.bypass_cache

        if self.cache_deception_armor is not None:
            result['CacheDeceptionArmor'] = self.cache_deception_armor

        if self.cache_reserve_eligibility is not None:
            result['CacheReserveEligibility'] = self.cache_reserve_eligibility

        if self.check_presence_cookie is not None:
            result['CheckPresenceCookie'] = self.check_presence_cookie

        if self.check_presence_header is not None:
            result['CheckPresenceHeader'] = self.check_presence_header

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.edge_cache_mode is not None:
            result['EdgeCacheMode'] = self.edge_cache_mode

        if self.edge_cache_ttl is not None:
            result['EdgeCacheTtl'] = self.edge_cache_ttl

        if self.edge_status_code_cache_ttl is not None:
            result['EdgeStatusCodeCacheTtl'] = self.edge_status_code_cache_ttl

        if self.include_cookie is not None:
            result['IncludeCookie'] = self.include_cookie

        if self.include_header is not None:
            result['IncludeHeader'] = self.include_header

        if self.post_body_cache_key is not None:
            result['PostBodyCacheKey'] = self.post_body_cache_key

        if self.post_body_size_limit is not None:
            result['PostBodySizeLimit'] = self.post_body_size_limit

        if self.post_cache is not None:
            result['PostCache'] = self.post_cache

        if self.query_string is not None:
            result['QueryString'] = self.query_string

        if self.query_string_mode is not None:
            result['QueryStringMode'] = self.query_string_mode

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.serve_stale is not None:
            result['ServeStale'] = self.serve_stale

        if self.sort_query_string_for_cache is not None:
            result['SortQueryStringForCache'] = self.sort_query_string_for_cache

        if self.user_device_type is not None:
            result['UserDeviceType'] = self.user_device_type

        if self.user_geo is not None:
            result['UserGeo'] = self.user_geo

        if self.user_language is not None:
            result['UserLanguage'] = self.user_language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalCacheablePorts') is not None:
            self.additional_cacheable_ports = m.get('AdditionalCacheablePorts')

        if m.get('BrowserCacheMode') is not None:
            self.browser_cache_mode = m.get('BrowserCacheMode')

        if m.get('BrowserCacheTtl') is not None:
            self.browser_cache_ttl = m.get('BrowserCacheTtl')

        if m.get('BypassCache') is not None:
            self.bypass_cache = m.get('BypassCache')

        if m.get('CacheDeceptionArmor') is not None:
            self.cache_deception_armor = m.get('CacheDeceptionArmor')

        if m.get('CacheReserveEligibility') is not None:
            self.cache_reserve_eligibility = m.get('CacheReserveEligibility')

        if m.get('CheckPresenceCookie') is not None:
            self.check_presence_cookie = m.get('CheckPresenceCookie')

        if m.get('CheckPresenceHeader') is not None:
            self.check_presence_header = m.get('CheckPresenceHeader')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('EdgeCacheMode') is not None:
            self.edge_cache_mode = m.get('EdgeCacheMode')

        if m.get('EdgeCacheTtl') is not None:
            self.edge_cache_ttl = m.get('EdgeCacheTtl')

        if m.get('EdgeStatusCodeCacheTtl') is not None:
            self.edge_status_code_cache_ttl = m.get('EdgeStatusCodeCacheTtl')

        if m.get('IncludeCookie') is not None:
            self.include_cookie = m.get('IncludeCookie')

        if m.get('IncludeHeader') is not None:
            self.include_header = m.get('IncludeHeader')

        if m.get('PostBodyCacheKey') is not None:
            self.post_body_cache_key = m.get('PostBodyCacheKey')

        if m.get('PostBodySizeLimit') is not None:
            self.post_body_size_limit = m.get('PostBodySizeLimit')

        if m.get('PostCache') is not None:
            self.post_cache = m.get('PostCache')

        if m.get('QueryString') is not None:
            self.query_string = m.get('QueryString')

        if m.get('QueryStringMode') is not None:
            self.query_string_mode = m.get('QueryStringMode')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('ServeStale') is not None:
            self.serve_stale = m.get('ServeStale')

        if m.get('SortQueryStringForCache') is not None:
            self.sort_query_string_for_cache = m.get('SortQueryStringForCache')

        if m.get('UserDeviceType') is not None:
            self.user_device_type = m.get('UserDeviceType')

        if m.get('UserGeo') is not None:
            self.user_geo = m.get('UserGeo')

        if m.get('UserLanguage') is not None:
            self.user_language = m.get('UserLanguage')

        return self

class ListSiteFunctionsResponseBodyConfigsCacheReserve(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        enable: str = None,
        instance_id: str = None,
    ):
        # The configuration ID.
        self.config_id = config_id
        # Specifies whether to enable cache reserve. Disabled by default. Valid values:
        # - on: enabled.
        # - off: disabled.
        self.enable = enable
        # The cache reserve instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

