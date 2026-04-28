# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WatermarkEnableConfig(DaraModel):
    def __init__(
        self,
        display_access_user_name: bool = None,
        display_custom_text: str = None,
        display_share_link_creator_name: bool = None,
        enable_doc_preview: bool = None,
    ):
        self.display_access_user_name = display_access_user_name
        self.display_custom_text = display_custom_text
        self.display_share_link_creator_name = display_share_link_creator_name
        self.enable_doc_preview = enable_doc_preview

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_access_user_name is not None:
            result['display_access_user_name'] = self.display_access_user_name

        if self.display_custom_text is not None:
            result['display_custom_text'] = self.display_custom_text

        if self.display_share_link_creator_name is not None:
            result['display_shareLink_creator_name'] = self.display_share_link_creator_name

        if self.enable_doc_preview is not None:
            result['enable_doc_preview'] = self.enable_doc_preview

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display_access_user_name') is not None:
            self.display_access_user_name = m.get('display_access_user_name')

        if m.get('display_custom_text') is not None:
            self.display_custom_text = m.get('display_custom_text')

        if m.get('display_shareLink_creator_name') is not None:
            self.display_share_link_creator_name = m.get('display_shareLink_creator_name')

        if m.get('enable_doc_preview') is not None:
            self.enable_doc_preview = m.get('enable_doc_preview')

        return self

