# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class ReadPageScrapeBody(DaraModel):
    def __init__(
        self,
        formats: List[str] = None,
        location: str = None,
        max_age: int = None,
        page_timeout: int = None,
        readability: main_models.ReadPageScrapeBodyReadability = None,
        timeout: int = None,
        url: str = None,
    ):
        # The formats of the parsed result. Valid values:
        # - rawHtml: The HTML of the target site.
        # - html: The page content processed based on the readabilityMode.
        # - markdown: The Markdown content converted from the HTML.
        # - text: The text content in the HTML.
        # - screenshot: The screenshot of the target site.
        self.formats = formats
        # This parameter is not required.
        self.location = location
        # The maximum cache duration, in seconds.
        # - If the cache duration is less than the maxAge value, the cached content is returned.
        # - If the maxAge value is set to 0, the cache is not used.
        # 
        # Default value: 1296000.
        self.max_age = max_age
        # The timeout period for waiting for the resources of the target site to fully load. The pageTimeout value must be less than the timeout value.
        # 
        # Default value: 15000.
        self.page_timeout = page_timeout
        # The readability configuration of the parsed result.
        self.readability = readability
        # The end-to-end processing timeout period, in milliseconds.
        # 
        # Valid values: 0 to 180000.
        # 
        # Default value: 60000.
        self.timeout = timeout
        # The target URL to parse. It must start with http:// or https://.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        if self.readability:
            self.readability.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.formats is not None:
            result['formats'] = self.formats

        if self.location is not None:
            result['location'] = self.location

        if self.max_age is not None:
            result['maxAge'] = self.max_age

        if self.page_timeout is not None:
            result['pageTimeout'] = self.page_timeout

        if self.readability is not None:
            result['readability'] = self.readability.to_map()

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('formats') is not None:
            self.formats = m.get('formats')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('maxAge') is not None:
            self.max_age = m.get('maxAge')

        if m.get('pageTimeout') is not None:
            self.page_timeout = m.get('pageTimeout')

        if m.get('readability') is not None:
            temp_model = main_models.ReadPageScrapeBodyReadability()
            self.readability = temp_model.from_map(m.get('readability'))

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ReadPageScrapeBodyReadability(DaraModel):
    def __init__(
        self,
        exclude_all_images: bool = None,
        exclude_all_links: bool = None,
        excluded_tags: List[str] = None,
        readability_mode: str = None,
    ):
        # Specifies whether to remove all images.
        # 
        # Default value: false.
        self.exclude_all_images = exclude_all_images
        # Specifies whether to remove all links.
        # 
        # Default value: false.
        self.exclude_all_links = exclude_all_links
        # The tags to exclude.
        self.excluded_tags = excluded_tags
        # The readability mode. Valid values:
        # - none: Does not remove any information. This is the default value.
        # - normal: Removes irrelevant information from the target page, such as headers, footers, and navigation elements, based on a proprietary algorithm.
        # - article: Extracts the main body content of the site based on a proprietary algorithm. This mode is suitable for blogs and news sites, but not for directory or navigation pages.
        self.readability_mode = readability_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_all_images is not None:
            result['excludeAllImages'] = self.exclude_all_images

        if self.exclude_all_links is not None:
            result['excludeAllLinks'] = self.exclude_all_links

        if self.excluded_tags is not None:
            result['excludedTags'] = self.excluded_tags

        if self.readability_mode is not None:
            result['readabilityMode'] = self.readability_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('excludeAllImages') is not None:
            self.exclude_all_images = m.get('excludeAllImages')

        if m.get('excludeAllLinks') is not None:
            self.exclude_all_links = m.get('excludeAllLinks')

        if m.get('excludedTags') is not None:
            self.excluded_tags = m.get('excludedTags')

        if m.get('readabilityMode') is not None:
            self.readability_mode = m.get('readabilityMode')

        return self

