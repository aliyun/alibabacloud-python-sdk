# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCacheTagRequest(DaraModel):
    def __init__(
        self,
        case_insensitive: str = None,
        site_id: int = None,
        site_version: int = None,
        tag_name: str = None,
    ):
        # Specifies whether to ignore case sensitivity. Valid values:
        # 
        # *   on
        # *   off
        self.case_insensitive = case_insensitive
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the website configurations. You can use this parameter to specify a version of your website to apply the feature settings. By default, version 0 is used.
        self.site_version = site_version
        # The name of the custom cache tag.
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

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaseInsensitive') is not None:
            self.case_insensitive = m.get('CaseInsensitive')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

