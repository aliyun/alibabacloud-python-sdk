# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSceneDefenseObjectsResponseBody(DaraModel):
    def __init__(
        self,
        objects: List[main_models.DescribeSceneDefenseObjectsResponseBodyObjects] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the protected assets.
        self.objects = objects
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success

    def validate(self):
        if self.objects:
            for v1 in self.objects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Objects'] = []
        if self.objects is not None:
            for k1 in self.objects:
                result['Objects'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.objects = []
        if m.get('Objects') is not None:
            for k1 in m.get('Objects'):
                temp_model = main_models.DescribeSceneDefenseObjectsResponseBodyObjects()
                self.objects.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSceneDefenseObjectsResponseBodyObjects(DaraModel):
    def __init__(
        self,
        domain: str = None,
        policy_id: str = None,
        vip: str = None,
    ):
        # The domain name that is protected by the policy.
        self.domain = domain
        # The ID of the policy.
        self.policy_id = policy_id
        # The IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance that is protected by the policy.
        self.vip = vip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.vip is not None:
            result['Vip'] = self.vip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('Vip') is not None:
            self.vip = m.get('Vip')

        return self

