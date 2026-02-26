# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InputOSS(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        match_expressions: List[str] = None,
        prefix: str = None,
    ):
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.bucket = bucket
        # The match expressions.
        self.match_expressions = match_expressions
        # The object key prefix.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.match_expressions is not None:
            result['MatchExpressions'] = self.match_expressions

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('MatchExpressions') is not None:
            self.match_expressions = m.get('MatchExpressions')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        return self

