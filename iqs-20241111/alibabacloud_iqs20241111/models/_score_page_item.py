# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class ScorePageItem(DaraModel):
    def __init__(
        self,
        card_type: str = None,
        correlation_tag: int = None,
        display_link: str = None,
        host_authority_score: float = None,
        host_logo: str = None,
        hostname: str = None,
        html_snippet: str = None,
        html_title: str = None,
        images: List[main_models.IncludeImage] = None,
        link: str = None,
        main_text: str = None,
        markdown_text: str = None,
        mime: str = None,
        page_map: Dict[str, str] = None,
        publish_time: int = None,
        rich_main_body: str = None,
        score: float = None,
        site_label: str = None,
        snippet: str = None,
        summary: str = None,
        title: str = None,
        website_authority_score: int = None,
    ):
        # This parameter is required.
        self.card_type = card_type
        self.correlation_tag = correlation_tag
        # This parameter is required.
        self.display_link = display_link
        self.host_authority_score = host_authority_score
        self.host_logo = host_logo
        self.hostname = hostname
        # This parameter is required.
        self.html_snippet = html_snippet
        # This parameter is required.
        self.html_title = html_title
        self.images = images
        # This parameter is required.
        self.link = link
        self.main_text = main_text
        self.markdown_text = markdown_text
        self.mime = mime
        self.page_map = page_map
        # This parameter is required.
        self.publish_time = publish_time
        self.rich_main_body = rich_main_body
        self.score = score
        self.site_label = site_label
        self.snippet = snippet
        self.summary = summary
        # This parameter is required.
        self.title = title
        self.website_authority_score = website_authority_score

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_type is not None:
            result['cardType'] = self.card_type

        if self.correlation_tag is not None:
            result['correlationTag'] = self.correlation_tag

        if self.display_link is not None:
            result['displayLink'] = self.display_link

        if self.host_authority_score is not None:
            result['hostAuthorityScore'] = self.host_authority_score

        if self.host_logo is not None:
            result['hostLogo'] = self.host_logo

        if self.hostname is not None:
            result['hostname'] = self.hostname

        if self.html_snippet is not None:
            result['htmlSnippet'] = self.html_snippet

        if self.html_title is not None:
            result['htmlTitle'] = self.html_title

        result['images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['images'].append(k1.to_map() if k1 else None)

        if self.link is not None:
            result['link'] = self.link

        if self.main_text is not None:
            result['mainText'] = self.main_text

        if self.markdown_text is not None:
            result['markdownText'] = self.markdown_text

        if self.mime is not None:
            result['mime'] = self.mime

        if self.page_map is not None:
            result['pageMap'] = self.page_map

        if self.publish_time is not None:
            result['publishTime'] = self.publish_time

        if self.rich_main_body is not None:
            result['richMainBody'] = self.rich_main_body

        if self.score is not None:
            result['score'] = self.score

        if self.site_label is not None:
            result['siteLabel'] = self.site_label

        if self.snippet is not None:
            result['snippet'] = self.snippet

        if self.summary is not None:
            result['summary'] = self.summary

        if self.title is not None:
            result['title'] = self.title

        if self.website_authority_score is not None:
            result['websiteAuthorityScore'] = self.website_authority_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardType') is not None:
            self.card_type = m.get('cardType')

        if m.get('correlationTag') is not None:
            self.correlation_tag = m.get('correlationTag')

        if m.get('displayLink') is not None:
            self.display_link = m.get('displayLink')

        if m.get('hostAuthorityScore') is not None:
            self.host_authority_score = m.get('hostAuthorityScore')

        if m.get('hostLogo') is not None:
            self.host_logo = m.get('hostLogo')

        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')

        if m.get('htmlSnippet') is not None:
            self.html_snippet = m.get('htmlSnippet')

        if m.get('htmlTitle') is not None:
            self.html_title = m.get('htmlTitle')

        self.images = []
        if m.get('images') is not None:
            for k1 in m.get('images'):
                temp_model = main_models.IncludeImage()
                self.images.append(temp_model.from_map(k1))

        if m.get('link') is not None:
            self.link = m.get('link')

        if m.get('mainText') is not None:
            self.main_text = m.get('mainText')

        if m.get('markdownText') is not None:
            self.markdown_text = m.get('markdownText')

        if m.get('mime') is not None:
            self.mime = m.get('mime')

        if m.get('pageMap') is not None:
            self.page_map = m.get('pageMap')

        if m.get('publishTime') is not None:
            self.publish_time = m.get('publishTime')

        if m.get('richMainBody') is not None:
            self.rich_main_body = m.get('richMainBody')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('siteLabel') is not None:
            self.site_label = m.get('siteLabel')

        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('websiteAuthorityScore') is not None:
            self.website_authority_score = m.get('websiteAuthorityScore')

        return self

