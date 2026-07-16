# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdatePageRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        site_ids: List[int] = None,
    ):
        # The BASE64-encoded page content, which must be consistent with `ContentType`.
        # 
        # **Encoding method**:
        # 1. Convert the original page content to a UTF-8 byte string.
        # 2. Encode the byte string using standard BASE64 encoding.
        # 
        # **Example**: `<html>hello page</html>` → `PGh0bWw+aGVsbG8gcGFnZTwvaHRtbD4=`
        # 
        # > The maximum size limit is subject to the server-side custom page specification. If this parameter is not specified, the original page content is retained.
        # 
        # This parameter is required.
        self.content = content
        # The MIME type of the page content, which is returned to the client as the HTTP `Content-Type` response header when a rule is matched.
        # 
        # **Common values**:
        # - `text/html`: HTML page
        # - `application/json`: JSON response
        # 
        # > The complete set of supported values is subject to the server-side specification. The actual format of `Content` must match this field. A mismatch may cause browser rendering issues.
        # 
        # This parameter is required.
        self.content_type = content_type
        # The description of the page after the update. This is used to identify the purpose of the page in the console list. This is an optional field. If this parameter is not specified, the original description is retained. The maximum field length is subject to the server-side limit.
        # 
        # This parameter is required.
        self.description = description
        # The ID of the custom response page. You can obtain this value by calling the [ListPages](https://help.aliyun.com/document_detail/2850223.html) operation.
        # 
        # This parameter is required.
        self.id = id
        # The name of the custom response page after the update.
        # 
        # **Naming suggestion**: Use a combination of letters, digits, and underscores (such as `blocked_page_v2`) for easy reference in rules. The character set, maximum length, and uniqueness constraints are subject to the server-side naming conventions for custom pages. If this parameter is not specified, the original name is retained.
        # 
        # This parameter is required.
        self.name = name
        # The list of site IDs associated with this page after the update. This parameter uses full overwrite semantics.
        # 
        # - You can obtain site IDs by calling the `ListSites` operation.
        # - Passing an empty list dissociates all sites from the page.
        # - Including a site ID that does not belong to your account returns an `InvalidParameter` error.
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

        if self.id is not None:
            result['Id'] = self.id

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SiteIds') is not None:
            self.site_ids = m.get('SiteIds')

        return self

