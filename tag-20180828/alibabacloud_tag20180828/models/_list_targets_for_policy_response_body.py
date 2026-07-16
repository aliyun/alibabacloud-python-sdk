# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class ListTargetsForPolicyResponseBody(DaraModel):
    def __init__(
        self,
        is_rd: bool = None,
        next_token: str = None,
        rd_id: str = None,
        request_id: str = None,
        targets: List[main_models.ListTargetsForPolicyResponseBodyTargets] = None,
    ):
        # Indicates whether the object belongs to the resource directory. Valid values:
        # 
        # *   true: The object belongs to the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   false: The object does not belong to the resource directory. This value is available if you use the Tag Policy feature in single-account mode.
        self.is_rd = is_rd
        # Indicates whether the next query is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token
        # The ID of the resource directory.
        # 
        # >  This parameter is returned only if you use the Tag Policy feature in multi-account mode.
        self.rd_id = rd_id
        # The ID of the request.
        self.request_id = request_id
        # The objects to which the tag policy is attached.
        self.targets = targets

    def validate(self):
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_rd is not None:
            result['IsRd'] = self.is_rd

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.rd_id is not None:
            result['RdId'] = self.rd_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsRd') is not None:
            self.is_rd = m.get('IsRd')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RdId') is not None:
            self.rd_id = m.get('RdId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.ListTargetsForPolicyResponseBodyTargets()
                self.targets.append(temp_model.from_map(k1))

        return self

class ListTargetsForPolicyResponseBodyTargets(DaraModel):
    def __init__(
        self,
        target_id: str = None,
        target_type: int = None,
    ):
        # The ID of the object.
        self.target_id = target_id
        # The type of the object. Valid values:
        # 
        # *   USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # *   ROOT: the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   FOLDER: a folder other than the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # *   ACCOUNT: a member in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

