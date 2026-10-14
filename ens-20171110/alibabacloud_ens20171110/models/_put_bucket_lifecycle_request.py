# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutBucketLifecycleRequest(DaraModel):
    def __init__(
        self,
        allow_same_action_overlap: bool = None,
        bucket_name: str = None,
        created_before_date: str = None,
        expiration_days: int = None,
        prefix: str = None,
        rule_id: str = None,
        status: str = None,
    ):
        # Whether to allow overlapping prefixes. Valid values:
        # 
        # - **true**: Overlapping prefixes are allowed.
        # 
        # - **false** (default): Overlapping prefixes are not allowed.
        self.allow_same_action_overlap = allow_same_action_overlap
        # The name of the bucket.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The date before which objects expire. The system applies the lifecycle rule to objects last modified before this date.
        # 
        # Use ISO 8601 format and UTC time. Format: yyyy-MM-ddTHH:mm:ssZ.
        # 
        # > ExpirationDays and CreatedBeforeDate are mutually exclusive. Specify one.
        self.created_before_date = created_before_date
        # The number of days after an object\\"s last modification when the lifecycle rule takes effect. Must be a positive integer greater than zero.
        # 
        # > ExpirationDays and CreatedBeforeDate are mutually exclusive. Specify one.
        self.expiration_days = expiration_days
        # The prefix that the rule applies to. You cannot set duplicate prefixes.
        # 
        # - If you specify a prefix, the rule applies only to objects in the bucket whose names start with that prefix.
        # 
        # - If you leave Prefix empty, the rule applies to all objects in the bucket.
        self.prefix = prefix
        # A unique ID that identifies the rule. Maximum length is 255 bytes.
        # 
        # - Omit this parameter when creating a new rule. The system generates a unique ID automatically.
        # 
        # - Specify RuleId when updating an existing rule. The rule must exist. Otherwise, the call fails.
        self.rule_id = rule_id
        # The status of the rule. Valid values:
        # 
        # - **Enabled**: The system runs the rule on schedule.
        # 
        # - **Disabled**: The system ignores the rule.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_same_action_overlap is not None:
            result['AllowSameActionOverlap'] = self.allow_same_action_overlap

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.created_before_date is not None:
            result['CreatedBeforeDate'] = self.created_before_date

        if self.expiration_days is not None:
            result['ExpirationDays'] = self.expiration_days

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowSameActionOverlap') is not None:
            self.allow_same_action_overlap = m.get('AllowSameActionOverlap')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('CreatedBeforeDate') is not None:
            self.created_before_date = m.get('CreatedBeforeDate')

        if m.get('ExpirationDays') is not None:
            self.expiration_days = m.get('ExpirationDays')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

