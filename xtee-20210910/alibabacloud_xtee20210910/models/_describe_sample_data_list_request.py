# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSampleDataListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        current_page: str = None,
        delete_tag: str = None,
        page_size: str = None,
        query_content: str = None,
        reg_id: str = None,
        sample_id: int = None,
        scene: str = None,
        status: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Current page number.
        self.current_page = current_page
        # Deletion status
        self.delete_tag = delete_tag
        # Page size, default value is 10.
        self.page_size = page_size
        # Query content
        self.query_content = query_content
        # Region code
        self.reg_id = reg_id
        # Sample ID.
        self.sample_id = sample_id
        # Scene
        self.scene = scene
        # Status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.delete_tag is not None:
            result['deleteTag'] = self.delete_tag

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.query_content is not None:
            result['queryContent'] = self.query_content

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.sample_id is not None:
            result['sampleId'] = self.sample_id

        if self.scene is not None:
            result['scene'] = self.scene

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('deleteTag') is not None:
            self.delete_tag = m.get('deleteTag')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('queryContent') is not None:
            self.query_content = m.get('queryContent')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sampleId') is not None:
            self.sample_id = m.get('sampleId')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

