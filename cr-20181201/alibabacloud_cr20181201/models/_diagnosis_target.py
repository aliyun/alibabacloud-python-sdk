# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class DiagnosisTarget(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        extra: Dict[str, str] = None,
        namespace: str = None,
        related_id: str = None,
        repository: str = None,
        start_time: str = None,
        tag: str = None,
    ):
        # The end time of the diagnostic.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.end_time = end_time
        # The extra parameters.
        self.extra = extra
        # The namespace name.
        self.namespace = namespace
        # The ID of the diagnosed item.
        self.related_id = related_id
        # The repository name.
        self.repository = repository
        # The start time of the diagnostic.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.start_time = start_time
        # The image tag.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.related_id is not None:
            result['RelatedId'] = self.related_id

        if self.repository is not None:
            result['Repository'] = self.repository

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')

        if m.get('Repository') is not None:
            self.repository = m.get('Repository')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

