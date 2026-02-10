# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceVulStatisticsRequest(DaraModel):
    def __init__(
        self,
        types: str = None,
        uuid: str = None,
    ):
        # The vulnerability type of the serverless instance. Valid values:
        # 
        # *   **sca**: middleware vulnerabilities
        # *   **app**: application vulnerabilities detected by using a scanner
        # 
        # >  Serverless instances allow you to detect only application vulnerabilities by using a scanner.
        self.types = types
        # The UUID of the instance to query.
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUID of the instance.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.types is not None:
            result['Types'] = self.types

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Types') is not None:
            self.types = m.get('Types')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

