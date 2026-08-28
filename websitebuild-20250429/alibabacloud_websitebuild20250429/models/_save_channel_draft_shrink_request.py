# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveChannelDraftShrinkRequest(DaraModel):
    def __init__(
        self,
        adapted_content: str = None,
        adapted_title: str = None,
        cover_images_shrink: str = None,
        draft_id: str = None,
    ):
        # The channel content (overseas only).
        self.adapted_content = adapted_content
        # The channel title.
        self.adapted_title = adapted_title
        # The collection of channel cover images (full overwrite).
        self.cover_images_shrink = cover_images_shrink
        # The ID of the channel draft.
        # 
        # This parameter is required.
        self.draft_id = draft_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adapted_content is not None:
            result['AdaptedContent'] = self.adapted_content

        if self.adapted_title is not None:
            result['AdaptedTitle'] = self.adapted_title

        if self.cover_images_shrink is not None:
            result['CoverImages'] = self.cover_images_shrink

        if self.draft_id is not None:
            result['DraftId'] = self.draft_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptedContent') is not None:
            self.adapted_content = m.get('AdaptedContent')

        if m.get('AdaptedTitle') is not None:
            self.adapted_title = m.get('AdaptedTitle')

        if m.get('CoverImages') is not None:
            self.cover_images_shrink = m.get('CoverImages')

        if m.get('DraftId') is not None:
            self.draft_id = m.get('DraftId')

        return self

