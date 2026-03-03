# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class Metadata(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.MetadataAttachments] = None,
    ):
        self.attachments = attachments

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['Attachments'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('Attachments') is not None:
            for k1 in m.get('Attachments'):
                temp_model = main_models.MetadataAttachments()
                self.attachments.append(temp_model.from_map(k1))

        return self

class MetadataAttachments(DaraModel):
    def __init__(
        self,
        arn: str = None,
        mime_type: str = None,
    ):
        self.arn = arn
        self.mime_type = mime_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.mime_type is not None:
            result['MimeType'] = self.mime_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('MimeType') is not None:
            self.mime_type = m.get('MimeType')

        return self

