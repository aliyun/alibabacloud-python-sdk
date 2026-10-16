# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCodeBundleRequest(DaraModel):
    def __init__(
        self,
        ci_metadata: str = None,
        filename: str = None,
    ):
        # An optional CI/CD metadata JSON string.
        self.ci_metadata = ci_metadata
        # The file name.
        # 
        # This parameter is required.
        self.filename = filename

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ci_metadata is not None:
            result['ciMetadata'] = self.ci_metadata

        if self.filename is not None:
            result['filename'] = self.filename

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ciMetadata') is not None:
            self.ci_metadata = m.get('ciMetadata')

        if m.get('filename') is not None:
            self.filename = m.get('filename')

        return self

