# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CheckPolarClawSkillResponseBody(DaraModel):
    def __init__(
        self,
        message: List[str] = None,
        ossbucket: str = None,
        ossregion_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned message.
        self.message = message
        # The name of the OSS bucket where the skill files are stored.
        self.ossbucket = ossbucket
        # The region ID of the OSS bucket where the skill files are stored.
        self.ossregion_id = ossregion_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **true**: The request is successful.
        # 
        # - **false**: The request fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.ossregion_id is not None:
            result['OSSRegionId'] = self.ossregion_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('OSSRegionId') is not None:
            self.ossregion_id = m.get('OSSRegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

