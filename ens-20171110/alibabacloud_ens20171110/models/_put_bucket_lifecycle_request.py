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
        # Specifies whether to allow overlapping prefixes. Valid values:
        # 
        # - **true**: Overlapping prefixes are allowed.
        # 
        # - **false** (default): Overlapping prefixes are not allowed.
        self.allow_same_action_overlap = allow_same_action_overlap
        # The bucket name.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The expiration date. The system performs lifecycle operations on objects that were last modified before this date.
        # 
        # The date must be specified in the ISO 8601 standard and in UTC. The format is yyyy-MM-ddTHH:mm:ssZ.
        # 
        # >ExpirationDays and CreatedBeforeDate are mutually exclusive. You must specify one of them.
        self.created_before_date = created_before_date
        # The number of days after the last modification time of an object before the lifecycle rule takes effect. The value must be a positive integer greater than 0.
        # 
        # >ExpirationDays and CreatedBeforeDate are mutually exclusive. You must specify one of them.
        self.expiration_days = expiration_days
        # The prefix to which the rule applies. You cannot specify the same prefix for multiple rules.
        # 
        # - If you specify a prefix, the rule applies only to objects whose names match the prefix in the bucket.
        # 
        # - If you leave the prefix empty, the rule applies to all objects in the bucket.
        self.prefix = prefix
        # The unique ID that identifies the rule. The ID can be up to 255 bytes in length.
        # 
        # - You do not need to specify this parameter when you create a rule. The system automatically generates a unique ID.
        # 
        # - You must specify the RuleId when you update an existing rule. The rule corresponding to the RuleId must exist. Otherwise, an error is returned.
        self.rule_id = rule_id
        # The status of the rule. Valid values:
        # 
        # - **Enabled**: The rule is executed periodically.
        # 
        # - **Disabled**: The rule is ignored.
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

