# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class Content(DaraModel):
    def __init__(
        self,
        message_attachments: List[main_models.AguiMessage] = None,
        query_attachments: List[main_models.QueryAttachment] = None,
        text_attachments: List[str] = None,
    ):
        self.message_attachments = message_attachments
        self.query_attachments = query_attachments
        self.text_attachments = text_attachments

    def validate(self):
        if self.message_attachments:
            for v1 in self.message_attachments:
                 if v1:
                    v1.validate()
        if self.query_attachments:
            for v1 in self.query_attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MessageAttachments'] = []
        if self.message_attachments is not None:
            for k1 in self.message_attachments:
                result['MessageAttachments'].append(k1.to_map() if k1 else None)

        result['QueryAttachments'] = []
        if self.query_attachments is not None:
            for k1 in self.query_attachments:
                result['QueryAttachments'].append(k1.to_map() if k1 else None)

        if self.text_attachments is not None:
            result['TextAttachments'] = self.text_attachments

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_attachments = []
        if m.get('MessageAttachments') is not None:
            for k1 in m.get('MessageAttachments'):
                temp_model = main_models.AguiMessage()
                self.message_attachments.append(temp_model.from_map(k1))

        self.query_attachments = []
        if m.get('QueryAttachments') is not None:
            for k1 in m.get('QueryAttachments'):
                temp_model = main_models.QueryAttachment()
                self.query_attachments.append(temp_model.from_map(k1))

        if m.get('TextAttachments') is not None:
            self.text_attachments = m.get('TextAttachments')

        return self

