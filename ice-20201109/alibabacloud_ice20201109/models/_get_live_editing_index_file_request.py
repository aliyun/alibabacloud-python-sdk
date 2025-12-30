# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLiveEditingIndexFileRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        project_id: str = None,
        stream_name: str = None,
    ):
        # The application name of the live stream.
        self.app_name = app_name
        # The domain name of the live stream.
        self.domain_name = domain_name
        # The ID of the live stream editing project.
        self.project_id = project_id
        # The name of the live stream.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

