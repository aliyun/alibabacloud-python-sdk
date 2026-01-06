# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrialLabel(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        key: str = None,
        trial_id: str = None,
        value: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.key = key
        self.trial_id = trial_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.key is not None:
            result['Key'] = self.key

        if self.trial_id is not None:
            result['TrialId'] = self.trial_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('TrialId') is not None:
            self.trial_id = m.get('TrialId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

