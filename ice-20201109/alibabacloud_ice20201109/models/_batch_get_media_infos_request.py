# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchGetMediaInfosRequest(DaraModel):
    def __init__(
        self,
        addition_type: str = None,
        auth_timeout: int = None,
        media_ids: str = None,
    ):
        # The types of additional media asset information to return. If this parameter is not specified, only basic information is returned. Valid values are:
        # 
        # -FileInfo
        # 
        # -DynamicMetaData
        self.addition_type = addition_type
        # The authentication timeout, in seconds.
        # 
        # - Minimum value: **1**.
        # 
        # - Maximum value: 86400.
        # 
        # - Default value: 3600.
        self.auth_timeout = auth_timeout
        # A comma-separated list of media asset IDs to query.
        self.media_ids = media_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type

        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')

        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        return self

