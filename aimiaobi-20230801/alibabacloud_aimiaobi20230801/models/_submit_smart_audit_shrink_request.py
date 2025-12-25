# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSmartAuditShrinkRequest(DaraModel):
    def __init__(
        self,
        image_url_list_shrink: str = None,
        note_id: str = None,
        sub_codes_shrink: str = None,
        terms_name: str = None,
        text: str = None,
        workspace_id: str = None,
        image_urls_shrink: str = None,
    ):
        self.image_url_list_shrink = image_url_list_shrink
        self.note_id = note_id
        self.sub_codes_shrink = sub_codes_shrink
        self.terms_name = terms_name
        self.text = text
        self.workspace_id = workspace_id
        self.image_urls_shrink = image_urls_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url_list_shrink is not None:
            result['ImageUrlList'] = self.image_url_list_shrink

        if self.note_id is not None:
            result['NoteId'] = self.note_id

        if self.sub_codes_shrink is not None:
            result['SubCodes'] = self.sub_codes_shrink

        if self.terms_name is not None:
            result['TermsName'] = self.terms_name

        if self.text is not None:
            result['Text'] = self.text

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.image_urls_shrink is not None:
            result['imageUrls'] = self.image_urls_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrlList') is not None:
            self.image_url_list_shrink = m.get('ImageUrlList')

        if m.get('NoteId') is not None:
            self.note_id = m.get('NoteId')

        if m.get('SubCodes') is not None:
            self.sub_codes_shrink = m.get('SubCodes')

        if m.get('TermsName') is not None:
            self.terms_name = m.get('TermsName')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('imageUrls') is not None:
            self.image_urls_shrink = m.get('imageUrls')

        return self

