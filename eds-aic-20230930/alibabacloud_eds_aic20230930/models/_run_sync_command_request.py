# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunSyncCommandRequest(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        content_encoding: str = None,
        instance_ids: List[str] = None,
        wait_time: int = None,
    ):
        # The content of the command.
        self.command_content = command_content
        # The encoding method of the script content. If the specified value is not within the valid values, the default value `PlainText` is used.
        self.content_encoding = content_encoding
        # The list of cloud phone instance IDs. A single request supports up to 50 instances.
        self.instance_ids = instance_ids
        # The wait time in milliseconds. Valid values: 500 to 3000. Default value: 1000.
        self.wait_time = wait_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.wait_time is not None:
            result['WaitTime'] = self.wait_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')

        return self

