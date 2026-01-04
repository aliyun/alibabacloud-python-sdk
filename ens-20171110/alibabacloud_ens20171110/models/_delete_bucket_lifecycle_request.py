# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBucketLifecycleRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        rule_id: str = None,
    ):
        # The name of the bucket.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The ID of the rule. If this parameter is not specified, all rules are removed.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

