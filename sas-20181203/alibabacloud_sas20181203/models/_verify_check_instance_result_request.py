# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class VerifyCheckInstanceResultRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        check_ids: List[int] = None,
        client_token: str = None,
        instance_ids: List[str] = None,
        task_source: str = None,
    ):
        # The ID of the check item.
        # 
        # > You can call the [ListCheckResult](~~ListCheckResult~~) operation to obtain the check item ID.
        self.check_id = check_id
        # The list of check item IDs.
        self.check_ids = check_ids
        # The client token that is used to ensure the idempotence of the request. Different requests should use different tokens. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The list of instance IDs of the affected assets under the check item.
        self.instance_ids = instance_ids
        # The task source. Valid values:
        # 
        # - **YAO_CHI**: ApsaraDB console.
        self.task_source = task_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.task_source is not None:
            result['TaskSource'] = self.task_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('TaskSource') is not None:
            self.task_source = m.get('TaskSource')

        return self

