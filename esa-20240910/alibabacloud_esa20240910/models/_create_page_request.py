# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreatePageRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        name: str = None,
        site_ids: List[int] = None,
    ):
        # The BASE64-encoded page content. The actual content format must match the value of `ContentType`.
        # 
        # **Encoding method**:
        # 1. Encode the original page content into a byte string by using UTF-8 encoding.
        # 2. Apply standard BASE64 encoding to the byte string.
        # 
        # **Example**:
        # - Original content: `<html>hello page</html>`
        # - BASE64: `PGh0bWw+aGVsbG8gcGFnZTwvaHRtbD4=`
        # 
        # > The maximum size, supported character sets, and security filtering rules are subject to the server-side custom page specifications.
        self.content = content
        # The MIME type of the page content. This value is returned to the client as the HTTP `Content-Type` response header after a match.
        # 
        # **Common values**:
        # - `text/html`: HTML page. The `Content` parameter must be set to the BASE64-encoded value of UTF-8 HTML text.
        # - `application/json`: JSON response. The `Content` parameter must be set to the BASE64-encoded value of a valid JSON string.
        # - `text/plain`: plain text. The `Content` parameter must be set to the BASE64-encoded value of plain text content.
        # 
        # > Note: The complete list of supported ContentType values is subject to the server-side specifications. If the specified `ContentType` does not match the actual format of `Content`, the client may fail to render the page properly.
        # 
        # This parameter is required.
        self.content_type = content_type
        # The description of the page, used to identify the purpose of the page in the console list.
        # 
        # **Suggested content**: Use the scenarios and identity information of the page, such as "CC protection block page - Chinese version". This is an optional field. If not specified, the value is empty by default.
        # 
        # > The maximum field length is subject to the server-side specifications.
        self.description = description
        # The name of the custom page.
        # 
        # **Naming suggestions**: Use a short name that consists of letters, digits, and underscores, such as `blocked_page_v1`, for easy reference in rules. The specific character set, maximum length, uniqueness, and other constraints are **subject to the server-side custom page naming specifications**.
        # 
        # This parameter is required.
        self.name = name
        # The list of website IDs to associate with this custom page.
        # 
        # - You can obtain website IDs by calling the `ListSites` operation.
        # - If you pass an empty list (no websites are associated), the page is still created but does not take effect. You can call the `UpdatePage` operation later to associate websites.
        # - If the list contains a website ID that does not belong to the current account, an `InvalidParameter` error is returned.
        self.site_ids = site_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.site_ids is not None:
            result['SiteIds'] = self.site_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SiteIds') is not None:
            self.site_ids = m.get('SiteIds')

        return self

