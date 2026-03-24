# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainCustomLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        remark: str = None,
        request_id: str = None,
        sample: str = None,
        tag: str = None,
    ):
        # The ID of the log configuration.
        self.config_id = config_id
        # The format of the log configuration.
        self.remark = remark
        # The ID of the request.
        self.request_id = request_id
        # The sample log configuration.
        self.sample = sample
        # The tag information about the log configuration.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

