# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UnifiedPageItem(DaraModel):
    def __init__(
        self,
        correlation_tag: int = None,
        host_authority_score: float = None,
        host_logo: str = None,
        hostname: str = None,
        images: List[str] = None,
        link: str = None,
        main_text: str = None,
        markdown_text: str = None,
        published_time: str = None,
        rerank_score: float = None,
        rich_main_body: str = None,
        snippet: str = None,
        summary: str = None,
        title: str = None,
        website_authority_score: int = None,
    ):
        self.correlation_tag = correlation_tag
        self.host_authority_score = host_authority_score
        self.host_logo = host_logo
        self.hostname = hostname
        self.images = images
        self.link = link
        self.main_text = main_text
        self.markdown_text = markdown_text
        self.published_time = published_time
        self.rerank_score = rerank_score
        self.rich_main_body = rich_main_body
        self.snippet = snippet
        self.summary = summary
        self.title = title
        self.website_authority_score = website_authority_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.correlation_tag is not None:
            result['correlationTag'] = self.correlation_tag

        if self.host_authority_score is not None:
            result['hostAuthorityScore'] = self.host_authority_score

        if self.host_logo is not None:
            result['hostLogo'] = self.host_logo

        if self.hostname is not None:
            result['hostname'] = self.hostname

        if self.images is not None:
            result['images'] = self.images

        if self.link is not None:
            result['link'] = self.link

        if self.main_text is not None:
            result['mainText'] = self.main_text

        if self.markdown_text is not None:
            result['markdownText'] = self.markdown_text

        if self.published_time is not None:
            result['publishedTime'] = self.published_time

        if self.rerank_score is not None:
            result['rerankScore'] = self.rerank_score

        if self.rich_main_body is not None:
            result['richMainBody'] = self.rich_main_body

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
        if m.get('correlationTag') is not None:
            self.correlation_tag = m.get('correlationTag')

        if m.get('hostAuthorityScore') is not None:
            self.host_authority_score = m.get('hostAuthorityScore')

        if m.get('hostLogo') is not None:
            self.host_logo = m.get('hostLogo')

        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')

        if m.get('images') is not None:
            self.images = m.get('images')

        if m.get('link') is not None:
            self.link = m.get('link')

        if m.get('mainText') is not None:
            self.main_text = m.get('mainText')

        if m.get('markdownText') is not None:
            self.markdown_text = m.get('markdownText')

        if m.get('publishedTime') is not None:
            self.published_time = m.get('publishedTime')

        if m.get('rerankScore') is not None:
            self.rerank_score = m.get('rerankScore')

        if m.get('richMainBody') is not None:
            self.rich_main_body = m.get('richMainBody')

        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('websiteAuthorityScore') is not None:
            self.website_authority_score = m.get('websiteAuthorityScore')

        return self

