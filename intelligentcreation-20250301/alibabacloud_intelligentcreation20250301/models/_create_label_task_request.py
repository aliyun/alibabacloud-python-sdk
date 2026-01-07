# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel



class CreateLabelTaskRequest(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        file_url: str = None,
        idempotent_id: str = None,
        label_template_id: str = None,
        project_id: int = None,
    ):
        self.callback_url = callback_url
        # This parameter is required.
        self.file_url = file_url
        self.idempotent_id = idempotent_id
        # This parameter is required.
        self.label_template_id = label_template_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.idempotent_id is not None:
            result['IdempotentId'] = self.idempotent_id

        if self.label_template_id is not None:
            result['LabelTemplateId'] = self.label_template_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('IdempotentId') is not None:
            self.idempotent_id = m.get('IdempotentId')

        if m.get('LabelTemplateId') is not None:
            self.label_template_id = m.get('LabelTemplateId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

