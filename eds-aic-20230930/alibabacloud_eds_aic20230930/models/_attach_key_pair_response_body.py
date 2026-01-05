# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class AttachKeyPairResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.AttachKeyPairResponseBodyData = None,
        request_id: str = None,
    ):
        # The object that is returned.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.AttachKeyPairResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class AttachKeyPairResponseBodyData(DaraModel):
    def __init__(
        self,
        attached_instance_ids: List[str] = None,
        fail_count: int = None,
        key_pair_id: str = None,
        total_count: int = None,
    ):
        # The IDs of the cloud phone instances to which the ADB key pair is successfully attached.
        self.attached_instance_ids = attached_instance_ids
        # The number of the cloud phone instances to which the ADB key pair failed to be attached.
        self.fail_count = fail_count
        # The ID of the ADB key pair.
        self.key_pair_id = key_pair_id
        # The total number of the cloud phone instances.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_instance_ids is not None:
            result['AttachedInstanceIds'] = self.attached_instance_ids

        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedInstanceIds') is not None:
            self.attached_instance_ids = m.get('AttachedInstanceIds')

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

