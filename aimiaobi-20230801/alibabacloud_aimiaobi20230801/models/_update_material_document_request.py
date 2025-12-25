# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateMaterialDocumentRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        author: str = None,
        doc_keywords: List[str] = None,
        doc_type: str = None,
        external_url: str = None,
        html_content: str = None,
        id: int = None,
        pub_time: str = None,
        region_id: str = None,
        share_attr: int = None,
        src_from: str = None,
        summary: str = None,
        text_content: str = None,
        title: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.author = author
        self.doc_keywords = doc_keywords
        # This parameter is required.
        self.doc_type = doc_type
        self.external_url = external_url
        self.html_content = html_content
        # This parameter is required.
        self.id = id
        self.pub_time = pub_time
        self.region_id = region_id
        self.share_attr = share_attr
        self.src_from = src_from
        self.summary = summary
        self.text_content = text_content
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.author is not None:
            result['Author'] = self.author

        if self.doc_keywords is not None:
            result['DocKeywords'] = self.doc_keywords

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url

        if self.html_content is not None:
            result['HtmlContent'] = self.html_content

        if self.id is not None:
            result['Id'] = self.id

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr

        if self.src_from is not None:
            result['SrcFrom'] = self.src_from

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.text_content is not None:
            result['TextContent'] = self.text_content

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Author') is not None:
            self.author = m.get('Author')

        if m.get('DocKeywords') is not None:
            self.doc_keywords = m.get('DocKeywords')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')

        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')

        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

